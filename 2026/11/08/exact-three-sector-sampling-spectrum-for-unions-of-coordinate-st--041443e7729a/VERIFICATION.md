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

# Reproducible finite checks and proof boundary

Run `python3 verify.py` with Python 3 (only the standard library is needed). The script builds the restricted first-harmonic Gram form on the entire Johnson slice independently of the closed spectrum formulas, by computing exact coordinate inclusion probabilities for every pair. Every comparison uses `fractions.Fraction` and `math.comb`, not floating-point tolerances.

At the time of review, the actual run produced:

```
EXACT_ALL_FIRST_BAND_SECTORS_OK 165 ties 4 O_smaller 10 M_smaller 151
SINGLETON_SLICE_RANK_BOUNDARY_OK
```

For all integer triples \(5\le n\le13\), \(3\le t\le n-2\), and \(2\le k\le n-t\), the script checks exact action on both within-block zero-sum sectors and the mixed sector, all cross-sector products, strictly positive small eigenvalues, and the exact eigenvalue-ordering criterion. It also checks the adjacent \(k=1\) boundary separately, where outside-coordinate modes vanish under the spatial mask.

This finite verification **does not** establish the theorem in untested dimensions. The all-parameter proof is the inclusion-probability calculation, orthogonal sector decomposition, lost-mass formulas, and exact factorization given in `RESULT.md`. The fixed-density and fixed-\(k,t\) limits follow from explicit finite products and rational expansions, not from computer sampling. No independent audit, external mathematical certification or computer-assisted infinite proof is claimed.
