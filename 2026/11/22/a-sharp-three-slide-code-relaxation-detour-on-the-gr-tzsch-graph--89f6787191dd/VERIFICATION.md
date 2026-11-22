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

# Computational verification

This is a finite exact enumeration of the 11-vertex Mycielskian of the five-cycle, not an infinite theorem inferred from samples. Reproduction requires Python 3, with only standard-library packages.

Run the two complete programs in the same directory:

```
python3 verification_a.py
python3 verification_b.py
```

The first constructs the 20 original edges using integer masks, tests every subset by size, constructs legal single-token moves and runs BFS on each finite state graph. It asserts exactly five required sensors for both code conditions; 110 minimum locating-total and 191 minimum identifying sets with strict inclusion; undirected edge counts of 520 and 1405 under jumps, 190 and 555 under slides; radii/diameters respectively (4,5),(4,5),(6,8),(5,6); and full pairwise improvement counts (5725,270) under jumps, (4135,1440,360,60) under slides.

The second reconstructs the graph independently with named tuples and Python sets, tests all cardinals and all five-sets, creates legal edges by pairwise intersection tests, and independently checks all 5995 locating-total endpoint pairs. It checks 13 dihedral locating-total orbits (9 ten-element, 4 five-element) and 24 identifying orbits (15 ten-element, 8 five-element, one singleton). It also checks each move in the explicit five-versus-two slide witness and verifies those two paths are shortest. Each program raises an assertion on any mismatch and prints PASS only after completing its tests.

Expected first-program terminal lines:

```
jump LT_edges 520 IC_edges 1405 LT_radius_diam 4 5 IC_radius_diam 4 5 unordered_distance_saving {0: 5725, 1: 270}
slide LT_edges 190 IC_edges 555 LT_radius_diam 6 8 IC_radius_diam 5 6 unordered_distance_saving {0: 4135, 1: 1440, 2: 360, 3: 60}
PASS exhaustive certificate: 5 selected vertices, 110 LT codes subset 191 identifying codes
```

Expected second-program terminal lines:

```
jump difference counts {0: 5725, 1: 270}
slide difference counts {0: 4135, 1: 1440, 2: 360, 3: 60}
PASS independent tuple certificate
PASS witness: five legal locating-total slides versus two identifying-code slides
```

No untested graph orders, external services, precomputed datasets, or outside runtimes are necessary. Reproduction verifies all claimed finite arithmetic and algorithms, but this does not substitute for independent review or guarantee historical novelty.
