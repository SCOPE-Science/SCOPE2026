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

The claim follows analytically from explicit supporting facet equations, symmetry averaging of the feasible-center set, a factored branch-comparison polynomial, and strict branch monotonicity. The accompanying `verify.py` is an optional standalone finite consistency checker requiring only Python's standard library. It enumerates supporting triangular facets directly from ten coordinates for more than two hundred heights, independently calculates volume by the divergence theorem, and compares the result with the two analytic radii. A successful local run reported `PASS 620 geometric consistency checks`. These numerical tests are not exhaustive over real heights and do not establish historical priority or global optimality for arbitrary ten-point spherical coverings. No independent audit has been performed.
