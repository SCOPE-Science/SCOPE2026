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

# Verification notes

The mathematical proof uses support functions, an exact common-tangent face decomposition and convex-hull normalization; it verifies all positive real semiaxes and every pair of real input vectors. The exact contact witnesses are \(e=(a^2,b^2)/\sqrt{a^2+b^2}\), \(f=(b^2,a^2)/\sqrt{a^2+b^2}\).

Run `python scripts/check.py` from this package root to reproduce fixed-seed numerical and exact-rational diagnostic assertions. Sampling is not a proof and does not claim exhaustiveness or verification beyond the checked cases. An independent audit has not been performed.
