# Independent mathematical audit

## correctness

PASS

Projection onto the capped isotonic polyhedron is continuous piecewise affine; on each strictly complementary face its derivative averages over consecutive blocks. Every block partition can be realized with lower-constraint KKT multipliers positive and interblock slopes strictly between 0 and caps (even for infinite caps), so the global H1 norm is the maximum over all block averages. In the edge-gradient representation A has nonnegative entries, column sums ≤1 and adjacent block row sums (a+b)/2. For three or more blocks ∥A∥₂²≤∥A∥₁∥A∥∞≤(n-1)/2. Two-block exact squared norm n/3+(1/a+1/b)/6 determines n=2,3,4 exceptions; three blocks (1,n-2,1) with constant gradients attain (n-1)/2 for every n≥5.

## originality

PASS

Ordinary isotonic regression contraction theory (Yang–Barber) addresses seminorms satisfying neighbor-averaging nonexpansivity; it does not compute the sharp superunit first-difference ℓ2 amplification for projection onto arbitrary positive two-sided slope caps. Agarwal–Phillips–Sadri treats algorithms for Lipschitz isotonic regression rather than this exact two-input H1 modulus. The derivative is a consecutive-block mean, which is classical; the optimized spectral constants, cap-independence and small-n exceptions constitute the asserted separate contribution.

## value

PASS

The exact cap-insensitive growth of gradient perturbation amplification despite ℓ2 contractivity is a mathematically motivated conditioning law for constrained least-squares trend fitting; small n exceptions and explicit extremizers are useful for interpolation and sensitivity analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
