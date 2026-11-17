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

# Verification record

The exact symbolic logit derivative and rational two-cycle were checked by `python checks/check.py` using SymPy and standard-library fractions. The checker also ran 776 finite exact-arithmetic word cases, confirming positivity of denominators and noncontraction. It ended with `SWITCHED_QUADRATIC_LOGIT_CHECK_OK word_cases=776 two_cycle_multiplier=27389/22440`.

The proof does not infer uniqueness or infinitary repulsion from those samples. Those conclusions follow analytically from strict monotonicity of the logit displacement and exact endpoint limits. Interval-boundary periodic points are outside scope. The claims have not undergone independent audit.
