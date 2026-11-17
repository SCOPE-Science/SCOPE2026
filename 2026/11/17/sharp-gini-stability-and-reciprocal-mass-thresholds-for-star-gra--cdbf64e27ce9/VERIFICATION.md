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

# Verification and mathematical limits

Execute `python3 checks/verify_star_fused_gini.py` using Python 3 without extra dependencies. The script uses `fractions.Fraction` to avoid rounding; it checks the exact binary-cut norm for each tested weighted block, evaluates actual proximal optimizers by solving the strictly monotone piecewise-linear hub equation, verifies sharp local witnesses for independent positive fusion-edge penalties, and compares random real two-input pairs with the analytical coefficient. The analytic proof, not finite experiments, establishes the formula for every integer number of leaves, every positive hub mass, every strictly positive penalty vector, and all real input pairs.

The central proof identities appear in RESULT.md: the exact local block Jacobian, the binary cut coarea reduction, concavity in the number of selected untouched leaves, the convexity of the hub-including cut factor, and the final one-variable optimization. Reproducibility checks do not establish historical novelty or independent certification. No external audit has been performed.
