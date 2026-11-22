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

# Reproducibility and limits

Run `python3 verify.py` using Python 3.9 or later; no third-party modules are required. The independent checker implements stable forms of the scalar stationarity equation, obtains roots by bisection and compares against a logarithmic competitor grid. It also checks the exact cubic-bias witness, derivative-sign certificate, strict correlation ordering and convergence toward the universal boundary-layer roots. Its deterministic seeded execution reports 20,174 supplementary checks.

Mathematical completeness is supplied by the polynomial-exactness constraint, exact bias/variance identity, strict quotient monotonicity and uniform asymptotic expansion in `RESULT.md`. Finite tests do not establish infinitely quantified claims and are not external certification. No independent audit has been performed.
