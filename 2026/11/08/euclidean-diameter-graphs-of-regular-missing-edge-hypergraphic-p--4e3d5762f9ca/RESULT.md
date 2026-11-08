# Euclidean diameter graphs of regular missing-edge hypergraphic polytopes

## Finding

For every finite simple regular graph \(G\), the Minkowski sum of coordinate simplices whose coordinates omit the endpoints of an edge has a two-shell Euclidean vertex structure. The outer shell is the complete set of contacts of a unique enclosing sphere. Moreover, its Euclidean diameter graph is an explicit double-cover-by-independent-twins of the edge-disjointness graph of the complement. This describes the distance extremizers in all dimensions, not just a bound on the diameter.

Fix an integer \(n\ge5\) and a simple \(r\)-regular graph \(G=([n],E)\), with \(2\le r\le n-2\). Write \(m=|E|=nr/2\) and \(q=n-r-1\). For an edge \(e=\{i,j\}\), put \(\Delta_{[n]\setminus e}=\operatorname{conv}\{e_t:t\notin e\}\), where \(e_t\) are the standard coordinate basis vectors of \(\mathbb R^n\). The polytope is
\[
P_G=\sum_{e\in E}\Delta_{[n]\setminus e}\subset\{x:\sum_{i=1}^{n}x_i=m\}.
\]
All distances below use the ordinary ambient Euclidean norm, restricted to this affine hyperplane. No connectivity or vertex-transitivity of \(G\) is assumed.

The distinct vertices of \(P_G\) are precisely the following vectors (discard repetitions in the second family):
\[
\begin{aligned}
v_{ts}&=(m-r)e_t+re_s&&\text{for ordered }t\ne s\text{ with }\{t,s\}\notin E,\\
w_{tsu}&=(m-r)e_t+(r-1)e_s+e_u&&\text{for ordered }t\ne s,\ \{t,s\}\in E,\ u\notin\{t,s\}.
\end{aligned}
\]
There are exactly \(nq\) first-family vertices. The second family contains \(n(2n-5)\) vertices when \(r=2\), or \(nr(n-2)\) when \(r\ge3\). In particular, these families are disjoint.

**Minimum enclosing sphere.** Its unique center is \(c=(r/2)\mathbf1\), and its squared radius is
\[
\boxed{R(P_G)^2=\frac{r^2}{4}(n^2-5n+8).}
\]
Exactly the \(nq\) first-family vertices touch the sphere. Every second-family vertex lies at the strictly smaller squared distance \(R(P_G)^2-2(r-1)\). No nonvertex point touches the sphere.

**Diameter and complete equality case.** The exact squared diameter is
\[
\boxed{\operatorname{diam}_2(P_G)^2=\frac{r^2}{2}\big((n-2)^2+4\big).}
\]
An unordered pair is diametral if and only if its members are two first-family vertices \(v_{ts}\), \(v_{ab}\) satisfying \(\{t,s\}\cap\{a,b\}=\varnothing\). Thus, with \(H=\overline G\), the graph on nonisolated diameter vertices is obtained from the edge-disjointness graph of \(H\) by replacing every vertex by two **nonadjacent** twins, and every edge by a complete bipartite \(K_{2,2}\). The exact number of diametral pairs is
\[
\boxed{\frac{nq}{2}\big(q(n-4)+2\big).}
\]
All second-family vertices are isolated in this diameter graph.

**Cycle/Schrijver consequence.** In the cyclic-interval instance \(G=C_n\), the summands are the length-\(n-2\) cyclic coordinate simplices, \(q=n-3\), and the edges of \(\overline{C_n}\) are the stable two-subsets of the cyclic vertex set. Therefore the nonisolated diameter graph is the independent-two-twin blow-up of the stable Kneser (Schrijver) graph \(SG(n,2)\). Schrijver's chromatic-number theorem yields
\[
\boxed{\chi(\text{diameter graph of }P_{C_n})=n-2.}
\]
In particular this Euclidean diameter-graph chromatic number is unbounded. The nonisolated vertex count is \(n(n-3)\), and the diameter-edge count is \(n(n-3)(n^2-7n+14)/2\). The graph-theoretic theorem of Schrijver is cited as prior work, not reproved or claimed as new.

