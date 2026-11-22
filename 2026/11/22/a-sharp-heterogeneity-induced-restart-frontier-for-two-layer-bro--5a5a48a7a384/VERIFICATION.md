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

Analytical proof: solve the flux-continuous two-layer backward exit-time moment recursions, substitute into the exact Poisson-renewal mean, factor its initial rate derivative, and evaluate the third moment on the symmetric critical branch. A local implicit-function argument proves the optimizer onset. The hyperbolic Laplace transform is derived independently as a check.

The supplied `checker.py` requires Python with SymPy and mpmath. Execute `python checker.py` in the directory containing this document. In the performed verification it completed 51 assertions/parameter cases: 3 general moment/slope identities, 4 symmetric third-moment and polynomial identities, 20 independent transform-derivative checks, 18 weak-rate comparisons, and 6 critical curvature comparisons. Finite test sets do not prove the infinite-parameter statements. The proof uses analytic transmission uniqueness and finite-interval ellipticity to justify moment and Taylor expansions. Publication priority and experimental realization are not independently certified.
