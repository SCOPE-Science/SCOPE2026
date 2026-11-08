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

The source programs are `census_cpp.cpp` (C++17; complete functional graph via indegree elimination) and `census_python.py` (Python standard library; complete forward-orbit path memoization). Their full recorded output is in `census_cpp.json` and `census_python.json`. Execute `python3 verify.py`; it compiles and executes the first program and executes the second, compares both outputs with the bundled records, and checks exact equality of all 33 nonzero time/period classes, basins, primitive-cycle populations, maximum entry time, symmetry orbit sizes, representative excitation profiles, and per-vertex long-orbit frequencies. The recorded successful run is in `verification_output.txt`.

The graph has exactly twelve vertices and eighteen edges; its vertices are the directed arcs of the complete graph on four points, connected by same-tail triangular adjacencies and reverse-arc matching edges. Both implementations construct this graph independently from this definition. The state encoding enumerates every integer between zero and \(531440\); no trajectories are sampled or pruned by an assumed time bound. The full long-period symmetry orbits are generated from all \(24\) permutations of the base tetrahedral labels. By a graph-theoretic argument using the four intrinsic triangles, these are all automorphisms.

The two separately structured algorithms agree on the exact periods \(1,3,4,6,8\); cycle counts \(1,3108,6,12,6\); basin counts \(52677,340848,4656,127116,6144\); maximum preperiod \(10\) attained \(384\) times; and one spatial orbit for each of periods \(4,6,8\). All period-four and period-six cycles excite each vertex once per full cycle, and all period-eight cycles excite each vertex twice. The source and output paths are part of this package and require no remote code or unavailable data.

This is a finite exhaustive certificate, not a proof of historical uniqueness or a claim of peer or independent formal verification. It does not classify the spatial action on the \(3108\) period-three cycles or generalize to larger graph families.
