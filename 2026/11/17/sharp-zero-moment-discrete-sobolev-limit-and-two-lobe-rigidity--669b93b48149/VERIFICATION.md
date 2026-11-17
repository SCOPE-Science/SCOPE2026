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

# Reproducibility and limits

The symbolic, all-dimension proof is in `RESULT.md`; no external proof service or unverified infinite enumeration is required. Running `python3 checker.py` in the directory containing the files reproduces 3,037 exact rational assertions: witness equations and masses for 30 even dimensions, exhaustive finite sign-dual comparisons at sizes 2 through 10, and 2,869 exact Dirichlet Green inverse entries at sizes 2 through 20. These checks test normalization and algebra, but are not a substitute for the infinite-dimensional compactness or sharpness arguments. A separate independent mathematical audit has not been performed.
