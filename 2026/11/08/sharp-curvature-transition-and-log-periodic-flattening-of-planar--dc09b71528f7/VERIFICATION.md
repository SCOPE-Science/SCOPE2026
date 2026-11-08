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

# Reproduction and limitations

Extract `RESULT.md` and `check_curvature.py` from the same evidence package, then execute `python3 check_curvature.py` using Python 3 with no third-party dependencies. The expected successful output is `PASS: 150 exact and numerical identities/limits; external dependencies: none`.

The program carries out 120 exact checks over rational parameters and rational unit-circle directions of the algebraic ellipse-radius identity, and 30 floating-point comparisons of equivalent radius series, axis values, the critical logarithmic coefficient, and periodic-phase convergence for a supercritical family. All parameter examples satisfy \(0<a<b<1\). Floating-point tolerances are explicit in the checker and are corroborative, not certificates of infinite limits or full geometric regularity.

The analytic proof in `RESULT.md` addresses the necessary uniform convergence, continuity at exceptional normals, sharp threshold, critical scaling, and nonconstant periodization. In particular, the proof of actual \(C^2\) boundary regularity uses Cartesian graph derivatives and does not require the support function to be \(C^2\) in its normal-angle variable.

Scope limitations: the noise support must be a complete closed Euclidean disk; the map must have two distinct positive diagonal contraction factors; no nonlinear persistence or higher-regularity claim follows. Searches and source comparisons establish originality only to the extent of accessible materials. Independent mathematical audit has not been performed.
