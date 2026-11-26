# Independent mathematical audit

## correctness

PASS

Gaussian convolution gives q₀=u^(d/2) and q_out/q₀=s^u. The unique full Gram solution is constant on each signed-permutation orbit; the outer row has affinities 1, s⁴, and 2(d−1) copies of s² within the outer orbit. Eliminating the center gives the strictly positive outer weight with denominator (1−s²)² and the stated center formula. As an independent sign check, define T(s)=2d s^(1+u)−1−2(d−1)s²−s⁴, so the center sign is the sign of −T. The derivative T′/(2s^u)=d(1+u)−2(d−1)s^(1−u)−2s^(3−u) decreases strictly from d(1+u)>0 to d(u−1)<0. Thus T rises from −1 to a positive maximum, then strictly falls to T(1)=0; the crossing in (0,1) is unique and the direction in radius reverses since s decreases with radius. With u fixed, the equation F_u(s*)=1/d forces s*→0, and F_u(s*)/(2s*^(1+u))→1, giving a*²/(2ℓ²)=log(2d)/(1+u)+o(1). At fixed a,τ,d with ℓ→∞, s^u−s∼a²τ²/(2ℓ⁴) and (1−s²)²∼a⁴/ℓ⁴, giving the two flat-kernel limits.

## originality

PASS

Credit the prior symmetric reduction, exact geometry, and large-d negative-center observation. The supported distinct claim is the all-radius, all-scale positivity iff with unique finite crossing and dimension-dependent sharp radius law. Prior general frameworks give the linear solve but do not give that classification or its dimension law. The exact indexed reentrant law is broader in mixtures and nuggets but is restricted to the one-dimensional three-node geometry.

## value

PASS

The radius of a standard sigma-point design is a practical control parameter. A qualitative high-dimensional negative-weight phenomenon does not tell a designer whether an arbitrary radius is safe or how much to increase it. The exact one-sided sign threshold and sharp normalized squared-radius law answer those questions for this natural design. The finding does not claim that this radius minimizes quadrature error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
