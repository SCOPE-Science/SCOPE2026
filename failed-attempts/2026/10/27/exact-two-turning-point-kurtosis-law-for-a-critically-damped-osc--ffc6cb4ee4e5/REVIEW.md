# Independent mathematical audit

## correctness

PASS

Two-sided reset Brownian walls have finite moments; stable convolution constructs the stationary state. Coupling at each wall's first reset and stability of the remaining homogeneous oscillator difference give uniqueness. Independently set y=x+u for a normalized single wall: x'=y-x and y'=z-y. For E[x^a y^b z^c], the triangular generator recursion has denominator a+b+r times the indicator of c>0 in the reset term, i.e. a+b+r·1_{c>0}; its numerator is a E[x^{a-1}y^{b+1}z^c]+b E[x^a y^{b-1}z^{c+1}]+c(c-1) E[x^a y^b z^{c-2}]. Expanding u=y-x reproduced both stationary moments, the two-wall excess (half the single-wall excess by cumulant additivity) and the derivative in RESULT.md. Exact P evaluations at 1/4, 2, 10 were 1490189781/262144, -3326712 and 87766512936; two Descartes variations give two simple roots and the stated sign sequence. Both numerical extrema and both limiting coefficients agree. Smoothness near damping 2 follows by local invertibility of the degree-two/four moment systems (and positivity of variance); the simple roots persist by the implicit function theorem. This is a mathematical check, not the frozen script's Monte Carlo or external/formal certification.

## originality

FAIL

A distinct indexed result gives the exact same function and turning-point structure under specialization and strictly strengthens the nearby-damping clause. This is verified existing coverage as of the audit, not a finding of earlier priority: the covering record is dated November 2 UTC, after this frozen record's October 27 UTC; the latter's date and evidence are preserved. The motivating 2023 article does not supply that coverage.

## value

PASS

The verified nonmonotonic fluctuation observable despite monotonically falling kinetic variance is a physically motivated structural phenomenon, and the critical case supplies precise benchmarks and a robustness result. This is an assessment of the scientific content rather than an assertion of independent added contribution after the broader indexed coverage; there is no demonstrated distinct valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
