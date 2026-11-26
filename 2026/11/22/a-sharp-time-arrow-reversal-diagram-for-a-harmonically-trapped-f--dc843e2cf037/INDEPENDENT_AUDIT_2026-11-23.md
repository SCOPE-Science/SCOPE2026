# Independent mathematical audit

## correctness

PASS

The motor generator sends S to −aS and S² to c−(a+c)S², with stationary E[S²]=c/(a+c). The causal stationary solution has all required moments. An independent symbolic stationary balance and polynomial resolvent calculation reproduces the stated Laplace numerator and denominator, including cancellation of diffusivity. A direct check of that cancellation writes X=Y+Z, with Z a centered independent stationary Gaussian OU process: the two-noise terms agree by covariance and equal-time variance symmetry of the two processes, the four-noise terms agree by Wick's rule, and odd-noise terms vanish. The positive exponential convolutions H,J give an inverse transform even when rates coincide. Log-concavity of H makes H(t−u)/H(t) nondecreasing in t for fixed 0<u<t; extending the interval of integration with positive integrand makes J/H strictly increasing. The small-time ratio is asymptotic to t/4. For m=min(a,b), e^{mt}H(t) is nondecreasing since one factor becomes the indicator of t≥0 and the others remain nonnegative. Thus H(t−u)/H(t)≤e^{mu}, an integrable majorant after weighting by e^{−(a+b+c)u}. The slowest-pole asymptotic gives the ratio's limit 1/(max(a,b)+c), including double multiplicity at a=b. The limits are not attained at finite time, which verifies the strict signs on both boundary cases. If a≤c the constant term is strictly negative and the coefficient of J/H nonpositive; otherwise the sign function increases strictly and crosses exactly once only for B_0<0<B_infinity. For the quoted witness (2,1,1,1), H=e^{−t}(1−e^{−t})³/6 and J=e^{−4t}∫_0^t(expm1(s))³ ds/6; separate scalar bisection of −H+5J gives 1.132906609052125. The frozen checker was inspected, not executed.

## originality

PASS

The strongest prior covers the same motor, including general active-velocity correlations and a Laplace diagram law for filtered single-time moments. A distinct class of prior records uses the same position statistic with no finite rest, or a different observable with the same rest dynamics. None of the inspected results supplies the position-only two-time phase diagram. Credit goes to the sharp finite-lag sign classification and its positive-kernel reduction, not to the motor model, general correlation method, or use of a quartic arrow.

## value

PASS

A position-only statistic that detects temporal order can change sign when only the observation lag changes. This is a substantive distinction from the strictly negative telegraph example and the positive mixed-observable result. The exact boundary tells when an experiment with inaccessible hidden motor states can in principle see a reversal; the resonance-safe formula rules out extra reversals and identifies equality cases even with arbitrary independent thermal diffusion. This is a statement of mathematical visibility, not a guarantee of finite-sample detection or a proxy for entropy production.

The dated certificate retains the supplied scientific assessment, sources and limitations.
