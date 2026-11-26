---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

I independently reconstructed the checkerboard bipartition of the graph and tested all 9! bijections of its two parts for adjacency. This yielded exactly 108 perfect matchings; nonempty bit submasks produced the stated 30353 faces. For each of the 14436 listed collapse pairs I verified the unique immediate coface against the current face set, and checked that the upper face was maximal. The terminal down-set has f-vector (30,270,694,487) and no faces of larger dimension. The listed 29 tree edges connect all 30 vertices. In order, all 241 triangle relations then have exactly one not-yet-trivial edge loop after setting the tree edges to 1; every remaining generator is killed. This establishes simple connectivity, and the rank of the degree-two boundary is 270-29=241. I reconstructed the oriented degree-three boundary from the terminal masks and independently cleared the 453 indicated unit pivots by column additions, followed by row additions affecting only the pivot column. The terminal matrix is zero, giving image rank 453 and primitivity in the full degree-two chain group. The simplicial boundary identity puts that image in the degree-two kernel of rank 694-241=453, so they are equal (including integrally). Degree-three homology is free of rank 487-453=34. Hurewicz in degrees two and three makes the core two-connected and realizes a basis by three-spheres; wedging their maps gives a homology equivalence of simply connected CW complexes, hence a homotopy equivalence. The nonzero H3 precludes shellability of the original pure eight-dimensional complex.

## originality

PASS

The checked exact-graph, exact-complex-family, and related classification sources do not contain or imply the asserted wedge for the longitudinally closed, three-row, six-column extendibility complex. An exact Resultary hit is the assigned record itself.

## value

PASS

Closing the six-column open strip is a natural boundary change in a studied family. It changes one two-sphere to 34 three-spheres; the result fixes connectivity, torsion and integral homotopy and disproves shellability for this cylinder. The exact topology gives a useful boundary-sensitive datum beyond face counts or homology ranks alone, without presuming a pattern for larger cylinders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
