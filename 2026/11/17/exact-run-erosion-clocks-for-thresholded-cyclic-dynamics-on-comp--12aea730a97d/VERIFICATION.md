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

# Reproducibility checks

The theorem's universal parts follow from the displayed population recurrence, monotone active-set erosion, and exact labelled exponential weights. The standalone checks use standard Python 3 and no external packages.

- `python3 verify_states.py`: direct labelled vertex-level updates and first-repetition detection for all configurations with 3 through 6 colors, contact thresholds 1 through 3, and 2 through 7 vertices. Exactly 1,376,046 configurations checked; no mismatches.
- `python3 verify_counts.py`: exact occupancy-composition multinomials compared against an independent three-category binomial-convolution census for 3 through 7 colors, thresholds 1 through 4, and 2 through 14 vertices. Exactly 260 parameter triples; no mismatches.

Their captured standard outputs are in `states_output.txt` and `counts_output.txt`. The tests do not constitute an independent mathematical audit and do not prove the unbounded-parameter statements by finite enumeration. An archival 1990 source was inaccessible for full historical comparison.
