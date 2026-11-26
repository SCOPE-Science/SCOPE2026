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

The fixed points of A composed with binary Frobenius form a binary vector space and are exactly the idempotents. In a minimal F_q dependence of binary-independent fixed vectors, normalize one coefficient to 1. Applying the semilinear map squares all coefficients; uniqueness of the normalized relation forces them into F_2, a contradiction. Hence D<=n. For k<=n, each eligible binary k-subspace has g_k ordered bases and all these bases are F_q-frames; there are Q_{n,k}(q)/g_k such subspaces. For any one of their frames the invertible group acts transitively, so the probability of sending its squared frame back to the original is 1/Q_{n,k}(q). This gives the exact moments including k=0. Comparing to q=2 and inverting the finite unit-triangular Gaussian-binomial transform gives the specified probabilities. The n=2 and n=3 histograms reduce respectively to (2,3,1)/6 and (48,98,21,1)/168; removing zero gives 2^D-1. The frozen checker and recorded finite histograms were inspected only; the proof is not inferred from those tests.

## originality

FAIL

The October 25 Resultary record states the same entire law for all n and all binary extensions with the same uniform labeled measure, counting zero as well. Transpose is a bijection on the uniform sample, subtracting one converts the count to nonzero idempotents, and binary logarithm recovers D. Its exact probabilities and the frozen expression are algebraically identical; the moments are those of the same known law. The different elementary proof is not a new distribution theorem.

## value

FAIL

The full random idempotent law is a meaningful statistic, but its entirety is already known for this sampling measure. The frame count is a concise alternative derivation; the frozen finding claims a law and its moments, not a distinct theorem or computational capability enabled by a new method. Subtracting the zero solution, rewriting known probabilities and deriving their moments leave no independently valuable new claim as submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
