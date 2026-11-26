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

The bounded categorical summands have uniformly bounded fourth moments for their normalized centered sums (the fourth-moment expansion is O(N²) before scaling). The cyclic functional is continuous and at most 6 times the maximum coordinate magnitude, so its first two moments converge by uniform integrability even when the Gaussian covariance is singular. Coupling the Gaussian through the positive square root of diag(p)−ppᵀ gives simplex continuity. With three coordinates the statistic is twice the range, giving full permutation invariance. On the symmetric line S=Z₁−Z₃ and M=−3Z₂ have variances 2a and 18a(1−2a) and zero covariance; their independence and the identity |(M+S)/2|+|(M−S)/2|=max(|M|,|S|) give the stated polar integrand. Its first and second angular moments give the stated profile. As an independent symbolic route, forming the covariance of the three contrasts and using pairwise Gaussian absolute-value covariances gives V(u)=1.052263614148347, V′(1/3)=0, V″(1/3)=3(81−16π−24√3)/π≈−10.34637812770789, and V(b)=4(1−2/π)≈1.453520910529675. The Gaussian density restricted to the fixed tangent plane is positive definite near u; parameter derivatives of its first two range moments are dominated on a smaller neighborhood by a polynomial times a common Gaussian tail. Thus the Taylor Hessian exists, permutation symmetry makes it scalar on the tangent plane, and ‖(1,−2,1)‖²=6 converts the ray second derivative to the stated coefficient by division by 12. Since b majorizes u and gives a larger value, Schur concavity fails; nearby nonuniform vectors also majorize u but give smaller values, ruling out Schur convexity. The segment drops below both endpoint values before reaching b, violating quasi-concavity and forcing a minimum strictly between the two endpoints.

## originality

PASS

The full permutation symmetry is the elementary three-point range identity. Credit the Gaussian/folded-normal framework and, in particular, the already covered uniform variance value at three bins from Part 5 Theorem 3.1; the simple standardized boundary law is a benchmark. The supported distinct claim is the full-simplex negative Hessian at uniformity coupled to a larger boundary value, with the resulting majorization and quasi-concavity counterexamples and the ray minimum for this matched cyclic statistic.

## value

PASS

Three bins are the first genuine cyclic case, have full permutation symmetry, and sit below the hypotheses of the inspected general nonuniform cyclic formula. A proved local maximum at uniformity might suggest a majorization principle; pairing its exact curvature with an explicit larger half-half boundary value decisively refutes that principle, and the ray profile also refutes quasi-concavity. This adds a structural conclusion about a natural variance family, not just a repeated uniform benchmark or a numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
