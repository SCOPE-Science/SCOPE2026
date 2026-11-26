# Independent mathematical audit

## correctness

PASS

For a specified triangle, its three vertices contribute no leaves; the other n−3 vertices each have an n−1 edge star disjoint from the triangle. Given the triangle, sampling m−3 of the M−3 remaining edges gives the leaf probability by requiring one selected and n−2 unselected star edges. Dividing by the unconditioned leaf probability leaves the factor (m−3)/m times (M)_{n−1}/(M−3)_{n−1}; the outside-vertex fraction (n−3)/n then reduces the latter factor to Q_n in the result. Summing over triangle indicators gives the covariance. Its bracket is increasing, with real zero strictly between n and n+1 for n≥5 and at 15/4 for n=4. The excluded strata have no leaves or no triangles, and for n≤3 the fixed-edge triangle count is deterministic. For independent edges, only the three triangle vertices' leaf probabilities change under conditioning, yielding the negative factor −3/n. For m/n→c, the absent-edge product in the leaf expectation tends to exp(−2c), giving E L∼2cn exp(−2c), while E T→4c³/3 and the rescaled bracket n[Q_n(1−3/m)−1]→3−3/c; the product also gives the zero limit at c=1. The supplied enumeration code and captured output were inspected, not run; the argument does not depend on the finite checks.

## originality

FAIL

The distinct indexed SCOPE leaf–motif theorem 81c56545debd already gives this exact result at the motif K₃, including the finite fixed-edge expression and integer sign change, the negative independent-edge expression, and the sparse limit. Differences from degree-count CLTs, isolated-edge counting, and ordinary subgraph covariance do not distinguish the result from that exact coverage. This is a statement-level coverage finding, not a claim about discovery order.

## value

PASS

The finite sign split and the sparse coefficient quantify how conditioning on the edge count changes dependence between a local degree observable and a motif count. The threshold is informative beyond an isolated numerical witness; the failure is that the statement is already covered, not that the mathematical phenomenon is of no interest.

The dated certificate retains the supplied scientific assessment, sources and limitations.
