from datetime import datetime, timedelta

def simulate_attack(attack_type):
    start = datetime.now()

    def event(seconds, event_type, description):
        return {
            "time": (start + timedelta(seconds=seconds)).strftime("%H:%M:%S"),
            "type": event_type,
            "description": description
        }

    if attack_type == "phishing":
        events = [
            event(0, "phishing_email", "Suspicious email delivered to employee"),
            event(5, "malicious_link", "Simulated phishing link clicked"),
            event(10, "credential_attempt", "Simulated credential submission detected"),
            event(15, "unusual_login", "Login from unusual location"),
        ]
    elif attack_type == "bruteforce":
        events = [
            event(0, "failed_login", "Multiple failed login attempts"),
            event(5, "failed_login", "Repeated authentication attempts"),
            event(10, "failed_login", "Authentication threshold exceeded"),
            event(15, "account_target", "Administrative account targeted"),
        ]
    elif attack_type == "ransomware":
        events = [
            event(0, "rapid_file_activity", "Abnormally high file modification activity"),
            event(5, "file_extension_change", "Multiple simulated file extensions changed"),
            event(10, "mass_file_operation", "Large number of files modified"),
            event(15, "suspicious_encryption", "Simulated encryption-like behavior detected"),
        ]
    else:
        events = [event(0, "suspicious_activity", "Suspicious activity detected")]

    return {"attack": attack_type, "events": events}
