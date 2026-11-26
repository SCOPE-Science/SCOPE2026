---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Berger moments are 1,m,ms at orders 0,1,2 and all positive-order denominators are positive. I independently checked the upper certificate by tilting with (R−t)dμ/(R−m), which gives a probability measure of mean a=m(R−s)/(R−m). Write C=U_n and f(t)=t^(n+1)−Ct^n. The continuous quotient (f(R)−f(t))/(R−t) equals t^n+(R−C) times the geometric divided difference (R^n−t^n)/(R−t). Equivalently it is t^n+(R−C)Σ_(j=0)^(n−1) R^(n−1−j)t^j. This is strictly convex on [0,R] for n≥2, since C≤R and t^n alone is strictly convex. Jensen yields ∫f≤0 by comparison to the one-point tilted law at a, which is exactly the tilt of the claimed two-atom extremizer. Equality forces support in {a,R}, then the first moment fixes the masses. This also explains the sign in the frozen Hermite proof: the remainder quotient consists of the nonnegative complete homogeneous terms given there. The lower bound follows from log-convexity; equality at any n≥2 forces equality already at n=2 and hence constant positive support under the t-tilt. When s=m the variance is zero, and when s=R the expectation of t(R−t) is zero, giving the stated unique endpoint laws. For interior s, mixing the lower and upper measures varies the ratio continuously between distinct endpoints; every positive share of the upper law charges R, while lower equality forces norm squared s. Moment roots converge to the support supremum, as do the monotone ratios; small mixture shares approximate s uniformly on any fixed finite set of indices. Finally the odds π/(1−π)=mδ/(R−m)^2 and the factor (R/a)^t give the stated crossover by substitution, with O(δ log(1/δ)) centering error. Inspected the frozen verification and checker; did not execute the bundled code or treat its reported finite assertions as proof.

## originality

FAIL

The central sharp simultaneous upper envelope, its two-point extremizer and its polynomial ratio comparison are covered by Resultary b6e42f10def5, an earlier distinct record. The earlier theorem assumes support bounded away from zero but allows any observation index. At its index zero set b=R and v=m(s−m): this gives exactly the frozen U_n and maximizing law. The nonnegative-support extension is obtained by an affine perturbation and continuity, with uniqueness from the same sign certificate. The known envelope also gives the crossover by balancing its two terms; exact-norm endpoint removal uses standard lower rigidity and mixing. This is demonstrated coverage of the main claim, not a failure caused by unavailable literature. The earlier record does not literally state the crossover or the open exact-norm interval.

## value

FAIL

A sharp simultaneous envelope is a useful structural object, but the earlier result already supplies that mathematical value. What this submission adds beyond it is a straightforward zero-endpoint limit and mixture corollary and the direct two-term asymptotic of the same explicit formula. Those are reasonable explanatory consequences, but do not supply a separate substantive mathematical contribution as a final finding; they do not justify a narrowed repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
