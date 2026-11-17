# Independent mathematical audit

## correctness

PASS

The discrete harmonic stencil identity A_n b=L e_1+R e_n gives A_n K_k=span{L e_j+R e_(n+1-j):1<=j<=k} through floor(n/2); these vectors have disjoint two-coordinate supports. Orthogonal residual projection yields the center sum plus ((R^2-L^2)^2/((L^2+R^2)(n+1)^2))*sum_(j<=k)j^2. Dirichlet sine eigenpairs have nonzero coefficients precisely on odd/even modes determined by L+(-1)^(s+1)R, yielding grades n,ceil(n/2),floor(n/2). For constant forcing the remaining squared residual is max(n-2k,0); for ramp forcing the Krylov image successively removes last coordinates, giving exact sums of squares and relative tolerance limits. Source RESULT.md theorem/proof read; independent rational Gram projections passed 380 cases. No finite check is claimed to prove arbitrary n, preconditioned or floating-point behavior.

## originality

PASS

Best-of-knowledge PASS. The exact complete two-parameter affine-harmonic right-hand-side residual profile, parity-sensitive relative Krylov grade and two exact tolerance limits are not implied by the full or relevant sections inspected of the older tridiagonal Toeplitz GMRES literature. The most directly related 2026 Chen-Soodhalter source emphasizes non-Hermitian constrained attainable curves; its complete v3 text was not accessible, creating a material priority risk, not an automatic scientific failure.

## value

PASS

PASS: discrete harmonic RHS data form the canonical two-parameter boundary-value family for a one-dimensional Dirichlet Poisson stencil; exact residual curves distinguish mesh-scale solver behavior on the same SPD operator with constant versus ramp data. The result is a natural exact numerical linear-algebra invariant, not a single arbitrary RHS run.

The dated certificate retains the supplied scientific assessment, sources and limitations.
