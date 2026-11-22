# Scientific review: involution assignment shattering

## Correctness (C): PASS

The central hypothesis class is **all** self-inverse permutations on \([n]\), queried by ordered position–image cells. All-positive consistency excludes conflicting cycles, while two opposite orientations of one transposition are duplicate Boolean coordinates and therefore cannot both be shattered. The only remaining obstruction is a support that covers the entire vertex set and contains a fixed-point query: negating just that loop while making every other query positive leaves one vertex with no possible partner. In all other valid cases, negative fixed-point queries can be paired internally, using a globally unused vertex if their number is odd; other unspecified vertices can be fixed. This independently reconstructs the sufficiency witness and proves every Boolean labeling is realized. Exact orientation-counting gives the bivariate exponential generating function; the facet formula and top integral class follow from the explicit face structure; the random threshold follows from a sequential product and a uniform \(m/n\) diagonal-error bound.

The actual full trace checker exhausts every ordered query support of size at most \(n\) through \(n=5\), reproducing all coefficients and facet counts. No empirical result substitutes for the uniform proofs. The finite checker and its exact output are enclosed as separate files.

## Originality (O): PASS with historical risk

The complete relevant primary manuscript of Fang–Hamaker–Troyka (2020) concerns involution pattern avoidance and enumeration, not Boolean assignment traces; Bucić–Devlin–Hendon–Horne–Lund (2019) compare perfect-matching/derangement counts, not these shattered supports; Johnson–Wickes (2021) shatter permutations in the relative-order sense, not as binary matrix cells. A separate published derangement trace theorem concerns nonsymmetric fixed-point-free permutations and gives a different criterion and limit. Direct published-finding corpus queries against involution assignments, monomer–dimer loop complexes, and random thresholds returned that derangement theorem and unrelated involution results, not the exact claim here. Comparison is by implications, not merely titles. Symmetric duplicates, diagonal saturation, all facet sizes, a top homology class and the exponent \(2\) cannot be obtained by simply replacing a derangement hypothesis with its self-inverse subfamily. Indexing under symmetric matchings or loop complexes could conceal an equivalent; independent priority confirmation remains outstanding.

## Value (V): PASS

This is a natural, complete infinite-family classification for membership learning of symmetric permutation matrices. Fixed points and two-cycles form the canonical structural decomposition of involutions, and the obstruction arises precisely when every vertex is committed. The same one-line criterion determines all face counts, all facet cardinalities, the rank-one top integral homology and a sharp birthday-scale threshold. The factor-of-two difference from the unrestricted derangement sampling law isolates a concrete effect of symmetry on learning. None of these consequences is argued to follow from correctness or reproducibility alone.

## Scientific limits

Lower homology and full homotopy type are not classified. Theorem assumes unrestricted fixed points and two-cycles and a complete matrix-query board; arbitrary restrictions are not covered. The threshold is for uniformly sampled distinct query cells. The full historical literature cannot be certified exhaustively and no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
