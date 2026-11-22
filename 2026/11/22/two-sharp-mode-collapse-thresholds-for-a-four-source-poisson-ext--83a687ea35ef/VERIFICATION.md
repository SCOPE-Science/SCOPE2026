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
Run `python3 verify.py` in a directory containing the standalone checker (requires SymPy). The checker derives the positive-root sextic from the paired Poisson factors and verifies the full polynomial parameter discriminant, center factor, algebraic uniqueness conditions and exact Sturm counts at squared heights \(q=1,2,5\). These are the finite exact certificates used by the continuous-parameter proof; decimal roots serve only presentation. No finite grid search was used as proof of the continuum result. The result is restricted to horizontal modes of four equally weighted sources. Independent mathematical audit has not been performed.
