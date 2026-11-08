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

# Numerical replication and exact proof boundaries

Install the packages listed in `requirements.txt`, then from this directory execute `python verify.py`. The script calculates the source's OU correlation moments through a change of variable and 128-point Gauss–Laguerre quadrature. It tests strict tilted moment inequalities and decreasing optimizer function values, finds roots by bracketing, confirms the critical response boundary, and compares both endpoint laws with direct quadrature. The analytical argument proving the statements for every positive parameter is in `RESULT.md` and does not depend on this finite numerical test.

With the supplied implementation, the script reports 61 successful numerical checks and finds, for \(D=\tau=\mu=1\), \(\beta_c\approx1.260202010789389\) and \(\gamma_*(2)\approx1.825828106869013\). Quadrature values are rounded and not asserted to be exact rational certificates. Source Eqs. (7)–(16) and (20)–(22) in arXiv:2609.35838v1 allow independent normalization checks.

The test does not simulate a finite interacting oscillator population, prove stochastic nonlinear stability, or measure experimental effects. It neither certifies priority nor replaces independent audit.
