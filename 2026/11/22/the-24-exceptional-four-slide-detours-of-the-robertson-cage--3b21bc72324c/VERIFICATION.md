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

# Verification scope

The proof package contains a complete edge list (`graph_edges.txt`), a Python 3 bit-mask checker (`verify_bitset.py`), and a separately implemented C++17 Boolean-array checker (`verify_independent.cpp`). Running `sh REPRODUCE.sh` from the extracted directory rebuilds all feasible minimum configurations and full shortest-path matrices and checks every exact claim against assertions.

Both programs were run successfully from the complete finite proof package. The Python checker additionally confirms graph girth five, 24 distinct validated automorphisms, the single orbit of exceptional pairs, the 36 exceptional endpoints, and a representative pair. The C++ program independently exhausts all singleton, pair and triple candidates, confirms all optimal propagation times, and recomputes both 753-state all-pairs distance tables.

**Finite limits:** all 283,128 unordered pairs are checked; no assertion concerns larger graphs. The named external sources support identification, definitions and historical comparisons, not computational outputs. Independent audit: not performed.
