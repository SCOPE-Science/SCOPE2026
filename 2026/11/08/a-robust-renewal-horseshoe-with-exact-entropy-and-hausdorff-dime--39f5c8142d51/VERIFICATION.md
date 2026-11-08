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
# Verification evidence

`verify.py` uses only Python's standard library and exact rational interval arithmetic for all theorem-critical coefficient and itinerary inequalities on the entire parameter square. It checks exact central/end-point return identities for both words, the adjacency-matrix relation, and prints numerical values of the uniquely defined spectral/dimension roots. Run from the extracted package using `python3 verify.py`.

Scientific limits: This does not perform a global census of all planar invariant sets or certify the entropy of the full attractor. The algebraic dimension and entropy formulas depend on the analytic coding and standard theorems stated in `RESULT.md`. No external independent validation is asserted.
