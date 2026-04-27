import os
def run_command(text):
    t = text.lower()
    if "браузер" in t:
        os.system("start chrome")
        return "Открываю браузер"
    if "блокнот" in t:
        os.system("notepad")
        return "Открываю блокнот"
    return None
