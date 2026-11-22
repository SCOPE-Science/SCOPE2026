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

# Reproduction of the finite classification

The finding concerns the graph on two labelled layers of nine vertices and a single replacement of a selected vertex, not adjacency-restricted sliding. The exact source files are `exact_hitting_census.cpp` and `direct_trace_census.py`. On a system with C++17 and Python 3.10 or later, run:

```sh
g++ -O2 -std=c++17 exact_hitting_census.cpp -o exact_hitting_census
./exact_hitting_census
python3 direct_trace_census.py
```

The C++ checker constructs all eighteen neighborhood bitmasks from the complete specified edge list, adds all 153 symmetric-difference constraints, tests all 262,144 vertex subsets, and checks the full optimum one-exchange graph. The Python checker independently constructs eighteen neighborhood traces for every subset of cardinality up to seven (63,004 cases); it checks nonemptiness, trace uniqueness, optimum exchanges, component degrees and edges, six dihedral orbits and preservation of adjacency. Both source implementations were executed successfully and produced the declared values: optimum size 7, 90 optimum codes, 81 exchange edges, component partition \(9(K_1\vee(2K_2))\sqcup9P_3\sqcup9K_2\).

Every loop has a stated finite search domain. No partial search, sampling, solver timeout, unchecked numerical approximation, machine-assisted infinite proof or independent external validation is asserted. A manual verification can inspect the two different finite acceptance predicates and the short mathematical reduction in RESULT.md. The result does not extend to other cycle lengths, token slides, or erasure-resilient codes.
