from gtts import gTTS
from playsound import playsound

weeks_words = ["tomato", "carrot", "pumpkin", "python", "children", "programming"]

problem_words = []

score = 0

language = 'en'

while score != len(weeks_words):

    word = weeks_words[score]

    output = gTTS(text=word, lang=language, slow=False)

    output.save("output.mp3")

    playsound("output.mp3")

    attempt = input("Please spell the word you have just heard. type 'repeat' to hear it again. ")

    if attempt == "repeat":
        playsound("output.mp3")
    elif attempt == word:
        score += 1
        print(f"Well done, Your current score is {score} out of {len(weeks_words)}.")
    elif attempt != word:
        print(f"Incorrect. Your current score is still {score}.")
        problem_words.append(word)

print(f"Your final score is {score}")
playsound("celebration.mp3")

if len(problem_words) > 0:
    print(f"Your problem words are {problem_words}")
if len(problem_words) >= 3:
    playsound("brah.mp3")

