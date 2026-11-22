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

# Reproducibility and checked limits

The two standalone programs are `verify_tori.py` (Python 3 standard library) and `verify_boundary.cpp` (C++17 standard library). Both contain the identical explicit 36-edge graph list and reconstruct their own exact integer calculations without external data files or network access. The first verifies the graph's eight triangles, its cube quotient, the 1,350 relevant simple cycles and 1,656 unordered disjoint-cycle triples, and sparse degree-three signed product cycles. It asserts the integer unit-pivot torus-rank filtration and prints four basis tori containing 12-cycles. The second constructs the full reduced Świątkowski differential at weight three and eliminates it with integer unit pivots, asserting ranks 16,192, 39,744 and 16,096.

Execution:

```
python3 verify_tori.py
g++ -O3 -std=c++17 verify_boundary.cpp -o verify_boundary
./verify_boundary
```

Both commands were executed successfully with the assertions enabled. The markers are `TORUS_INTEGER_UNIT_BASIS_OK` and `BOUNDARY_INTEGER_UNIT_PIVOTS_OK C3=16192 C2=39744 rank=16096 nullity=96 peak=1`. These are exhaustive checks for the one fixed graph, not extrapolations from tests of smaller graphs. Correctness also uses the published equivalence between the chain model and unordered graph configuration spaces. Independent mathematical validation is not performed. Lower-degree homology and other particle counts were not computed.
