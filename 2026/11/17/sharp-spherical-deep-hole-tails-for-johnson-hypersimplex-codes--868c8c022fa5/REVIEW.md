# Independent mathematical audit

## correctness

PASS

The centered hypersimplex is the section of the coordinate box by sum z_i=0. Nearest genuine facet planes occur at the coordinate bounds and have Euclidean origin distance s/sqrt((N-1)k(N-k)) after division by r=sqrt(k(N-k)/N); the minimizing normals are exactly the claimed sign-coordinate orbits. In a tangent chart near a deep hole, only subsets active on the nearest facet matter; the maximum perturbation equals (1/r)F_s(z), where F_s is the sum of the s largest zero-sum coordinates (up to sign). Since F_s is positive away from zero, T<=c+epsilon forces ||z||=O(epsilon); rescaling z=r epsilon y reduces the cap to Q_{m,s}={F_s(y)<=1}. Sorted coordinate chambers have difference coordinates d_j>=0 with coefficients a_j=j(m-s)/m for j<=s and s(m-j)/m otherwise, and Euclidean Jacobian 1/sqrt(m). Multiplying simplex chamber volume by m! gives sqrt(m)m^(m-1)/[s!(m-1-s)!(m-s)^s s^(m-1-s)], proving the full coefficient and exponent m-1=N-2; spherical chart Jacobian contributes relative O(epsilon). The boundary cases s=1 and k=N-1 and both balanced orbits are included. Independently recalculated N=3,k=1 coefficient 2sqrt(3)/pi; source verifier derives facet hulls and polar volumes for small dimensions, corroboration only.

## originality

PASS

Best-of-knowledge PASS. The old centered-hypersimplex facet geometry and two-distance Johnson spherical code are prior; their statements do not imply the all-rank Haar tail exponent, exact factorial coefficient, or balanced-orbit doubling. Related code nearest-vertex tails concern other sampling measures, spaces or codes. Incomplete unindexed historical integral-geometry coverage is a genuine residual risk.

## value

PASS

Spherical covering codes are natural objects and the probability of directions near their deepest holes quantifies robustness of worst-case covering; an exact Haar coefficient sharp in rank is a nontrivial geometric invariant with factorial dependence and a balanced rank phase transition. This is not merely recomputation of the facet inradius: the local tangent polar volume and deep-hole count determine the tail.

The dated certificate retains the supplied scientific assessment, sources and limitations.
