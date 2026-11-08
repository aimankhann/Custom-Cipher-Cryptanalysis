
from combined import (
    affine_encrypt,
    affine_decrypt,
    vigenere,
    custom_encrypt,
    custom_decrypt
)

print("=" * 65)
print("       FUNCTIONAL TESTING - CLASSICAL CIPHER PROJECT")
print("=" * 65)

passed = 0
failed = 0


def check_test(name, condition):
    global passed, failed

    if condition:
        print("RESULT: PASS")
        passed += 1
    else:
        print("RESULT: FAIL")
        failed += 1


# TEST 1: AFFINE ENCRYPTION AND DECRYPTION
print("\nTEST 1: AFFINE CIPHER")

message = "HELLO WORLD"

encrypted = affine_encrypt(message, 5, 8)
decrypted = affine_decrypt(encrypted, 5, 8)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)

check_test("Affine", decrypted == message)


# TEST 2: VIGENERE ENCRYPTION AND DECRYPTION
print("\nTEST 2: VIGENERE CIPHER")

message = "HELLO WORLD"
key = "KEY"

encrypted = vigenere(message, key)
decrypted = vigenere(encrypted, key, decrypt=True)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)

check_test("Vigenere", decrypted == message)


# TEST 3: COMBINED ENCRYPTION AND DECRYPTION
print("\nTEST 3: COMBINED CIPHER")

message = "HELLO WORLD"
a = 5
b = 8
vig_key = "NETWORKINGKEY"

encrypted = custom_encrypt(message, a, b, vig_key)
decrypted = custom_decrypt(
    encrypted, a, b, vig_key
)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)

check_test("Combined", decrypted == message)


# TEST 4: INVALID AFFINE KEY
print("\nTEST 4: INVALID AFFINE KEY")

try:
    affine_encrypt("HELLO", 2, 8)
    invalid_key_rejected = False

except ValueError:
    invalid_key_rejected = True
    print("Invalid Affine key correctly rejected.")

check_test("Invalid Key Validation", invalid_key_rejected)


# TEST 5: SPACES AND CASE PRESERVATION
print("\nTEST 5: SPACES AND CASE PRESERVATION")

message = "Hello World!"
encrypted = custom_encrypt(message, 5, 8, "NETWORKINGKEY")
decrypted = custom_decrypt(
    encrypted, 5, 8, "NETWORKINGKEY"
)

print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)

check_test("Case and Spaces", decrypted == message)


# FINAL SUMMARY
print("\n" + "=" * 65)
print("                 FINAL TEST SUMMARY")
print("=" * 65)

print("Total Tests:", passed + failed)
print("Passed:", passed)
print("Failed:", failed)

if failed == 0:
    print("FINAL STATUS: ALL TESTS PASSED")
else:
    print("FINAL STATUS: SOME TESTS FAILED")

print("=" * 65)
