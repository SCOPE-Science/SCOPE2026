# Independent mathematical audit

## correctness

PASS

Independently reconstructed the asymptotics in RESULT.md, lines 64–111. Strict positivity keeps the polar factor equal to U; the defect evolves by the binomial average of U^{-t}AU^t. On each column-indexed diagonal the Fourier multiplier is the finite sum of a_h(j) exp(-ijt). Its first surviving Taylor term is (-it)^r M_{r,h}/r!, giving (-1)^r times the Gaussian derivative at x=(n+kq)/sigma, hence the stated Hermite sign. Selfadjointness gives M_{r,-h}=conj(M_{r,h}) by a shift of origin that changes only vanishing lower moments. The contour shift is justified by entire periodicity: for shift iy with |y|=1/sigma, the binomial factor normalized at t=0 on the shifted line is a Bernoulli characteristic function with tilted parameter qe^{-y}/(1-q+qe^{-y}), uniformly interior. The zero-frequency mass and phase give exp(-(n+kq)y+O(1)), so integration with the order-r zero yields a summable exponential envelope. On a fixed rescaled window, cutting into growing o(sigma)-length blocks deletes O(sigma/block_length) rows near boundaries; freezing the coefficients changes each entry uniformly by o(1). Closed band walks give the normalized Toeplitz moments, and polynomial approximation on the bounded spectra gives all fixed-p absolute moments on the window. Outside it, summing diagonal p-powers and using the finite-band Schatten inequality gives a vanishing normalized tail for every p>0 (p-subadditivity for p<=1, the norm triangle inequality for p>=1). Signed tests follow from closed walks and polynomial approximation of F(t)/t^2 with the uniform normalized second-moment bound. A squared partition of unity gives an O(block_length^{-2}) band commutator error; the localized constant Laurent norm bounds the limsup, and an interior plane-wave packet gives the reverse bound. The resulting positive Schatten constants yield all three regimes at p=1/(r+1). Independently checked the exact example via sum p_k^2 = binom(2k,k)/4^k and sum p_k(j)p_k(j+1) = binom(2k,k-1)/4^k. These give the identity for all k, including k=0.

## originality

PASS

The surviving contribution is the explicit moment-selected Hermite–Fourier law and its global fixed-p and sharp norm consequences in this operator orbit, not the iteration identity, general Szegő/GLT theory, or Gaussian inversion. No inspected distinct claim implied that full specialized result.

## value

PASS

Sharp asymptotics distinguish operator-norm stability from decay in stronger ideals. One moment index predicts the exact critical Schatten exponent, while the band symbol retains off-diagonal geometry and eigenvalue signs that neither a norm bound nor a scalar shift example captures. These are useful invariants of a standard transform's perturbation orbit, not a numerical recount of the exact iteration formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
