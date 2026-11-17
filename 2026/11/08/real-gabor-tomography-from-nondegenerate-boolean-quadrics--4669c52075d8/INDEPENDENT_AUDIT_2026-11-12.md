# Independent mathematical audit

## correctness

PASS

For V=F_2^(2m), N=2^(2m), t=2^m (m>=2), the nondegenerate quadratic polar map is a bijection between coordinates and Walsh frequencies and yields Gauss transform ±t. Expanding g(x)g(x+a) gives A(a,b)=N/4[1_{b=0}+(-1)^Q(a)1_{b=L(a)}]+epsilon*t/4*(-1)^Q(z_b)[1+(-1)^(a·b)]. This formula gives one k=(N+epsilon*t)/2, 2(N-1) coefficients of magnitude lambda=(N+2epsilon*t)/4, (N-1)(N/2-1) of t/2, and N(N-1)/2 zeros. Real symmetric Weyl operators are exactly a·b=0; their output characters are orthogonal, so singular values are sqrt(N) times these magnitudes. Since t>=4 all symmetric coefficients are nonzero, giving maximal real-symmetric rank N(N+1)/2 and positive condition number t+epsilon; skew-symmetric matrices exhaust the complex-linear kernel. Real rank-one phase retrieval is injective up to sign via ff^T=hh^T. Independently enumerating all 256 coefficients at m=2 yielded ε=+1 magnitudes {10:1,6:30,2:105,0:120}, ε=-1 magnitudes {6:1,2:135,0:120}; this checks the coincident levels case but does not prove all m.

## originality

PASS

Bojarovska–Flinth 2015 Theorems 2.2–2.3, directly inspected in arXiv PDF, give complex Gabor phase retrieval and frame bounds when every Weyl ambiguity coefficient is nonzero. For real windows over F_2^n, every skew Weyl index vanishes necessarily, so that condition cannot apply. The published SCOPE scalar Boolean quadratic GRAPH window theorem concerns indicator of {(x,Q(x))} in one extra group coordinate, not indicator of the ZERO-LEVEL SET {x:Q(x)=0}; its rank is generally much less than full real-symmetric rank. The new statement is the exact all-m zero-set signed ambiguity spectrum and Gauss-sign conditioning; Gauss sums and bent difference-set parameters alone do not specify these operator singular-level counts.

## value

PASS

Structured real phase-retrieval windows with provably maximal symmetric-matrix tomography rank and exact worst-case conditioning are natural and useful in finite harmonic analysis. The result identifies both Arf-sign classes, complete singular multiplicities and a uniform sharp stability ratio. It is not merely a generic rank existence result or a relabeling of the published quadratic-graph measurement problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
