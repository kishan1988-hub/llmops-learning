import requests

response = requests.post("http://localhost:11434/api/generate", 
                         json={"model": "llama3.2", "prompt": "Whats kubernetes?", "stream": False})

data = response.json()
print(data["response"])
print(f"Tokens used:{data['eval_count']}")