## Assumptions and scope

All graphs are finite, simple, labelled, undirected, and regular; \(n\ge5\) and \(2\le r\le n-2\). The original Euclidean metric of \(\mathbb R^n\) is fixed: rescaling or applying an arbitrary affine equivalence would change the metric conclusions. The affine dimension of \(P_G\) is \(n-1\). The diameter graph here connects **distinct vertices at maximum Euclidean distance**, not edges of the polytope's ordinary one-skeleton, and not shortest-path distances on a graph.

## Proof

**Step 1 (exposed vertices).** Take any generic linear functional with strict coordinate ordering \(t\succ s\succ u\succ\cdots\). A Minkowski-sum vertex chooses, from each summand \(\Delta_{[n]\setminus\{i,j\}}\), its unique coordinate of largest weight. Exactly \(m-r\) graph edges avoid \(t\), and those summands choose \(e_t\). Among the \(r\) graph edges incident to \(t\), if \(\{t,s\}\notin E\), every summand permits \(s\), giving \(v_{ts}\). If \(\{t,s\}\in E\), all but the summand for edge \(\{t,s\}\) permit \(s\), while that single exceptional summand chooses the third-highest coordinate \(u\); the result is \(w_{tsu}\). Conversely, every ordered tuple in either description can be put first in a generic ordering, and hence produces an exposed vertex. Every vertex admits some generic exposing functional, so there are no others.

Because \(m-r=r(n-2)/2>r\ge2\), the largest coordinate uniquely identifies \(t\) in both families. Distinct ordered nonedges yield distinct outer vertices. For \(r\ge3\), the coordinate \(r-1>1\) also uniquely identifies \(s\) in the inner family, and \(u\) follows, yielding \(nr(n-2)\) distinct inner vertices. For \(r=2\), there are two possible equal unit coordinates \(s,u\); for each fixed \(t\), unordered choices of \(\{s,u\}\) with at least one neighbour of \(t\) number \(\binom{n-1}{2}-\binom{n-3}{2}=2n-5\). The two families cannot coincide because they have different numbers or values of positive coordinates.

**Step 2 (two norm shells).** All vertices have coordinate sum \(m\), and with \(c=(m/n)\mathbf1=(r/2)\mathbf1\) the identity \(\|z-c\|^2=\|z\|^2-m^2/n\) holds for every vertex. Each outer vertex has \(\|v\|^2=(m-r)^2+r^2\); each inner has \(\|w\|^2=(m-r)^2+(r-1)^2+1=\|v\|^2-2(r-1)\). Substituting \(m=nr/2\) gives the displayed squared radius. Thus the ball with center \(c\) and radius \(R\) contains all vertices, hence their convex hull. No nonvertex can be on the same sphere: a nontrivial convex combination of distinct vertices has strictly smaller squared norm relative to \(c\) than the corresponding combination of their squared norms.

**Step 3 (uniqueness and optimality).** Each coordinate appears as first label of exactly \(q\) ordered nonedges and as second label of exactly \(q\). Therefore the arithmetic average of all \(nq\) outer vertices is \(c\). For every alternative center \(z\), the average of squared distances from \(z\) to these outer vertices equals \(R^2+\|z-c\|^2\). Consequently any enclosing ball centered at \(z\) has squared radius at least this average. The proven ball is smallest, and equality requires \(z=c\), proving center uniqueness.

