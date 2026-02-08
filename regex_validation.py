import re

# ---------- Email Validation ----------
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.fullmatch(pattern, email)


# ---------- Mobile Number Validation (India) ----------
def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'
    return re.fullmatch(pattern, phone)


# ---------- Password Validation ----------
def validate_password(password):
    """
    Rules:
    - Minimum 8 characters
    - At least 1 uppercase
    - At least 1 lowercase
    - At least 1 digit
    - At least 1 special character
    """
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.fullmatch(pattern, password)


# ---------- Main Program ----------
def main():
    email = input("Enter Email: ").strip()
    phone = input("Enter Mobile Number: ").strip()
    password = input("Enter Password: ").strip()

    if not email or not phone or not password:
        print("❌ Input cannot be empty")
        return

    print("\n--- Validation Results ---")

    if validate_email(email):
        print("✅ Email is valid")
    else:
        print("❌ Invalid Email format")

    if validate_phone(phone):
        print("✅ Mobile number is valid")
    else:
        print("❌ Invalid Mobile number")

    if validate_password(password):
        print("✅ Password is strong")
    else:
        print("❌ Weak Password")


if __name__ == "__main__":
    main()
