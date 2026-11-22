# Review of the two-line reciprocal metric-switching law

## Correctness

**PASS, self-review.** Orthogonal projection onto the two lines gives the explicit two-component update. Reciprocal symmetry makes the conditional second-moment matrix exactly scalar, and independence turns this one-step identity into an all-time identity. The factorization of the scalar growth rate establishes all strict and equality cases; Schur's quadratic criterion handles the separate deterministic comparator. The rational example distinguishes mean-square divergence from periodic linear convergence exactly. The packaged standard-library verifier passed 1481 exact-rational assertions. Numerical experiments and finite enumeration are not treated as proofs of the universal statement.

## Originality

**PASS, qualified.** The primary 2026 variable-metric splitting paper supplies the exact proximal update and controlled-metric convergence results, not an unrestricted iid metric theorem. The closely matching published two-period result already supplies the deterministic uniform threshold \(3+2\sqrt2\), which is expressly credited. It cannot alone imply the current exact iid second-moment identity and sharp \(2+\sqrt3\) threshold. Classical fixed-metric and nonstationary convergence results have different hypotheses. Searches of published mathematical results and the related literature identified no stronger covering exact iid claim. The full text of one relevant stochastic preconditioned splitting article was inaccessible, so historical priority is not established exhaustively.

## Value

**PASS.** The result pinpoints a sharp distinction among fixed, periodic and freshly randomized metric choices in a natural convex feasibility model and provides a complete distribution/angle safety test. The structural contrast matters when evaluating robustness of variable-metric proximal schemes. The result is limited to reciprocal distributions, two lines, and mean-square convergence; it does not contradict safeguarded schemes or establish almost-sure divergence.

## Closest literature and limitations

Suh and Isaac, *Variable Metric Three Operator Splitting*, arXiv:2610.38935v1; *Sharp two-period metric-ratio barrier for convex-subspace three-operator splitting*, published 2026-11-08 (public result linked in RESULT.md); Lorenz and Tran-Dinh, arXiv:1801.03765; Bauschke and coauthors, arXiv:1309.4709; Dong, Bredies and Sun, arXiv:2212.13001 (abstract only). Important unresolved risk: the last paper's full text could not be inspected. The necessary-and-sufficient mean-square threshold does not classify pathwise behavior in the divergent regime.

Self-review: passed. Independent audit: not yet performed.
