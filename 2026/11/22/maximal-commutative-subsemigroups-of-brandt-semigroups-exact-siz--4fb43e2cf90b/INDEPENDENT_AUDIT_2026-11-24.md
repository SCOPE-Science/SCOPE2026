# Independent mathematical audit

## correctness

PASS

A composable pair of off-diagonal triples either has unequal zero/nonzero products or has nonzero diagonal products at different indices. Thus the source and target sets are disjoint; the full block between them can be adjoined without changing commutativity or closure. Each unused index must be filled by an actual maximal abelian subgroup. Conversely a new edge either touches an occupied diagonal, composes with an existing edge, or already lies in the full block. A missing diagonal label at an occupied index cannot commute with the whole maximal abelian subgroup, as it would generate a larger abelian subgroup with it. The recovered coordinates give the weighted polynomial by multinomial counting, and missing-color inclusion–exclusion gives the total. Writing f(k)=floor(k^2/4), the increments f(k)-f(k-1)=floor(k/2) show f(n)-f(n-d)>d when n>=4 and 2<=n-d<n; f(n)>=n and a balanced no-diagonal rectangle attains the bound. Listing the rectangular and diagonal choices gives the n=1,2,3 exceptions. In the uniform coloring model the missing-color probability and the extra diagonal fraction decay exponentially (it is the failure of the conditioning event that is rare). Expanding A_n B_n around (np,np) leaves p(A_n+B_n-2np)/sqrt(n) after normalization, since the cross term is O_P(n) and the diagonal contribution O(n) for fixed G. The binomial variance for A_n+B_n gives 2p^3(1-2p). The ten recorded cases are finite; the independently written /workspace/branches/independent-finite-checks.py found all 18 families and spectrum {5:9,6:6,7:3} in B_2(S_3).

## originality

PASS

The abstract groups-plus-annihilators decomposition already occurs in the Brandt and completely zero-simple divisor results. The supported distinct claim is the full fixed-host classification with actual maximal abelian subgroups of G, and its weighted census and fixed-G limit law. The inspected antecedents do not supply the saturation and counting of these embedded subsets.

## value

PASS

A complete labeled size spectrum of maximal commuting families in a natural inverse semigroup is useful beyond a maximum or an abstract structural description. The polynomial isolates precisely which group data are needed. For fixed G the Gaussian law distinguishes the typical quadratic scale from the larger balanced-rectangle extremum, and treats abelian and nonabelian groups by the same encoding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
