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

The hub is in no independent triple with zero or one missing spoke, or with two adjacent missing spokes, so the complex is a nonempty cone for n>=6. At two nonadjacent failures, the single new triple {h,a,b} adds exactly the simplex on A=V minus {a,b}. Its intersection with the original cone is the restriction of the rim total cut complex to A. Faces omitting a vertex nonadjacent to both a and b are all in the intersection. For the other faces, at cyclic distance two the five candidate vertices induce a path on five vertices, whose only independent triple is its alternating triple; at distance at least three, any independent triple contains one of the two full neighbor pairs, and either pair extends by the opposite endpoint. This gives the two stated joins. Their inclusions are simplicial cofibrations, so unions of the two contractible pieces realize the corresponding suspensions. At n=6 the inner complex is already two disjoint simplices in both cases, including U empty for antipodes. The outer suspension gives S^(n-5), an actual homotopy equivalence. The source verifier inspects all 266 pairs at n=6,...,12 and only uses mod-two boundary ranks; it is not needed for the proof and was inspected rather than run.

## originality

PASS

The directly deducible cone cases are not the distinct contribution. The identified cycle and ordinary cut results do not supply the induced restriction or the sphere at the nonadjacent two-spoke threshold; no exact equivalent was found in the checked sources.

## value

PASS

Classifies a natural minimal edge-fault threshold for a standard graph complex on an unbounded family. The first noncontractible case depends exactly on the relative positions of the two missing spokes, and the result finds the full sphere homotopy type, not just a finite homology pattern.

The dated certificate retains the supplied scientific assessment, sources and limitations.
