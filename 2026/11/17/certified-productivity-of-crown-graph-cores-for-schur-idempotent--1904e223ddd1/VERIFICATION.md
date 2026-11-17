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

Run `python verify_schur_productivity.py schur_productive_certificate.json` using Python 3. The checker depends only on the standard library and reads both attached exact data and the reconstructed rational operator blocks. It checks the thirteen matrices' dimensions, integer entries and symmetry, bounds each matrix-square defect with rational arithmetic, and proves a rational strict lower bound greater than \(20029/10000\). It does not use a numerical eigensolver, an external package, random sampling, or a timeout to prove anything.

The graph-to-block identity and extension to every larger crown core are mathematical arguments in RESULT.md, not program assertions. A successful run verifies the finite premise needed by those arguments, rather than proving the external published reduction afresh. The independent audit status is not_performed.
