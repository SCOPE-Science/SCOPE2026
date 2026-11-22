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

# Finite verification

The exact public certificate consists of `check_cpp.cpp` and `check_python.py`.

* `g++ -O2 -std=c++17 check_cpp.cpp -o check_cpp && ./check_cpp` exhausts all sixteen-vertex masks, reconstructs both concept families by maximality and domination, enumerates all Boolean traces, checks four complete face-support characterizations, checks mod-two boundary ranks and confirms the periodic torus triangle list. Expected marker: `SHRIKHANDE_ROOK_DUAL_SHATTER_PASS`.
* `python3 check_python.py` requires `networkx` and independently constructs all concept sets by maximal cliques of original and complementary graphs, compares all supports through size four, and independently computes mod-two chain ranks. Expected marker: `INDEPENDENT_GRAPH_CLIQUE_SHATTER_PASS`.

All tests were performed on the embedded source files after package extraction. Size-four checks plus hereditary shattering exclude every larger support. This is an exhaustive finite verification, not an independently performed mathematical audit or a result for unspecified graphs.
