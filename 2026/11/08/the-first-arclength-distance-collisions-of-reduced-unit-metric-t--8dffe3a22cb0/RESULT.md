# The first arclength-distance collisions of reduced unit metric trees occur at fifteen vertices

## Finding
A finite metric tree is **reduced** if each essential vertex has degree one or degree at least three: no degree-two combinatorial vertices are permitted. This is the intrinsic model in which edges cannot be suppressed without changing the stipulated common edge length. Among reduced unit-edge metric trees, the full intrinsic distance distribution for two independent points sampled from normalized arclength is injective through fourteen vertices and first fails at fifteen. Exactly **three** unordered pairs of fifteen-vertex trees have coincident distributions, and every other pair is distinguished.

The three collision spectra, using the number of unordered pairs of distinct edges at each minimum endpoint distance, are
\[
(25,26,24,16),\qquad (25,28,26,12),\qquad (37,42,12).
\]
Every one of these lists sums to \(\binom{14}{2}=91\). The 132 reduced trees on fifteen vertices form 129 distance-law classes: three doubletons and 126 singletons. Each pair consists of nonisometric metric trees.

## Assumptions and scope
For each integer \(n\ge2\), consider connected, simple, unlabelled combinatorial trees with \(n\) vertices, all edges metrized as closed unit intervals, and no vertex of degree two. Give the resulting length space intrinsic geodesic distance and normalized one-dimensional arclength. Take independent samples \(X,Y\) from this measure and let \(D=d(X,Y)\). Vertex endpoint events have zero sampling probability.

For a tree \(G\) with \(m=n-1\) edges and distinct edges \(e,e'\), define \(\delta(e,e')=\min\{d_G(u,v):u\in e,\,v\in e'\}\), where \(u,v\) are graph vertices and \(d_G\) is edge-count distance. Write \(H_j\) for the number of unordered distinct-edge pairs with \(\delta(e,e')=j\); the equivalent line-graph distances are \(j+1\). Only integer-edge lengths and normalized arclength sampling are covered.

