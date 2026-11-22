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

The proof derives a Poisson-to-Gamma mixture representation of each step response, an exact Poisson-pmf error formula, strict monotonicity of each interior critical-point equation, a signed-measure equality argument, and a moderate-deviation location estimate. The all-\(n\) conclusions and the logarithmic limit rely on those arguments, not on finite numerical sampling.

Reproduce finite crosschecks with `python check_szasz.py` (Python 3.10+ and SciPy). The tests compare direct numerical integration with the distinct Gamma-Poisson formula on 768 cases, inspect 110 numerically resolved cell maxima, and test 36 four-jump BV bounds. For roots closer than machine resolution to a cell endpoint the checker **skips that root**, rather than mistaking floating-point resolution for a mathematical counterexample or exhaustive verification. Such roots are covered in the analytic argument.

The numerical checks are finite sanity tests. No independent audit has been performed. Historical equivalence checks cannot certify priority.
