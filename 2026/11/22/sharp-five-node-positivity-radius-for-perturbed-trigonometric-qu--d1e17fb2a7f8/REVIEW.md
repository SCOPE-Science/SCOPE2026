# Self-review

## Correctness — PASS

The four-sine Lagrange formula has a strictly positive denominator for five cyclically ordered distinct nodes. Its normalized integral gives a three-cosine numerator whose sign is optimized uniformly over four perturbation intervals: positive derivative in the first free angle, negative derivative in the last; explicit four-corner comparisons and positive sine interpolation handle the two inner angles. The unique algebraic root gives the exact sharp radius. The constructed alternating grid has negative weight for every larger radius below one half. Supplementary independent Fourier-moment solves and direct numerator checks passed. The finite checks do not replace the analytic universal proof.

## Originality — PASS, with remaining publication-priority risks

Austin's 2016 thesis reports quadrature-weight experiments, including sub-quarter negative weights for seven/nine nodes, not the sharp five-node radius. Austin–Trefethen (2016/2017) give perturbation error and Lebesgue-constant theory, not a five-node sign classification. Yu–Townsend (2022) provide a large-grid alternating negative-weight construction and Appendix B size bounds; that alternating design is explicitly acknowledged here as prior, but their stated large-size results do not determine the exact all-grid five-node threshold. Indexed comparisons include the closest three-node exact positivity result; it is a first-harmonic claim and does not imply the second-harmonic five-node result. Possible historical equivalent formulas in trigonometric moment theory remain a risk.

## Value — PASS

This is the first nontrivial multi-harmonic small-grid robustness boundary after the three-node first-harmonic case. Positivity is a natural stability/safety property for interpolatory quadrature, and a precise deterministic tolerance can be used to specify or test five-point rules. The strict inequality \(\alpha_*<1/4\) separates positive-weight robustness from the common one-quarter conditioning scale. The classification supplies an extremal perturbation and all zero-weight boundary designs; it is not merely a routine substitution into an asymptotic inequality. Its scope is deliberately finite and does not claim a general grid-size theorem.

## Closest literature and limits

The thesis of Austin (2016), Austin–Trefethen (2016), and Yu–Townsend (2022) address the same perturbed periodic grids; the thesis and Yu–Townsend already show negativity in larger cases, so this work does not claim the original discovery of negative weights. A previously indexed three-node result covers a different degree. Historical equivalence and independent review are outstanding; no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
