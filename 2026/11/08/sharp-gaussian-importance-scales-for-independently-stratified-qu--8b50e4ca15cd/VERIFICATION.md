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

The proof uses the exact conditional-variance identity, a sharp approximation limit for piecewise-constant averages, Gaussian even moments, and a one-positive-root polynomial sign test. These steps establish the all-scale moment classification and unique optimum without numerical inference.

Run `python check.py` with the packages listed in `requirements.txt`. The observed output in `check_output.txt` verifies the symbolic coefficient and derivative identities, numerical Gaussian-moment quadratures, within-stratum conditional variances for selected sample counts and scales, and the ordinary Monte Carlo comparison. Finite quadrature does not prove the infinite asymptotic assertions, which are proved in `RESULT.md`.

The comparison concerns independent strata and fixed Gaussian proposal variance only. No independent external audit was performed.
