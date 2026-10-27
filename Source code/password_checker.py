"""
Password Strength Checker
Educational project: evaluates a password against five basic criteria.
Do not enter or store a real password when demonstrating this project.
"""

import string


def analyze_password(password):
    """Return a dictionary showing whether each password rule is satisfied."""
    checks = {
        "Length (at least 8 characters)": len(password) >= 8,
        "Uppercase letter (A-Z)": any(char.isupper() for char in password),
        "Lowercase letter (a-z)": any(char.islower() for char in password),
        "Number (0-9)": any(char.isdigit() for char in password),
        "Special character": any(
            char in string.punctuation for char in password
        ),
    }

    passed = sum(checks.values())

    if passed == 5:
        strength = "STRONG"
    elif passed >= 3:
        strength = "MODERATE"
    else:
        strength = "WEAK"

    return checks, strength


def display_analysis(password):
    checks, strength = analyze_password(password)

    print("\nPassword Analysis:")
    for rule, satisfied in checks.items():
        status = "Satisfied" if satisfied else "Not satisfied"
        mark = "✓" if satisfied else "✗"
        print(f"  {mark} {rule}: {status}")

    print(f"\nPassword Strength: {strength}")


def main():
    print("=" * 34)
    print("     PASSWORD STRENGTH CHECKER")
    print("=" * 34)
    print("Educational demo only. Do not enter a real password.")
    print("Type 'exit' to quit.")

    while True:
        try:
            password = input("\nEnter a sample password: ")
        except (EOFError, KeyboardInterrupt):
            print("\nThank you! Goodbye!")
            break

        if password.lower() == "exit":
            print("Thank you! Goodbye!")
            break

        if not password:
            print("Please enter a sample password.")
            continue

        display_analysis(password)

        again = input("\nCheck another sample password? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you! Goodbye!")
            break


if __name__ == "__main__":
    main()
