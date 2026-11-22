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

# Verification record

The proof is self-contained in `RESULT.md`. The supplementary `checker.py` is executable with Python 3 and standard-library modules only; run `python checker.py` with the current directory containing the script. Checks completed successfully: 1607 deterministic assertions for the exact rational null moments, all-order analytic limits and variance ratios; plus 25000 independent raw-uniform simulated samples at sample size 100 with fixed RNG seed 773052.

Observed simulated mean = 0.16507407727782775, compared with exact 0.165. Observed variance = 0.0000567705965508411, compared with exact 0.00005665. The arithmetic-check code does not independently establish the Lindeberg CLT, which is proved in `RESULT.md`. The normal quantile 1.959963984540054 is used solely for numerical illustration of the exact limiting-size formula. The published source was inspected for the exact statistic, variance assertion and tabulated critical values; no independent mathematical audit has occurred.
