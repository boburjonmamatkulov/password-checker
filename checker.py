def check_password(password):
    score = 0
    feedback = []

    # Uzunlik tekshiruvi
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Kamida 8 ta belgi bo'lsin")

    # Katta harf
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Katta harf qo'shing (A-Z)")

    # Kichik harf
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Kichik harf qo'shing (a-z)")

    # Raqam
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Raqam qo'shing (0-9)")

    # Maxsus belgi
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if any(c in special for c in password):
        score += 1
    else:
        feedback.append("Maxsus belgi qo'shing (!@#$...)")

    return score, feedback


# Asosiy dastur
password = input("Parolni kiriting: ")
score, feedback = check_password(password)

levels = {5: "Juda kuchli", 4: "Kuchli", 3: "O'rtacha", 2: "Zaif", 1: "Juda zaif"}
level = levels.get(score, "Juda zaif")

print(f"\nNatija: {level} ({score}/5 ball)")
if feedback:
    print("Maslahatlar:")
    for tip in feedback:
        print(f"  - {tip}")