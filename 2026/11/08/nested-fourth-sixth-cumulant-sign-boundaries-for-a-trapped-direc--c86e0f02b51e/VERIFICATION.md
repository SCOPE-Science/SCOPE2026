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

The self-contained `check.py` reconstructs the stationary generator-moment system and verifies the exact rational identities with SymPy. Successful execution reports `PASS` after symbolic and five exact-rational independent matrix checks.

The proof is algebraic and universal: it uses the stationary Markov generator, the triangular recurrence, strictly positive rational denominators, and a quadratic polynomial with strictly negative derivative for nonnegative reversal rates. Finite computational examples are verification aids, not evidence of an infinite parameter sweep. No independent scientific audit has been performed.
