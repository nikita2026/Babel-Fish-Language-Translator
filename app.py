from flask import Flask, render_template, request, jsonify
from utils.stt import transcribe_audio
from utils.translate import translate_text
from utils.tts import synthesize_speech

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    audio_file = request.files['audio']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']

    text = transcribe_audio(audio_file, source_lang)
    translated = translate_text(text, target_lang)
    audio_output = synthesize_speech(translated, target_lang)

    return jsonify({'text': text, 'translated': translated, 'audio': audio_output})

if __name__ == '__main__':
    app.run(debug=True)
