# scheduler.py
from datetime import datetime


# -----------------------------
# Urgency Model
# -----------------------------

def compute_urgency(revision_time):
    """
    Higher urgency = needs revision sooner
    Urgency = 1 / remaining time
    """
    remaining_seconds = (revision_time - datetime.now()).total_seconds()

    if remaining_seconds <= 0:
        return float('inf')  # overdue topics get highest priority

    return 1 / remaining_seconds


# -----------------------------
# Priority Sorting
# -----------------------------

def sort_by_priority(study_list):
    """
    study_list = [
        {
            "topic": "Thermodynamics",
            "revision_time": datetime_object
        }
    ]
    Returns list sorted by urgency (highest first)
    """
    return sorted(
        study_list,
        key=lambda x: compute_urgency(x["revision_time"]),
        reverse=True
    )


# -----------------------------
# Time Formatting Helper
# -----------------------------

def format_time(hour_float):
    """
    Converts float hour (18.5) → '18:30'
    """
    hours = int(hour_float)
    minutes = int((hour_float - hours) * 60)
    return f"{hours:02d}:{minutes:02d}"


# -----------------------------
# Daily Timetable Generator
# -----------------------------

def generate_schedule(topics):
    schedule = []

    start_hour = 18
    start_min = 0

    for topic in topics:
        time = f"{start_hour}:{start_min:02d} - {start_hour}:{start_min+30:02d}"
        schedule.append({"topic": topic, "time": time})
        start_min += 30

    return schedule

def generate_daily_timetable(sorted_topics, start_hour=18, duration_hours=3):
    """
    sorted_topics = list sorted by urgency
    start_hour = when student starts studying (24h format)
    duration_hours = total study duration for the day

    Assumption: each topic takes 30 minutes
    """
    timetable = []
    current_time = start_hour
    max_slots = duration_hours * 2  # 30-min slots

    for topic in sorted_topics:
        if len(timetable) >= max_slots:
            break

        start = format_time(current_time)
        end = format_time(current_time + 0.5)

        timetable.append({
            "topic": topic["topic"],
            "time": f"{start} - {end}"
        })

        current_time += 0.5

    return timetable


# -----------------------------
# Local Test (Optional)
# -----------------------------

if __name__ == "__main__":
    from datetime import timedelta

    mock_topics = [
        {
            "topic": "Thermodynamics",
            "revision_time": datetime.now() + timedelta(hours=5)
        },
        {
            "topic": "Newton Laws",
            "revision_time": datetime.now() + timedelta(hours=2)
        },
        {
            "topic": "Algebra",
            "revision_time": datetime.now() + timedelta(hours=8)
        }
    ]

    prioritized = sort_by_priority(mock_topics)
    timetable = generate_daily_timetable(prioritized)

    for slot in timetable:
        print(slot)
