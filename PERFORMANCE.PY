
import time
import statistics

from combined import (
    affine_encrypt,
    affine_decrypt,
    vigenere,
    custom_encrypt,
    custom_decrypt
)

# MESSAGE SIZES
MESSAGE_SIZES = [100, 1000, 10000, 100000]

# NUMBER OF REPETITIONS
REPEATS = 5

# ENCRYPTION KEYS
A = 5
B = 8
VIG_KEY = "NETWORKINGKEY"


def measure_time(function):
    """Measure function execution time in seconds."""

    start = time.perf_counter()
    function()
    end = time.perf_counter()

    return end - start


def benchmark(name, encrypt_func, decrypt_func, message):

    # WARM-UP RUN
    ciphertext = encrypt_func(message)
    decrypted = decrypt_func(ciphertext)

    # VERIFY CORRECTNESS
    if decrypted != message:
        raise ValueError(name + " encryption/decryption failed!")

    encryption_times = []
    decryption_times = []

    # REPEATED MEASUREMENTS
    for i in range(REPEATS):

        enc_time = measure_time(
            lambda: encrypt_func(message)
        )

        dec_time = measure_time(
            lambda: decrypt_func(ciphertext)
        )

        encryption_times.append(enc_time)
        decryption_times.append(dec_time)

    # CALCULATE AVERAGE
    avg_encryption = statistics.mean(encryption_times)
    avg_decryption = statistics.mean(decryption_times)

    return avg_encryption, avg_decryption


def main():

    print("=" * 85)
    print("          PERFORMANCE ANALYSIS OF CLASSICAL CIPHERS")
    print("=" * 85)

    algorithms = {

        "Affine": (
            lambda msg: affine_encrypt(msg, A, B),
            lambda cipher: affine_decrypt(cipher, A, B)
        ),

        "Vigenere": (
            lambda msg: vigenere(msg, VIG_KEY),
            lambda cipher: vigenere(
                cipher, VIG_KEY, decrypt=True
            )
        ),

        "Combined": (
            lambda msg: custom_encrypt(
                msg, A, B, VIG_KEY
            ),
            lambda cipher: custom_decrypt(
                cipher, A, B, VIG_KEY
            )
        )
    }

    print("\nMessage sizes:", MESSAGE_SIZES)
    print("Repetitions per operation:", REPEATS)
    print("Warm-up runs: 1 per operation")

    for size in MESSAGE_SIZES:

        message = "A" * size

        print("\n")
        print("-" * 85)
        print("MESSAGE LENGTH:", size, "characters")
        print("-" * 85)

        print(
            f"{'Algorithm':<15}"
            f"{'Encryption (ms)':<23}"
            f"{'Decryption (ms)':<23}"
        )

        for name, functions in algorithms.items():

            encrypt_func, decrypt_func = functions

            enc_avg, dec_avg = benchmark(
                name,
                encrypt_func,
                decrypt_func,
                message
            )

            print(
                f"{name:<15}"
                f"{enc_avg * 1000:<23.6f}"
                f"{dec_avg * 1000:<23.6f}"
            )

    print("\n")
    print("=" * 85)
    print("PERFORMANCE TESTING COMPLETED SUCCESSFULLY")
    print("All encryption/decryption correctness checks passed.")
    print("Average calculated from", REPEATS, "measurements.")
    print("=" * 85)


if __name__ == "__main__":
    main()
