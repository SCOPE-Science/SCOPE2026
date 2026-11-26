# Independent mathematical audit

## correctness

PASS

In the exact-data scalar model the perimeter is 2πR and the curvature-squared integral is 2π/R. Dividing by 2πR₀ gives Hξ(y)=y+ξ/(6y)−B(ξ), so the positive-radius domain excludes the spurious y=0 introduced by multiplying through at ξ=0. For ξ>0 the first two terms have unique minimum 2sqrt(ξ/6), diverge at both ends, and decrease then increase; subtracting B gives the two/one/no-root classification. F=B−2sqrt(ξ/6) is strictly decreasing from 1 to a negative value at 1/2. The stronger bound ξ*<9/20 puts the exact-flow radius on the increasing side of Hξ. Simpson overestimates the exact dissipated energy because g⁽⁴⁾>0 for g(s)=(1−2s)^(−1/2), so Hξ at the exact radius is positive and y₊ lies strictly below it. The one-panel residual at the exact radius is (105/2880)ξ⁵+O(ξ⁶), and the y derivative there tends to 1; this independently recovers the −7/192 coefficient. Factoring Δ=F(F+4sqrt(ξ/6)) gives the root-gap constant, and Hξ′(y₊)=(y₊−y₋)/y₊ gives the stated normalized inverse Jacobian. Round two-sphere dissipation is the constant 16π, yielding the unique exact positive radius throughout its lifetime.

## originality

PASS

The prior flow identities, Simpson formula and generic double-root behavior are not the contribution. The supported distinct claim is the sharp branch and conditioning classification for the specified exact-data positive-radius closure. No examined independent source provides this classification or a stronger result that specializes to it.

## value

PASS

The exact-data reduction is motivated as a diagnostic for geometric integrators rather than an arbitrary example: even removing numerical start and midpoint error, an energy-decreasing scalar design can have no positive-radius solution while the exact circle still exists. Its exact cutoff and inverse sensitivity inform whether a failed or ill-conditioned scalar solve can be blamed on input errors. The exact sphere contrast identifies constant versus increasing dissipation as a useful distinction, without a claim about the coupled algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
