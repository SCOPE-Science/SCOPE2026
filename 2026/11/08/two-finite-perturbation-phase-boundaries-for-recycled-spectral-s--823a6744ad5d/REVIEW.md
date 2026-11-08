# Scientific review

## Correctness

PASS. The model and transformation are explicit, with a complete SPD domain. Its spectrum consists exactly of the two simple eigenvalues of a coupled two-by-two block and a flat bulk value. A determinant sign test determines the sole possible eigenvalue collision. Strict monotonicity of the two-by-two condition number on either side of the diagonal balance, together with strict increase of the upper eigenvalue after collision, proves the global unique optimizer in both regimes. The minimal-polynomial argument proves the exact two-step classification; the singular limit proves the unbounded tradeoff. Exact-rational and floating-point checks were rerun from the standalone verifier. At the boundary both optimization formulas coincide.

## Originality

PASS on presently inspected evidence, with residual historical-priority uncertainty. The closest 2026 perturbation paper uses first-order and second-order error estimates for recycled eigenvector preconditioning, not the exact two-boundary finite-perturbation solution. The earlier 2026 cluster-placement paper treats a spectral source for the current matrix and iteration-budget-specific errors. Giraud–Gratton (2006) studies first-order preconditioner sensitivity. Braatz–Morari (1994) gives general convex optimization of matrix scaling but does not provide these explicit collision and two-step PCG boundaries. Search comparisons with published mathematical records and accessible historical claims found no implication that directly yields the entire stated result. Earlier special-purpose explicit scaling results may be unindexed.

## Value

PASS. A structural question in reused spectral information is whether the best condition-number tuning also restores a two-eigenvalue cluster, hence uniform two-step exact CG. The answer is a sharp two-threshold phase diagram, valid at finite rather than infinitesimal perturbation, with a quantitatively diverging price of insisting on the finite-step property. This supplies an exact benchmark for deciding which objective is relevant when recycling a spectral preconditioner. The model is special and the result is not a universal solver-rate theorem.

## Closest literature and limitations

Sources: arXiv:2610.28808; arXiv:2603.28969; DOI:10.1137/040617546; DOI:10.1137/S0363012992238680. This is a one-parameter, real SPD, isolated-pair/flat-bulk model; numerical precision and arbitrary couplings are not covered. Unindexed equivalences remain possible.

Self-review: passed. Independent audit: not yet performed.
