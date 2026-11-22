# Independent mathematical audit

## correctness

PASS

Reconstructed assigned RESULT.md for λ>1, 0<γ<1, βγK=1, c≥0, K=λ−1. The actual Jacobian at (K,0) has multipliers 1/λ and 1 with center tangent h_1=-λγ. Independent SymPy Taylor expansion of the original map and invariant graph verifies h_2=-λ²γ²/K at c_*=1/2+λγ/K; quadratic reduced drift c−c_*; cubic drift exactly −b where b=1/3+λγ/K+2(λγ/K)^2>0. For c<c_* monotone small positive center trajectories have 1/y_{n+1}−1/y_n=(c_*-c)+O(y_n), giving n y_n→1/(c_*-c); at equality 1/y_{n+1}²−1/y_n²=2b+O(y_n), giving sqrt(n)y_n→1/sqrt(2b). y=0 is the invariant strong-stable line, so each sufficiently near positive orbit has a positive center projection and exponential tracking, giving identical limits; h_1 transfers prey deficits. A fresh independent direct fixed-point scalar residual verifies y²[δ−b y+O(δy+y²)]=0, so yδ=δ/b+O(δ²), xδ=K−λγδ/b+O(δ²). Center multiplier 1−δ²/b+O(δ³) and transverse 1/λ+O(δ) imply local asymptotic stability. Numerical checks of original maps across 3 parameter pairs and finite n=300000 corroborated relative amplitudes within 0.4%, and three δ=.001 positive fixed points with the exact scalar equations. Bounded calculations corroborate, do not prove, the universal theorem. Scope local only, no global claim.

## originality

PASS

Best-of-knowledge originality PASS: the exact 2023 normalized recurrence and the numerical/analytic cooperation cutoff are preexisting and explicitly credited, so neither is claimed new. The surviving contribution is the computed model-specific strictly negative cubic center coefficient at R=1,c=c_*, the exact 1/n versus 1/sqrt(n) local extinction amplitudes and asymptotically stable positive branch slope δ/b. Jang–Yousef Theorem 2.4 gives fixed-point nonexistence at the cutoff but no critical polynomial time law. Published same-model Resultary finding requires R<1 and does not classify this boundary; no-refuge and continuous-time cubic works have different equations and cannot imply these amplitudes. Searches are bounded, not proof of absolute novelty.

## value

PASS

The critical predator reproduction boundary R=1 is a natural ecological bifurcation where linearization is inconclusive, while the cooperation threshold c_* is independently motivated by the published equilibrium-count boundary. Its codimension-two coincidence cancels the generic quadratic restoring term, changing a well-defined extinction-time invariant from a universal 1/n amplitude to a 1/sqrt(n) amplitude and birthing a stable positive equilibrium at calculable slope. The exact b>0, rate amplitudes and stable-branch normal form are nontrivial model-specific quantities not implied by equilibrium existence alone; a future analyst of critical demographic persistence can use them. Claims correctly remain local, not global or stochastic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
