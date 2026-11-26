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

T_6 has diameter two, so the forbidden geodesic triples are induced P3s; in the source K_6 these are exactly simple three-edge paths on four distinct source points. In the full complete simplicial 1-skeleton, every missing triangle loop bounds the cone built with the edge on the two unused source points: its three pieces are valid triangles because that edge is disjoint from each of the original three. Thus all triangular loops, which generate the fundamental group of the complete skeleton, are nullhomotopic. My independent code tested the source-path predicate, recovered f=(15,105,275,240,66,10), and made legal elementary free-face collapses only in dimensions (4,5) and (3,4), reaching a 3-complex with f=(15,105,275,184). The exact signed third-boundary Smith form (FLINT) has 169 ones and 15 zero column invariants. Hence H_3 has rank 184-169=15, and H_2 is free of rank 275-(105-14)-169=15 using H_1=0. The collapse keeps homotopy type, and guarantees vanishing above degree three. For the upgrade, choose a map from a wedge of fifteen 2-spheres inducing an H_2 isomorphism by Hurewicz. Its mapping-cylinder pair is 2-connected and relative Hurewicz gives all relative H_3 classes by relative homotopy. The absolute-to-relative H_3 map is an isomorphism and the absolute-to-relative pi_3 map is onto since the pi_2 map from the wedge is injective. Thus choose fifteen 3-sphere maps representing the H_3 basis; together the sphere maps are a homology equivalence between simply connected CW complexes, so are a homotopy equivalence. Replay: python3 /workspace/repro/record3.py, output /workspace/repro/record3.out. The frozen certificate was inspected rather than run; the independent collapse and Smith computation are alternative exact verification for T_6 only.

## originality

PASS

Prior work already covers the allowed-face condition, the complete face-size polynomial for all T_n, and maximal cluster structure. Those parts are not novel. The supported distinct claim is the integral nonequivariant homotopy type of the six-point complex.

## value

PASS

The full complex on a small standard triangular graph is a natural test object for topological general-position theory, not just a list of maximal sets. Integral topology distinguishes this example from related complexes and confirms two nonzero consecutive homology degrees even though the Euler characteristic alone cancels them. The degree-two and degree-three multiplicities together with a simple-connectivity and collapse check give a concrete benchmark for future structural arguments on this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
