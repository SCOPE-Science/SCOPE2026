# Independent mathematical audit

## correctness

PASS

For the specified regulator dX=√(2D)dB+dL and jumps in position only, solve the bounded interior hitting-time ODE with u(0)=1 and set φ=−u′(0). Multiplying u by exp[−(h−ℓ)φ] gives the reset backward equation and the reflection condition F_x+F_ℓ=0. Stopping at the first regulator level h gives the claimed transform: at that level X=0, and for s>0 the bounded terminal term at deterministic time tends to zero. The limit at s=0 is 1; expanding the logarithm at zero gives both finite cumulants. With z=x₀√(r/D), the sign of the derivative is that of z−2+2e^(−z)+λz(z−1). It is negative through z=1 (the λ term is zero at 1, not strictly negative as the proof's prose says), then changes sign exactly once by the strict decrease of Λ from +∞ to 0 on (1,z₀). It is positive for z≥z₀. The expansions follow by inversion at z₀, where Λ′=−1/z₀ and Λ″=(z₀²+2z₀−2)/(z₀²(z₀−1)), and the simple pole at 1 with residue 1−2/e. Subtraction of the first two cumulants in the form V−M² gives −2∂_r M−b², with b=h e^z/√(rD); hence at the optimum V=M_H(M_H+2b)>0 with M_H=(e^z−1)/r, and V<M². If contact is erased, the no-reset passage transform is exp[−(x₀+h)√(s/D)], giving the stated renewal optimizer q=z₀/(1+λ). For q>1 the claimed comparison with Λ(q) reduces to strict convexity of N(q), vanishing with its derivative at z₀; for q≤1 it is immediate. No h=0 claim beyond a limit is needed.

## originality

PASS

Pass is for the finite positive threshold joint optimizer, optimal-dispersion and reset-protocol comparison, not for the already known MFPT, full transform, or complete-renewal benchmark. The known transform permits computation of both cumulants but specializing it to one site does not supply the all-threshold minimizer classification, exact stationary cancellation, or strict comparison. No directly covering optimization theorem was identified in the bounded comparison.

## value

PASS

A physically meaningful change in what a reset erases alters a familiar renewal optimum law. The exact, strictly positive variance deficit and the ordering of optimal rates for every h>0 distinguish the protocols; the second-order separation explains why their small-threshold rates can appear similar. This is more than a new presentation of the known mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
