# Independent mathematical audit

## correctness

PASS

A thin SVD reduces the iteration to positive scalar multipliers g_alpha(t) with residual update h_alpha(t)=1-(1-t)g_alpha(t)^2. Differentiation and evaluation at t_* give the stated maximum, whose difference from 1+1/(2alpha) is the positive prefactor times the cubic. The maximum is strictly increasing (compare at a positive maximizer, or from its boundary value 1 at alpha=3/8), whereas the comparison function decreases. Below the crossing, t in (0,1) maps into (-1/(2u),t). On (-1/(2u),0), the second-order Taylor polynomial upper bounds (1-t)^(-1/2), since the third derivative is positive and t is negative; hence 0<g_alpha(t)<1 and t<h_alpha(t)<=0. Uniform strict drift at any nonzero candidate limit then gives scalar convergence for every schedule, and the multipliers preserve the polar branch. The exact polynomial h_alpha(t)/t^2 extends jointly continuously at zero on the full compact interval [-1/(2u),1] times [3/8,u], so the claimed uniform inequality even holds with K=0 after enlarging C_u; this says nothing about a condition-number-independent entrance time into a small residual neighborhood. At the maximizing start the endpoint lands on the nonunit g=1 fixed point; above it the same start crosses the fixed point and the scalar increases without a finite limit. Independent rational spot checks of the identities and bisection corroborated the root 1.472229260972032370849477394..., but the universal result is analytic. VERIFICATION.md and verify.py were inspected; the uploaded checker was not executed.

## originality

FAIL

The distinct mirrored adaptive-quintic matrix-sign/polar theorem supplies the same exact coefficient frontier, arbitrary switching guarantee, and sharp counterexamples for a strictly broader coefficient interval. Its exact residual map also implies the quadratic estimate by one local expansion. The narrower frozen theorem therefore adds no distinct mathematical claim over current indexed coverage. The matching entry is later-dated; this is not a finding of earlier priority, dependence, or lack of independent derivation. PRISM itself does not cover the frontier.

## value

PASS

As a mathematical result the exact cap is useful: it certifies every schedule in a previously empirical operating range and explains failure at the boundary rather than just improving a constant. It is not evidence of finite-precision stability or failure of a specific selector. That usefulness does not add distinct content over the broader indexed theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
