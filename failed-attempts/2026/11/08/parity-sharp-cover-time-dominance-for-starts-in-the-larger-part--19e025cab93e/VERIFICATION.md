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

For the specified non-lazy walk, the two streams of uniform vertex draws are independent; fixing the first label in the starting part leaves the law of its coupon completion count unchanged by label symmetry. The alternating draw counts give all three CDF formulas including t=0. In RESULT.md lines 43–53, the Stirling recurrence differentiates z(1+z)Q_k; Rolle interlacing from Q_1=1 puts all roots of Q_k simply in (-1,0). Newton's inequalities give strict unnormalized coefficient log-concavity on the positive support, so U_n(k+1)/U_n(k)=1+A_{n-1}(k)/A_n(k) increases strictly over 1<=n<=k. The zero-support and first positive time k=a-1 are separate cases. With the same independent coupon counts on both starts, the time difference equals +1, 0, or -1 according to their ordering, giving precisely the stated mean identity and boundaries. For K_{3,2} the first gap is (2/9)(1/2)=1/9 and the mean gap is 1-3E[2^(1-X_3)]=7/10 by summing the geometric series for the 3-coupon distribution. The 'uniquely' wording is about the starting part, not a unique vertex: the minimizer set is exactly A when a>b. The supplied checker and verification notes were inspected, not executed; the analytic proof is unbounded.

## originality

FAIL

An independent indexed companion result for the d-offer walk explicitly excludes d=1 from its stated novelty, but its proof covers the entire audited claim by immediate substitution, not just a similar inequality. The mechanical implication follows at d=1 from the actual displayed probabilities and likelihood-ratio proof. This is demonstrated overlap, not a historical ordering determination from same-day metadata. The Stirling proof is a different elementary route, not a distinct claimed result or new polynomial inequality.

## value

FAIL

A sharp start-side order for all deadlines is a useful question, but the entire audited answer is a one-parameter specialization of a comparison already supplied by the multi-offer proof. The specific example and strict test-function consequence are routine evaluations of that coverage; the alternative use of classical ordered-Bell real-rootedness does not establish a new structural fact or a valuable surviving finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
