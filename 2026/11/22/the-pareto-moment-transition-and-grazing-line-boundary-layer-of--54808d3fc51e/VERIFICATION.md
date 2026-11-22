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

# Verification record

The proof is in `RESULT.md`. Run `python verify.py` to check the numerical reproduction of the exact chord-survival law against independently sampled offsets, both moment integrals against quadrature, and the finite-thickness scaling predictions. This script needs Python, SciPy and standard libraries and uses a fixed deterministic offset grid, not randomness.

At review, the script reported **PASS 115 deterministic checks**. The analytical proof, not the numerical count, supplies the infinite-domain statements. The one-dimensional elliptic reduction was additionally checked by algebraic integration by parts and high-precision numerical quadrature. No external/independent audit, formal proof assistant, or exhaustive certification was performed.
