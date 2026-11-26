# Independent mathematical audit

## correctness

PASS

Reconstructed the projector calculation in RESULT.md (22–64): P_i=J/q_i and Q_i=I−P_i give L_i=w_iq_i Q_i, so a differing coordinate has local entries (1,−1)/q_i and an agreeing coordinate (1,q_i−1)/q_i. Summing the differing-coordinate indicators gives (−1)^k times the k-fold mixed difference; all weights for agreeing coordinates are positive. Independently, writing x=1+z and φ=arctan(1/x), partial fractions give (−1)^k f^(k)(z)=2 k! sin((k+1)φ)/(x²+1)^((k+1)/2). For z>0, 0<φ<π/4, so this is positive through k=3; at z=0 only k=3 has a zero. The iterated integral of this derivative is strict for each positive-step box of positive volume. The denominator recurrence gives coefficients 1,−1,1/2,0,−1/4 through degree four. At a four-coordinate pair no shorter walk contributes even with Laplacian diagonal terms, and the 24 shortest walks have weight ∏w_i and positive sign. Hence the negative coefficient is exactly −6∏w_i. The spectral eigenvalues are positive and f(0)=1 preserves constants; h=0 is the identity and only the constant mode survives h→∞. The scalar Padé step matches through order two and is L-stable: for z=u+iv, u≥0, the squared denominator is ((1+u)^2+1)^2/4+((1+u)^2−1)v²/2+v^4/4≥1 and grows at infinity. I inspected artifacts/verify.py as a finite unit-weight supplement; no uploaded code was executed, and the proof covers independent coordinate weights, not arbitrary edge weights within a factor.

## originality

PASS

The distinct claim is unconditional positivity for arbitrary mixed, coordinate-weighted products of up to three clique factors for this particular [0/2] filter. The distance-four obstruction and smaller positive subclasses are already covered. No inspected competing result gives the positive-side mixed-factor statement; same-object results for another filter do not imply it.

## value

PASS

The theorem distinguishes unconditional entrywise positivity from scalar spectral stability and fixes the sharp factor frontier for arbitrarily large, anisotropic graph families. Users of this heat step can decide the all-step question from the number of clique factors alone. The mechanism explains which entries are protected by signed derivatives and why protection fails at graph distance four; no unrestricted diameter or floating-point guarantee is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
