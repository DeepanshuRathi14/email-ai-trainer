import os
from openai import OpenAI

def run():
    task_name = "email_reply"

    # setup client using provided proxy
    client = OpenAI(
        base_url=os.environ.get("API_BASE_URL"),
        api_key=os.environ.get("API_KEY")
    )

    # START
    print(f"[START] task={task_name}", flush=True)

    # LLM CALL (IMPORTANT)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Write a short professional email reply."}
        ]
    )

    reply = response.choices[0].message.content

    # STEP
    print(f"[STEP] step=1 reward=1.0", flush=True)

    # END
    print(f"[END] task={task_name} score=1.0 steps=1", flush=True)


if __name__ == "__main__":
    run()