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

# Reproducible finite verification

All binaries are reconstructed from the embedded C++17 source files; no precompiled binaries, external datasets or external libraries are required. Commands (on a C++17-capable compiler):

```sh
g++ -std=c++17 -O2 verify_paths.cpp -o verify_paths
./verify_paths
g++ -std=c++17 -O2 verify_topological.cpp -o verify_topological
./verify_topological
```

The output files `verify_paths.out` and `verify_topological.out` record actual executions. The first program stores a complete next-state table and uses forward path tracing and explicit group-image closure. The second independently computes the full transition table from coordinate loops, prunes vertices of zero indegree to isolate cycles, assigns transient distances by reverse topological order and calculates each symmetry orbit size from stabilizers and Burnside's lemma. Both classify all \(1048576\) states and output the same seven orbit populations, twenty-two entry-time populations, seven basin populations and twenty-three geometric classes.

State-count partition: \(1097+1047479=1048576\). Maximum entry time: \(21\), attained by \(80\) states. Largest individual basin: \(884500\), belonging to the empty equilibrium. Period-five basin mass is exactly \(40\), equal to its \(40\) periodic states, proving these cycles have no transient predecessors. The scripts provide an exhaustive *finite* certificate for this exact geometry only. Independent external review is not performed.
