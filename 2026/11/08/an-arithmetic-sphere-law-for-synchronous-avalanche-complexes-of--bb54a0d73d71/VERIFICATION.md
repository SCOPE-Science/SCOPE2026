---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

Each zero-chip vacancy moves one step per simultaneous firing on its directed cycle; the exact global period is lcm(n_i)=d*product(u_i). With pairwise gcd d, generalized CRT says precisely simultaneous hole tuples whose phase-corrected labels have the same residue mod d occur. In each residue block the complement of a transversal is a join of r simplex boundaries, a sphere of dimension sum u_i-r-1. For disjoint forbidden-hyperedge systems the complement complex is (D_U*Delta(V)) union (Delta(U)*D_V), intersection D_U*D_V, so the cofibration homotopy pushout is a suspension. Iterating d blocks gives dimension N-(r-1)d-2, including d=1. The inspected independent code checks six CRT orbit families and direct GF2 homology of (3,4,5) (60 facets, 3255 faces, degree-8 beta=1); a separate direct subset enumeration independently confirmed these counts. Integer conclusion comes from the proved join/pushout, not from mod-two sampling.

## originality

PASS

Best-of-knowledge PASS for a multicycle disjoint synchronous avalanche sphere theorem with equal pairwise gcd; primary avalanche authors primarily discuss directed paths/cycles and their revised abstract, and indexed residue support work is distinct. Full revised primary paper was inaccessible, flagged explicitly.

## value

PASS

Natural synchronous chip-firing dynamics on disconnected directed cycles yields an infinite arithmetic-to-topology sphere law with arbitrarily many components and variable common gcd. An exact sphere result is a structural gap beyond either single-cycle behavior or the known two-cycle subcase, not an arbitrary finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
