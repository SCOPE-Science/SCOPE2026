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

Scalar parts of square-zero elements vanish. Squaring a+b+c in the augmentation ideal gives 2a∧b; top degree is radical. Projection to U in degree one forces the pure degree-two part to be U^perp by polarization and maximality. Its dimension 3-r, and the perfect pairing then gives exactly one maximal space for each alternating form on U with values in the top-degree line. Mixed cubic products cancel; hence W²=∧²U and closure is equivalent to ∧³U=0. The characteristic filtration preserves r, while GL(V) moves U and conjugation by 1+a adds the restrictions of -2a∧u∧v; these exhaust the form parameters. For an intersection of two quotient spaces the pure degree-two kernel is (U+U')^perp; its projected image is the radical of the difference of forms restricted to U∩U'. This gives all stated dimensions and the point/hyperplane equations using a common volume identification. Witt extension gives uniform incidence for the nonzero isotropic vectors; dividing the count of space–vector incidences gives 2(q+1). Independent bitmask multiplication over F_3 exhausted 33,880 candidate quotient 3-spaces, found all 80 with the stated product ranks and intersection totals, and checked 780 noncentral square-zero elements, each in eight spaces. The symbolic proof covers the general field, not extrapolation from this test.

## originality

PASS

The abstract polar geometry, generator counts and incidence of the Klein quadric are not novel. Credit the classification in the ungraded algebra with its actual exterior multiplication and its intrinsic four automorphism orbits; this is not a classification under the full split orthogonal group or of pairwise-annihilating spaces.

## value

PASS

The minimal nontrivial exterior rank for this square equation exhibits elementwise-zero spaces that are annihilating, closed but noncommutative, and not subalgebras. The classification and intrinsic orbit decomposition turn this distinction into precise reusable structure, beyond recomputing the classical graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
