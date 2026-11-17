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

The analytical proof establishes the global orbit portrait, no-other-equilibria statement, and asymptotic limits; the finite checks below independently recompute their algebraic prerequisites but do not prove the infinite claims on their own.

Run `python verify.py` with SymPy, NumPy, and SciPy. The checker verifies Hamiltonian differentiation, the polynomial factorization defining the sharp boundary, the degenerate quartic identity, Taylor coefficients, boundary energy, and the exact splay linear spectrum. It also integrates ten sample noncollision trajectories and computes eight representative collision-clock quadratures. Expected status:

`VERIFY_OK symbolic_hamiltonian=3 polynomial_factors=2 local_series=2 splay_spectrum=3 collision_boundaries=3 numerical_energy=10 critical_clocks=8`

No independent audit or external validation has been performed.
