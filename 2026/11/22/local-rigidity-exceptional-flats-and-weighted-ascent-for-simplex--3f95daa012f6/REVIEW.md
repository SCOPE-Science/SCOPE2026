# Independent mathematical audit

## correctness

PASS

From the incidence identity BᵀB=(q−2)I+J, the midpoint Gram projection has the stated three nonzero entry types. Thus its sign matrix is 2BBᵀ−2I−J and on the constant, midpoint, and remaining spaces its eigenvalues are (−m²+7m−4)/2, 2(m−2), and −2. As F is the trace against this sign matrix divided by N in the sign neighborhood, the loss is exactly the two spectral-gap-weighted leakage traces. Their sum is half the squared Frobenius distance. Testing a rotation toward either complementary eigenspace gives sharpness, and comparing the gaps yields the equality sets and the m=7 crossover. A different projection cannot be another local optimum within the sign neighborhood for m≥5: stationarity under conjugating rotations would require it to commute with the sign matrix, and a missing top-eigenvalue direction could then replace a lower one by arbitrarily small improving rotations. At m=4 the constant and midpoint spaces tie, so the equal-value locus near P₀ is the dimension-four Grassmannian of hyperplanes in their sum. Writing the complementary normal w near c, the row sums of the absolute Gram are 8/5+4/N−4w_e². The constant-vector Rayleigh quotient equals the top eigenvalue only for constant row sums, forcing w=c locally. The derivative at zero sends c to −(4/5)u while the constant Rayleigh quotient stays fixed. The unperturbed weighted eigenvalue gap to the u-space is 8/5+1/15=5/3, giving the Taylor coefficient (16/25)/(5/3)=48/125. Independently built midpoint vectors give max leakage error 3.19e-15 in 21 perturbations across seven dimensions, with small-angle weighted coefficients 0.38399756 to 0.38399960 across sampled directions. This supplements the exact trace and perturbation proofs.

## originality

PASS

Credit the midpoint configuration, its baseline value and fixed-frame weight spectrum, and the standard spectral variational and eigenvalue perturbation tools. The supported distinct claim is the behavior as the real Gram projection varies: the sharp local leakage and equality diagram and the exceptional dimension-four flat with strict optimized-weight ascent and explicit curvature.

## value

PASS

The local geometry of a natural candidate projection-constant frame is useful independently of the global conjecture. The theorem distinguishes dimensional regimes, identifies which directions are cheapest at fixed weights, and shows that a whole equal-weight flat in rank four is nevertheless improving when weights adapt. The explicit positive coefficient measures that instability rather than just detecting a larger value elsewhere.

The dated certificate retains the supplied scientific assessment, sources and limitations.
