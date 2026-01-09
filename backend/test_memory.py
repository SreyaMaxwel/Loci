from models import *

S = 2
print("Initial memory:", S)

days = predict_revision_time(S)
print("Next revision in days:", days)

# Simulate successful revision
S = update_memory_strength(S, success=True)
print("Memory after revision:", S)

days_new = predict_revision_time(S)
print("New revision interval:", days_new)
from models import *

S = 2
print("Initial memory:", S)

days = predict_revision_time(S)
print("Next revision in days:", days)

# Simulate successful revision
S = update_memory_strength(S, success=True)
print("Memory after revision:", S)

days_new = predict_revision_time(S)
print("New revision interval:", days_new)
