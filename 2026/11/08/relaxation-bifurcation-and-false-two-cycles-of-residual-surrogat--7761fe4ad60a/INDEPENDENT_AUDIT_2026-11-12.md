# Independent mathematical audit

## correctness

PASS

For b=Ax*+z with A^T A=λI, z in ker A^T nonzero, e=x−x* obeys A^Tr=−λe and ||r||²=||z||²+λ||e||². The exact update is e'=−(ω−1+ω c/||e||²)e with c=||z||²/λ>0, so it is always defined from nonzero e for 1≤ω<2 and the error direction alternates. Radius ρ'=(ω−1)ρ+ωc/ρ gives an exact involution at ω=1. When 1<ω<2, the rescaled s map is (ω−1)s+(2−ω)/s, a strict contraction in |log s| with a compactness argument for convergence to s=1. Thus the two subsequences approach a false 2-cycle of radius sqrt(ωc/(2−ω)), and adjacent midpoints approach x*. Local derivative is 2ω−3; at ω=3/2 the radius is the Newton/Babylonian iteration ρ'=(ρ+3c/ρ)/2 with exact quadratic error (ρ−sqrt(3c))²/(2ρ). Independent SymPy algebra and direct 480-step vector tests across four relaxation values agree; source code tests are additional corroboration, not an infinite proof.

## originality

PASS

The 2023 surrogate hyperplane paper assumes consistency; the 2024 sparse variant is a different regularized model; the 2026 residual double/triple algorithms use extended normal equations and avoid precisely this unextended full-residual map. The resulting precise global false-cycle bifurcation and quadratic attraction to a wrong solution are not consequences of those convergence statements. Qualified best-of-knowledge PASS, especially because the closest 2026 complete publisher article was not accessible.

## value

PASS

This is a sharply motivated algorithmic failure mode: a standard-looking full-residual projection on an inconsistent problem has exact false two-cycles even when all singular values coincide. The exact global bifurcation, unexpected quadratic attraction to the wrong cycle at ω=3/2 and provably consistent midpoint averaging are useful diagnostics for numerical linear algebra and model design, not a cheap generic pathology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
