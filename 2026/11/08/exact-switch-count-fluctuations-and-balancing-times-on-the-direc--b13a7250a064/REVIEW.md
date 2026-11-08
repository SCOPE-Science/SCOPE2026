# Scientific review

## Correctness
**PASS.** For the directed triangle, the Osborne row/column balance update is exactly the averaging of two logarithmic edge weights. Its restriction to the zero-sum plane is one of three one-dimensional orthogonal projections, with pairwise absolute cosines \(1/2\). Uniform iid coordinate choices imply independent Bernoulli\((2/3)\) switch indicators, giving all finite-time norms and geometric waiting times. A deterministic two-sided comparison of the original \(\ell_1\) residual with log-error norm, uniform over the six post-first rays, transfers the negative-binomial central limit theorem. The first-step exceptional set is stated explicitly. The exact-rational verifier checks 10,005 finite identities/relations; infinite assertions follow from the written argument.

## Originality
**PASS, qualified.** Altschuler--Parrilo (arXiv:2004.02837, inspected full accessible article) covers the randomized Osborne procedure and general complexity, but does not provide this three-cycle exact finite error distribution or \(\ell_1\) stopping-time CLT. Boyd et al. (2006, inspected PDF) analyze spectral-gap-controlled gossip convergence, rather than the complete pathwise switch law. Shi et al. (arXiv:1206.0992, inspected PDF) address deterministic finite-time consensus, not tolerance fluctuations. Movassagh--Szegedy--Wang (arXiv:2205.04535, inspected full text) analyze expected averaging convergence and graph families without a corresponding negative-binomial triangle stopping formula. Equivalent formulations under edge gossip and conditional renewal are explicitly considered; no exact stronger published claim was located. Residual risk: an older specialized small-graph averaging calculation could already contain the law, and the derivation is elementary once the projection geometry is recognized.

## Value
**PASS, with narrow scope.** The directed triangle is the smallest strongly connected directed cycle for which Osborne row/column balancing cannot be characterized solely by a two-edge one-step reset. An exact complete finite-time distribution and a sharp confidence-calibration CLT for the very \(\ell_1\) error criterion used by the motivating matrix-balancing paper provide a concrete benchmark beyond generic worst-case complexity bounds. The result quantifies the genuine gap between average-square and typical convergence and identifies the exceptional input set. This is not an arbitrary parameter slice or a claim of a general faster algorithm.

## Limits
Only iid uniform coordinate choices and strictly positive directed-triangle edge weights are covered; nonlinear \(\ell_1\) residual results assume no one-step exact balance. General gossip mixing theorems may allow alternative derivations, and a specialist precedence search remains advisable. Independent external scientific review has not been performed.

Self-review: passed. Independent audit: not yet performed.
