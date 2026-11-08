# Self-review

## Correctness (PASS)

The center-to-target Laplace transform follows by solving the backward equation separately on the absorbing arm and reflecting arms and enforcing Kirchhoff derivative balance. Substitution in the standard Poisson restart renewal identity gives the exact absorption mean. The small-rate coefficient shows why one arm cannot benefit while every added reflecting dead end makes a positive rate beneficial. The identity \(H_m=F+G/(m-1/2)\), with \(G>0\), proves strict monotonicity of optimal fractional saving. A power series for the derivative of \(F\) gives one positive zero and therefore a unique limiting optimum. The script separately checks the boundary problem numerically at 52 diagnostic points; the proof does not depend on these approximate tests.

## Originality (PASS; residual historical-priority risk)

The earliest underlying resetting paper by Evans and Majumdar (2011, arXiv:1102.2704) supplies the general renewal idea and a half-line calculation. Their broader 2011 study covers reset and target distributions. Riascos et al. (arXiv:1910.13568) derive spectral reset formulas on discrete graphs and analyze Cayley trees, but not this continuum Kirchhoff-star all-degree fractional-gain bound. The accessible primary Dassios–Zhang work (2021, DOI 10.1007/s11009-021-09884-4) calculates *unreset* Brownian first-hitting times with every outer tip a stopping boundary, which differs from the single absorbing tip and reflecting blind arms here. The examined primary literature and searches of published mathematical research records gave no identical statement; this does not rule out unpublished or unindexed precedents. The renewal identity and the generic observation that branching sometimes helps restarting are expressly not claimed as new.

## Mathematical value (PASS)

The result turns the branch count into a quantified search-design parameter. It proves a sharp first beneficial topology at two arms, strict improvement in the relative optimum with every added arm, and a sharp limiting bound of approximately \(14.474\%\) for an entire metric-star family. This structurally motivated threshold and asymptotic benchmark are more informative than an arbitrary numerical finite-graph example. The value is limited to the precisely specified Brownian/star reset model.

## Scientific limitations and literature risk

The model requires equal arm lengths, uniform diffusion, Kirchhoff junction matching, exactly one absorbing tip, all other tips reflecting, and instantaneous Poisson resets to the hub. Neither finite-degree optimizer uniqueness nor universality beyond this family is claimed. An unindexed exact calculation may already contain a special case; source comparison cannot establish absolute priority. Numerical diagnostics supplement rather than replace the proof.

Self-review: passed. Independent audit: not yet performed.
