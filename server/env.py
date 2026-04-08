import random

TASKS = [
    {
        "email": "Payment failed, money deducted!",
        "label": "urgent",
        "priority": "high",
        "department": "billing",
        "expected_reply": "We are sorry. Billing team will resolve your issue urgently."
    },
    {
        "email": "How to reset password?",
        "label": "support",
        "priority": "medium",
        "department": "tech",
        "expected_reply": "You can reset password from settings."
    },
    {
        "email": "You won lottery click now!",
        "label": "spam",
        "priority": "low",
        "department": "general",
        "expected_reply": "This looks like spam. Please ignore."
    }
]

class EmailEnv:
    def __init__(self):
        self.step_count = 0
        self.current = None
        self.stage = 0

    def reset(self):
        self.step_count = 0
        self.stage = 0
        self.current = random.choice(TASKS)

        return {
            "email": self.current["email"],
            "task": "classification",
            "step": self.step_count
        }

    def step(self, action):
        self.step_count += 1
        response = action.get("response", "").lower()

        reward = 0

        # Stage 1: Classification
        if self.stage == 0:
            if self.current["label"] in response:
                reward = 0.3
                self.stage = 1
                next_task = "priority"
            else:
                reward = -0.2
                next_task = "classification"

        # Stage 2: Priority
        elif self.stage == 1:
            if self.current["priority"] in response:
                reward = 0.3
                self.stage = 2
                next_task = "routing"
            else:
                reward = -0.2
                next_task = "priority"

        # Stage 3: Final response
        else:
            if self.current["department"] in response:
                reward += 0.2
            if any(word in response for word in ["sorry", "help", "resolve", "ignore"]):
                reward += 0.2

            next_task = "done"

        done = next_task == "done"

        return {
            "observation": {
                "email": self.current["email"],
                "task": next_task,
                "step": self.step_count
            },
            "reward": max(0.0, min(1.0, reward)),
            "done": done,
            "info": {"stage": self.stage}
        }