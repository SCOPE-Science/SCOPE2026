# Bounded connected-subtree classifiers are shattering-extremal, with mixed-dimensional star complexes

## Finding

Let \(T\) be any finite nonempty tree with \(n\) vertices and let \(1\le r\le n\). A binary concept is an indicator of a connected induced vertex set of \(T\) containing at most \(r\) vertices, with the empty set also admitted. Write \(\mathcal C_r(T)\) for this concept class. For nonempty \(S\subseteq V(T)\), let \(H_T(S)\) be its minimal connecting subtree. Let \(L(U)\) be the set of degree-one vertices of the nontrivial tree \(T[U]\), with \(L(U)=U\) for singletons.

**Complete shattering theorem.** A nonempty vertex support \(S\) is shattered precisely when
\[
|V(H_T(S))|\le r\quad\text{and}\quad S=L(V(H_T(S))).
\]
Every such support is *strongly shattered*: there exists one fixed labeling of all outside vertices such that all \(2^{|S|}\) labelings on \(S\) occur. In particular, \(\mathcal C_r(T)\) is shattering-extremal and has an explicit bijection between its concepts and shattered supports: the empty set maps to the empty support, and each nonempty connected subtree \(U\) maps to its leaf set \(L(U)\). Consequently,
\[
\Phi_{T,r}(z)=1+\sum_{\substack{\varnothing\ne U\subseteq V(T)\\ T[U]\;\mathrm{connected},\ |U|\le r}}z^{|L(U)|},\qquad
\mathrm{VCdim}(\mathcal C_r(T))=\max_{\substack{T[U]\;\mathrm{connected}\\1\le|U|\le r}}|L(U)|.
\]
The leaf-count optimization on the right and subtree-polynomial enumeration are previously studied invariants; the contribution is the all-support shattering and strong-shattering identification, its exact link to subtree enumeration, and the topological consequence below.

**Mixed-dimensional topology.** Let \(T=K_{1,m}\) be a star with \(m\ge4\) leaves. For \(4\le r\le m\), the shattered-support simplicial complex has facets of cardinalities \(2\) and \(r-1\), and
\[
|\operatorname{Sh}(\mathcal C_r(K_{1,m}))|\simeq
\bigvee^{m-1}S^1\ \vee\ \bigvee^{\binom{m-1}{r-1}}S^{r-2}.
\]
Thus both first and higher-dimensional reduced integral homology can be nonzero, even though the class is shattering-extremal. For the endpoint \(r=m+1\), the complex is a wedge of \(m-1\) circles.

## Assumptions and scope

Graphs are finite, simple, undirected; the input is a nonempty tree, including a singleton tree. Both empty and nonempty concepts are present, and the cardinality budget is an inclusive upper bound. A connected induced subset is identified with its vertex set. The leaf convention for one vertex is one leaf; a two-vertex tree has two leaves. Strong shattering means a full Boolean subcube with identical fixed coordinates outside the support, not merely distinct witnesses for each trace. The star homotopy statement uses ordinary geometric realization of the finite shattering complex.

## Proof

**Necessity.** Suppose nonempty \(S\) is shattered. The all-positive labeling must occur in a connected concept of size at most \(r\), so its minimal connecting subtree \(H_T(S)\) has at most \(r\) vertices. If a queried \(s\in S\) is internal to \(H_T(S)\), there exist distinct queried vertices in different components of \(H_T(S)-s\) (minimality of the hull). Any connected vertex set containing those two vertices must contain \(s\), contradicting the trace labeling that makes them positive and \(s\) negative. Thus every queried vertex is a leaf of the hull. Conversely, every leaf of a minimal connecting subtree necessarily belongs to the set being connected; hence \(S=L(H_T(S))\).

**Sufficiency and the full cube.** For any eligible support, put \(H=V(H_T(S))\) and \(I=H\setminus S\). If \(|H|\ge3\), the vertices in \(I\) induce a nonempty connected tree and every vertex of \(S\) is attached by one edge to \(I\); therefore \(I\cup A\) is connected for every \(A\subseteq S\). If \(|H|=2\), then \(I=\varnothing\) and \(I\cup A\) is either empty, a singleton, or the whole edge, all admitted. If \(|H|=1\), then \(I=\varnothing\) and the same assertion holds for its two subsets. In all cases the sets \(I\cup A\) lie in \(\mathcal C_r(T)\), agree outside \(S\), and realize all traces. This is strong shattering.

