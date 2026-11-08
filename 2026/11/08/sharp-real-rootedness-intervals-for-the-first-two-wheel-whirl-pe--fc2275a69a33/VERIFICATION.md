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

# Reproduction

Use `python wheel_whirl_sturm_check.py` with Python 3 and SymPy installed. The checker performs independent direct lattice-count/transfer-matrix comparisons, the generating-function binomial transform, exact polynomial discriminants, exact rational Sturm real-root counts for the parameter discriminant and for the three sample polynomials, and endpoint-isolation tests.

The analytical step not reducible to finite sample checking is the constancy of the number of simple negative roots on parameter intervals free of discriminant zeros, combined with constant leading and constant terms and the positive-coefficient necessity for negative roots. This step is proved in RESULT.md.

All inputs are exact rationals or integers; displayed endpoint decimals are not used for root certification. The conclusion concerns the polynomial pencil, not realization as polytopes away from its endpoints. Independent mathematical audit has not been performed.
