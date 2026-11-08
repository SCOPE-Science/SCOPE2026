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

Run `python3 verify_crown_ld.py` using Python 3 standard library. It constructs the graph from the definition \(a_i b_j\in E\iff i\ne j\), enumerates every selected subset, verifies all outside-vertex signatures directly, and compares observed coefficients with both formulas. Minimality is checked by deleting each individual selected vertex. This is conclusive for finite orders because the locating-dominating property is upward-closed, so every strictly smaller code would yield a valid one-vertex deletion.

Observed independent code output:

```
n=4: candidate_subsets=256, locating_dominating=149, inclusion_minimal=56
n=5: candidate_subsets=1024, locating_dominating=588, inclusion_minimal=72
n=6: candidate_subsets=4096, locating_dominating=2103, inclusion_minimal=182
n=7: candidate_subsets=16384, locating_dominating=7178, inclusion_minimal=436
n=8: candidate_subsets=65536, locating_dominating=23913, inclusion_minimal=1010
n=9: candidate_subsets=262144, locating_dominating=78552, inclusion_minimal=2288
VERIFY_OK orders=4..9 subsets=349440 LD_sets=112483 minimal=4044 characterization=PASS minimal_families=PASS both_polynomials=PASS
```

The brute-force verification checks only \(4\le n\le9\); the unrestricted result uses the signature criterion and a combinatorial argument, not extrapolation. Independent audit has not been performed.
