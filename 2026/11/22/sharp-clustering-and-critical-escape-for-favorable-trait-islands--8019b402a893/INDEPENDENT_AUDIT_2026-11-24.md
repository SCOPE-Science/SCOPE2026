# Independent mathematical audit

## correctness

PASS

Under the stipulated biased nearest-neighbor mutation and finite equal-mortality set, irreducibility of the stationary equation makes a nonzero nonnegative solution positive. Summing it gives tm=m−(1−d)sum_S x, hence 0<t=λ(1−m)<1. The ℓ¹ Neumann inverse on this range reduces the equation to the finite Green principal matrix, and positivity and strict increase of its Perron root give precisely one root below 1 iff d<d_*(S). At the endpoint the Green entries are δ⁻¹ times 1 for i≥j or (q/p)^(j−i) otherwise; conjugation by diag(s^(−a_i)) gives the similarity with symmetric K_S/δ. The resolvent reconstructs the unique normalized profile, and its required mass 1−t/λ is positive precisely for λ>t. Strict Perron comparison proves unique optimal clustering; principal submatrix monotonicity is strict (extending the positive eigenvector by zero cannot be a top eigenvector of the larger positive matrix). Finite row sums are strictly below the infinite geometric sum. Independently, the cosine profile cos((i−(k+1)/2)θ) is positive for θ∈(0,π/k) and the ghost condition yields tan(kθ/2)tan(θ/2)=(1−s)/(1+s), equivalent to the displayed quantization. With θ=π/k+O(k⁻²), the mortality deficit is exactly 2sδ(1−cos θ)/(1−s²), giving π²√(pq)/k² to leading order. As d approaches threshold from below, t→1 and the normalized favorable-site mass tends to zero. The endpoint Green formula is summable uniformly in t≤1 on every left half-line j≤J for each source in S, proving directed escape, not equilibrium at equality. In the two-site example the threshold condition reduces to 3^(−L/2)>1/4; for L=1 the symmetric off-diagonal Green factor is 1/2 at the root, giving t=8/(5√3) and the recorded mass. Replay: RESULT.md lines 35–100; VERIFICATION.md and checker.py inspected without executing. Finite recorded tests are supplementary.

## originality

PASS

The general equation, finite-rank resolvent reduction and block matrix are known; another catalogue result proves a related qualitative escape effect. The distinct contribution supported by the inspected material is the exact finite-pattern boundary, its strict optimization with a sharp block correction, and positive-total-mass escape when mortality approaches that boundary from below at fixed geometry and fixed λ>1. The block spectral step is not an independent new matrix theorem.

## value

PASS

The theorem gives an exact feasibility boundary for a natural deterministic model, distinguishes finite favorable geometries at fixed size, quantifies the finite-size gap to the infinite-block ceiling, and explains why positive total population in the parameter limit does not produce a stationary ℓ¹ limit. The global classification and escape law are useful beyond the illustrative example, without purporting to predict transient stability or stochastic survival.

The dated certificate retains the supplied scientific assessment, sources and limitations.
