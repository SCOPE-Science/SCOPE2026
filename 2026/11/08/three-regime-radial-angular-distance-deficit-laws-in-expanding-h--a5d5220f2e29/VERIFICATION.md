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

# Computational verification and limitations

The executable `checker.py` and `requirements.txt` accompany the proof. Run `python checker.py` with its declared dependencies. All seeds are fixed. The script checks the odd-dimensional gamma-beta Laplace product identities, the explicit dimension-three survival expression, an exact one-dimensional integral for the upper tail, and direct hyperbolic-law-of-cosines distances from two independently sampled isotropic points. It uses 85,000 pairs for each of five models at radius 18, spanning radial-dominant, critical, and angular-dominant regimes, and accepts explicit Monte Carlo quantile tolerances. It prints `HYPERBOLIC_RADIAL_ANGULAR_TAIL_PHASES_OK 85000 5` on success.

No exact symbolic polynomial identity is inferred from finite Monte Carlo. The proof independently covers each fixed dimension, all positive rates, and all real tail thresholds after convergence. The local simulation does not test all dimensions, all sample radii, or the order-of-limits requirement, and it provides no historical priority certificate.
