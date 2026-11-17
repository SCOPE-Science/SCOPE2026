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

# Reproducible verification

Run `python3 check_three_zone.py` using Python 3 with no third-party dependencies. It reconstructs a published CCC example in exact rational arithmetic, verifies the four outer and central energy identities over a quadratic extension, checks positive transverse speeds and the nonunit return derivative, and compares the reversed-time case. Output confirms `THREE_ZONE_HAMILTONIAN_RATIONAL_CERTIFICATE_OK`. The numerical multiplier values are diagnostics only. The infinite-parameter theorem is proved in RESULT.md by exact Hamiltonian matching and sign analysis; no sampled calculation is offered as an infinite proof. Full independent mathematical audit is not performed.
