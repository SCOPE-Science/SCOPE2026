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

# Reproducibility and evidence

Run `python3 verification/verify.py` with Python 3 standard library from the extracted artifact package. The checker performs exact rational-polynomial identities for the root-derived residue formulas, constructs the degree-12 Bernstein coefficient array from the original polynomial, and checks that all 13 entries are strictly positive (minimum \(7443/78125\)). It reproduces the exact isolated-step resonance \(r=3\) through numerical index 100 and rational first-negative witnesses at \(r=1,2,4\).

The check completes with `VERIFY_OK` when every test passes. The root-discriminant argument and the infinite-rotation sign proof are human-readable analytic arguments in RESULT.md and are not inferred by finite enumeration. Historical novelty remains conditional on inspected source coverage. Independent validation and independent mathematical audit have not been performed.
