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

# Reproducible verification

Run `python3 verify_derangement_projection.py` with a standard Python 3 installation. It reconstructs all permutations in dimensions 3 through 7, constructs the exact rational nearest-point candidate, checks its row and column sums, diagonal constraints, entrywise nonnegativity, squared-distance identity, and exact row/column-potential inequalities on every available off-diagonal matrix entry. It checks all fixed-point shell counts via the inclusion-exclusion formula and the exact squared gap of 2 between the largest two permutation-vertex shells. The completed run printed:

```
DERANGEMENT_PROJECTION_PASS exhaustive_permutations= 5910 exact_KKT=PASS vertex_gap_squared=2
```

If NumPy and SciPy are installed, run `python3 independent_scipy.py` from the same directory. It computes numerical Euclidean projections using independent constrained optimization for 18 permutations covering all attainable fixed-point counts at orders 3 through 6 and checks 870 permutation singular-value bounds. The completed run printed:

```
INDEPENDENT_SLSQP_PASS cases 18 max_entry_error 4.55e-15
SPECTRAL_CHECKS_PASS permutations 870 singular_bounds=PASS nuclear_locus=PASS
```

The complete infinite-dimensional-family proof is the analytical feasibility and optimality certificate and the Schatten norm spectral inequality given in `RESULT.md`. These finite computations neither certify historical novelty nor constitute an independent mathematical audit. The spectral-norm farthest-point set beyond the identity is not classified.
