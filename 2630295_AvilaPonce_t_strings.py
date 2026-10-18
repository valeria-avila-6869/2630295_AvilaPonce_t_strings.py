"""
Manejo de strings en Python
2630295
Valeria Alejandra Avila Ponce
I M1-2
"""

def problem_1_full_name_formatter():
    # Normalize a full name, remove extra spaces, format it in Title Case,
    # and display the initials separated by periods.
    # Inputs: full_name (string; may contain mixed case and extra spaces).
    # Outputs: Formatted name and initials.
    # Validations: Name must not be empty and must contain at least two words.
    # Test cases:
    # "Valeria Alejandra Avila Ponce" ->  "Valeria Alejandra Avila Ponce", "V.A.A.P"
    # Borde: valeria avila -> "Valeria Avila", "V.A."
    # Error: -> "  " ' name cannot be empty' 
     full_name = input("Enter your full name: ")
    cleaned_name = " ".join(full_name.strip().split())

    if not cleaned_name:
        print("Error: name cannot be empty")
        return

    name_parts = cleaned_name.split()
    if len(name_parts) < 2:
        print("Error: enter at least two words")
        return

    formatted_name = cleaned_name.title()
    initials = "".join(part[0].upper() + "." for part in name_parts)
    print(f"Formatted name: {formatted_name}")
    print(f"Initials: {initials}")


def problem_2_simple_email_validator():
    # Check a basic email structure and display its domain when valid.
    # This is a simple classroom check, not a complete email-standard validator.
    # Inputs: email_text (string).
    # Outputs: "Valid email: true/false"; domain when valid.
    # Problema: estructura + dominio 
    # Entradas: email_text
    # Non-empty, exactly one '@', no whitespace, non-empty local/domain
    # parts, and at least one dot after '@'.
    # Test cases:
    # 'valeriaavila@upv.com' -> valid
    # Error: 'valeria.com' -> invalid
  email_text = input("Enter an email address: ").strip()

    if not email_text:
        print("Error: email cannot be empty")
        print("Valid email: false")
        return

    at_count = email_text.count("@")
    at_position = email_text.find("@")
    has_whitespace = any(character.isspace() for character in email_text)

    if at_count != 1 or has_whitespace:
        print("Valid email: false")
        return

    local_part = email_text[:at_position]
    domain_part = email_text[at_position + 1:]

    if not local_part or not domain_part or "." not in domain_part:
        print("Valid email: false")
        return

    if domain_part.startswith(".") or domain_part.endswith("."):
        print("Valid email: false")
        return

    print("Valid email: true")
    print(f"Domain: {domain_part}")


def problem_3_palindrome_checker():
    # Determine whether text reads the same forward and backward, ignoring
    # spaces and letter case. Punctuation is not removed by this version.
    # Inputs: phrase (string).
    # Outputs: normalized phrase and palindrome result.
    # Validations: Phrase must not be empty and must contain at least 3
    # non-space characters.
    # Test cases:
    # Normal: "Vale lava la tina" -> true
    # Border: "ale" -> true
    # Error: "  " -> error
    phrase = input("Enter a phrase: ").strip()

    if not phrase:
        print("Error: phrase cannot be empty")
        return

    normalized_phrase = phrase.lower().replace(" ", "")
    if len(normalized_phrase) < 3:
        print("Error: enter at least 3 non-space characters")
        return

    print(f"Normalized phrase: {normalized_phrase}")
    print(f"Is palindrome: {str(normalized_phrase == normalized_phrase[::-1]).lower()}")

def problem_4_sentence_word_stats():
     # Test cases:
    # 1) Normal: "Python strings are useful" -> count 4; shortest "are"; longest "strings"
    # 2) Border: "  Hello  " -> count 1; first/last/shortest/longest "Hello"
    # 3) Error: "   " -> "Error: sentence cannot be empty"
    sentence = input("Enter a sentence: ").strip()

    if not sentence:
        print("Error: sentence cannot be empty")
        return

    words = sentence.split()
    if not words:
        print("Error: sentence must contain at least one word")
        return

    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    print(f"Word count: {len(words)}")
    print(f"First word: {words[0]}")
    print(f"Last word: {words[-1]}")
    print(f"Shortest word: {shortest_word}")
    print(f"Longest word: {longest_word}")


