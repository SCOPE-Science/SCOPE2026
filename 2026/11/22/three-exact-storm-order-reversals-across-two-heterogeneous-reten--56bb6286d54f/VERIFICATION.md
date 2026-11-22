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

The source of the theorem is the explicit capped affine runoff recurrence in `RESULT.md`. The symbolic proof partitions the single roof by saturation at its first event; the exact two-roof certificate partitions at the four stated rational breakpoints and checks all candidate affine zeros. Reproduce the exact checks with `python verify.py` (Python 3 standard library). That script compares direct independent first- and second-event runoff evaluations to all specified rational piecewise formulas at breakpoints and 2,001 grid points, checks the exact three zeros, and checks four alternating strict-sign witnesses. A finite grid does not itself establish the absence of other roots; the exhaustive analytic branch partition does. Neither independent scientific validation nor calibration to field runoff observations has been performed.
