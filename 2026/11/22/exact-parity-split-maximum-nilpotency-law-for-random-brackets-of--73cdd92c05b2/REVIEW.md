# Independent mathematical audit

## correctness

PASS

Reconstructing the path proof, every bracket entry at distance one vanishes, so consecutive steps in a nonzero product must jump at least two positions. At odd size 2h+1 the sole path of length h uses disjoint consecutive pairs of first-superdiagonal vectors; each determinant is nonzero with probability a=(1-q^(-2))(1-q^(-1)). At even size 2h, set m=h-1. The two all-length-two path products survive with union probability 2a^m-b_h: their intersection requires a first nonzero vector followed by 2m vectors outside the preceding span. The third entry is a sum of paths with a single length-three step at position j. Its coefficient is nonzero precisely when all earlier odd and all later even determinants survive. If the odd list is not wholly nonzero, partition on its first failure j; the earlier odd tests, the failed test, and the later even tests use disjoint vector pairs. This yields total activity a^m+m(1-a)a^(m-1). Given the first-superdiagonal vectors, each active third-diagonal entry is an independent linear functional of a disjoint pair of second-superdiagonal vectors. An active term's functional is zero exactly when both odd endpoint vectors are zero. These two zeros force failure of both central determinants and exclude every other active index. The disjoint exceptional events thus remove m q^(-4)a^(m-1). Either all-short path surviving implies there is an active nondegenerate functional (use the last odd or first even position). Outside that union, the remaining entry is uniform exactly on the nondegenerate activity event and otherwise identically zero. This proves the stated even probability. All arguments are finite-field arguments, including in characteristic two; the index bound is attained with positive probability. The ratio divides by a^(h-1), and b_h/a^(h-1) decays at geometric base q/(q+1), leaving the stated positive linear coefficient. Independently enumerating all pairs of n=4 matrices by their six strictly upper entries and calculating XY-YX entry by entry gave 3072/4096 and 489888/531441 nonzero brackets for q=2 and q=3; a nonzero bracket at n=4 has index two. This is bounded corroboration, not a proof for general q. The supplied code and recorded checks were inspected without executing the supplied code.

## originality

PASS

The all-dimension additive-bracket law, especially its even-dimensional exceptional term and resulting comparison with odds, is the distinct contribution supported by the inspected evidence. The n=4 case is already covered by an exact bracket-fiber count, and the parity phenomenon itself has a very close strict-radical product analogue. Neither is credited as independently new here.

## value

PASS

Maximal Jordan-block attainment is a natural extremal statistic for a nonuniform Lie-bracket distribution. The all-dimension answer is useful beyond the small zero-fiber case and exhibits a sharp parity contrast in consecutive dimensions with equal attainable index. The even formula resolves overlapping determinant tests and an exact characteristic-independent degeneracy correction rather than transferring the known product parity phenomenon by analogy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
