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

# Verification of the exact boundary-flip latency

Analytic validation: For any positive parameters, the radial projection step saturates to the opposite endpoint exactly when \(\lambda\eta/S_k\ge2\). Repeating the exact accumulator multiplier gives the logarithmic integer count. At the first non-saturated step, all later step coefficients lie strictly in \((0,2)\); the difference-of-squares argument bounds the accumulator and gives geometric contraction. A direct Taylor expansion of the reciprocal logarithm gives the sharp parameter limit.

Executable check: run `python checker.py` (Python 3, standard library only). It independently applies two-dimensional Euclidean ball projection and multiplicative accumulator updates for eight displayed unit-parameter gains and three additional parameter tuples; it verifies two exact rational threshold certificates. The test exited successfully on all assertions during preparation. Recorded counts for gains 0.1, 1, 2, 4, 8, 16, 32 and 64 are 0, 0, 1, 7, 46, 269, 1423 and 7102, matching the derived formula.

The checker is finite and diagnostic: the mathematical proof, not experimentation, establishes the all-dimensional result. There is no independently performed mathematical audit or certification. The conclusion is only about the deterministic exact-projection radial test problem, not noisy gradients, general constraints or universal optimization lower bounds.
