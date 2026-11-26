---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and verification

The expansion in `RESULT.md` is analytic. The two harmonic quantities are differences of ordinary harmonic sums and reciprocal-square tails. Expanding those differences by Euler–Maclaurin and substituting \(2\lfloor n/2\rfloor\) gives the coefficients and the remainder without numerical extrapolation.

The supplied `verify_fejer_bv.py` can be used with Python 3, NumPy and SciPy. Its `PARITY_THIRD_ORDER_ASYMPTOTIC_CHECKS_PASS` check uses the finite Fourier expression at six degrees and is only a finite numerical check. The other sections concern the first-moment and arc background and numerical discrete inputs; none establishes the all-degree expansion or the scope of originality. No formal verification or expert attestation is claimed.
