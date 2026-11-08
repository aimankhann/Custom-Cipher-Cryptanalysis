"""Affine cipher: encryption and decryption.

Encrypt: E(x) = (a*x + b) mod 26
Decrypt: D(y) = a_inv * (y - b) mod 26
where a must be coprime with 26 and a_inv is the modular inverse of a.
"""

from math import gcd

ALPHABET_SIZE = 26


def mod_inverse(a, m=ALPHABET_SIZE):
    """Return the modular multiplicative inverse of a mod m."""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for a={a} (mod {m})")


def validate_key(a, b):
    if gcd(a, ALPHABET_SIZE) != 1:
        raise ValueError(
            f"Key 'a' ({a}) must be coprime with 26. "
            "Valid values: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25"
        )


def _shift_char(ch, func):
    """Apply func to a letter's 0-25 index, preserving case; leave others unchanged."""
    if ch.isalpha() and ch.isascii():
        base = ord("A") if ch.isupper() else ord("a")
        return chr(func(ord(ch) - base) % ALPHABET_SIZE + base)
    return ch


def encrypt(plaintext, a, b):
    validate_key(a, b)
    return "".join(_shift_char(c, lambda x: a * x + b) for c in plaintext)


def decrypt(ciphertext, a, b):
    validate_key(a, b)
    a_inv = mod_inverse(a)
    return "".join(_shift_char(c, lambda y: a_inv * (y - b)) for c in ciphertext)


if __name__ == "__main__":
    print("=== Affine Cipher ===")
    choice = input("Encrypt or Decrypt? (e/d): ").strip().lower()
    text = input("Enter text: ")
    try:
        a = int(input("Enter key a (coprime with 26): "))
        b = int(input("Enter key b: "))
        if choice == "e":
            print("Ciphertext:", encrypt(text, a, b))
        elif choice == "d":
            print("Plaintext:", decrypt(text, a, b))
        else:
            print("Invalid choice. Enter 'e' or 'd'.")
    except ValueError as err:
        print("Error:", err)