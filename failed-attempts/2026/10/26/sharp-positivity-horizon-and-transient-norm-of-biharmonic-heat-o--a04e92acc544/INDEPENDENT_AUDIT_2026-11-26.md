# Independent mathematical audit

## correctness

PASS

The point incidence matrix satisfies BB^T=A+2I and B^TB=(n-2)I+J. Centering its columns gives an orthogonal projector with entries (|S intersection T|-4/n)/(n-2); the positive Laplacian eigenvalues are n and 2(n-1). The stated disjoint entry follows from the spectral exponential, and the adjacent entry is strictly positive because n-4>=0 and e^(-n^2 t)>e^(-4(n-1)^2 t) for t>0. The diagonal is positive, rows sum to one, and symmetry gives the equality of the absolute row and column norm maxima. There are (n-2)(n-3)/2 disjoint positions per row. F_n starts at zero, its derivative changes once from negative to positive at the stated theta_n, and its limit is n-2>0; hence it has precisely one positive zero. The norm strictly falls from the peak to that zero and is flat thereafter. The given sign datum is an infinity-norm extremizer; for the 1-norm a unit coordinate vector attains the maximal column sum. For the graph-size limits, scaling time by n^2 gives the limit (1-r)(1-r-r^2-r^3), r=e^(-s). Bracketing its unique positive-time sign change with compact uniform convergence pins down the scaled zero. Expanding the explicit peak gives the stated limit and coefficient. In the independent replay the first-size defect estimator at n=10^6 is 1.4040750649, consistent with coefficient 1.4040753446, and direct exponentials agree with the norm and sign formulas for n=4,6,7.

## originality

FAIL

The distinct indexed November 22 strongly regular graph theorem completely covers the finite-n result by exact substitution. It also gives the exact peak as a function of the graph parameters, and the large-n limit and first-order coefficient are direct evaluations/expansions of that expression; the printed coefficient need not be present verbatim for the coverage to be mechanical. There is no separate asymptotic obstruction or family structure in this claim not already determined by the explicit formula. This is current-catalogue coverage, not a claim that the later record anticipated the earlier dated frozen work.

## value

FAIL

The structural sharp cutoff and transient are mathematically meaningful, but already determined by the available strongly regular theorem. The remaining displayed coefficient is valuable as an illustrative comparison with rook graphs, not as an independent exact fact beyond the existing formula: it is its first elementary Taylor coefficient, with no new comparison inequality or nontrivial asymptotic step. The review identifies no distinct valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
