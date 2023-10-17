# Pixelated Poets Music Generator

Frontend and Backend to generate music with Facebook's MusicGen model. Check us out on https://www.youtube.com/@PixelatedPoets/

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

## Starting the front-end

```bash
python app.py
```
