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

The accompanying standalone Python 3 program `verify_cycle_fault.py` uses only standard-library functions. Run `python verify_cycle_fault.py` in the same directory as this file.

The completed local replay produced:

```
CYCLE_SQUARE_EDGE_FAULT_VERIFY_OK: 112 independently generated finite instances (n=9..64, both edge orbits)
```

For every tested order and edge orbit it independently forms the graph's open neighborhoods; enumerates all faces; validates each prescribed elementary collapse pair by checking **all** containing cofaces in the current complex; compares the resulting complex with the exact punctured torus model; checks six-cycle links and oriented integral surface cancellation; collapses all remaining triangles; checks connectivity, Euler characteristic and circle rank; and independently performs exact binary boundary reduction on the original faulted complex. The original f-vector is \((n,4n-2,4n-6,n-2)\) and the reduced Betti ranks over \(\mathbb F_2\), from degree zero to three, are \((0,3,0,0)\).

This finite replay is a check of the combinatorial construction, not an infinite proof. The general claim is proved by the uniform index formulas and dual-graph argument in RESULT.md. No independent external verification has been performed.
