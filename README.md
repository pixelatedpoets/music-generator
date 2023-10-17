# Pixelated Poets Music Generator

Frontend and Backend to generate music with Facebook's MusicGen model. Check us out on https://www.youtube.com/@PixelatedPoets/

## The application

Generate music samples up to 30 seconds. In the prompt describe your music style, instruments, and other characteristics.
The backend will generate the sound sample, and the frontend will play the audio sample for you.

## Installation

AudioCraft requires Python 3.9, PyTorch 2.0.0. To install AudioCraft, you can run the following:

```bash
git clone https://github.com/pixelatedpoets/music-generator.git
cd music-generator
python3.9 -m venv .venv
source .venv/bin/activate
pip install 'torch>=2.0'
pip install -U audiocraft
pip install flask
pip install torchaudio
```

## Starting the webserver

```bash
python app.py
```

After that navigate to `http://127.0.0.1:5000/`. Type a prompt and select a duration and hit 'generate'.
