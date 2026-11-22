# A complement-sensitive mobility switch for optimal landmarks on the Clebsch graph

## Finding

Let \(G\) be the five-regular Clebsch graph on \(V=\mathbb F_2^4\), with \(u\sim v\) exactly when \(u+v\) is in the five-vector set \(H=\{1000,0100,0010,0001,1111\}\). Let \(\overline G\) be its complement. A *metric basis* is a smallest set of landmarks that distinguishes all vertices by their vectors of graph distances.

**Theorem.** The minimum metric bases of both \(G\) and \(\overline G\) are exactly the \(80\) sets
\[
B(c,t)=N_G(c)\setminus\{t\},\qquad c\in V,\ t\in N_G(c).
\]
They all have size \(4\); each basis has a unique center \(c\). If two minimum bases are adjacent when one landmark can be replaced by one other landmark, their exchange graph is the disjoint union \(16K_5\), containing \(80\) states and \(160\) edges. If a replacement is additionally required to slide along an edge of the underlying graph, the slide graph is \(80K_1\) for \(G\), but exactly \(16K_5\) for \(\overline G\). Consequently every optimum is slide-frozen in the five-regular graph, while every legal optimum-preserving exchange is a slide in its ten-regular complement.

The value \(\operatorname{dim}(G)=\operatorname{dim}(\overline G)=4\) was previously known. The claim here concerns the *complete family* of optimal landmark placements and its exact complement-dependent reconfiguration geometry.

## Assumptions and scope

Graphs are simple and undirected; vertex sets of metric bases are unordered. Distances are ordinary unweighted shortest-path distances. In the one-token-jump model exactly one vertex is removed and one previously unselected vertex is inserted, with both endpoints required to be metric bases; a slide is such an exchange with the removed and inserted vertices adjacent in the specified base graph. No temporary extra landmarks or nonoptimal intermediate sets are permitted. Statements concern only the sixteen-vertex five-regular Clebsch graph and its complement, not all folded cubes or all strongly regular graphs.

## Proof

**1. The five-generator model.** The five nonzero vectors in \(H\) have total sum zero, and no nonempty proper subcollection has sum zero. In particular the ten sums of two distinct generators are different and comprise exactly the ten nonneighbors of \(0\), while the five generators themselves are its five neighbors. Translations are graph automorphisms. Two adjacent vertices have no common neighbor, since no three distinct generators sum to zero; two nonadjacent vertices have exactly two common neighbors, given by the unique representation of their difference as a sum of two generators. Thus \(G\) is strongly regular with parameters \((16,5,0,2)\), in particular triangle-free. Every open neighborhood \(N_G(c)\) is independent, and two distinct open neighborhoods intersect in at most two vertices.

**2. No smaller basis.** For any three landmarks, the remaining thirteen vertices have distance vectors in \(\{1,2\}^3\), which has only eight possible values. Hence no three-set resolves the graph. The same holds for smaller sets by monotonicity.

**3. A resolving four-set must be independent.** Fix a four-set \(S\). If its induced subgraph has \(e\) edges, the twelve vertices outside \(S\) supply altogether \(4\cdot5-2e=20-2e\) incidences with \(S\). Their adjacency signatures are four-bit words. Twelve *different* four-bit words require at least nineteen total one-bits: the cheapest twelve are one word of weight zero, all four of weight one, all six of weight two, and one of weight three. If \(e\ge1\), at most eighteen ones occur. Then two outside vertices have identical adjacency signatures and therefore equal distance vectors to \(S\), so \(S\) does not resolve. Thus every resolving four-set is independent.

**4. Classification of independent four-sets.** By translation assume an independent four-set is \(S=\{0,x,y,z\}\). Each of \(x,y,z\) is a sum of two distinct elements of \(H\), thus corresponds to an edge of an abstract five-vertex complete graph on the generator labels. Two such nonzero vertices are adjacent in \(G\) exactly when their two-label sets are disjoint (their symmetric difference then consists of four generators and sums to the remaining generator). Therefore independence means three distinct pair-labels are pairwise intersecting. Three pairwise intersecting edges in a simple complete graph are either a three-edge star or a triangle.

For a star \(\{\{i,j\},\{i,k\},\{i,l\}\}\), the set is \(\{0,h_i+h_j,h_i+h_k,h_i+h_l\}\), precisely four of the five neighbors of \(h_i\). Conversely any four of the five neighbors of a center have this form after translation. There are \(16\binom54=80\) such four-sets, all distinct: a four-set cannot lie in two open neighborhoods because their intersection size is at most two.

For a triangle on generator labels \(i,j,k\), the four-set is \(\{0,h_i+h_j,h_i+h_k,h_j+h_k\}\). Let \(l,m\) be the two unused generator labels. The vertices \(h_l,h_m\) have *identical* distances \((1,2,2,2)\) to these four landmarks, because a sum of any three distinct generators is not itself a generator. Hence this triangle type fails to resolve.

