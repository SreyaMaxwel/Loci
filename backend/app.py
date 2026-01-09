from flask import Flask, request, jsonify
from datetime import datetime, timedelta



import math

app = Flask(__name__)

memory_db = {}

@app.route("/")
def home():
    return "Server is running"

@app.route("/add_study", methods=["POST"])
def add_study():
    data = request.json
    topic = data["topic"]

    S = 2  # memory strength
    memory_db[topic] = S

    threshold = 0.8
    t = -S * math.log(threshold)

    return jsonify({
        "topic": topic,
        "next_revision_days": t
    })
def get_next_revision_datetime(days):
    """
    Converts fractional days into an actual datetime.
    """
    now = datetime.now()
    revision_time = now + timedelta(days=days)
    return revision_time

if __name__ == "__main__":
    app.run(debug=True)
