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

For j=1,2,3 the marked rings must be pairwise disjoint and each unmarked ring must avoid their union. This yields p1=q^(n-1), p2=q r^(n-2), p3=q r u^(n-3), then p3-3p1p2+2p1^3 by centering. The text uses u in the definition and Greek nu in subsequent equations; they denote the same third avoidance ratio, as is fixed by the probability argument and verifier. P>=4K keeps all ratios positive. Strict concavity of log h(j) gives r<q^2 and u<r^2/q<qr. With t=n-3, division by (qr)^t leaves a positive decaying exponential plus a positive growing exponential minus a constant. Strict convexity bounds the number of real crossings, hence also integer sign changes. I independently expanded the logarithms of the avoidance ratios with the sums of i and i^2 through cubic order, then expanded the exponent ratios through order P^-2; the constant and linear terms cancel and the quadratic coefficient is K^3(cK-1)(3cK^2-3K-2). The prefactor tends to exp(-3cK^2). Remainders are uniform for n/P on compact positive intervals at fixed K. The two distinct positive simple roots give strict sign test points on each side, chosen at integers for sufficiently large P. Continuity and the convex crossing bound pin both real roots by arbitrarily tight brackets; the integer samples force two actual sign changes. The P=8,K=2 signs at n=4,5,6 were checked by exact fractions.

## originality

PASS

The joint-moment enumeration is standard in mechanism, with pair cases in prior work. The inspected sources do not establish the global crossing bound or the evaluated fixed-K limit with the two sharp separated crossings for distinct isolation indicators in uniform random key graphs.

## value

PASS

Pairwise isolation dependence and the total-count third moment cannot resolve sign for three distinct marked vertices. For a canonical random-intersection graph this obtains two sharp sign boundaries and a matching global bound on the number of transitions, a meaningful classification of the connected three-vertex statistic rather than an isolated parameter example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
