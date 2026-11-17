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

# Reproducibility and verification

Run `python verify_weighted_isotonic.py` with Python 3 and no additional dependencies. The script uses `fractions.Fraction` for every verified equality and inequality. It enumerates all consecutive-block partitions for \(2\le n\le7\) over nine rational mass/weight profiles per order; checks step-basis operator norms against the closed chord formula; verifies that the exact mass-coordinate concavity inequalities characterize nonexpansivity; independently computes the least-concave-majorant formula; and checks each constructed local strictly pooled ratio through an exact weighted PAV solver.

Observed output:
```
EXACT_ALL_BLOCK_PARTITION_NORMS_PASSED 54
EXACT_ALL_ACTIVE_BLOCK_WITNESSES_PASSED 1134
EXACT_MASS_AWARE_CONCAVITY_EQUIVALENCE_PASSED
LINEAR_TIME_LEAST_CONCAVE_MAJORANT_FORMULA_PASSED
ALL_WEIGHTED_ISOTONIC_VARIATION_CHECKS_PASSED
```
The full real-parameter theorem uses the mathematical proof in `RESULT.md`. Finite verification does not certify the unrestricted theorem or bibliographic originality. No independent audit has been performed.
