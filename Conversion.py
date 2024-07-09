import pyphen
import speech_recognition as sr
recognizer = sr.Recognizer()

from SpeechToTexxt import speechtotext

# Initialize the pyphen dictionary


audio_file = 'output.wav'

dic = pyphen.Pyphen(lang='en')

# Sample text to split into syllables
text = speechtotext(audio_file,recognizer)

# Split text into words
words = text.split()

# Print the split words for debugging
print("Words:", words)

# Split each word into syllables and print the output for each word
syllables_list = []
for word in words:
    syllables = dic.inserted(word).split('-')
    print(f"Word: {word}, Syllables: {syllables}")
    syllables_list.append(syllables)

# Join syllables with hyphens and words with spaces
hyphenated_text = ' '.join(['-'.join(syllable) for syllable in syllables_list])

# Print the result
print("Hyphenated text:", hyphenated_text)
