# Maximal edge-general-position sets of trees: saturated subtrees and the lower number

## Finding
Let \(T\) be a finite simple tree with \(n\ge3\) vertices and \(m=n-1\) edges. An **edge-general-position set** is a set of edges containing no three edges on one shortest path. For \(S\subseteq E(T)\) with \(|S|\ge2\), let \(H(S)\) be the unique smallest connected subtree containing the edges of \(S\). Write \(\ell(H)\) for the number of leaf vertices of a nontrivial tree \(H\). Then:

**Structural classification.** \(S\) is edge general position if and only if \(S\) consists of all the leaf edges of \(H(S)\). It is inclusion-maximal if and only if, in addition, every vertex of \(H(S)\) with degree at least two in \(H(S)\) has all its neighbors in \(T\) already in \(H(S)\). Thus inclusion-maximal edge-general-position sets correspond bijectively to connected subtrees \(H\subseteq T\) with at least two edges whose nonleaf vertices are **saturated** (\(\deg_H(v)=\deg_T(v)\)).

The complete edge-general-position and inclusion-maximal enumerators are respectively
\[
P_T(z)=1+mz+\sum_{\substack{H\subseteq T\text{ connected}\\|E(H)|\ge2}}z^{\ell(H)},\qquad
M_T(z)=\sum_{\substack{H\subseteq T\text{ connected}\\|E(H)|\ge2\\ \deg_H(v)=\deg_T(v)\,\forall v:\deg_H(v)\ge2}}z^{\ell(H)}.
\]
Each sum counts **distinct vertex-and-edge subtrees** of the fixed labelled tree, not isomorphism classes.

The smallest and largest cardinalities of inclusion-maximal edge-general-position sets are
\[
\boxed{\operatorname{gp}_{e}^{-}(T)=\min_{v:\deg_T(v)\ge2}\deg_T(v),\qquad
\operatorname{gp}_{e}(T)=\ell(T).}
\]
The largest value was established by Manuel, Prabha, and Klavžar; the first formula and the maximal-set census are the new parts. In particular, **all inclusion-maximal sets have one common size if and only if \(T\) is a path or a star** (including \(P_3=K_{1,2}\)).

The number of inclusion-maximal two-edge sets equals
\[
[z^2]M_T(z)=\sum_{Q}\binom{|E(Q)|}{2},
\]
where \(Q\) ranges over the maximal degree-two chains in \(T\): edge-disjoint paths whose internal vertices have degree two in \(T\) and whose endpoints have degree different from two. If \(T\) has a vertex of degree at least three, let \(A_1,\ldots,A_{\ell(T)}\) be the terminal chains from the last branching vertex to each leaf, with lengths \(a_i=|E(A_i)|\). Then the number of maximum edge-general-position sets is
\[
[z^{\ell(T)}]M_T(z)=\prod_{i=1}^{\ell(T)}a_i.
\]
When \(T\) is a path instead, this coefficient is \(\binom{m}{2}\).

## Assumptions and scope
All graphs are finite, simple, undirected, and labelled; there are no edge weights. A connected subtree always means a connected subgraph of \(T\), equivalently a connected induced vertex set with its tree edges. A leaf edge is incident to a degree-one vertex in the specified subtree. Since \(n\ge3\), every inclusion-maximal edge-general-position set has at least two edges. The *lower edge-general-position number* \(\operatorname{gp}_{e}^{-}\) means the minimum cardinality over inclusion-maximal edge-general-position sets, and is distinct from the classical maximum \(\operatorname{gp}_{e}\).

## Proof
**1. The leaf-edge bijection.** Fix \(S\) with at least two edges and let \(H=H(S)\) be its edge-hull. Every leaf edge of \(H\) lies in \(S\); otherwise deleting that leaf edge would leave a smaller connected subtree containing \(S\). If an edge \(e\in S\) were internal to \(H\) (both its endpoints nonleaves in \(H\)), minimality of \(H\) would force at least one edge of \(S\) in each component of \(H-e\). The unique path between these two selected edges passes through \(e\), contradicting edge general position. Therefore \(S\) is exactly the set of leaf edges. Conversely, a path in \(H\), and hence in \(T\), contains at most two leaf edges of \(H\). Thus the leaf edges of any connected \(H\) with at least two edges are an edge-general-position set whose hull is precisely \(H\). This proves the first bijection, including uniqueness.

