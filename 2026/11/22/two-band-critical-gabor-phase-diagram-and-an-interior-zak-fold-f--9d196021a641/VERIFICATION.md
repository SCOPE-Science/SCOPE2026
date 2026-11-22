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

The analytic Zak multiplier, imaginary-part inequality, strict one-sided spectral criterion, stationary-point location, endpoint ranges, and Taylor coefficient are proved in `RESULT.md`. Run `python3 CHECK.py` with Python's standard library. It executes exact rational checks and representative finite numerical samples, including direct evaluation at analytically prescribed Zak zeros. A run printed `PASS: 1680 supplementary algebraic and finite-sample checks` for the fixed rational specialization; the checker is not an exhaustive continuous search and does not substitute for the proof.

The correct sharp band endpoints use one-sided frequency limits. At the fold, two spatially aligned interior zeros coalesce; the square-root formula holds locally above the lower threshold only. No external proof assistant, independent audit, or historical priority certification was used.
