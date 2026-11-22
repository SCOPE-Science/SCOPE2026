---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For binary triples the sum of pairwise Hamming distances is <=2n. Thus 3(n-2)>2n excludes triangles for every n>=7; graph connectivity follows antipodal two-step coordinate flips, and counting degrees gives all ranks and primitive graph inclusion. Independent exhaustive clique enumeration for Q5/Q6 found all f-vectors (32,256,480,120)/(64,704,960,240), each triangle in exactly one tetrahedron. Reconstructed full oriented edge-by-triangle boundary and projection to new edges, then independently performed exact unimodular unit-pivot eliminations: (rank∂2,rank projected∂2)=(209,159)/(418,418), with zero residual. Unique triangle cofaces give ∂3 injective. Relative LES proves free inclusion cokernels and the Smith forms, without finite-field extrapolation.

## originality

PASS

Anti-Rips literature defines the inclusive far-distance clique complex but does not determine these full Hamming-cube integral inclusion maps. Ordinary hypercube Rips uses near-distance edges, not an equivalent complex. Engström correspondence to graph-power independence complexes translates definitions but does not provide these ranks. The previously published parity reduction at ordinary n-2 scale is different (forbidden antipodal edges) and does not imply anti n-2 packing homology.

## value

PASS

This is a natural complete classification of the first two anti-Rips shells on full binary cubes, with a sharp n=5 exceptional killing of 50 integral cycles versus primitive persistence for all n>=6. Exact integral torsion and inclusion behavior supply a useful test case for distance-filtration topology beyond ordinary VR and finite numerical Betti tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
