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

# Verification evidence and limits

The proof is a direct analytic derivation, not a probabilistic experiment. The key checked steps are the coordinate orthogonality inequality, a sharp weighted Cauchy envelope with explicit equality witnesses, a constrained convex minimization, and the lower bound from a uniform reference and its least-probability coordinate. The two limiting angles and the dimension-dependent transition are treated explicitly. Supplementary reproducibility: execute `python check_minimax.py` with a Python 3 standard library, which passed 11,050 numerical/algebraic assertions during preparation. The checker does not prove the infinite-dimensional quantifiers (the theorem itself is finite-dimensional but for arbitrarily many dimensions and continuum parameters); the printed checks do not substitute for the displayed analytic proof. No external mathematical audit or independent validation was conducted. The source comparison is finite and does not establish absolute priority.
