def detect_threat(events):
    types = {event.get("type") for event in events}

    if "phishing_email" in types:
        return {
            "detected": True,
            "severity": "HIGH",
            "threat": "Phishing / Credential Compromise",
            "confidence": 94,
            "weakest_point": "Identity Layer"
        }

    if "failed_login" in types:
        return {
            "detected": True,
            "severity": "HIGH",
            "threat": "Brute Force Attempt",
            "confidence": 91,
            "weakest_point": "Authentication Layer"
        }

    if "rapid_file_activity" in types:
        return {
            "detected": True,
            "severity": "CRITICAL",
            "threat": "Possible Ransomware Behavior",
            "confidence": 96,
            "weakest_point": "Endpoint Layer"
        }

    return {
        "detected": True,
        "severity": "LOW",
        "threat": "Suspicious Activity",
        "confidence": 76,
        "weakest_point": "Unknown"
    }
