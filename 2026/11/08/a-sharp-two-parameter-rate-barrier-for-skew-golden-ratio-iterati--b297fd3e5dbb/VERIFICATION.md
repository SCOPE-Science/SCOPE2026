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

The analytic proof in `RESULT.md` derives the two-step recurrence from the published algorithm, reduces to the two characteristic quadratics, proves the elementary disk-root inequality, and gives an exact nonnegative decomposition ruling out spectral radius below \(1/\sqrt2\). Equality is completely classified.

Run `python verify.py` using Python 3, SymPy, and NumPy. In the assembled package this script produced: 1,309 exact rational parameter checks, 9,120 numerical spectral-root comparisons, 20 checks of the six-dimensional real-rotation recurrence, and symbolic identities of the factorization, characteristic polynomial and compatible initialization. These finite diagnostics do not replace the parameter-uniform proof.

The result is for a real skew-isometry and exact arithmetic, not for arbitrary monotone operators, variable steps, nontrivial proximal terms or finite-precision implementations. Independent external verification has not been performed.
