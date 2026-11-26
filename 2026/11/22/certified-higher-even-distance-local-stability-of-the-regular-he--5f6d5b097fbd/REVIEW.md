# Independent mathematical audit

## correctness

PASS

Fixing labeled vertices 0 and 3 eliminates exactly translations, rotation and positive scaling; each sufficiently close strictly convex hexagon has a unique direct-similarity representative with these vertices fixed. For T(u,v)=(u/2,sqrt(3)v/2), the distance scaling and both area Jacobians give the factor 3^(-m/2) multiplying J_m/A^(m+2). The origin remains inside, so the oriented triangular moment formula integrates the relevant polynomial exactly by the simplex beta integral. Dihedral symmetry followed by scale invariance implies stationarity; the verifier also checks it rationally. Differentiating the quotient at stationarity gives the stated K_m with coefficient b(1-b) on the area-gradient outer product. Inspection of verify.py confirmed the binomial convolution and differentiation, including doubling the diagonal quadratic coefficients. A separate Fraction check, without executing the submitted scripts, certified 72 positive pivots across all nine stored symmetric matrices, matching the listed pivots and reconstructing 576 entries. The submitted reconstruction from moments is checked by source inspection; the independent factorization alone does not check that derivation. A positive Hessian and Taylor's theorem yield strict minimality on the slice and equality only up to direct similarity in the stated neighborhood.

## originality

PASS

The Hessian signs for precisely these parameters are already numerical observations of Bogosel–Bucur–Fragalà. What survives as distinct is the exact proof for arbitrary vertex variations of the hexagon at k=8,10,...,24. The close exact catalogue results concern k=6 for the hexagon or a different number of vertices. This is a statement-level comparison, not a historical-priority guarantee.

## value

PASS

This rigorously settles the nine higher-even hexagon cases in the window actually tested by BBF. The unresolved distinction was whether the smallest transverse eigenvalue was genuinely positive in every vertex direction, not merely in a symmetry-restricted model or numerical experiment. The exact finite family is useful independently of the global Riesz optimization problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
