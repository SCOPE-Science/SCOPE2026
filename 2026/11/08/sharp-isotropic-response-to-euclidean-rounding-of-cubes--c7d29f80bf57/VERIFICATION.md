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

The mathematical proof uses exact disjoint face/edge/corner integration and a sign polynomial with five positive coefficients; no finite search is treated as a proof of an infinite-radius statement. The standalone `check.py` computes the exact orthant-ball monomial integrals from gamma functions, matches both three-dimensional moment polynomials, checks the derivative identity, and proves every sign inequality using rational bounds on \(\pi\). Its additional symbolic calculation matches the all-dimensional quadratic coefficient. The optional Sobol integration independently checks the numerical moments at three radii; its output is not a certification of the analytic theorem.

Known scientific limitations: the global monotonicity result covers dimension three, while the higher-dimensional result establishes only a local asymptotic; no independence audit has been performed.
