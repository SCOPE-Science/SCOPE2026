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

The theorem follows from the exact ball-slice integral, enclosing-ball extremal argument, and dominated-convergence integrations over the three rescaled regions. The normalizer is a one-dimensional support-width integral. The critical rare-plane law is obtained by normalizing the same limiting Jacobian, not by extrapolating finite calculations.

Run `python verify.py` with NumPy and SciPy installed. The script numerically integrates the actual planar circular segments arising from three-dimensional ball-cap sections, using polar orientation and affine-offset grids independently of the limiting-domain integral. It checks 20 near-maximum coefficients/crossovers and five exact normalizers. All 25 assertions passed. Grid tolerances are deliberately finite; they neither prove all dimensions nor certify the asymptotics or historical novelty.

Conditions: ambient dimension at least three; rigid-motion invariant affine plane measure conditional on hitting a solid cap; fixed height or fixed critical-window parameter; no independently performed audit.
