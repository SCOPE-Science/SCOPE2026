# Independent mathematical audit

## correctness

PASS

Normalize the two Jordan parts of the circular derivative by V/2, and pair them to express the function modulo constants as a probability average of oriented arc indicators times V/2. Equality can be checked by the Hilbert-space variance identity: the residuals must all equal one maximizing residual. The multiplier 1−sinc²(πka) is nonzero for k≠0, so equality of residuals identifies the arc modulo constants. For the arc energy F(L), expansion of (I−T_a)^2 gives F(L)=L+2∫₀ᴸ(L−x)(K_a*K_a−2K_a)(x)dx, using circular kernels. The unwrapped four-box spline gives F(az)=aΦ(z) for z≤1; no translate contributes even at a=1/3 and z=1. The quartic is strictly convex with opposite endpoint signs and has exactly one root on (0,1). Beyond a, F''≥0 all the way to 1/2 even with wrapping, so F'≤0 by symmetry. The strict decrease from ar to a rules out every other length except the complementary one. For a≤1/4 integration of the outer spline gives the a/5 plateau; V=2 for a unit arc gives the claimed squared-norm factor 1/4. Exact independent spline-integral, root-enclosure and plateau checks passed; replay from /workspace with python3 -I -B branches/frozen_review_checks.py.

## originality

PASS

The supported distinct contribution is the exact centered triangular-convolution norm throughout 0<a≤1/3 and its rigid pulse equality class. The general BV reduction and the phenomenon of interacting jump layers in other smoothers are not independently new claims. The closest available statements have different operators or conclusion strength; the comparison is provisional where only indexed summaries or frozen source inspections were available.

## value

PASS

Twice-centered moving averages are a natural smoothing operation for periodic jump data. The separation between the worst short pulse and a pair of isolated jumps is structural: the exact squared residual is about 23.17% larger than the separated plateau where that plateau exists. The complete extremizer geometry and endpoint-valid bandwidth law give a sharp benchmark not supplied by a convergence rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
