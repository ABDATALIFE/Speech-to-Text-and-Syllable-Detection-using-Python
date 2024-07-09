from pydub import AudioSegment
from gtts import gTTS
import pyphen

# Initialize the pyphen dictionary
dic = pyphen.Pyphen(lang='en')

# Sample text to convert into syllables
text = "turn on normal speech into trunk type vocals today"

# Split text into words
words = text.split()

# Split each word into syllables and join with hyphens
syllables_list = [dic.inserted(word).split('-') for word in words]

# Create an empty audio segment
audio_with_silence = AudioSegment.empty()

# Add each syllable to the audio with silence between them
for word_syllables in syllables_list:
    for syllable in word_syllables:
        tts = gTTS(syllable)
        tts.save("temp.mp3")  # Save the syllable as a temporary MP3 file
        audio_syllable = AudioSegment.from_file("temp.mp3")  # Load the temporary MP3 file
        audio_with_silence += audio_syllable  # Add the syllable to the audio with silence
        audio_with_silence += AudioSegment.silent(duration=50)  # Add 50 milliseconds of silence between syllables

# Save the reconstructed audio with syllables more prominent
audio_with_silence.export("output_with_syllables.mp3", format="mp3")
