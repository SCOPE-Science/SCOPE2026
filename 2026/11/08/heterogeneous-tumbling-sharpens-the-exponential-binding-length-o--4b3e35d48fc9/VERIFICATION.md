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

# Reproducible checks

Run `python3 verify.py` with NumPy and SymPy installed. The script checks the symbolic four-phase characteristic determinant and its equal-rate factorization, tests stationary phase and boundary identities in 55 numerical configurations, checks monotonicity under fixed rate sum and the singular limiting scales, and independently integrates three long event-driven realizations of the reflected separation dynamics without discretizing jump times. The check is deterministic and uses fixed random seeds; all tested assertions pass. The proof of the theorem is analytic and does not infer uniqueness or infinite parameter coverage from finite testing.

Critical equations are the Perron root equation, the cubic determinant identity, the boundary mass balance and the convexity-based ordering in `RESULT.md`. The independent audit field remains unperformed.
