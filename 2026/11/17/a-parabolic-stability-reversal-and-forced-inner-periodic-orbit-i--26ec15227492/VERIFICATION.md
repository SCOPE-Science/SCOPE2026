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

# Reproducibility and verification

The independent-audit channel is unperformed. To rerun the ordinary internal diagnostic, use Python 3 with SymPy and mpmath and execute `python verify.py` in this directory. Its final successful output is `KUKLES_PARABOLIC_EXACT_IDENTITIES_AND_DIAGNOSTICS_OK`.

The checker reconstructs the polynomial cofactor and second radial Taylor coefficient; exactly integrates the trigonometric moment; confirms the exact height, curvature and amplitude order at the Laplace maximum; and samples the K-integral numerically at two finite parameters. The numerical sign samples are **not** certificates of a universal sign or of periodic-orbit existence. The continuous-parameter theorems follow from the analytic proof and the planar basin-boundary argument in RESULT.md.

The extra periodic orbit is asserted to exist, not to be unique, hyperbolic or explicitly located. Completeness of older inaccessible literature and independent mathematical validation are not claimed.
