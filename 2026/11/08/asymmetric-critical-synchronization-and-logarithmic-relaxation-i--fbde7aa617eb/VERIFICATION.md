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

# Reproduction and limits

Run `python verification.py` from the same directory, with Python 3 and the `sympy` and `mpmath` packages available. The program checks an exact symbolic sixth-order expansion of \(g^2\), exact rational equilibrium identities for three unequal-coupling pairs, and three 14,000-iterate high-precision trajectory tests. It prints six PASS messages; its completed execution produced no assertion failures.

The first two checks verify precise algebraic premises used in the proof. The finite orbit checks evaluate the normalized even-time critical rate, the stabilization of the residual after subtracting \((8/3)m+(8/5)\log m\), and the exponential synchronization of both species; they are not an exhaustive parameter or initial-state test. The analytical infinite-time limit follows from the global-convergence theorem, the exact ratio contraction, the exponential-shadowing lemma, and summable asymptotic increments, not from numerical extrapolation.

Full mathematical independence has not been assessed. The originating global convergence premise is cited in RESULT.md. No formal proof assistant or external certification is claimed.
