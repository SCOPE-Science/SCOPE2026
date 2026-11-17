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

The bundled `verify_hypercube_gini.py` was executed with Python 3 and SymPy/NumPy and returned:

```
SYMBOLIC_ALL_13_CUBE_ORBITS_EXACT_DOMAINS_PASS
ALL_BINARY_CUTS_D1_TO_D3_EXACT_RATIONAL_PASS
DIMENSION4_ALL_CUTS_NUMERICAL_TESTS_PASS
HYPERCUBE_GINI_CHECKS_PASS
```

The symbolic test checks the 13 complete symmetry/complement classes of nontrivial three-bit cuts, their exact interior ordering thresholds, and the full parameter-interval inequalities needed for the dimension-three norm. Rational tests enumerate all cuts in dimensions 1, 2 and 3 at six distinct parameters. Four-bit numerics are corroboration only and are not used to prove the theorem in arbitrarily high dimension. The high-dimensional cutoff and single-site Gaussian limit are established analytically by the comparisons and limit theorems in the proof. No independent audit has been conducted.
