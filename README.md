#  Email AI Trainer

##  Problem
Many users fall victim to phishing and scam emails due to lack of awareness and training.

##  Solution
Email AI Trainer is an interactive system that simulates real-world email scenarios and trains users by evaluating their responses using AI-based logic.

---

##  Features
- Email simulation (spam + legitimate)
- User response input
- AI-based evaluation
- Score + feedback system
- Simple interactive UI

---

##  How it Works
1. User clicks **Get Email**
2. System generates an email (can be scam or normal)
3. User writes a response
4. System evaluates response and gives:
   - Score
   - Feedback

---

##  Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Server:** Uvicorn

---

##  Project Structure
email-ai-trainer/
│
├── server/
│ ├── main.py
│ ├── models.py
│ ├── grader.py
│
├── ui/
│ └── index.html
│
├── inference.py
├── requirements.txt
├── Dockerfile
├── README.md

---


##  Run Locally

```bash
pip install -r requirements.txt
uvicorn server.main:app --reload

Open:

ui/index.html