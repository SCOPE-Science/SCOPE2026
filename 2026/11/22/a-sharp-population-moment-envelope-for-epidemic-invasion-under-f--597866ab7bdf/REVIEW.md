# Independent mathematical audit

## correctness

PASS

For p_i>0 summing to one, ∑ᵢⱼpᵢpⱼaᵢⱼ=(1−e)+(e/s₂)∑pᵢ²=1 and the given closed e-interval is exactly entrywise admissibility. Dividing by c and conjugating with diag(√p) yields the symmetric nonnegative S(e)=uuᵀ+eB, u_i=√p_i, B=D/s₂−uuᵀ. Its Perron root is the largest algebraic eigenvalue even at the closed endpoints. The unit trial vector u has constant Rayleigh quotient one; at e≠0 it is a top eigenvector only if Bu=0, equivalently all p_i=s₂. For equal p, S(e)=uuᵀ+e(I−uuᵀ) and the top eigenvalue stays one. In the unequal case the unique minimum and convexity imply strict one-sided monotonicity; simple-eigenvalue perturbation at e=0 gives curvature coefficient ||Bu||²=s₃/s₂²−1>0, since the spectral gap is one and uᵀBu=0. On {u,w=Bu/√v}, the exact compression has diagonal (1,et) and off-diagonal e√v, with t=wᵀDw/s₂ equal to the displayed moment ratio. This gives the lower envelope. If the shares take two values, the span consists of class-constant functions after division by u, so Perron symmetry puts a leading vector in the span for e<1 (strictly positive off-diagonals), and at e=1 the vector on any largest-share class suffices. Conversely, a top Ritz vector at e≠0 must have a nonzero w coefficient and satisfy Dx in the span; divided by u this forces a genuinely quadratic polynomial to agree with a linear polynomial at every distinct share, impossible for three or more shares. With uniform shares the envelope formula is undefined rather than an extra equality case; with e=0 equality is automatic for all unequal shares. The exact two-group radicals and the resulting strict threshold comparisons agree. Sharpness is attainment by the stated equality class and not a claim of pointwise optimization over every fixed feasible moment triple. All conclusions are for the stipulated deterministic reduced matrix, not sparse finite-network outbreak probabilities or an intervention recommendation.

## originality

PASS

The two-community normalization and reproduction-number formula are already in Gupta–Landry; their equal-product specialization implies the two-community minimization. The weighted Rayleigh budget bound itself is elementary. A notably close Resultary two-rate theorem already develops the same two-class compression idea for reciprocal matrices at prescribed class row rates. The supported distinct result is the arbitrary-finite-share quantitative law along the fixed-global-budget affine family, especially the explicit (s₂,s₃,s₄) envelope and the strict necessity of at most two share values for equality at nonzero e. Neither the general variational machinery nor the inspected close statements settle this multi-valued moment and equality claim; best-of-knowledge only.

## value

PASS

Fixing population-wide activity is a natural comparison in the stated model and is not equivalent to fixing each community's degree. The elementary lower bound alone would have limited value. The small set of population moments instead yields a quantitative bound away from proportional mixing and an exact structural test for when it loses no information. Distinguishing the two-share configurations from all multi-valued ones is a useful sharp result beyond a two-group computation, while the model's deterministic scope limits extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
