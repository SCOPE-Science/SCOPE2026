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

The standalone program `verify_hop_tr.py` was executed from its actual saved source bytes and returned:

```text
VERIFY_OK profiles=28 labels=523422 valid=376483 independent_shortest_paths=PASS full_integer_polynomials=PASS linear_matching_defect=PASS minimum_placements=PASS
```

It constructs each graph from the bipartite edge definition, deletes matching edges, performs independent breadth-first search for every vertex, and checks each ternary labelling under the original distance-two defender and positive-support adjacency conditions. The enumerator formula is evaluated by a separate standard-library integer-polynomial calculation, and all coefficients are compared. The parameter range is \(3\le a\le b\le5\) and \(0\le t\le a\), giving 28 profiles and 523,422 evaluated labellings. The verifier checks the weight-four count and the integer coefficients without relying on the case classification from the proof.

Finite exhaustive checks at small parameter sizes are not an all-size certificate; the general result follows from the written distance argument and bad-event inclusion-exclusion. The verification is not an independent mathematical audit.
