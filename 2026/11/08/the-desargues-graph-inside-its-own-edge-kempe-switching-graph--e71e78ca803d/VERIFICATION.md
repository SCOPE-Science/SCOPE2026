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

# Reproducibility

The `certificate.json` file gives the 32 canonical colour strings in lexicographic edge order, all 36 distinct switching edges, an explicit bijection from the 20-state component to the original Desargues graph, and the six extra edges. No external datasets, graph libraries, or internet connections are used by either verifier.

```
python3 verify_colouring.py
python3 verify_matchings.py
```

`verify_colouring.py` enumerates all \(192\) proper colourings with three named colours by constrained edge labelling, quotients by all six global permutations, enumerates each full bichromatic cycle, and checks every certificate item. It verifies the two possible colour-pair cycle profiles and the adjacency isomorphism.

`verify_matchings.py` enumerates all \(60\) perfect matchings by smallest-uncovered-vertex branching, traces the complementary even two-factors, generates all unlabelled three-matching partitions, and reconstructs the switching adjacency by matching symmetric differences. It checks the complementary cycle table, state census, complete adjacency list and supplied isomorphism without relying on the first algorithm's backtracking or colour-swap routine.

Expected independent success lines:

```
COLOURING_ENUMERATION_PASS named=192 unlabelled=32 edges=36 graph=GP(10,3)+6K2
PERFECT_MATCHING_ENUMERATION_PASS 60 matchings=(36 double-10,24 Hamilton)
MATCHING_TOGGLE_PASS 32 factorisations, 36 moves, 20-state GP(10,3), six K2
```

Scope is finite; verification is exhaustive in that finite domain, not extrapolation to an infinite family. The exact certificate includes only states defined by the stated graph convention. External scholarly evaluation has not occurred.
