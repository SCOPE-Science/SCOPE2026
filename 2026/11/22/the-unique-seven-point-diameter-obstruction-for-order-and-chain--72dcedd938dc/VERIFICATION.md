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

To verify the finite classification, run `python3 CHECK.py` in the same directory as this document. The program requires no third-party packages. It constructs complete topological-order-labelled poset sets, detects the five-element obstruction, builds both polytope graphs using standard published adjacency criteria, and computes exact breadth-first distances and canonical graph-isomorphism relation codes.

The executed output was:

```
4 40 0 0
5 357 1 0
6 4824 66 0
7 96428 3705 46
Two isomorphism types, exchanged by duality; Lee P1 representative.
PASS
```

This verifies the finite certificate and the source example's diameters, not any claims for eight or more poset elements. Numerical approximate checks are not used. The entire enumeration's correctness relies on the stated, established equivalences between polytope edges and connectivity of symmetric differences, and on every finite poset admitting a linear extension. Historical priority and independent mathematical verification are outside this execution.
