from brain import ask_ai
from actions import run_command

def process(text):
    action = run_command(text)
    if action:
        return action
    return ask_ai(text)
