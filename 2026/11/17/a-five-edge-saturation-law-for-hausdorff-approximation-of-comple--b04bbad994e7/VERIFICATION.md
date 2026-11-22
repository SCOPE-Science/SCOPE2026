---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

In canonical Euclidean zero-sum coordinates the path-root matrix B is injective and P_n={Ba:||a||_1<=1}. The KKT projection criterion g_k=(e_k-e_{k+1})·(v-Ba)=lambda sign(a_k) when active and |g_k|<=lambda otherwise is necessary and sufficient. For endpoint root e1-en: n=3,4,5 have listed rational certificates with squared distances 1/2,4/5,9/10; all n>=6 use a1=a_(n-1)=5/12,a2=a_(n-2)=1/12 and zeros elsewhere, lambda=1/4, residual 7/12,1/3,1/12 at opposite ends, giving 11/12. All separated roots j-i>=5 split into disjoint endpoint blocks; boundary contributes 11/24 squared norm, interior 3/8, giving 11/12,5/6,3/4. Shorter roots have explicitly feasible projections <11/12. A nonextreme point cannot tie, by convexity and strict extremal vertex set plus scaling toward origin. For the second largest root-vertex shell, separation-four potential ties are ruled out by inactive edge gradient 1/3>lambda=1/4; long roots with exactly one path endpoint count 4(n-6) for n>=7. Only vertex second shell claimed, not second level over a continuum.

## originality

PASS

Strong partial overlap: the separate published same-day cycle-vertex deletion result gives precisely the 1/2,4/5,9/10,11/12 plateau and a four-edge projection of one omitted root, but in a *different pair of polytopes* (deleting one oriented vertex of a cycle-edge polytope). Its certificate can reprove the longest path root distance because its contact point lies in the path hull; that numerical plateau by itself is NOT original here. The assessed package also classifies ALL complete-root vertices relative to the path hull, three long-root metric shells, unique continuous farthest points and exact second vertex shell. These latter assertions do not follow from a single deleted-cycle-vertex distance, and the separate cycle-root distance-shell theorem has distinct values and target body. Those independent nontrivial additions support best-of-knowledge originality of the full final claim despite overlap of the headline plateau.

## value

PASS

A complete natural metric approximation of the type-A complete-root polytope by one of its spanning-tree path polytopes, including *all* distant-root shells and exact second vertex shell, remains a meaningful geometric invariant even though its farthest-root constant is separately known through cyclic vertex deletion. The distinction between boundary and interior root positions is geometrically motivated and not a mere reparametrization; it sharpens a single worst-case radius into a localized classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
