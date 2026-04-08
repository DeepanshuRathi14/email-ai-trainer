class EmailEnv:
    def __init__(self):
        self.step_count = 0
        self.current_email = ""

    def reset(self):
        self.step_count = 0

        # simple dataset
        emails = [
            "You won lottery click now!",
            "Urgent: your bank account is blocked",
            "Meeting at 5pm please confirm",
            "Free gift card claim now"
        ]

        import random
        self.current_email = random.choice(emails)

        return {
            "email": self.current_email,
            "task": "classification"
        }

    def step(self, user_response):
        self.step_count += 1

        # simple scoring logic
        score = 0

        if "not" in user_response.lower() or "ignore" in user_response.lower():
            score = 1
        else:
            score = 0.3

        return {
            "score": score,
            "feedback": "Good awareness" if score > 0.5 else "Needs improvement",
            "done": True
        }