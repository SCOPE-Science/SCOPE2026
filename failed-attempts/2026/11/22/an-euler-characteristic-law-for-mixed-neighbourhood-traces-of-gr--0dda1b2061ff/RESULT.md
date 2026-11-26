# An Euler characteristic law for mixed neighbourhood traces of graph incidence structures

## Finding

Let \(H=(V,E)\) be any finite simple undirected graph. Its **incidence graph** \(I(H)\) has an original-vertex node for each \(v\in V\), an edge-node for each \(e\in E\), and an adjacency precisely when \(v\in e\). Fix \(A\subseteq V\) and \(B\subseteq E\), not both empty. The **mixed marked trace family** is
\[
\mathcal T_H(A,B)=\big\{N_{I(H)}(x)\cap(A\sqcup B):x\in V\sqcup E\big\}.
\]
These are open-adjacency profiles, not complete first-order types including equality or the centre's sort.

Write \(a=|A|\), \(b=|B|\). Put
\[
e_A=|E(H[A])|,\qquad
\lambda_A=\big|\{v\in A:N_H(v)\setminus A\ne\varnothing\}\big|.
\]
Let \(H_B\) have edge set \(B\) and just its edge-incident endpoints (no isolated vertices). Let \(c_B\) be its number of connected components, \(p_B\) the number of those components containing at least two edges, and
\[
\beta_B=b-|V(H_B)|+c_B
\]
its cyclomatic number. All these quantities are zero if \(B=\varnothing\). Let \(\eta=1\) if some centre of \(I(H)\) has an empty trace, and let \(\eta=0\) otherwise. Equivalently, \(\eta=1\) if some original vertex is incident with no edge in \(B\), or some edge of \(H\) has both endpoints outside \(A\).

**Exact identity (all finite simple graphs):**
\[
\boxed{\ |\mathcal T_H(A,B)|=\eta+e_A+\lambda_A+b+p_B-\beta_B.\ }
\]
Thus for all integers \(a,b\ge0\) with \(a+b\ge1\),
\[
\boxed{\ \Pi(a,b)=\max_{H,A,B}|\mathcal T_H(A,B)|
=1+a+\binom a2+\left\lfloor\frac{3b}{2}\right\rfloor.\ }
\]
The maximum is attainable even with \(H\) connected. For a particular \((H,A,B)\), equality holds precisely when \(\eta=1\), \(H[A]\) is complete, every \(v\in A\) has a neighbour in \(V\setminus A\), \(\beta_B=0\), and \(p_B=\lfloor b/2\rfloor\) (vacuous clauses apply when a marked side is empty).

**Complete marked-edge extremizers.** Discard original vertices isolated in \(H_B\). For \(b=2k\ge2\), its only maximizing isomorphism type is \(kP_3\), the disjoint union of \(k\) two-edge paths. For \(b=2k+1\ge3\), the maximizing types are precisely
\[
kP_3\sqcup K_2,\quad
(k-1)P_3\sqcup K_{1,3},\quad
(k-1)P_3\sqcup P_4.
\]
For \(b=1\), the sole type is \(K_2\). Their minimum original-vertex orders are \(3k\) in the even case and \(3k+1\) in the odd case \(b\ge3\); in the latter case exactly the last two displayed families attain that minimum. When every marked edge has a distinct fixed name but original vertices have no names, the numbers of minimum-order types are
\[
L_{2k}=\frac{(2k)!}{2^k k!}\quad(k\ge1),\qquad
L_{2k+1}=4\binom{2k+1}{3}\frac{(2k-2)!}{2^{k-1}(k-1)!}\quad(k\ge1),
\]
with \(L_1=1\).

As an untyped graph-family corollary, allowing the marked split to vary for \(m=a+b\) gives exactly \(1+m+\binom m2\) traces. The open-neighbourhood set systems of incidence graphs have VC dimension at most two, and some have VC dimension two.

## Assumptions and scope

All graphs are **finite, undirected and simple**, with no multiple edges or loops; disconnected and isolated-vertex hosts are permitted. The marked original vertices and marked edge-nodes are distinct incidence-graph vertices even if the underlying notation overlaps. Open neighbourhoods are used: the centre itself is never automatically counted. The theorem holds for every individual triple \((H,A,B)\), without connectivity or degree bounds. The extremal maximum is over graph orders large enough for the prescribed marked elements. The empty-mark case is excluded from the maximum statement; the exact identity still works for nonempty \(V\) with \(A=B=\emptyset\).

