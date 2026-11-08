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

# Verification

Run `python3 verify.py` using Python 3 with only its standard library. The checker independently constructs the rational polynomial in the proof by three-variable polynomial arithmetic, divides exactly by \(1-z\), verifies that the remainder vanishes, and converts its 46 nonzero monomials to the degree-eight trivariate Bernstein basis. Each of the 729 coefficients is checked as a rational number and the minimum equals \(1/8\). This finite exact coefficient check, together with the elementary Bernstein convex-combination property, is an infinite-domain proof of positivity on the unit cube.

The checker also runs reproducible seeded floating-point tests: 20,000 stable parameter triples and seven illustrative counterexample parameter values below the claimed threshold. These are supplemental diagnostics and are not needed to justify universal quantifiers. The analytic fixed-point multiplier proves sharpness for all excluded stabilization parameters.

The one-step result is not invariant-domain preservation. A limiting output at stabilization one exceeds the starting interval, so the theorem alone does not guarantee energy descent on subsequent iterations. The scientific comparison with an unavailable full 2022 article remains a residual historical-priority risk; no independent audit has been performed.
