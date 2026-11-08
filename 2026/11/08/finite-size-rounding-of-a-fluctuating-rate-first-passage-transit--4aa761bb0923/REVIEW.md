# Scientific review: finite-size rounding of a fluctuating-rate first-passage transition

## Correctness — PASS

The exact claim is confined to a single absorbing/reflecting one-dimensional nearest-neighbor continuous-time walk, with independently drawn nonnegative rates satisfying \(\mathbb E e^{-s\lambda}=(1+s^\alpha)^{-1}\) and deterministic refresh period \(\tau\). Absorption happens at its physical jump time. For each finite interval, the killed generator is positive definite; renewal across rate-refresh epochs yields its physical-time mean as a spectral multiplier. The scalar multiplier splits *exactly* into a fractional inverse and a nonnegative remainder uniformly bounded by \(\tau\alpha/(1+\alpha)\). The trigonometric eigenbasis, source-vector coefficients, fixed-parameter asymptotics, and logarithmic critical-window profile are explicitly derived in RESULT.md. The finite-volume independent diagonalization and amplitude tests replayed successfully. The tests are not replacements for the proofs of the infinite-volume statements.

## Originality — PASS, with priority risk

The closest primary papers were read for statements rather than title matching. Levit and Reuveni (arXiv:2609.26925, first posted September 22, 2026) establish the same rate law and the half-line threshold \(\alpha=1/2\), but not reflecting finite-volume rounding or its exact amplitude. Arutkin and Reuveni (arXiv:2302.07041) derive finite-interval exit formulas for the exponentially resampled-rate case and indicate the eigenmode method's broader geometry; this is an important structural antecedent, but not the periodically refreshed heavy-tailed finite-size critical window. Angstmann and colleagues (arXiv:2410.10077; arXiv:2511.18256) establish related finite-domain spectral fractional models and first-passage formulas, including two absorbing boundaries, but with a different microscopic time construction. The actual novelty is therefore the discrete mixed-boundary *physical-time* mean, bounded correction, three volume regimes with constants, and two-parameter finite-size crossover taken together, not the general spectral renewal technique or the already known infinite-half-line threshold.

Scientific search and comparison included published-finding corpus queries for finite-size first passage, Mittag-Leffler jump-rate refresh, absorbing/reflecting boundaries, mixed spectral fractional Laplacians, exact log criticality, as well as primary paper text and related prior claims. No indexed statement examined supplied this complete result. The strongest residual risk is an unindexed general killed-graph resolvent or fractional first-passage calculation that already gives the same mixed-boundary asymptotic crossover as a direct specialization. Negative search results do not prove absolute novelty.

## Value — PASS

A sharp infinite-system mean-time transition is difficult to measure on a finite chain. The theorem predicts exactly how a single reflecting boundary rounds that transition: a bounded regime, a logarithmic divergence at the critical tail exponent, a fractional power above it, and a universal profile when the tail exponent differs from criticality by \(O(1/\log N)\). The explicit physical-time correction bound separates new finite-size scaling from complications of observation within a refresh interval. These are natural quantitative observables in confined fluctuating-diffusivity models, and are not an arbitrary finite table or a substitution into a known half-line statement.

## Limits and external review

The microscopic reflecting convention, fresh-at-zero rate sampling, fixed initial site and refresh duration, and precise rate distribution are indispensable. The results are analytical and checked with finite numerical examples; no external physical data or independent scientific audit is claimed. The source comparison is substantial but not an exhaustive priority certificate.

Self-review: passed. Independent audit: not yet performed.
