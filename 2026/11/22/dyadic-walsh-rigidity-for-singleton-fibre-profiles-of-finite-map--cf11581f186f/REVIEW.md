# Scientific review

## Correctness — PASS

The only nontrivial counting identity is exact inclusion–exclusion on selected singleton fibres; the number of maps with each of \(j\) prescribed fibres singleton is \((n)_j(n-j)^{n-j}\). In the even-order valuation proof, the \(j=1\) term has valuation \(1+\nu_2(n)+\nu_2(k)\); both the \(j=0\) term and every \(j\ge2\) term have strictly higher valuation, including the endpoint \(j=n\) under the \(0^0=1\) convention. For odd orders the constant term is odd and all remaining terms are even. The two singular eigenvalues at order two and the determinant formula follow from explicit frequency multiplicities. Independently enumerated exact maps and a separate generating-function method agree with the theorem in their stated finite ranges. Computations do not prove the infinite statement.

## Originality — PASS (bounded comparison)

The 2004 full-text study by Milenkovic–Compton provides general occupancy transforms and de-Poissonization, not signed finite-cube frequency valuations. Riedel's 2015 bivariate singleton-count generating function subsumes the raw unsigned occupancy enumeration and makes the characteristic generating-function formula accessible by substitution; it does not state nor directly provide the exact dyadic order of each of the \(n+1\) Fourier bands. Barbour–Gnedin's small-count asymptotic work likewise uses occupancy statistics but does not yield this finite exact classification. Related spectral analyses of vacant-image profiles concern a different event (zero rather than one occupant) with different coefficients, dyadic valuations and order-two nullity. Public index searches for singleton occupancy Walsh transforms, 2-adic valuations and equivalent binomial sums found no claimed equivalent theorem; this is a bounded priority judgment, not a uniqueness certificate. Risk: unindexed arithmetic variants of occupancy generating functions may already contain the exact valuation statement.

## Value — PASS

Singleton urns are the first occupied-cell frequency class in classical balls-into-boxes and a natural genuinely dependent occupancy vector. The exact full-dimensional binary Fourier recovery classification is not a restatement of the marginal occupancy-count distribution: it distinguishes each character band and exposes a singular order with two lost modes. The all-dimensional valuation formula is a structural arithmetic spectral law, yielding determinant exponents and complete dyadic multiplicities without numerical extrapolation. The precise spectrum is relevant to injectivity of convolution by the empirical-counting kernel over characteristic zero and to the arithmetic denominator structure of its matrix. No sharp real condition estimate or downstream theorem is claimed.

## Closest sources and limits

O. Milenkovic and K. J. Compton (2004), DOI 10.1017/S0963548304006285; M. Riedel (2015), https://math.stackexchange.com/questions/801454/probability-of-k-boxes-contain-exactly-1-ball/1379701; A. D. Barbour and A. V. Gnedin (2008), arXiv:0809.4387. The first two provide the main broad counting framework and constitute the closest possible implication checks. The code covers finite orders; the proof covers every positive order. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
