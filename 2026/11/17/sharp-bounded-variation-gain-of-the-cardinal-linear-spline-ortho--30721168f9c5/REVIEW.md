# Independent mathematical audit

## correctness

PASS

The unit hats give tridiagonal Gram entries 2/3 and 1/6; q=sqrt(3)-2 solves q+q^(-1)=-4 and the zero row gives the coefficient sqrt(3) of the summable inverse. The inverse defines the stated extension, reproduces constants and agrees with the Hilbert-space projector by the Gram equations. Independently solved the two inhomogeneous interface equations and verified both distinct quadratic branches (/workspace/independent_exact_checks.py, linear_projection()). The central slope is strictly positive, and summing the two alternating tails gives the multiplier (1-q)/(1-|q|)=sqrt(3). The upward-opening left amplitude is positive at 0 and negative at 1/2 and 1, so its unique zero lies before 1/2; reflection gives exactly the other sign transition. This yields the three pieces and a strict interior loss since the middle maximum is 3/2. The finite signed derivative measure decomposes any admitted input into jumps plus a constant; absolute summability and Tonelli for the absolute nodal differences give the upper bound. Knot jumps belong to the extension domain, not L², and truncating the summable gradient tails proves asymptotic additivity for two separated jumps from compact interval indicators.

## originality

PASS

No checked distinct source gives the sharp homogeneous variation norm together with the exact uniform-cell phase profile. The closest results address endpoint range overshoot or finite graded meshes; the geometric inverse itself is classical. The decision is scoped to the uniform whole-line variation theorem, without a priority claim for spline stability or Green functions.

## value

PASS

The natural uniform Galerkin projector can increase total variation even for a monotone step. Its exact gain is a usable sharp stability constant for BV data, and the phase profile tells how ringing accumulation depends on alignment with the grid, beyond a worst-case overshoot or an arbitrary-mesh bound. Showing the same sharp coefficient for compactly supported inputs makes the invariant relevant to the genuine L² operator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
