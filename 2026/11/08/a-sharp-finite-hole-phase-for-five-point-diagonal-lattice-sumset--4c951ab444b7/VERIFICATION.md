---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Let u=min(x,y),v=|x−y|. Shortest A_m representation length is v+f_m(u), with u=(m+1)q+r and f=q for r=0; f=q+1 when r>=1,q+r>=m; otherwise f=q+2r. The polygon inequalities give v+ceil(u/(m+1))≤h. Their difference occurs only when 1≤r≤m−1 and 0≤q≤m−r−1, with q+1≤h−v≤q+2r−1. Count the two orientations except once at v=0, then sum all (r,q) intervals; maximal endpoint is 2m−3 uniquely at (m−1,0), proving stabilization begins at h=2m−2 and constant m(m−1)(2m−1)/3, one less at preceding h. Independently enumerated small m,h lattice sets matched exact hole locations; finite enumeration is a check, not the universal proof.

## originality

PASS

Curran–Goldmakher exact sumset cardinality for d+2 points gives FOUR generators in dimension 2, not this five-generator semigroup; broad Granville–Shakan–Walker effective eventual growth and Nathanson general holes do not furnish the stated all-degree complete residue-hole locus or sharp onset. Resultary search did not identify exact identical five-point family except this assignment. No uncovered stronger theorem found in inspected sources, with residual unindexed-special-case priority risk.

## value

PASS

A natural five-generator planar affine semigroup exhibits a nontrivial finite hole plateau. Exact location classification, sharp first stable degree, and transition from the four-generator linear hole growth to five-generator eventual constancy are motivated semigroup-normalization invariants, not an arbitrary small numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
