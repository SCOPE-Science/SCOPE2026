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

The proof covers arbitrary ambient order and both marked and unmarked centers. In the vertex–block incidence forest, two neighbors of an unmarked center from the same connected marked component must use the same clique, or there would be two paths between them. For the multicomponent count, contract the disjoint connected subtrees formed by each marked component and its incident clique nodes. Keep only terminal-to-center edges, without any suppression: with c terminals and s centers seeing multiple terminals, the forest has at least 2s and at most c+s−1 edges. This gives at most m+Σ_i(u_i+b_i+1) traces. The deficit from 2t_i in u_i+b_i+1 is the count of vertices of degree at most one plus Σ_B(|B|−2); it is at least two except on a singleton or a triangle. In the one-triangle case with other vertices, contracting the triangle gives a tree with a leaf outside the triangle. These deficits imply the 3m−2 upper bound for m≥4, and 2^m suffices below four marks. The path-of-triangles witness separates adjacent pairs, distance-two pairs, singletons and the empty trace; the small witnesses attain all subsets, including the unique empty trace at m=0 on a nonempty graph. The four-mark obstruction and three-mark witness give VC dimension 3, and the eventual exact linear formula gives density 1.

## originality

PASS

The inspected statements cover related trace problems and broader asymptotic or small-profile bounds, not this all-m open-adjacency maximum of 3m−2 on block graphs. The exact function, not the generic technique or the VC terminology, supports this assessment.

## value

PASS

This is the exact shatter function of a natural clique-tree class, independent of ambient order and including both center types. It determines not just the growth exponent but the sharp linear coefficient and deficit, and explains the small-set exception via the different singleton and triangle deficits. The extremal witnesses and the trace-counting lemma are useful when a generic growth or VC-dimension estimate is too coarse.

The dated certificate retains the supplied scientific assessment, sources and limitations.
