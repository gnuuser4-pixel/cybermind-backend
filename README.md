# CYBERMIND Backend

AI-style attack detection and attack-path simulation using safe synthetic events.

## Local setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
```

Open:

- http://localhost:8080/
- http://localhost:8080/api/health

Test simulation:

```bash
curl -X POST http://localhost:8080/api/simulate \
-H "Content-Type: application/json" \
-d '{"attack":"phishing"}'
```

Supported simulations:

- phishing
- bruteforce
- ransomware

## Render

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
gunicorn app:app
```

The app uses Render's `PORT` environment variable automatically.
