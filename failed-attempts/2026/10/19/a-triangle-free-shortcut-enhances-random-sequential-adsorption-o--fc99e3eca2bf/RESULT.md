# A triangle-free shortcut enhances random sequential adsorption on almost every cycle

## Finding

For every integer \(N\ge5\), place a site-adsorption process on the simple cycle \(C_N\) with labeled vertices \(0,1,\ldots,N-1\). Give each vertex one independent continuous arrival priority, and accept it permanently precisely when neither of its neighbors has previously been accepted. Let \(J(G)\) denote the expected total number of accepted vertices on a finite graph \(G\). Let \(G_N=C_N+\{0,3\}\), where the extra edge joins two vertices of cycle distance three except for the smaller-cycle identifications.

**Theorem.** The expected jamming increment \(\Delta_N=J(G_N)-J(C_N)\) is strictly positive for \(N=6\) and all \(N\ge8\), while \(\Delta_5=\Delta_7=0\). In particular, adding a repulsive exclusion bond forming a four-cycle strictly **increases** the mean number of adsorbed particles for every sufficiently large cycle, and in fact for every \(N\ge8\). The smallest positive example is \(\Delta_6=1/9\). For every \(N\ge29\), the quantitative bound \(\Delta_N>0.0366\) holds.

## Assumptions and scope

The input is a labeled simple, unweighted, undirected graph. Each vertex is visited exactly once in a uniformly random permutation. An arriving vertex is occupied if no previously occupied vertex is adjacent to it; otherwise it is permanently rejected. This is **vertex** random sequential adsorption, or random-order greedy maximal independent-set construction, not edge/dimer adsorption. All arrival-priority distributions are independent and continuous and therefore induce the same uniform permutation. The added edge \(\{0,3\}\) is the shortest triangle-free chord for \(N\ge7\); for \(N=5,6\), the same labeled definition is used even though the shorter cycle distance differs.

Every claim concerns the *expectation* of jammed particle number; pathwise monotonicity, higher moments, and arbitrary chord positions are not asserted.

## Proof

**1. Exact expectation recurrence.** For any finite simple graph \(G\), write \(F(G)=J(G)\). Conditioning on the first arriving vertex, which is always accepted, gives
\[
F(\varnothing)=0,\qquad F(G)=1+\frac1{|V(G)|}\sum_{v\in V(G)}F(G-N_G[v]),
\]
where \(N_G[v]\) is the closed neighborhood and \(G-N_G[v]\) is the induced remaining graph. The recursion is an exact rational identity: after deleting the first vertex and its excluded neighbors, the remaining relative arrival order is uniform. It may equally be applied to any induced subgraph encoded as a vertex bitmask.

**2. Priority-path locality.** Couple adsorption on graphs differing only by the edge \(\{a,b\}\) using the same independent uniform priorities \(U_v\). If an occupied/rejected decision at vertex \(v\) differs, successive tracing to the earliest neighbor whose decision differs produces a strictly increasing-priority, self-avoiding path from either \(a\) or \(b\) to \(v\), in the graph *with* the extra edge. Every fixed path with \(\ell\) edges has probability \(1/(\ell+1)!\) of strictly increasing priorities. Independently, when passing from a full graph to an induced subgraph, a decision at \(v\) cannot change unless there is a strictly **decreasing**-priority self-avoiding path from \(v\) to a deleted vertex: follow recursively the earlier neighbors on which its decision depends.

For a cycle with one chord and its induced subgraphs, the only vertices of degree three are the two chord endpoints; all others have degree at most two. From an arbitrary starting vertex there are at most eight self-avoiding paths of any prescribed positive length, and from either chord endpoint at most six. (Before encountering either branching endpoint, the route is forced; each endpoint may be visited at most once.) The unchorded cycle has at most two paths of any prescribed length from a vertex.

Put \(T_k=\sum_{\ell=k}^\infty1/(\ell+1)!\) for nonnegative integers \(k\). The first path argument implies that the probability of a chord-induced decision change at a vertex at graph distance \(d\) from \(\{a,b\}\) is at most \(12T_d\). The expected number of changed decisions among *all* vertices at distance at least \(k\) is at most \(12T_k\), because paths may be counted over their endpoints. By the second path argument, deleting vertices at graph distance at least \(s\) from a given vertex can change either its chorded-graph or unchorded-graph decision with combined probability at most \(10T_s\).

