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

# Mathematical verification

The accompanying `verify.py` runs with only Python 3's standard library. It independently reconstructs the Gini/order-statistic covariance and both variances using exact rational covariance matrices, and independently reconstructs affine conditional means by enumerating five disjoint pair types (lower-lower, upper-upper, lower-upper, lower-pivot, upper-pivot). Across every sample size from 2 through 60 and every allowable order-statistic rank it compares these calculations with the displayed formulas, including the explained-variance fraction.

For sizes from 2 through 600, it computes the integer score at all ranks, verifies exactly the nearest-square rank-set characterization, and checks whether four-way ties coincide with solutions of the Pell equation. It also checks the recurrence and explicit tie-rank sets for sizes 9, 57, and 337. The executed checker reported `PASS: 12775 exact rational, integer optimization, and Pell checks`.

These finite checks do not certify the full theorem. General correctness rests on the conditional uniform-group decomposition, exact Dirichlet spacing covariance, scalar quartic optimization and classical Pell descent. Source comparisons and self-review do not replace independent mathematical audit.
