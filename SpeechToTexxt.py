import speech_recognition as sr
# audio_file = "output.wav"

# with sr.AudioFile(audio_file) as source:
#     audio_data = recognizer.record(source)
#     text = recognizer.recognize_google(audio_data)

# print("Transcription: ", text)



def speechtotext(audio_file,recognizer):
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    return text
    