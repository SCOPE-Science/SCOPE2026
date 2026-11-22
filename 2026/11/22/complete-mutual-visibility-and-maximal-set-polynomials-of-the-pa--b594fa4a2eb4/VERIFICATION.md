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

# Verification of the finite exhaustive census

There are \(2^{18}=262144\) candidate subsets. `visibility_paths.cpp` uses shortest-path masks and tests every subset; `visibility_bfs.cpp` independently tests shortest distance with selected interior vertices blocked and enumerates every feasible subset by extension. They agree in every one of the 262,144 Boolean states as independently represented by the deterministic sequence fingerprint `35086ad4bd0f946` (FNV64). Coefficients through size 8 are \(1,18,153,762,2340,4374,4605,1998,36\) with zero coefficients after size 8; facets occur only in sizes \(6,7,8\), with counts \(63,1710,36\). Both sources were compiled with `g++ -O3 -std=c++17` and replayed from the artifact's `verification/` source directory. The path-based source reconstructs the 1,809 maximal masks in `maximal_sets.txt`.

The pure-Python `symmetry_orbits.py` then enumerates the explicitly described 108 incidence-preserving affine maps and composes each with one incidence-reversing polarity; it verifies all 216 vertex permutations preserve the incidence graph, then partitions every regenerated maximal mask into exact orbits. It returns two, twelve, and one orbit for the three facet sizes; the sole largest orbit has 36 members. The separate `count_automorphisms.py` uses exhaustive distance-preserving-bijection backtracking and finds exactly 216 automorphisms, verifying the asserted group is complete. Transcripts of all four runs are included. Repeat in the `verification/` directory using the commands in `RESULT.md`. No external graph-science datasets, precomputed state arrays, or unprovided source files are required.

The proof rests on explicit finite exhaustive loops, whose coverage follows from the mask domain and the downward closure of mutual visibility. The numerical outputs alone would not establish correctness without the source and proof of the visibility criterion. This check does not establish global priority, infinitary generality, or independent external certification.
