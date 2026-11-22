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

# Verification

Execute the included standard-library-only program from this package:

```sh
python verify_voltage_graph.py
```

This enumerator was run and passed all seven pairs \((q,m)=(3,2),(3,3),(3,5),(4,2),(4,4),(5,3),(6,2)\). It enumerates vertices and edges, rejects every potential triangle, checks cyclic edge invariance and the free vertex action, computes the connected orbit graph and its cycle rank, and checks all face numbers and the Euler characteristic of the quotient-metric flag complex. These are independent finite sanity checks of the formulas, not exhaustive proof of the infinite family.

The general proof uses an inconsistent voltage around each three-color triangle to rule out triangles in the cover, connectivity of the regular cover via a monodromy-one loop, identification of the quotient graph, the standard join-of-zero-spheres description, and the standard two-periodic resolution of the finite cyclic group to handle coefficient fields and continuation maps. All boundary scales use the inclusive convention. The result is not an external certification or independent mathematical audit.
