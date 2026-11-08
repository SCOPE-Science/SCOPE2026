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

# Finite verification and scope

The two executable companion programs use only the Python 3.10+ standard library and contain their entire object specifications, enumeration algorithms, BFS, interval-median algorithms, and integer assertions. Run them separately:

```
python3 verification/permutohedral_face_flips.py
python3 verification/signed_coordinate_face_flips.py
```

The permutation implementation reconstructs the graph from adjacent swaps on all 24 four-letter permutations, constructs the fourteen coset faces, enumerates all 169 perfect matchings by least-uncovered-vertex recursion, and uses the XOR-of-face-edges rule. It checks exact full-graph edge counts, radii, diameters, eccentricity and pair-distance histograms and 790244 median intersections, tests the three canonical no-median states, and checks every individual face omission (including representative medianity tests).

The independent coordinate implementation reconstructs the truncated octahedron as integer signed coordinate permutations of \((0,1,2)\), builds its six square and eight hexagonal supporting faces, enumerates matchings using a stack, tests alternation directly, recomputes all-source distances, checks every omitted face's radius and diameter, and reproduces the full graph's median intersection census.

Successful execution of both independently constructed files yielded these exact checks:

```
PERMUTATION_MODEL_24_VERTICES_36_EDGES_6_SQUARES_8_HEXAGONS_PASS
MATCHINGS_169_FULL_FLIPS_460_RADIUS_7_DIAMETER_9_PASS
ECCENTRICITIES_69_AT_7_92_AT_8_8_AT_9_PASS
PAIR_DISTANCES_460_1324_2428_3138_3032_2436_1204_170_4_PASS
ALL_FACES_NONMEDIAN_79828_EMPTY_9642_DOUBLE_MEDIANS_PASS
THREE_GENERATOR_MATCHINGS_NO_MEDIAN_PASS
REMOVE_ANY_SQUARE_410_EDGES_RADIUS11_DIAMETER22_PASS
REMOVE_ANY_HEXAGON_440_EDGES_RADIUS11_DIAMETER21_PASS
PUNCTURED_MEDIAN_GRAPHS_PASS
SIGNED_COORDINATES_24_VERTICES_36_EDGES_14_SUPPORT_FACES_PASS
SECOND_MATCHING_ENUMERATION_169_PASS
SECOND_FLIP_CENSUS_460_EDGES_RADIUS7_DIAMETER9_PASS
SECOND_ALL_PAIR_DISTANCE_AND_ECCENTRICITY_HISTOGRAM_PASS
SECOND_ALL_TRIPLES_MEDIAN_INTERSECTION_CENSUS_PASS
SECOND_ALL_14_FACE_DELETIONS_22_OR_21_DIAMETER_PASS
```

The finite algorithms are exhaustive because every matching is recovered uniquely by the least-uncovered recursion, all facial cycles are explicitly listed and verified, every permitted local transition is tested, and every shortest-path distance is computed by BFS. The computations do not prove any statement for larger permutohedra or arbitrary spherical embeddings. The mathematical review here is not independent scholarly validation.
