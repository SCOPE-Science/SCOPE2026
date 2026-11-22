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

# Reproducibility and scientific boundaries
Run `python3 verify.py` with Python 3 and no third-party dependencies. The finite checker enumerates minimum dominating sets directly, reconstructs the token-slide graph and two-separated-token graph independently, checks the excess-pair bijection and all adjacency relations, compares every ordered-pair BFS distance with the lifted Möbius formula, and confirms the state counts, degrees, edge counts and self-centeredness.

The executed verification reported `ALL_VERIFY_OK: 11290 ordered source-target pairs; exact graph-to-strip isomorphism` for cycle lengths 4, 7, 10, 13, 16 and 19, using the supplied source file itself. The infinite-family assertions rest on the mathematical arguments in RESULT.md, not on enumeration. No independent mathematical audit has been performed; comparisons with unindexed literature cannot establish absolute historical priority.
