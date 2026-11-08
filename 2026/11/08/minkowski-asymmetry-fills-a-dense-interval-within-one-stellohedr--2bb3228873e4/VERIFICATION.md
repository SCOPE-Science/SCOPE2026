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

# Reproducibility and checks

Run `python checker/check_minkowski.py` after installing SciPy. The checker uses exact `fractions.Fraction` for all candidate reflection constraints and separately solves a continuous linear program with `scipy.optimize.linprog(method="highs")`. It checks all nonempty subset inequalities for 360 parameter vectors in dimensions 2–5, seven classical examples in dimensions 2–8, and 30 parameters in two extremal families. Its expected successful output is `PARKING_ASYMMETRY_CHECKS_PASSED 360 7 30`.

The exact proof derives both an optimal lower bound and feasibility using the complete published halfspace description; the finite computations do not certify all possible integer parameters. Strict proper-subset inequalities and equality of aggregated facet constraints establish respectively feasibility and uniqueness. The dense-range construction and cube/simplex Hausdorff limits are proved analytically via the complete vertex description. Independent audit has not been performed.
