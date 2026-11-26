# Independent mathematical audit

## correctness

PASS

Gram inversion gives the nonnegative hyperbolic cardinal coefficients inside the interval and one decaying coefficient outside. The inward derivative at the endpoint is +infinity, so both the exterior and the endpoints lose. With L(x)=log(cosh x)+(p−1)log(sinh x), the derivative of the objective has the sign of H(x)=L(x)−L(h−x). On the left half H is strictly convex because L'' is positive and strictly decreasing; H tends to +infinity at 0, vanishes at the midpoint, and has midpoint slope 2L'(h/2). This classifies all maximizers including at the zero-slope threshold. Strict decrease in h follows by evaluating at the larger-h maximizer with the relative offset fixed, since z coth z is strictly increasing. As h approaches the threshold from above, compactness and the threshold sign imply the off-center node converges to the midpoint (the near-zero divergence excludes an endpoint limit). Expanding the centered stationarity equation then gives delta²∼−6 L''(u0)(h/2−u0)/L'''(u0), with the derivatives in the source. At large h the left root tends to 0 by comparing L(x) with L(h−x) at every fixed positive x. The root equation gives x∼2^{p/(1−p)} exp(−ph/(1−p)); writing A,B for the small and large cardinal coefficients, it also gives A^p/B^p=tanh x/tanh(h−x)∼x while B^p=1−px+o(x), yielding the stated excess. At p=1/2 the unequal root is characterized by sinh x sinh(h−x)=1, which gives the offset and both agreeing branches. Coefficient p-subadditivity proves sufficiency of the factor, the maximizing single atom proves sharpness on interpolants, and the general representer-penalty criterion applies in this injective coefficient model. For necessity with finite continuous losses one can also enforce the atom's two target values with increasingly weighted squared loss, taking the finite-dimensional sample-span minimum to the interpolant penalty.

## originality

PASS

The factor definition, its exact representer interpretation, the Laplace two-site coefficients and the qualitative violation of a unit factor are known and credited. The inspected sources do not fix the sharp maximum as a function of separation and p, classify its maximizers, or supply the asymptotics and half-power expressions.

## value

PASS

This quantifies a known failure of the unit sample-span penalty by giving the exact multiplier, when the worst atom is no longer at the midpoint, and how fast amplification decays for well-separated sites. The bifurcation and sharp constants give a tunable quantitative benchmark for a standard kernel and sparse coefficient geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
