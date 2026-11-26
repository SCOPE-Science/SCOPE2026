# Independent mathematical audit

## correctness

PASS

For a support S in a size-k ideal layer, comparability obstructs shattering, and the all-positive and all-negative traces force |D(S)|≤k≤mn−|U(S)|. For an antichain these bounds suffice: the ideals forcing the positive and negative labels of any trace give nested lower and upper ideals bracketing k, and one can extend by minimal elements of their difference to exactly k. For |S|=m−1, cells incomparable to all queries lie in the one missing row and in unused columns, hence number at most m−1. Since D∩U=S, feasibility forces exactly m−1 incomparable cells and k=|D|. All unused columns must then lie in the one open gap in the missing row. Strict decrease forces the queried columns above the gap to be the largest h−1 and those below to be the smallest m−h. Summing down-closure widths gives m(m+1)/2−1 at h=1; advancing h replaces one row width by a width larger by m−1 and decreases the next width by one, giving the step m−2 (including a terminal zero width). For |S|=m the incomparable set is empty and the closure bounds contradict each other. This covers the extreme missing rows, m=3, the empty and full layer ranks, and uniqueness. Independent direct projections of partitions encoded by lattice paths at m=3,4,5 tested 19,307 support-rank pairs; the exceptional ranks and unique supports matched exactly.

## originality

PASS

Credit the fixed-rank finite-poset trace test as background. The supported distinct result is the rectangle-specific equality case, which yields m isolated feasible ranks with exactly one size-(m−1) support at each and no support of size m at any rank. The closest square-board theorem shares the trace test but not this equality case.

## value

PASS

The board shape is a critical boundary: the number of unused columns at support size m−1 is exactly the number of incomparable cells needed for any feasible rank. At that boundary the exact unique-support progression shows repeated loss and recovery of the top shattering dimension, notwithstanding unimodal counts of all ideals. This supplies an all-size structural example, rather than a single-parameter tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
