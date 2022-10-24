import speech_recognition as sr
from os import path
from pydub import AudioSegment

# convert mp3 file to wav
sound = AudioSegment.from_mp3("transcribe2.mp3")
sound.export("transcribe2.wav", format="wav")

# transcribe audio file
AUDIO_FILE = "transcribe2.wav"

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

    print("Transcription: ")
    print(r.recognize_google(audio, language='ja'))
