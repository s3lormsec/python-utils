import re

def check_password_strength(password):
    issues = []

    if len(password) < 8:
        issues.append("Password must be at least 8 characters long")

    if not re.search(r"[A-Z]", password):
        issues.append("Add at least one uppercase letter")

    if not re.search(r"[a-z]", password):
        issues.append("Add at least one lowercase letter")

    if not re.search(r"[0-9]", password):
        issues.append("Add at least one number")

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        issues.append("Add at least one special character")

    if issues:
        print("\nPassword is WEAK ❌")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("\nPassword is STRONG ✅")

if __name__ == "__main__":
    user_password = input("Enter a password to check: ")
    check_password_strength(user_password)

