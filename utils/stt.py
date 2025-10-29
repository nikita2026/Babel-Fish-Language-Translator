import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def transcribe_audio(audio_file, language):
    authenticator = IAMAuthenticator('YOUR_IBM_API_KEY')
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url('YOUR_IBM_STT_URL')

    response = stt.recognize(audio=audio_file, content_type='audio/wav', model=f'{language}_BroadbandModel').get_result()
    return response['results'][0]['alternatives'][0]['transcript']
