---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

In the actual frozen RESULT.md the degree of a fixed label is a sum of independent Bernoulli trials with mean c_gamma(log(v)/log(n))*log(n)+O(1). Exponential-tail upper bounds and the lower large-deviation bound n^{-I(t;c)+o(1)} reduce the maximum to max_a[a-I(t;c_gamma(a))]. Differentiating yields the interior maximizer 1-t/2 or boundary gamma and the unique cutoff gamma*=1-1/(2log2). Negative quadrant dependence of distinct child-degree events controls the second moment. Polynomial error bounds on dyadic n plus monotonicity prove a.s. coefficient; the unique maximizer of the rate function localizes the label in probability. Assumptions include fixed 0<gamma<1 and independent uniform parent choices.

## originality

PASS

PASS best of knowledge: arXiv:2510.18856 treats the same limited-memory recursive-tree framework but explicitly sets j(n)=theta*n or j(n)=n-n^beta, and Remark 1.1 leaves j(n)=floor(n^beta) to future work; its height/local-limit theorems do not imply the current maximum-degree constant or hub-position exponent. Related Resultary records on degree/leaf covariance and batch recursive trees do not cover this cutoff transition. Residual risk remains from broader recursive-tree extreme-degree literature, not located as a decisive covering statement.

## value

PASS

The earliest eligible vertex changes by a power-law cutoff, making a natural extreme-degree and hub-birth-label phase transition. The sharp exponent gamma*=1-1/(2log2), max coefficient and hub location jointly describe a nontrivial asymptotic regime that does not follow from ordinary recursive-tree degree maxima alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
