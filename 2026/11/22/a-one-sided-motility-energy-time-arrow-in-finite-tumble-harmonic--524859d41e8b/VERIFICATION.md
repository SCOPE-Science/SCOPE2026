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

The exact analytic proof and domain are in RESULT.md. Run `python check.py` from the same directory with `sympy`, `numpy`, and `scipy` available. The check code recomputes the exact Laplace transform and its positive-kernel decomposition independently, tests the integrated arrow and short-lag slope symbolically, then compares a direct matrix semigroup with convolution integrals for 30 cases, including coincident decay rates. An event-driven Monte Carlo sample provides only a finite sanity check for one case; its sampling tolerance is stated in the code.

Verified execution produced the three PASS messages: symbolic identities, independent matrix-semigroup/positive-kernel checks (30 tests), and event-driven simulation (30,000 paths). The general positivity conclusion does not depend on simulation, numerical quadrature, or any external proof service. The claim does not address independent scientific audit or certify publication priority.
