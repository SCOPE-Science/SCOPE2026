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

For each summand W_S, an isolate in S contributes zero since k≥2 and S is connected whenever W_S is nonzero. Given the data determining W_S, any v outside S has probability (1−p)^(n−k−1) of being isolated on the event used by W_S: the edges to S are already absent and the remaining edges are independent. This gives E[IT]=(n−k)(1−p)^(n−k−1)E[T], including n−k=1. Subtracting E[I]E[T] gives the claimed sign and its unique root for positive E[T]. For t=k/n the function −log(1−t)/t=∫₀¹(1−ts)⁻¹ds is strictly increasing, giving the threshold ordering. Expanding its exponential gives the fixed-k and proportional-size limits; at k=n−1 the exponent is log(n)/(n−1), giving the final scale. The bundled verify.py was inspected, not run; it checks the 60 finite graph comparisons but does not contain the additional threshold stress tests described in the notes. None of the general conclusions depends on these tests.

## originality

FAIL

A distinct indexed shape-universal component covariance theorem covers the core formula and sign threshold by taking the first component to be a single vertex. Permutation averaging and linearity extend it to exactly the asserted arbitrary internal weights, even when the weights are label dependent. Ordering and scales are routine consequences of that same threshold and do not constitute an independent result.

## value

FAIL

The sign change is an intelligible graph-statistical phenomenon, but the contribution as frozen is an isolated-vertex substitution into a known exact shape-universal covariance, followed by permutation averaging and elementary analysis of its root. The size ordering and asymptotic expansions do not supply a separate structural result or an independent application.

The dated certificate retains the supplied scientific assessment, sources and limitations.
