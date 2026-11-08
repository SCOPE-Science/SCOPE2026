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
# Verification of the multipartite TOI-coalition spectrum

The accompanying `verify.py` is a standalone Python 3 program using the standard library only. Run `python verify.py` in the directory containing this file. It builds the adjacency masks of each graph directly and tests total domination and complement independence for each candidate set; it does not use the theorem's structural TOIDS criterion as an oracle.

It then exhaustively constructs unordered vertex partitions and tests each class and every candidate coalition partner from the graph definitions. It checks all 67 sorted positive part-size profiles with at least three parts and total order at most nine. The accepted partition totals are 8,199 two-class partitions and 5,140 three-class partitions, with no other class counts. For three-class partitions it independently checks whether the coalition graph is a path or a triangle and whether the pure-class criterion holds. The program also evaluates the closed formulas for a larger unbalanced vector without brute-force enumeration.

Expected terminal lines:

```text
EXHAUSTIVE_MULTIPARTITE_PROFILES_OK 67 partitions_accepted 13339 two_blocks 8199 three_blocks 5140
LARGE_PROFILE_FORMULAS_OK (2, 4, 7, 10) 4193135 150666
VERIFY_OK
```

The unrestricted proof is in `RESULT.md`. The brute-force run is finite corroboration only; no independent mathematical audit has been performed.
