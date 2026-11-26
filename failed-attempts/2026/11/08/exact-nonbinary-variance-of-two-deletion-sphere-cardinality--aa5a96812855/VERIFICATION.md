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

Appending a symbol partitions deletion descendants into D1(u) and D2(u)a; their overlap consists of the one-deletion descendants ending in a. Retaining the terminal copy or deleting the last two symbols supplies the shorter prefix as appropriate, including the length-one base case. This proves the pointwise binomial(run count,2) plus long runs minus internal singleton returns formula. The increment parametrization is bijective, and on each nonzero block the number of choices at each step is 1 for a return and q−2 otherwise, proving the conditional binomial law even with self-inverse symbols. The centered conditional mean has linear coefficient (m−1)p and square-free pair coefficients 1 (nonadjacent) and −1/(q−1) (adjacent). Independence makes these terms orthogonal; adding the expected conditional binomial variance gives the boxed polynomial and its cubic leading term. Expectation simplifies to 1+(m−1)p+binom(m,2)p²; at m=1 the empty descendant has count one. Independent replay: python3 -B /workspace/branches/independent_checks.py 5 used leftmost embeddings and matched exact moments on 26,194 words, for q=2–5 and n=2–6. Finite only; the general result follows from the argument.

## originality

FAIL

Three earlier catalogue findings directly cover this uniform nonbinary variance. October 25 record 1cbd5a76d8bf gives an algebraically identical polynomial; November 2 record b1a2bd3da18e gives the same moments and conditional law, and record 8af4e5cf362e gives the moments and a full distribution formula. The comparison is for the exact same uniform linear word and distinct two-deletion outputs; the explicit restriction of novelty to q≥3 does not avoid these sources.

## value

FAIL

An exact variance for this natural channel statistic is useful in isolation, but the identical result is already given alongside stronger distributional information. The orthogonal expansion is a valid derivation; the frozen record does not show a separate new structural conclusion or application that would supply a valuable remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
