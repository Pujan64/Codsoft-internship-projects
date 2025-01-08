
import random

def generate_password(length):
    # Alphabet pool for password generation
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    password = ""

    # Generate a random password of the specified length
    for _ in range(length):
        next_letter_index = random.randrange(len(alphabet))
        password += alphabet[next_letter_index]

    # Add numbers and uppercase letters for complexity
    password = replace_with_number(password)
    password = replace_with_uppercase_letter(password)
    
    return password


def replace_with_number(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password) // 2)
        password = password[:replace_index] + str(random.randrange(10)) + password[replace_index + 1:]
    return password


def replace_with_uppercase_letter(password):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(password) // 2, len(password))
        password = password[:replace_index] + password[replace_index].upper() + password[replace_index + 1:]
    return password


def main():
    print("Password Generator")
    print("Minimum password length should be 3.")
    
    length = int(input("Enter the desired length of your password: "))
    if length < 3:
        print("Password length too short. Setting it to the minimum value of 3.")
        length = 3

    # Generate the password
    password = generate_password(length)
    print(f"Your generated password is: {password}")


if __name__ == "__main__":
    main()