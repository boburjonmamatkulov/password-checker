from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

WEAK_PASSWORDS = [
    "123456", "password", "123456789", "12345678", "12345",
    "1234567", "qwerty", "abc123", "111111", "123123",
    "admin", "letmein", "welcome", "monkey", "dragon"
]

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

def check_password(password):
    score = 0
    feedback = []

    if password.lower() in WEAK_PASSWORDS:
        return 0, ["Bu parol juda mashhur — xakerlar birinchi sinab ko'radi!"]

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Kamida 8 ta belgi bo'lsin")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Katta harf qo'shing (A-Z)")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Kichik harf qo'shing (a-z)")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Raqam qo'shing (0-9)")

    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special for c in password):
        score += 1
    else:
        feedback.append("Maxsus belgi qo'shing (!@#$...)")

    return score, feedback

def get_level(score):
    if score >= 5:
        return "Juda kuchli", "#22c55e"
    elif score == 4:
        return "Kuchli", "#86efac"
    elif score == 3:
        return "O'rtacha", "#facc15"
    elif score == 2:
        return "Zaif", "#fb923c"
    else:
        return "Juda zaif", "#ef4444"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    generated = None

    if request.method == "POST":
        if "password" in request.form:
            password = request.form["password"]
            score, feedback = check_password(password)
            level, color = get_level(score)
            result = {
                "score": score,
                "level": level,
                "color": color,
                "feedback": feedback
            }
        elif "generate" in request.form:
            generated = generate_password()

    return render_template("index.html", result=result, generated=generated)

if __name__ == "__main__":
    app.run(debug=True)