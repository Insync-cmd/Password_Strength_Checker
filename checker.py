import re
import hashlib
from colorama import Fore, Style, init

# Initialize colorama (for Windows support too)
init(autoreset=True)

def check_password_strength(password: str) -> dict:
    """Check strength of a password and return details."""
    
    criteria = {
        "length": len(password) >= 8,
        "lowercase": bool(re.search(r"[a-z]", password)),
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special": bool(re.search(r"[^A-Za-z0-9]", password)),
    }

    score = sum(criteria.values())

    if score <= 2:
        strength = "WEAK"
        color = Fore.RED
    elif score in (3, 4):
        strength = "MEDIUM"
        color = Fore.YELLOW
    else:
        strength = "STRONG"
        color = Fore.GREEN

    return {
        "strength": strength,
        "criteria": criteria,
        "color": color
    }


def hash_password(password: str) -> str:
    """Return SHA256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()


if __name__ == "__main__":
    pwd = input("Enter a password: ")
    result = check_password_strength(pwd)

    # Strength (colored)
    print(f"\nStrength: {result['color']}{result['strength']}{Style.RESET_ALL}")

    # Criteria check
    print("Criteria passed:")
    for key, value in result["criteria"].items():
        mark = "✅" if value else "❌"
        print(f" - {key}: {mark}")

    # Bonus: show SHA256 hash
    print(f"\nSHA256 hash: {hash_password(pwd)}")
