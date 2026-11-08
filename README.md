# Two-Stage Custom Cipher (Affine + Vigenère)

Complex Computing Problem for **Network and Information Security (CT-486)**, NED University of Engineering & Technology, Karachi.

A custom product cipher that chains two classical ciphers, with a known-plaintext attack, a test suite and a performance benchmark. Written in pure Python 3 with no external dependencies.

## How it works

| Stage | Cipher | Operation |
|-------|--------|-----------|
| 1 | Affine | `E(x) = (a·x + b) mod 26`, with `gcd(a, 26) = 1` |
| 2 | Vigenère | `C_i = (P_i + K_(i mod m)) mod 26` |

- **Encryption:** Plaintext → Affine → Vigenère → Ciphertext
- **Decryption:** Ciphertext → Vigenère⁻¹ → Affine⁻¹ → Plaintext
- **Key:** `(a, b, keyword)`. Example: `a = 5`, `b = 8`, keyword `NETWORKINGKEY` (13 letters, meets the ≥ 10 character requirement).
- Letter case is preserved. Spaces, digits and punctuation are left unchanged.

**Example:** `HELLO WORLD` → `EGEHO FKXYD`

## Project structure

| File | Purpose |
|------|---------|
| `vigenere.py` | Standalone Vigenère cipher (CLI) |
| `affine.py` | Standalone Affine cipher with key validation (CLI) |
| `combined.py` | Two-stage custom cipher (CLI), imported by the other scripts |
| `attack.py` | Known-plaintext attack simulation |
| `testing.py` | Functional test suite (5 tests) |
| `performance.py` | Encryption/decryption benchmark |

## Usage

Requires Python 3.8 or newer.

```bash
python combined.py      # encrypt / decrypt with the custom cipher
python affine.py        # Affine cipher only
python vigenere.py      # Vigenère cipher only
python attack.py        # run the known-plaintext attack
python testing.py       # run functional tests
python performance.py   # run benchmarks
```

Sample session (`python combined.py`):

```
=== Two-Stage Custom Cipher (Affine + Vigenère) ===
Encrypt or Decrypt? (e/d): e
Enter text: HELLO WORLD
Enter Affine Key 'a' (coprime with 26): 5
Enter Affine Key 'b': 8
Enter Vigenère Key (string): NETWORKINGKEY

Final Ciphertext: EGEHO FKXYD
```

Valid values of `a`: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25. Any other value is rejected.

## Known-plaintext attack

`attack.py` brute-forces all 312 Affine pairs (12 values of `a` × 26 values of `b`) against a dictionary of candidate Vigenère keywords, re-encrypting the known plaintext until it matches the known ciphertext.

- Test: `NETWORKSECURITY` → `IGSKOGQCPYOTUMC`
- Result: key recovered (`a = 5`, `b = 8`, `NETWORKINGKEY`) after 243 of 1,248 trials.
- Limitation: it only succeeds if the keyword is in the dictionary. A dictionary-free attack is also possible and is described in the report.

## Testing

`testing.py` runs 5 tests: Affine round trip, Vigenère round trip, combined round trip, invalid key rejection, and case/space preservation. Result: **5/5 passed**.

## Performance

Average of 5 runs, `a = 5`, `b = 8`, key `NETWORKINGKEY`. Time in milliseconds.

| Length | Affine enc / dec | Vigenère enc / dec | Combined enc / dec |
|--------|------------------|--------------------|--------------------|
| 100 | 0.26 / 0.68 | 0.23 / 0.24 | 0.44 / 0.50 |
| 1,000 | 4.97 / 3.75 | 3.55 / 4.05 | 6.33 / 8.64 |
| 10,000 | 21.86 / 23.74 | 16.22 / 14.28 | 45.38 / 58.22 |
| 100,000 | 174.80 / 151.16 | 97.71 / 114.29 | 269.82 / 338.12 |

All operations run in linear time, O(n). The combined cipher costs roughly the sum of its two stages.

## Security notes

- The nominal key space is 12 × 26 × 26^13 ≈ 2^69, but `b` merges into the Vigenère key, so the effective key space is about 2^65.
- Both stages work letter by letter, so the cipher is still periodic and can be broken with Kasiski examination or the index of coincidence.
- **Not secure for real data.** This project is for learning only. Use a modern cipher such as AES-GCM in practice.
- Suggested improvements: add a transposition stage (e.g. Rail Fence), use an autokey Vigenère, use longer random keys, and remove spaces and punctuation before encryption.

## Report

The full report (design, algorithms, attack, results, security and complexity analysis) is in `NIS_CCP_Report.pdf`.

## Authors

| Name | Roll No. |
|------|----------|
| Umme Aiman Khan | CR-23003 |
| Nisa Fatima | CR-23024 |
| Musfirah | CR-23003 |
| Nabiha | CR-23048 |

Submitted to Dr Shariq Mehmood Khan.
