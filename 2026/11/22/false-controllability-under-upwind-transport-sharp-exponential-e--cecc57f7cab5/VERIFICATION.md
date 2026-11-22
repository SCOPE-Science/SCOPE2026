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

The exact finite Poisson convolution identity follows from the nilpotent one-way shift matrix. The proof uses uniform geometric control of the Poisson tails before the arrival time, Stirling's formula and an endpoint Laplace estimate for its exponential asymptotic, then a centered Poisson limit and integrable tail control for the critical layer. No finite computation is treated as an infinite-mesh proof.

`checks/upwind_gramian_check.py` checks direct semigroup-versus-Poisson impulse calculations, subcritical asymptotic ratios across refined meshes, the arrival asymptotic constant, moving-window ratios, and the Gaussian integral identity. Run it with Python 3, NumPy, and SciPy.

The claimed limits apply only along endpoint-aligned meshes with fixed positive physical interval length, gap, and transport speed. The indicators are cell averages and observations use the mass matrix. Numerical underflow can occur when testing deep subcritical asymptotics at extremely fine resolution; the checker uses endpoint-rescaled quadrature for those tests.
