# Independent mathematical audit

## correctness

PASS

Every labelled incidence vector is an extreme point since a convex combination representing a binary vector must agree in every coordinate. For compatible e=(i,j), f=(k,l), there are (n-2)^2 remaining positions; the forbidden diagonal contributes n-4+[i=l]+[j=k]. This yields the pair-completion count D-[i=l]-[j=k], with both indicators counted on reciprocal pairs. Summing over ordered compatible pairs and dividing by six gives T; inclusion–exclusion on the forbidden diagonal also gives this T. Edge transitivity gives p=3/m. On a matrix x, writing S for its total and r,c for its row and column sums, the uncorrected compatibility sum is S-r_i-c_j+x_ij and the indicator correction is c_i+r_j. Thus the covariance operator has the stated actions on constants, symmetric and antisymmetric potentials, and zero row/column sums. These subspaces are orthogonal and exhaustive: the row/column-sum constraints have one redundancy because the crown graph is connected. The exact gap formulas and factorization 2T lambda_minus=(n-3)(n-2)(D-1) prove positivity and ordering for n>=4 and give the stated ratio. Its strict decrease and asymptotic follow from that rational function. For n=3 the two matchings of C6 are disjoint, and the squared difference of their incidence vectors is six, giving rank one and eigenvalue 3/2. Independent exact moment and rank calculations agreed at n=4,5,6.

## originality

PASS

The rook count, underlying fixed-cardinality polytope and symmetry methods are established. The closest indexed spectra use a different board or a different sampling law, and crown line-graph spectral results use a different matrix even on the same coordinate set. The supported distinct claim is the fixed-three crown covariance with its three positive levels and exact condition ratio, not the rook count or a general polytope construction.

## value

PASS

The crown board is a canonical symmetric deletion from the complete assignment board. The smallest and largest positive eigenvalues capture how this deletion affects intrinsic directional variance at fixed size. The exact formula gives a full-dimensional tangent covariance for n>=4, contrasts with the rank collapse at n=3, and quantifies approach to isotropy through a condition number that drops from 5 to 1+2/n+O(n^-2). The split row/column potential modes, their ranks and the exact rate make this an interpretable family invariant rather than a routine count of three rook placements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
