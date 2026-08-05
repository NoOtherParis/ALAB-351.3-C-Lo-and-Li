# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Convert the sentence to uppercase
print(f"Uppercase: {sentence.upper()}")

# Print the sentence in reverse
print(f"Reversed: {sentence[::-1]}")

# Count the vowels
vowel_count = 0

for letter in sentence:
    if letter.lower() in "aeiou":
        vowel_count += 1

print(f"Vowel Count: {vowel_count}")

# Replace spaces with hyphens
print(f"Hyphenated: {sentence.replace(' ', '-')}")


def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")


try:
    age = int(input("Enter your age: "))
    validate_age(age)
    print("Age accepted.")

except ValueError as error:
    print("Error:", error)