# Independent mathematical audit

## correctness

PASS

The exact inverse-Gaussian conjugation of the Gaussian adjoint reduces singular values to symmetric tensor powers of e^{tB}; second quantization gives exp(pt tr B) product(1-sigma_i(t)^p)^-1. The dissipative Gramian W_t=I-e^{tB^T}e^{tB}=integral_0^t e^{sB^T}Qe^{sB} ds is strictly positive exactly for a full Kalman flag; a missing direction leaves tensor powers with singular value one, so no compactness. Orthogonal filtration projections have first coefficients s^k C_k, yielding D_t^-1 W_t D_t^-1 -> positive G, det W_t ~ det G t^K. Positivity follows from independent polynomial coefficients and full row ranks. Replacement 1-sigma^p ~ p(1-sigma^2)/2 yields the coefficient. Nonincreasing Kalman increments and delayed one-dimensional levels give sharp upper bound; explicit dissipative skew-chain B=J_m + scalar blocks gives extremal m=d-r+1, its signed Hilbert determinant gives factorial coefficient. Independently recomputed exact rank-one d=3 determinant(G)=1/1080 and S1 leading 8640; inspected source CHECK.py exact-rational checker through m=8 but did not treat it as a universal proof.

## originality

PASS

Best-knowledge PASS for exact all-dimension positive Kalman-graded singular-value product coefficient, sharp fixed-rank upper bound and extremal factorial family, NOT for general second quantization, Kalman controllability, or existing inverse OU spectral equivalence. Read relevant primary-article abstracts/available sections and compared published planar inverse OU work; the general 1995 Araki–Sinha–Sunder product theorem is an admitted premise. Full access to some historical primary text was limited, leaving explicit risk.

## value

PASS

The exponent K can jump from d to d^2 when diffusion loses directions, despite operator trace staying order t^-d; the exact graded coefficient and rank-sharp extremizer quantify a genuine nonnormal smoothing/singular-value phenomenon across all dimensions. This is motivated operator-theoretic information, not a one-off calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
