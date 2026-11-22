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
# Verification

The exact hyperbolic nearest-side formula was independently expanded in three distinct regimes: fixed nonsquare, exact square, and critical \(c^2=1/2+\lambda\sqrt h\). Every asymptotic compares the actual area of the clearance superlevel set to its predicted coefficient; the total hyperbolic area is \(2\pi\). The local-limit arguments also prove total-variation convergence of the rescaled conditional densities, not merely weak convergence, because they produce bounded supports and \(L^1\) convergence of unnormalized densities.

Run `python checks/clearance_quadrature.py` with Python 3 and SciPy. This evaluates the exact hyperbolic area integral numerically, rather than simulating points. The nine deterministic quadrature comparisons passed in the original verification. The checks cover two nonsquare shapes at two radii each, four positive critical parameters on both sides of the pinch, and the square. There is no numerical or independently audited claim about all \(h\) or all \(\lambda\). Normalization, compactness of near-maximizer sets, the shape of each blow-up, and the singular area integral are handled analytically in the proof; computations are supplementary.