**5. Every star type resolves.** Fix \(c\) and put \(S=N_G(c)\setminus\{t\}\). The four selected landmarks are individually identified by a zero in their own coordinate. The center \(c\) has distance signature \((1,1,1,1)\); the omitted neighbor \(t\) has \((2,2,2,2)\), as \(N_G(c)\) is independent. Each of the remaining ten vertices is a nonneighbor of \(c\) and has exactly two neighbors in \(N_G(c)\). Those ten neighbor-pairs run through all ten two-subsets of \(N_G(c)\): for each pair, the strong-regularity common-neighbor condition gives a unique common neighbor other than \(c\). Removing coordinate \(t\) leaves six distinct signatures having two coordinates of value \(1\) and four distinct signatures having just one coordinate of value \(1\) among the four selected landmark coordinates. They are distinct from the center, omitted neighbor and selected landmarks. Thus every \(S\) resolves. Combined with steps 2–4 this proves the metric-basis classification.

**6. Complement and movement.** For any landmark set \(S\), a vertex in \(S\) has distance zero at its own coordinate in both \(G\) and \(\overline G\). For vertices outside \(S\), complementation exchanges graph distance \(1\) with \(2\), since both graphs have diameter two. Hence \(S\) is resolving in \(G\) exactly when it is resolving in \(\overline G\), proving equality of their basis families.

For a fixed \(c\), any two of the five bases \(B(c,t)\) differ in exactly one selected vertex and therefore form a clique \(K_5\) under one-landmark jumps. For distinct centers \(c,d\), any two such bases intersect in at most \(\lvert N_G(c)\cap N_G(d)\rvert\le2\), so there is no jump between them (which would require three common landmarks). This gives exactly sixteen disjoint \(K_5\) components and \(16\binom52=160\) exchange edges. Every exchange moves between two vertices of a common independent neighborhood of \(G\), so its endpoints are nonadjacent in \(G\) but adjacent in \(\overline G\). Thus no jump is a slide in \(G\), and all jumps are slides in \(\overline G\). \(\square\)

## Verification

The included standalone programs `verify_binary.py` and `verify_incidence.py` use two different constructions: a four-bit Cayley graph and an incidence/disjointness graph on one center, five singleton labels and ten pairs. Each exhaustively checks all \(\binom{16}{4}=1820\) four-sets, the minimum-basis set, the jump graph, and both slide graphs. Both produced `verification=PASS`, \(80\) bases, \(160\) jumps, no original slides and \(160\) complementary slides. The proof above, rather than the finite computations alone, establishes the structural classification.

Run `python3 verify_binary.py` and `python3 verify_incidence.py` from any directory with Python 3 and no third-party packages.

## Relationship to prior work

Bailey established the Clebsch graph's metric dimension as four and recorded the same value for its complement. Lu and Ye studied metric dimensions of folded cubes and recorded \(\beta(F_5)=4\). These existing dimension values are not new here. Kelenc and coauthors study the distinct hypercube and edge/mixed-resolution setting. The contribution here is the full eighty-basis classification together with exact reconfiguration graphs and the complement-induced switch in *local* mobility. Related published studies of edge-metric bases, locating-dominating sets and determining sets on the Clebsch graph concern different solution families, and their reported statistics do not by themselves imply the statement above.

## Limitations

The theorem is for one named sixteen-vertex graph and its complement; no extension to all folded cubes or general graphs is claimed. A historically related full paper by Zhang and coauthors on folded-cube metric dimension was not accessible in full text during the literature comparison. Its available abstract and first-page preview concern constructions and upper bounds; the absence of an equivalent classification from that full paper has **not** been established. An earlier unindexed solution or independent classification remains possible. The computational checks are independent implementations, not independent external mathematical audits.

## References

- R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, Australasian Journal of Combinatorics 62 (2015), 18–34; first public arXiv:1312.4973, https://arxiv.org/abs/1312.4973. The Clebsch dimension appears in the metric-dimension tables.
- C. Lu and Q. Ye, *A bridge between the minimal doubly resolving set problem in (folded) hypercubes and the coin weighing problem*, Discrete Applied Mathematics 309 (2022), 147–159; first public arXiv:2012.00396 on 2020-12-01, https://arxiv.org/abs/2012.00396, Section 4 and Table 1.
- Y. Zhang, L. Hou, B. Hou, W. Wu, D.-Z. Du and S. Gao, *On the metric dimension of the folded n-cube*, Optimization Letters 14 (2020), 249–257; first published online 2019-09-09, https://doi.org/10.1007/s11590-019-01476-z (abstract and first-page preview only inspected).
- A. Kelenc, A. T. M. Toshi, R. Škrekovski and I. G. Yero, *On Metric Dimensions of Hypercubes*, arXiv:2102.10916 (2021), https://arxiv.org/abs/2102.10916.
