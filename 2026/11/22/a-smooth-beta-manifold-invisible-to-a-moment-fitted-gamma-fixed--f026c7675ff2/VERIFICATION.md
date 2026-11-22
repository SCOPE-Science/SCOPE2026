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

# Reproduction and limits

The accompanying `verify_gamma_blind.py` requires Python 3 and SymPy and can be invoked with `python verify_gamma_blind.py`. It checks the exact \(\operatorname{Beta}(a,1)\) departure, the first derivatives determining the implicit zero curve, the uniform and Gamma influence-function expectations and variances, the variance ratio and the 5% limiting rejection probability. The checker reports **19 passed analytic assertions** when executed with SymPy.

The derivation of the local Beta curve uses analytic differentiation under integrable beta densities, followed by the implicit-function theorem; numerical root finding is not used as proof of existence. Both asymptotic-normal assertions use the ordinary two-sample U-statistic projection and the delta method on the empirically fitted first two moments. The Gamma variance reduces to a finite sum of exact polynomial–exponential integrals, with polynomial coefficients reproduced in `RESULT.md` and in the checker. The reported 5% limiting power is an asymptotic calculation for a refitted moment-parametric Gamma calibration, not a finite-sample simulation estimate.

The code does not verify historical publication priority. The result has been reviewed internally at the same-model level only. No independent audit or third-party certification has been performed.
