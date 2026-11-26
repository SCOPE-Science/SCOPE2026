# Independent mathematical audit

## correctness

PASS

For two vertices in row i, their closed-neighborhood symmetric difference consists exactly of their two columns off row i, so at most one column can have all its selected cells confined to row i. The transposed condition is necessary and sufficient for the other adjacent pairs; non-domination requires an empty row and an empty column. With an empty column, every other column must have at least two selected cells, giving the strict bound 2(l−1)>2l−s; with no empty column the singleton columns have distinct occupied rows and at most s of them exist. Equality in 2l−s forces exactly one singleton per row and double occupancy elsewhere. Every template meets both adjacency conditions and dominates, and its row-to-singleton injection is unique, giving the stated labelled product count. For nonadjacent vertices with equal traces, each row's singleton must appear in the other trace, forcing the crossed singleton positions. Their traces agree exactly when neither row is touched by a double column. Inclusion-exclusion therefore counts both full coverage and coverage with exactly one untouched row. At q=l−s=0 no code is globally identifying for s≥3. For q>0 the threshold 2q≥s−1 is sufficient by taking disjoint pairs until at most one row remains, using one further pair if necessary and repetitions for surplus columns; it is necessary by capacity. Inspected VERIFICATION.md, CHECKS.txt, the two C++ verifiers and the Python occupancy verifier without executing them; finite checks corroborate both the unrestricted minimum proof and global-subcount reasoning, without exhausting larger boards.

## originality

PASS

The credited contribution is the exact local-minimum family for all labelled rectangles and its two counts. The ordinary-identification criterion on these templates is an instance of established line-graph results, and the ordinary transition agrees with (and given the local minimum follows from) the previously reported ordinary size formula; neither is credited as a separate novelty. The strongest inspected prior sources do not determine the local extremizers or produce the count over that family.

## value

PASS

Local identification on a natural graph family can behave quite differently from ordinary identification. The proof explains exactly how the local optimum avoids ordinary constraints, and the exact two counts quantify that gap across every labelled rectangle, not just a numerical coincidence or a few boards. Inclusion-exclusion in isolation is routine; the useful result is the exhaustive minimum family to which it applies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
