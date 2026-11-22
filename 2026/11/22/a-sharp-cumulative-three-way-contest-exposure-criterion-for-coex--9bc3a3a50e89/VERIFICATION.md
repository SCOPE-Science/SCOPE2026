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

# Reproducibility and claim boundaries

The complete mathematical argument is in `RESULT.md`, equations (1)–(6). The exact-rational algebraic cross-check can be run using `python checker.py` with Python 3 and no third-party packages. It verifies the initial conservation/entropy identities with 1,200 generated cyclic three-species parameter sets and independently evaluated equations, including distinct positive birth and death rates subject to proportionality. This check passed.

The convergence iff condition relies on rigorously bounded entropy sublevels and exact integration of the Lyapunov identity; finite tests cannot verify it. The time-average theorem uses an exact bounded-log integral identity, and three-species periodicity uses the geometry of entropy level sets. No claims about nonproportional demographics, stochastic fluctuations or exact asymptotic phase are made. Independent audit and independent validation have not been performed.
