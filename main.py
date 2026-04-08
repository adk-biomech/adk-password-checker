import re

def check_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Use at least 8 characters")

    # Uppercase & lowercase
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        score += 2
    else:
        feedback.append("Include both uppercase and lowercase letters")

    # Numbers
    if re.search("[0-9]", password):
        score += 2
    else:
        feedback.append("Add at least one number")

    # Special characters
    if re.search("[@#$%^&*]", password):
        score += 2
    else:
        feedback.append("Include a special character (@#$%^&*)")

    # Bonus for longer passwords
    if len(password) >= 12:
        score += 2

    # Strength rating
    if score >= 8:
        strength = "Strong"
    elif score >= 5:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, score, feedback


def main():
    print("=== ADK Password Strength Checker ===")

    while True:
        password = input("\nEnter a password (or type 'exit' to quit): ")

        if password.lower() == "exit":
            print("Exiting... 👋")
            break

        strength, score, feedback = check_password(password)

        print(f"\nStrength: {strength}")
        print(f"Score: {score}/10")

        if feedback:
            print("Suggestions:")
            for tip in feedback:
                print(f"- {tip}")
        else:
            print("Great password. No suggestions needed.")


if __name__ == "__main__":
    main()
