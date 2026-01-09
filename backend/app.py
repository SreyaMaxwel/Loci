from flask import Flask, request, jsonify
from datetime import datetime, timedelta
from models import predict_revision_time
from scheduler import generate_daily_timetable
from flask import render_template


app = Flask(__name__)

# Dummy memory store (later can be DB)
memory_db = []


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_study", methods=["POST"])
def add_study():
    data = request.json
    topic = data["topic"]

    # Memory model output
    S = 2
    days = predict_revision_time(S)

    revision_time = datetime.now() + timedelta(days=days)

    memory_db.append({
        "topic": topic,
        "revision_time": revision_time
    })

    return jsonify({
        "topic": topic,
        "next_revision_days": days
    })

@app.route("/get_timetable", methods=["GET"])
def get_timetable():
    timetable = generate_daily_timetable(memory_db)
    return jsonify(timetable)

if __name__ == "__main__":
    app.run(debug=True)
