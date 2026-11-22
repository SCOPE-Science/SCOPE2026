---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For capacity-one 3x5 nonattacking rook placements, rotation by one of five columns acts freely on every nonempty face: each row contains at most one rook and no nontrivial column rotation fixes a cell. Source has 15/60/60 cells and quotient has 3/12/12 vertex/edge/triangle orbits. With maximal tree edges a1,b1 collapsed, each of 12 triangle attaching words equals a_i c_{j-i} b_j^{-1}. Nine elementary free-group generator/two-cell cancellations leave attaching words t^5, t^{-5}, and empty, and a standard two-cell slide changes these to degree-five and two null 2-cells, giving M(Z/5,1) wedge S2 wedge S2. The quotient has fundamental group Z/5 and H2=Z². As it is the universal regular C5-cover, the standard chain R -N-> R -(g-1)-> R of degree-five Moore space has ker N=augmentation ideal I_C5; the two lifted 2-spheres supply R², giving rank4+10=14. Independently enumerated all quotient simplex orbits and computed abelianized quotient boundary Smith factor 5 plus H2 rank 2; inspected exact nonabelian reduction and source verification code for nine free-group eliminations.

## originality

PASS

Known three-row chessboard wedge/connecting results concern unquotiented complexes, rational symmetric-group representations do not fix the integral C5 deck lattice, and previously published cyclic quotient theorems cover 5x5 ordinary or three-row capacity-two rook complexes, not the 3x5 capacity-one orbit space. A generic fundamental-group formula gives only pi1=C5, not the Moore attaching map and two sphere summands. No found stronger published result implies both claimed precise quotient and integral module. Best-of-knowledge; unindexed equivariant homotopy calculations remain possible.

## value

PASS

This is a small but natural minimal simply connected chessboard complex under a canonical free fivefold symmetry. Unlike routine additive homology, the degree-five attaching map and the integral augmentation-ideal deck module distinguish integral orbit topology from rational representations and supply a reusable worked equivariant example. The exact finite quotient presentation is a motivated complete classification, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
