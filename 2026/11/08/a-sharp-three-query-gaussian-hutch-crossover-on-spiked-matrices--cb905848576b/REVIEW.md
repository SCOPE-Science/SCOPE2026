# Scientific review: Gaussian three-query trace-estimation crossover

## Correctness
**PASS.** The proof gives a conditional Gaussian fourth-moment reduction to \(\mathbb E\operatorname{tr}((PAP)^2)\), then a direct rank-one projector identity and an exact Gaussian/chi-square integral. The four-dimensional Beta integral yields rational moment formulas, and their variance difference has a polynomial with one positive root by Descartes' rule. The fixed-dimensional large-spike coefficient follows by a dominated integral and an explicit remainder bound, not from simulation. The accompanying checker independently confirms arithmetic, quadrature and implementation; finite samples are not used to prove a universal assertion.

## Originality
**PASS, qualified.** Original Hutch++ (Meyer et al., arXiv:2010.09649) and improved variants (Persson et al., arXiv:2109.10659) establish unbiased deflation, general variance-control frameworks, and qualitative spectral behavior, including adaptive budget allocation. The inspected primary sections, experiments and appendices do not state the exact rank-one-sketch one-spike variance integral, its sharp three-query Gaussian crossover in dimension four, or the all-fixed-dimension linear rare-sketch asymptotic coefficient. The general variance identity is prior work; the claim is the nontrivial evaluation and sharp comparison. Hidden specialist literature and closely related finite-dimensional formulas are residual risks. This is not evidence of global uniqueness.

## Value
**PASS.** At a fixed three-query budget, low-rank deflation spends two queries constructing a sketch, which can lose to ordinary quadratic probing on sufficiently flat spectra. The first nontrivial dimension \(d=4\) admits a complete, exact decision boundary. The all-fixed-dimension linear variance asymptotic reveals the price of rare missed-spike sketches and quantifies why deflation eventually dominates quadratic baseline variance despite that price. This is a reproducible algorithm-selection benchmark, not a universal recommendation for all trace estimators.

## Limits
The results use independent standard Gaussian vectors, exact arithmetic, a unit-multiplicity spike, fixed dimension in the asymptotic, and three queries. No superiority is claimed over Rademacher, adaptive, dimension-aware, or Nyström-based alternatives. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
