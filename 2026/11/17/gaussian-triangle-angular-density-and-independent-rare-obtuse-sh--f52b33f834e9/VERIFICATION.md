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

# Verification record

The theorem's analytic proof establishes the exact Wishart density, two Jacobians, an evaluated radial gamma integral, and its normalization; the conditional limit uses a beta boundary Laplace argument and independent spherical/chi-square central limit theorems.

## Executable numerical corroboration

Run `python verify_angles.py` after installing the two Python packages in `requirements.txt`. The checker uses four exact angle-density double integrals, an independent beta-marginal comparison for each, three samples of deterministic-algebra identity tests, and exact finite-dimensional beta tails across four dimensions.

Observed: the total-mass integrals for dimensions \(2,3,4,7\) differ from one by at most \(2\times10^{-11}\), and the obtuse-marginal integrals agree with \(I_{1/4}(d/2,d/2)\) to the same tolerance. The three-side factorization agrees to less than \(6\times10^{-14}\) absolute error in tested coordinates. For dimensions \(20,80,320,1000\), the maximum discrepancy from an exponential tail among four specified thresholds decreases from \(0.086\) to \(0.0023\). The checker ends with `GAUSSIAN_TRIANGLE_ANGLE_SHAPE_LAWS_OK`.

No finite numerical test establishes an all-dimensional identity, a conditional limit theorem, mathematical priority, or independent validation. The cited Eisenberg–Sullivan full text was not available for source comparison. No independent audit has been performed.
