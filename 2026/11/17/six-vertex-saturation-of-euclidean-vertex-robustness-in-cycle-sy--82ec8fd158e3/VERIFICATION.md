---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

In the canonical Euclidean zero-sum model r_i=e_i-e_(i+1), the remaining path roots b_j=r_(j+1) have tridiagonal Gram G=diag(2)+offdiag(-1) and r_1=-sum b_j. For each n, the stated positive weights s sum to one; q=-sum s_j b_j belongs to Q_n, y=r1-q=-sum(1-s_j)b_j, h_j=(G(1-s))_j. Exact rational reconstruction independently checked every claimed contact support inequality for n=3..50: min h>=0, h_j=lambda on s_j>0 and h_j<=lambda otherwise, while <y,-r1> is smaller. Thus (r1-q)·(z-q)<=0 for every surviving vertex, a complete KKT projection certificate. The squared norm v^T Gv is 1/2,4/5,9/10 for n=3,4,5 and identically 11/12 for n>=6; supports sizes 2,3,4,4. The displayed algebraic support formulas prove these facts for all n, and affine independence of path roots proves the exposed face count. Finally distance-to-convex-set is convex, giving directed Hausdorff equality. No nonorthogonal unimodular coordinate change is used.

## originality

PASS

Canonical Euclidean deletion radius and exact stable contact face are not implied by the general vertex-robustness definition or combinatorial facet-subgraph classification; complete-bipartite signed-edge deletion is a different graph family.

## value

PASS

A natural vertex robustness invariant for the canonical symmetric-edge polytope of a cycle admits an unexpected finite sharp saturation: deleting one oriented root gives the same squared Euclidean loss 11/12 at every n>=6 with a stable four-vertex contact simplex. This gives an exact geometric tolerance and projection face beyond combinatorial facet counts and is useful for vertex enumeration and deletion stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