## Proof
**1. Complete distance law.** Sampling from normalized arclength first chooses each of the \(m\) unit edges with probability \(1/m\), then a coordinate uniform on \((0,1)\). With probability \(1/m\), the two points lie on the same edge; their difference distance has density \(2(1-r)\) for \(0<r<1\). For two distinct edges the unique connecting path joins the closest endpoints. Independently measured distances to those endpoints are uniform on \((0,1)\), so conditional distance equals \(j+U+V\) where \(j=\delta(e,e')\). The sum \(U+V\) has tent density \(\tau(t)=t\) for \(0<t<1\), \(\tau(t)=2-t\) for \(1\le t<2\), and zero elsewhere. There are two ordered edge choices per unordered pair. Thus
\[
f_G(r)=\frac{2}{m}(1-r)\mathbf1_{(0,1)}(r)+\frac{2}{m^2}\sum_{j\ge0}H_j\tau(r-j).
\]
This formula holds for almost every \(r>0\); it integrates to one because \(\sum_jH_j=\binom m2\). In particular \(f_G(0+)=2/m\), so the full distribution determines the number of edges and hence \(n\). For fixed \(m\), the histograms are recovered inductively: after subtracting the same-edge contribution, the restriction to \((0,1)\) determines \(H_0\); then restrictions to \((j,j+1)\), successively, determine each \(H_j\) once earlier coefficients are known. Thus full distribution equality is equivalent to equality of histograms.

**2. Exhaustive classification.** Every unlabeled tree on \(n\ge3\) vertices is obtained by attaching a leaf to some \((n-1)\)-vertex tree; deleting an arbitrary leaf proves exhaustiveness inductively. To remove duplicates, canonically encode each tree via its one center vertex or two center vertices: recursively encode each rooted branch by balanced parentheses with lexicographically sorted child encodings, then label the center type `V` or `E`, concatenating sorted encodings of both sides for a two-center tree. Repeatedly pruning leaves identifies the center(s). Two unlabelled trees have the same code if and only if they are isomorphic, by induction on rooted branches and the uniqueness of the center(s).

The accompanying standalone `reduced_tree_checker.py` implements these exact operations without third-party libraries and counts for \(n=3,4,\ldots,15\) all trees \((1,2,3,6,11,23,47,106,235,551,1301,3159,7741)\); the reduced subsets have counts \((0,1,1,2,2,4,5,10,14,26,42,78,132)\). Breadth-first graph distances between endpoints of every edge pair compute exact integer histograms. No histogram repeats for reduced orders \(n<15\). At \(n=15\), exactly three histogram groups are doubletons and all others are singletons, with the three spectra listed above. The checker emits each pair's two distinct canonical tree encodings and all fourteen edges of each representative, making the finite certificates inspectable. It asserts the expected counts and the exact classification, and prints `REDUCED_METRIC_TREE_SHARP_ORDER_15_PASS` upon success.

**3. Nonisometry.** A metric-tree isometry preserves valence at each point and preserves the unit-length branch structure. For a reduced unit-edge tree, valence-one and valence-at-least-three points are exactly the combinatorial vertices, so an isometry induces a combinatorial graph isomorphism. The distinct canonical codes printed for each pair rule this out. The pair with histogram \((37,42,12)\) also has differing degree multisets: \((7,5,4,1^{12})\) versus \((8,3,3,3,1^{11})\).

## Verification
Run `python3 reduced_tree_checker.py` with a standard Python 3 interpreter. The script independently enumerates every unlabelled tree by induction, computes breadth-first distance histograms, verifies the singleton and doubleton counts for every order through fifteen, and prints all colliding canonical representatives and edge lists. The recorded successful terminal line was `REDUCED_METRIC_TREE_SHARP_ORDER_15_PASS`. No numerical approximation, statistical simulation, or unbounded search is used in the classification. The finite enumeration's mathematical completeness depends on the proved leaf-attachment and canonical-tree-encoding lemmas, not simply on the printed success line.

## Relationship to prior work
The edge-distance histogram is the coefficient list of the known edge-Hosoya polynomial, equivalently the usual Hosoya polynomial of the tree's line graph with exponents shifted by one. This transformation is prior art, not itself a claim of novelty. The general possibility of nonisomorphic metric trees with indistinguishable distance distributions is also known; for example Mémoli and Needham (2018 preprint; 2022 journal) give substantially larger examples using even local distance distributions. A previous small-order census including nine-vertex unrestricted trees likewise provides prior evidence of earlier collisions when degree-two vertices are allowed. The contribution here is the **sharp fifteen-vertex cutoff and complete three-pair classification for reduced equilateral trees**, the intrinsic no-degree-two subclass. Ramane et al. (2013) study terminal, not full edge-pair, Hosoya polynomials of line graphs.

## Limitations
No conclusion is claimed for nonunit edge lengths, graph cycles, all trees with degree-two vertices, or for any order exceeding fifteen. The broad existence of colliding tree distance distributions and the concept of an edge-Hosoya polynomial are previously known. The finite exact census could have a historical counterpart in old unindexed chemical graph theory; one relevant 1982 paper on distance-degree sequences was not available in full and its different invariant was assessed from the abstract only. Independent mathematical review has not been performed.

## References
1. H. S. Ramane, A. B. Ganagi, K. P. Narayankar, S. S. Shirkol, *Terminal Hosoya Polynomial of Line Graphs*, Journal of Discrete Mathematics (2013), doi:10.1155/2013/857908, first public 2013-06-13.
2. F. Mémoli, T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (first posted 2018-10-23), Section 4.1, Example 4.3; journal version 2022, doi:10.1111/sapm.12526.
3. P. J. Slater, *Counterexamples to Randić's conjecture on distance degree sequences for trees*, J. Graph Theory 6 (1982), 89–92, doi:10.1002/jgt.3190060111 (abstract only inspected).
4. H. Hosoya, *On some counting polynomials in chemistry*, Discrete Applied Mathematics 19 (1988), 239–257, doi:10.1016/0166-218X(88)90017-0 (background reference via Ramane et al.).
