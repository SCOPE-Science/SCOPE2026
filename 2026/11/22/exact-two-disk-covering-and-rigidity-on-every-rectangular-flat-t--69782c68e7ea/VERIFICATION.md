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

# Reproducibility and limits

An all-center analytic argument uses the horizontal fiber at half the shorter period to prove the radius lower bound for any pair of sites. For proposed half-diagonal sites, concavity of exact horizontal circle-intersection half-widths proves a sharp cover on every fiber. Equality on that fiber, with a limiting adjacent-fiber argument at the square, proves rigidity. Strict concavity away from the two endpoint fibers identifies exactly the displayed farthest torus points. Differentiation gives the unique fixed-area density minimizer.

The complete bundled `checker.py` is a Python standard-library exact-fraction script. Run `python3 checker.py`. It tests nine positive rational aspect ratios, verifies the contact positions and radii, evaluates a \(33\times33\) rational torus grid at each ratio (total 9,801 exact rational inequalities), and checks the symbolic polynomial identity used in the density derivative. Such a finite grid is *not* an exhaustive proof of a continuum theorem; the analytic proof above is independent of it.

Limitations: only Euclidean rectangular flat tori and exactly two equal intrinsic disks. The square value and classical triangular planar covering density were known. Historical priority outside identified and inspected primary sources, particularly older periodic coverings, is unverified; there is no independent mathematical audit.
