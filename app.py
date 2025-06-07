"""
Professional AI TTS Web Application
Supports Sinhala & English with Multiple Voices and Advanced Features
"""

import os
import io
import asyncio
import json
import base64
import mimetypes
import struct
from datetime import datetime
from typing import Dict, List, Optional, Union
from pathlib import Path

# Web Framework
from flask import Flask, render_template, request, jsonify, send_file, session
from flask_cors import CORS
from werkzeug.utils import secure_filename

# AI/TTS Libraries
from google import genai
from google.genai import types
import edge_tts
import pyttsx3

# Audio Processing
import librosa
import soundfile as sf
import numpy as np
from pydub import AudioSegment
from pydub.effects import normalize, compress_dynamic_range

# Utilities
import asyncio
import threading
import queue
import logging
from functools import wraps

# Configuration
class TTSConfig:
    """TTS Application Configuration"""
    
    # API Keys
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
    
    # Supported Languages
    LANGUAGES = {
        'si-LK': 'Sinhala (Sri Lanka)',
        'en-US': 'English (US)',
        'en-GB': 'English (UK)',
        'en-AU': 'English (Australia)',
        'ta-IN': 'Tamil (India)',
        'hi-IN': 'Hindi (India)'
    }
    
    # Voice Profiles
    VOICE_PROFILES = {
        'gemini': {
            'Zephyr': {'gender': 'neutral', 'style': 'warm'},
            'Puck': {'gender': 'neutral', 'style': 'friendly'},
            'Aoede': {'gender': 'female', 'style': 'professional'},
            'Charon': {'gender': 'male', 'style': 'authoritative'},
            'Fenrir': {'gender': 'male', 'style': 'deep'},
            'Kore': {'gender': 'female', 'style': 'gentle'}
        },
        'edge': {
            'si-LK-ThiliniNeural': {'gender': 'female', 'language': 'si-LK'},
            'en-US-AriaNeural': {'gender': 'female', 'language': 'en-US'},
            'en-US-GuyNeural': {'gender': 'male', 'language': 'en-US'},
            'en-GB-SoniaNeural': {'gender': 'female', 'language': 'en-GB'},
            'en-AU-NatashaNeural': {'gender': 'female', 'language': 'en-AU'}
        }
    }
    
    # Audio Settings
    AUDIO_FORMATS = ['wav', 'mp3', 'ogg', 'flac']
    SAMPLE_RATES = [16000, 22050, 24000, 44100, 48000]
    
    # File Storage
    UPLOAD_FOLDER = 'uploads'
    OUTPUT_FOLDER = 'outputs'
    MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Initialize Flask App
app = Flask(__name__, template_folder='.')
app.secret_key = os.urandom(24)
CORS(app)

