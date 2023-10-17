from flask import Flask, render_template, request, jsonify
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
from io import BytesIO

import base64
import torchaudio

app = Flask(__name__)

model = MusicGen.get_pretrained('facebook/musicgen-melody')
model.set_generation_params(duration=8)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    promptText = data['prompt']
    durationValue = int(data['duration'])  # Extract the duration from the request

    model.set_generation_params(duration=durationValue)  # Set the duration before generating

    # Generate the audio
    wav = model.generate([promptText])

    # Convert the tensor to bytes
    buffer = BytesIO()
    torchaudio.save(buffer, wav[0].cpu(), model.sample_rate, format="wav")
    audio_bytes = buffer.getvalue()

    # Encode the audio bytes to base64
    base64_encoded_audio = base64.b64encode(audio_bytes).decode('utf-8')

    return jsonify({"audio": base64_encoded_audio})

if __name__ == '__main__':
    app.run(debug=True)
