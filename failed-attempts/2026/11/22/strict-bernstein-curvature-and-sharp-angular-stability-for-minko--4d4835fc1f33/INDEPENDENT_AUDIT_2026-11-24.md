# Independent mathematical audit

## correctness

FAIL

The Steiner reduction, determinant/trace calculation, Gaussian radial constant and differentiated integral are correct for a>b>0 and c>d>0. Domination at zero and infinity gives all endpoint derivatives; -F'' is strictly decreasing, so m=-F''(1) is indeed the optimal pointwise curvature bound. The stated chord inequality holds strictly in the interior and circles give a constant. The finding also calls the fixed-endpoint quadratic surplus sharp (RESULT.md lines 4 and 39); that sharpness is false if it refers to the chord coefficient, rather than the separately stated curvature modulus. In fact let q(x)=-F''(x) and G(u)=F(u)-(1-u)F(0)-uF(1). Then G(u)/[u(1-u)]=u^{-1}∫_0^u xq(x)dx+(1-u)^{-1}∫_u^1(1-x)q(x)dx. Its derivative is -(1/u²)∫_0^u xq(x)dx+(1/(1-u)²)∫_u^1(1-x)q(x)dx<0, since the two scaled weights each have mass 1/2 and q decreases strictly. Its endpoint limit at 1 gives the largest coefficient in the normalization of line 37, namely 2∫_0^1 xq(x)dx=2(F(1)-F(0)-F'(1))>m. Read as claiming only optimal pointwise curvature and a nonoptimal chord refinement, the precise inequalities are correct; that reading does not cure the originality issue below. The finite numerical checker does not compare optimal chord constants and was not executed.

## originality

FAIL

The central all-orders law and optimal pointwise modulus are a direct specialization of classical Legendre and Euler integrals after the known planar Steiner/perimeter reduction. This is affirmative mathematical implication from inspected formulas, not an inference from unsuccessful retrieval. The frozen determinant-Laplace integral is a convenient alternative representation; it is not evidence that the angular sign or optimal curvature is new. The distinct intersection-perimeter record is not being treated as coverage.

## value

FAIL

Quantitative orientation dependence is a worthwhile question, and the Gaussian expression can be an alternative computational form. But the supportable claims here are a direct specialization of exact classical identities followed by the generic curvature-to-chord inequality; no independent need for that alternative integral as a new invariant is established. The headline fixed-chord sharpness does not hold. Merely changing its coefficient to the endpoint divided-difference value deduced from monotone curvature would remove the error but does not furnish a surviving nonroutine result in this package.

The dated certificate retains the supplied scientific assessment, sources and limitations.
