# Independent mathematical audit

## correctness

PASS

The protocol is completely jammed large rods first, then small rods; the infinite-substrate limit precedes k→∞ and K/k→L. Pinsky's gap law and parking limit give the first-stage inputs with density per original site. For F_k(y)=M_k(floor(ky))/k, the discrete first-placement sum is exactly the integral of this step function up to A_k=(floor(ky)−k+1)/k, multiplied by 2/A_k and with 1 added. The first strip is constant, and bounded convergence using 0≤F_k(y)≤y propagates convergence strip by strip to the continuum recurrence, including the Riemann-sum limit without reliance on values at strip endpoints. In the gap formula s=exp(−z/K), the scaled prefactor is K(1−exp(−z/K)) and the exponential is exp(−(ℓ+1)z/K); uniform domination by z exp(−a₀z) holds for ℓ/K≥a₀>0. One may choose a₀<1/L on the entire second-stage sum. The limiting scaled gap density and the rod count yield the factor 2/L² and inner exponent −zy/L. The delay identity ((y−1)C(y))′=1+2C(y−1), starting from the jump 1 at y=1, gives matching derivatives below order m−1 and first jump d_m=2d_(m−1)/(m−1) at m. Method of steps gives analyticity on each open strip; the kernel is analytic locally in L and y where Re(y/L)>0 by exponential domination. Splitting at fixed strip boundaries and applying Leibniz leaves a single jump at order m in Φ, equal to w(m,m)d_m. This gives the claimed coefficient and strict positivity. An independently written bounded quadrature reproduced Φ(2), Φ(2.5), Φ(3) and I to the stated displayed accuracy, and confirmed the coefficients for m=2,3,4; replay via /workspace/branches/738ac5fc-165e-4136-b4c7-87cd9a6f7d64/bounded_quadrature.py. The supplied CHECK.py was not used as a fresh run, and finite quadrature does not verify the universal hierarchy.

## originality

PASS

The distinct content is the all-fixed-ratio scaling law beyond the credited L≤2 case and the exact differentiability hierarchy of its coverage function. Neither the first-stage gap density, the finite discrete gap decomposition, nor the single-length parking recurrence is distinct by itself. Pinsky explicitly isolates L>2 as an open regime in the inspected text. The related same-day fixed-small-rod result and competing-species formulas do not cover the scaling or regularity asserted here.

## value

PASS

The limit resolves the specified previously untreated physical size-ratio regime and shows exactly how new gap-filling possibilities affect a macroscopic observable: coverage remains smooth to progressively higher order but has a nonzero prescribed jump at every integer threshold. The statement supplies a useful continuum benchmark beyond the one-rod-gap regime, restricted to the two-stage expectation and stated limit order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
