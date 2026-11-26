# Independent mathematical audit

## correctness

PASS

This is the supremum over all SPD orientations at a fixed condition number and all nonzero gradients, not a bound attained for every fixed Hessian. In units where eigenvalues lie in [1,κ], use the gradient-squared spectral weights, with moments m1 and m2. Exact line search gives α=1/m1, h=g⁺ perpendicular to g, and ||h||₂²/||g||₂²=m2/m1²−1. The inequality m2≤(1+κ)m1−κ yields the sharp Euclidean factor c=(κ−1)/(2√κ) by maximizing at m1=2κ/(1+κ). Projection onto g's perpendicular space bounds |h_j| by c times (Σ_{i≠j}g_i²)^{1/2}. The supplied two-plane block has trace 1+κ, determinant κ and sends the chosen unit g=u to a step with h=cv; its projections attain the claimed factor. Equivalently take any sharp Euclidean step and rotate to g supported equally on n−1 coordinates, h supported on the remaining coordinate. For κ=1 the update is zero. Solving c√(n−1)≤1 yields the stated inclusive threshold. Independently checked the displayed 3×3 matrix by exact symbolic arithmetic: spectrum {1,1,4}, α=5/8, h=(3√2/4,−3√2/8,−3√2/8), which gives both ratios. The frozen decimal checker was read, not run.

## originality

FAIL

The max-norm law is not asserted verbatim in the inspected primary result, but it is mechanically implied by the known sharp Euclidean step estimate, ordinary exact-line-search orthogonality and the freedom to rotate the entire problem. The evidence is the direct implication, not the presence of matching search words or a claim that the paper literally prints the infinity-norm formula.

## value

FAIL

The diagnostic and contrast with Euclidean decrease are mathematically legitimate, but the advertised frontier for unrestricted orientations is a routine norm-geometric consequence of the established sharp exact-line-search result. The particular numeric matrix is a freely rotated equality step, not a separately motivated problem or a nonroutine new witness. No genuinely independent exact claim for fixed orientations, structured Hessians or trajectories is offered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
