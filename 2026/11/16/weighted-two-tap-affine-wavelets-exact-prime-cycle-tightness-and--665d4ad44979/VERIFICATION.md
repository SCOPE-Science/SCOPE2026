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

# Reproducible mathematical checks
Execute `python3 verify_wavelet_two_tap.py` with Python 3 and its standard library only. The script builds Fourier multipliers from two-tap vectors, exhausts unweighted and small integer-weighted scale assignments, independently checks one actual time-coordinate frame matrix, and checks exact scale-erasure extrema for six primes.

Completed program checks: 6,624 unweighted cases at primes \(3,5,7,11\), 4,896 weighted cases at primes \(3,5,7\), time-coordinate matrix for \(p=7\), and erasure boundaries at primes \(3,5,7,11,13,17\). The final program assertion prints `TWO_TAP_AFFINE_PASS unweighted_cases=6624 weighted_cases=4896`.

The proof does not depend on finite computation: it is the finite Fourier inversion argument plus the exact antipodal equations. Numerical floating-point tests have rounding tolerance and do not independently certify results for all primes or weights. No independent mathematical audit has been performed.
