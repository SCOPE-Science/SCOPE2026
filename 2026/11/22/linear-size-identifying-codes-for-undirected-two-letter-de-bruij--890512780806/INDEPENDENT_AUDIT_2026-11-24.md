# Independent mathematical audit

## correctness

PASS

The frozen numerical claims were true, but three were already tabulated. Re-audited repair: the two overlaps plus the vertex itself give R_b union K_a union own membership, even for diagonal words. With fewer than q sensors, two empty rows require at least one sensor for each of q disjoint paired vertices, and the column argument is symmetric. Thus there would be one empty row r and one empty column c, and singletons otherwise. Domination forces (c,r), so c differs from r. Another sensor (i,j) then gives identical singleton signatures at (j,r) and (c,i): their own membership is excluded by the occupied column r and row c respectively. This proves the lower bound; a separate incidence count using at most |C| singletons and at most 2q signatures per sensor also gives q by rounding. Direct recalculation gave all three published template masks and no collisions over 4895 vertices for q=3,...,24. The proof for all q is not an extrapolation: with two blocks, both nonempty supports recover the blocks, the ordered case is injective by disjoint rows/columns, and the reversed order would force row-column equality in a triple, impossible. Counting the pairs yields q+floor(q/3) in all residues; generating each pair in the chosen labeling is unit word work. A separate exact neighborhood/difference hitting-set enumeration found no size-q codes among 84, 1820 and 53130 codes respectively and found size-(q+1) codes in each case. This corroborates prior table entries, not new minima.

## originality

PASS

Frozen originality FAIL in part: the unsupported treatment of gamma(3)=4, gamma(4)=5, gamma(5)=6 as sharp new cases contradicts the original Horan–Adachi–Bak tables. The repaired claim removes these from the Finding and names them as prior benchmarks only. The counting lower bound is baseline, not a novelty claim. The surviving claim is the uniform family with a linear-time code of size q+floor(q/3) and its resulting explicit 4/3 guarantee. No inspected exact source states or mechanically implies this construction or guarantee.

## value

PASS

The repaired result supplies a scalable explicit design for the undirected problem that Horan identified, selecting O(q) vertices in a q^2-vertex graph with a guaranteed ratio to optimum. It is the cross-block separation enabling a simple code listing without a graph-size solver that adds value beyond computing familiar small optima. The known minima are only context and finite checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
