from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import base64

def synthesize_speech(text, language):
    authenticator = IAMAuthenticator('rGSdEsOW5CaVFrie7LVctvpoY4xnT7PcvnHbJrS7vR3S')
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/60cde0ad-6a7f-4c23-9373-cb4cbc07eb37')

    response = tts.synthesize(text, voice=f'{language}_Voice', accept='audio/wav').get_result().content
    return base64.b64encode(response).decode('utf-8')