## Proof

**1. Edge-node contributions.** An edge-node \(e=\{u,v\}\) sees \(\{u,v\}\cap A\). Every nonempty such trace has size one or two. The distinct size-two traces are exactly the edges of \(H[A]\), giving \(e_A\) of them. The distinct singleton traces are exactly \(\{u\}\) for those \(u\in A\) incident with an edge to \(V\setminus A\), giving \(\lambda_A\) of them. No other nonempty trace arises from an edge-node.

**2. The marked-edge star lemma.** An original-vertex node \(v\) sees the marked-edge incidence star \(\{e\in B:v\in e\}\). Consider two distinct original vertices with equal nonempty incidence stars. They share an edge \(e\in B\), which therefore joins them. If either lies on any other marked edge \(f\), then equality requires \(f\) to join exactly the same two endpoints, contradicting simplicity. Hence duplicate nonempty stars arise **only** at the two endpoints of a connected component isomorphic to \(K_2\), and each such component creates exactly one duplicate. Distinct components have disjoint, nonempty edge-label sets. If \(q_B\) counts the one-edge components, then the number of distinct nonempty original-node traces is
\[
|V(H_B)|-q_B=b+c_B-\beta_B-q_B=b+p_B-\beta_B.
\]
The second equality is the graph Euler formula, and the last uses \(c_B=q_B+p_B\).

**3. Addition of traces.** Any nonempty edge-node trace is a subset of the marked original-vertex side \(A\); any nonempty original-node trace is a subset of the disjoint marked edge-node side \(B\). Consequently these two families cannot overlap. There is at most one common empty trace, present exactly when \(\eta=1\). Adding steps 1 and 2 and the empty trace gives the claimed exact identity, with no probabilistic or asymptotic argument.

**4. Sharp upper bound and realization.** The elementary bounds \(e_A\le\binom a2\) and \(\lambda_A\le a\) are sharp simultaneously: mark the vertices of a clique \(K_a\), connect each to one additional unmarked helper vertex, and use the corresponding original edges. Every component counted by \(p_B\) contains at least two marked edges, so \(p_B\le\lfloor b/2\rfloor\); also \(\beta_B\ge0\). Thus
\[
|\mathcal T_H(A,B)|\le1+\binom a2+a+b+\lfloor b/2\rfloor.
\]
For the marked edges use \(\lfloor b/2\rfloor\) vertex-disjoint copies of \(P_3\) and, if \(b\) is odd, one additional disjoint \(K_2\). Take their original vertices disjoint from the marked clique and helper. The graph contains an empty-trace centre: an original vertex when \(b=0\), an edge-node when \(a=0\), or a marked original vertex when both sides are nonempty. It has \(\beta_B=0\) and \(p_B=\lfloor b/2\rfloor\), proving equality. If connectedness of \(H\) is additionally desired, join the finitely many original components with new *unmarked* edges, without changing \(A,B\) or their already-saturated nonempty trace sets; emptiness may be preserved by reserving one extra unmarked, isolated-in-\(H_B\) original vertex and linking it to one of the components. This does not alter any counted quantity and preserves realization of the empty trace.

**5. Equality rigidity.** All terms in the upper bound have independently nonnegative deficits, so equality forces and is forced by \(\eta=1\), \(e_A=\binom a2\), \(\lambda_A=a\), \(\beta_B=0\), and \(p_B=\lfloor b/2\rfloor\). The latter two say that \(H_B\) is a forest with as many components containing at least two edges as possible. If \(b=2k\), all edges are consumed by \(k\) components with exactly two edges each, hence \(kP_3\). If \(b=2k+1\) with \(k\ge1\), either \(k\) two-edge components leave a single isolated edge \(K_2\), or one of the \(k\) large components has exactly three edges while the other \(k-1\) have two edges. A three-edge tree is precisely a three-star \(K_{1,3}\) or a four-vertex path \(P_4\). This proves completeness of the families, including all boundary cases.

**6. Minimum orders and edge-label census.** A two-edge path uses three original vertices. An isolated edge uses two; either three-edge tree uses four. Thus the minimizing orders and minimizing isomorphism types are as stated. For \(2k\) individually named edges, a minimizing forest pairs their labels into \(k\) unordered cherry pairs, giving \((2k)!/(2^kk!)\). For \(2k+1\ge3\), choose the three labels in the distinguished three-edge component and pair the remaining \(2k-2\) labels. There are four possible unlabelled-vertex ways to place the chosen three labels: one three-star and three paths according to which label occupies the middle edge. This yields the odd formula. Finally, the sharp global \(m\)-mark trace function is obtained at \(a=m,b=0\), and is strictly below \(2^3\) at \(m=3\) but equals \(2^2\) at \(m=2\), establishing VC dimension exactly two for the class.