**3. Exact 28-vertex local gadget and uniform error.** Let \(R=12\). Start from a path \(P_{28}\) with vertices \(0,\ldots,27\), and insert a chord between vertices \(12\) and \(15\). Write \(\delta_*\) for its expectation change. Repeated exact application of the recurrence in step 1 gives
\[
\delta_* = \frac{13738981531700639}{304554407185153125}>0.0451117.
\]
For every \(N\ge29\), the induced subgraph of \(C_N\) consisting of \(\{0,1,2,3\}\) and the first \(R\) vertices along each side of the longer arc between 0 and 3 is exactly \(P_{28}\), in an appropriate relabeling; the extra edge corresponds to \(\{12,15\}\). Call this induced vertex set \(H\). Each vertex in \(H\) has distance \(d\le R\) from the pair of chord endpoints, and there are at most four vertices at any such distance. Each vertex outside \(H\) is at distance at least \(R+1\). Also each vertex of \(H\) at distance \(d\) is at distance at least \(R-d+1\) from any excluded vertex.

Let \(D_v\in\{-1,0,1\}\) be the difference between its chorded and unchorded occupation indicators in the full graph, and \(D_v^H\) the analogous difference in the induced gadget. The event \(D_v\ne D_v^H\) requires both (i) some decision change caused by truncation and (ii) at least one of \(D_v,D_v^H\) to be nonzero. The two priority-path bounds give
\[
\Pr(D_v\ne D_v^H)\le\min\bigl\{10T_{R-d+1},\,24T_d\bigr\}.
\]
Since \(|D_v-D_v^H|\le2\), and the total expected absolute difference outside \(H\) is at most \(12T_{R+1}\), the global increment differs from the gadget increment by at most
\[
B_R=8\sum_{d=0}^{R}\min\bigl\{10T_{R-d+1},\,24T_d\bigr\}+12T_{R+1}.
\]
The factorial series can be bounded using rational arithmetic, and \(B_{12}<0.008501\). Hence for all \(N\ge29\),
\[
\Delta_N\ge\delta_*-B_{12}>0.0366107>0.0366.
\]

**4. Remaining finite sizes.** The same exact recurrence, applied independently to \(C_N\) and \(G_N\) for each \(5\le N\le28\), yields equality exactly at \(N=5,7\) and strictly positive differences at \(N=6\) and every \(8\le N\le28\). The entire bounded enumeration is recreated by the standalone script `verify_chord.py`; the program does rational arithmetic (not random simulation), reproduces the displayed gadget fraction, and confirms the finite signs. At \(N=5,6,7\), direct exhaustive permutation enumeration provides a second check independent of the first-vertex expectation recurrence. Together with step 3 this covers every claimed integer \(N\). \(\square\)

## Verification

Run `python3 verify_chord.py` with Python 3.9 or later and no nonstandard packages. It computes exact rational expectations, compares direct permutation enumerations for \(N=5,6,7\), evaluates the exact 28-vertex gadget, and bounds the infinite factorial remainder. The script reports the strict lower bound \(\delta_*-B_{12}\approx0.03661135\), the two exceptional small cycles, and strict positivity of every remaining finite size through 28. The analytic priority-path locality proof, not finite enumeration alone, handles all \(N\ge29\).

## Relationship to prior work

Pippenger's 1989 study analyzes random sequential adsorption on graphs, in particular sparse-cycle and regular settings; the available abstract singles out a short-cycle condition that each edge belongs to at most one cycle. The chorded cycle here has overlapping cycles, and the new result concerns an **order-one difference** caused by adding one nonlocal exclusion edge, not limiting per-vertex density. Dhara, van Leeuwaarden, and Mukherjee (first public arXiv version 2016-04-13) analyze generalized adsorption on random Erdős–Rényi graphs, not this fixed-graph defect comparison. Krivelevich, Mészáros, Michaeli, and Shikhelman present a general local-limit framework for normalized greedy occupancy; its local-limit statements alone do not determine the sign of an \(O(1)\) chord perturbation. Exact comparison searches have not identified a direct earlier statement of this all-size sign classification, but cannot guarantee priority.

## Limitations

The theorem is limited to random-order vertex adsorption and the single chord joining positions three edges apart. No claim is made about other chord distances, distributional stochastic domination, transient adsorption kinetics, or the large-\(N\) exact limit of \(\Delta_N\). The stabilizing comparison is deliberately quantitative but not sharp. The 1989 primary text could not be inspected in full under the available access and remains a bibliographic risk; the retrieved abstract and journal metadata do not establish that the whole paper excludes this result. No independent external validation has been performed.

## References

1. N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* 2 (1989), 393–401, DOI: 10.1137/0402034. Full article not accessed; abstract and publisher bibliographic page examined.
2. S. Dhara, J. S. H. van Leeuwaarden, D. Mukherjee, “Generalized random sequential adsorption on Erdős–Rényi random graphs,” arXiv:1604.03918 (first public 2016-04-13), https://arxiv.org/abs/1604.03918. Open-access full text examined, especially introduction, model definitions, and main results.
3. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, “Greedy maximal independent sets via local limits,” arXiv:1907.07216 (first public 2019-07-16), https://arxiv.org/abs/1907.07216. Open-access full text examined, especially introduction and local-limit statements.
