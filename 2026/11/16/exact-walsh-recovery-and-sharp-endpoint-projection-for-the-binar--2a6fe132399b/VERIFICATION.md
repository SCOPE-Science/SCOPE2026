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
# Verification of the finite Fourier classification

The target is every rooted length-sixteen cyclic binary word with sixteen distinct four-bit factors. Both programs need only a standard C++17 compiler or Python 3 and no network or external datasets.

```
g++ -std=c++17 -O2 -Wall -Wextra check_debruijn4.cpp -o check
./check
python3 verify_debruijn4.py
```

The compiled checker independently enumerates every one of the \(2^{16}\) words, examines every one of the \(2^8\) feedback tables and its full state orbit, compares the two generated sets, performs the transform and directly checks all \(2^{16}\) character sums. It independently checks the complete signed histogram, Plancherel identity, modulo-sixteen divisibility, exact separation-dependent pair correlations, the Fourier-support projection-kernel absolute sum and kernel normalization.

The Python checker uses independent standard-library loops to generate all words, run the Walsh transform, and recompute each published finite invariant. The CSV histogram is provided solely as a readable certificate; no program assumes the CSV entries as input.

Executed outputs:

```
DEBRUIJN4_FOURIER_PASS rooted=256 feedback_rules=16 zeros=42022 rank=23514 gap=16 odd_zeros=32768 pair_zeros=48 projection_abs_sum=2520272 projection_denominator=65536
DEBRUIJN4_PY_PASS support=256 zero=42022 rank=23514 projection=157517/4096 signed_levels=12
```

All computations use exact signed integers. Integer loops over the stated complete finite domains certify the numerical result; they do not assert an infinite-family theorem. The assertion about the minimum among all real or complex linear projections also uses a separate mathematical argument: translation averaging reduces the problem to the unique Fourier-support projection.
