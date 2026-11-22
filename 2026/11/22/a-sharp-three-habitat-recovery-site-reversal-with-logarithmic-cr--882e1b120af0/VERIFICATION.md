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

The derivation uses the symmetric Jacobi spectrum, a three-exponential zero bound, the leading eigenvector identity, Hellmann–Feynman differentiation and analytic simple-eigenvalue perturbation. The complete scope and boundaries are given in `RESULT.md`.

Running `python3 CHECK.py` yields `PASS: 126 exact-rational check assertions`; checks include a strict sign bracket on the time crossover for an explicit integer-parameter witness with a rigorous rational Taylor-tail bound, and 60 exact critical-eigenvector instances. This is supplementary finite verification. The analytic proof, not this finite program, proves global claims.

No formal proof assistant or independent expert review was used. Numerical root locations are informational only, with signs independently certified at the reported rational times. The generalization to other graphs and stochastic population survival is not established. The historical priority assessment relies on accessible inspected sources and remains provisional.
