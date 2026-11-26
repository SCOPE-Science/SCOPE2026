---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Condition on the unordered value set A in the first i positions. The conditional mean of R_i is always 1/i. If j is in the suffix, S_j depends only on the suffix order; if j is in A but a smaller value is outside A, S_j is identically zero. Otherwise all values up to j lie in A, and the position of the maximum of A is independent of their induced order unless A=[j] and i=j. In that exceptional case both indicators equal the indicator of pi_i=i, with variance (i-1)/i^2, and the prefix set has probability 1/binom(n,i). Total covariance now gives the exact kernel; the Bernoulli marginals give the stated joint law and off-diagonal independence. For the total covariance, i=n, n-1 and 2 give 1/n-1/n^2, 1/n^2+O(n^-3) and 1/(2n^2)+O(n^-3). The exceptional near-end terms i=3,n-2,n-3 are O(n^-3) individually, and the middle range is at most n/binom(n,4). The independent uniform successive relative ranks give the marginal variance H_n-H_n^(2), hence the correlation asymptotic. The deterministic first indicators and n=2 are consistent with the formula.

## originality

FAIL

A distinct Resultary finding gives the identical forward–inverse indicator covariance for every i,j, with the same rank, independence statements and aggregate expansion, and a weighted extension. The catalogue labels it later; this verifies equivalent coverage, not who had priority. Separately, Jin’s prior generating function already determines the unlabelled joint count law; it does not give the positional kernel.

## value

FAIL

A labelled diagonal dependence law is intrinsically informative and stronger than a joint count law. The frozen record, however, adds no distinct result to the verified equivalent kernel and its consequences. The aggregate reduction is also determined by a prior count enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
