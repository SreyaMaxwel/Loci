from quiz import generate_quiz, score_quiz
from memory import update_memory_strength

topic = "math"

quiz = generate_quiz(topic)

# Fake user answers
user_answers = {
    quiz[0]["id"]: quiz[0]["answer"]  # assume correct
}

score = score_quiz(user_answers, quiz)
new_strength = update_memory_strength(topic, score)

print("Score:", score)
print("Updated Memory Strength:", new_strength)