**Step 4 (diameter and equality).** For any vertices \(x,y\), coordinates are nonnegative and \(\|x\|^2,\|y\|^2\le Q:=(m-r)^2+r^2\). Hence
\[
\|x-y\|^2=\|x\|^2+\|y\|^2-2\langle x,y\rangle\le2Q.
\]
Equality holds precisely when \(x,y\) are first-family vertices and have disjoint positive-coordinate supports. Such pairs exist: the complement \(H\) is a simple \(q\)-regular graph, \(q\ge1\), and has
\[
M_2(H)=\binom{nq/2}{2}-n\binom q2=\frac{nq}{8}\big(q(n-4)+2\big)>0
\]
unordered pairs of disjoint edges. Each disjoint edge pair yields four pairs of oriented first-family vertices, and no others, giving the claimed diameter count. As in Step 2, strict convexity of squared Euclidean distance in either variable excludes all nonvertex diameter endpoints. Substituting \(m=nr/2\) into \(2Q\) proves the diameter formula. The edge-Kneser and Schrijver identification follows directly from the ordered-nonedge labels and the definition of cyclically stable two-subsets; independent twins do not change graph chromatic number.

For completeness, the stated affine dimension follows because any distinct coordinate indices \(i,j\) can be avoided simultaneously by some edge of \(G\) (there are \(m-2r+\mathbf1_{\{i,j\}\in E}>0\) such edges for \(n>4\)). Thus one summand contains both \(e_i,e_j\), and \(e_i-e_j\) is a direction of \(P_G\), so all zero-sum directions are spanned.

## Verification

Run `python verify_regular_hypergraph.py`. It independently constructs every exposed vertex by enumerating all generic coordinate permutations, compares that set to both stated vertex families, checks shell radii using exact rational arithmetic on small cases, and tests all candidate diameter pairs against the disjoint-support criterion. Test graphs include cycles, disconnected regular graphs, complete bipartite graphs, matching complements, and every admissible regular simple graph in the NetworkX graph atlas through seven vertices when NetworkX is installed. The replay checked 16 admissible examples and passed. The finite computation tests the formula but does **not** prove its unbounded range; Steps 1–4 are the unrestricted argument.

## Relationship to prior work

Gélinas and Yang (2026) introduce and analyze lattice/poset properties of cyclic-interval hypergraphic polytopes, providing the fresh motivating family. Their manuscript does not assert an ordinary-Euclidean circumradius, diameter-graph, or Schrijver-colouring theorem. Agnarsson and Morris (2006) study normal fans, combinatorial vertex structure, and face orders of general Minkowski sums of simplices; that broader combinatorial framework is compatible with Step 1 but does not itself give the stated Euclidean equality classification. Schrijver (1978) proves the chromatic theorem for stable Kneser graphs, used here as an explicitly cited ingredient after establishing the new geometric realization. Previously published work on graphical zonotopes, symmetric-edge polytopes, and star hypergraphic polytopes uses different Minkowski summands or metrics and does not imply this assertion for missing-edge regular-graph hypergraphic sums.

## Limitations

This is an exact metric theorem for the stated canonical realization, not an affine-invariant claim or a theorem about graph-theoretic polytope diameter. Regularity and \(2\le r\le n-2\) are essential to the formulas as written; nonregular graphs are not classified here. Only the cycle subfamily is asserted to have the Schrijver graph chromatic number. The literature comparison supports provisional historical priority, not a guarantee of global uniqueness. No independent external validation has been performed.

## References

- A. Gélinas and L. Yang, *Lattice characterization of cyclic interval hypergraphic posets* (2026), arXiv:2605.03913, first publicly posted 2026-05-05, https://arxiv.org/abs/2605.03913 .
- G. Agnarsson and W. Morris, *On Minkowski sums of simplices* (2006), arXiv:math/0605564, https://arxiv.org/abs/math/0605564 .
- A. Schrijver, *Vertex-critical subgraphs of Kneser-graphs*, Nieuw Archief voor Wiskunde 26 (1978), 454–461; chromatic theorem on stable Kneser graphs.
