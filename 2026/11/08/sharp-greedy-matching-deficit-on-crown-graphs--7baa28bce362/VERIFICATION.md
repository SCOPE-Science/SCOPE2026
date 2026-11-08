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

# Verification and reproducibility

Execute `python checker.py` using Python 3.9 or later, with no dependencies. It independently computes exact rational failure probabilities from both the two-parameter common-label Markov chain and a labeled state-space recursion. The comparison covers initial sides of size two through eight. The checker also verifies finite-state probability conservation, the explicit error inequality, the two-label factorial moment bounds, and uniform maximal matching derangement counts.

The checker reports 328 exact assertions. These finite computations do not prove the unbounded-size statements: the proof uses a conditional survival bound for two labels, its convergent product, and an exact telescoping identity to obtain the asymptotic. No independent external mathematical audit has been performed.
