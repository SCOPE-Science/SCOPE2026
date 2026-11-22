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

# Verification and limits
The exact Pareto mismatch maximization and Cramér–von Mises integral were checked symbolically for selected rational shapes; the reproducibility script `pareto_checker.py` passed 23 assertions including numerical sample-and-refitted-bootstrap behavior at \(\beta=1/2\) and sample sizes 2,000, 10,000, 40,000. The probability-theoretic proof is analytic and does not infer infinite-sample statements from finite computation.

The conditional bootstrap uses the fitted sample-mean moment estimator on both the observed data and each bootstrap repetition; the theorem excludes maximum-likelihood fitting, the boundary shape one, and tests not defined by the stated EDF formulas. Historical-priority assessment recognizes the 2022 published observation of null-size distortion at shape one and the classical finite-mean obstruction. Independent mathematical audit has not been performed.
