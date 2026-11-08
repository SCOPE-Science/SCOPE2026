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

Run `python3 verify.py` with Python 3. The exact-rational tests cover the explicit dyadic resonances and nonresonant finite-time formula, and exercise strict two-versus-two mean chambers. Seeded finite random tests are only diagnostics. Infinite claims use the elementary affine-ratio argument and the rank-loss invertibility proof in RESULT.md; no finite computation is being promoted to proof. Mathematical limitations: no floating-point terminal guarantee, no assertion for matrix size other than four singular modes.
