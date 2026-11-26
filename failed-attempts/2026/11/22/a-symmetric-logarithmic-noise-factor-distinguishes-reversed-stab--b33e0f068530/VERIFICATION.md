---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For t>0 and independent unit-scale processes, conditioning on the inner clock and using self-similarity gives the independent-factor products t^(beta/alpha) S_alpha J_beta^(1/alpha) and t^(beta/alpha) S_alpha^beta J_beta. In particular J_beta has the one-time law S_beta^(-beta), by the first-passage tail and scaling, so the stable gamma ratio yields both moment formulas. The moment strip -alpha<Re z<alpha is common to the two products, contains an open neighborhood of zero, and gamma reflection gives the stated quotient on the imaginary axis (continuously 1 at zero). For a=1/alpha and b=beta the quotient is the logistic ratio phi_a phi_b/(phi_1 phi_ab). The logarithmic-scale Bose kernel is strictly convex because its positive derivative is q e^q/(e^q-1)^2 with q=x exp(-y), and its log derivative in q is 1/q-coth(q/2)<0. The rectangular difference is therefore strictly positive; it is (a-1)(1-b)/x+O(x) near zero and decreases exponentially at infinity. This proves an integrable-in-the-Lévy-sense symmetric density, a nondegenerate centered noise of finite variance, and the independent convolution on each one-time logarithmic marginal. Differentiation gives the common mean (beta/alpha)log(t)+gamma(beta/alpha-1); expanding the logs of the sinh factors to order two gives variance gap (pi^2/3)(a^2-1)(1-b^2). Jensen is strict for strictly convex tests with finite expectations. This says nothing about the joint law of the original two compositions or a process-level noise and does not compare the raw clocks in finite-mean convex order. At either index-one limit the quotient is 1. The supplied protocol and numerical checker were inspected but not run.

## originality

FAIL

No inspected source was found phrasing the result as this exact clock-order comparison. However, the claimed new noise and four-term positivity are a scale specialization of the known logistic background-driving Lévy law, not a new infinite-divisibility mechanism. Jurek–Yor give the exact background-driving density and integral representation; these imply the infinite divisibility of every iterated scale remainder of the logistic law by the displayed one-variable monotonicity test. The standard one-marginal transforms of the two clocks identify the quotient as precisely such a remainder. The failure rests on this concrete implication, not on an empty search or on assigning the exact clock wording to an older source.

## value

FAIL

Comparing the two clock orders is a natural question, and the computation is a readable illustration of the logarithmic scale. The claimed new kernel is nevertheless an iterated scale remainder of a known law, identified by reflection from standard transforms; its sign test is exactly monotonicity of the known background-driving spectral kernel. The variance and Jensen corollaries add no nonmechanical invariant or result once that remainder is identified. No separate process-level or wider non-logistic theorem is established, and the record has no genuine new valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
