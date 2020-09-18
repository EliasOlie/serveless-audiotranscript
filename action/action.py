from base64 import b64decode
from cgi import parse_multipart, parse_header
from io import BytesIO
import speech_recognition as sr
import json, os


def main(args):
    
    try:
        _c_type, p_dict = parse_header(
        args['__ow_headers']['content-type']
        )
        
        # Decode body (base64)
        decoded_string = b64decode(args['__ow_body'])

        # Set Headers for multipart_data parsing
        p_dict['boundary'] = bytes(p_dict['boundary'], "utf-8")
        p_dict['CONTENT-LENGTH'] = len(decoded_string)
        
        # Parse incoming request data
        multipart_data = parse_multipart(
            BytesIO(decoded_string), p_dict
        )

        # Build flac file from stream of bytes
        fo = open("audio_sample.flac", 'wb')
        fo.write(multipart_data.get('audio')[0])
        fo.close()
        # Read audio file and call Watson STT API:
        with open(
        os.path.join(
            os.path.dirname(__file__), './.',
            'audio_sample.flac'
        ), 'rb'
    ) as audio_file:
            r = sr.Recognizer()
            file = audio_file
        
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

