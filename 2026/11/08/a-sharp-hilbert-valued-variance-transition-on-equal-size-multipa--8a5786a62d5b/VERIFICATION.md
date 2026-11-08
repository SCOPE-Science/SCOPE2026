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

Run `python3 check_hilbert_clusters.py` with the Python standard library. The program uses exact `fractions.Fraction` matrix entries and exact squared-distance/variance comparisons. It checks 288 explicit Gram witness instances and 1,200 independently generated nonexpansive sampled maps; it also compares the analytically predicted rank formulas for finitely many integer parameters.

Successful observed output:

```
EXACT_GRAM_WITNESSES_OK 288
EXACT_RANDOM_ADMISSIBLE_MAP_UPPER_BOUND_OK 1200
EXACT_CRITICAL_GRAM_RANKS_OK
ALL_CLUSTER_HILBERT_SPREAD_CHECKS_OK
```

The Gram matrices are positive semidefinite because the proof constructs them as sums of nonnegative multiples of centered orthogonal projection matrices. The checker itself tests exact entries, distances and variances rather than independently certifying positivity for arbitrary matrix dimensions. A finite enumeration is not a proof for all real distance parameters. The rigorous argument in `RESULT.md` provides the general theorem and equality conditions. No independent mathematical audit has been carried out.
