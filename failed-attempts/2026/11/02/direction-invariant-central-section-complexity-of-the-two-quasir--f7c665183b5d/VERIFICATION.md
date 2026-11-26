---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A generic plane cuts a polytope edge exactly when its endpoints have opposite signs. At a midpoint x the four neighbors are exactly the midpoint pairs in the two incident original triangles: each midpoint triangle is an exposed facet of the rectification, so its sides are edges. The balance equation makes the four neighbor projections onto x-perp cancel in two opposite pairs. At a simple wall there are two positive and two negative neighbors and no jump in crossing count. The general criterion's origin-interiority step can be supplied as follows. The exposed triangles in distinct facet planes give a full-dimensional rectification. If the origin were not interior, there would be a supporting plane through it touching a nonzero midpoint vertex (for exterior origin vary a strictly separating normal continuously to its opposite until the minimum projection is zero; at a boundary vertex choose an incident facet). At any nonzero touching vertex the neighbor sum is parallel to that vertex; nonnegativity makes all its neighbors touch. The polytope graph remains connected on deletion of at most the vertex 0, so all vertices would lie in the plane, a contradiction. Consequently simultaneous switching vertices are opposite radial endpoints and are nonadjacent, so their zero jumps add. The regular originals have balanced diamonds by their edge-axis half-turns. Independent exact base-direction enumeration for normal (1,2,4) found no midpoint ties. Enumerating original triangles as triples with all squared distances 2 for the octahedron or 4 for the icosahedron gives counts by number of positive midpoint signs of (2,2,2,2) and (7,3,3,7); each mixed triangle contributes two crossed edges, giving 8 and 12. For replay, sign a midpoint by n·(u+v), comparing the signs of 2a+b and b and then (2a+b)² with 5b² for a+bφ. Each cut edge separates the two distinct face types, forcing alternation and therefore the stated face counts. Central symmetry, measure-zero exceptions and affine invariance follow with the stipulated centers and vertex avoidance.

## originality

FAIL

The distinct earlier equatorial-edge-belts record explicitly gives both solid counts and a more general projected-neighbor pairing criterion for centrally symmetric polytopes. For these two solids the face-colored counts follow immediately from classical edge incidence, and the affine assertion transports by bijection. The midpoint equation is a sufficient coordinate test of the same local pairing: the earlier local-jump cancellation (or paired planar-belt proof) requires only origin-interiority and the nonadjacency of simultaneously switching vertices for this sufficiency direction, not equal antipodal radii or overall central symmetry. This covers the material conclusions without a new section mechanism. This is statement-level and implication evidence, not a chronological inference from the distinct same-day match.

## value

FAIL

The section invariant is well motivated, and its constancy is not a generic property of polyhedra. The incremental claim, however, repeats two established constants and gives their immediate color alternation and affine transport. The coordinate specialization of the established wall-balance test gives no new class of examples or independently needed exact fact here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
