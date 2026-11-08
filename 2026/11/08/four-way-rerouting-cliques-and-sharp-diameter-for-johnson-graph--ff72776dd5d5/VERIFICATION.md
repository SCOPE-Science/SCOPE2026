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

The theorem is proved for all Johnson graphs and all distinct endpoints in `RESULT.md`, not by extrapolating the finite tests.

To reproduce the two independent finite checks, use Python 3 with no third-party packages:

```sh
python3 verify_direct.py
python3 verify_cayley.py
```

`verify_direct.py` explicitly enumerates every shortest path in the Johnson graph with antipodal endpoints in \(J(2d,d)\), for \(1\le d\le4\). For each order it constructs all rerouting edges directly from path-vertex sequences and verifies cardinality, degree, edge and triangle counts, connectivity, and eccentricity. `verify_cayley.py` instead enumerates the Cayley moves on paired permutations for \(1\le d\le5\), checks all reachable states and the exact eccentricity, and then verifies the common bubble-sort comparator schedule on 400 deterministic randomized pairs at every order \(2\le d\le10\). Both produce `*_ALL_PASS` when all assertions hold.

The test families have, respectively, \((d!)^2\) states. For \(d=4\), the direct test enumerates 576 paths, 2592 transitions and 1728 triangles. For \(d=5\), the independent Cayley test traverses 14,400 states and confirms radius/diameter 10. The arguments for arbitrary \(N,k,A,B\), the clique uniqueness, and the infinite diameter formula are mathematical proofs. Independent audit has not been performed.
