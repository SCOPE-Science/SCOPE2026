# Independent mathematical audit

## correctness

PASS

Under x=cos θ the measure is (2/π)sin²θ dθ and the second-kind basis is orthonormal by sine orthogonality. The real BV derivative measure represents the input modulo constants as a signed integral of unit jumps; Minkowski for the residual and equality at a maximizing jump reduce the norm to one scalar jump. The compact jump parameter has continuous residual, with zero at the endpoints and positive residual in the interior since a jump is not a polynomial almost everywhere. Direct integration gives p(θ) and the signed coefficients [sin(kθ)/k−sin((k+2)θ)/(k+2)]/π (the signed representative is used when differentiating their squares), with the stated full tail by Parseval. At π/2 reflection gives stationarity; differentiating the finite residual yields curvature coefficient 8[−1−floor(n/2)+Σ_{k odd≤n}(1+1/(k(k+2)))]. The sum of reciprocal products telescopes by 1/(k(k+2))=(1/k−1/(k+2))/2, verifying both exact signs and the degree-zero case. With N=n+2, square the leading tail coefficient −2 sinθ cos(mθ)/(πm); summability of the cross-error terms yields O(|cosθ|n^−2+n^−3) uniformly. The plain sum from N of m^−2 is n^−1−3/(2n²)+O(n^−3). Twice differencing the weights in the complex oscillatory sum gives its boundary term exp(2iNθ)/(N²(1−exp(2iθ))) with a uniform O(N^−3) error on compact interior arcs. On the endpoint arcs sin²θ≤1/4, the crude bound by the plain sum already keeps the leading residual below the centered residual. Uniform comparison on the remaining arc forces every maximizing angle to the midpoint. There the oscillatory term is at most (1+o(1))/(2n²) and the error from cosθ is o(n^−2). The even midpoint and odd angle π/2+π/(2N) align the leading phase and attain that upper expansion. At the midpoint without phase adjustment the boundary term carries (−1)^n, giving the exact parity-dependent second-order deficit. This proves the asymptotic norm, not a finite-cutoff optimizer classification.

## originality

PASS

Related results already give the BV unit-jump extremizer for a single orthogonal coefficient and weighted L² projection-error upper bounds or rates. The contribution is the sharp optimization of the entire squared tail for the semicircle probability weight, specifically its second term and exact midpoint-curvature parity. The relevant full-text comparisons distinguish those questions; the assessment is best-of-knowledge only.

## value

PASS

The norm is a natural worst-case L² approximation benchmark for variation-bounded data under a canonical weight. The exact second term resolves a measurable failure of the midpoint choice at every odd degree, despite all optimal jump positions approaching the midpoint. This identifies a parity effect not seen in the leading error rate, with an explicit phase-aligned witness; it does not claim global finite-degree uniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
