---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

All arithmetic is exact. The supplied Python program enumerates every parking tuple in the five asserted lengths, reduces the character-count polynomial modulo the relevant cyclotomic polynomial, and inspects each sorted frequency multiset with its full multinomial orbit size. It generates `parking5_frequency_orbits.csv` with all 252 orbit representatives. Its output ends `PARKING_SIXTH_ROOT_FIRST_EXTRA_ZERO_PASS`.

The independent C++17 program directly evaluates all 7776 length-five frequencies by summing 1296 preference terms, reducing sixth roots to integer pairs and checking vanishing. It reproduces the five exceptional symmetry types, 360 additional zeros, 1295 forced zeros and rank 6121. Its output ends `PARKING5_DIRECT_CHARACTER_PASS`.

Use `python3 check_parking.py` and `g++ -O2 -std=c++17 check_direct.cpp -o check_direct && ./check_direct`. The computation has a finite exhaustive domain and does not rely on probabilistic sampling, numerical Fourier approximations, or mathematical independence claims. Independent external audit has not been performed.
