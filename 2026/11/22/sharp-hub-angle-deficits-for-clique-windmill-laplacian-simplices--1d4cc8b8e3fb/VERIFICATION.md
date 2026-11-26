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

Independent proof check of RESULT.md lines 4–23 and 25–92. For Gaussian objectives the score differences between hub and periphery are n(G_0−mean G_periphery)−(Z_{b,j}−mean G_periphery), with d=rm, n=d+1, and Z_{b,j}=rG_{b,j}−sum_{k≠j}G_{b,k}. Projecting onto the zero-sum hyperplane does not change the scores. The first normal factor is independent of the entire centered peripheral array. Its variance before multiplication by n is 1+1/d. The centered maximum is almost surely positive since the centered array has zero sum and is not identically zero. This proves the strict finite bound and the exact conditional probability. The uncentered maximum has mean squeezed between the maximum of m iid normals of variance r²+r−1 (one per clique) and sqrt(2 log(rm)) times their standard deviation (exponential-moment bound on all coordinates). The usual Gaussian tail bound at (1−ε)sqrt(2 log m) gives the matching lower asymptotic; the negative part of the iid maximum has bounded mean. Centering does not change the expected maximum, and integrating the union bound for the maximum magnitude gives a third moment O_r((log m)^(3/2)). Taylor expansion of Φ at zero thus yields the coefficient, with error from linearization O_r((log m)^(3/2)/n³). Transitivity gives the exact peripheral probabilities. At equal order the two logs differ only by log 2, so the deficit ratio is sqrt(5), not the ratio of the angles. The alternate direct Gaussian gap covariance is (n²+d+2) times the all-ones matrix plus block diagonal Cov(Z); it yields an independent one-dimensional quadrature for the star, including agreement with the bivariate arcsine formula at m=2.

## originality

PASS

Credit the already indexed leading star law and the standard Gaussian orthant representation; those are not the claimed contribution. The supported distinction is the explicit first deficit for the fixed-r windmill family and its equal-order matching sensitivity. The closest same-family dihedral results concern a different quantity, and the closest rank-one cone family can cover the finite star representation without an identified joint dimension/sharp-deficit asymptotic. No examined statement covered the fixed-r coefficient or the sqrt(5) ratio.

## value

PASS

The leading 1/2 mass is insensitive to the graph change. The first deficit supplies a useful Euclidean geometric test: adding a matching at fixed hub degree and vertex count changes the first correction by a sharp nontrivial factor. The family-level coefficient isolates within-clique structure and distinguishes measures that leading-angle or combinatorial information alone cannot distinguish.

The dated certificate retains the supplied scientific assessment, sources and limitations.
