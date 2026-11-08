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
# Reproducible checks and scientific limits

Run the embedded `verification/check.py` with Python 3 and SymPy installed. It performs: exact symbolic reconstruction of the period-two Jacobian trace, determinant, Schur factor, and fixed-point flip eigenvalue; rational verification of the explicit two-cycle; an exact-rational interval certificate for its attracting multipliers using the positive arctanh series for log 2; 491 parameter samples with high-precision bisection roots of the defining cycle equation; and three small-excess threshold tests of the square-root law.

Observed output from the packaged checker prior to embedding:

```text
VERIFY_OK symbolic_identities=5 exact_rational_witness=8 numerical_two_cycles= 491 attracting_witness=1
```

The exact mathematical proof is in RESULT.md. Finite checks cannot establish the infinite, all-parameter quantifiers; they are supplemental and do not provide independent certification. The \(r=1/3\) stability boundary and higher periods remain outside the claim.
