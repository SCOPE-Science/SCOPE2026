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

The proof applies to every integer \(k\ge3\) and is self-contained. The necessary inequality is a union-bound counting certificate over pairs of marker positions; the construction maps every weak composition of \(k-2\) to a specific pair. No finite test is used as a substitute for the infinite argument.

Standalone Python 3 code: `python3 verify.py`. Its intended output includes `EXPLICIT_CONSTRUCTION_SELECTED_H_K_3_TO_180_OK`, `PAIR_COVERING_BOUND_EXHAUSTIVE_LENGTH_8_OK`, `RECTANGLE_EQUIVALENCE_DIRECT_SUBSEQUENCE_OK`, short exact minimum lines, and `ALL_CHECKS_PASSED`. The implementation checks direct subsequences for the short regimes and algebraic counts for larger regimes; the finite parameter limits do not constitute exhaustive verification for all \(k\). The sharp leading asymptotic constant and exact general optimal lengths are not proved.
