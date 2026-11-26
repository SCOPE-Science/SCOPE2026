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

Independently oriented vertex pairs by Euler's criterion mod 11, and reconstructed the three complexes from their out-neighborhoods. For each, actual free-face collapses eliminate all cells of dimension greater than two in descending dimension without deleting any critical cells (55,51,62 pairs for X,Y,Z). In the remaining 2-complex, contract the star spanning tree at vertex 0 for the edge presentation of pi1. Repeatedly using triangles with two trivial edges eliminates all the generators (all 55 edges thereby trivial in this presentation). Euler characteristics then give H2 ranks 21,18,17. A basis realized by Hurewicz gives a homology equivalence from the corresponding wedge of 2-spheres, hence a homotopy equivalence by simple connectivity. Relative check: X and Z are each Y with one simplex attached. For X the intersection is the tetrahedron on {3,4,5,9} plus four edges from 1 to its vertices. Contracting that tetrahedron leaves a graph with four parallel edges, homotopy equivalent to a wedge of three circles. For Z the intersection is the full simplex on {2,4,5,6,10} plus the cone from 0 over cycle 2-4-10-5-6-2. Collapsing the full simplex to a point yields the cone modulo its base, an S^2. In both cases the quotient by Y is the attached simplex modulo its intersection, homotopy equivalent to the suspension of that intersection. This gives the stated wedge of three 2-spheres and S^3. The integral long exact sequences then give the claimed injection with free cokernel and surjection with free rank-one kernel; free splittings and the degree-matrix classification for maps between wedges of 2-spheres give the noncanonical normal forms. Every arc is an affine image of 0→1 under multiplication by a nonzero square and translation, transporting the whole diagram. Replay: python /workspace/replays/paley.py. No larger-order, multi-arc or equivariant classification is needed or proved.

## originality

PASS

The intact Paley-11 wedge of 21 spheres is already known and expressly excluded from the original contribution. Distinct supported content is the pair of faulted homotopy types and the comparison of the two relative cofibers and integral maps with the deletion complex as common source. Several related fault calculations already establish primitive maps or reversal effects on other complexes; they are not coverage of this particular directed pair.

## value

PASS

For a standard highly symmetric tournament, deleting and then restoring or reversing one arc yield two sharply different attachment topologies, including maps whose primitive kernels and cokernels are not recoverable merely from intact homology. This is a complete exact benchmark for the natural smallest perturbations, uniform over the arc orbit, not a recomputation of the intact invariant or an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
