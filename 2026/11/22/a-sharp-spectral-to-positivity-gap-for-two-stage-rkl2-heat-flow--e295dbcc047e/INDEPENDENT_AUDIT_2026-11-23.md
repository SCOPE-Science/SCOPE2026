# Independent mathematical audit

## correctness

PASS

The cited RKL2 polynomial with two stages reduces to I−hL+h²L²/2. Its diagonal entries 1−dh+d(d+1)h²/2 are positive, the nonedge entries are nonnegative, and the ij edge entry is h[1−h(2d−(A²)ij)/2]; an edge minimizing (A²)ij stays negative at every h>2/(2d−t). The connected d≥1 condition excludes an empty edge set. The symmetric Laplacian gives Euclidean contraction exactly for hΛ≤2, since its multipliers are [1+(1−hλ)²]/2. The rows and columns sum to one at all h. For J(n,2), counting common neighbors gives t=n−2, and the unsigned vertex–edge incidence matrix of K_n gives A=BᵀB−2I, BBᵀ=(n−2)I+J. The latter is nonsingular, while B has a nonzero null space for n≥4, so Λ=d+2=2(n−1); the two cutoffs, equality at n=4, strict gap thereafter, and ratio follow. The n=5 edge arithmetic at 7/30 yields −7/600 exactly. The nonlinear necessity argument is not an inference from linear stability: matching the signs of a negative-entry row gives heat output equal to its absolute row sum, greater than one. In this example it is 57/50 before the last half-flow. The reaction fixes input signs, preserves the cube, and cannot bring an outside coordinate back into it at finite time. Uploaded verify.py was inspected only; its rational finite checks do not support an all-graph inference without the proof.

## originality

PASS

The completed scheme, its scalar stability radius, the triangular-graph spectrum and the forward sufficiency of a monotone heat step are not new. The distinct claim is the graph-dependent exact positivity criterion and consequent exact stable-but-not-positive interval, including an unbounded family and the corresponding necessary and sufficient cube condition. The strongest inspected results cover particular discretizations, particular graph families or different polynomials, not this combination.

## value

PASS

The cutoff is an exact step-size test depending on a local graph statistic, rather than a generic sufficient bound. The triangular graphs show a constant-factor gap approaching 3/2 and give an explicit stable one-step failure of the nonlinear maximum principle. This is a substantive distinction for a completed diffusion step even though the spectral calculation and graph entry expansion are elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
