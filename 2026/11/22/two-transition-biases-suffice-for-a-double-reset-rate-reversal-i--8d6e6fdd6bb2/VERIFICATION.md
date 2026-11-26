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

Read as specified with initial site equal to the fixed reset site. Each cycle absorbs at endpoint j with probability E_5[s^T 1_{J=j}], and retries from 5 otherwise. Renewal divides the lower cycle probability by the sum for either endpoint. Solving the killed tridiagonal equations gives cofactors for the two directed paths of lengths 5 and 7, with unused blocks [6,11] and [1,4] and directed path-weight ratio e(1-e). Each restricted killed matrix has spectral radius below 1: at fixed e>0 every state has a uniformly positive chance of leaving its block in a bounded number of steps. Thus the determinant is initially one and never zero for 0<=s<=1. Independent symbolic sums over disjoint adjacent transpositions verify both continuants and the derivative numerator. F is positive at x=0 and x=1, and negative at x=3/4 uniformly, independently checked by strictly negative Bernstein coefficients after rescaling the e interval. Since the nonzero polynomial has finitely many roots, each of the two disjoint subintervals has a sign-changing root; the derivative switches in the opposite direction since its denominator is positive. At e=1/20 the exact quartic has Sturm variations 4 and 2, is square-free, and changes sign in both stated rational brackets; this gives exactly a minimum then a maximum in increasing s. For homogeneous p with q=1-p, the killed resolvent recurrence after scaling by (q/p)^(i/2) gives U/V=(q/p)^(N/2) sinh((N-z)theta)/sinh(z theta), cosh(theta)=1/(2s sqrt(pq)). The logarithmic derivative in theta has the sign of N-2z because t coth(t) is strictly increasing for t>0. As theta is decreasing in s this is monotone (constant at the midpoint), covering both parities and confirming the one-valued exclusion without assuming the cited proof. The literal phrase 'both absorbing boundaries are reached almost surely' is an editorial misstatement: one of the two is reached almost surely and each has positive probability. The process, renewal proof and finding use first absorption, not simultaneous or successive visits to both endpoints.

## originality

PASS

General double turning in heterogeneous chains is not new. The substantiated distinct result is double turning using just two complementary probabilities, on a whole explicit interval, together with an exact two-root witness and hence sharp alphabet threshold. The known homogeneous monotonicity supplies the lower bound, not the two-bias construction. The most similar indexed examples use more than two probabilities. Same-day overlap is compared by mathematical scope, not presumed chronological order.

## value

PASS

Bounding the alphabet, rather than the number of states, tests how much spatial heterogeneity is necessary to defeat homogeneous reset monotonicity twice. The result gives the sharp threshold on that natural structural measure and a whole interval of two-bias examples, so it is not just another many-parameter numerical witness. The exact rational root certificate makes a reusable benchmark for reset-response classifications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
