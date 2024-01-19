import time

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define animation variables
transition_start_time = 0
transition_duration = 0.5  # In seconds
transition_alpha = 0

# Define transition states
TRANSITION_NONE = 0
TRANSITION_IN = 1
TRANSITION_OUT = 2

def transition(state):
    global transition_start_time, transition_alpha
    transition_start_time = time.time()
    if state == TRANSITION_IN:
        transition_alpha = 255
    elif state == TRANSITION_OUT:
        transition_alpha = 0
