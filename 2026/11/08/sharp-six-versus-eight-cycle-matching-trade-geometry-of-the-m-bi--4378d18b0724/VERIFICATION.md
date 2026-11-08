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

# Reproduction and finite limits

Run the two included scripts from any Python 3 environment with the standard library:

```
python3 verification/verify_gp.py
python3 verification/verify_permutations.py
```

The first script builds the 16-vertex edge list explicitly, recursively enumerates all matchings, enumerates all simple six- and eight-cycles by DFS, applies legal cycle exchanges and performs exact all-source shortest-path searches. The second script builds the same graph independently as a bipartite adjacency matrix, checks all 40,320 bijections, and detects legal exchanges from relative permutation cycles rather than explicit graph-cycle enumeration. Both assert the number of matchings, every component size, degree type, all-pairs distance histogram, and octagon-only structural model.

Expected facts: 33 matchings; complementary two-factor types with multiplicities 3, 6, 24; 96 hexagon edges, 36 octagon edges, 132 combined edges. Hexagon-only components: 30, 1, 1, 1, with connected-component radius 3 and diameter 4. Octagon-only graph: connected, radius 3 and diameter 4, explicitly a subdivided doubled triangle with eight leaves per hub. Both move types: connected, every eccentricity 3. Pair-distance counts: hexagon-only nontrivial component [96,216,120,3]; octagon-only [36,198,54,240]; combined [132,342,54].

The result applies only to all simple 6- or 8-cycles in GP(8,3), not to an embedded face-only subset. Finite exhaustion here proves this finite theorem, not an all-order statement, a complexity claim, a mixing-time estimate, or a claim of literature-wide uniqueness.
