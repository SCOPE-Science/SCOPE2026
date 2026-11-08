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

# Reproduction and scope of finite verification

Run from this directory using Python 3 and a C++17 compiler:

```sh
python3 q4_square_metric.py
g++ -std=c++17 -O2 -Wall -Wextra q4_square_metric_independent.cpp -o q4_metric
./q4_metric
```

The Python program constructs the sixteen binary vertices, recursively enumerates exact matchings by the least free vertex, independently generates all 24 coordinate squares, toggles each alternating square, traverses connected components, and performs breadth-first search from each of the 264 mobile states. It also tests the complete natural cube symmetry group and the orbit structure of all distance-eight pairs.

The independent C++17 program starts instead from the bipartition of the cube into eight even and eight odd vertices, scans all 8! bijections, filters for cube edges, and generates legal flips by swapping two odd partners whenever both cross-edges exist. It reconstructs the complete component and distance information without calling or reading the Python program.

Both programs assert 272 perfect matchings, 768 square-flip edges, eight singletons and one 264-state component, radius 7, diameter 8, eccentricity counts 252 and 12, the exact eight-bin unordered distance profile, and a specific pair requiring eight flips. They assert that the twelve eccentricity-eight states are precisely the degree-four states and that the distance-eight relation is three disjoint four-cycles. The Python program additionally checks that the extremal states and pairs are each single cube-symmetry orbits.

No stochastic sampling, external graph library, downloaded dataset, precomputed distance table, SAT oracle, or independent peer audit is used. The result does not include higher-dimensional generalization or an argument for rapid sampling/mixing.
