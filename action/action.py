from ibm_watson import SpeechToTextV1, ApiException
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator
from base64 import b64decode
import speech_recognition as sr
import json, os


def main():
    
    try:

        # Read audio file and call Watson STT API:
        r = sr.Recognizer()
        file = sr.AudioFile('action/audio_sample.flac')
        
        with file as source:
            audio = r.record(source)

            transcription = r.recognize_google(audio, language='pt-br')

        # Print STT API call results
        json.dumps(transcription, indent=2)

        # Return a dictionary with the transcribed text
        return {
            "transcript": transcription
        }

    except:
        pass

print(main())