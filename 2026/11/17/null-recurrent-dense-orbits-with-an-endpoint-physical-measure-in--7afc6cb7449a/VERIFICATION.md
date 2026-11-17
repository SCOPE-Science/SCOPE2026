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

# Reproducible finite checks and analytical boundaries

Execute `python3 CHECK.py` with the Python standard library from the same directory. The script reconstructs exact vertex sequences for source blocks \(0\) through \(100\), and its output is

```
VERIFY_OK direct_branch_counts=101 invariant_balance=101 reversible_edges=101 harmonic_ruin_boundaries=99 finite_path_depth=4
```

This checks transition multiplicities, normalization, detailed balance, stationary Perron transfer, gambler's-ruin harmonic functions with finite ceiling \(2\le L\le100\), and finite Markov path probabilities through depth four. Computations use exact rational arithmetic and contain no tolerance-based acceptance. The code and its results are evidence for algebraic identities in the tested finite range, not an exhaustive proof over all states or an independent audit. The mathematical proof gives those unrestricted identities by direct formulas and establishes recurrence, infinite return-time mean, almost-everywhere time averages and dense orbits using exact Markov and renewal arguments. No external validation or certification is asserted.
