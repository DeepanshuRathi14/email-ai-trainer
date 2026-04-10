def grade(task, response, truth):
    response = response.lower()

    score = 0.0

    # -------- TASK 1: EMAIL CLASSIFICATION --------
    if task == "email_classification":
        if truth.get("label", "") in response:
            score += 0.3
        if truth.get("priority", "") in response:
            score += 0.3
        if truth.get("department", "") in response:
            score += 0.2
        if len(response.split()) > 5:
            score += 0.2

    # -------- TASK 2: EMAIL SUMMARY --------
    elif task == "email_summary":
        if len(response.split()) > 5:
            score += 0.5
        if "summary" in response or "brief" in response:
            score += 0.5

    # -------- TASK 3: EMAIL REPLY --------
    elif task == "email_reply":
        if "thank" in response or "regards" in response:
            score += 0.5
        if len(response.split()) > 5:
            score += 0.5

    return min(score, 1.0)