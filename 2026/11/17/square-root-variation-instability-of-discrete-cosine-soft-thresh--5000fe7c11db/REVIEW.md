# Review of DCT-II soft-threshold variation instability

## Correctness — PASS

The exact claim is the realized spectral-mask formula and the two-sided bounds \(\tfrac12+(n-2)/(2\sqrt{3n})\le L_n\le\sqrt{n-1}\), for every \(n\ge2\), \(\lambda>0\). The four proof steps are: (i) continuous piecewise-affine global Lipschitz reduction, with all masks realizable on open cells; (ii) telescoping step decomposition; (iii) exact DCT-to-DST first-difference kernel identity and orthogonal column bound; (iv) random masks, a trigonometric fourth-order sum, and Rademacher moment interpolation. Explicit finite pairs attain each maximizing mask column. Checker success corroborates but is not the proof.

## Originality — PASS, with residual priority risk

Strang (1999) supplies DCT basis and eigenvector algebra without a DCT soft-threshold BV norm. Durand–Froment (2003) studies TV reconstruction after wavelet coefficient shrinkage, not two-input DCT-II path-variation gain. An analogous Haar soft-threshold analysis has logarithmic, not square-root, order and does not cover the DCT-II statement. Search comparisons included sine-basis projection norms, Fourier conditionality and DCT BV shrinkage aliases. The risk that a general, possibly unindexed trigonometric unconditionality theorem gives the same asymptotic order remains; no claim of independent historical priority is made.

## Mathematical value — PASS

The exact all-mask coefficient relates nonlinear spectral denoising directly to a classical sine-projection conditionality invariant, and the proved \(\Theta(\sqrt n)\) growth explains an unbounded edge-variation instability despite Euclidean nonexpansivity. It is a family-wide stability law, not a selected small-grid calculation.

## Limits

The leading constant is open here. The result does not generalize to other DCT types, hard thresholding, weighted graphs or higher-dimensional image BV. No external audit has been performed.

Self-review: passed. Independent audit: not yet performed.
