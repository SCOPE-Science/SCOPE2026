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

# Reproduction and analytical boundaries

The analytical proof is self-contained in `RESULT.md`. It uses only the four-state stationary generator, a stationary harmonic convolution, and elementary rational algebra. The generator uses event-level label transition \(\Pr(Z'=z'\mid Z=z)=(1+\rho zz')/2\), independent uniform heading redraw, and event rate \(\gamma\). The parameter domain for the unique stationary chain is \(-1\le\rho<1\), \(\mu,\gamma>0\), \(a,b>0\), \(a\ne b\), \(D\ge0\).

To reproduce the finite exact checks, install Python 3 and SymPy and run `python verify.py` in the extracted package directory. The script constructs the four-state jump generator and directly solves the exact stationary moment equations over rational values. It passed 1,347 deterministic exact assertions, including the variance, fourth-cumulant, symmetry, and rational threshold identities. A formal \(\rho=1\) limiting setting is included solely as a check of the rational formulas, not as a claim of stationary uniqueness. The exact sign classification holds for all admissible parameters by a strictly monotone rational expression, and cannot be established by a finite test grid alone.

The thermal diffusion term is an independent centered Gaussian Ornstein–Uhlenbeck convolution. Its fourth cumulant vanishes identically. This argument requires thermal Brownian noise independent of the internal mark dynamics. No external verification or priority certification has been performed.
