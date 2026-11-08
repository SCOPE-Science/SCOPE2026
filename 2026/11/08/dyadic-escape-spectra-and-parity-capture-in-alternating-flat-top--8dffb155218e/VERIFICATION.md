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

Run `python3 verify_markov.py` with Python 3.9 or later. It uses only the Python standard library and exact fractions. Expected messages:

```
DYADIC_ALTERNATING_TENT_EXACT_MARKOV_AND_CHARPOLY_OK parameters=22 cells_checked= 198
DIRECT_GRID_CYLINDER_LENGTHS_OK independent_comparisons= 24
```

The first part checks the forward-invariant endpoint sets, all affine images and retained-cell transitions, characteristic polynomials using exact integer matrix traces, and critical-orbit capture for parameter indices \(1\) through \(22\). The second part is an independently coded full rational cylinder-grid enumeration for indices \(1\) through \(6\), depths \(1\) through \(4\), compared with the transfer-matrix length formula.

The proof for every integer parameter is the indexed boundary/transition argument and Perron eigenvalue elimination in RESULT.md. Finite computations do not constitute an exhaustive proof of infinitely many parameters; numerical simulation is not used to justify dimension or asymptotic estimates. No independent mathematical audit has been performed. 
