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

# Reproduction and limits

Use Python 3 with SymPy installed, then run `python check.py` in the same directory. The program uses exact rational matrices and exact principal minors, not numerical eigenvalue tolerance. It independently constructs the signed Hessian in a mean-zero basis for all tested single-bridge graphs. It checks the strict theorem, including rational samples on both sides and the equality boundary, and displays computed path/clique thresholds.

The finite run produced:
```
path 2 R=0 threshold=2
path 4 R=1/2 threshold=4/3
path 6 R=10/9 threshold=None
path 8 R=7/4 threshold=None
path 10 R=12/5 threshold=None
barbell 4 R=1/2 threshold=4/3
barbell 6 R=4/9 threshold=18/35
barbell 8 R=3/8 threshold=16/65
barbell 10 R=8/25 threshold=50/357
barbell 12 R=5/18 threshold=36/403
PASS: exact positive-definiteness and threshold on 388 bridge graph cases; finite tests only
```

The unrestricted assertion relies on the energy minimization and rank-one Schur complement in `RESULT.md`, not on the checker. The two-block partition is not claimed to be an invariant *two-dimensional cluster manifold*: only the specified antipodal orbit is an exact equilibrium. Equality at the sharp threshold is linearly nonhyperbolic and no nonlinear stability classification is asserted. No independent mathematical audit has been performed.
