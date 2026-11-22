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

The derivation is self-contained in RESULT.md. The standard-library `verify.py` performs a finite exact-rational consistency check, not infinite or automated proof certification. Run `python verify.py` with Python 3; expected output reports 36,044 exact-rational assertions and a strict rational bracket around the unique positive cubic root. The key mathematical certificate is the symbolic failure derivative factorization and the exact endpoint-versus-midpoint identity in RESULT.md, not the test count.

The probability model assumes four independent corridor events and the specified rational success law. The unique-root classification uses Descartes' sign rule and explicit signs at the boundaries. No physical data, experiments, or external independent audit are asserted. Classical resource-allocation literature accessible only by abstract remains a historical-priority limitation.
