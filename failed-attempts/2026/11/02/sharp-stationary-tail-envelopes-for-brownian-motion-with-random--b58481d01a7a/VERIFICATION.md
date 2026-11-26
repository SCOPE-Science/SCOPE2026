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

Backward Poisson gaps yield iid symmetric Laplace increments of rate a=√(λ/D). Since products of R are at most ρ^j, the backward series converges absolutely, and a common-noise coupling contracts initial separation by at most ρ raised to the number of resets, proving uniqueness. For a<s<a/ρ, the Laplace transform of the absolute majorant for the residual W is bounded by ∏_{j≥1}(1−sρ^j/a)⁻¹, which also justifies passing from finite conditional products to the limit. Conditioning on W, the independent first Laplace increment gives e^{ax}P(X>x)→(1/2)E e^{aW}, since P(W>x)=O(e^{−sx}); symmetry gives the absolute coefficient. The nonnegative series is coordinatewise increasing in every even multiplier moment and includes a standalone E R² term. Jensen and the chord bound therefore give the stated extremizers, strictly unless supported as claimed. The Bernoulli geometric-run identity and deterministic product both agree with the alternative product T=∏_{k≥1}(1−E R^{2k})⁻¹ proved in the comparison below. Read the frozen verifier and its output without execution; `python3 /workspace/branches/review_reproduction.py 4` separately bounded both endpoint products by rational intervals and checked an interior exact finite tree with a certified remainder. Finite checks do not prove the tail limit.

## originality

FAIL

The exact envelope is a mechanical implication of the preexisting subordinator exponential-functional moment theorem and the leading-Laplace innovation, not just a qualitative analogue of an earlier bound. Poisson thinning treats R=0 as independent killing within the earlier theorem's hypotheses. The stationary moment recurrence in the distinct same-day Resultary record supplies a second route; this is scientific overlap, not evidence for priority between same-day records.

## value

FAIL

The optimization question is natural, but in this strict-cap Poisson model the existing exact moment theorem reduces the entire sharp envelope and both strictness claims to a telescoping sum and pointwise Jensen/chord comparisons. No new asymptotic mechanism, harder regime, or distinct invariant survives the coverage check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
