---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The path exploration gives disjoint successful stopping events after k fresh delegators, with success hazard m/(N−1). On the sqrt(N) mesh the survival product converges to exp(−ct−t²/2), dominated by a Gaussian tail. The small-m Gaussian bound and large-m repeat bound are sufficient for the two probability limits by Markov's inequality; the critical claim is only a mean limit. Complete representation is exactly the prescribed-root forest event; the minor N I−J has determinant m N^(N−m−1), with the m=N case handled separately. The joint factorial moment for any chosen counts a_ℓ of distinct cycles is (N−m)_(∑ℓa_ℓ)/(N−1)^(∑ℓa_ℓ) times the product of ℓ^(−a_ℓ), since simultaneously occurring distinct cycles are vertex-disjoint. It converges to the independent Poisson factorial moments, and the uniform geometric tail for the expected number of long cycles supplies the total-count limit. The mean starts at length two, consistently with forbidden self-delegation. The mass of zero cycles then matches the direct forest calculation.

## originality

FAIL

The two central scales are covered by exact mathematical reductions: the indexed Bernoulli-direct model gives the fixed-m first moment by coefficient extraction and its square-root crossover by monotone conditioning; the complete-coverage formula and linear-regime limit are direct consequences of the classical prescribed-root forest count. Pairing these two formulas does not add an uncovered mathematical assertion. The residual cycle statement is a routine application of disjoint labeled cycle enumeration and the factorial-moment criterion; an antecedent explicitly giving every fixed-m cycle statement was not verified. This is a decision about statement coverage, not a claim of historical priority for the indexed record.

## value

FAIL

The contrast between average and universal representation is a useful explanation of the model, but the frozen finding does not supply a distinct mathematical gap beyond the mean and forest laws. The two-scale contrast is an immediate comparison of their existing consequences, and the remaining cycle count is the routine disjoint-cycle Poisson computation rather than a new representation invariant. In particular, the result does not determine the critical represented fraction's fluctuations or distribution; the closest indexed finding already goes beyond the mean in that direction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
