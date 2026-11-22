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

The result is established by the displayed elementary derivative, the exact induced maximum-row-sum norm, an equality-attaining Cauchy--Schwarz reduction, a piecewise one-variable maximization, and integration plus a matching interior finite-difference sequence. These analytic steps handle every positive dimension and real contrast in the stated domain; they are not inferred from sampling.

The standalone program `verification.py` uses only the Python 3 standard library. Run `python verification.py`. Its recorded execution produced `VERIFY_OK 124715 deterministic mathematical assertions`; tests include numerical derivative and finite-difference checks, scalar comparisons, and asymptotic samples. They do not establish novelty, independence, or an infinite exhaustive certificate.

The bound is absolute-coordinate rather than relative error. The case of a singleton box and the one-coordinate map are explicitly separate. A stabilizing offset or signed/zero-valued inputs are not covered. Independent mathematical validation has not been carried out.
