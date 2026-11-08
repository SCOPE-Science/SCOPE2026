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

## Reproducible checks

Compile the standalone standard C++17 checker and run the separate Python 3 implementation:

```sh
python3 check_enumeration.py
c++ -std=c++17 -O2 check_structural.cpp -o check_structural
./check_structural
```

The Python checker exhaustively enumerates all four-subsets for even cycle orders eight through twenty-six, simulates synchronous propagation using bitmasks, reconstructs the full one-vertex-replacement graph without assuming the proposed adjacency table, and checks exact size, degrees, number of edges and every eccentricity.

The C++ checker uses an independently structured sets-and-neighbor implementation. It enumerates all four-subsets through order twenty-two, checks every predicted optimum set through order thirty, constructs the complete reconfiguration graph using set intersections, and performs a BFS from every state through order thirty.

Both checks succeeded on the included source code. The assertions cover the stated finite ranges only. The all-order conclusion relies on the proof in `RESULT.md`, notably the initial-force classification and center-coordinate lower bound together with three-consecutive-anchor upper bound. No external independent audit is asserted.
