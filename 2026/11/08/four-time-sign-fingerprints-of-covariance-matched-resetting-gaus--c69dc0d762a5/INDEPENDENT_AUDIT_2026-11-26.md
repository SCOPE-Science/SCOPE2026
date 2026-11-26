# Independent mathematical audit

## correctness

PASS

An independent renewal/Wick reconstruction gives the claimed asymmetric earliest-gap term. Condition on the stationary Poisson reset history. The Brownian samples are then centered jointly Gaussian with conditional covariance Kij=2D Ai times the indicator of no reset from ti to tj for i≤j, where Ai is the backward age at ti. Its expectation is (2D/r)e^(−r(tj−ti)). Divide products of K by (2D/r)². For (12)(34), survival in the first and last gaps contributes e^(−r(u+w)); if the middle gap survives the age at t3 is A1+u+v, otherwise its truncated age has unnormalized mean [1−e^(−rv)(1+rv)]/r and is independent of A1. Using E[A1]=1/r and E[A1²]=2/r² gives the contribution e^(−r(u+w))[1+e^(−rv)(1+ru)]. Each other pairing requires survival across all gaps and contributes e^(−r(u+v+w))(2+ru). Subtracting the three products of unconditional covariances yields exactly the stated reset cumulant, whose bracket is ≥3. The OU cumulant is zero by Wick. The telegraph sign is Poisson at rate r/2, so its conditional mean decays at r and its square is 2D/r; its fourth moment is the uncrossed pairing alone and subtraction gives the stated two equal negative terms. These arguments include zero gaps; at full coincidence the reset and telegraph cumulants are 12D²/r² and −8D²/r². Stationarity gives a uniform fourth-moment bound so the L¹ filters exist in L⁴ and Hölder/Fubini justify integrating the cumulant. Sorting shifted times preserves the formula, and a positive-measure product support gives strict sign. This in fact only requires each nonnegative filter to be nonzero as an L¹ element. Identical filtering preserves the matching pair covariances, and an independent Gaussian vector adds no fourth cumulant. The source generator/matrix script and quadrature procedure were inspected, not run; their finite scope is not needed by the argument. In the prior-work paragraph the name attached to reference [2] should be Singh and Pal, as in the bibliography and paper, not Smith and Majumdar; this is a bibliographic error, not a mathematical change.

## originality

PASS

The supported distinct claim is the complete ordered stationary reset-Brownian connected four-time kernel and its role in the strict three-bath sign distinction under arbitrary nonnegative L¹ filters. The covariance matching was already explicit; Gaussian vanishing is standard, and the earlier cooperative-network result covers part of the negative telegraph comparison. Known one-time harmonic moments and related filtered fourth-order slices are not a complete unequal-time kernel. This is a best-of-knowledge judgment about the combined result, not separate novelty for the comparison cases or settled priority.

## value

PASS

Covariance matching makes every second-order comparison after the same linear probes inconclusive. A closed four-time kernel with uniform sign makes the fourth connected moment an exact discriminator among the three specified mechanisms at any probe times and under any nonzero nonnegative response filters, not just for one rate or at equal time. This is a useful structural result for reset-driven linear systems. It is not a claim of experimental detectability, statistical identification among all baths, or persistence for signed filters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
