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

# Reproducing the finite proof

Run:

```sh
python3 star_verify.py
g++ -O3 -std=c++17 star_cpp.cpp -o star_cpp
./star_cpp
```

Both programs generate graph incidences directly, enumerate every canonical 3- and 4-color star coloring, reconstruct all named optimal colorings and all single-vertex moves, and perform complete component traversal. No outside graph data or package is needed; the Python code uses only the standard library and the C++ code uses C++17. Output recorded from successful local executions is preserved in `verification_output.txt`. The Python proof explicitly checks that each nine-vertex component has an alternating eight-cycle rim, characterizing the \(P_3\square P_3\) template. The C++ implementation uses an independently reordered graph traversal. Runtime depends on ordinary local hardware; both were executed to successful `PASS` completion rather than inferred from compilation alone.

Unproved limits: neither program proves any claim for arbitrary cubic graphs or additional palettes. The reproducible exhaustive proof checks four specified finite graphs only. Independent human scholarly assessment is not performed.
