# Independent mathematical audit

## correctness

PASS

For the repaired RESULT.md, bounds normalize to [0,1] when m<M. The step decomposition is convex after adding masses y₀ on the constant one and 1−yₙ on the constant zero. At a nonnodal point j+t only the jump line to the right can contribute negatively; upper overshoot follows by reflected complement. Dividing by the two local weights gives the stated H(s), s≥1−t. In H′ the positive term subtracted from 1 is increasing in s and already exceeds 1 at s=1−t, so the adjacent jump gives the largest possible two-weight bound. On ≥4 nodes an extra strictly positive denominator weight makes the negative estimate strict; continuity and finitely many steps give a strict uniform bound on each fixed grid. Three-node step data realize the exact maximand. The change of variable r=t/(2−t) gives the stationary equation by logarithmic differentiation, and monotonicity of its two sides proves uniqueness. Independent high-precision evaluation agrees with the quoted gamma=2 value. The original unqualified endpoint wording did not distinguish equality on m=M or strict positivity from nonnegativity: (m,m,M) reaches exactly zero at M/m=1+1/δ. The complete replacement separates those cases and proves both sharp ratio guarantees; it retains the all-grid range theorem without alteration for m<M.

## originality

PASS

The supported distinct contribution is the sharp all-grid bound and strict larger-grid inequality at nonzero scale, with the corresponding global contrast guarantees; the formula and attained three-node optimum themselves are credited to the separate three-site result.

## value

PASS

The repaired claim turns an exact short-grid example into an optimal envelope independent of grid length, with strict rigidity and a sharp positivity/nonnegativity contrast that matters when interpolating positive monotone data. Uniform Lebesgue stability alone cannot furnish such a guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
