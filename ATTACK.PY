#attack script
from combined import custom_encrypt, custom_decrypt

def known_plaintext_attack(sample_plaintext, sample_ciphertext, dictionary_keys):
    """
    Brute-forces the 312 possible Affine key pairs (12 valid 'a' values * 26 'b' values)
    and checks against candidate Vigenère keys from a list.
    """
    valid_a = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
    print("[*] Initiating Known-Plaintext Attack...")

    for a in valid_a:
        for b in range(26):
            for vig_key in dictionary_keys:
                try:
                    test_cipher = custom_encrypt(sample_plaintext, a, b, vig_key)
                    if test_cipher == sample_ciphertext:
                        print(f"[+] KEY RECOVERED! Affine(a={a}, b={b}), Vigenere Key='{vig_key}'")
                        return a, b, vig_key
                except Exception:
                    continue

    print("[-] Attack failed to recover key.")
    return None

if __name__ == "__main__":
    # Test scenario
    secret_msg = "NETWORKSECURITY"
    a, b, vig_key = 5, 8, "NETWORKINGKEY" # Total key chars >= 10
    
    cipher = custom_encrypt(secret_msg, a, b, vig_key)
    print(f"Original: {secret_msg}")
    print(f"Ciphertext: {cipher}\n")
    
    # Simulate attacker key recovery
    possible_vig_keys = ["PASS", "CYBER", "NETWORKINGKEY", "ADMIN"]
    known_plaintext_attack(secret_msg, cipher, possible_vig_keys)