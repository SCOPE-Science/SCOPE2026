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

# Reproducibility and checks

The exact proof is in `RESULT.md`. Execute `python3 verify.py` with Python 3 and no third-party dependencies. The code applies the edge-adjacency strong-majority test directly and constructs codes using actual graph distances. Its final run reported:

```
DIRECT_ALL_COLOURINGS_EXHAUSTIVE_ZERO_OK K5
DIRECT_ALL_COLOURINGS_EXHAUSTIVE_ZERO_OK K44
ALL_SINGLETON_CODES_AND_EDGE_TESTS_OK Q4 16 four_cycles 24
ALL_SINGLETON_CODES_AND_EDGE_TESTS_OK switched_Q4 8 four_cycles 22
ALL_496_TWO_POINT_CODE_CANDIDATES_OK 40
VERIFY_OK
```

Finite checks include exhaustive named edge colourings for the two stated small graphs, exhaustive singleton centers in both order-16 examples, and the complete 496 two-point candidates for the order-32 cover. They are not a proof for arbitrarily large graphs. The unrestricted proof uses endpoint colour-degree equations, the connected five-class transition structure, reconstruction of distance layers, and exact edge-counting; those arguments do not require computational extrapolation. Independent mathematical assessment has not been performed.
