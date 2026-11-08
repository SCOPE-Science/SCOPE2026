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

# Reproducibility

Run `python verify.py` with Python 3.8 or later. The script builds each crown graph directly using its bipartition and deleted diagonal and performs independent union-find acyclicity tests for every selected vertex subset. It checks inclusion maximality by attempting to add every omitted vertex, then compares the literal counts and structural types with the theorem's polynomial coefficients.

Observed checks: graph orders 4, 5, 6, 7, and 8; 87,296 labelled subsets exhaustively inspected, with 32, 70, 132, 224, and 352 maximal forests respectively. Their all-forest counts are 189, 478, 1,102, 2,425, and 5,227. Checks of exact coefficient identities also cover 146 larger integer parameters.

The unrestricted conclusion follows from the mathematical proof, not from finite tests. No independent audit has been performed.
