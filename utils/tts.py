from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import base64

def synthesize_speech(text, language):
    authenticator = IAMAuthenticator('YOUR_IBM_API_KEY')
    tts = TextToSpeechV1(authenticator=authenticator)
    tts.set_service_url('YOUR_IBM_TTS_URL')

    response = tts.synthesize(text, voice=f'{language}_Voice', accept='audio/wav').get_result().content
    return base64.b64encode(response).decode('utf-8')
