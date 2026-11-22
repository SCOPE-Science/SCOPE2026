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

# Verification of the ternary three-cube classification

The computational theorem concerns the fixed, labeled graph on \(\{0,1,2\}^3\) with Hamming-distance-one adjacency. Verification uses only Python 3's standard library and the files embedded beside this document.

Run `python3 verify_bitmask.py` and `python3 verify_symmetry.py`. The first exhausts all 27 singleton sets, 351 pairs and 2925 triples, computes power domination by bit-mask closure, builds both 1296-vertex relocation graphs, and performs two complete all-state BFS sweeps over the 839160 unordered pairs. The second independently rebuilds the original graph with coordinate tuples and sets, enumerates the 1296 automorphisms and all ten triple orbits, computes propagation separately, and counts metric distances and same-pair penalties by symmetry-orbit BFS. Both check the exact three successful types and their full distance distributions.

Expected terminal success markers are `BITMASK_OK` and `SYMMETRY_OK`. Orbit representative and forcing-step data appear in `orbit_table.json`. The two algorithms have different state representations and shortest-path counting methods, reducing shared implementation risk. Their exhaustive finite checks supply the proof for this one 27-vertex graph, not for any unbounded parameter family. Human/independent audit remains unperformed, and no claims of independent certification are made.
