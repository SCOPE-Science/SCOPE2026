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
# Verification

The following ordinary standard-library programs are included as standalone files. Execute each in the same directory as this document, without external packages:

```
python3 verify_bitmask.py
python3 verify_set_independent.py
python3 verify_symmetry.py
```

`verify_bitmask.py` constructs the two 16-vertex graphs from Cayley differences and row/column tests and verifies their degree and common-neighbor parameters. It enumerates every vertex subset of cardinality 0 through 5 and tests both original and complement open-neighborhood signature conditions. It checks the 96-neighborhood obstruction sets exactly and exhausts all possible one-element replacements, with and without adjacency constraint. Breadth-first search from every code verifies all distances, connectivity, radius and diameter. Its complete output is in `verify_bitmask.out`.

`verify_set_independent.py` reconstructs the graphs via unordered edges and independently evaluates set intersections without the first program's bitmask representation. It enumerates all subsets of cardinality 0 through 5 and independently constructs and counts exchange graph links and components, output in `verify_set_independent.out`.

`verify_symmetry.py` constructs 192 Shrikhande and 1152 rook-graph automorphisms, verifies that every permutation preserves every graph edge, and computes complete orbits of the minimum global locating-dominating codes; expected output is in `verify_symmetry.out`.

All source graphs are finite and are covered by the exhaustive loops; no inference from sampled configurations to infinite graph families is made. The short paper proof of the globality filter and the unique-neighborhood obstruction is independent of execution. The counting and distance statements require executable exhaustive enumeration, which is supplied in full. Verification does not establish bibliographic priority, and no external independent audit was performed.
