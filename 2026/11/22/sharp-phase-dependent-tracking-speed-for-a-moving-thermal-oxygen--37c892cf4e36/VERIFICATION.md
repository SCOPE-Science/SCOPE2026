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

# Reproducibility and verification boundaries

Run `python verification.py` using a standard Python 3 interpreter. The source is standalone and uses only the standard library. The last package-path execution reported 4,541 passing deterministic supplementary assertions, covering numerical root/supremum agreement, representative ordered-phase pairs, sharp feasibility endpoints, near-feasibility scaling, the near-constant-depth limit, and a physical-unit example.

The proof does not rely on numerical checks. The one-dimensional max/min result is established symbolically via an explicit distance-envelope selection. The code verifies examples and randomized parameter families but cannot establish completeness, exact algebraic equality at all real parameters, or literature priority. The model does not measure or predict actual fish behavior.
