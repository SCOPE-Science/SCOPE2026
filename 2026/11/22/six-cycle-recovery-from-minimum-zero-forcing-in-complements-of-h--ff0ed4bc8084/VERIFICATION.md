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

# Reproducibility

The proof applies to every finite simple graph of minimum degree at least two and girth at least five. The following finite computations are illustrative consistency tests, not an exhaustive proof for all orders.

Execute in a directory containing the two source files:

```
python3 verify_python.py
g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp
./verify_cpp
```

Each program builds the seven underlying graphs directly from combinatorial definitions, checks the absence of triangles and quadrilaterals and the minimum-degree assumption, computes the complement color-change rule, enumerates every two-, three- and four-white set, and independently counts six-cycles. The Python checker uses sequential force steps and the C++ checker uses synchronous parallel force steps. Both check the first-force criterion on every three-set and the degree-and-distance-two formula. Their numerical outputs are preserved in `TEST_OUTPUT.txt`.

The seven cases include cubic examples with equal order/degree but different hexagon counts, an order-three projective plane's incidence graph with degree four, and two irregular examples. Full source code, not just an execution log, is supplied. Computations check only those cases; they cannot establish the theorem for all graphs, test historical novelty or constitute independent audit.