## Verification

The standalone `CHECKER.py` constructs incidence traces directly and checks both the Euler identity and equality conditions against the theorem. Its executed output is supplied in `CHECKER_OUTPUT.txt`. An exhaustive search classified \(93{,}025\) labelled marked-edge skeletons with at most seven original vertices and at most six edges, finding \(4{,}402\) extremal cases; all had and only had the predicted component structures. It also verified \(120\) explicit mixed-side constructions, all small graph/mark configurations through four original vertices, \(40{,}000\) random larger configurations, and \(50{,}260\) total equality/identity comparisons. These finite tests corroborate, but do not substitute for, the all-size proof.

Run with a standard Python 3 interpreter: `python CHECKER.py`. No external dependencies or data are required.

## Relationship to prior work

The motivating paper by Berthe, Foucaud, Lehtilä and Parreau (2026) studies **closed** neighbourhood complexity at bounded treewidth and pathwidth. It motivates exact trace growth but does not assert this mixed-sort **open** incidence-graph Euler formula or its edge-component equality classification. Arbitrary one-subdivisions of large cliques have unbounded treewidth, so its fixed-width bounds cannot be specialized to this whole class.

Beaudou, Bok, Foucaud, Quiroz and Raymond (2025) study distance-neighbourhood/profile complexity for minor-excluding or tree-structured graphs, not the present unrestricted one-subdivision family. Foucaud, Gahlawat, Mc Inerney and Tale (2025) use bipartite incidence graphs for computational VC-dimension problems, but their treewidth-parameterized algorithm and complexity lower bounds do not imply an exact bivariate profile count or forest extremizer classification. The published full proof of *All identifying open codes of subdivided complete graphs* already uses the same elementary fact that two original vertices can have equal nonempty marked-edge incidence stars only when they are the endpoints of an isolated selected edge. **That duplicate-star observation is not claimed new here.** Its theorem classifies total open-identifying codes of a fully subdivided clique, whereas the present statement counts the traces of arbitrary marked sets in incidence graphs of every simple original graph. The published full proof of *Maximal induced matchings of complete-graph incidence families* enumerates maximal induced matchings rather than adjacency profiles; its all-parameter formulas cannot be substituted for the present count. Both full texts were inspected for these scope comparisons.

The standard Sauer–Shelah size bound already explains the shape of the **one-parameter** quadratic corollary once VC dimension two is known. That familiar upper bound is not claimed as the new contribution. The claim here is the **all-graph exact Euler formula**, its sharp **two-parameter** maximum, and its full forest rigidity/census.

## Limitations

Only finite simple graphs and ordinary one-subdivision incidence graphs are covered. Multigraphs, higher-rank hypergraphs, higher-radius neighborhoods, and closed-neighborhood traces are not included. The minimal-vertex census counts the marked-edge skeleton, not minimum *total* incidence-host order with both marked sides. Historical novelty is best-knowledge relative to inspected publications and database records, not a guarantee of priority. The proof has received no independent mathematical audit; computational sampling cannot establish the infinite assertions by itself.

## References

1. G. Berthe, F. Foucaud, T. Lehtilä and A. Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889v1, first public 18 July 2026. https://arxiv.org/html/2607.16889v1
2. L. Beaudou, J. Bok, F. Foucaud, D. A. Quiroz and J.-F. Raymond, *Profile and neighbourhood complexity of graphs with excluded minors and tree-structured graphs*, arXiv:2501.08895v1, first public 15 January 2025. https://arxiv.org/html/2501.08895v1
3. F. Foucaud, H. Gahlawat, F. Mc Inerney and P. Tale, *The Parameterized Complexity of Computing the VC-Dimension*, arXiv:2510.17451v1, first public 20 October 2025. https://arxiv.org/html/2510.17451v1
4. *All identifying open codes of subdivided complete graphs*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-all-identifying-open-codes-of-subdivided-complete-graphs--078f1db52295
5. *Maximal induced matchings of complete-graph incidence families: exact polynomials and cardinality gaps*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-maximal-induced-matchings-of-complete-graph-incidence-families-e--3a1144b1760f