**2. Maximality.** Suppose \(H\) has an internal vertex \(v\) incident to an edge \(vu\) outside \(H\). The leaf edges of the strictly larger subtree \(H+vu\) are exactly \(S\cup\{vu\}\), so \(S\) was not maximal. Conversely, suppose every internal vertex of \(H\) has no neighbor outside \(H\). Any outside edge \(f\) lies in a component attached to some leaf \(x\) of \(H\). The hull of \(S\cup\{f\}\) makes the previously selected leaf edge incident with \(x\) internal, so the first classification rules out the enlarged set. This is equivalent to inclusion-maximality. (The unique attachment point exists because \(T\) is a tree.) The displayed subtree sums follow immediately; singletons contribute \(mz\), and the empty set contributes \(1\) only to \(P_T\).

**3. Extremal sizes.** Any saturated subtree \(H\) with at least two edges has an internal vertex. Writing \(I(H)=\{v:\deg_H(v)\ge2\}\), the leaf-degree identity yields
\[
\ell(H)=2+\sum_{v\in I(H)}(\deg_H(v)-2)
=2+\sum_{v\in I(H)}(\deg_T(v)-2).
\]
Set \(d=\min_{v:\deg_T(v)\ge2}\deg_T(v)\). One summand corresponds to a vertex of degree at least \(d\), and the remaining summands are nonnegative, whence \(\ell(H)\ge d\). Taking \(H\) to be the full star at any nonleaf vertex of degree \(d\) gives a saturated subtree with exactly \(d\) leaf edges, so the lower bound is sharp. For every subtree \(H\), the same identity yields \(\ell(H)\le\ell(T)\); the whole tree attains this, proving the upper formula.

If \(T\) is a path, its only saturated subtrees with at least two edges are subpaths with at least two edges, all with exactly two leaves. If \(T\) is a star, only its whole edge set is inclusion-maximal. Otherwise, if some vertex of \(T\) has degree two and some has degree at least three, then the lower number is two while \(\ell(T)\ge3\). If there are no degree-two vertices but at least two branching vertices, the leaf-degree identity gives \(\ell(T)\ge d+1\). These cases exhaust trees that are neither paths nor stars and prove the well-edge-general-position characterization.

**4. Two-edge and maximum multiplicities.** A saturated subtree with exactly two leaves is a path, and all its internal vertices must have degree two in \(T\). Such paths are precisely subpaths of maximal degree-two chains, with at least two edges, yielding \(\sum_Q\binom{|E(Q)|}{2}\) distinct possibilities. For the maximum size, suppose \(T\) has at least one branching vertex. Equality \(\ell(H)=\ell(T)\) in the leaf-degree identity forces *every* branching vertex of \(T\) to be present in \(H\) with full original degree; otherwise a positive degree-excess contribution would be lost. All paths between branching vertices are then forced. On each terminal chain \(A_i\), the subtree can stop after any one of its \(a_i\) edges, independently. These choices give precisely \(\prod_i a_i\) distinct maximum sets. A path has no branching vertex, and every two-edge subset is maximum, giving \(\binom m2\).

**5. Explicit polynomial-time recurrences.** Root \(T\) at an arbitrary vertex \(r\). Let \(\mathrm{ch}(v)\) be the children of \(v\). Define polynomials in postorder by
\[
F_v=z+\prod_{u\in\mathrm{ch}(v)}(1+F_u)-1,\quad
L_v=\sum_{u\in\mathrm{ch}(v)}F_u,\quad
Q_v=\prod_{u\in\mathrm{ch}(v)}(1+F_u).
\]
The empty product is \(1\). Here \(F_v\) enumerates connected downward subtrees containing \(v\), with an assumed incoming parent edge and weight \(z\) per descendant leaf (not counting the incoming parent). The choice of no child makes \(v\) a leaf; choosing one or more children makes it internal. Counting each unrooted connected subtree from its unique vertex closest to \(r\) gives
\[
\boxed{P_T(z)=1+mz-mz^2+\sum_{v\in V(T)}\big(zL_v+Q_v-1-L_v\big).}
\]
The subtracted \(mz^2\) removes the one-edge subtrees, which otherwise have two leaf vertices but only one distinct edge.

