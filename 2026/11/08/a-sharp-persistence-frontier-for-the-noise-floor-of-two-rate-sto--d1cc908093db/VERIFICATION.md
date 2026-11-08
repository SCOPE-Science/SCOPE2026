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

# Reproduction and limits

Run `python verify.py` with Python 3.10+ and SymPy 1.10+. The recorded execution passed 250 assertions: five symbolic algebraic identities (the stationary covariance system, the exact variance formula, variance-difference factorization, persistence derivative, IID specialization and determinant decomposition grouped as five tests), five exact rational identities (the four example variances and cutoff), and 240 distinct numerical recurrences of conditional Markov-state second moments.

Each finite numerical recurrence starts from zero, iterates the two-state conditional second-moment update for 4000 steps, and compares with the independent closed form. The randomized parameters are generated using a fixed seed and satisfy the strict one-step stability bounds.

The proof in RESULT.md establishes the unrestricted real-parameter inequalities; numerical checks are not evidence for an infinite universal statement by themselves. No independent external audit or publication-precedence certification has been performed.
