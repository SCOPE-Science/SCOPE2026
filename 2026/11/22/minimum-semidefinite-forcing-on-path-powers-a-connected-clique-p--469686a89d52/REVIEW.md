# Independent mathematical audit

## correctness

PASS

Fewer than k deleted positions cannot create a surviving-order gap greater than k, so there is just one white component; every blue vertex has at least two white neighbors. For a seed of size k, disconnected whites force all k deleted positions to be one consecutive internal gap. If whites are connected, a first forcer has one white neighbor and at most k−1 blue neighbors, hence degree at most k and must be an endpoint. This is the intended upper-bound argument in RESULT.md line 44 ('at least' should be 'at most'). Endpoint seeds fill a boundary interval and sweep across it. For an interior interval, the rightmost blue vertex can force the next left white vertex in its component, and the leftmost does the reverse; the enlarged blue interval sustains these moves. This proves the exact disjoint census L_i,R_j,C_a. Intersections of size k−1 give two K_k's and the consecutive internal path, with all terminal attachments, one extra attachment at each end when n≥k+3, and between-clique edges a matching, one bridge, or none. Counting these gives the three stated edge totals. The terminal path bounds all distances by n−k; the one-internal-node case is noncomplete, and for two internal nodes the nonexceptional left and right vertices have no common neighbor. For n≥k+4 the integer labels in RESULT.md line 56 are 1-Lipschitz on every listed edge and attain a gap n−k. Ordinary forcing permits only endpoint first moves, so its optimizers induce the asserted disconnected graph for n≥k+4. The independent sequential-force and exchange BFS replay matched every count, seed family and diameter on 36 parameter pairs (4≤n≤11, 2≤k≤n−2); this corroborates but does not replace the all-order proof.

## originality

PASS

The scalar PSD value follows from an earlier chordal corollary, and the explicit ordinary comparison is prior coverage; do not credit those as new. The contribution is the complete PSD minimum-set census and its exchange geometry for the full two-parameter family. Neither the earlier ordinary census nor the broader inspected PSD algorithm and scalar theorems give this result.

## value

PASS

The known scalar says how many blue vertices are needed but not where to place them or how to move between optimal placements. The exact PSD census turns interior graph separators into the configurations that connect two previously disjoint ordinary clusters. The derivation gives complete adjacency, boundary cases and a growing exact diameter over a naturally motivated unbounded family, not a routine calculation of Z_+.

The dated certificate retains the supplied scientific assessment, sources and limitations.
