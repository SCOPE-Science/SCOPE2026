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

# Verification

`python general_parking_inball_checker.py` was run after writing the standalone checker, using available NumPy and SciPy. It returned:

```text
GENERAL_PARKING_INBALL_CHECKS_PASSED 150 104 explicit_rank2_radius 735.747765659393
```

The checker independently formulates all coordinate and upper-subset Euclidean containment constraints as a linear program, solving 150 seeded parameter cases with dimensions from 2 to 7. It also checks a rank-two eight-dimensional witness and 104 integer realizations of every individual rank in dimensions 2 through 14. Numerical tolerances are recorded in the checker; these computations are finite corroborations, not certificates of the universal theorem. The analytical proof derives the inradius, uniqueness, and rank realization for every integer parameter vector in scope.

No independent audit has been performed.
