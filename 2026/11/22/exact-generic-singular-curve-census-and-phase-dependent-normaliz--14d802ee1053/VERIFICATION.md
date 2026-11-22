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

Proof: see `RESULT.md`, including finite normalization, all sign subsets, connectedness and distinctness, differential-rank exhaustiveness, transverse tangent normals, and symmetric-phase fixed-point analysis.

Run `python check_example.py` with SymPy to reproduce the exact nine-curve slice check for weights \( (1,1,2) \) and phase \(\lambda=2\). This computation is a consistency check only, not an exhaustive proof of arbitrary weights. No independent external audit has been performed.
