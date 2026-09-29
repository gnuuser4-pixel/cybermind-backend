from flask import Flask, jsonify, request
from flask_cors import CORS
from simulator import simulate_attack
from detector import detect_threat
from attack_engine import build_attack_path
import os

app = Flask(__name__)
CORS(app)

@app.get("/")
def home():
    return jsonify({
        "message": "CYBERMIND Security API is running",
        "service": "CYBERMIND",
        "status": "online"
    })

@app.get("/api/health")
def health():
    return jsonify({"status": "healthy"})

@app.post("/api/simulate")
def simulate():
    data = request.get_json(silent=True) or {}
    attack = str(data.get("attack", "phishing")).lower().strip()

    allowed = {"phishing", "bruteforce", "ransomware"}
    if attack not in allowed:
        return jsonify({
            "success": False,
            "error": f"Unsupported attack. Use one of: {', '.join(sorted(allowed))}"
        }), 400

    result = simulate_attack(attack)
    detection = detect_threat(result["events"])
    attack_path = build_attack_path(attack, detection)

    return jsonify({
        "success": True,
        "attack": attack,
        "events": result["events"],
        "detection": detection,
        "attack_path": attack_path
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"CYBERMIND starting on port {port}")
    app.run(host="0.0.0.0", port=port, debug=True)
