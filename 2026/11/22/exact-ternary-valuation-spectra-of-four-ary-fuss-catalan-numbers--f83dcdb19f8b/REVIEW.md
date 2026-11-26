# Independent mathematical audit

## correctness

PASS

Integrality follows from binom(4n,n)-3 binom(4n,n-1) with the out-of-range binomial zero. The denominator 3n+1 is a 3-adic unit, so Kummer gives the carries in n+3n. Lump states to s=previous digit plus incoming carry. Each digit a sends s to a+floor((s+a)/3) with weight t to that floor. Initial state is zero; only terminal state 3 has weight t for the extra high digit of 3n. Independent exact inversion of this four-state transfer verifies the stated numerator and denominator. Its first and second t-derivatives at t=1 agree identically with the generating series for the stated factorial moments, and normalization by 3^r gives the mean and variance (also at r=0,1). The first input digit cannot carry. Equality at r requires the first two digits to sum to at least three, all later neighboring pairs to sum to at least two, and last digit two, realized by all digits two for r>=2. Exact inversion of this separate adjacency count verifies the maximum multiplicity GF and recurrence. At t=1 the reachable transfer is primitive, with simple Perron eigenvalue 3 and remaining eigenvalues of modulus at most one. Its analytic perturbation gives a leading analytic exponential times an analytic nonzero amplitude, with exponentially small relative remainder uniformly near t=1. At t=exp(w), the log-eigenvalue has derivatives 1/2 and 2/3 from the moment slopes. Taylor expansion at imaginary w of order r^(-1/2) proves convergence of the normalized characteristic functions to the stated Gaussian. Independent direct integer histograms agree through r=6.

## originality

PASS

The strongest exact same-parameter precedent proves the valuation-zero census alone; the closest full spectra change the prime or the arity. The classical carry equivalence and known digit rules are not novel. The contribution supported by the comparisons is the complete evaluated ternary-block law for arity four, including its exact moments, Gaussian fluctuations and exact top stratum. General finite-state and congruence machinery are not themselves counted as new.

## value

PASS

The statistic counts prime divisibility of a standard family of tree enumeration integers; powers of three are the natural blocks for its digit structure. The full law gives frequency information about arbitrarily high divisibility, exact finite fluctuations and a nontrivial sharp maximum multiplicity, rather than only a divisibility predicate or a handful of test values. These quantities distinguish the four-ary sequence from its closest ternary-arity analogue.

The dated certificate retains the supplied scientific assessment, sources and limitations.
