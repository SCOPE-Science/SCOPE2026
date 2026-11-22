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

# Reproducibility and check limits

Run the two standard-library scripts with Python 3.9 or later:

```
python3 verify_permutations.py
python3 verify_cube_paths.py
```

`verify_permutations.py` checks all unordered pairs of forbidden proper nonempty subsets up to coordinate relabeling. Every orbit is classified by the cardinalities of the two forbidden sets and their intersection. It enumerates all \(n!\) permutations, builds the full adjacent-position-swap graph, removes disallowed prefixes, and counts components. Expected orbit counts in dimensions three through eight: 4, 10, 19, 32, 49, 71. The only disconnected orbit in that range occurs at dimension three with cardinalities \((1,2,0)\) and has two one-vertex components. It additionally compares every entry of the ten-row dimension-four table in `RESULT.md` against hard-coded expected counts.

`verify_cube_paths.py` independently enumerates all length-\(n\) monotone cube paths as sequences of bitmask vertices, compares each pair of paths by their entire sequence of intermediate nodes, and builds one-vertex rerouting adjacency directly. It checks **every** fault set of sizes zero, one and two in dimensions two through six. Counts of such fault sets for \(n=2,3,4,5,6\) are respectively 4, 22, 106, 466, 1954. The graph is connected for every case in dimensions four through six, with three disconnected cases at dimension three and one no-route case at dimension two.

The exhaustive checks establish the finite dimension-four induction base and expose the sharp dimension-three counterexample. They do not verify any dimension beyond eight and are not presented as an infinite proof. The independent mathematical induction is given in `RESULT.md`. No external validation was performed.
