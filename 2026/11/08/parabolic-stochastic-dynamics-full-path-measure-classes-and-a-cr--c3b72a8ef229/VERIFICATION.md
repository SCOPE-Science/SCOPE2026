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

# Reproducibility and proof limits

The standalone `checker.py` was run from its packaged directory using the standard Python interpreter; execution terminated successfully with:

```
PARABOLIC_EXACT_ITERATE_RATIONAL_OK
FINITE_DEFECT_COUPLING_BOUND_OK
LIKELIHOOD_SECOND_MOMENT_BOUND_OK
TRIANGULAR_CRITICAL_WINDOW_MEAN_VARIANCE_OK
PARABOLIC_MARKOV_PATH_CHECK_OK
```

The checker verifies exact rational iterations at \(\gamma=1\) and numerical spot checks for the mean-value coupling bound, the conditional likelihood second-moment identity, and crossover means/variances. Each check is finite. The independent-coordinate equivalence, almost-sure eventual coupling, singularity classification and limit theorems are mathematical conclusions of the proof in `RESULT.md`, not automated certifications.

The identity between the nonlinear operator and transition matrices follows the explicit row construction in Souissi–Mukhamedov (2024), Section 3. The comparison with existing sufficient summability conditions uses Jamilov et al. (2024), Section 4. The full paper texts were inspected; a general search cannot eliminate every unpublished or unindexed equivalent theorem. The item has not received independent mathematical validation.
