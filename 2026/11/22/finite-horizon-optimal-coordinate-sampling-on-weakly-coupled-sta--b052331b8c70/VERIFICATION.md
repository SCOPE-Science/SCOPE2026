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

Run `python artifacts/verify_horizon.py` with Python 3, NumPy and SciPy available. It reproduces exact-rational full-matrix update recurrences, compares independently constructed original-coordinate and energy-coordinate expected-energy forms, checks the exact two-step projection polynomial, and tests the predicted small-coupling coefficient for several leaf counts and horizons. The recorded execution reported **PASS: 534 exact rational/matrix and numerical asymptotic assertions**.

The exact analytical proof concerns every integer leaf count at least two and every fixed positive finite horizon; no finite list of examples proves that all-size statement. The recurrence identities, Taylor expansion, Perron simple-eigenvalue convexity and compactness of the probability simplex are the proof-critical ingredients. No formal proof assistant or independent human audit was used.
