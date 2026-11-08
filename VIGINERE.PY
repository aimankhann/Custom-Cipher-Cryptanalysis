def vigenere(text, key, decrypt=False):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key[key_index % len(key)]) - ord('A')
            if decrypt:
                shift = -shift
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char

    return result


def main():
    while True:
        mode = input("\nEncrypt, Decrypt or Exit? (e/d/x): ").strip().lower()

        if mode == "x":
            print("Goodbye!")
            break

        if mode not in ("e", "d"):
            print("Error: enter 'e' to encrypt, 'd' to decrypt, or 'x' to exit.")
            continue

        text = input("Enter the word or sentence: ")
        key = input("Enter the key: ").strip()

        if not key.isalpha():
            print("Error: key must contain letters only (no spaces, digits or symbols).")
            continue

        if mode == "e":
            print("Encrypted Message:", vigenere(text, key))
        else:
            print("Decrypted Message:", vigenere(text, key, decrypt=True))


if __name__ == "__main__":
    main()