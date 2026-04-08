import requests

BASE = "http://localhost:8000"

def run():
    obs = requests.post(f"{BASE}/reset").json()["observation"]
    print("EMAIL:", obs["email"])

    while True:
        action = {
            "response": "urgent high billing sorry we will resolve your issue"
        }

        result = requests.post(f"{BASE}/step", json=action).json()
        print(result)

        if result["done"]:
            break

if __name__ == "__main__":
    run()