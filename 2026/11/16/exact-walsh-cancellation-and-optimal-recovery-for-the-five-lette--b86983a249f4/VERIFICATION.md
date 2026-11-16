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

# Reproducing the exact order-five spectral census

The packaged standalone programs are `check_even_permutation_walsh.py` (Python 3 standard library) and `check_even_permanent.cpp` (ISO C++17). They independently evaluate the entire 65,536-member gauge-reduced domain, with no data files or stochastic sampling.

Run from this directory:

```sh
python3 check_even_permutation_walsh.py
g++ -O2 -std=c++17 check_even_permanent.cpp -o check_even_permanent
./check_even_permanent
```

The Python program constructs the sixty even permutation-incidence masks, performs the sixteen-bit Walsh transform, verifies the complete ten-level absolute-value census, checks Parseval and the projection norm, and separately checks all 25-coordinate frequency supports of size at most three, including exactly 400 vanishing length-three paths.

The C++ program independently enumerates all 120 permutations and computes the integer permanent and determinant for each gauge-reduced sign matrix; it uses their half-sum to check the ten-level spectrum, Parseval and the projection-kernel absolute sum. Both use an integer butterfly only for the final projection-norm step.

Observed outputs include `rank=27758592`, `nullity=5795840`, minimum positive multiplier magnitude 4, projection absolute-kernel sum 4,265,776, and exact norm \(266611/4096\). Computation is finite and exhaustive only at this order; it cannot validate a higher-order formula. No independent external mathematical audit was undertaken.
