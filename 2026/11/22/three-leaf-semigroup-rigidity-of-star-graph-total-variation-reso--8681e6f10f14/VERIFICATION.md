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

# Verification of the star-graph semigroup classification

The accompanying standalone `star_tv_semigroup_checker.py` can be run with Python 3.9 or newer and has no third-party imports. It checks exact rational stationarity and edge-sign subgradient membership for the two exhibited counterexamples at half-step and full-step penalty scales. It also verifies 58 pair-extension instances and all 39 sign/tie configurations in degrees one through three. The analytic flux symmetry argument handles infinitely many inputs and the all-degree pair-extension proof handles arbitrarily many leaves; finite checker output does not assert exhaustive testing beyond its explicit finite ranges.

The positive direction invokes the established MINSUB/polyhedral equivalence theorem (Burger et al., arXiv:1601.02912, Theorem 5). Its hypotheses are checked in the proof. The negative direction is entirely self-contained: each KKT certificate proves global optimality because the quadratic objective is strictly convex. Thus it does not rely on floating-point results. Publication-priority uncertainty remains; no independent audit has been performed.
