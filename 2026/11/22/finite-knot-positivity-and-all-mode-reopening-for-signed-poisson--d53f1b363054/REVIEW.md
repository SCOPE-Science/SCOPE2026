# Independent mathematical audit

## correctness

PASS

For the stated nonzero positive compactly supported non-point measure and d>=2, k>=1, the change y=2-2 cos(theta) expresses F as a Stieltjes transform of a positive weighted pushforward onto t=(1-r)^2/r. Complete-Bernstein reciprocity and its integral representation were verified in Kwaśnicki, Corollary 2.16 and Proposition 2.17(a). The representation can be integrated termwise (0<=y<=4 yields an integrable bound proportional to (1+t)^(-1)); the positive geometric resolvent coefficients of (y+t)^(-1) give only nonpositive off-diagonal Fourier coefficients of 1/F. They are all strictly negative because the representing measure cannot be zero. Independently of transform uniqueness, if W is the mass and m_j the normalized t-moments of the weighted pushforward, the reciprocal has expansion y/W+m_1/W+(m_1^2-m_2)/(Wy)+O(y^(-2)), ruling out an affine reciprocal when the pushforward has positive variance. The inverse Fourier coefficients are summable and have positive row sum. Applying the minimum argument directly outside the finite set {0,+/-k,...,+/-dk} proves nonnegativity, and an exterior zero contradicts its strictly negative coupling to a positive knot. This also verifies the original two-stage proof. Invertibility follows from the positive weighted cosine Gram matrix (the factor 2 in the nonconstant mask columns is removed by column scaling); hence every nonzero feasible mask has a positive knot. Bochner, the consecutive-frequency Vandermonde argument, and the Fourier character density/missing-coefficient test prove PSD, finite-site strictness, and the universality equivalence, including the zero-mask exception. An independent exact calculation gives b_0,...,b_4=(1,0,0,1/30,1/30) in the example and b_n=[(3/4)^(n-2)-(1/4)^(n-2)]/15 for n>=2. Replay: /workspace/branches/b9005369-05b0-45d9-8a9b-e24720b8f5d5/two_radius_exact.txt. Neither this example nor the inspected, unexecuted package checker proves the full mixture theorem.

## originality

PASS

Best-of-knowledge pass for the exact arbitrary multi-harmonic mixture cone and classification of its spectral zeros, not for complete-Bernstein reciprocity, the maximum principle, or one-harmonic reopening. The closest indexed results overlap materially but specialize either to a single Poisson radius or to a mask with one nonconstant harmonic. The verified analytic literature supplies a representation and general spectral tests, not a previously verified full classification in this signed-mask setting.

## value

PASS

Signed harmonic modulation is a natural case not resolved by multiplying two positive-type kernels. Reducing infinitely many Fourier inequalities to independent finite knot inequalities is useful; the sharper distinction from the one-radius case is that every nonzero cone face gives a cofinite spectrum and strict finite-site positivity, even with several zero knots and without universality. That boundary result requires the non-point mixture's full inverse coupling; it does not follow from geometric nearest-neighbor interpolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
