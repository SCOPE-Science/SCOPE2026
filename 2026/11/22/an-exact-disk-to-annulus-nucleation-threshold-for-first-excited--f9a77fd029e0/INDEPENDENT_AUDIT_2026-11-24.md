# Independent mathematical audit

## correctness

PASS

Abreu–Speckbacher Proposition 1, Eqs. (19)–(21), gives the unit-normalized self-transform by taking w=i in the kernel and removing its α/(4π) normalization, or directly by (21). The degree-one Jacobi polynomial gives 1−(α+2)u; the squared radial amplitude is (1−u)^(α+1) times its square. The Cayley area element integrates to 4π du/(1−u)²; differentiation of J_α and its endpoints verify the total energy 4π/α and the normalized mass. The derivative has exactly the stated inner zero node and outer nondegenerate maximum; the outer height bound is strictly below one. Strict superlevel area is continuous and strictly decreasing from infinite area to zero, and null level circles make the bathtub comparison unique even for fractional masks. The derivative of the optimal mass is the normalized common boundary level. For level deficit η, the two outer roots separate by 2√(2η/k_α)+O(η), weighted by 4π/(1−u_p)² in area; the inner displacement is η/|f'_α(u_*)|+O(η²). This gives the stated coefficients. Using √η as a smooth right-hand parameter yields zero right curvature, while the inner derivative is strictly negative on the left. At α→0 the limiting inner root is 1/3; at α→∞ uniform convergence in v=αu on [0,1] and strict monotonicity of e^(−v)(1−v)² give the claimed Lambert W root. At α=1 taking the positive square root on the inner branch gives the stated radicals. Read RESULT.md, VERIFICATION.md and check.py; the supplied finite script was inspected, not run. The analytic proof is decisive and does not extend to optimization over arbitrary input signals.

## originality

PASS

The response and normalizations are explicit specializations of prior Laguerre wavelet theory, and the bathtub principle is standard. The supported distinction is the complete topology, exact curvature change, birth laws, and parameter limits for the fixed first-excited self-response. The nearest optimized-signal Cauchy results concern a different window and a different optimization problem.

## value

PASS

The first nonanalytic Laguerre level is a natural setting to ask when a hyperbolic disk stops being optimal for a fixed state. The exact calculation answers that geometric question across all budgets: a second component appears with linear width while the old boundary shifts quadratically, and the optimal energy is not C². This supplies a quantitative boundary to disk optimality without overstating it as an operator-norm counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
