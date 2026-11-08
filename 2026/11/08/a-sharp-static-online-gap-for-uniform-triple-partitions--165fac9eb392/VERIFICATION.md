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

# Reproduction and boundaries

Run `python3 CHECK.py` with Python 3.10 or later, requiring no external packages. The script enumerates all partitions into triples by choosing the smallest remaining vertex first, derives pair-answer masks, enumerates all candidate supports occurring inside an all-positive hypothesis, checks full trace sets, and computes exact complete binary decision-tree feasibility using memoized recursion. Every shattered support must occur in an all-positive hypothesis; accordingly the candidate enumeration is exhaustive.

The checks cover all supports for three, six and nine vertices; exhaustive online depths for six and nine vertices; and the minimum trace multiplicity on the constructed strong witness for six, nine and twelve vertices (the twelve-vertex check does not enumerate all supports). Successful output ends with `TRIPLE_BLOCK_SHATTERING_AND_ONLINE_PASS`. The general theorem for arbitrary multiples of three is proved in the accompanying result; finite checks do not replace that argument. No independent mathematical audit has been performed.
