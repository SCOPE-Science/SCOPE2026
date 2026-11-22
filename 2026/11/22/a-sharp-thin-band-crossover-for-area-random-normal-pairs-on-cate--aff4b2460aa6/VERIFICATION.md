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

The mathematical proof derives the probability law without assuming a numerical limit. The self-contained `checker.py` (Python 3 with NumPy and SciPy) checks 33 independent numerical comparisons: four latitude normalizations, four direct axial second moments, four Legendre second moments, four endpoint coefficient quadratures, six crossover integral identities, eight finite-band crossover ratios, one critical-height root, and two endpoint-profile asymptotics. Output is in `CHECKS.txt`.

The code and finite checks cannot establish infinite Legendre-series convergence, exact uniqueness, or uniformity. Those depend on the analytic arguments in `RESULT.md`. Sampling is surface-area-uniform on a finite symmetric catenoid band; no experiment is claimed to prove statements outside this domain.
