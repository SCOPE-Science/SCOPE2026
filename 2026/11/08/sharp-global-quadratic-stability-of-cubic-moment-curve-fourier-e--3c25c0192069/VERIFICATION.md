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

## Reproducibility
Run `python3 CHECK.py` using Python 3 with no additional dependencies. This performs 276 exact-rational probability-vector checks for symbol counts \(5,7,11\), each comparing explicit ordered-triple rearrangements with the cubic power-sum formula, verifying the exact nonnegative remainder. It also performs eight direct complex finite-field Fourier sixth-moment comparisons for primes \(5,7\).

Successful execution prints:

`CHECK_OK exact_probability_vectors= 276 direct_Fourier_tests= 8 cases= [(5, 126, 'point_mass,uniform'), (7, 84, 'point_mass'), (11, 66, 'point_mass')]`

These are finite tests, not a proof for infinitely many fields. The infinite theorem uses character orthogonality, Newton's power-sum identities in characteristic greater than three, the exact three-draw rearrangement polynomial, and classical normalized Newton inequalities. The sharpness witness is the point-mass probability vector. The target Fourier norm uses counting measure; the curve measure is normalized. No independent audit has been performed.
