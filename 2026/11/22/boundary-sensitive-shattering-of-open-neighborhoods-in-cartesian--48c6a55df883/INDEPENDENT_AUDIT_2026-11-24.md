# Independent mathematical audit

## correctness

PASS

Manhattan distance shows that distinct centers share at most two open neighbors; a trace on three elements of a hypothetical shattered four-set would contradict this when compared with the all-positive center. Every singleton has both labels. A pair is shattered exactly when it has a common center and each endpoint has a private center; a support vertex itself supplies the empty trace by bipartiteness. Straight distance-two pairs have just one common center, diagonal pairs two. This gives n-4 truncated at zero on a path, removes exactly four corner incidences for diagonal pairs in a rectangle (correcting the double subtraction of its two diagonals at 2 by 2), and leaves all distance-two pairs in d>=3. For triples, opposite neighbors on the same axis cannot be labeled positive without the third point. On three distinct axes the unique all-positive center, pairwise intermediate centers, and bipartiteness supply all but singleton traces. A singleton has a witness exactly when its chosen direction extends straight, or there is an unused direction on another axis. A fourth axis always works. In d=3 the numbers of interior axes h=3,2,1,0 give, respectively, 8 times the product, the sum of pairwise products, the sum of truncated (n_i-3), and the all-sides-at-least-3 indicator, using the interior counts (n_i-2). These counts imply the stated VC thresholds, including (2,2,3) and (2,2,4) on opposite sides of the threshold.

## originality

PASS

The distinct result is the exact support classification and coefficientwise boundary dependence for all Cartesian path boxes. The Hamming upper bound and the entire all-binary specialization are already covered and receive no originality credit. Inspected results on all boxes, convex sets and different neighborhood relations are not equivalent.

## value

PASS

The coefficients answer more than the scalar VC dimension: they locate and count every support. The private-witness criterion explains why three dimensions are genuinely boundary sensitive and why a fourth axis removes the obstruction; it decides concrete finite-box questions, such as the first cubic support appearing at 2 by 2 by 4 rather than 2 by 2 by 3. This is a structural and exact result for the natural finite induced-grid family, beyond the already known degree cap and binary counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
