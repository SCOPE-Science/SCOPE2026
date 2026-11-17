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

# Reproducibility verification

The proof is self-contained in `RESULT.md`: the independent Poisson nearest-offset representation, redundancy criterion, exponential Laplace products, and exhaustive mixed-event combinatorics are the critical analytic steps.

Run `python checks/verify.py` from the root of this artifact bundle after installing `numpy>=1.24` from `checks/requirements.txt`. The checker performed exact rational evaluation at equal rates; 900,000 simulated exponential-gap configurations over three rate triplets; and a separate halfplane-vertex reconstruction for 15,000 cells. All comparisons satisfied the programmed tolerances, including the exact rate-one four-atom formula.

Expected final diagnostics:

`EXACT_FOUR_TYPE_PROBABILITIES_OK`

`DIRECT_GEOMETRIC_15000_SAMPLES_OK`

`ALL_ZERO_CELL_DIAGNOSTICS_OK`

Monte Carlo deviations are finite-sample errors rather than theorem certificates. No independent mathematics audit, formal proof assistant, or independent historical-priority certification has been performed.
