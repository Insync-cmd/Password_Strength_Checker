# Password_Strength_Checker
fully functional password strength checker with colors + hashing
# 🔒 Password Strength Checker

A simple Python tool to evaluate password strength and demonstrate secure storage (SHA256 hashing).

## 🚀 Features
- Rates password strength as **Weak / Medium / Strong**
- Criteria:
  - Minimum length (≥ 8)
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
- Color-coded output:
  - ✅ Green = Strong
  - ⚠️ Yellow = Medium
  - ❌ Red = Weak
- Bonus: Shows SHA256 hash of the entered password

For Usage:
bash
python checker.py


Example:
Enter a password: Hello123!

Strength: STRONG
Criteria passed:
 - length: ✅
 - lowercase: ✅
 - uppercase: ✅
 - digit: ✅
 - special: ✅

SHA256 hash: a592d23c4f56...
