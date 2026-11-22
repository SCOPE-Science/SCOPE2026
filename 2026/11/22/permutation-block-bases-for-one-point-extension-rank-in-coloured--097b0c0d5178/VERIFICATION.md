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

# Verification of the finite coloured-order rank theorem

The supplied `verify_colored_rank.py` uses two independently implemented recurrences. `rank_by_game` applies the one-point-extension definition recursively to every marked subset of each host word. `interval_rank` implements the separate mathematical gap-word recursion. They agree for all 2,127 host words (one colour through length 10, two through length 9, and three through length 6), across every marked state of each host.

For exact minimum-host classification, the checker independently enumerates all words of minimum length for the cases \(q=2,\ t\le3\) and \(q=3,\ t\le2\) and compares them as sets to the recursive grammar, also testing the one-colour singleton extremizer. The output includes `EXTREMA 2 3 14 128` and `EXTREMA 3 2 9 216`.

The predicate `is_subsequence` is a direct greedy positional matching test, distinct from the rank implementation. It confirms the basis equivalence on 69,029 cases and checks 180 additional larger grammar-generated extremal words with two, three and four colours.

Reproduction: with Python 3 and only its standard library, run `python3 verify_colored_rank.py` from the directory containing this file. Successful completion prints `ALL_CHECKS_OK`. The unbounded mathematical claim is justified by the complete proof in `RESULT.md`, not by these finite tests. No independent expert or external certification is represented.
