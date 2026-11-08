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

# Reproduction and verification

Run `python3 verify.py` in the directory containing this package. The only dependency is Python 3's standard library. The script implements rational Gaussian elimination and exact policy iteration, checks that each computed value vector satisfies every Bellman equality, and inspects **all** offered-neighbor pairs with unequal graph distances. Each connected labeled undirected graph with 2–6 vertices appears as an edge bitmask and an arbitrary target may be relabeled to vertex 0. The counts by graph order are 1, 4, 38, 728, and 26,704; the total is 27,475.

Actual local execution returned:

```
EXACT_FAMILY_IDENTITIES_OK K=0,1 AND K=2..17 SEVEN_VERTEX_GAP 4/415
EXHAUSTIVE_CONNECTED_LABELLED_ROOTED {2: 1, 3: 4, 4: 38, 5: 728, 6: 26704} TOTAL 27475
VERIFY_OK
```

The family test checks additional integers for independent reproduction of the rational formulas. The proof of **all** integer parameters \(k\ge2\), however, is the symbolic elimination and positivity argument in `RESULT.md`; no finite list of tested values establishes an infinite statement. Likewise, the small-graph minimality is finite but exhaustively covered by construction of every labeled edge mask, not inferred from a sample. The script has been locally replayed, but its correctness has not been assessed through an independent external audit or proof assistant.
