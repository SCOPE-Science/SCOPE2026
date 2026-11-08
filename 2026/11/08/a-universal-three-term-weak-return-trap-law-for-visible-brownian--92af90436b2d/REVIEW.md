# Scientific review

## Correctness — PASS

The proof reconstructs the exact regenerative single-cycle mean; solves the positive-return splitting/exit boundary problems; derives the negative-return OU mean via a globally remainder-controlled scaled-complementary-error-function expansion; controls the integrated remainder using the clock's finite second moment; and uses stopped first-, second- and third-moment Brownian identities. In particular the clock-independent constant \(L^2/(2D)\) comes from a quadratic optional-stopping cancellation, while the cubic identity \(\mathbb E[B_{T\wedge R}^3]=-6DL\mathbb E[(R-T)_+]\) fixes the first protocol-dependent term. The sharp Poisson specialization and strict comparison with uninterrupted OU follow algebraically. Fifty-two independent numerical checks passed, without being treated as an infinite-parameter proof.

## Originality — PASS (qualified)

The full 2025 Frydel preprint directly covers the visible-return harmonic protocol and has exact renewal/mean-time expressions, and the 2023 Biswas–Kundu–Pal paper establishes a general stochastic-home-return renewal framework. These **already cover the model's baseline formulas**, which are therefore explicitly excluded from the novelty claim. The October 2026 Dubey–Pal paper covers the harmonically confined two-phase model. The new assertion is a three-term weak-return-trap theorem for every independent finite-second-moment reset-clock law, with a universal constant term and an explicit strictly positive first clock-dependent correction. The closest accessible primary full texts give MFPT formulas, comparisons and phase diagrams but not this asymptotic statement. Semantic searches found no equivalent registered finding; absence of a search hit is not a proof of novelty. There remains a priority risk from unindexed supplements and partially accessible newer formulations.

## Value — PASS

Harmonic traps are implementable return controls and the weak-confinement limit is experimentally meaningful. Determining a universal divergence plus clock-independent finite term is a structural classification, not a routine single-parameter numerical calculation. The first nonuniversal coefficient quantifies a positive overhead against uninterrupted OU search and the Poisson factor \(1+6/(q\sinh q)\) gives a testable dependence on reset frequency. Arbitrary finite-variance clock laws—including deterministic scheduling—share the same two leading terms, improving the interpretability of weak-return experiments.

## Limitations and closest prior literature

The result is a theorem for driftless search, 1D OU return, active target sensing during return, and independent clocks of finite second moment. All asymptotics fix the reset law. The underlying renewal model and the existence of finite-parameter MFPT formulas are prior results. Closest comparisons: Dubey–Pal (2026, arXiv:2610.18814), Frydel (2025, arXiv:2511.14646), Biswas–Kundu–Pal (2023, arXiv:2307.16294). No independent scientific review or certification is claimed.

Self-review: passed. Independent audit: not yet performed.
