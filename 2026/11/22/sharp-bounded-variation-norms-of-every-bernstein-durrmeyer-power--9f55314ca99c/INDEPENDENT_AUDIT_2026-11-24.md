# Independent mathematical audit

## correctness

PASS

For n≥1 the two end columns of the Bernstein basis have a strictly positive 2×2 minor at every ordered pair x₁<x₂, even at endpoints. All other such minors are nonnegative; the kernel minor expansion and the integral composition identity therefore give strict TP2 for every power. For t interior the rows are positive; K_n(0,1)=K_n(1,0)=0 at r=1, which does not affect the ratio or single-crossing arguments on the interior. Markov normalization gives ordered tails, and reflection puts the sole endpoint-row crossing at 1/2. This strictly maximizes jump variation there. Integration against |Df| bounds general BV data, and equality forces the derivative measure to be one midpoint atom. For oscillation, each ordered row pair has one crossing by TP2, so its probability TV distance is its maximum tail difference; stochastic ordering bounds that difference by the one for the endpoint pair. This is the step implicit in the proof's oscillation argument. Orthogonality, degree preservation and the beta-binomial leading coefficient give the stated Legendre eigenvalues. Subtracting endpoint rows and using the Legendre derivative identity leaves precisely the odd-mode differences at zero. The alternating magnitudes strictly decrease, giving the two-mode bounds, and the leading mode yields the fixed-n equivalent. Applying the r-power bound to the smooth strictly increasing s-power midpoint response makes submultiplicativity strict. Independent rational check: for n=3 the first-step Bernstein coefficients are (1,5,11,15)/16, and the second-step endpoint row difference is (−19,−6,6,19)/35 in that basis; their product gives 151/280, also found from the two spectral terms.

## originality

PASS

The one-step number and the spectral kernel are prior. The supported distinct result is the sharp TV and oscillation coefficient for every power together with midpoint rigidity and the strict variation decay law. The closest prior oscillation result explicitly stops at one step. The all-power Legendre expansion is strong input, but evaluating it at a midpoint step gives only a candidate without a sharp all-power optimizer argument.

## value

PASS

The all-power norm is a natural stability invariant of this classical smoothing operator. The coefficient and explicit leading correction quantify how much multiplying optimal one-step bounds misses, while midpoint rigidity explains why iteration never attains the product bound. The result gives exact finite-power information not furnished by generic convergence to constants or by the leading eigenvalue alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
