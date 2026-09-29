def build_attack_path(attack_type, detection):
    if attack_type == "phishing":
        return [
            {"id": "attacker", "name": "Attacker", "icon": "🔴"},
            {"id": "phishing", "name": "Phishing", "icon": "🎣"},
            {"id": "employee", "name": "Employee", "icon": "👤"},
            {"id": "workstation", "name": "Workstation", "icon": "💻"},
            {"id": "admin", "name": "Admin Account", "icon": "👑"},
            {"id": "database", "name": "Database", "icon": "🗄️"},
        ]

    if attack_type == "bruteforce":
        return [
            {"id": "attacker", "name": "Attacker", "icon": "🔴"},
            {"id": "login", "name": "Login Portal", "icon": "🔐"},
            {"id": "account", "name": "Target Account", "icon": "👤"},
            {"id": "admin", "name": "Admin System", "icon": "👑"},
        ]

    if attack_type == "ransomware":
        return [
            {"id": "attacker", "name": "Attacker", "icon": "🔴"},
            {"id": "endpoint", "name": "Employee Device", "icon": "💻"},
            {"id": "files", "name": "Files", "icon": "📁"},
            {"id": "data", "name": "Sensitive Data", "icon": "🗄️"},
        ]

    return [{"id": "unknown", "name": "Unknown Source", "icon": "❓"}]
