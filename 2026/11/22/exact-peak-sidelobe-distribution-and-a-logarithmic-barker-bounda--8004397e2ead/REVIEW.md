# Independent mathematical audit

## correctness

PASS

The map from the four original phases to the initial phase and three consecutive differences is a unimodular torus change of variables, so the differences are independent Haar. The lag-two magnitude is the magnitude of the sum of the two outer difference phasors, 2X with X=|cos((delta_0-delta_2)/2)|; lag one adds the independent uniform middle phasor to this sum. Thus the angle relative to the outer sum is conditionally Haar (the zero sum is null), and V=1+4X^2+4X cos(Phi). Since X has density 2/(pi sqrt(1-x^2)), U=4X^2 has density 1/(pi sqrt(u(4-u))); conditional V is shifted arcsine with center 1+u and radius 2 sqrt(u). Their product is exactly the stated density on its open region. Lag three has modulus one, so it is not a third random density coordinate. In the threshold event X<=s/2, lag one automatically passes for X<=(s-1)/2; integration of its conditional probability in the rest gives the claimed CDF with the clipped arcsine function. At s=1, setting x=sin(t) leaves (2/pi^2) times the integral of pi/2-t from 0 to pi/6, which is 5/36. The support is all of [1,3]: the minimum occurs when the outer difference phasors cancel, the maximum when all three align, and the peak is continuous on the connected torus with Haar of full support. For s=1+epsilon the interval from 0 to a fixed large multiple of epsilon affects the difference by O(epsilon), as do the O(epsilon) motion of the upper cutoff and the integrand change bounded away from x=0. On the intermediate interval from C epsilon to a fixed small eta, both arcsine arguments stay away from clipping, and Taylor expansion with bounded second derivative gives epsilon/(pi^2 x(1-x^2)) plus O(epsilon^2/x^2). The latter integrates to O(epsilon); the former yields exactly the log term and its coefficient. This provides an analytic error estimate rather than a fit to simulations. The supplied numerical quadrature/simulation checker and output were inspected, not executed; neither is required to derive the law or remainder.

## originality

PASS

The distinct claim is the exact peak distribution in the four-chip continuous-Haar model, in particular the positive Barker atom and the sharp logarithmic boundary beyond it. A close same-ensemble prior result is stronger than a list of scalar moments: its phase-character representation makes the basic conditional arcsine law recoverable. That ingredient is credited, not treated as a separate novelty. The inspected prior results do not give the peak cutoff calculation or the singular boundary law; the latter requires a nonuniform analysis near cancellation of the outer sum. This is a bounded statement-level assessment, not priority certification.

## value

PASS

For a continuous random polyphase code, the distribution at the lowest feasible peak is a natural comparison against designed Barker codes. Length four is the first length with two nonconstant aperiodic sidelobes (length three has only one); their dependence matters for that probability. The result gives a usable exact reference CDF, quantifies the positive measure of the optimum-peak region, and identifies its logarithmic growth immediately above the minimum, rather than merely recomputing a scalar energy moment or finding one optimal code.

The dated certificate retains the supplied scientific assessment, sources and limitations.
