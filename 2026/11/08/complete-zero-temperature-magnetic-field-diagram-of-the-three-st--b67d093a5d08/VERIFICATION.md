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

The two self-contained verifiers use the same explicitly defined dodecahedral graph, but eliminate opposite halves first. They execute exhaustive integer counting for every fixed preferred-color occupancy and assert the entire resulting table.

```sh
g++ -std=c++17 -O2 verify_inner_ring.cpp -o verify_inner_ring
./verify_inner_ring
python3 verify_outer_pentagons.py
```

Expected final printed markers are `INNER_RING_DP_OK` and `INDEPENDENT_PENTAGON_OK`. The Python verifier additionally compares the piecewise ground sectors at representative interior and boundary fields using exact rational arithmetic. Its sector data and the C++ sector data match `SECTOR_TABLE.csv`.

The enumeration is finite and exhaustive because fixing all ten inner or all ten outer vertices partitions the complete \(3^{20}\)-configuration space into disjoint subproblems. The recurrence traverses all three colors at each remaining vertex and aggregates every tie, with 64-bit integer counts. This is a certificate of the stated finite claims, not evidence for any infinite-size behavior. Independent external validation has not been performed.
