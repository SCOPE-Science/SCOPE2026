# Review of sharp doubled-window extrapolation for symmetric three-frequency Fourier sums

## Correctness — PASS

The exact evaluation norm follows from the Gram matrix of \(1\), \(\cos(\omega t)\), and \(\sin(\omega t)\), with positive minors ensured by linear independence. The only nonstandard global step is positivity of \(F(u)\) for every \(u>0\). For \(0<u\le9\), `CHECK.py` proves a strict lower bound via 603 exactly rational Bernstein coefficients, an analytic Cauchy coefficient majorant, and an integer inequality for the remainder. For \(\omega\ge3\), Gershgorin gives the stronger squared evaluation bound \(9\). Legendre kernel convergence proves the optimal factor \(657/4\) and nonattainment. The embedded checker passed as executed; its finite exact computations and the stated analytic bounds jointly establish the infinite claim, not numerical tests alone.

## Originality — PASS relative to checked sources

Ruizhe Zhang, arXiv:2607.10501 (first posted July 11, 2026), proves frequency-independent exponential-in-sparsity extrapolation bounds and describes exterior leverage, but no exact \(657/4\) three-tone result at \(x=2\). The published symmetric three-tone Nikolskii result proves its sharp bound only at \(x=1\). Its general reproducing-kernel identity does not establish the strict all-gap exterior positivity required here. The published two-frequency exterior result has a smaller dimension and does not control three tones. The published three-tone interior-frequency transition treats \(|x|\le1\), not the exterior point \(2\). Searches for equivalent statements, the coefficient, doubled-window sharp leverage, and Legendre collision limits identified no dominating published comparison. Search absence is not proof of worldwide novelty.

## Value — PASS

At \(x=2\), the prediction location is the far boundary of the immediately adjacent extrapolation window \([1,2]\) singled out by current sparse-Fourier extrapolation research. It is a natural sharp testing benchmark for a minimally nontrivial three-frequency cluster, not an arbitrary combinatorial slice. The result specifies an exact frequency-uniform constant and a strict finite-gap deficit, separating actual oscillatory clusters from the polynomial collision limit. Its proof illustrates how exact rational positivity can settle a global oscillatory extremal inequality. It does not supply the complete exterior leverage profile or a sharp theorem for all three-frequency supports.

## Closest source comparisons and limitations

- Zhang, *Optimal Extrapolation Bounds for Sparse Fourier Sums*, https://arxiv.org/abs/2607.10501: broad sharp growth scale, not sharp coefficient here.
- *Sharp endpoint Nikolskii constant for symmetric three-tone Fourier sums*, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-endpoint-nikolskii-constant-for-symmetric-three-tone-fouri--e11889d28f9d: exact endpoint \(x=1\), not \(x=2\).
- *An interior frequency-splitting transition for three-tone Fourier leverage*, https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-an-interior-frequency-splitting-transition-for-three-tone-fourie--4a3bedbd64a2: local behavior at \(|x|\le1\), not global exterior rigidity.
- *Sharp two-frequency exterior Fourier leverage and the quadratic collision defect*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-two-frequency-exterior-fourier-leverage-and-the-quadratic--517d41b07a68: two frequencies, not three.

The exact finite certificate requires its supplied Python standard-library source. Independent validation and an exhaustive historical literature survey are not claimed; an unindexed equivalent specialized result remains possible.

Self-review: passed. Independent audit: not yet performed.
