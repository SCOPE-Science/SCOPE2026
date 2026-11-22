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

Reproduction: run `python3 check.py` in the same directory as this document, using only Python 3's standard library. The exact enumeration evaluates every mapping of orders 1 through 6, the cycle-set cardinality, its least label, the exact core probabilities, all minimum tails, and conditional rising moments of orders 1 through 5. Outcome: 244 exact assertions passed. Numerical checks for sizes up to 100000 are diagnostic only and do not establish any asymptotic theorem.

The independent mathematical audit has not been performed. The rigorous proof is in RESULT.md. The limit law requires Rayleigh core convergence, conditional hypergeometric-to-Poisson convergence, and tightness; the variance coefficient requires controlling the entire harmonic range through size \(\sqrt n\); higher moments require a dominated-convergence argument. No simulation alone certifies these steps.
