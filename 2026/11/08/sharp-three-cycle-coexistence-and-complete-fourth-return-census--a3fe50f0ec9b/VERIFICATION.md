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

# Exact verification

Run `python verify_coexistence.py` with Python 3.9 or later. The standalone script has no external dependencies and uses `fractions.Fraction` for every arithmetic operation.

Its full loop enumerates all sixteen branch words of length four. For each word it constructs the exact affine fourth-return matrix and displacement, solves the invertible two-dimensional fixed-point equation, and checks all four strict branch signs and the return equality. It checks pairwise distinct roots, all six cyclic necklace classes, their exact determinants, and the least-period distribution \(2,2,12\). The three nontrivial necklace classes have their reported exact monodromy traces and determinants independently checked, and the \(LRRR\) Schur inequalities are checked without floating-point tolerances.

A successful replay prints:

```
EXACT_16_WORD_CENSUS_OK
PERIODS_2_2_12_OK
MONODROMY_AND_HYPERBOLICITY_OK
```

The analytic proof in `RESULT.md` establishes the universal bound on isolated strict period-four orbits and the open-neighborhood persistence. A finite symbolic computation alone cannot prove those global parameter statements. The verifier does not investigate or certify periodic orbits of higher period, arbitrary branch-border degeneracies, or the global attractor. No independent audit was performed.