**Bijection and extremality.** Any nonempty connected induced vertex set \(U\) is the minimal connecting subtree of its leaf set: this is evident for one and two vertices, and for larger trees follows because every edge separates at least one leaf from another. The mapping \(U\mapsto L(U)\) is therefore injective, with inverse \(S\mapsto V(H_T(S))\) on eligible nonempty supports. Adding the empty set gives a bijection between concepts and shattered supports, proving equality of cardinalities, the polynomial formula, and the VC formula.

**Star topology.** On \(K_{1,m}\), a support of at least three vertices is shattered precisely when it lies wholly among the leaves and has at most \(r-1\) members. Every pair comprising the center and one leaf is shattered when \(r\ge2\), but no support containing the center and two leaves is shattered. Thus for \(r\ge3\) the complex is the \((r-2)\)-skeleton of the simplex on the \(m\) leaves (with full simplex when \(r=m+1\)), together with the \(m\) edges joining the additional center vertex to the leaves. The leaf skeleton, being connected, and the additional star form a graph-of-spaces attachment: contracting one center-to-leaf edge leaves \(m-1\) extra independent circles. For \(4\le r\le m\), the \((r-2)\)-skeleton of the \((m-1)\)-simplex is a wedge of \(\binom{m-1}{r-1}\) spheres in dimension \(r-2\). The latter standard skeleton formula follows inductively by splitting off one simplex vertex: the deletion is a skeleton, the link is the preceding skeleton, their inclusion is null-homotopic by connectivity, and Pascal's identity counts spheres. The displayed wedge decomposition follows. The center-leaf edges and maximal leaf faces give the two asserted facet sizes. At \(r=m+1\), the leaf simplex is contractible and only the circles remain.

## Verification

A standalone Python 3 and NetworkX script, `check_subtree_shattering.py`, compares the direct finite trace definition with the hull-leaf criterion for all unlabeled tree shapes through eight vertices and all budgets; it independently compares the bivariate rooted-subtree recurrence with direct enumeration, tests star face sizes, and computes mod-two Betti numbers of small star complexes. The successful output was:

```
BOUNDED_SUBTREE_SHATTERING_PASS 48 tree_shapes 59906 support_radius_cases
STAR_FACETS_PASS 11
STAR_HOMOLOGY_PASS 39
```

The finite checks are only corroboration; all claimed parameters are proved by the unrestricted arguments above. For reproducing the enumeration install the common Python package `networkx`.

## Relationship to prior work

Munaro (2013) studies VC dimension of graph subgraph-concept families and cites earlier leaf-spanning-tree bounds for unrestricted connected subgraphs; those bounds are not new here, but they do not supply the budgeted all-support or strong-shattering theorem. Baste (2023) studies algorithmic maximum-leaf induced-subtree problems under size restrictions; the leaf objective is therefore not new. Klavžar, Kuziak, Peterin and Yero (2021) study graph Steiner general-position sets and tree cases, which motivate the leaf-hull obstruction but are not equivalent to all membership-label traces. Aliste-Prieto, Martin, Wagner and Zamora (first public 2024) establish relationships involving the already-known subtree polynomial; neither that polynomial nor the basic subtree dynamic programming alone is asserted as novel. Kusch and Mészáros (2017) provide the established general shattering-extremal vocabulary. The new, narrower assertion is the simultaneous complete support description, equality with strong shattering at each size cap, and explicit mixed-dimensional star realization.

## Limitations

The theorem requires the ambient graph to be a tree and explicitly includes the empty concept. The star formula is restricted to the displayed parameters; it makes no corresponding homotopy claim for arbitrary trees. The classical general-position and subtree-enumeration results have substantial overlap with the corollaries. The accessible searches and inspected primary full texts did not exhibit the joint budgeted strong-shattering/topology statement, but priority under other terms (especially convex-tree ranges, lopsided systems, or subtrees) is not exhaustively ruled out. No independent audit is represented.

## References

1. Julien Baste, *The Leafed Induced Subtree in chordal and bounded treewidth graphs*, first public 2023-01-30, https://arxiv.org/abs/2301.12783.
2. Sandi Klavžar, Dorota Kuziak, Iztok Peterin, Ismael G. Yero, *A Steiner general position problem in graph theory*, first public 2021-05-18, https://arxiv.org/abs/2105.08391.
3. José Aliste-Prieto, Jeremy L. Martin, Jennifer D. Wagner, José Zamora, *Chromatic symmetric functions and polynomial invariants of trees*, first public 2024-02-15, https://arxiv.org/abs/2402.10333.
4. Andrea Munaro, *The VC-Dimension of Graphs with Respect to k-Connected Subgraphs*, first public 2013-02-26, https://arxiv.org/abs/1302.6500.
5. Christopher Kusch, Tamás Mészáros, *Shattering-extremal set systems from Sperner families*, first public 2017-10-09, https://arxiv.org/abs/1710.03165.
