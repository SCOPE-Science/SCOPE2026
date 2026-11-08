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

The independent-audit channel has not been used. The included `verify.py` is an ordinary exact-arithmetic diagnostic, not external certification.

Run `python3 verify.py` from this directory. The checker uses only Python standard-library modules. It directly integrates fourth powers of general symmetric, non-diagonal Gaussian quadratic-plus-linear polynomials using an exact rational polynomial representation, checks the fourth-cumulant formula and nonnegative three-term deficit, checks the algebraic equality witnesses in dimensions two through eighty, and performs small integer spectral grids.

Passing finite tests does not prove inequalities in all dimensions or exhaust all coefficient configurations. Universality and equality classifications follow from the proof in RESULT.md, in particular the constrained spectral maximum lemma and exact scalar factorization.
