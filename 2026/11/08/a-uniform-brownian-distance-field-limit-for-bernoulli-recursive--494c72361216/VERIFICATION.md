---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With X_k=H_k-H_(k-1), parent choice gives X_k=1 or 1-X_(k-1), in particular nonnegative increments. The centered innovation xi_k=X_k-1+q X_(k-1) has conditional mean zero and variance pq X_(k-1). Summing gives (1+q)(H_m-mu m)=sum_(k=2)^m xi_k+Y_1+qY_m, with bounded remainder. Bounded-increment concentration and Borel–Cantelli give the height strong law. It also gives uniform predictable-variation convergence: sup_(m<=n)|H_m-mu m|/n tends to zero, so the scaled variation up to nt converges uniformly to pq mu t. Thus the bounded-jump martingale functional CLT yields the stated variance pq/(1+q)^3 for the interpolated height. For a last success k<=i, both v_k and v_(k+1) descend from v_(k-1), and the same is true by induction at all later times. Consequently the LCA deficit in distance from i to j is no more than twice i-k+1. The union bound n q^r and summability at r=ceil(3 log n/|log q|) yield a uniform O(log n) almost-sure error. Grid bilinear interpolation does not enlarge this error, and the ordered increment field of the linearly interpolated centered heights changes by at most 2/sqrt(n) within a mesh square. This proves convergence in the asserted uniform topology and the interval-overlap covariance. The first-order distortion tends to zero; coupling Lebesgue to uniform masses at grid labels mu i/n within O(1/n) gives the measured limit. Monotone height and the root-to-newest distance sandwich the diameter by H_n and H_n+O(log n). Finally sum(j-i)=n(n+1)(n+2)/6 over unordered pairs; the Riemann-sum Brownian functional is 2 sigma integral_0^1 u(1-u)dB(u), since u(1-u) is the area of ordered pairs crossing u. Its variance is 4 sigma^2/30. The baseline shift mu(n+2)/3 versus mu n/3 is negligible on the square-root scale.

## originality

PASS

Restricted to the uniform second-order birth-time pair-distance field and its new projections, notably the centered mean-distance fluctuation. Earlier exact-catalogue results cover the diameter CLT, the endpoint-height variance, and a same-model uniform first-order distance comparison that implies the interval metric limit. Those overlapping ingredients, first-order facts and diameter consequences are not credited as independently new. The frozen headline and primary theorem are the uniform Brownian field; the diameter and mean are stated as consequences, not new independent findings.

## value

PASS

The distinct output tells how distances for overlapping and disjoint birth-time intervals fluctuate together, uniformly across all pairs, rather than giving further individual depth or diameter marginals. It appears at a genuine scale below the deterministic linear geometry. Integration yields an explicit centered mean-distance variance and shows why the scalar result is part of the same field rather than a separate simulation finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
