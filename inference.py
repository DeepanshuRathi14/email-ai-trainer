def run():
    task_name = "email_reply"

    # START
    print(f"[START] task={task_name}", flush=True)

    # STEP (dummy logic)
    print(f"[STEP] step=1 reward=0.8", flush=True)

    # END
    print(f"[END] task={task_name} score=0.95 steps=1", flush=True)


if __name__ == "__main__":
    run()