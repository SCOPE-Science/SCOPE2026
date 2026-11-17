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

# Verification and reproducibility

The exact Cartesian-to-polar identity is checked using integer/rational arithmetic for 441 parameter/state combinations. The integral profile is checked by numerical quadrature for positivity, periodicity, its first-order differential equation and the half-turn reciprocal integral. Numerical quadrature in angle (not forward Euler time stepping) checks both the exact time-shift identity and two successive half-turn return clocks. The first-order anisotropy amplitude is checked at two small parameter values. Run `python3 checker.py` with a standard Python 3 installation; it has no third-party dependencies.

The checker outputs PASS on all tests. The numerical value grid for \(a=1,b=5\) has extrema near \(0.110\) and \(682\); this is illustrative, not a rigorous interval certificate. The proof of the assertions for all \(a>0\), real \(b\), all nonzero initial states and arbitrarily long time is analytic in `RESULT.md` and does not depend on numerically sampling the infinite domain. Neither the checker nor this document certifies publication priority or provides independent validation.
