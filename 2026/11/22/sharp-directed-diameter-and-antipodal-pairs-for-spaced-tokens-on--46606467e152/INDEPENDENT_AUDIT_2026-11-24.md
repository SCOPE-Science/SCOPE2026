# Independent mathematical audit

## correctness

PASS

Reassessed repairs/4/RESULT.md. With positive slack, route conservation fixes arc uses to p_j+c, with least nonnegative choice p_j−min p. A cut at a minimum orders the sources and targets with x_i≤y_i. The published comparable-lift descent from y to x reverses to a clockwise route, stays between the coordinate endpoints, and avoids the cut. The direct blocking argument also works: an unfinished token with next gap r forces its successor unfinished by the target constraint, including the lifted wrap, and complete blockage would require n=rk. The distance is thus Σ(y_i−x_i), and each difference is bounded by n−1−r(k−1). Equality forces both endpoint bounds for every i. Conversely the proposed packed pair satisfies x_i≤y_i in the displayed cut, so all prefixes are nonnegative and the cut really does minimize flow; the bound is attained. The unique widened gap in each packed source makes its rotation orbit free, giving exactly n ordered extremal pairs and a unique farthest target for each extremal source. The repair explicitly excludes the isolated n=rk branch from metric and diameter formulas. The counts follow from rooted gap compositions and subtracting one unit ahead of the moving token. Inspected the supplied BFS checker and its recorded 73 cases/1,896,844 ordered pairs; they are not a rerun, do not cover the frozen branch, and do not prove the unbounded result. Independently the (n,r,k)=(7,2,2) packed pair has prefix flow cost 8 and a legal eight-slide route.

## originality

PASS

Pass for the repaired diameter and ordered equality classification only. The frozen novelty distinction for the clockwise distance fails: it says the earlier undirected bounded-gap results do not imply the one-way distance, but the earlier proof's full one-unit descent lemma supplies exactly the monotone route after a cut. The repair credits that concrete implication, moves the metric and connectivity out of the claimed distinct extremal result, and retains the proof of the separate maximum and its equality cases. No verified comparator gives the same directed maximum and full family of ordered antipodes; the unavailable extended-particle full text remains a risk, not a verdict.

## value

PASS

The repaired claim gives the exact worst-case number of legal one-way hops for a natural exclusion graph and identifies every source and target attaining it. This structural eccentricity and antipode classification remains useful even once metric realizability is known: it describes which configurations force worst-case reconfiguration and proves there is only one farthest target per extremal source. It is not a mixing or stationary-current assertion, nor a rebranding of the transport-path lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
