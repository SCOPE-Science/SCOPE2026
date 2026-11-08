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

Run `python CHECK.py` in any Python 3 environment with only the standard library. The program prints `PASS 23666 independent finite checks` on success. It checks exact elementary inequalities, finite integer-length triple equivalence, generated feasible gap vectors and the implied energy constraint, finite gamma bounds, quadrature against two exact small cases and reproducible Monte Carlo comparisons. The all-sample and limiting claims are proved analytically in `RESULT.md`; tests are finite evidence only.

The literature comparison includes a later exact-integral theorem for Pareto samples, which supplies finite-sample probabilities but not the evaluated quadratic-rate limit; it does not establish a claim of absolute historical uniqueness. The primary result is limited to independent fixed-index Pareto type-I lengths and a leading large-deviation rate.
