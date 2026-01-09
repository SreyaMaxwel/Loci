import json

def load_memory():
    with open("data/student_memory.json", "r") as f:
        return json.load(f)

def save_memory(memory):
    with open("data/student_memory.json", "w") as f:
        json.dump(memory, f, indent=2)

def update_memory_strength(topic, score):
    memory = load_memory()

    S_old = memory.get(topic, 1.0)

    S_new = S_old * (1 + 0.1 * (score - 0.8))

    # Keep memory strength safe
    S_new = max(0.1, min(S_new, 2.0))

    memory[topic] = S_new
    save_memory(memory)

    return S_new
