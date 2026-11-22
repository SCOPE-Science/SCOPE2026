# Scientific review: twice-centred Steklov smoothing

## Correctness — PASS

The claim is a sharp, all-bandwidth statement on \(0<a\le1/3\) for real periodic \(BV\), not a finite enumeration. A signed-derivative coupling expresses each \(BV\) input modulo constants as a mean of oriented arc indicators; the Hilbert triangle inequality reduces the norm to an exact arc residual, and strict equality plus nonzero Fourier multipliers gives the full equality classification. Fourier differentiation identifies \(F_a''=2(K_a*K_a-2K_a)\) away from zero, and the fourfold-box convolution gives a polynomial on \(0<L<a\). Its integrated derivative \(p\) has one root in \((0,1)\) by strict convexity and endpoint signs. On \(a\le L\le1/2\), positivity of the fourfold convolution forces \(F_a''\ge0\), while reflection forces \(F_a'(1/2)=0\), excluding all additional maxima including wrapping regimes. The exact constant follows from \(V(\mathbf1_I)=2\). Explicit rational checks and a bounded Fourier tail verify the algebra without purporting to certify all arcs computationally.

## Originality — PASS, with explicit residual risk

Compared at the statement/implication level: Costarelli–Vinti (2014, https://doi.org/10.1216/JIE-2014-26-4-455, accessible complete article including its B-spline kernel section) proves rates for discrete sampling-Kantorovich operators on Lipschitz and Orlicz classes; the input class, operator and target sharp constant all differ. Mejía–Silvestre (2015, https://doi.org/10.1155/2015/253636, open full-text rendering with equations partially degraded) uses iterated forward Steklov means in higher \(p\)-variation/modulus inequalities but does not provide the centred residual \(BV\)-to-\(L^2\) norm or maximizing pulse. The later full Angeloni–Vinti et al. (2023, https://doi.org/10.1515/math-2022-0573) studies convergence in variation of sampling-Kantorovich schemes, not sharp smoothing residuals. Separate related work on one-sided boxcars and Poisson mixtures has different spectral multipliers and optimized arc geometry; neither dominates this result. Searches for triangular and fourfold B-spline sharp circle \(BV\) errors found no equivalent, but search incompleteness and an unindexed historical equivalent are remaining risks. No literature-wide uniqueness is claimed.

## Value — PASS

A twice-applied positive moving average is a standard smoothing operation, and exact worst-case variation-normalized \(L^2\) error matters when signals contain jumps. The theorem supplies a complete sharp constant and **all** extremizers over a nontrivial continuum of bandwidths. The worst pulse is only \(0.6111143254\ldots\) times the averaging width: its two error layers reinforce, increasing squared residual by roughly \(23.17\%\) over widely separated jumps in the nonwrapping range. This is a structural distinction from isolated-jump or semicircle heuristics, not merely a substituted parameter or computed table entry.

## Limitations and follow-up risk

The proof relies on the small-support geometry \(a\le1/3\); the full larger-width phase diagram remains unproved. No signed kernels, other \(L^p\) metrics or forward-shifted error norm are covered. Historical priority is qualified because indexing cannot exclude equivalent formulations in older smoothing-inequality literature.

Self-review: passed. Independent audit: not yet performed.
