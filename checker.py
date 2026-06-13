import random
import string

# Keng tarqalgan zaif parollar
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

    # Keng tarqalgan zaif parol tekshiruvi
    if password.lower() in WEAK_PASSWORDS:
        return 0, ["Bu parol juda mashhur — xakerlar birinchi sinab ko'radi!"]

    # Uzunlik
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Kamida 8 ta belgi bo'lsin (12+ ideal)")

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

def get_level(score):
    if score >= 5:
        return "✅ Juda kuchli"
    elif score == 4:
        return "🟢 Kuchli"
    elif score == 3:
        return "🟡 O'rtacha"
    elif score == 2:
        return "🟠 Zaif"
    else:
        return "🔴 Juda zaif"

# Asosiy dastur
print("=" * 40)
print("   PAROL KUCHI TEKSHIRUVCHI")
print("=" * 40)

while True:
    print("\n1 - Parolni tekshirish")
    print("2 - Kuchli parol yaratish")
    print("3 - Chiqish")
    
    tanlov = input("\nTanlang (1/2/3): ")
    
    if tanlov == "1":
        password = input("Parolni kiriting: ")
        score, feedback = check_password(password)
        level = get_level(score)
        print(f"\nNatija: {level} ({score}/6 ball)")
        if feedback:
            print("Maslahatlar:")
            for tip in feedback:
                print(f"  - {tip}")
    
    elif tanlov == "2":
        password = generate_password()
        print(f"\nYangi kuchli parol: {password}")
        score, feedback = check_password(password)
        print(f"Kuchi: {get_level(score)}")
    
    elif tanlov == "3":
        print("Xayr!")
        break
    
    else:
        print("Noto'g'ri tanlov, qaytadan urining")