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

The derivation uses stationary Markov-generator equations and exact factorization of a quadratic characteristic polynomial. In the included `checker.py`, exact rational stationary-moment identities, the derivative recurrence, cancellation formulas, and the fourth cumulant are checked on a finite rational parameter grid. Matrix exponentiation and direct residue evaluation agree at five nonnegative lags per parameter case. The current replay passed 1,050 parameter cases. Finite checks do not prove parameter-uniform results; that is provided by the analytical proof in `RESULT.md`.

No inference stability or experimental data were examined. Independent scientific audit has not been performed.
