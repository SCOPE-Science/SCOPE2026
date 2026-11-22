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

# Verification and reproducibility

The analytic derivation in `RESULT.md` proves the continuum results. The standalone `verify.py` uses only the Python 3 standard library and can be run with `python3 verify.py` after extraction. It was executed against the actual file contents and printed:

`VERIFY_OK deterministic_checks=66052; finite numerical diagnostics, analytic proof required`

The tests compare radial formulas against both generating disks, test ellipse containment and area bounds on angle grids, check quadratic and cusp coefficients through several small perturbations, compare the disk distribution with an independent midpoint angular enumeration, evaluate the mixed-parabolic region area, compare crossover quadratures at multiple parameters, check the large-parameter coefficient, and independently integrate local rare-event regions for three positive separations. Finite tests do not establish uniqueness, limiting probabilities, or absence of earlier published equivalents. The analytic arguments in `RESULT.md` carry those obligations within the given scope, subject to independent review.

The sampling measure is uniform in direction, not arclength; no external data or proprietary code is required.
