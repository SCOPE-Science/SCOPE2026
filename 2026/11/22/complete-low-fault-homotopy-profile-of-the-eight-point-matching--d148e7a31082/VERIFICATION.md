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

The nine orbits follow by the components of a simple ≤3-edge fault graph: for three edges the connected shapes are triangle, path and star, with the two disconnected possibilities obtained by partitioning the edge count as 2+1 or 1+1+1. Relabeling graph vertices induces a simplicial isomorphism. Inclusion–exclusion in the alternating face sum, including the empty face, gives a term +reduced-chi(M(K_(8−2k))) for each matching of k faulty edges (the signs from exclusion and the shift in simplex size cancel). For k=0,1,2,3 these values are 132, −16, 2, 0, giving the formula and every row. The frozen Morse checker enumerates every Hasse incidence on each representative, not just incidences in its chosen pairs; its augmented orientation, and dropping the empty-face pair, give exactly the required discrete-Morse hypothesis. Independently verified the homotopy type without relying on that matching: each perfect-matching tetrahedron has a free triangular face since a three-edge matching leaves just two graph vertices and at most one extension. Collapse every tetrahedron along one such triangle, contract a maximal tree in the remaining connected 1-skeleton, and read triangle boundary relators. The independent checker verifies that iteratively killing generators appearing as the sole live generator of a triangle relator kills all generators on each of the nine representatives. This proves simple connectivity; a simply connected finite 2-complex has free H_2 of rank reduced χ, and Hurewicz plus homology Whitehead give the wedge of that many 2-spheres. Replay: python3 /workspace/reviews/check_mathematics.py 1. The nine generator counts before elimination are 183,169,155,156,141,141,142,143,144; zero survive in every case, with ranks 132,116,100,102,84,84,86,88,90.

## originality

PASS

The intact wedge of 132 spheres is established prior art. The contribution supported is the full nonempty low-fault homotopy profile; neither the Euler inclusion–exclusion method nor the Morse method is new. The closest distinct same-day perfect-matching deletion is real overlap in setting, but not coverage on these fault graphs.

## value

PASS

At the eight-point intact case where the ordinary complex is a known two-sphere bouquet, the low-deletion question tests stability of the integral homotopy type under every small fault shape, through the first cyclic fault. This is a complete natural cutoff rather than chosen sample graphs. The nontrivial topology is uniform, while the sharp rank is incidence-sensitive already for two faults; the resulting benchmark distinguishes equal fault counts and identifies genuinely homotopy-equivalent nonisomorphic examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
