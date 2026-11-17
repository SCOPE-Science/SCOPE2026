# Independent mathematical audit

## correctness

PASS

The assigned proof directly computes Fourier window response i a ω/(a+iω)^2 and squared modulus (1/4)sech²(log|ω/a|). Plancherel gives the periodized positive frame multiplier P_h(t)+P_h(t-θh). Its strict centered periodic unimodality follows analytically from the Jacobi dn² Fourier identity (DLMF 22.11.13), not a numerical grid. For θ=1/2, two banks form the h/2 lattice; evaluating at the longer-gap midpoint and grid center proves every other θ has a smaller sharp lower bound and larger sharp upper bound. Nearest sech tails and the first Poisson Fourier coefficient yield the stated sparse/dense asymptotic constants. Independent mpmath verified Poisson-vs-direct sums for three scales; full parameter theorem is analytic.

## originality

PASS

The exact simultaneous two-bank offset maximization/minimization and explicit frame bounds for causal exponential derivatives are distinct from finite DoE and DoT filter-bank reconstructions. Classical equally-spaced polarization theorems assume convex distance kernels, violated by the periodized sech² peak, and only compare the minimum, not the maximum. Historical priority qualified by missing closest full primary paper.

## value

PASS

A sharp robust filter-design theorem: one unique half-logstep stagger simultaneously improves worst and best continuum frame bounds at all ratios, with exact sparse/dense deterioration. That structural optimizer classification matters beyond computing one special-function sum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
