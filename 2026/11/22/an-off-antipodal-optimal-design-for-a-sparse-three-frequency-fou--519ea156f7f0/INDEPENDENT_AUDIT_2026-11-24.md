# Independent mathematical audit

## correctness

PASS

Integration with dt/(2π) gives diagonal 2a/π and off-diagonal (2/π)sin((k-h)a)cos((k-h)θ/2)/(k-h); the endpoint case θ=2a has only a measure-zero intersection. With c=cos(θ/2) the polynomial (z²-2cz+1)(z+2c) has frequencies 0,1,3 and vanishes at both centers. For u=c² its coefficient norm is 16u²-4u+2 and each center derivative squared is 4+28u-32u². The odd term of degree three in the local energy integrates to zero, giving the Rayleigh upper bound a³F(u)/(3π)+O(a⁵) uniformly, including moving or coalescing centers. The normalized Gram matrix πG/a is analytic in a² with limiting rank two away from coalescence (the columns of frequencies 0 and 1 suffice). In the one-dimensional null direction the order-a² entry is F(u)/3, while coupling to the positive two-dimensional block is O(a²) and affects the eigenvalue only at order a⁴. The simple-root implicit function theorem gives this expansion in C² in θ on a neighborhood of the interior maximizer. The derivative F' has the sign of 9-32u-40u² and a simple zero at (√154-8)/20. The uniform upper bound and a matching lower value by evaluating at that fixed angle confine every global maximizer to its neighborhood. Strict concavity there and the critical equation give uniqueness and O(a²) displacement, without requiring a uniform spectral gap at coalescence. At θ=π the odd-odd 2×2 block has off-diagonal -sin(2a)/π and the isolated zero mode is diagonal; since 0<2a<π the reported least eigenvalue and gain follow. Independent evaluation gives θ*=2.164014966851562 and gain 2.2728105208558365. The frozen checker was inspected (symbolic identities, integration and numerical grids), not executed or relied on for global uniqueness. No finite-width threshold or formula for arbitrary a is established.

## originality

PASS

The distinctive claim is the off-antipodal optimized coefficient and limiting separation for the non-arithmetic support, with uniqueness for sufficiently small positive widths. Neither the earlier consecutive-band optimizers nor the arbitrary-support fixed periodic array determine it; the latter already gives the leading antipodal benchmark. This is a bounded statement-level priority comparison.

## value

PASS

This minimal non-arithmetic triple supplies an explicit counterexample to transferring antipodal optimality from consecutive bands to sparse ones, at unchanged arc count and total observed measure. The sharp gain exceeds a factor of two, and locating the unique small-width optimizer rather than only exhibiting a better design makes the result useful as a benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
