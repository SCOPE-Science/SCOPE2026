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

# Verification

The analytic identity and uniqueness proof appear in RESULT.md. Run `python check/verify_hermite.py` using SymPy and SciPy. Its exact checks cover the upper contact, full factorization, positivity of the remaining quadratic through discriminant \(-16\), stationarity and unique weight. Numerical cross-checks independently integrate the centered ambiguity kernels at ten specified non-axis-aligned or axis points and evaluate twenty thousand deterministic radial/weight samples. Numerical checks are not proofs of the global bound. No independent validation has been performed.
