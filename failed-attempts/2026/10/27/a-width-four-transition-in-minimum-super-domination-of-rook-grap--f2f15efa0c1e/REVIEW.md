# Independent mathematical audit

## correctness

PASS

For a witness outside T in the same row as a target, its omitted-neighbor set is the disjoint union of omitted cells in its row and column, so its row must have degree one and its column zero; the transposed condition is analogous. If a part has no empty line, the other must and the omitted cells form the corresponding nonsurjective transversal. With both kinds of empty lines, every incidence edge has a degree-one endpoint, so the graph is a star forest. One-sided centers give strictly fewer than q edges in this case. For a row-centered and a column-centered component, at least two stars and two isolates are required, giving at most p+q−4 edges; equality saturates both sides with exactly two components, opposite nontrivial centers, and one isolate each. At p=4 both bounds tie; outside the tie the larger bound determines the optimum. Inclusion–exclusion counts the nonsurjective maps, and each crossed-star configuration uniquely determines its two centers and two isolates. The families are disjoint. Independent direct adjacency tests of the optimum and next size ran on 2×2, 2×6, 3×3, 3×5, 4×4 and 5×5, matching all corresponding families and counts. Downward closure in T excludes larger complements when the next size is infeasible. Replay: python /workspace/review_checks/rook.py 2x2 2x6 3x3 3x5 4x4 5x5. The frozen output and code were inspected, not rerun; finite results corroborate, not replace, the proof.

## originality

FAIL

A distinct indexed result covers the count by its full labeled omission polynomial and directly covers the stable crossed-star classification. Its all-size characterization and extremal proof also mechanically give the remaining boundary classification: the two nonsurjective-function families occur at the stated sizes, a single star with both kinds of isolates is too small, and two saturated components at width four force precisely the crossed stars. This is coverage of mathematical content; it does not establish that the later-dated indexed record predates this record or settle priority.

## value

FAIL

Optimizer growth at a sharp finite width is a natural question, but no independent scientific increment remains relative to the exact all-size partition and stable equality proof. The tied width-four geometry and resulting formula are immediate size comparisons and extraction from that result, rather than a new motivated invariant or structural lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
