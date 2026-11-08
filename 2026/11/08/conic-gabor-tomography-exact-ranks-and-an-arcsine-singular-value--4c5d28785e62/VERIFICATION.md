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

# Reproduction and limits

Run `python3 checks/verify.py` with Python 3 and NumPy. The program checks norm-one conic sizes and all shift overlaps in four prime fields, directly enumerates full ambiguity coefficients and rank for each, and checks the predicted singular values against the direct lifting SVD when the field order is three. Recorded output:

```text
p=3 conic_size=4 shift_support=9 pair_counts={1: 4, 2: 4, 4: 1} Gabor_rank=81 nullity=0
p=5 conic_size=4 shift_support=9 pair_counts={0: 16, 1: 4, 2: 4, 4: 1} Gabor_rank=225 nullity=400
p=7 conic_size=8 shift_support=33 pair_counts={0: 16, 1: 8, 2: 24, 8: 1} Gabor_rank=1617 nullity=784
p=11 conic_size=12 shift_support=73 pair_counts={0: 48, 1: 12, 2: 60, 12: 1} Gabor_rank=8833 nullity=5808
CONIC_GABOR_AMBIGUITY_RANK_CHECKS_OK
DIRECT_COMPLEX_LIFTING_SVD_OK
```

The direct enumeration and SVD comparisons use floating-point tolerances. The mathematical proof of all-prime nonvanishing is exact via cyclotomic irreducibility and odd-order root structure. Weak convergence is analytic, not numerically inferred. The zero-shift Fourier magnitudes have not been individually evaluated. No external independent validation has been conducted.
