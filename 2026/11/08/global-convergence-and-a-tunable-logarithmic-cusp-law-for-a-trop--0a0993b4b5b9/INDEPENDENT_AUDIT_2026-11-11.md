# Independent mathematical audit

## correctness

PASS

For every positive r,k,tau the derivative of T_tau(x) is strictly positive, since H-xH'=2x^3/(1+x²)^2>0. The first step fixes direction of all later steps; iterates remain bounded, and repulsion from zero proves convergence to a positive fixed point with correct nearest-equilibrium selector even if multiple fixed points exist. The tau=infinity map remains positive, bounded and increasing. At the Ludwig cusp (s,r*,k*)=(sqrt3,3sqrt3/8,3sqrt3) the exact H-r* factor is (x-s)^3/[8(1+x²)], so the unique fixed point attracts globally without crossing. Taylor expansion z_next=z-c z³+d z⁴+0*z⁵+O(z⁶), c=tau*sqrt3/(32+12sqrt3*tau), d=c/(2sqrt3), yields w=z^-2 increments a-2d sigma w^-1/2+3c² w^-1+O(w^-3/2). Summable correction analysis gives the exact signed sqrt(n), log(n), finite-constant expansion. The log coefficient 3a/4-1/12 vanishes uniquely at tau=16sqrt3/9; tau=infinity case has a=1/6, ell=1/24. Finite checks support algebra only.

## originality

PASS

Best-of-knowledge PASS. The primary Ludwig source identifies exactly this map and cusp but presents local bifurcation correspondence, rather than the all-parameter global monotone attraction and exact subleading asymptotic. Generic one-dimensional order preservation and parabolic asymptotic methods are prior mathematical tools. A previously published signed/log law occurs in a different positive rational map at a flip (-1), not this positive-derivative (+1) cusp.

## value

PASS

The global order-preserving basin theorem excludes cycles for every positive timestep despite cusp bifurcation literature focusing locally. The exact sign-changing logarithmic correction and its unique cancellation timestep quantify a natural critical-slowing observable in the actual discretization coordinate; these are motivated, model-specific dynamical invariants rather than a generic Taylor exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
