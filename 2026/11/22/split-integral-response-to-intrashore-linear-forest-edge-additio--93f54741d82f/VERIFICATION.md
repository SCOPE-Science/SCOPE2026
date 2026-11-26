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

The pure shores are full simplices at both stages. A mixed face cannot have two vertices on each shore (a 4-cycle) or three on one shore (degree at least three across it). The only lost faces are then the mixed triangles with two A-vertices forming an edge of D and any B-vertex. The complement of L' is connected: three components force a triangle in L', two nonsingleton components force a 4-cycle, and a singleton component forces degree at least a−1≥3. For any missing triangle, cone a simple complement path between its A-vertices to its B-vertex; cap the resulting A-path with the A-simplex fan. The two disks are valid subcomplexes and give an actual null-homotopy, with oriented boundary [v,w]−[u,w]+[u,v], not just a homological filling. Changing those attaching maps to constants in the path-connected base gives the wedge equivalence relative to the unchanged subcomplex. The relative chain complex has just the free group of oriented lost triangles in degree two; with the B-vertex last, its action is exactly the tensor of the B-permutation action and the A-edge orientation action. The boundary map vanishes by the disks, and the integral splitting follows from freeness without asserting equivariant splitting. For the stagewise argument, the undeformed complex has the complete two-skeleton; relative to the union of the pure simplices, there are no cells above degree two. H_2 is free specifically because the pair sequence identifies it with relative H_2, a subgroup of the free relative degree-two chains (one should not assume absolute degree-three chains vanish). The mixed-cell Euler count agrees with R(a,b). The relative splitting from the undeformed complex makes each stage a homotopy retract with free degree-two homology and no other reduced homology; simple connectivity and Hurewicz–Whitehead give the asserted absolute wedge types. As a sign check, for a=4, b=2 and empty L contained in the path 1–2–3–4, the relative rank is six; path reflection fixing B reverses the central oriented edge and exchanges the two outer edges, so its trace is −2 on the relative group.

## originality

PASS

Best-of-knowledge pass for the map and pair on adding edges inside one shore, particularly the explicit relative fillings and the signed equivariant quotient. Do not credit the absolute sphere counts or general CW attaching-map facts as new. Adjacent degree or cross-edge filtration results address different maps.

## value

PASS

Internal graph perturbations define actual inclusion maps on a natural degree-limited forest complex. Uniform filling disks give their relative homotopy behavior; the signed integral cokernel distinguishes edge reversal from ordinary permutation, information invisible even in a complete list of Betti numbers. These data can be used in nested perturbations or under side-preserving symmetries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
