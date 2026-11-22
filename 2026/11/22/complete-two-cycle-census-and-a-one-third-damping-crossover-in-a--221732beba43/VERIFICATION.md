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

# Verification and reproducibility

The accompanying `verify.py` is standalone within this package and requires Python 3 and SymPy. Run `python verify.py` from the extracted directory. It performs an exact symbolic expansion of the two-step Jacobian determinant, substitutes the orbit product constraint and checks the claimed factorization. It then checks 16 exact rational reflected orbit constructions over four damping values, both nonlinearity signs and two coordinate orderings. It additionally tests the exact phase boundary and the ordering reversal at \(r=1/3\) for five rational damping values.

The mathematical proof in RESULT.md is universal over the stated parameter domain: it reduces all period-two solutions to the sum/product root condition and separately treats zero coordinates and both equal-square cases. The finite tests support algebraic reproducibility, and do not replace the universal proof or establish the absence of inaccessible equivalent literature. Numerical simulations, interval covering, and independent audit were not used or claimed.
