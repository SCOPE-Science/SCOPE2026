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

Analytic verification of the all-size theorem: strict inverse-trace convexity on the symmetric stochastic feasible space; dihedral averaging; Fourier eigenvalues; strict monotonicity in the rim weight and then the spoke weight, with the explicit derivative upper bound \(-1/(m+1)\); exact finite Poisson-kernel summation; asymptotics of the relevant kernel roots.

The standalone `verify_wheel.py`, using only Python's standard library, performs 138 finite exact-rational and numerical checks for wheel sizes 3 through 12 and four larger asymptotic examples. It forms complete transition matrices and computes exact inverses independently of the Fourier formula. The finite checks are not a substitute for the universal proof. The result excludes nonreversible chains, arbitrary stationary laws, and conductance-budgeted optimization. No independent mathematical audit is claimed.
