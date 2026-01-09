# test.py
from models import retention, predict_revision_time, add_study_session
from datetime import datetime

# Memory database
memory_db = {}

# Add a study session
memory_db = add_study_session(memory_db, "Newton's Laws", datetime.now())

# Check retention after 1 day
S = memory_db["Newton's Laws"]["S"]
t = 1  # 1 day later
print("Retention after 1 day:", retention(S, t))

# Predict next revision
next_revision = predict_revision_time(S)
print("Next revision should be after (days):", next_revision)
