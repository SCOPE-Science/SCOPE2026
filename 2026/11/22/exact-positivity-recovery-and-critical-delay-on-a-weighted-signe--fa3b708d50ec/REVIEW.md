# Scientific review: signed-triangle positivity recovery

## Correctness — PASS

For the stated repelling row-sum-zero three-vertex Laplacian, the quadratic characteristic identity fixes the two nonzero eigenvalues and the repulsive-edge coefficient. A two-exponential zero-count lemma proves exactly one recovery after the initial negative interval, while the attractive-edge coefficients are strictly positive and the diagonal entries are positive spectral sums. The same formula shows permanent repulsive-edge negativity when the negative weight reaches or exceeds the spectral boundary. Conservation and the sign census give the sharp induced maximum norm, and explicit derivative/root calculations establish the distinct small-repulsion and near-critical asymptotics. The self-contained checker confirms the polynomial identity with exact rational arithmetic and tests matrix-exponential values numerically; the infinite assertions rest on the written proof.

## Originality — PASS, with historical-priority limitations

The effective-resistance stability threshold was already known from Zelazo–Bürger (2014). The equivalence between stable simple-zero signed Laplacians and eventual positivity was established by Chen et al. (2020), with related general signed-network criteria in Fontan et al. (2022). The claimed result is not either background theorem: it identifies the *unique precise recovery*, all transition signs, the global norm peak, and an inverse-margin recovery horizon that separates from a logarithmic peak time. Targeted searches for the signed-triangle time law, negative-edge three-state matrix exponentials, and reciprocal-resistance critical recovery found no directly equivalent statement. A related general published spectral-window bound provides a worst-case universal positivity horizon, not an exact parameter-specific threshold for every weighted signed triangle. Earlier specialized three-state formulas and inaccessible full records remain priority risks; these searches do not prove uniqueness.

## Mathematical value — PASS

One negative edge in a positive path is the smallest nontrivial signed consensus loop whose stability is controlled by effective resistance. The exact one-crossing law supplies a physically interpretable positivity and maximum-norm contractivity horizon, instead of merely certifying that some eventual-positive time exists. The near-critical result separates two different operational timescales and shows that a finite amplification penalty can coexist with arbitrarily delayed positivity recovery. The small-repulsion quadratic amplification law provides the complementary perturbative regime. These are natural structural and quantitative limits, not arbitrary tabulated cases.

## Scope and limitations

Only symmetric conservative three-vertex signed Laplacians with two positive links and one repulsive link are treated. The general recovery time is defined by a unique implicit exponential root. A numerical checker cannot establish claims for all real parameters or times. The published works cited below cover broader qualitative stability and positivity conditions, and the historical-priority search is not exhaustive. No independent validation has been carried out.

## Closest sources

- Zelazo and Bürger, *On the Definiteness of the Weighted Laplacian and its Connection to Effective Resistance* (2014), https://arxiv.org/abs/1408.2187 — preexisting spectral threshold.
- Chen et al., *On Spectral Properties of Signed Laplacians with Connections to Eventual Positivity* (2020), https://arxiv.org/abs/2009.03581 — preexisting equivalence of stability and eventual positivity.
- Fontan et al., *Multi-agent consensus over time-invariant and time-varying signed digraphs via eventual positivity* (2022), https://arxiv.org/html/2203.04215v1 — related signed-consensus theory.
- *Sharp entrywise spectral-window envelopes and the exact eventual-positivity horizon* (2026), public record `2026/11/17/SCOPE-sharp-entrywise-spectral-window-envelopes-and-the-exact-eventual--aea2a1d10bf1` — related uniform spectral-window comparison; full source was unavailable in this review.

Self-review: passed. Independent audit: not yet performed.
