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

# Computational verification

The accompanying `verify.py` constructs the full eight-configuration continuous-time generator from the transition rules (one central departure-time multiplier and two boundary reservoirs), normalizes the stationary distribution, and verifies the exact current on the first bond, second bond and left reservoir. All expressions use exact SymPy rational functions, with exact cancellation checks rather than floating-point fitting. It also checks the displayed quartic derivative, homogeneous and fast-centre limits, the strict-comparison factorization and the radical example. A separate family of 45 admissible rational state-space solves checks stationary nonnegativity and the current expression.

Run with `python verify.py` after installing SymPy. The packaged script was executed successfully. Infinite parameter coverage depends on the symbolic identities, coefficient sign bounds, Descartes' rule and the explicitly stated parameter domain; the 45 checks only guard the implementation. No formal proof assistant or independent scientific audit has been performed.
