import secrets
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_chars=True):
lowercase_chars = string.ascii_lowercase
uppercase_chars = string.ascii_uppercase if include_uppercase else ''
number_chars = string.digits if include_numbers else ''
special_chars = string.punctuation if include_special_chars else ''

all_characters = lowercase_chars + uppercase_chars + number_chars + special_chars

if not all_characters:
raise ValueError("You must select at least one character set for the password.")

password = []

if include_uppercase:
password.append(secrets.choice(uppercase_chars))
if include_numbers:
password.append(secrets.choice(number_chars))
if include_special_chars:
password.append(secrets.choice(special_chars))

password += [secrets.choice(all_characters) for _ in range(length - len(password))]

secrets.SystemRandom().shuffle(password)

return ''.join(password)

if __name__ == "__main__":
print("Welcome to the Random Password Generator!")
desired_length = int(input("Enter desired password length (8-20): "))

if desired_length < 8 or desired_length > 20:
print("Please choose a length between 8 and 20.")
else:
generated_password = generate_password(length=desired_length)
print(f"\nGenerated Password: {generated_password}")

