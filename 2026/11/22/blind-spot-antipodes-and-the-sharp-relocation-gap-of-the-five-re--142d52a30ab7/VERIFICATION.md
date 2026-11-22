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

# Reproducibility of the Clebsch blind-spot theorem

The six required research documents and the two scripts are included together in the delivered finding. Run each Python 3 script separately in a directory containing the extracted files:

```bash
python3 check_cayley.py
python3 check_setmodel.py
```

Both use only the standard library. Both runs were performed from the actual file paths with an exit status of zero, each printing `PASS`.

`check_cayley.py` creates the sixteen-vertex XOR graph with generators `1,2,4,8,15`; explicitly checks 40 undirected edges; exhaustively rejects all singleton and two-vertex seeds; classifies all 560 triples by the power-domination closure; verifies the blind-spot involution for all 320 minimum configurations; constructs every legal jump and slide; checks degrees and 3,360 versus 1,120 edges; and recomputes every pairwise distance, sharp diameter and unique farthest blind spot. Its source-level assertions specify all expected counts.

`check_setmodel.py` starts from a distinct graph representation on empty, singleton and two-element subsets of five labels. It independently tests the propagation closure and all seeds of size up to three. It constructs relocation graphs from direct pairwise comparisons of successful triples and independently recomputes all shortest distances. It checks the exact locality-penalty distribution and unique farthest blind-spot correspondence.

The two graph constructions are different descriptions of the same five-regular Clebsch graph. The graph is completely finite, so the enumerations are exhaustive for the stated instance. Neither program establishes results on larger folded cubes, and neither constitutes an external independent audit. Historical novelty depends on the separate literature comparison.
