from transformers import pipeline

translator = pipeline("translation", model="google/flan-ul2")

def translate_text(text, target_lang):
    return translator(text, tgt_lang=target_lang)[0]['translation_text']