For saturated subtrees use
\[
B_v=\begin{cases}z,&\mathrm{ch}(v)=\varnothing,\\ z+\prod_{u\in\mathrm{ch}(v)}B_u,&\mathrm{ch}(v)\ne\varnothing.\end{cases}
\]
If the parent edge is included, vertex \(v\) can either be a leaf, or can be internal and then must include *all* its child edges. In a saturated subtree with highest vertex \(v\ne r\), that vertex must be a leaf (its parent lies outside), so it includes exactly one child; for \(v=r\), it may additionally be internal and include all children. Therefore
\[
\boxed{M_T(z)=-mz^2+\sum_{v\in V(T)}z\sum_{u\in\mathrm{ch}(v)}B_u
+\mathbf 1_{\deg_T(r)\ge2}\prod_{u\in\mathrm{ch}(r)}B_u.}
\]
The same one-edge correction applies. For arbitrary root choice, the formulas give the same polynomials. Straightforward dense polynomial multiplication uses at most \(O(n^3)\) arithmetic operations and \(O(n^2)\) polynomial storage; they also work with exact integer coefficients.

## Verification
A standalone Python program implements both recurrences and independently checks every edge subset against all unique vertex-to-vertex paths. It verifies both complete cardinality distributions, the lower and upper numbers, and the exact two-edge and maximum-set multiplicities for every labelled tree of orders three through seven, plus 450 deterministic additional trees of orders eight through ten. Its result on the verified package is recorded in `VERIFICATION.md`. These finite tests corroborate but do not prove the infinite all-tree theorem; the argument above establishes the unrestricted claim.

## Relationship to prior work
Manuel, Prabha, and Klavžar, *The Edge General Position Problem* (first public 2021-05-10), introduced the edge version and proved the maximum cardinality \(\operatorname{gp}_e(T)=\ell(T)\) for every tree (Theorem 3.3); their proof also uses the fact that a selected non-pendant edge cannot have selected edges on both sides. That fact underlies, but does not supply, the complete maximal-set bijection, lower parameter, or two polynomial recurrences here. Tian, Klavžar, and Tan, *Extremal Edge General Position Sets in Some Graphs* (first public 2023-02-03), examine maximum-cardinality bounds and block graphs, not all inclusion-maximal tree edge sets. Manuel, Prabha, and Klavžar, *Generalization of Edge General Position Problem* (first public 2022-07-15), primarily study higher-order edge position and geodesic covering, not the stated distributions.

A prior result on **spider trees**, *All edge general-position sets of spider trees* (published mathematical research record, 2026), gives the factorization \(\prod_i(1+\ell_i z)+z^2\sum_i\binom{\ell_i}{2}\) and counts maximal sets for trees with just one branch vertex. This is genuinely contained in the arbitrary-tree theorem: on a spider, the maximal-subtree classification reduces to full choices of one edge per arm or two edges within one arm. The new theorem treats **arbitrary trees with multiple branching vertices**, which the spider theorem explicitly leaves out; for example, the tree formed by joining the centers of two three-vertex stars has \(M_T(z)=2z^3+z^4\). A different prior work on the general-position polynomial of *tree coronas* enumerates vertex sets in another graph and has a related connected-subtree counting mechanism; it does not imply the saturated-subtree characterization or lower edge parameter of the original tree.

## Limitations
The results concern ordinary undirected trees only, not edge-general-position sets in arbitrary graphs or the \(k\)-edge variant for \(k>3\). The computation is finite corroboration, not an infinite certificate or independent audit. Publication priority cannot be guaranteed by finite literature and database searches, especially against unindexed equivalent statements. The known maximum cardinality and the previously classified spider special case are not asserted to be new.

## References
1. P. Manuel, R. Prabha, S. Klavžar, *Edge general position problem*, arXiv:2105.04292 (v1 2021-05-10), Bulletin of the Malaysian Mathematical Sciences Society 45 (2022), 2997–3009, DOI 10.1007/s40840-022-01319-8. https://arxiv.org/abs/2105.04292.
2. J. Tian, S. Klavžar, E. Tan, *Extremal edge general position sets in some graphs*, arXiv:2302.01587 (v1 2023-02-03), Graphs and Combinatorics 40 (2024), Article 40, DOI 10.1007/s00373-024-02770-z. https://arxiv.org/abs/2302.01587.
3. P. Manuel, R. Prabha, S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357 (v1 2022-07-15), Art of Discrete and Applied Mathematics 8 (2025), article P1.02. https://arxiv.org/abs/2207.07357.
4. *All edge general-position sets of spider trees*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-edge-general-position-sets-of-spider-trees--96369ffaa123.
