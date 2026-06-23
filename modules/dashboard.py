import re

import re

def extract_scores(evaluation_text):

    scores = {
        "accuracy": 0,
        "completeness": 0,
        "communication": 0
    }

    patterns = {
        "accuracy": r"Technical\s*Accuracy.*?(\d+)\s*/\s*10",
        "completeness": r"Completeness.*?(\d+)\s*/\s*10",
        "communication": r"Communication.*?(\d+)\s*/\s*10"
    }

    for key, pattern in patterns.items():

        match = re.search(
            pattern,
            evaluation_text,
            re.IGNORECASE | re.DOTALL
        )

        if match:
            scores[key] = int(match.group(1))

    return scores