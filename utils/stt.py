import json
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def transcribe_audio(audio_file, language):
    authenticator = IAMAuthenticator('nohuGThh7Hi9xknxWyWXaxnL1-0QysaxVCnnP5mefGtb')
    stt = SpeechToTextV1(authenticator=authenticator)
    stt.set_service_url('https://api.au-syd.speech-to-text.watson.cloud.ibm.com/instances/5ee0282b-2c4f-4d5b-990d-b5047a2186c9')

    response = stt.recognize(audio=audio_file, content_type='audio/wav', model=f'{language}_BroadbandModel').get_result()
    return response['results'][0]['alternatives'][0]['transcript']
