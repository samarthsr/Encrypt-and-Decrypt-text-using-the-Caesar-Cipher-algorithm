def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around using modulo
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Non-alphabetic characters are unchanged
    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Perform the reverse shift and wrap around using modulo
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char  # Non-alphabetic characters are unchanged
    return decrypted_message

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Would you like to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice in ['E', 'D']:
            message = input("Enter your message: ")
            shift = int(input("Enter the shift value (0-25): "))
            if choice == 'E':
                encrypted = caesar_cipher_encrypt(message, shift)
                print(f"Encrypted message: {encrypted}")
            elif choice == 'D':
                decrypted = caesar_cipher_decrypt(message, shift)
                print(f"Decrypted message: {decrypted}")
        else:
            print("Invalid choice. Please choose E, D, or Q.")

if __name__ == "__main__":
    main()