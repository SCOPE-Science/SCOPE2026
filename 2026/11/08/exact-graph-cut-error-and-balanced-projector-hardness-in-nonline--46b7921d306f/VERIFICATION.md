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

The standalone `CHECK.py` uses exact rational arithmetic to construct the two projected propagators and the first parareal iteration, and checks their residual vectors against the theorem. It also exhaustively compares forest bisections with an independently implemented cardinality-indexed dynamic program on small instances.

Execute `python3 CHECK.py` from the extracted directory. The recorded invocation returned `VERIFY_OK: 430 exact split/modified recurrences and forest cut tests; 6 balanced-projection comparisons`.

These computations are finite checks. The all-graph identities follow algebraically from the recurrence, the asymptotic statement from exact expressions, and the hardness statement from a polynomial-time reduction to the classical minimum-bisection decision problem. No independent mathematical audit has been performed.
