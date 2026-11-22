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

# Verification performed

The analytic proof is self-contained in RESULT.md: it uses positive physical reset-cycle durations, stationary renewal reward, conditional first-reset survival, an exact beta integral and a conditional Gaussian fourth-moment identity. The included checker.py is executable using only Python's standard library and tests finite algebraic identities, quadrature convergence and the three leading asymptotic coefficients. The proof, rather than computational tests, establishes the limits.

Run `python3 checker.py` in a directory containing this file. Its finite numerical checks cannot establish originality or a uniform discrete-walk scaling theorem; both are outside the claimed scope. The independent audit has not been performed.
