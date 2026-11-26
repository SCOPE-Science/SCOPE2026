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

The order-two decompositions have projections proportional by positive constants to centered A(x)=E|x−X| and B(x)=E(x−X)². Finite fourth moment controls the kernel second moments, so the O(n⁻²) degenerate terms do not affect the limiting correlation. B cannot be constant on the support because each level has at most two points. If A were constant there, atomlessness makes every support point an accumulation point and A′=2F−1 everywhere, which would force F=1/2 on the support, incompatible with the two tails. Equality in Cauchy–Schwarz extends A=cB+d continuously to the support. Taking derivatives along support sequences, including endpoints of gaps, gives F(x)=1/2+c(x−μ) there. Monotonicity gives c>0; the bounded range of F makes the support bounded. Any internal open gap has endpoints with equal F by atomlessness, contrary to strict slope c. Thus the support is an interval and F is uniform. The converse has identical centered pair projections for G_n and Q_n=2S_n² at unit length. For the finite formulas, the same-pair variances are 1/18, 7/180 and covariance 2/45; distinct pairs sharing one index give 1/180. For any one pair there are 2(n−2) other pairs sharing an index, so each covariance entry is 2/[n(n−1)] times its same-pair entry plus 2(n−2) times 1/180 inside the brackets. This gives all three stated moments and the contrast variance. For any deterministic unit-interval sample, the centered bridge is the average of the translated periodic functions 1/2−{t−U_i}, up to values at jumps. Parseval yields (2n)⁻¹Σ_{i,j}B₂(|U_i−U_j|); subtracting diagonal terms yields the exact contrast identity including ties/endpoints. Under iid uniformity the sine/cosine CLT gives independent variance-1/2 coordinates; the expected Parseval tail is bounded by (2π²)⁻¹Σ_{k>K}k⁻² uniformly in n. The contrast limit is the stated centered weighted chi-square sum, with variance π⁻⁴Σ k⁻⁴=1/90. Almost-sure summability follows from its finite nonnegative uncentered mean, and the squared coefficients are summable for L² convergence.

## originality

PASS

Prior influence functions already give the uniform direction, and the Watson law and Bernoulli/empirical-bridge representation are classical. The exact contrast is an algebraic identification with that statistic, not a new Watson theorem. The supported distinct claim is the converse, ruling out all other atomless laws, together with the paired finite-sample moment formulas and their interpretation as a Gini–variance contrast. The inspected prior statements do not establish that classification.

## value

PASS

Determining which laws cause two common dispersion estimators to lose a first-order contrast is a natural characterization problem. The support argument resolves it without assuming a density or absence of gaps, and the exact finite covariance and second-order contrast explain what replaces the lost first-order fluctuation under the uniform law. The value is in this characterization and scale-estimator connection, not in a new goodness-of-fit limit theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
