# Independent mathematical audit

## correctness

PASS

In an eigenbasis, writing the real Gaussian probe as Rv with v uniform on the circle and independent R²∼χ²₂ gives S₁=R²/(vᵀBv) and S₂=R²vᵀB⁻¹v; two Lanczos vectors span the compression almost surely. The angular first reciprocal moment is 1/√(ab) by the tangent substitution, and differentiating it jointly in a and b gives the second moment (a+b)/(2(ab)^(3/2)). The radial moments 2 and 8 and the Gaussian coordinate variances give the two claimed variances, whose difference factors as stated. Independent averaging yields error difference bias²−(2 Var(S₂)−Var(S₁))/M at equal product count, giving the exact even-budget inequalities and the example M*=44. This compares the two homogeneous allocations under the stated per-node cost, not mixtures, total running time, or corrected covariance. The frozen verifier was inspected, not executed; the reported tests are supplementary.

## originality

FAIL

Demonstrable prior implication: the October 26 indexed result provides both of the same two angular estimators in dimension two, their common beta direction variable and its full moment sequence. The frozen Gaussian moments and variance comparison follow by independent radial scaling, and the one-versus-two-node budget boundary is then the zero of the elementary bias–variance difference using the existing P-SLQ node cost. The previous result need not have printed M* to cover the mathematical content of this special-case calculation.

## value

FAIL

A product-budget depth comparison is a sensible practical question, but the exact narrow invariant here is mechanically supplied by the published two-dimensional angular comparison, χ²₂ rescaling, and standard independent-mean cost arithmetic. As frozen it gives no additional nonmechanical allocation result, such as an optimization over mixed depths or a theorem beyond the two-point spectrum. This is not a rejection for the small dimension alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
