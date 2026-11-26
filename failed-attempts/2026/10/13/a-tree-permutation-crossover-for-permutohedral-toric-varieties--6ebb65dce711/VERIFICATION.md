---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For n>=1 and the specified regular polarization, the permutohedron is the sum of [e_i,e_j] over i<j on n+1 coordinates: a strict ordering of the objective chooses one endpoint for each edge and yields precisely a permutation of 0,...,n. Differences generate the lattice A_n. A maximal set of edge differences has determinant of magnitude one in A_n when the edges form a spanning tree (integral path differences give a basis) and zero otherwise. Consequently the lattice-covolume volume counts (n+1)^(n-1) trees. The Ehrhart leading coefficient gives degree n! times that volume. By the torus-orbit stratification, positive-dimensional complex tori contribute zero Euler characteristic and the (n+1)! maximal cones contribute one each. The quotient is (n+1)^(n-2), giving 1/2, 1, and >1 respectively at n=1, n=2, n>=3, with both invariants 6 for the hexagonal del Pezzo surface. The comparison is of n! times the tree count with the permutation count, not the two bare counts; in dimension two the latter are 3 and 6. The unique-equality statement is for positive dimensions as in the stated classification.

## originality

FAIL

The entire crossover is mechanically implied by exact established formulas on the very same object, not merely adjacent results for a different fan or polarization. Postnikov's Proposition 2.4 at m=n+1 and the standard degree-volume identification give D exactly; Henderson–Lehrer's Eq. (9) for the type-A Coxeter fan at q=1 gives E exactly. Dividing cancels the factorial and leaves (n+1)^(n-2); only inspection of the sign of the exponent remains. No direct earlier phrasing of the ratio was established, but none is needed for this implication. No unaccounted invariant or new comparison lemma survives.

## value

FAIL

The standard polarization and both invariants are natural, but the proposed finding only divides two established invariant formulas and classifies the elementary exponent. It is useful as an illustration of the factorial normalization, not an independently useful new exact fact. Clarifying the tree-count scaling does not leave a scientifically substantive claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
