# Independent mathematical audit

## correctness

PASS

Three disjoint rail routes force one selected vertex per row in a minimum cut and an internal column attains size three. A gap of at least two columns between adjacent-row selections admits a two-rail detour; differences of at most one give a left/right partition with no surviving crossing edge. Legal slides are one-coordinate unit steps. The coordinatewise meet is feasible; for comparable states, increasing a least current coordinate among those still below target cannot be blocked by a smaller coordinate, since such a tight blocker would itself have to increase for the target to be feasible. Thus paths via the meet attain L1. Each central layer has 12 edges and its next interface 4. In target layer q the worst distance is 2+|i-q|+|j-q|+|k-q|, convex in q, so only the two endpoint layers are needed. The radius lower bound comes from the sum of the endpoint distances and is attained by the stated parity-dependent central states; the two extreme triples attain diameter 3n−5, including n=3. The proof is for all n≥3. Independent bounded check: python /workspace/branches/grid_independent.py, exhaustive two- and three-vertex deletions, original-grid slides and all-pairs Floyd–Warshall for n=3,…,10. Frozen scripts and recorded output were inspected, not executed.

## originality

PASS

Qualified to the full quantitative slide geometry of this specific three-rail family. The coordinate constraints overlap strongly with two same-day records, and the Manhattan metric conditional on reachability specializes the general canonical-path theorem. Neither point is a new method. The combination of unrestricted all-pairs reachability and explicit slide order, size, eccentricities, radius and diameter was not covered by the inspected results.

## value

PASS

The thin rectangular network is a natural smallest setting with three disjoint rail routes. Its exact state count and slide geometry distinguish feasibility, travel cost and central configurations under optimum preservation, giving a uniform sharp benchmark rather than a list of verified examples or a general algorithm evaluated at one size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
