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

Run `python3 verify.py` using Python 3's standard library in the directory containing `verify.py`. The observed output was:

`ALL CHECKS PASSED: exact recurrence, simplex, F-stochastic inequalities, cylinders, rate tail and moments`

The checker verifies, with `fractions.Fraction`, simplex invariance and the exact closed product for every binary word through length six for two nontrivial parameter pairs and two positive initial states; exact F-stochastic inequalities on a rational simplex grid; exact probabilities, means and variances of all binary cylinders through length eleven; exact convergence of the geometric coefficient sums; and the small-iterate contraction condition for the auxiliary map. `decimal.Decimal` at precision 90 independently compares direct nonlinear iteration with the logarithmic recurrence and the deterministic tail bounds for a ten-symbol environmental sequence.

**Logical scope:** These are bounded diagnostic checks. The theorem for all real parameters, arbitrarily long trajectories, singularity, and exact Hausdorff dimension is proved in `RESULT.md` using algebra, the strong law and dyadic mass estimates, not by numerical sampling. No independent audit has been performed. The closest accessible primary literature provides class definitions, stability and distinct path-measure results but not a verified priority certificate for this specific rate law.
