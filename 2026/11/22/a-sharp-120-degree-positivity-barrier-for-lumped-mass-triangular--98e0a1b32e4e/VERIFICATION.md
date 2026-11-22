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

Run `python verify_triangle.py` with Python 3 and no third-party dependencies. Expected summary lines are contained in `verify_output.txt`. The script assembles exact finite-element matrices from triangular geometry; it does not merely substitute symbolic expected formulas. Exact rational inversion, spectral reconstruction, row-sum preservation, symmetry, sign cases and the \(120^\circ\) boundary are checked. The exponential case is sampled numerically at five altitudes, whereas its global uniqueness follows from the derivative proof in `RESULT.md`.

These checks are supporting evidence, not an exhaustive test over all real heights and times. This package has not undergone an independent audit. The inaccessible relevant 2018 chapter prevents an unconditional historical-priority assertion.
