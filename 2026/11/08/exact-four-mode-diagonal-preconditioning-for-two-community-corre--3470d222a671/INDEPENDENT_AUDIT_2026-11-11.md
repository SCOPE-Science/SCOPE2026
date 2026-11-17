# Independent mathematical audit

## correctness

PASS

For SPD A with m,n>=2,0<u,v<1,g>0 and Delta=mng^2<alpha beta, condition-number feasibility kappa(DAD)<=K is equivalent to the affine SDP W <= A <= K W with W positive diagonal. Averaging feasible W over within-community permutations proves unrestricted diagonal optimum is achieved by D=diag(sqrt(x)I_m,I_n). In-group contrast eigenvalues ax,b and 2x2 quotient eigenvalues lambda_±(x) give kappa(x)=max(lambda+/lambda-,lambda+/(ax),lambda+/b). The first decreases then increases at x0=beta/alpha; the latter two respectively decrease/increase, and cross at xc=b/a, so two constrained lower-mode collisions produce the stated clipped rational x*. Numerically independently optimized 80 random admissible cases over log x by bounded scalar minimization and matched the analytical formula. For m=n=2,u=3/10,v=3/5,g=1/2, exact x*=6/7 and eigenvalues 2/5,2/5,3/5,81/35 yield kappa=81/14. Local/numeric tests corroborate, not replace, the analytic SDP/spectral argument.

## originality

PASS

Existing general optimal diagonal preconditioning SDP characterizations and near-optimal algorithms do not display the specialized complete three-regime closed-form optimizer for two compound-symmetry communities. Resultary near neighbors treat one-hub, windmill, and different graph/community matrices. Kolotilina 2002 block-optimality and 2006 3x3 diagonal scaling pose real implied-prior risk, but only accessible descriptions were available; no demonstrated coverage of this m,n>=2 four-eigenmode exact clipped formula.

## value

PASS

An explicit globally optimal diagonal scaling for structured SPD correlation matrices is useful as an exact benchmark for general algorithms and reveals transitions where within-block fluctuation and global quotient eigenmodes determine optimality. It is a motivated natural structured family, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
