---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The repaired theorem is for the limiting variance per label and for a joint CLT at fixed interior retention, not a finite-size or moving-window optimizer. Shared leaves are labels vacant in both Prüfer words; single-position avoidance gives the finite factorial and cross-moment identities, with empty products at n=2. In m log a_{n,k} the coefficient of k²/n is c=(1−ρ)−(2−ρ)²/2, so the covariance contribution to the variance density is 2cQ², Q=e^(ρ−2). This gives v=Q−(3−2ρ+ρ²)Q². The positivity bound uses (3−ρ)Q≤2/e; the sign bracket for v' is 1−2(2−ρ+ρ²)Q, strictly decreasing from positive to negative, so exactly one strict maximum. For the Gaussian law, the shared stream count S is binomial in latent retention decisions, not observed coincidences; its conditioning leaves three independent fixed-total allocations. In the conditional characteristic-function integral, positivity of rates bounds the probabilities of Poisson box-count differences e_j away from zero. The independent-copy cosine identity then bounds 1−|φ|² from below by c||θ||²−C/n for small θ, giving Gaussian domination after θ=u/√n; on the complement the unperturbed modulus is uniformly below one and bounded f adds O(n⁻¹ᐟ²). The resulting conditional covariance is a Schur complement; the exact conditional mean differs from Poisson centering by O(1). The correction subtracts q² from each marginal leaf variance, ρq² from their covariance, qQ from marginal/common covariance, and (2−ρ)Q² from common variance. The conditional mean g_n(S) of H has derivative tending to Q at E S and second derivative O(1/n). The binomial fluctuation is asymptotically independent of the conditional limit by bounded conditional characteristic functions converging to a deterministic limit. It adds ρ(1−ρ)Q² to the last variance only; the matrix agrees with separate finite second-moment expansions. Replay: repaired RESULT.md, finite identities and both limit proofs; frozen check.py lines 9–70 (inspected, not executed) separately checks finite moments, not the limiting statements. No field or other tree-coupling result is asserted.

## originality

PASS

PASS is for the repaired claim only. The frozen AUDIT.json explicitly counts the noisy coupling and exact common-leaf factorial transform as novel. That component fails: the same-day c552f8b16e6b result gives the identical coupling and strictly stronger finite mixed-moment identity. A direct specialization gives the entire finite common-leaf transform, not just a numeric coincidence; the mixed vacancy counts also recover the joint finite leaf moments. Dates do not establish priority between the records. The repair removes novelty for these identities and uses them as credited premises. The surviving contribution is the uniquely maximizing retention of the limiting common-leaf variance at linear load plus the specified joint fixed-retention Gaussian law. The nearest primary and published limit theorems do not supply this combination or the individual repaired conclusions on inspected evidence.

## value

PASS

Even after removing the exact finite transform from the contribution, the result gives a sharp and interpretable nonmonotonicity: limiting noise of a natural common-leaf statistic is worst at a strictly intermediate retain probability, not at either baseline endpoint. The joint Gaussian limit identifies how that overlap covaries with each marginal leaf total, including fluctuation from the randomized shared-stream size. These are meaningful properties of the coupled-tree null model rather than a rebranding of known finite vacancy moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
