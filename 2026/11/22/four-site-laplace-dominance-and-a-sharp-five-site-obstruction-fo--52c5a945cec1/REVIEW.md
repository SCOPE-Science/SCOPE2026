# Scientific review: cyclic versus independent reset destinations

## Correctness — PASS

The attempted protocol is fully specified, including random initial cyclic phase and independently restarted Poisson clocks. The discounted single-attempt capture and interruption weights are derived from the exponential-clock integral. Summing discounted trajectories gives the exact block-product identity. The two/three/four-site inequalities follow from AM–GM, elementary symmetric means and the opposite-pair factorization; the periodic factorization extends them to all cycle lengths. The mean follows by dominated convergence at zero discount because the full-cycle failure product is less than one. The five-site reversal is an exact rational evaluation and is realized by finite Brownian reset distances. The general five-or-more obstruction follows by continuity and a small-discount-factor expansion. The independent rational checker is supplementary, not an infinite proof.

## Originality — PASS, with publication-priority limits

The close two-site paper by Julián-Salgado–Dagdug–Boyer (arXiv:2311.11897, Section III and setup) treats independently occurring reset-to-site events at two rates, not a random-phase deterministic cycle of modes. Méndez–Flaquer-Galmés–Campos (arXiv:2401.01125, Section II, equation (6), and conclusions) independently redraw reset positions from a density; no phase-correlated site order or sharp site-number boundary is provided. The exact assessed advance is the universal four-site transform comparison and sharp five-site failure; classical renewal transforms and inequalities are not presented as separately new. Search was also directed at cyclic permutations, periodic sites versus periodic clocks, aliases and the published-finding corpus records identified in AUDIT.json. A broader unpublished or unindexed correlated-scheduling result could imply this result; no claim of exhaustive priority is made.

## Mathematical value — PASS

The location schedule is an experimentally and algorithmically meaningful control dimension that is invisible to the independent-reset spatial marginal. The result finds a sharp, minimal obstruction: at most four modes, fair cyclic scheduling is universally favorable in Laplace order, whereas five modes can invert the comparison despite unchanged marginal use frequencies and identical clocks. It supplies a nontrivial boundary of a plausible comparison principle for spatial resetting, a complete small-mode classification with general counterexamples beyond the threshold, and a fully physical exact Brownian example. The five-mode bound is not an arbitrary numerical slice, and the distinction is not a routine restatement of first-passage renewal.

## Closest literature and limitations

- Julián-Salgado, Dagdug and Boyer, "Diffusion with two resetting points," arXiv:2311.11897 (2023-11-20).
- Méndez, Flaquer-Galmés and Campos, "First-passage time of a Brownian searcher with stochastic resetting to random positions," arXiv:2401.01125 (2024-01-02).

Only Laplace-transform dominance and a mean corollary are established, not pointwise first-passage survival order. The five-site witness reverses a Laplace comparison, not necessarily the mean. Other scheduling protocols are outside the theorem. Unindexed stronger coverage remains the principal originality risk.

Self-review: passed. Independent audit: not yet performed.
