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

# Verification of the exact five-solid projection-volume spectrum

Run `python3 verify_platonic.py` with SymPy, NumPy and SciPy available. The local execution completed successfully and printed `PLATONIC_PROJECTION_OK minor_spectra=20+120 hull_vertices=64+1024 ratios=5`. The program reconstructs all six and ten antipodal normal pairs from explicit golden-ratio coordinates, enumerates each of the 20 and 120 unordered triples exactly, checks every algebraic determinant class, computes the two projection-body volumes, and verifies all five scale-free ratios. It then evaluates independent convex-hull volumes from the 64 and 1024 signed sums as a floating-point corroboration. The hand-checkable determinant multiplicity tables and normalization are in RESULT.md; the numeric hull check is not the proof. No independent audit or generalized inequality certification was performed.
