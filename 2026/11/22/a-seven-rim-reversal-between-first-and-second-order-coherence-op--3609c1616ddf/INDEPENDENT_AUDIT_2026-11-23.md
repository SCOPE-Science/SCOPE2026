# Independent mathematical audit

## correctness

PASS

On the connected-support domain X=L+11ᵀ/(m+1) is positive definite and F_p=tr(X^(−p))−1. The second derivative along any nonzero conductance direction is positive: differentiating the inverse powers and diagonalizing X writes the Hessian as a sum of |H_ij|² times positive inverse-power coefficients, and the off-diagonal entries make the edge map injective. This domain is convex and costs diverge at disconnecting boundaries, so a unique optimum exists on the full simplex. Uniqueness forces rotational invariance. The constant-rim mode gives eigenvalue (m+1)a and the other cycle modes give a+b(2−2cos(2πk/m)); the null mode is excluded. The scalar derivative at u=0 has sign of (m+1)^(−p)−(m+1)<0, and cost diverges at u=1, so both conductance classes are positive. K4 edge transitivity gives the tie at m=3. I independently computed all seven exact separator pairs from the characteristic polynomial P(y)=2u^m(T_m(y/(2u))−1), y=1+u, using its exact Taylor coefficients through order three to recover Σ_k(1−u+u μ_k)^(−j), j=1,2,3. This gave signs (+,−) for 4–6 and (−,+) for 7–10 (replay: python3 /workspace/evidence/4_wheels.py; output /workspace/evidence/4_wheels.txt). For the remaining sizes, the Fourier geometric series gives Σ_k(s−cos(2πk/m))^(−1)=m C(s)/√(s²−1), with z=(s−√(s²−1))^m and C=(1+z)/(1−z). Differentiating with C′=−2mT/√(s²−1), T′=−mTC/√(s²−1), T=z/(1−z)², reproduces S1,S2,S3 at s=2. In the derivative at u=1/3 the full-mode constant correction is +1 in D_p=2S_p−3S_{p+1}+1. Then D1=1−2m²T>(m+1)^(−1) using 2m²T<243/338<3/4, and D2<1−m/(6√3)<0 for m≥11. Hence u2<1/3<u1 there without extrapolating from finite numerics. Uniform Riemann sums for objectives and derivatives on compact interior intervals let the limiting derivative bracketing control the finite roots. The cosine integrals give f1=1/√((1−u)(1+3u)) and f2=(1+u)/[(1−u)(1+3u)]^(3/2), with roots 1/3 and the unique positive solution to 3u²+4u−1=0. Compact uniform convergence at the converging minimizers justifies the objective ratio; independent evaluation gives 1.0459424374291556. The frozen script was inspected, not executed.

## originality

PASS

Prior sources directly cover the first-order wheel allocation and the second-order functional as separate topics. Under the equivalent biharmonic-index formulation and in the closest distinct Resultary graph families, the inspected material does not give the wheel reversal or the second-order wheel limit and relative loss. No priority is claimed for the p=1 comparator, symmetry reduction, definition of coherence, or general spectral calculus.

## value

PASS

The two inverse moments express different coherence objectives under exactly the same natural resource constraint. On a common, nontrivial graph family, the optimal reallocation goes in opposite directions below and above a specific sharp size, so first-order design does not even predict the direction of second-order design uniformly. The positive roughly 4.6% limiting second-order relative loss makes the mismatch quantitative rather than a numerical curiosity. The result adds a proved comparison and limit, not another derivation of the known first-order optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
