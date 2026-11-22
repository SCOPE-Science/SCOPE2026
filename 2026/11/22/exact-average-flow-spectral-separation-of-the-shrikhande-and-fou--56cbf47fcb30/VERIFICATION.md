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

The two input graphs are defined by integer coordinate differences modulo four, with no external graph data. `verify.py` computes all rooted simple paths by exact visited-subset/last-vertex dynamic programming. The recurrence sums paths after every extension by one previously unseen adjacent vertex. `verify.cpp` independently enumerates each complete rooted simple path by recursive depth-first search and accumulates exact 64-bit counts. Neither program uses floating point computations, and no partial search is presented as exhaustive.

Reproduction commands:

```sh
python3 verify.py
c++ -O2 -std=c++17 verify.cpp -o verifier
./verifier
```

The exact expected totals are 13,991,682 paths and 177,310,488 total path edges for the rook graph, and 14,029,326 paths and 177,724,236 total path edges for Shrikhande. The Python script checks all fifteen coefficients, first discrepancy at length seven, 6-regularity and two common neighbors per vertex pair, local neighborhood triangles, and the exact reduced rational difference; the C++ implementation independently checks full path totals and weighted sums. These checks were executed successfully on the embedded source files before packaging. The eigenspectrum proof follows directly from the displayed common-neighbor matrix identity, so spectral floating-point numerical diagonalization is not relied on.

No assertion is made about graphs of other parameter sets. Independent mathematical audit has not been performed.
