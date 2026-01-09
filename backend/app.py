from flask import Flask, request, jsonify
from datetime import datetime
from models import (
    add_study_session,
    predict_revision_time,
    revision_time_to_datetime,
    days_to_hours_minutes,
    update_memory_strength
)
from scheduler import sort_by_priority, generate_daily_timetable

app = Flask(__name__)

# -----------------------------
# In-memory storage
# -----------------------------
memory_db = {}
study_queue = []

print("🔥 CORRECT app.py IS RUNNING 🔥")


# -----------------------------
# Health Check
# -----------------------------
@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"})


# -----------------------------
# Submit Study Session (MAIN API 1)
# -----------------------------
@app.route("/submit_study", methods=["POST"])
def submit_study():
    data = request.get_json()

    if not data or "topic" not in data:
        return jsonify({"error": "Topic is required"}), 400

    topic = data["topic"]

    # 1. Record study session
    add_study_session(memory_db, topic)

    # 2. Predict next revision
    S = memory_db[topic]["S"]
    days = predict_revision_time(S)
    revision_time = revision_time_to_datetime(days)

    # 3. Store for scheduling
    study_queue.append({
        "topic": topic,
        "revision_time": revision_time
    })

    h, m = days_to_hours_minutes(days)

    return jsonify({
        "message": "Study session recorded",
        "topic": topic,
        "next_revision_in": f"{h} hours {m} minutes"
    })


# -----------------------------
# Get Optimized Timetable (MAIN API 2)
# -----------------------------
@app.route("/get_timetable", methods=["GET"])
def get_timetable():
    if not study_queue:
        return jsonify({"study_plan": []})

    sorted_topics = sort_by_priority(study_queue)

    timetable = generate_daily_timetable(
        sorted_topics,
        start_hour=18,
        duration_hours=3
    )

    return jsonify({
        "study_plan": timetable
    })


# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
