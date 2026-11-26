# Independent mathematical audit

## correctness

PASS

All simple cycles of K_{2,n} use the two hubs and exactly two leaves. A directed cycle therefore occurs exactly when opposite hub-to-hub two-edge paths coexist. The endpoints differ on all edges, and flipping every a-edge then every b-edge avoids coexistence, so the distance is 2n and every minimizing path flips each edge exactly once. Open intervals for leaves have types determined by the first flip. Splitting an event order at every return to an empty open set yields unique monochromatic indecomposable blocks; a nonempty open set cannot change type in one step. For a prescribed type on m labeled leaves, (2m)!/2^m edge permutations obey the m disjoint precedence constraints. The EGF of a single indecomposable block is thus 1−1/S; a sequence of such blocks each with two types gives the formal EGF S/(2−S). Its coefficient comparison proves the recurrence and the arithmetic-operation bound, not a bit-complexity bound. For the asymptotic, Vandermonde bounds T_n=Σ s_k s_{n−k}/s_n by Σ 1/binom(n,k)=O(1/n) over 1≤k<n. The bound is below 1/2 for n≥7, and the direct ratios for n=2,…,6 are at most 1/2. The recurrence inductively yields 2s_n≤f_n≤4s_n and then 0≤f_n/s_n−2≤4T_n. The labeled count and uniform-order probability follow, with n=0 only a convention. A separate bounded subset-prefix DP reproduced the eight stated counts: extend a valid flip mask by any unused edge if the resulting mask has no opposite mixed leaf columns, summing predecessor counts from the empty mask. This tests finite instances only. The frozen BFS/DP code and its recorded log were inspected, not run.

## originality

PASS

The normalized sequence and recurrence are precisely known (OEIS A321628), and the distance and one-type factors are background. The supported distinct finding is that this sequence multiplied by n! enumerates the shortest paths for the specified graph endpoints, proved through the graph-specific busy-period bijection. No primary passage inspected identifies that geodesic invariant with the known coefficients. The sequence itself, its recurrence in isolation, and a new integer sequence are not credited as original.

## value

PASS

The number of optimal routes is distinct from their standard Hamming-length lower bound and from the orientation census. For a natural pair of opposite orientations, the bijection relates the reconfiguration obstruction to interval components, eliminates exponentially many graph states from exact counting, and estimates the viable fraction of edge orders. It is the graph interpretation and resulting exact path invariant, not recomputing a table, that carry value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
