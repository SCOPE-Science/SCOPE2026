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

# Verification of the capacity-constrained recolouring theorem

Run `python3 verify_capacity_recolor.py` with standard Python 3. The program exhaustively builds every proper occupancy-limited colouring for each of 17 combinations of \(1\le n\le6\) and \(1\le q\le3\) at \(k=n+1\), omitting only \((6,3)\) due to exhaustive-search cost. Because permutations of vertices and named colours act by reconfiguration-graph automorphisms, BFS from a representative for each colour-class-size partition determines the full diameter. Every resulting diameter equals \(n+\lfloor n/(2q)\rfloor\).

The second suite tests the explicit saturated-class Euler routing algorithm and the lower-bound witness for \(1\le n\le15\), \(1\le q\le5\), and randomized legal endpoints, asserting every intermediate recolouring is legal and the bound is met. The recorded run was:

```
EXACT_ORBIT_REDUCED_ALL_PAIR_BFS_PASS cases= 17 source_state_pairs= 401984
CONSTRUCTIVE_ROUTING_AND_SHARP_WITNESS_PASS cases= 1028 path_steps= 6621
VERIFY_OK
```

These tests are finite cross-checks. The general theorem is justified by the saturation, Euler-tour, amortized episode count and lower-block argument given in `RESULT.md`. No proof assistant or independent mathematical audit was used.
