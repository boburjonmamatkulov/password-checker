# 🔐 Parol Kuchi Tekshiruvchi

Foydalanuvchi parolini tahlil qilib, kuchini baholaydi, maslahat beradi va kuchli parol yaratib beradi.

## ✨ Xususiyatlar

- ✅ Parol kuchini 6 balllik tizimda baholaydi
- 🔴 15+ keng tarqalgan zaif parollarni aniqlaydi
- 💡 Yaxshilash bo'yicha aniq maslahatlar beradi
- 🎲 Tasodifiy kuchli parol generatori
- 🌐 Brauzerda ishlaydigan veb interfeys (Flask)
- 🚨 HaveIBeenPwned API — parol real data breach da chiqganmi tekshiradi
- 🛡️ K-anonymity texnikasi — parol hech qachon to'liq yuborilmaydi

## 🚀 Ishlatish

```bash
pip3 install -r requirements.txt
python3 app.py
```

Keyin brauzerda oching: `http://127.0.0.1:5000`

## 🛡️ Nima uchun parol xavfsizligi muhim?

Kiberxavfsizlikda eng ko'p ishlatiladigan hujum usullaridan biri — **brute force** va **dictionary attack**. Kuchli parol bu hujumlardan himoya qiladi.

`123456` paroli **209,972,844** marta real data breach larda topilgan!

## 🔬 HaveIBeenPwned qanday ishlaydi?

1. Parol SHA-1 algoritmi bilan shifrlanadi
2. Faqat birinchi 5 ta belgi API ga yuboriladi (**k-anonymity**)
3. API o'xshash hash larni qaytaradi
4. Dastur solishtirib, parol buzilganmi aniqlaydi
5. Parol hech qachon to'liq internet ga yuborilmaydi ✅

## 🧰 Texnologiyalar

- Python 3
- Flask (veb framework)
- HaveIBeenPwned API
- HTML / CSS
- SHA-1 kriptografiya

## 👤 Muallif

**Boburjon Mamatqulov** — kiberxavfsizlikka qiziquvchi dasturchi
