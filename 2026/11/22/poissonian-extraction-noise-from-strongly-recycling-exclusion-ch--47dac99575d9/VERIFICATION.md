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

# Reproducibility and evidence
Run `python CHECKER.py` with NumPy and SciPy in the same directory as `RESULT.md`. The checker builds the complete Markov generator for lengths two, three and four; compares exact stationary current with the independent two-site formula; and obtains zero-frequency extraction Fano noise from the tilted-generator Poisson equation. Its successful output is: `PASS: 165 deterministic generator, cumulant and convergence assertions; dimensions 2 through 4.`

The proof of the all-fixed-length Poisson process limit is analytic, using cycles that regenerate at the singleton-entry configuration. The numerical evidence is finite and cannot establish a functional limit or exclude all other literature. All rates are strictly positive, and length is fixed before the reset rate diverges. Independent validation has not been performed.
