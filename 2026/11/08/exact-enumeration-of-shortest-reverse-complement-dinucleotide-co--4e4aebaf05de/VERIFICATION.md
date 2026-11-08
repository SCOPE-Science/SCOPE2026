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

# Computational verification

The final embedded versions of `verify_direct.py`, `verify_graph.cpp`, and `catalog.txt` were executed or consumed directly, independently of any earlier temporary output.

```sh
python3 verify_direct.py
# DIRECT_VERIFY_OK rooted=5440 necklaces=544 physical=272 classes=37
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_graph.cpp -o verify_graph
./verify_graph
# GRAPH_VERIFY_OK balanced=24 connected=24 total=544 groups=8x12+8x20+8x36
```

`verify_direct.py` exhausts all rooted DNA words of exactly ten letters, tests the ten reverse-complement dinucleotide classes including the wraparound window, and checks catalog completeness, Burnside fixed points, and symmetry-orbit sizes. `verify_graph.cpp` independently exhausts all sixty-four fixed-edge selections, checks balance and directed spanning-tree cofactors, and computes all Euler-circuit multiplicities. The equality of both totals is an explicit cross-check, not an assumption.

The infinite-length version of the problem, all longer k-mer orders, linearized probe coverage, and independent historical priority have not been verified and are not claimed.
