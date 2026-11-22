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

# Reproducibility and mathematical verification

The exact theorem is proved in `RESULT.md` through an exhaustive classification of the radial pair cases followed by the tree-edge transport identity. The finite computation is corroborative rather than a substitute for that proof.

Run from the directory containing `check_tree.py` using `python check_tree.py` with Python 3, NumPy, and SciPy. The program enumerates 3,960 center/radius instances of generated finite ultrametrics, verifies all center-cost pair distances against an independently built radial tree, tests the four-point condition, and compares two independently specified optimal transportation linear programs per instance with the subtree imbalance expression. It also verifies that a specific four-point ordinary line does **not** admit a tree pseudometric representation for the corresponding localized cost. All tests passed at numerical tolerance \(10^{-7}\) or better.

The argument uses exact algebra and finite-tree flow conservation, so no computation claims to prove the theorem beyond tested sizes. Publication-priority coverage is limited by available indexed sources. No independent external mathematical audit or validation has been performed.
