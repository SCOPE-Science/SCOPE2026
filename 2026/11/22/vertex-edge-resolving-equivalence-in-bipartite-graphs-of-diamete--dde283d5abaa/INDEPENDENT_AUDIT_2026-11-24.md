# Independent mathematical audit

## correctness

PASS

In a connected bipartite graph of diameter at most 3, distinct same-shore vertices are distance 2 and share a neighbor; opposite-shore distances are 1 for neighbors and 3 otherwise. Independently one can see the stronger identity D_E(ab,a′b′)=D_V(a,a′)∪D_V(b,b′) (use the empty mask for an unchanged endpoint). For a sensor on A, if it is a differing A-endpoint the edge containing it is uniquely at distance 0; if it is a common endpoint both edge distances are 0 and both B-endpoints are adjacent. Otherwise both A-endpoint distances are 2 and each edge distance is 1 or 2 according to B-endpoint adjacency, so the vertex-mask union matches. The B-sensor argument is the reflection. Thus each edge mask contains at least one actual same-shore vertex mask, and every same-shore vertex mask is realized by two edges through a common neighbor. Cross-shore vertex masks are all of V and hence redundant for nonnegative weights because at least one same-shore pair exists (n≥3); K₂ is correctly excluded. This proves every threshold and the full nonnegative fractional equivalence by monotonicity. Independent witness replay in python3 /workspace/independent_checks.py (section 5) gives diameter 4, the seven distinct edge signatures (0,1),(1,0),(1,1),(2,1),(2,0),(1,2),(0,2), and vertices 3 and 6 both at (2,2). This disproves a larger universal bound for equivalence of sets, not necessarily of scalar dimensions.

## originality

PASS

Qualified pass for the full diameter-at-most-three class, in particular the transfer for incomplete bipartite graphs of diameter three. The specialized mask and fractional-polytope reduction on complete bipartite graphs are already covered, as are scalar dimension equality there and edge-resolving enumerators for some restricted families. None of the inspected broader-looking statements supplies the two directions of all-mask constraint domination on the actual class.

## value

PASS

Equality of every nonnegative separation constraint system, rather than just two optimum counts, transfers all resolving sets, optimal weighted/fractional solutions, enumerators and multiple-separation thresholds across a natural class including nontrivial design incidence graphs. The verified diameter-four example delimits that transfer. It is neither a scalar coincidence nor a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
