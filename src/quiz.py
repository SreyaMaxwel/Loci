import json
import random

def load_questions():
    with open("data/questions.json", "r") as f:
        return json.load(f)

def generate_quiz(topic, num_questions=2):
    questions = load_questions()
    
    if topic not in questions:
        return []

    return random.sample(questions[topic], min(num_questions, len(questions[topic])))
def score_quiz(user_answers, quiz):
    correct = 0

    for q in quiz:
        qid = q["id"]
        if user_answers.get(qid) == q["answer"]:
            correct += 1

    score = correct / len(quiz)
    return score
