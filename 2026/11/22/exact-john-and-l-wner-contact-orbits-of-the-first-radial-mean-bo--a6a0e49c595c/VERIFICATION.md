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

# Verification of exact radial contacts

Run `python3 verify.py` beside `RESULT.md`. The script uses only the Python standard library and prints `CUBE_R1_EXACT_CONTACT_CHECKS_OK` if all exact and independent checks succeed. It verifies the values of \(H^2\) at the interior stationary point, axial endpoint, body-diagonal endpoint and relevant edge critical point; checks the exact rational gap \(31/729\); and checks the gradient and edge-derivative factorizations over rational sample points. It independently integrates the original covariogram, rather than the closed polynomial form, over \(160\) deterministic unit directions using composite Simpson quadrature and checks the error against the closed formula.

These are finite consistency checks, not an exhaustive proof for uncountably many directions. The global argument consists of the exact sign of \(D-S\), factorization of interior stationarity, and complete boundary critical-point analysis in `RESULT.md`. Classical convexity and uniqueness of John–Löwner ellipsoids are used as identified, not independently reproved. Independent mathematical audit remains unperformed.
