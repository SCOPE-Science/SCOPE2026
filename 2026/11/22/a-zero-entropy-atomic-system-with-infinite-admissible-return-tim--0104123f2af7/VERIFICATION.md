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

# Reproducibility and limits

The theoretical proof is in `RESULT.md`. The self-contained Python 3 program `checker.py` uses only Python's standard library and may be executed as `python3 checker.py`.

It checks three exact claims on finite truncations with cycle cutoffs 16, 22, and 29 and word lengths 1 through 13: the shortest overlap return equals 1, the minimum compatible period of a single marker, or the period identified by two markers; the maximal return time is at most the word length and all individual cycle points are identified by length twice their cycle length; and the finite-truncation analog of the exact moment identity equals a direct sum of rational point masses. The run passed 921 word-atom overlap comparisons and 468 exact rational identities across three weight exponents and four moment orders.

These are finite checks only. The infinite assertions for arbitrary real exponent rely on a direct combinatorial classification, monotone convergence, and comparison of power sums, all supplied in `RESULT.md`. External independent mathematical audit was not performed.
