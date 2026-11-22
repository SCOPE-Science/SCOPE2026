# Self-review

## Correctness — PASS

The domain, symmetry, and branch formulas were derived directly from the normalized max update. In odds variables the two branches are explicit: consecutive unmixed steps contract the odds ratio by a factor strictly below one, so they cannot persist forever; one mixed step enters the invariant rectangle \(D_\alpha\). The exact mixed map then enters the smaller invariant rectangle \(D_\alpha^{\rm s}\) where the weighted Jacobian norm is at most \(55/64<1\). Banach's theorem gives convergence of every off-diagonal orbit in the claimed regime. Positivity at the excluded endpoint and the max-selection tie have been handled. The verified symbolic identities and 700 rational/1500 floating trajectory tests supplement but do not replace the infinite proof.

## Originality — PASS with identified residual risk

The initiating article (Satur, arXiv:2611.13318v1, especially its attractor theorem, numerical section and conclusions) already supplies the exact map and asymmetric equilibrium and proves local stability. It explicitly describes global attractivity as numerically supported, rather than proved. This theorem establishes that missing global conclusion for the nontrivial full interval \(\alpha\ge4\), including a new absorbing-region mechanism and uniform convergence estimate. Published-result title/claim and parameter-equivalence searches found related, mathematically distinct replicator, lottery-contest and generic max-difference systems but no established normalized-maxima contraction theorem with the same domain. A general 2003 max-equation source could only be examined by publicly available abstract; an unindexed or terminologically different equivalent remains possible. Absence from search is not itself evidence of uniqueness.

## Mathematical value — PASS

A global attraction question left to experiments by the motivating research receives a rigorous solution for an entire unbounded parameter range and every strictly off-diagonal initial condition. The proof builds a natural finite-time trapping mechanism, resolves a priori branch switching, and yields an explicit uniform rate after absorption. This is a global basin result, not a restatement of local linear stability. The sufficient cutoff is not claimed sharp; the complementary resource range remains open.

## Sources and boundaries

- O. R. Satur, *From oscillations to symmetry breaking in a two-dimensional piecewise-smooth dynamical system*, arXiv:2611.13318v1, submitted 9 November 2026; full text checked for model, order preservation, fixed points, locally proved assertions, numerical global evidence and conclusions.
- G. Papaschinopoulos, C. J. Schinas, V. Hatzifilippidis (2003), DOI 10.1023/A:1022833112788; abstract available, full text not obtained, residual priority risk.
- The provided exact-rational and symbolic checks are limited test cases. No higher-precision computer-assisted or formal proof certificate is asserted.

Self-review: passed. Independent audit: not yet performed.
