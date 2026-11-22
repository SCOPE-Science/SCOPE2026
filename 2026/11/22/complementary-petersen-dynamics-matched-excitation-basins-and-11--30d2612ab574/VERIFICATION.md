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

From this directory run:

```sh
python3 verification/check_all.py
```

Requires Python 3 and a C++17 compiler. `verification/census.py` enumerates every encoded color assignment with a global successor/indegree analysis, `verification/independent.cpp` separately rebuilds all transitions and applies Floyd's cycle algorithm from every initial state, and `verification/symmetry.py` enumerates all \(120\) graph automorphisms and their action on the \(10{,}080\) common primitive-three temporal cycles. The Python programs compare independently generated arrays and counts against the embedded `data/census.json` and `data/symmetry.json` files. The C++ code compares the full first-entry distributions and joint eventual periods against exact integer data.

An actual replay of all three programs completed successfully with the markers `CENSUS_ALL_59049_OK`, `SYMMETRY_ALL_10080_OK`, `INDEPENDENT_FLOYD_ALL_59049_OK` and `ALL_EXHAUSTIVE_CHECKS_OK`. The algorithms enumerate all \(59{,}049\) initial states and all \(120\) point permutations, not samples. The shared-oscillator set and common transitions are checked state by state, including the direct local successor-neighbor characterization. The proof of completeness rests on the stated functional-graph invariant and the intrinsic-maximal-clique characterization of the automorphism group.

The findings concern this specified finite graph and deterministic synchronous rules only; no infinite extrapolation or external independent mathematical audit is claimed. Publication priority beyond the inspected sources remains uncertain.
