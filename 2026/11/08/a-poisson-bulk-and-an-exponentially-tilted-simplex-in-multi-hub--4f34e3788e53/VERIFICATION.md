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
The analytic argument checks detailed balance, the finite canonical partition function, dominated convergence of the finite outside occupation, and a uniform exponential expansion followed by a simplex Riemann sum. The bulk Poisson law and the hub law are shown jointly independent for every fixed number of hubs at least three. The result does not cover changing hub counts, mass-dependent departure rates, or mixing times.

Reproduce the finite checks with `python verify.py` using Python 3 and its standard library. The script prints a pass count only after checking both direct labeled-state enumeration and reduced coefficient enumeration, local detailed-balance identities, and asymptotic predictions. Finite numerical checks are corroboration, not certification of the infinite limit.
