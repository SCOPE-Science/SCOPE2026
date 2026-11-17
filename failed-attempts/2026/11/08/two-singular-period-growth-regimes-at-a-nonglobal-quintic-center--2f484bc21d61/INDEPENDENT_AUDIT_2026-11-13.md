# Independent mathematical audit

## correctness

PASS

For the flow dx/dt=v, dv/dt=-x+kappa x^3 v^2-beta x^5, the integrating factor p(x)=exp(-kappa x^4/4) gives a conserved H=p(x)^2 v²/2+integral_0^x s(1+beta s^4)exp(-kappa s^4/2)ds. V is even, strictly increasing on x>0 and approaches the displayed finite H_infinity, so every 0<H<H_infinity is a single regular periodic oval with turning amplitude A; the center is not global. The physical period is 4 integral_0^A [2 exp(kappa x^4/2)(V(A)-V(x))]^-1/2 dx, with exact transformed exponential kernel. Large-x Laplace estimates give T(A)/A² -> 2sqrt(kappa) for beta=0 and T(A)=4sqrt(kappa/beta)log A+O(1) for beta>0, after controlling the turning-point strip. The time-preserving coordinate z=integral_0^x p(s)ds gives restoring force z+(beta-kappa/5)z^5+O(z^9) and T(A)=2pi[1+(kappa-5beta)A^4/16+O(A^8)], so beta>kappa/5 guarantees an interior minimum and two amplitudes for sub-2pi periods. Independent integrals with kappa=1, beta=0,2 at A=4,8 corroborated the amplitude laws, not their universality. The leading period laws, local period jet and parameter scope agree with the PRIOR November 1 theorem for alpha=kappa; the November 8 additive O(1) logarithmic remainder is a routine quantitative sharpening of the earlier exact quadrature, not explicitly displayed there.

## originality

FAIL

A November 1 published theorem treats the identical flow and explicitly establishes the conserved H, periodic annulus, both leading period-growth laws with the same constants, local A^4 period coefficient, and beta>kappa/5 interior minimum/two-orbit corollary. It additionally classifies critical and supercritical escape trajectories and the energy clocks. One literal strengthening in the November 8 formulation is the bounded additive O(1) remainder for beta>0, whereas the prior displays asymptotic equivalence only. However, that bound is a routine integral estimate from the earlier exact physical-time quadrature and exponentially localized tail: on 1<=x<=A/2 the Laplace-kernel integrand differs from sqrt(kappa/beta)/x by O(x^-5), while A/2<=x<=A gives O(1) (the turning strip is integrable and negligible). No independently original central theorem remains; the bounded-error sharpening does not rescue covered main findings.

## value

FAIL

The two leading period-growth laws, the nonglobal-center annulus and the forced interior minimum are meaningful, but they were already established for this exact flow in the stronger November 1 theorem. The November 8 O(1) additive remainder at beta>0 (compared with prior leading equivalence) is a routine integrability estimate from the known exact quadrature, with no new constant, limiting correction, parameter boundary, or independently motivated invariant. This minor technical improvement cannot make the repackaged central classification scientifically valuable under the same V bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
