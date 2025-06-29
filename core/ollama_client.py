import requests

def ask_ollama(prompt: str):
    payload = {
        "model": "tinyllama",  # or tinyllama or whichever you pulled
        "prompt": f"Convert this to JSON:\n\n{prompt}",
        "stream": False
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload)

    # Extract the raw response
    raw = response.json()["response"].strip()

    try:
        return eval(raw)  # ⚠️ Works for now. Use json.loads() with better formatting later.
    except:
        return {"error": "Failed to parse JSON", "raw": raw}
