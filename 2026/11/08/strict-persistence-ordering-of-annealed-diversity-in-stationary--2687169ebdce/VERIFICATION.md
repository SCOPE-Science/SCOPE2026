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

## Verification scope

The proof reduces the expected discounted Markov renewal functional to one scalar ratio of integrals. Its strictness is analytic: the parameter-dependent Radon–Nikodym ratio is decreasing in the current break, and the powered response function has a fixed strict monotonicity sign.

Run `python check.py` from the package directory (Python standard library only). In the recorded run, the checker reported 4,625 exact rational assertions and 3,080 floating-point comparisons as passed. It solves the finite-state conditional renewal equations by a separate rational Gauss–Jordan inversion, checks their agreement with the closed formula for integer powers, checks strict change across five persistence values, checks a fractional-power case and the entropy identity with independent finite-state linear solves, bounds the full power sum between an exhaustive eight-step partial sum and its remaining-stick certificate, and certifies the two-point collision endpoints \(5/11\) and \(13/35\).

Finite computations do not establish global strictness or the convergence of the infinite stick construction; those steps are proved in RESULT.md. The manuscript does not claim independent validation or completeness of the historical literature search.
