# Independent mathematical audit

## correctness

PASS

Normalized Haar measure makes the coefficient norm Euclidean, and the least Rayleigh quotient is the minimal Gram eigenvalue. For centers z_i, the degree-four polynomial Q=(z−z_1)²(z−z_2)² has squared coefficient norm S=34+32c+4c², c=cos δ, and normalized squared angular quadratic term R=4(1−c)²/S at either center. Direct differentiation gives R_c'=80(c−1)(2c+5)/S², so R peaks uniquely at δ=π with value 8/3. On separated centers the four value/first-derivative constraints can be imposed by a bounded inverse on cubics (a cubic cannot have two distinct double roots), uniformly for δ≥ε>0. Starting with Q/√S, the value corrections −C_i h_i²/3 and zero derivative corrections are O(a²) in coefficient norm. The Taylor expansion and integration then cost (8/45)|C_i|²h_i⁵ on arc i before Haar normalization, with total remainder O_ε(a⁶); normalization of the corrected vector does not change that leading term. For δ→0 the uncorrected Q gives O(a⁵(a+δ)^4), which also covers touching arcs. These bounds apply to subsequences of near-supremizers even without a finite-a maximizer. Strict maximization of R and of the convex width sum h_1⁵+h_2⁵ at the boundary of fixed total width gives the geometric necessity if the upper coefficient is reached. For the antipodal construction, bounded unit coefficients give Taylor estimates |f(b)|=O(a^{5/2}h^{-1/2}+h²), |f'(b)|=O(a^{5/2}h^{-3/2}+h) by averaging against 1 and u on each arc, since the trial bounds the L² mass there. Both tend to zero also for h=a^{3/2}. Compactness forces all limit directions into the one-dimensional normalized double-zero kernel; thus the squared large-arc quadratic coefficient tends to 8/3. Projection onto u²−h²/3 lower-bounds each applicable local integral by (8/45)|C_i|²h⁵+O(h⁶), using uniform third-derivative control. The large arc alone, h_1/a→2, yields (1/(2π))(8/45)(8/3)2⁵=1024/(135π). For equal antipodal widths the same argument projects on both arcs and replaces 2⁵ by 2, giving 64/(135π). The proof uses RESULT.md §§1–6; the supplied VERIFICATION.md and checker were inspected, not executed. No claim about maximizing at any fixed a or over general measurable sets is needed.

## originality

PASS

An earlier Resultary theorem covers the equal-width coefficient and antipodal placement, and a distinct same-day record supplies a stronger finite-aperture statement on the equal-width slice. The reviewed remainder is the different two-width minimax with a singular allocation, sharp sixteenfold gain and rigidity of the width share and separation. None of the compared statements dominates that problem.

## value

PASS

Given a fixed total observation measure and two components, allocating their widths is a natural part of the design rather than an arbitrary generalization. Equal allocation, though optimal over placements on its own slice, loses a factor of sixteen at leading order. The result shows that a companion with negligible measure can still enforce two independent jet conditions, and that all near-maximizers must use a vanishing width fraction there while staying antipodal in the limit. This changes the design conclusion, not merely a normalization or numerical estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
