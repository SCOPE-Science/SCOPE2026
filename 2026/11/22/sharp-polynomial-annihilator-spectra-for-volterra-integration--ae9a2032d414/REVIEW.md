# Scientific review

## Correctness — PASS

The Legendre antiderivative recurrence gives the two-diagonal coefficient matrix with an exact rational Gram diagonal. Its telescoping trace proves the full Hilbert–Schmidt identity, not merely a finite truncation. The finite-window moment method establishes the continuous symbol law for a polynomial basis; Weierstrass approximation extends it to every fixed real Schatten exponent. Weighted-shift tail bounds, uniform in the moment cutoff, control passage from windows to the infinite operator. The same density estimate yields arbitrarily many top singular values near the sharp shift upper bound. A finite-rank comparison with the classical Volterra spectrum proves the fixed-cutoff Schatten threshold. The standalone checker independently recalculates 3,054 identities and finite witnesses, but does not certify the infinite argument.

## Originality — PASS, with residual priority risk

The exact Volterra singular-value sequence and Legendre polynomial antiderivative relation are prior background, not new claims. The inspected 2014 Legendre pseudospectral article concerns finite collocation and convergence for nonlinear Volterra systems. The 2018 Stenger integration-operator paper and 2019 Gutleb–Olver sparse spectral study concern finite computational representations. Generalized locally Toeplitz spectral distribution theory supplies a broad context for the *finite-window bulk symbol*, which is not claimed as a new abstract principle. The distinguishable combined contribution is the infinite-dimensional polynomial-moment annihilator \(T_m\), its exact entire Hilbert–Schmidt energy for every cutoff, all-real-exponent global Schatten-mass constants with a controlled infinite tail, and the no-outlier proof for each fixed top singular value. No equal or dominating statement was identified in the inspected material and checked research records, but an undiscovered specialization of older GLT or operator-approximation work remains possible. This is a self-review, not a proof of global historical uniqueness.

## Value — PASS

Moment annihilation is a natural preprocessing operation in spectral approximation and residual smoothing. The sharp \(1/(2m)\) operator attenuation, exact total-square energy, and full \(p>1\) Schatten-mass law give distinct, nontrivial quantitative information about how suppressing polynomial modes changes the entire integration spectrum. The fixed-index edge result in particular cannot follow merely from a finite-window empirical density without an outlier bound. No unspecified downstream theorem or numerical speedup is claimed.

## Limitations and source coverage

The result is restricted to the unweighted interval, orthogonal polynomial cutoff, and fixed \(p,k\). The 2003 general spectral-distribution framework is compared through its accessible abstract, not represented as fully inspected; the 1996 Volterra singular-value work was read at abstract level. Independently checking the historical literature and all infinite-dimensional arguments remains advisable.

Self-review: passed. Independent audit: not yet performed.
