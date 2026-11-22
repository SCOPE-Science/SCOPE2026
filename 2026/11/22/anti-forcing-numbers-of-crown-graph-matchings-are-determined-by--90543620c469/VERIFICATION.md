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

# Verification record

The symbolic proof establishes an exact all-order bijection between a selected matching's competing matchings and directed cycles of the contracted allowed-arc graph; optimum deletion equals total allowed arcs minus maximum acyclic arcs. The missing-arc directed cycle cover forces at least one missing forward arc per cycle. Reversing each cycle attains that lower bound. Hence all integer \(n\ge3\) cases follow from a constructive argument, not extrapolation.

## Reproducible test
Run `python3 checker.py` from the same extracted directory. The program uses only the Python standard library and reconstructs the definitions. For every derangement through order six, it calculates the minimum number of backward allowed arcs over all total orders and compares the formula. For orders three and four, it also enumerates competing perfect matchings and tests deletion subsets directly against all differences, without using the digraph result. At order seven, it counts the predicted cycle-type distribution but does not search every order; this is not presented as a seventh-order optimization check.

Expected output:
```
3 2 [(1, 2)] passed True
4 9 [(3, 6), (4, 3)] passed True
5 44 [(6, 24), (7, 20)] passed True
6 265 [(10, 120), (11, 130), (12, 15)] passed True
7 1854 [(15, 720), (16, 924), (17, 210)] passed True
VERIFY_OK
```

These finite checks validate stated boundary cases and support, but do not independently certify all infinite cases. Publication priority also remains provisional. No independent audit has been performed.
