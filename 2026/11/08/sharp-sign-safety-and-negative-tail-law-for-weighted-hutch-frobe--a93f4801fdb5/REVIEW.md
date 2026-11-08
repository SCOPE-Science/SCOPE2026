# Scientific review

## Correctness — PASS
For any nonzero real matrix and positive mixture weight, an explicit singular-direction sketch yields a strictly negative estimator, and Gaussian full support makes this event positive probability. Rank-one sketches reduce exactly to independent scaled chi-square variables. The exact tail integral follows by conditioning. The rate minimum is unique in sum/difference coordinates, and a two-variable boundary Laplace calculation gives the \(r^{-1/2}\) prefactor; a uniform variant handles the variance-optimal weight. Exact-rational, randomized-algebra, quadrature and Bessel-function tests in `verify.py` all passed (`VERIFY_OK 35456 checks`). Limits: this proof requires real Gaussian sketches and the rank-one asymptotic excludes higher ranks.

## Originality — PASS, with documented priority risk
The primary 2026 Hutch# paper was examined in its publicly accessible full HTML text (introduction, method definition, Sections 2–5 and Appendix A). Its exact variance formula, oracle mixture optimizer, and mean-square error guarantee are acknowledged as prior results; the new claim is about sign safety and **sharp one-sided negative-output probability**. Neither those source results nor the inspected Hutch++ baseline imply the all-matrix sign classification or the explicit rank-one sharp prefactor. Targeted literature and semantic mathematical-record searches for Hutch# negativity, chi-square-product equivalents, weighted-mixture safety, and rare-event limits yielded no matching result. The original general product-gamma probability literature is not exhaustively indexed, and the accessible Hutch++ baseline was primarily abstract-level; historical priority is consequently not independently established. A lack of search hits is not treated as uniqueness proof.

## Value — PASS
The object is a numerical estimator of a squared norm, for which sign admissibility is an intrinsic reliability requirement. The result distinguishes unconditional sign safety from improved variance, gives an exact failure probability rather than merely an illustrative negative sample, and quantifies the rare-event effect of the source paper's variance-optimal weight by a nontrivial limiting factor \(e^{-2}\). This is relevant to interpreting or guarding nonadaptive matrix-free norm outputs. It does not claim that negative values are common, nor that sign clipping preserves unbiasedness.

## Scientific limitations
The sharp probability law is established for rank-one real matrices and deterministic weights; the all-matrix conclusion is only the qualitative sign-safety boundary. The distinct full-rank negative-tail law remains open here. No independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
