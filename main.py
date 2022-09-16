
from gtts import gTTS
import os

weeks_words = ["tomato", "carrot", "pumpkin", "python", "children", "programming"]

score = 0

language = 'en'

while score != len(weeks_words):

    word = weeks_words[score]

    output = gTTS(text=word, lang=language, slow=False)

    output.save("output.mp3")

    os.system("open output.mp3")

    attempt = input("Please spell the word you have just heard. type 'repeat' to hear it again. ")

    if attempt == "repeat":
        os.system("open output.mp3")
    elif attempt == word:
        score += 1
        print(f"Well done, Your current score is {score} out of {len(weeks_words)}.")
    elif attempt != word:
        print(f"Incorrect. Your current score is still {score}.")

print(f"Your final score is {score}")
