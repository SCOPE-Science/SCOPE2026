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

# Numerical and algebraic verification

`check.py` is the standalone implementation of the complete inclusion-exclusion formula, the left-product formula, the transition root and the endpoint coefficient. Execute with Python 3.10 or later and mpmath 1.3 or later using `python check.py`. The checker was executed from this package source, yielding 53 passing assertions and representative exact CDF and endpoint values. The finite numerical tests include n=2,...,7 and seeded simulation comparisons; they do not prove the general theorem, which rests on the analytic Dirichlet and interval arguments in RESULT.md. No external or independent audit has been conducted. The original null is exactly centered and the filtration fully covered; alternative implementations may produce different laws.
