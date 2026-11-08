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

# Reproduction of finite checks

Run `python verify.py` with Python 3 and no external dependencies from the directory holding the paper and code. The checker builds explicit Paley graphs at prime orders 5, 13, 17 and 29 and the 3-by-3 rook graph of order 9 (the nine-vertex conference case). Each has the prescribed strongly regular parameters. It compares direct rational Gauss--Jordan inversion of the actual Radau IIA matrix with all three closed-form entry classes at eight rational timestep values per graph, checks row sums and local Laplacian-square identities, and performs 1,000 additional parameter identity/sign checks.

The observed completion message was:

```
PASS: 40 exact matrix inversions, 11240 exact entry identities, 300 exact cutoff witnesses, 700 additional diagonal identities.
```

The argument for infinitely many parameter values is algebraic and is given in `RESULT.md`. The finite checker cannot establish a root-count theorem, novelty, or independent validation. The use of direct inversion confirms the normalization of the completed end-step matrix and checks the critical entry-type formulas on concrete graphs; it is not a computer-assisted proof of the unrestricted theorem.
