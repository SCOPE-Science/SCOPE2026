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

# Reproducibility verification

Run `python3 verify.py` with the Python standard library. The checker independently evaluates probability integrals by Simpson quadrature and closed forms, locates the two derivative stationary points and mortality transition, checks strict signs across representative parameter grids and crosses the computed roots. The latest extraction replay returned 5,824 successful assertions. The mathematical conclusions for every positive deadline and nonnegative mortality parameter follow from the exact proof in `RESULT.md`, not from a finite test grid. No stochastic field samples, calibration data or independent audit are supplied.
