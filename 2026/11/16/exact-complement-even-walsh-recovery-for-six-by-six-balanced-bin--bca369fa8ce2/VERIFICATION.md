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

# Reproduction of the exact finite claim

1. Compile `check_spectrum.cpp` with `g++ -O3 -std=c++17 check_spectrum.cpp -o check_spectrum` and run `./check_spectrum`. Uses only the C++17 standard library and no floating point.
2. Run `python check_spectrum.py` with Python 3 and NumPy installed. It enumerates columns rather than rows and applies its own exact-integer vectorized 25-axis transform. The array needs approximately 410 MB peak working memory.

Actual recorded checks, successfully rerun from these files:

```text
tables=297200 characters=33554432 zeros=16777216 all_even_residue=16_mod_32 min_nonzero=16 first_min_frequency=36045 parseval=9972377190400 PASS
tables=297200 characters=33554432 zeros=16777216 all_even_residue=16_mod_32 min_nonzero=16 PASS
```

The scripts check every reduced Fourier multiplier; neither asserts an infinite-size theorem. The reported exact values are verified by assertions, not inferred from these printed lines alone. The source codes themselves and their defined finite loops provide the reproducible evidence. The full 36-coordinate assertion follows by the proved row/column frequency-gauge symmetry. Independent external mathematical audit has not been performed.
