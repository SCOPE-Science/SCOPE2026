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

# Verification scope
The proof works with the exact two inverse branches of \(e^x-x-1\), and the exact original-time density \(dt=\lambda|dy|/|e^x-1|\). No simulation is used to infer an infinite limit. The source-normalized Hamiltonian is checked analytically by direct differentiation, and the turning-point estimates use its nondegenerate convex minimum.

`check_lv_crossover.py` uses SciPy and NumPy to integrate the exact branch densities at finite energy. With \(c=1/2,1,2\) and \(E=10,30,100\), it checks convergence of \(T/\lambda\), the positive-branch occupation share and first moments of both limiting coordinates. Execution completed with `RARE_RATE_LOTKA_VOLTERRA_CROSSOVER_CHECK_OK`.

The proof establishes an all-energy asymptotic bound for each fixed c, but no uniform quantitative constant across unbounded c. Independent audit and physical ecological model validation were not performed.
