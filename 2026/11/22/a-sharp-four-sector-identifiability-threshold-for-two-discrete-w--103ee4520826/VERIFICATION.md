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

# Reproducibility and limits

From a directory containing the attached script, run `python3 check.py` with a Python 3 standard-library installation. The script outputs the number of tested assertions, the four-bin example probability vector, and its positive reciprocal contrast. In the recorded run, 2,814 assertions passed. The script reconstructs sector probabilities by two independent numerical routes, tests the exact two- and three-bin reparameterization numerically, verifies zero conditionalized contrast and positive marginalized contrast over a range of parameters, and evaluates the key second derivative with finite differences.

These numerical checks diagnose implementation and algebraic mistakes; they cannot prove the all-parameter or every-sector statements. Their proofs are the branch-safe integral expression, strict reciprocal convexity, symmetry, and monotone central-probability reparameterization in `RESULT.md`. A separate independent mathematical audit has not occurred.
