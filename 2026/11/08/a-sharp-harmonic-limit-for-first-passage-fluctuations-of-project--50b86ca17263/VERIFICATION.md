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

# Reproduction notes

Run `python verify.py` with Python 3 and SciPy. The checker compares the exact positive hypergeometric-coefficient series against an independent nested first-passage ODE quadrature over five dimensions and six thresholds per dimension, checks positivity and strict order on the sampled grid, and checks endpoint estimates and the two-level logarithmic mean identity. It passed 196 assertions.

The exact proof uses the regular Jacobi hypergeometric boundary-value solution, termwise differentiation on compact subintervals, a strictly positive covariance derivative, divergent coefficient weights, and the explicit mean hitting-time integral. These analytical steps, rather than the finite computations, establish the universal statements. This package contains no independent external audit evidence.
