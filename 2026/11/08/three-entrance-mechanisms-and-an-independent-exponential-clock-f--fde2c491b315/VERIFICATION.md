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

# Verifiable calculations and limits

From the complete package root, run `python3 checks/verify.py` using Python 3 and SymPy. The checker performs 1,078 assertions with exact rational expressions for parameter values 3/5, 2/3, 3/4, 4/5 and target depths from 2 to 21. Assertions compare the full marked success probability against the exact decomposition, check the gambler's ruin harmonic relation, and for small depths independently invert the finite hitting-time system and verify the regeneration ratio. Additional large-depth profiles at depth 200 confirm the three formulae within stated numerical tolerances. The checker prints `PASS 1078 exact algebra checks and controlled asymptotic comparisons` when successful.

The proof of infinite-depth convergence does not follow from finite tests: it uses explicit summable limits of geometric weights, an exact finite-difference solution, and a dominated-convergence renewal Laplace argument. The critical selection parameter 2/3 is already known for the stationary density, and the present novelty assertion is restricted to the conditional *mechanism* and its joint waiting-time law. Full independent mathematical and publication-priority audits have not been performed.
