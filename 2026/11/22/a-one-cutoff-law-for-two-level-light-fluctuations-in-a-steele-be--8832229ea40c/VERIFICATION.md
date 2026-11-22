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

The proof is a closed analytical argument given in `RESULT.md`. Supplementary `verify.py` uses only standard Python, a fixed random seed, and an independent composite-Simpson depth quadrature. It checks finite-depth signed comparisons against exact logarithmic thresholds, positive-light admissibility, 400 critical-depth examples and their bracketing, symmetric special cases, and high-mean expansions; it prints 10,510 diagnostic assertions on successful execution. Run `python verify.py` from the extracted file directory. No external files, network, floating-point packages, or hidden certificates are needed.

The numerical work does not certify the exact number of roots for all parameter values. That follows from Rolle's theorem for the three-exponential derivative, plus the strict Jensen inequality. The asymptotic expansion is also justified analytically and is not inferred from finite tables. The physical interpretation is limited to depth-averaged *instantaneous* gross photosynthesis with a fixed Steele response and a quasi-static two-level light forcing. Independent review has not been performed.
