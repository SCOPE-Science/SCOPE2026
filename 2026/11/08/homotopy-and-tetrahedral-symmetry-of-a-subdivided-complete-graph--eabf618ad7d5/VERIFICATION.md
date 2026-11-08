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

Run `python3 verify.py` from this directory with standard Python 3. The file independently derives the twelve vertices of the truncated-tetrahedral graph and all 163 independent faces, constructs 78 finite acyclic Morse pairs, checks the full 432-cover directed Hasse graph by topological sorting, and computes augmented mod-two boundary ranks. It then evaluates all 24 signed permutation Lefschetz numbers and checks that each tetrahedral permutation preserves a nonempty independent face. The recorded exact output in `verification_output.txt` is:

```
ALL_VERIFY_OK faces=163 nonempty=162 pairs=78 critical=(1,0,5,0) covers=432
BOUNDARY_RANKS (1, 11, 37, 30)
S4_CLASS_CHARS {'(1, 1, 1, 1)': 5, '(2, 1, 1)': -1, '(2, 2)': 1, '(3, 1)': 2, '(4,)': 1}
GROUP_ELEMENTS=24 FIXED_POINT_ELEMENTS=24 QUOTIENT_RANKS_S4=1_A4=2
```

The topology conclusion uses the exhaustive acyclic matching and Forman's theorem, not a conjecture inferred from homology ranks. Character equality uses the augmented simplicial Lefschetz formula and rational semisimplicity; quotient fundamental groups use the orbit-space theorem, and quotient rational homology uses finite-group transfer. No computational experiment establishes a statement about larger graph orders. An independent mathematical audit has not been performed.
