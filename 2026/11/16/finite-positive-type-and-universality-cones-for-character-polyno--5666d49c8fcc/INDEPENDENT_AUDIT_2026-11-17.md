# Independent mathematical audit

## correctness

PASS

SU(2) Clebsch–Gordan product chi_j chi_k=sum chi_{j+k-2h} gives the exact coefficient C_n; for n>=d the sum is r^n((n+1)S+T), with the only candidate negative k index at n=d-1,j=d,h=0 contributing coefficient zero, extending affine tail to n=d-1. Algebraic elimination yields the claimed r^(n-d+1)C_(d-1)+(n-d+1)r^n S identity. Peter–Weyl/Bochner central positivity makes individual C_n nonnegative necessary and sufficient, and asymptotic n forces S>=0. The square coordinate map has trivial kernel: all C_n=0 implies P_r q_b=0; P_r>0 everywhere, so b=0. An atomic measure with finitely many nonzero Peter–Weyl blocks must equal a smooth Haar-density Fourier polynomial yet is singular unless zero, so strictly positive tails imply strict finite-site PD; the converse finite rank fails on large finite subsets. All strictly positive coefficients are exactly uniform RKHS universality. Independently checked rational identities for radii 1/2,2/3,3/5 and d=1..6 through n=d+14 with exact fractions. Read source su2_poisson_checker.py, confirming its separate formulas and boundary tests. This is all degrees, not finite extrapolation.

## originality

PASS

The published degree-two central SU(2) Abel-mask positivity cone gives exactly three inequalities and two vertices (d=2) but explicitly does not classify arbitrary mask degrees. The present all-degree affine tail and d+1-simplex theorem dominates it and is a nontrivial extension; its formulas can specialize to d=2 and are not claimed to be novel there. Said et al. and Azangulov et al. give general universality and spectral representation criteria without this explicit family-specific finite-cone classification.

## value

PASS

Finite positivity and universality tests for every character-polynomial degree replace infinitely many constraints with precisely d+1 independent facets, controlling strict/finite-rank/universal strata of a natural compact-group covariance kernel. This uniform all-degree structural result has clear use in harmonic-analysis kernel design; no broad theorem for other groups is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
