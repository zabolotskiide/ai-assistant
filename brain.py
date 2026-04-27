import requests
def ask_ai(prompt):
    try:
        r = requests.post("http://localhost:11434/api/generate",
        json={"model":"tinyllama","prompt":prompt,"stream":False})
        return r.json().get("response","")
    except Exception as e:
        return str(e)
