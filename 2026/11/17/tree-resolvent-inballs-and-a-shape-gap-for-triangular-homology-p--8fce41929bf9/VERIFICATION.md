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

Use Python 3 with NumPy and execute `python verify_homology_tree.py`. The script constructs genuine signed triangle-boundary matrices of tree-glued triangulations, verifies the Euclidean Gram identities, computes exact rational inverses for path sizes 1 through 10, exhaustively compares facet-normal squared norms for small path sizes, checks path closed forms, and checks complete-binary formulas for heights 0 through 6. The recorded output is `PASS 2258 checks`. The all-dimensional result depends on the proof in RESULT.md, not these finite tests. No independent audit has been performed.
