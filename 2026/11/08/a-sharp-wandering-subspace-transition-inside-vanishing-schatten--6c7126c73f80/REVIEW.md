# Scientific review: sharp Schatten-local Wold transition for rootless-tree weighted shifts

## Correctness — PASS
The construction is a bounded positive left-invertible shift on a rootless, leafless quasi-Brownian tree. Its outgoing column norm is exactly one on the positive spine and at least one elsewhere, so expansivity is proven without extrapolating from finite sections. The Chavan–Trivedi analytic-series criterion applies: the original ancestor path ratio is \(g_m/N\), and the Cauchy-dual ratio is \(1/(Ng_m)\), with \(g_m=(1+m/N)^\beta\) for \(m\geq2\). The first series always diverges; the dual diverges exactly for \(\beta\leq1\). This yields analytic shifts with and without wandering-subspace generation at a sharp parameter transition.

The perturbation columns have pairwise disjoint support, making their norms *exact* singular values. Two spine sums enforce \(p>2\); the tooth sum is of lower asymptotic order, giving the coefficient \(4/(p-2)\) and operator-norm decay. The standalone checker passed 17,129 finite tests; it supports algebraic consistency but does not substitute for the infinite-dimensional analysis.

## Originality — PASS (qualified)
Chavan–Trivedi, arXiv:2501.01296, already characterize Wold decompositions for rootless positive weighted shifts and give expansive analytic failures. Kujur, arXiv:2609.14662, extends related examples to higher-order concavity and strict \(4\)-isometries on the same type of tree. Neither inspected full-text result states or implies the construction's arbitrarily small Schatten perturbations of a *fixed* isometry, nor its sharp \(\beta=1\) transition together with the exact perturbation exponent and asymptotic constant. Bala–Golla, arXiv:2607.15222, independently characterize membership in Schatten-perturbation classes but do not study the wandering-subspace property. Searches of relevant primary literature and published claims found no implication covering the combined theorem. An unlocated general compact-perturbation result phrased in different language remains a publication-priority risk; negative search is not independent certification of novelty.

## Mathematical value — PASS
The bounded perturbation theory of isometries and the Wold decomposition are classical, natural invariants. The theorem shows a genuine **instability** of wandering-subspace generation in every Schatten topology above a sharp threshold, with both sides analytic and expansive on the same tree. The quantitative constant and the crossing at \(\beta=1\) distinguish qualitative counterexamples from an explicit, parameter-controlled local classification. No downstream theorem is presumed. The threshold \(p>2\) belongs to the specific family, not all isometries or trees.

## Closest literature and limitations
The principal tool is the published Chavan–Trivedi rootless-tree criterion, not an original result here. The closer recent counterexamples of Kujur use the same tree geometry but address higher-order concavity, not small Schatten perturbations. The source of the Schatten perturbation criterion for general partial isometries is Bala–Golla. The construction uses a particular unbounded-depth comb and does not claim global classification of weighted shifts. Possible broader implicit coverage remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
