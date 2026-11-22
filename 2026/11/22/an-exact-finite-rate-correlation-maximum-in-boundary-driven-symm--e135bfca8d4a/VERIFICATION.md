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
# Reproducibility

Run `python CHECK.py` with Python 3 and SymPy. The standalone program builds the unsymmetrized polynomial generator for the complete bipartite inclusion process, solves every degree-one and degree-two stationary moment equation with exact rational arithmetic, and checks the explicit stationary covariance formulas across all sites.

Test configurations: \(n=2\), \(\kappa=1\), \(\gamma=2\), \(v=3\), \((\rho_A,\rho_B)=(1,4)\); \(n=2\), \(\kappa=3\), \(\gamma=2\), \(v=1\), \((\rho_A,\rho_B)=(1/2,5/3)\); \(n=3\), \(\kappa=2\), \(\gamma=3\), \(v=1/2\), \((\rho_A,\rho_B)=(5/4,11/4)\); and \(n=3\), \(\kappa=\gamma=1\), \(v=2\), \(\rho_A=\rho_B=4\). The checker verifies respectively 14, 14, 27 and 27 independent degree-at-most-two stationarity equations and every distinct-site within- and cross-shore covariance in each instance.

The program provides finite-instance checks, not an independent certificate of the theorem for all \(n\). The infinite-family argument is the explicit Lyapunov/moment derivation in `RESULT.md`. No external independent audit has been performed.
