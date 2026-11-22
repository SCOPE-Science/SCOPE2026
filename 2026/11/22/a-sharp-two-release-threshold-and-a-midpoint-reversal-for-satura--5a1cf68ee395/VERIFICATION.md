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

The full derivation is in `RESULT.md`. The provided standard-library Python program `checker.py` computes the exact objective from the two explicitly integrated intervals, tests its agreement with a separately written piecewise Simpson quadrature, compares the closed optimizer against numerical point searches and a golden-section optimizer, and tests the critical horizons, equality cases, and derivative formula. It completed 187,417 supplementary assertions successfully with its fixed deterministic random seed.

Run from a directory containing the two files using `python checker.py`. The script requires no third-party libraries or external data. Mathematical universality comes from the independent analytic proof using a strictly increasing quadratic over the entire admissible interval, not from a finite numerical sample. Parameter values too extreme for floating-point exponentials are outside the numeric test range, but not outside the analytic theorem.

The timing theorem applies only to a constant wild-male competition pool and the specified integrated mating-pressure proxy. No independent external mathematical assessment or empirical calibration has occurred.
