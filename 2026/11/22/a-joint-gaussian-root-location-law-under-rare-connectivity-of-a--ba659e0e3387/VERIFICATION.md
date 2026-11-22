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

# Reproducibility

Execute `python checker.py` with a standard Python 3 installation. It independently enumerates all permutations of the interior spacing ranks for every \(2\le n\le9\) and verifies the connected-pattern counts and exact reciprocal-pair index frequencies. A separate exact rational integration, via independent increments of exponential order statistics and the Gamma normalization identity, verifies all five conditional moment entries across those eight sizes. Observed result: `PASS: 8 sizes n=2..9`.

The normal limit is established by the analytic conditional Lindeberg argument in `RESULT.md`, not by this finite checker. No claim of exhaustive verification beyond the stated eight finite sizes or an independent external audit is made.
