# models.py
import math
from datetime import datetime, timedelta


# -----------------------------
# Forgetting Curve Model
# -----------------------------

def retention(S, t):
    """
    S = memory strength of topic (higher = slower forgetting)
    t = time passed since study (days)
    Returns retention value between 0 and 1
    """
    return math.exp(-t / S)


# -----------------------------
# Predict Next Revision Time
# -----------------------------

def predict_revision_time(S, threshold=0.8):
    """
    S = memory strength
    threshold = retention level at which revision is needed
    Returns next revision time in DAYS (float)
    """
    if threshold <= 0 or threshold >= 1:
        raise ValueError("Threshold must be between 0 and 1")

    t = -S * math.log(threshold)
    return t


# -----------------------------
# Convert Days → Actual Time
# -----------------------------

def revision_time_to_datetime(days):
    """
    Converts predicted days into an actual datetime
    """
    return datetime.now() + timedelta(days=days)


def days_to_hours_minutes(days):
    """
    Converts fractional days into hours and minutes
    Example: 0.446 → 10 hours 42 minutes
    """
    total_minutes = int(days * 24 * 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes


# -----------------------------
# Track Study Session
# -----------------------------

def add_study_session(memory_db, topic, study_date=None, S_default=2):
    """
    memory_db = dictionary storing memory information
    topic = topic name
    study_date = datetime of study (defaults to now)
    S_default = initial memory strength
    """

    if study_date is None:
        study_date = datetime.now()

    memory_db[topic] = {
        "last_study": study_date,
        "S": S_default
    }

    return memory_db

def update_memory_strength(S, success=True):
    """
    Updates memory strength after revision.
    If revision was successful → increase strength
    If failed → slight decrease
    """
    if success:
        return S * 1.2   # memory improves
    else:
        return max(1, S * 0.9)  # memory weakens but not below 1
