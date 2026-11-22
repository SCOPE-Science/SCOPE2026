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

The formal argument is in RESULT.md. The script `verify_min_cf.py` checks the Bessel identity by independent quadrature, the exact clipping decomposition, explicit nonasymptotic error estimates, fixed-sample endpoint correction, MLE mean-one constraint, and an example of the reverse-maximum ranking. Its 66 numerical assertions passed with 65-digit precision; these checks do not certify the limiting theorem for all inputs. The source paper defines the statistic in equations (3.1), (3.3) and (4.1)–(4.3). The only external Python dependency is `mpmath>=1.2`. No independent mathematical validation is represented by this file.
