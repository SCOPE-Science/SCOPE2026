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

For sparse paving rank 2<=k<=n-2, distinct nonbasis hyperplanes intersect in <=k-2, so at most one x(H)>k-1 can be violated by a point in Delta_(n,k). Given violation t>0, x_i>=t on H and x_j<=1-t outside. Subtracting t/k inside H and adding t/(n-k) outside preserves [0,1] and all other nonbasis inequalities, by y(J)<=|H∩J|+y(H^c)<=k-1. The displacement is orthogonal to x(H)=k-1 within the sum-k affine slice, proving the global Euclidean projection and squared gap t² n/[k(n-k)]. Missing incidence vertices uniquely maximize the gap. Excised cap has apex 1_H, base Delta(k,k-1)×Delta(n-k,1), Euclidean volume sqrt(n) binom(n-2,k-1)/(n-1)!, and its superlevel region at t>u scales by (1-u)^(n-1), giving exact mixture mass and conditional Beta(1,n-1) law. Independently checked an exact n=6,k=3 violating point (9/10 on H and 1/10 elsewhere): projected y=(2/3 on H,1/3 outside) with distance squared 49/150. The general proof does not depend on finite samples.

## originality

PASS

Best-of-knowledge PASS for the full claimed new pointwise projection and conditional Euclidean distance distribution. Known hypersimplex corner cutting, cap volumes and Eulerian normalization are explicitly credited. Published November 17 broader paving-matroid distance-shell theorem already entails the vertex Hausdorff and farthest-point corollary for sparse paving, so those cannot be treated as novel. But it only projects incidence vertices, not arbitrary interior hypersimplex points, and does not give the normalized-volume beta distance distribution. The November 8 sparse-paving surface-area theorem uses the same caps but not their global nearest-point distance map. Thus the surviving all-point orthogonal feasibility certificate and distance-law characterization are mathematically separate. Literature priority remains provisional.

## value

PASS

The exact projection operator on the entire hypersimplex to a nontrivial sparse-paving matroid polytope and a rank/arrangement-independent conditional distance law are natural, potentially reusable computational and geometric invariants. Their proofs require checking feasibility of the orthogonal projection against EVERY other hyperplane; the beta height scaling alone would not establish a distribution of actual distances. The work does not demand a downstream theorem or claim novelty of the already-known cap-volume and Hausdorff ingredients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