# Setup directories
for folder in [TTSConfig.UPLOAD_FOLDER, TTSConfig.OUTPUT_FOLDER]:
    Path(folder).mkdir(exist_ok=True)

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('tts_app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class AudioProcessor:
    """Advanced Audio Processing Class"""
    
    @staticmethod
    def enhance_audio(audio_data: bytes, enhancement_type: str = 'basic') -> bytes:
        """Apply audio enhancements"""
        try:
            # Convert bytes to AudioSegment
            audio = AudioSegment.from_wav(io.BytesIO(audio_data))
            
            if enhancement_type == 'normalize':
                audio = normalize(audio)
            elif enhancement_type == 'compress':
                audio = compress_dynamic_range(audio)
            elif enhancement_type == 'boost':
                audio = audio + 3  # Increase volume by 3dB
            
            # Convert back to bytes
            output_buffer = io.BytesIO()
            audio.export(output_buffer, format="wav")
            return output_buffer.getvalue()
            
        except Exception as e:
            logger.error(f"Audio enhancement failed: {e}")
            return audio_data
    
    @staticmethod
    def convert_format(audio_data: bytes, target_format: str) -> bytes:
        """Convert audio to different format"""
        try:
            audio = AudioSegment.from_wav(io.BytesIO(audio_data))
            output_buffer = io.BytesIO()
            audio.export(output_buffer, format=target_format)
            return output_buffer.getvalue()
        except Exception as e:
            logger.error(f"Format conversion failed: {e}")
            return audio_data

class GeminiTTSEngine:
    """Advanced Gemini TTS Engine"""
    
    def __init__(self):
        if not TTSConfig.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        self.client = genai.Client(api_key=TTSConfig.GEMINI_API_KEY)
        self.model = "gemini-2.5-flash-preview-tts"
    
    def generate_speech(self, 
                       text: str, 
                       voice: str = "Zephyr",
                       temperature: float = 1.0,
                       multi_speaker: bool = False,
                       speaker_configs: Optional[List[Dict]] = None) -> bytes:
        """Generate speech with advanced options"""
        
        try:
            contents = [
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=text)]
                )
            ]
            
            # Configure speech settings
            if multi_speaker and speaker_configs:
                speech_config = types.SpeechConfig(
                    multi_speaker_voice_config=types.MultiSpeakerVoiceConfig(
                        speaker_voice_configs=[
                            types.SpeakerVoiceConfig(
                                speaker=config['speaker'],
                                voice_config=types.VoiceConfig(
                                    prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                        voice_name=config['voice']
                                    )
                                )
                            ) for config in speaker_configs
                        ]
                    )
                )
            else:
                speech_config = types.SpeechConfig(
                    voice_config=types.VoiceConfig(
                        prebuilt_voice_config=types.PrebuiltVoiceConfig(
                            voice_name=voice
                        )
                    )
                )
            
            generate_config = types.GenerateContentConfig(
                temperature=temperature,
                response_modalities=["audio"],
                speech_config=speech_config
            )
            
            # Generate and collect audio data
            audio_chunks = []
            for chunk in self.client.models.generate_content_stream(
                model=self.model,
                contents=contents,
                config=generate_config
            ):
                if (chunk.candidates and 
                    chunk.candidates[0].content and 
                    chunk.candidates[0].content.parts):
                    
                    part = chunk.candidates[0].content.parts[0]
                    if part.inline_data and part.inline_data.data:
                        audio_chunks.append(part.inline_data.data)
            
            if audio_chunks:
                # Combine all audio chunks
                combined_audio = b''.join(audio_chunks)
                return self._convert_to_wav(combined_audio)
            
            raise Exception("No audio data generated")
            
        except Exception as e:
            logger.error(f"Gemini TTS generation failed: {e}")
            raise
    
    def _convert_to_wav(self, audio_data: bytes, mime_type: str = "audio/L16;rate=24000") -> bytes:
        """Convert audio data to WAV format with proper header"""
        
        parameters = self._parse_audio_mime_type(mime_type)
        bits_per_sample = parameters["bits_per_sample"]
        sample_rate = parameters["rate"]
        num_channels = 1
        data_size = len(audio_data)
        bytes_per_sample = bits_per_sample // 8
        block_align = num_channels * bytes_per_sample
        byte_rate = sample_rate * block_align
        chunk_size = 36 + data_size
        
        header = struct.pack(
            "<4sI4s4sIHHIIHH4sI",
            b"RIFF", chunk_size, b"WAVE", b"fmt ", 16, 1,
            num_channels, sample_rate, byte_rate, block_align,
            bits_per_sample, b"data", data_size
        )
        
        return header + audio_data
    
    def _parse_audio_mime_type(self, mime_type: str) -> Dict[str, int]:
        """Parse audio MIME type for parameters"""
        bits_per_sample = 16
        rate = 24000
        
        parts = mime_type.split(";")
        for param in parts:
            param = param.strip()
            if param.lower().startswith("rate="):
                try:
                    rate = int(param.split("=", 1)[1])
                except (ValueError, IndexError):
                    pass
            elif param.startswith("audio/L"):
                try:
                    bits_per_sample = int(param.split("L", 1)[1])
                except (ValueError, IndexError):
                    pass
        
        return {"bits_per_sample": bits_per_sample, "rate": rate}

class EdgeTTSEngine:
    """Edge TTS Engine for multiple language support"""
    
    @staticmethod
    async def generate_speech(text: str, voice: str, rate: str = "+0%", pitch: str = "+0Hz") -> bytes:
        """Generate speech using Edge TTS"""
        try:
            communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
            audio_data = b""
            async for chunk in communicate.stream():
                if chunk["type"] == "audio":
                    audio_data += chunk["data"]
            return audio_data
        except Exception as e:
            logger.error(f"Edge TTS generation failed: {e}")
            raise

