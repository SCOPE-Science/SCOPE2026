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

A cycle with fresh speeds has duration L/M_N and tail P(M_N<L/t)=(1-exp(-λL/t))^N. Its tail is asymptotic to (λL)^N t^(-N), giving exactly the positive moments of orders p<N. For N≥2, the finite-mean regenerative occupation measure is invariant and unique on the stated position-and-speed state space (each admissible state reaches a fresh cycle after finite time, and normalized time averages identify every invariant probability). For N=1, fix any η>0 and count time with V≥η: the cycle reward is bounded by L/η, while the average cycle duration diverges almost surely by the truncated strong law. The time fraction, including any final incomplete cycle, is zero in the limit from any admissible initial state. An invariant probability would then assign zero probability to each V≥η, impossible for a strictly positive speed. At equilibrium substitute age a=uL/M_N in the occupation integral: the mark distribution is normalized by E(1/M_N) and U is independent uniform. The minimum is exactly L(1-U), while the tagged mean is strictly above L/2 since the tag fails to have maximal speed with positive probability. Writing Y=max_i(λV_i), the product-law probabilities of Y<(1-δ)log N and Y>(1+δ)log N are bounded by exp(-N^δ) and N^(-δ). The former event contributes at most log N·(E Y_3^(-2))^(1/2)·exp(-N^δ/2) to E(log N/Y); Y_3's inverse second moment is finite by its small-y distribution. This verifies L¹ convergence of log N/Y to one and hence total-variation disappearance of the tilt even for events involving all particles. Under the untilted law the empirical Exp(1) measure converges and its mean tends to one. Rescaling by U/(Y/log N) gives both the fixed-tag joint law and weak empirical convergence; the common U is not averaged out. Evaluation above z>0 is continuous at every limiting measure, and solving exp(-z/U)≤q gives z/(-log q) on 0<q<exp(-z), zero below and one above. The empirical first moment and unscaled collapse follow by the same product-law law of large numbers and total-variation transfer.

## originality

PASS

Best-of-knowledge pass for the combined population profile: an exactly uniform front with a logarithmically scaled, conditionally exponential random empirical bulk, including its random exceedance law. The survival and finite-mean cutoff are existing coverage; neither they nor the routine regenerative change of variables are credited as independent novelty. The strongest model-family overlap, a distinct same-day record, treats fixed population and different finite-mean speed laws, and does not give the asserted empirical crossover.

## value

PASS

The theorem distinguishes the front, which spans the full interval at every N, from a macroscopic empirical bulk concentrated near reset. The retained common clock supplies a nonconstant empirical exceedance fraction even at diverging N, so the exact random conditional measure answers a question that a tagged marginal or a two-point correlation alone cannot. This is a concrete prediction for a natural regenerative many-particle model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
