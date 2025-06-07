# ✨ AI TTS Pro ✨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-2.3.3-green.svg)](https://flask.palletsprojects.com/)
[![Google Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)](https://ai.google.dev/)
[![Edge TTS](https://img.shields.io/badge/AI-Edge%20TTS-blueviolet.svg)](https://github.com/rany2/edge-tts)
[![Tailwind CSS](https://img.shields.io/badge/css-Tailwind%20CSS-38B2AC?logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Frontend](https://img.shields.io/badge/frontend-HTML%2FCSS%2FJS-red.svg)](./index.html)
[![Status](https://img.shields.io/badge/status-active-success.svg)]()

---

**AI TTS Pro** is a cutting-edge, professional Text-to-Speech web application designed to bring your text to life. It offers seamless support for multiple languages, including **Sinhala** and **English**, powered by advanced AI engines like Google Gemini and Microsoft Edge TTS. With a sleek user interface and a rich set of features, AI TTS Pro is your go-to solution for high-quality voice generation.

![AI TTS Pro Screenshot]([[https://via.placeholder.com/800x400.png?text=App+Screenshot+Here](https://i.ibb.co/d44pHrpV/Screenshot-2025-06-07-203730.png)](https://i.ibb.co/d44pHrpV/Screenshot-2025-06-07-203730.png))


---

## 🚀 Features

*   🌐 **Multi-Language Support**: Generate speech in various languages, with special focus on Sinhala (si-LK) and English (en-US, en-GB, en-AU). Also supports Tamil (ta-IN) and Hindi (hi-IN).
*   🗣️ **Multiple AI Voice Engines**:
    *   **Google Gemini**: Access premium, natural-sounding voices like Zephyr, Puck, Aoede, and more.
    *   **Microsoft Edge TTS**: Utilize a wide range of multilingual voices, including Thilini (Sinhala) and Aria (English).
*   🔊 **Advanced Audio Controls**:
    *   Adjust **speech rate** and **pitch** for fine-tuned audio output.
    *   Control voice **temperature/expressiveness** (Gemini).
    *   Enable **audio enhancement** (normalization, compression, volume boost).
*   🎧 **Multiple Output Formats**: Export your generated audio in WAV, MP3, OGG, or FLAC formats.
*   ⚙️ **Customizable Voice Profiles**: Choose from a variety of pre-defined voice profiles with different genders and styles.
*   📝 **Text Input Enhancements**:
    *   Character and word count.
    *   Quick text templates for common phrases.
*   ✨ **Modern & Intuitive UI**:
    *   Built with Tailwind CSS for a responsive and visually appealing experience.
    *   Glassmorphism effects and smooth animations.
    *   Light/Dark theme toggle (conceptual, check `index.html` for implementation status).
*   📊 **User Statistics**: Track total generations, total audio duration, and more (conceptual, check `index.html` for implementation status).
*   🔄 **Batch Processing**: Generate speech for multiple text inputs at once (API endpoint available).
*   💾 **Recent Generations History**: Quickly access your previously generated audio files.
*   🛠️ **Robust Backend**: Built with Flask (Python) for reliable performance.
*   📄 **Comprehensive Logging**: Detailed logging for monitoring and troubleshooting.

---

## 🛠️ Tech Stack

*   **Backend**: Python, Flask
*   **Frontend**: HTML, Tailwind CSS, JavaScript
*   **TTS Engines**:
    *   Google Gemini API (`google-genai`)
    *   Microsoft Edge TTS (`edge-tts`)
    *   `pyttsx3` (potentially as a fallback or local engine)
*   **Audio Processing**: `librosa`, `soundfile`, `pydub`, `numpy`
*   **Deployment (Example Configs Provided)**:
    *   `gunicorn` (WSGI server)
    *   `nginx` (Reverse proxy - `ai_tts_nginx.conf`)
    *   `systemd` (Service management - `tts_app.service`)
*   **Environment Management**: `python-dotenv`

---

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://your-repository-url/ai-tts-pro.git
    cd ai-tts-pro
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: For some audio libraries, you might need system-level dependencies. Check `requirements.txt` for notes on `portaudio` and `ffmpeg`.*

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your API keys:
    ```env
    GEMINI_API_KEY="YOUR_GOOGLE_GEMINI_API_KEY"
    # Add any other necessary environment variables
    ```

5.  **Create necessary folders (if not auto-created by `app.py`):**
    ```bash
    mkdir uploads
    mkdir outputs
    ```

---

## 🚀 Running the Application

To run the application in development mode:

```bash
python app.py
```

The application will typically be available at `http://127.0.0.1:5001` or `http://0.0.0.0:5001`.

For production deployment, refer to the example configurations provided:
*   `ai_tts_nginx.conf` for Nginx setup.
*   `tts_app.service` for systemd service setup.
*   You would typically use `gunicorn` to serve the Flask application in a production environment.

---

## API Endpoints

The application exposes several API endpoints:

*   `GET /`: Serves the main HTML page.
*   `POST /api/generate`: Generates TTS audio.
    *   **Payload (JSON)**: `{ "text": "...", "engine": "gemini/edge", "voice": "...", ... }`
*   `GET /api/voices/<engine>`: Retrieves available voices for the specified engine (`gemini` or `edge`).
*   `GET /api/download/<filename>`: Downloads the generated audio file.
*   `POST /api/batch`: Batch TTS generation.
    *   **Payload (JSON)**: `{ "texts": ["text1", "text2"], "config": { ...tts_params... } }`

---

## 🎨 Customization

*   **Voices & Languages**: Modify `TTSConfig.LANGUAGES` and `TTSConfig.VOICE_PROFILES` in `app.py` to add or change supported languages and voices.
*   **Frontend**: The UI is built with Tailwind CSS. You can customize styles in `index.html` or by modifying Tailwind's configuration if you set up a build process.
*   **Audio Processing**: Adjust parameters in `AudioProcessor` class in `app.py` for different enhancement effects.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please make sure to update tests as appropriate and follow the existing code style.

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

*(You'll need to create a `LICENSE` file with the MIT License text if you don't have one)*

---

## 🙏 Acknowledgements

*   [Google Gemini](https://ai.google.dev/) for the powerful TTS capabilities.
*   [Edge TTS Project](https://github.com/rany2/edge-tts) for the versatile Edge TTS integration.
*   The developers of Flask, Tailwind CSS, and other open-source libraries used in this project.

---

## 📞 Contact

Your Name / Organization - your.email@example.com

Project Link: [https://github.com/your-username/ai-tts-pro](https://github.com/your-username/ai-tts-pro) *(Replace with your actual project link)*

---

Made with ❤️ and ☕
