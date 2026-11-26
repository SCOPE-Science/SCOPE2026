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

At a vertex an even positive degree cannot be carried by only one odd multiplicity, so both colors of the opposite parity-side palette occur and occur oddly. Thus for either side the indicator solves Bf=1; the other indicator works because B1=0. A coordinate half of the side gives a solution (neighbor counts 1 and d-1). Independently, write the full binary adjacency matrix in last-coordinate slices as A=[[P,I],[I,P]], with P the adjacency of Q_(d-1). The coordinate flips commute in characteristic two, so P^2=I, and the kernel is the graph of P with dimension 2^(d-1). In parity order A has off-diagonal blocks B and B^T, so rank B=2^(d-2). Also A^2=0, giving BB^T=B^TB=0; rank half implies that the image of each transpose equals the kernel of its opposite block, hence each side kernel equals its orthogonal complement. Constants are ruled out as solutions, so all palettes are used. The independent side choices yield the stated sixfold named count and a free 24-fold renaming quotient. For the four-color minimum, a putative three-coloring forces (I+A)h=1 for every color indicator h; squaring I+A gives I, hence h=1 for each color, impossible. Two and one colors are excluded by even positive degree and properness, respectively. The argument includes d=2 and makes no count for nonsplit colorings.

## originality

PASS

The supported distinctive result is the complete optimal parity-split census and its identification with two independent affine code cosets. The minimum palette is known. Self-duality of the full even-cube adjacency code is known and implies the side-kernel dimension and self-duality by the parity direct-sum decomposition, so those binary linear facts are not fresh standalone coding results.

## value

PASS

The canonical bipartition is the natural setting of the known optimal construction, not an arbitrary class restriction. Counting every optimum in that setting shows exactly how nonunique the construction is; the affine description gives the full degrees of freedom for constructing or sampling split optima and a baseline for separate nonsplit enumeration. The contribution is the census and its coloring characterization, not recomputation of the known code rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
