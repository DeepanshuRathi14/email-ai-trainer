def grade(response, truth):
    response = response.lower()
    score = 0.0

    if truth["label"] in response:
        score += 0.3
    if truth["priority"] in response:
        score += 0.3
    if truth["department"] in response:
        score += 0.2
    if len(response.split()) > 5:
        score += 0.2

    return min(score, 1.0)