class TTSManager:
    """Main TTS Management Class"""
    
    def __init__(self):
        self.gemini_engine = None
        self.initialize_engines()
    
    def initialize_engines(self):
        """Initialize TTS engines"""
        try:
            if TTSConfig.GEMINI_API_KEY:
                self.gemini_engine = GeminiTTSEngine()
                logger.info("Gemini TTS engine initialized")
        except Exception as e:
            logger.warning(f"Failed to initialize Gemini TTS: {e}")
    
    async def generate_tts(self, 
                          text: str, 
                          engine: str = "gemini",
                          voice: str = "Zephyr",
                          language: str = "en-US",
                          **kwargs) -> Dict:
        """Generate TTS audio with specified parameters"""
        
        try:
            if engine == "gemini" and self.gemini_engine:
                audio_data = self.gemini_engine.generate_speech(
                    text=text,
                    voice=voice,
                    temperature=kwargs.get('temperature', 1.0),
                    multi_speaker=kwargs.get('multi_speaker', False),
                    speaker_configs=kwargs.get('speaker_configs')
                )
            
            elif engine == "edge":
                audio_data = await EdgeTTSEngine.generate_speech(
                    text=text,
                    voice=voice,
                    rate=kwargs.get('rate', '+0%'),
                    pitch=kwargs.get('pitch', '+0Hz')
                )
            
            else:
                raise ValueError(f"Unsupported engine: {engine}")
            
            # Apply audio enhancements if requested
            if kwargs.get('enhance'):
                audio_data = AudioProcessor.enhance_audio(
                    audio_data, 
                    kwargs.get('enhancement_type', 'basic')
                )
            
            # Convert format if needed
            output_format = kwargs.get('format', 'wav')
            if output_format != 'wav':
                audio_data = AudioProcessor.convert_format(audio_data, output_format)
            
            # Save file
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tts_output_{timestamp}.{output_format}"
            filepath = os.path.join(TTSConfig.OUTPUT_FOLDER, filename)
            
            with open(filepath, 'wb') as f:
                f.write(audio_data)
            
            return {
                'success': True,
                'filename': filename,
                'filepath': filepath,
                'size': len(audio_data),
                'duration': self._estimate_duration(len(audio_data)),
                'format': output_format
            }
            
        except Exception as e:
            logger.error(f"TTS generation failed: {e}")
            return {
                'success': False,
                'error': str(e)
            }
    
    def _estimate_duration(self, data_size: int, sample_rate: int = 24000, channels: int = 1, bits: int = 16) -> float:
        """Estimate audio duration in seconds"""
        bytes_per_sample = bits // 8
        total_samples = data_size // (channels * bytes_per_sample)
        return total_samples / sample_rate

# Initialize TTS Manager
tts_manager = TTSManager()

# Flask Routes
@app.route('/')
def index():
    """Main application page"""
    return render_template('index.html',
                         languages=TTSConfig.LANGUAGES,
                         voices=TTSConfig.VOICE_PROFILES,
                         formats=TTSConfig.AUDIO_FORMATS)

@app.route('/api/generate', methods=['POST'])
async def generate_tts_api():
    """API endpoint for TTS generation"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('text'):
            return jsonify({'error': 'Text is required'}), 400
        
        # Generate TTS
        result = await tts_manager.generate_tts(
            text=data['text'],
            engine=data.get('engine', 'gemini'),
            voice=data.get('voice', 'Zephyr'),
            language=data.get('language', 'en-US'),
            temperature=data.get('temperature', 1.0),
            rate=data.get('rate', '+0%'),
            pitch=data.get('pitch', '+0Hz'),
            enhance=data.get('enhance', False),
            enhancement_type=data.get('enhancement_type', 'basic'),
            format=data.get('format', 'wav'),
            multi_speaker=data.get('multi_speaker', False),
            speaker_configs=data.get('speaker_configs')
        )
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"API generation error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/voices/<engine>')
def get_voices(engine):
    """Get available voices for specific engine"""
    if engine in TTSConfig.VOICE_PROFILES:
        return jsonify(TTSConfig.VOICE_PROFILES[engine])
    return jsonify({'error': 'Engine not found'}), 404

@app.route('/api/download/<filename>')
def download_file(filename):
    """Download generated audio file"""
    try:
        filepath = os.path.join(TTSConfig.OUTPUT_FOLDER, secure_filename(filename))
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/batch', methods=['POST'])
async def batch_generate():
    """Batch TTS generation endpoint"""
    try:
        data = request.get_json()
        texts = data.get('texts', [])
        config = data.get('config', {})
        
        results = []
        for i, text in enumerate(texts):
            result = await tts_manager.generate_tts(
                text=text,
                **config
            )
            result['index'] = i
            results.append(result)
        
        return jsonify({
            'success': True,
            'results': results,
            'total': len(texts),
            'successful': sum(1 for r in results if r['success'])
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.errorhandler(Exception)
def handle_error(e):
    """Global error handler"""
    logger.error(f"Unhandled error: {e}")
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    print("🎤 Professional AI TTS Web Application")
    print("=" * 50)
    print("✅ Sinhala & English Support")
    print("✅ Multiple Voice Engines")
    print("✅ Advanced Audio Processing")
    print("✅ Batch Processing")
    print("✅ Multi-format Export")
    print("=" * 50)
    print("🌐 Starting server...")
    
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=True,
        threaded=True
    )
