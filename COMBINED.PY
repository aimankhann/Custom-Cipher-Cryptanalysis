#combined script
from math import gcd

ALPHABET_SIZE = 26

# --- AFFINE CIPHER COMPONENTS ---
def mod_inverse(a, m=ALPHABET_SIZE):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for a={a} (mod {m})")

def validate_affine_key(a, b):
    if gcd(a, ALPHABET_SIZE) != 1:
        raise ValueError(f"Key 'a' ({a}) must be coprime with 26.")

def _shift_char(ch, func):
    if ch.isalpha() and ch.isascii():
        base = ord("A") if ch.isupper() else ord("a")
        return chr(func(ord(ch) - base) % ALPHABET_SIZE + base)
    return ch

def affine_encrypt(plaintext, a, b):
    validate_affine_key(a, b)
    return "".join(_shift_char(c, lambda x: a * x + b) for c in plaintext)

def affine_decrypt(ciphertext, a, b):
    validate_affine_key(a, b)
    a_inv = mod_inverse(a)
    return "".join(_shift_char(c, lambda y: a_inv * (y - b)) for c in ciphertext)

# --- VIGENÈRE CIPHER COMPONENTS ---
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

# --- TWO-STAGE COMBINED CIPHER ---
def custom_encrypt(plaintext, a, b, vig_key):
    """
    Stage 1: Affine Cipher (Substitution via linear transformation)
    Stage 2: Vigenère Cipher (Polyalphabetic substitution)
    """
    stage1 = affine_encrypt(plaintext, a, b)
    stage2 = vigenere(stage1, vig_key, decrypt=False)
    return stage2

def custom_decrypt(ciphertext, a, b, vig_key):
    """
    Stage 2 Reverse: Vigenère Decryption
    Stage 1 Reverse: Affine Decryption
    """
    stage1 = vigenere(ciphertext, vig_key, decrypt=True)
    stage2 = affine_decrypt(stage1, a, b)
    return stage2

# --- CLI INTERFACE ---
if __name__ == "__main__":
    print("=== Two-Stage Custom Cipher (Affine + Vigenère) ===")
    mode = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    text = input("Enter text: ")
    
    try:
        a = int(input("Enter Affine Key 'a' (coprime with 26): "))
        b = int(input("Enter Affine Key 'b': "))
        vig_key = input("Enter Vigenère Key (string): ").strip()
        
        # Enforce CCP Requirement: Key length >= 10
        total_key_len = len(str(a)) + len(str(b)) + len(vig_key)
        if total_key_len < 10:
            print(f"\n[Warning] Total key representation length ({total_key_len}) is under 10 chars.")
            print("Recommendation: Use a longer Vigenère keyword (e.g., 'CYBERSECURITY').")

        if mode == 'e':
            encrypted = custom_encrypt(text, a, b, vig_key)
            print("\nFinal Ciphertext:", encrypted)
        elif mode == 'd':
            decrypted = custom_decrypt(text, a, b, vig_key)
            print("\nFinal Plaintext:", decrypted)
        else:
            print("Invalid mode selected.")
    except Exception as err:
        print("Error:", err)