def problem_5_password_strength_classifier():
    # Classify a password as weak, medium, or strong using the rules below.
    # Rules: weak if shorter than 8 characters; strong if length >= 8 and
    # it contains uppercase, lowercase, digit, and non-alphanumeric symbol;
    # medium if length >= 8 but does not meet all strong requirements.
    # Password_input (string).
    # Outputs: password strength.
    # Validations: Password must not be empty.
    # Ejemplo:
    # "Vale123!" -> strong
    # "abcdefgh" -> medium
    # "  " -> "Error: password cannot be empty"
    password_input = input("Enter a password: ")

    if not password_input:
        print("Error: password cannot be empty")
        return

    has_upper = any(character.isupper() for character in password_input)
    has_lower = any(character.islower() for character in password_input)
    has_digit = any(character.isdigit() for character in password_input)
    has_symbol = any(not character.isalnum() for character in password_input)

    if len(password_input) < 8:
        strength = "weak"
    elif has_upper and has_lower and has_digit and has_symbol:
        strength = "strong"
    else:
        strength = "medium"

    print(f"Password strength: {strength}")



def problem_6_product_label_formatter():
 # Build a product label containing the product name and price. The final
    # label must contain exactly 30 characters, padded with spaces or truncated.
    #
    # Inputs: product_name (string), price_value (text convertible to a positive number).
    # Outputs: label of exactly 30 characters.
    # Validations: Product name cannot be empty; price must be numeric and positive.
    # Test cases:
    # Name "Notebook", price "25.50" -> a 30-character label
    # Name "P", price "1" -> padded to 30 characters
    # Error: name "Pen", price "-2" -> invalid price
    product_name = input("Enter product name: ").strip()
    price_text = input("Enter product price: ").strip()

    if not product_name:
        print("Error: product name cannot be empty")
        return

    try:
        price_number = float(price_text)
    except ValueError:
        print("Error: price must be a number")
        return

    if price_number <= 0:
        print("Error: price must be positive")
        return

     # Preserve the user's price representation after validating its numeric value.
    label = f"Product: {product_name} | Price: ${price_text}"
    label = label[:30]  # Keep only the first 30 characters if the label is too long.
    label = label.ljust(30)  # Add trailing spaces if the label is shorter than 30.
    print(f'Label: "{label}"')
    print(f"Label length: {len(label)}")


def main():
    print("STRING TOOLS")
    print("1. Full name formatter")
    print("2. Simple email validator")
    print("3. Palindrome checker")
    print("4. Sentence word stats")
    print("5. Password strength classifier")
    print("6. Product label formatter")
    choice = input("Choose a problem (1-6): ").strip()

    problem_functions = {
        "1": problem_1_full_name_formatter,
        "2": problem_2_simple_email_validator,
        "3": problem_3_palindrome_checker,
        "4": problem_4_sentence_word_stats,
        "5": problem_5_password_strength_classifier,
        "6": problem_6_product_label_formatter,
    }

    selected_problem = problem_functions.get(choice)
    if selected_problem is None:
        print("Error: invalid choice. Select a number from 1 to 6.")
        return
    selected_problem()


if __name__ == "__main__":
    main()

"""
# CONCLUSIONS

# String handling is essential when programs receive or display text.
# strip() removes leading and trailing whitespace, while lower() helps
# compare text without case differences.
# split() separates text into a list of words, and join() combines strings.
# Normalizing text before comparison reduces errors caused by extra spaces
# or inconsistent capitalization.
# Clear validations stop empty or malformed data before it is processed.
# Strings are immutable, so methods create new strings rather than changing
# the original string; slicing is useful for extracting or limiting text.

 REFERENCES
 1) Python Software Foundation. Built-in Types: Text Sequence Type — str.
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
 2) Python Software Foundation. Built-in Functions.
    https://docs.python.org/3/library/functions.html
 3) Python Software Foundation. Errors and Exceptions.
    https://docs.python.org/3/tutorial/errors.html
 4) Python Software Foundation. An Informal Introduction to Python.
    https://docs.python.org/3/tutorial/introduction.html
 5) Python Software Foundation. More on Defining Functions.
    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
"""