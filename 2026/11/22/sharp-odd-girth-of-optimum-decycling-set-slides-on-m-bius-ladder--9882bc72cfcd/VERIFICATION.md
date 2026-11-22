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

# Reproduction

Using Python 3.9 or later with only the standard library:

```sh
python3 check_construct.py
python3 check_finite.py
```

The first tests every explicit intermediate configuration for even rung counts from 4 through 100, including edge adjacency, minimum cardinality, original-graph forest, nonadjacent empty columns, at most one selected edge and pairwise distinct states. The second independently constructs the graph as a cycle with antipodal chords, exhausts all smaller-cardinality candidate subsets, and calculates shortest odd closed paths in the optimal token-slide graph for 3 to 8 rungs. The finite checks do not establish the infinite theorem; the combinatorial argument in RESULT.md does. Full publisher text of one close prior work was not accessible; this is an originality limit, not a numerical verification error.
