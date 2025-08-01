import string

def decode_shift(encrypted_message, shift_key):
    """Decodes a message encrypted with a shift cipher."""
    if not encrypted_message:
        return "Error: Encrypted message is empty."
    decoded_message = ""
    for char in encrypted_message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            # Modify the calculation for forward shift with positive key and backward with negative key
            decoded_char_code = (ord(char) - start - shift_key) % 26 + start
            decoded_message += chr(decoded_char_code)
        else:
            decoded_message += char
    return decoded_message

def decode_substitution(encrypted_message, substitution_key):
    """Decodes a message encrypted with a substitution cipher."""
    if not encrypted_message:
        return "Error: Encrypted message is empty."
    decoded_message = ""
    alphabet = string.ascii_lowercase
    substitution_key_lower = substitution_key.lower()
    for char in encrypted_message:
        if char.isalpha():
            is_lower = char.islower()
            char_lower = char.lower()
            try:
                index_in_key = substitution_key_lower.index(char_lower)
                original_char = alphabet[index_in_key]
                decoded_message += original_char if is_lower else original_char.upper()
            except ValueError:
                # Character not in the substitution key, keep it as is
                decoded_message += char
        else:
            decoded_message += char
    return decoded_message

def decode_vigenere(encrypted_message, vigenere_key):
    """Decodes a message encrypted with a Vigenère cipher."""
    if not encrypted_message:
        return "Error: Encrypted message is empty."
    if not vigenere_key:
        return "Error: Vigenère key cannot be empty."
    decoded_message = ""
    key_length = len(vigenere_key)
    key_index = 0
    for char in encrypted_message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            key_shift = ord(vigenere_key[key_index % key_length].lower()) - ord('a')
            # Modify for decoding in Vigenere
            decoded_char_code = (ord(char) - start - key_shift) % 26 + start
            decoded_message += chr(decoded_char_code)
            key_index += 1
        else:
            decoded_message += char
    return decoded_message

def encode_shift(message, shift_key):
    """Encodes a message with a shift cipher."""
    encoded_message = ""
    for char in message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            encoded_char_code = (ord(char) - start + shift_key) % 26 + start
            encoded_message += chr(encoded_char_code)
        else:
            encoded_message += char
    return encoded_message

def encode_substitution(message, substitution_key):
    """Encodes a message with a substitution cipher."""
    encoded_message = ""
    alphabet = string.ascii_lowercase
    substitution_key_lower = substitution_key.lower()
    for char in message:
        if char.isalpha():
            is_lower = char.islower()
            char_lower = char.lower()
            try:
                index_in_alphabet = alphabet.index(char_lower)
                substituted_char = substitution_key_lower[index_in_alphabet]
                encoded_message += substituted_char if is_lower else substituted_char.upper()
            except ValueError:
                # Character not in the alphabet, keep it as is
                encoded_message += char
        else:
            encoded_message += char
    return encoded_message

def encode_vigenere(message, vigenere_key):
    """Encodes a message with a Vigenère cipher."""
    encoded_message = ""
    key_length = len(vigenere_key)
    key_index = 0
    for char in message:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            key_shift = ord(vigenere_key[key_index % key_length].lower()) - ord('a')
            encoded_char_code = (ord(char) - start + key_shift) % 26 + start
            encoded_message += chr(encoded_char_code)
            key_index += 1
        else:
            encoded_message += char
    return encoded_message


def get_user_input():
    """Prompts the user for encode/decode, cipher type, key(s), and message."""
    while True:
        mode = input("Do you want to 'encode' or 'decode' a message? ").lower().strip()
        if mode in ['encode', 'decode']:
            break
        else:
            print("Invalid choice. Please enter 'encode' or 'decode'.")

    while True:
        cipher_type = input("Enter the type of cipher (shift, substitution, or Vigenère): ").lower().strip()
        if cipher_type in ['shift', 'substitution', 'vigenere']:
            break
        else:
            print("Invalid cipher type. Please enter 'shift', 'substitution', or 'Vigenère'.")

    key = None
    if cipher_type == 'shift':
        while True:
            try:
                key_input = input("Enter the shift key (an integer): ").strip()
                key = int(key_input)
                break
            except ValueError:
                print("Invalid input. Please enter an integer for the shift key.")
    elif cipher_type == 'substitution':
        while True:
            key = input("Enter the substitution key (a 26-letter string with no repeating characters): ").strip()
            if len(key) == 26 and len(set(key.lower())) == 26 and key.isalpha():
                key = key.lower()
                break
            else:
                print("Invalid substitution key. Please enter a 26-letter string with no repeating characters.")
    elif cipher_type == 'vigenere':
        while True:
            key = input("Enter the Vigenère key (a string): ").strip()
            if key.isalpha() and key:
                key = key.lower()
                break
            else:
                print("Invalid Vigenère key. Please enter a string containing only letters and not empty.")

    message = input(f"Enter the message to {mode}: ").strip()

    return mode, cipher_type, key, message

def main():
    """Main function to handle the encoding/decoding process."""
    while True:
        mode, cipher_type, key, message = get_user_input()

        print(f"\nMode: {mode}")
        print(f"Cipher Type: {cipher_type}")
        print(f"Key: {key}")
        print(f"Message: {message}")

        result_message = ""
        if mode == 'encode':
            if cipher_type == 'shift':
                result_message = encode_shift(message, key)
            elif cipher_type == 'substitution':
                result_message = encode_substitution(message, key)
            elif cipher_type == 'vigenere':
                result_message = encode_vigenere(message, key)
        elif mode == 'decode':
            if cipher_type == 'shift':
                result_message = decode_shift(message, key)
            elif cipher_type == 'substitution':
                result_message = decode_substitution(message, key)
            elif cipher_type == 'vigenere':
                result_message = decode_vigenere(message, key)

        print(f"\nResulting Message: {result_message}")

        another_message = input(f"\nDo you want to {mode} another message? (yes/no): ").lower().strip()
        if another_message != 'yes':
            break

main()
