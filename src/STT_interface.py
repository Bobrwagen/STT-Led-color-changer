import argparse
from google.cloud import speech

class STT():
    def transcribe_file(self,speech_file: str):
        """Transcribe the given audio file."""
        client = speech.SpeechClient()

        with open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
           # encoding = speech.RecognitionConfig.AudioEncoding.,
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            language_code="de-DE",
    )

        response = client.recognize(config=config, audio=audio)

        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        res = []
        for result in response.results:
           res.append(result.alternatives)
           text = []
        for alt in res:
            text.append(alt[0].transcript)
        res = ""
        for t in text:
            res+=t 
        return res

