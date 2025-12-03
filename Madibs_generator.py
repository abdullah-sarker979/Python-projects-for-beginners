with open("story.txt", "r") as f:
    story = f.read()


words = set()
start_of_words = -1

starting_target = "<"
ending_target = ">"

for i, char in enumerate(story):
    if char == starting_target:
        start_of_words = i

    if char == ending_target and start_of_words != -1:
        word = story[start_of_words: i + 1]
        words.add(word)
        start_of_words = -1

answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])
print(story)
