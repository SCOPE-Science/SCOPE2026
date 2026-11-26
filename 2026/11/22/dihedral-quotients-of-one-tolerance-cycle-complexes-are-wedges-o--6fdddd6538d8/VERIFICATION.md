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

The tolerance complex has complete graph as one-skeleton and exactly the triples containing a cycle edge as triangles. The geometric quotient of that graph is a tree: one arm per unoriented cyclic distance, with the endpoint-swapping reflection halving each representative edge. No nonidentity rotation stabilizes a triangle, since a rotation-invariant triple would have equal gaps and contain no cycle edge for n≥4; two different stabilizing reflections would give such a rotation. For a reflection-stabilized triangle, take the half-triangle with two inherited boundary edges. It strongly deformation retracts onto their union, relative to that union, so the retraction descends even when the inherited edges are identified in the quotient tree. The other triangle orbits are disks attached along their entire boundaries to the tree. Collapsing the tree, a contractible CW subcomplex, gives one S² for each of these disks. Three-consecutive-vertex triangles are reflection-fixed. For every other triangle normalize its unique cycle edge to {0,1}; the third vertex k ranges from 3 to n−2 and the edge reflection pairs k with n+1−k, fixing exactly one permitted k for odd n. The resulting count is floor((n−4)/2), including zero at n=4,5. This proves the integral homotopy classification without using finite calculations.

## originality

PASS

The same-object unquotiented classification, the same-action second-tolerance quotient, and the distinct octagonal first-tolerance quotient do not give this geometric full-dihedral quotient. The identified tolerance-complex literature supplies definitions and collapsibility/Leray results rather than this stabilizer-dependent integral homotopy classification.

## value

PASS

This is an integral, all-order homotopy classification for the natural full symmetry quotient of the simplest cycle tolerance enlargement. It identifies exactly which orbit cells survive and why reflection-stabilized faces do not contribute, distinguishing a linearly growing orbit-space sphere count from the quadratic unquotiented count. The fold cancellation is a reusable explanation, not just a finite Betti-number computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
