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

The proof obtains the exact Gaussian-to-Haar support identity and radial moment relation, computes all finite moments for fixed-core hub trees from a \(k\)-dimensional Gaussian integral, bounds overlapping edge exceedances using their \(\pm1/2\) correlations, applies a published dependency-neighborhood Poisson bound, and separately proves uniform second-moment control and the fixed-hub \(L^2\) limit.

The executable `verify_width_regimes.py` tests small-tree root support, rank, and hub reductions, the exact one-hub Gaussian CDF integral, the two-hub first-two-moment identities, and Monte Carlo approximations to both asymptotic regimes. Execute `python verify_width_regimes.py` with NumPy and SciPy. Finite numerical agreement is corroborative; the infinite statements are not inferred from a finite computation. The maximum-degree growth hypothesis is sufficient and is not claimed sharp. An independent mathematical audit has not been performed.
