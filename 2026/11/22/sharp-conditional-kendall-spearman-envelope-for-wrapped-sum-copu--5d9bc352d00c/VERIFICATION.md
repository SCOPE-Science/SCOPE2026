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

# Reproduction and verification

Run `python check.py` with Python's standard library. It constructs piecewise-constant probability generators with `fractions.Fraction` and computes the exact moments and centered CDF norm by polynomial integration. In this execution its report was:

`PASS: 4444 exact-rational/randomized consistency assertions.`

The executable checks the centered-uniform positive-rho equalities, exact prescribed-rho negative approximation sequences, strict negative branch, and 1800 randomly seeded piecewise generator distributions against the asserted upper envelope. Exact fractions are used for the algebraic branch and moment constraints; the radical positive-rho comparison uses floating-point only as a diagnostic. No finite experiment establishes the infinite-dimensional statement. The mathematical proof is in `RESULT.md`, specifically the Cauchy–Schwarz argument, exact fixed-moment endpoint sequence, and nonnegative obstacle-sign comparison. Original published identities used at the proof's start are in the cited 2025 source, Propositions 4 and 5.

Limitations: no lower envelope, no classification for all axis-reflection signatures, no independent audit and no exhaustive publication-priority certificate. Some relevant mathematical literature may not be indexed by the consulted searches.
