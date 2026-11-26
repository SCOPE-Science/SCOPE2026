# Independent mathematical audit

## correctness

PASS

For a in (1/2,1), the future discount is asymptotic to (n/m)^a with uniform multiplicative error from summable logarithmic remainders. The discounted martingale's conditional variance is R^2(1-a^2 S_m^2/m^2); the second-moment recursion gives O(n) on bounded future time intervals for x=O(sqrt(n)), so the cumulative variance correction on the scaled clock vanishes. Discounted jumps satisfy Lindeberg. After subtracting the deterministic discounted target, a signed crossing is an exact lattice hit because the undiscounted integer difference changes by ±1. Brownian extrema are atomless by Cameron–Martin and reflection; at initial equality the Brownian path visits both sides immediately. The late-hit bound follows by splitting at m_T between an endpoint within η+|c|(1+T)^(-a) of zero on the scaled clock (Gaussian density bound) and a later martingale increment of magnitude η (Doob inequality and O((1+T)^(-δ)) tail variance). A possible hit only at the clock endpoint has probability zero. The global maximal Azuma envelope controls remote starting sites. The cited local limit factor 2 cancels the mesh 2/sqrt(n), giving exactly f_a(0) times the integrated hitting profile; inserting a bounded continuous test function proves the conditional law. The range identity follows by Tonelli on the continuous path image. Pathwise convexity and a Brownian small-ball event give a strict minimum at zero and hence strict increase on the positive half-line; reflection, Jensen and the oscillation triangle inequality give the constants and bounds. The conclusion includes q=0,1 and arbitrary lower-order lattice rounding.

## originality

PASS

The leading coefficient for c=0 overlaps Trinas's last-return result and is not new. The supported distinct claim is the nonzero square-root singleton displacement, its conditional starting-position profile, and the geometry of its Brownian range. The closest centered-interval and subcritical-target statements do not include that geometry or the nonzero displacement.

## value

PASS

Critical displacement is the first scale at which the target location enters the future diffusive fluctuation kernel. The result determines both the rare-event coefficient and the position profile of walks contributing to it, and distinguishes displacement from widening an interval (slopes 1 and 2). This is structural information not available from the known last-zero coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
