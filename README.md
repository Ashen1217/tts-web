# ✨ AI TTS Pro - Enhanced Edition ✨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)](https://ai.google.dev/)
[![Edge TTS](https://img.shields.io/badge/AI-Edge%20TTS-blueviolet.svg)](https://github.com/rany2/edge-tts)
[![Render Ready](https://img.shields.io/badge/Deploy-Render.com-46E3B7.svg)](https://render.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)](https://www.docker.com/)
[![Status](https://img.shields.io/badge/status-production--ready-success.svg)]()

---

**AI TTS Pro Enhanced Edition** is a cutting-edge, professional Text-to-Speech web application featuring **30+ premium Gemini voices** and advanced AI capabilities. Built for production deployment with comprehensive multilingual support including **Sinhala**, **English**, and 15+ other languages.

<p align="center">
  <a href="https://i.ibb.co/d44pHrpV/Screenshot-2025-06-07-203730.png" target="_blank">
    <img src="https://i.ibb.co/d44pHrpV/Screenshot-2025-06-07-203730.png" alt="AI TTS Pro Enhanced" style="max-width: 100%; height: auto; border-radius: 10px;" />
  </a>
</p>

---

## 🚀 New Features in Enhanced Edition

### 🌟 **30+ Premium Gemini Voices**
- **Core Collection**: Zephyr, Puck, Aoede, Charon, Fenrir, Kore
- **Mythological Series**: Leda, Enceladus, Iapetus, Callirrhoe, Autonoe
- **Stellar Collection**: Algieba, Despina, Erinome, Algenib, Rasalgethi, Laomedeia
- **Constellation Voices**: Achernar, Alnilam, Schedar, Gacrux, Pulcherrima, Achird
- **Zodiacal Series**: Zubenelgenubi, Vindemiatrix, Sadachbia, Sadaltager, Sulafat

### 📱 **Fully Responsive Help System**
- Mobile-optimized modal design
- Touch-friendly navigation
- Comprehensive feature documentation
- Interactive voice categorization

### 🔧 **Enhanced Technical Features**
- Advanced error handling and validation
- Real-time statistics and monitoring
- Production-ready deployment configurations
- Docker containerization support
- Render.com auto-deployment
- Enhanced security measures

---

## 🌐 Multi-Language Support

### **Fully Supported Languages:**
- 🇱🇰 **Sinhala (si-LK)** - Native Unicode support
- 🇺🇸 **English (US)** - Premium voice collection
- 🇬🇧 **English (UK)** - British accent support
- 🇦🇺 **English (Australia)** - Australian accent
- 🇮🇳 **Tamil (ta-IN)** - South Indian language
- 🇮🇳 **Hindi (hi-IN)** - Devanagari script support
- 🇹🇭 **Thai (th-TH)** - Southeast Asian support
- 🇻🇳 **Vietnamese (vi-VN)** - Tone language support
- 🇰🇷 **Korean (ko-KR)** - Hangul script support
- 🇯🇵 **Japanese (ja-JP)** - Hiragana/Katakana support
- 🇫🇷 **French (fr-FR)** - Romance language support
- 🇩🇪 **German (de-DE)** - Germanic language support
- 🇪🇸 **Spanish (es-ES)** - Iberian Spanish
- 🇮🇹 **Italian (it-IT)** - Romance language support
- 🇧🇷 **Portuguese (pt-BR)** - Brazilian Portuguese

---

## 🎭 Voice Engine Comparison

### 🤖 **Gemini AI (Premium)**
| Feature | Capability |
|---------|------------|
| **Voice Count** | 30+ premium voices |
| **Quality** | Ultra-high fidelity |
| **Expressiveness** | Advanced emotional control |
| **Multi-speaker** | ✅ Supported |
| **Languages** | 24+ languages |
| **Use Case** | Professional, broadcasting, content creation |

### 🌐 **Edge TTS (Standard)**
| Feature | Capability |
|---------|------------|
| **Voice Count** | 13+ regional voices |
| **Quality** | High-quality synthesis |
| **Speed** | Fast generation |
| **Multilingual** | ✅ Excellent support |
| **Regional Accents** | ✅ Native pronunciation |
| **Use Case** | General purpose, everyday use |

---

## 🛠️ Technical Specifications

### **Core Technologies**
- **Backend**: Python 3.8+, Flask 2.3.3, Gunicorn
- **Frontend**: HTML5, Tailwind CSS 2.2.19, Vanilla JavaScript
- **AI Engines**: Google Gemini 2.5, Microsoft Edge TTS
- **Audio Processing**: librosa, pydub, numpy, soundfile
- **Deployment**: Docker, Render.com, Nginx, systemd

### **Audio Capabilities**
- **Input**: Text (up to 5,000 characters)
- **Output Formats**: WAV, MP3, OGG, FLAC
- **Sample Rates**: 16kHz, 22kHz, 24kHz, 44.1kHz, 48kHz
- **Enhancement**: Normalization, compression, volume boost
- **Quality Options**: Standard, High, Premium

### **Performance Features**
- **Rate Limiting**: 30 requests/minute, 500/hour
- **Batch Processing**: Up to 10 texts simultaneously
- **Caching**: Intelligent response caching
- **Auto-scaling**: Dynamic resource allocation
- **Health Monitoring**: Real-time status checks

---

## 📦 Quick Start Guide

### **1. Clone Repository**
```bash
git clone https://github.com/chamika1/tts-web.git
cd ai-tts-pro
```

### **2. Environment Setup**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt
```

### **3. Configuration**
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your API keys
nano .env
```

**Required Environment Variables:**
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
SECRET_KEY=your_super_secret_key_here
FLASK_ENV=production
LOG_LEVEL=INFO
```

### **4. Run Application**
```bash
# Development mode
python app.py

# Production mode with Gunicorn
gunicorn --bind 0.0.0.0:5001 --workers 3 app:app
```

**Application will be available at:** `http://localhost:5001`

---

## 🐳 Docker Deployment

### **Quick Docker Setup**
```bash
# Build production image
docker build --target production -t ai-tts-pro:latest .

# Run container
docker run -d \
  --name ai-tts-pro \
  -p 5001:5001 \
  -e GEMINI_API_KEY=your_api_key \
  -e SECRET_KEY=your_secret_key \
  -v $(pwd)/outputs:/app/outputs \
  --restart unless-stopped \
  ai-tts-pro:latest
```

### **Docker Compose**
```yaml
version: '3.8'
services:
  tts-app:
    build: .
    target: production
    ports:
      - "5001:5001"
    environment:
      - GEMINI_API_KEY=your_api_key_here
      - SECRET_KEY=your_secret_key_here
    volumes:
      - ./outputs:/app/outputs
      - ./uploads:/app/uploads
    restart: unless-stopped
```

---

## ☁️ Render.com Deployment

### **One-Click Deployment**
1. **Fork this repository** to your GitHub account
2. **Connect to Render.com** and create new Web Service
3. **Point to your repository** - Render will auto-detect `render.yaml`
4. **Set Environment Variables** in Render dashboard:
   - `GEMINI_API_KEY`: Your Google Gemini API key
5. **Deploy!** - Automatic deployment with HTTPS

### **Manual Render Setup**
```yaml
# render.yaml is included for automatic configuration
# Supports:
# ✅ Auto-scaling (1-5 instances)
# ✅ Health checks
# ✅ Persistent storage
# ✅ Environment management
# ✅ HTTPS/SSL certificates
# ✅ Custom domains
```

**Estimated Cost**: $7-10/month on Render.com

---

## 🔧 Advanced Configuration

### **Voice Selection Examples**
```python
# Gemini Premium Voices
voices = {
    'Zephyr': 'Warm & neutral for narration',
    'Aoede': 'Professional female for business',
    'Charon': 'Authoritative male for announcements',
    'Pulcherrima': 'Beautiful feminine for content',
    'Achernar': 'Swift & dynamic for presentations'
}
```

### **API Usage Examples**
```javascript
// Generate speech with custom settings
const response = await fetch('/api/generate', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        text: 'ආයුබෝවන්! Welcome to AI TTS Pro!',
        engine: 'gemini',
        voice: 'Zephyr',
        language: 'si-LK',
        temperature: 1.2,
        enhance: true,
        format: 'wav'
    })
});
```

### **Batch Processing**
```javascript
// Process multiple texts
const batchResponse = await fetch('/api/batch', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
        texts: [
            'Hello world!',
            'ආයුබෝවන් ලෝකයට!',
            'Welcome to the future!'
        ],
        config: {
            engine: 'gemini',
            voice: 'Puck',
            format: 'mp3'
        }
    })
});
```

---

## 📊 API Reference

### **Endpoints**

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Main application interface |
| `POST` | `/api/generate` | Generate TTS audio |
| `GET` | `/api/voices/{engine}` | List available voices |
| `GET` | `/api/download/{filename}` | Download generated audio |
| `POST` | `/api/batch` | Batch text processing |
| `GET` | `/api/statistics` | Application statistics |
| `GET` | `/api/health` | Health check endpoint |

### **Request/Response Examples**

**Generate TTS:**
```json
POST /api/generate
{
    "text": "Your text here",
    "engine": "gemini",
    "voice": "Zephyr",
    "language": "en-US",
    "temperature": 1.0,
    "rate": "+0%",
    "pitch": "+0Hz",
    "enhance": true,
    "format": "wav"
}

Response:
{
    "success": true,
    "filename": "tts_gemini_zephyr_20250610_143022.wav",
    "size": 245760,
    "duration": 3.2,
    "format": "wav",
    "voice": "Zephyr",
    "engine": "gemini"
}
```

---

## 🎨 Customization Guide

### **Adding New Voices**
```python
# In app.py - TTSConfig.VOICE_PROFILES
'CustomVoice': {
    'gender': 'neutral',
    'style': 'custom',
    'emoji': '🎭',
    'quality': 'premium',
    'category': 'Custom'
}
```

### **Theme Customization**
```css
/* Custom color scheme in index.html */
.custom-gradient {
    background: linear-gradient(135deg, #your-color1, #your-color2);
}
```

### **Language Addition**
```python
# Add new language support
LANGUAGES = {
    'your-lang': 'Your Language Name',
    # ... existing languages
}
```

---

## 🔒 Security Features

### **Built-in Security**
- ✅ **Input Validation**: XSS and injection prevention
- ✅ **Rate Limiting**: DoS attack protection
- ✅ **CORS Configuration**: Cross-origin request control
- ✅ **Security Headers**: Content Security Policy
- ✅ **File Upload Validation**: Safe file handling
- ✅ **Environment Variable Protection**: Secret management
- ✅ **HTTPS Enforcement**: Encrypted communications

### **Security Best Practices**
```env
# Strong secret key generation
SECRET_KEY=$(python -c 'import secrets; print(secrets.token_hex(32))')

# Enable security features
ENABLE_SECURITY_HEADERS=true
ENABLE_RATE_LIMITING=true
CORS_ORIGINS=your-domain.com
```

---

## 📈 Monitoring & Analytics

### **Built-in Metrics**
- 📊 **Generation Statistics**: Total count, duration, success rate
- 🎭 **Voice Usage**: Most popular voices and engines
- 🔍 **Error Tracking**: Failure rates and error types
- ⚡ **Performance Metrics**: Response times and throughput
- 💾 **Resource Usage**: Memory and storage consumption

### **Health Check Endpoint**
```bash
curl https://your-app.render.com/api/health

Response:
{
    "status": "healthy",
    "timestamp": "2025-06-10T14:30:22Z",
    "gemini_available": true,
    "version": "2.0.0"
}
```

---

## 🚨 Troubleshooting

### **Common Issues**

**1. Gemini API Key Error**
```bash
Error: "GEMINI_API_KEY not found"
Solution: Set environment variable or check .env file
```

**2. Audio Generation Fails**
```bash
Error: "Text too long. Maximum 5000 characters"
Solution: Break text into smaller chunks or use batch processing
```

**3. Memory Issues**
```bash
Error: "Out of memory"
Solution: Reduce worker count or upgrade server plan
```

**4. File Upload Problems**
```bash
Error: "File too large"
Solution: Check MAX_FILE_SIZE setting (default: 16MB)
```

### **Debug Mode**
```bash
# Enable debug logging
export LOG_LEVEL=DEBUG
export FLASK_DEBUG=true
python app.py
```

---

## 🤝 Contributing

### **Development Setup**
```bash
# Clone repository
git clone https://github.com/chamika1/tts-web.git
cd ai-tts-pro

# Create feature branch
git checkout -b feature/your-feature-name

# Install development dependencies
pip install -r requirements.txt
pip install pytest black isort

# Run tests
pytest

# Format code
black app.py
isort app.py

# Commit changes
git commit -m "Add your feature"
git push origin feature/your-feature-name
```

### **Contribution Guidelines**
1. **Fork** the repository
2. **Create** a feature branch
3. **Write** tests for new features
4. **Ensure** code quality with black/isort
5. **Update** documentation
6. **Submit** a Pull Request

---

## 📜 License & Credits

### **License**
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### **Acknowledgements**
- [Google Gemini](https://ai.google.dev/) - Premium AI voice synthesis
- [Microsoft Edge TTS](https://github.com/rany2/edge-tts) - Multilingual TTS support
- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Tailwind CSS](https://tailwindcss.com/) - UI styling
- [Render.com](https://render.com/) - Deployment platform

### **Special Thanks**
- **Google AI Team** for Gemini API access
- **Microsoft Speech Team** for Edge TTS
- **Open Source Community** for invaluable libraries
- **Contributors** who help improve this project

---

## 📞 Support & Contact

### **Get Help**
- 📧 **Email**: rasanjanachamika@gmail.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/chamika1/tts-web/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/chamika1/tts-web/discussions)
- 📖 **Documentation**: Built-in help system

### **Professional Services**
- 🔧 **Custom Integrations**
- 🎯 **Enterprise Deployment**
- 📊 **Analytics & Monitoring**
- 🛡️ **Security Auditing**
- 🎓 **Training & Support**

---

## 🗺️ Roadmap

### **Version 2.1 (Q3 2025)**
- [ ] Real-time streaming TTS
- [ ] Voice cloning capabilities
- [ ] Advanced emotion control
- [ ] Multi-language detection
- [ ] Voice mixing and effects

### **Version 2.2 (Q4 2025)**
- [ ] Mobile app (iOS/Android)
- [ ] Offline voice synthesis
- [ ] Custom voice training
- [ ] Enterprise dashboard
- [ ] API rate plan tiers

### **Version 3.0 (2026)**
- [ ] Video lip-sync generation
- [ ] AI voice conversation
- [ ] Voice style transfer
- [ ] Advanced analytics
- [ ] Marketplace integration

---

<div align="center">

### Made with ❤️ by [Ashen Chamika](https://github.com/chamika1)

**Star ⭐ this repository if you found it helpful!**

[![GitHub stars](https://img.shields.io/github/stars/chamika1/tts-web.svg?style=social&label=Star)](https://github.com/chamika1/tts-web)
[![GitHub forks](https://img.shields.io/github/forks/chamika1/tts-web.svg?style=social&label=Fork)](https://github.com/chamika1/tts-web/fork)
[![GitHub issues](https://img.shields.io/github/issues/chamika1/tts-web.svg)](https://github.com/chamika1/tts-web/issues)

</div>

---

*Last updated: June 10, 2025 • Version 2.0.0 Enhanced Edition*
