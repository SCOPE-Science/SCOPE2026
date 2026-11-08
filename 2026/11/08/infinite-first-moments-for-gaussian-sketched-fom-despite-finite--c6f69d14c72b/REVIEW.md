# Scientific assessment

## Correctness — PASS

The claim follows from two distinct exact Gaussian regressions. For FOM, \(Sb\) and the sketch of its orthogonal complement are independent standard Gaussian vectors, giving reciprocal coefficient \(\alpha+\beta Z/R\) with \(R\) chi distributed; the resulting density is strictly positive at zero. The reciprocal therefore has a sharp \(t^{-1}\) tail, yielding the exact \(p<1\) moment cutoff. For GMRES, regression of \(Sb\) on \(SAb\) instead produces an ordinary affine Student law and the \(p<s\) cutoff. Completing the square in the true residual and using the inverse chi-square mean gives the exact finite-variance formula for \(s>2\). All parameters and boundary cases, including \(\beta>0\), integer \(s\ge2\), and almost-sure denominator nonvanishing, are included. The attached numerical checker validates examples and formulas, not the infinite-tail proof.

## Originality — PASS, with residual precedence risk

Güttel–Schweitzer (arXiv:2208.11447) explicitly derive sketched FOM/GMRES and recognize potentially negative projected eigenvalues and large FOM errors. Timsit–Grigori–Balabanov (arXiv:2302.07466) give high-probability quasi-optimality and report severe spikes caused by small Ritz outliers. Burke–Güttel–Soodhalter (arXiv:2311.14206) prove the sketched GMRES/FOM projection relationship. Direct reading of these primary articles did not identify a statement of the exact one-step Gaussian inverse-coefficient Student law together with its sharp unconditional moment threshold, negative-Ritz probability, tail coefficient and matching GMRES contrast. Those papers' qualitative findings are prior work rather than new claims. Routine regression/Student facts and potential unindexed randomized-Galerkin moment literature remain residual precedence risks; no global novelty certification is asserted.

## Value — PASS

The result gives a mathematically sharp distinction missed by checking only near-isometry probability or typical simulation errors: for every finite oversampling size, raw sketched FOM has infinite first absolute error moment on every SPD system whose first Krylov step is nontrivial, whereas the same one-step trial space has a finite-variance sketched minimum-residual approximation for three or more Gaussian rows. It quantifies both the failure probability and the exact residual cost of the more stable alternative. This is a motivated risk criterion for randomized Krylov solvers, not a routine table entry or a universal solver performance ranking.

## Closest literature and limitations

The qualitative FOM instability is already visible in Güttel–Schweitzer section 2.3 and the ROPM experiments of Timsit–Grigori–Balabanov. Generalized Gaussian linear-regression ratios already have Student laws. The novel assertion is confined to an exact solver-distribution/moment classification; equivalent older specialist derivations may exist. One-step SPD, i.i.d. Gaussian sketches and unregularized exact arithmetic are essential to the present theorem. Independent assessment remains to be performed.

Self-review: passed. Independent audit: not yet performed.
