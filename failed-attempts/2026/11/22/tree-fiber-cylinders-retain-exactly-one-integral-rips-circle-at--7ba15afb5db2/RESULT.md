# Tree-fiber cylinders retain exactly one integral Rips circle at scale two

## Finding
Let \(T\) be any finite nonempty tree with \(t\) vertices, let \(n\ge7\), and put \(G=C_n\square T\), with the unit-edge shortest-path metric. For the inclusive graph-vertex Vietoris–Rips complexes \(X_r=\operatorname{VR}_{\le r}(V(G))\), the complete integral homotopy type at radius two is
\[
\boxed{X_2\simeq S^1.}
\]
Moreover the inclusion \(X_1\hookrightarrow X_2\) induces a split-surjective homomorphism of free abelian groups
\[
\mathbb Z^{n(t-1)+1}\longrightarrow\mathbb Z
\]
whose primitive kernel has rank \(n(t-1)\) and is **generated over \(\mathbb Z\) by the oriented boundaries of the \(n(t-1)\) product squares** associated with an edge of \(C_n\) and an edge of \(T\). Every cycle around the \(C_n\) factor maps to a generator of \(H_1(X_2;\mathbb Z)\), and all reduced homology outside degree one vanishes. Thus attaching any number of arbitrarily branching tree vertices changes only the number of transient degree-one classes, not the scale-two homotopy type.

## Assumptions and scope
Here \(C_n\) is a simple cycle on the residues \(\mathbb Z/n\mathbb Z\), \(T\) is a finite simple connected acyclic graph (the one-vertex tree is allowed), and vertices of \(G\) are \((i,u)\). The product distance is
\[
d_G((i,u),(j,v))=d_{C_n}(i,j)+d_T(u,v).
\]
An abstract simplex of \(X_r\) is a finite vertex set of diameter at most \(r\), with equality included. For a graph \(J\), write \(\operatorname{Cl}(J)\) for its flag (clique) complex; then \(X_2=\operatorname{Cl}(G^2)\), where \(G^2\) joins vertices of distance at most two. All homotopy and homology claims are over the **integral** spaces, not merely mod-two calculations.

## Proof
**1. A uniform contractible-strip lemma.** For every finite nonempty tree \(T\) and \(k\in\{1,2,3\}\), the inclusive radius-two Rips complex
\[
Y_{k,T}=\operatorname{VR}_{\le2}(P_k\square T)
\]
is contractible; in fact its flag complex strongly collapses to a vertex by a sequence of deletions of dominated vertices. Recall that in a flag complex a vertex \(x\) can be removed whenever there is a different vertex \(y\) whose closed neighborhood in its underlying graph contains that of \(x\); this is a simplicial strong collapse and hence a homotopy equivalence.

We prove the lemma by deleting tree leaves. If \(T\) has one vertex, \(P_k\) has diameter at most two, so \(Y_{k,T}\) is a full simplex. Otherwise choose any leaf \(\ell\) of \(T\), with its unique neighbor \(p\), and consider the graph of distance-at-most-two adjacency on \(P_k\square T\). When \(k=1\), the vertex \((0,\ell)\) is dominated by \((0,p)\). When \(k=2\), first remove \((0,\ell)\), dominated by \((1,p)\), and then \((1,\ell)\), dominated by \((0,p)\). When \(k=3\), remove \((0,\ell)\) and \((2,\ell)\), both dominated by \((1,p)\), and finally \((1,\ell)\), dominated by \((1,p)\). For verification, any vertex within product distance two of an endpoint \((0,\ell)\) has tree-coordinate \(\ell\), \(p\), or a neighbor of \(p\), with the permitted path-coordinate determined by the remaining distance; each such vertex is within distance two of \((1,p)\). The analogous symmetric endpoint and middle-column checks give the other asserted dominations. The induced graph left after deleting the leaf column is exactly the distance-two graph of \(P_k\square(T-\ell)\), because removing a leaf does not change distances between surviving tree vertices. Induction finishes the proof. These dominations hold regardless of the degree of \(p\) or any branching in \(T\).

**2. Classifying all faces using three consecutive cycle columns.** A set of cycle indices with pairwise cyclic distance at most two is contained in a set \(\{i-1,i,i+1\}\) for some \(i\), provided \(n\ge7\). Indeed, if there is a pair of indices at distance two, its two closed radius-two neighborhoods in the cycle intersect exactly in the three intervening consecutive indices; otherwise all projected distinct indices are mutually adjacent in a triangle-free cycle, so there are at most two. This argument also handles the one-index case. Since projection from \(G\) to \(C_n\) cannot increase distances, every Rips face is contained in one of the induced subcomplexes
\[
U_i=X_2[\{i-1,i,i+1\}\times V(T)],\qquad i\in\mathbb Z/n\mathbb Z.
\]
Each \(U_i\) is exactly \(Y_{3,T}\) because the cycle distances within three consecutive columns coincide with path distances. Any nonempty intersection of distinct members of the cover is induced on either one column or two adjacent columns, and is therefore \(Y_{1,T}\) or \(Y_{2,T}\). By Step 1, every nonempty finite intersection of this cover is contractible.

**3. The nerve is a circle.** The simplicial nerve of the \(n\) sets \(U_i\) is the nerve of their three-column index windows. When \(n\ge7\), a family of windows meets exactly when all its centers lie among three consecutive cycle indices with a common column. Thus the nerve is the clique complex of \(C_n^2\): its vertices and edges are the cycle indices and their distance-one and distance-two pairs, and its only two-simplices are the triples \(\{i-1,i,i+1\}\). There are no higher simplices. Every distance-two edge \(\{i-1,i+1\}\) is a free face of exactly one such triangle. Collapse each triangle along its distance-two edge; the residual complex is the ordinary cycle \(C_n\). The simplicial nerve lemma applied to the cover in Step 2 therefore gives
\[
X_2\simeq |N(\{U_i\})|\searrow |C_n|\cong S^1.
\]
This establishes the infinite-family **homotopy** claim; it does not infer it from finite Betti counts.

**4. An exact integral description of the scale-one map.** Since \(n\ge7\) and \(T\) is a tree, \(G\) has no three-cycles. Hence \(X_1\) is precisely the graph \(G\), with
\[
|V(G)|=nt,\quad |E(G)|=nt+n(t-1),\quad
H_1(X_1;\mathbb Z)\cong\mathbb Z^{n(t-1)+1}.
\]
The Cartesian product CW complex \(|C_n|\times|T|\) is formed by attaching exactly \(n(t-1)\) oriented squares to this graph along the four-edge cycles over \(e\in E(C_n)\) and \(f\in E(T)\). Since \(T\) is contractible, this cellular product deformation retracts onto \(C_n\); its cellular map \(\partial_2\) is injective, its image is a **primitive** sublattice of the integral graph cycle lattice, and the quotient is \(\mathbb Z\). In particular the square boundaries are linearly independent over \(\mathbb Z\) and form a basis for that primitive subgroup (not just a finite-index subgroup).

Each square has four vertices of pairwise graph distance at most two: adjacent vertices have distance one and opposite corners have distance two. Thus all four span a tetrahedral simplex in \(X_2\), so its oriented square boundary is null-homologous in \(X_2\). We have already identified a primitive subgroup \(L\cong\mathbb Z^{n(t-1)}\) contained in the inclusion kernel. To see the kernel is exactly \(L\), projection \(G\to C_n\) induces a simplicial map \(X_2\to\operatorname{VR}_{\le2}(C_n)\); restricting to any fixed tree vertex gives a simplicial section. The proof of Step 3 specialized to the one-vertex tree identifies \(\operatorname{VR}_{\le2}(C_n)\simeq S^1\), and its ordinary length-\(n\) cycle generates first homology (the free-skip-edge collapses retain exactly that cycle). The section therefore carries a generator of \(H_1(X_2;\mathbb Z)\), so the map \(H_1(X_1;\mathbb Z)\to H_1(X_2;\mathbb Z)\cong\mathbb Z\) is surjective and split. Its kernel has rank \(n(t-1)\). Because the quotient by \(L\) is already free of rank one and maps a generator isomorphically onto \(H_1(X_2;\mathbb Z)\), \(\ker=L\) exactly, proving integrality, primitivity, and the asserted basis.

**5. Sharpness of the cycle threshold.** For \(T\) the one-vertex tree and \(n=6\), the radius-two Rips complex is \(\operatorname{Cl}(C_6^2)\), the boundary of an octahedron, so it is \(S^2\) rather than \(S^1\). Therefore the uniform bound \(n\ge7\) cannot be relaxed to \(n\ge6\), even for the smallest possible tree.

## Verification
Run `python3 verify_tree_cylinders.py` using only the Python standard library. The verifier independently enumerates all radius-two flag faces via the shortest-path product distance, checks their three-column-window covering, independently dismantles each strip of one, two or three columns using exhaustive closed-neighborhood containment, computes every mod-two boundary-matrix rank, and checks the rank of all square-boundary cycles over \(\mathbb F_2\). Twenty test instances pass for cycle lengths \(7,8,9,10\), with tree fibers a point, a two-vertex path, a three-vertex path, a four-leaf star, and a six-vertex branched broom. The recorded final line is `VERIFY_OK 20 all-face and chain complex tests; every strip k<=3 dismantled; primitive square basis mod two`.

This computation is corroboration only: Step 1 proves all finite trees, Steps 2–3 prove all cycle lengths in scope, and Step 4 proves the integral lattice statement without relying on mod-two evidence.

## Relationship to prior work
Adamaszek et al.'s metric-gluing theorems address wedge sums and restricted isometric gluing, not the arbitrary repeatedly branched **vertex-metric Cartesian cylinder** here; their product-metric discussion uses a maximum-type metric, not the graph Cartesian distance sum. An existing high-girth prism theorem proves the width-two fiber \(T=K_2\) for arbitrary high-girth base graphs, a proper special case of this cylinder theorem. A published clique-fiber result treats \(H\square K_m\) for \(m\ge3\) with base graph of girth at least seven, but its complete fiber \(K_m\) is not a nontrivial tree for \(m\ge3\); it does not imply arbitrary tree-fiber branching and has a different carrier decomposition. The existing cyclic-clique result treats \(C_n\square K_m\), but not \(C_n\square T\) for trees with at least three vertices. Results about rectangular tori concern cycle fibers rather than contractible tree fibers. A high-girth Cartesian-product Čech theorem is for a different nerve and does not imply this Rips homotopy type or the stated primitive integral persistence map. Neither a matching name nor the absence of a database result is taken as proof of novelty; an unindexed equivalent remains possible.

## Limitations
This is a nonequivariant homotopy statement for unit-edge **graph-vertex** shortest-path metrics, **inclusive radius two**, cycle length at least seven, and an arbitrary finite tree. It does not classify intermediate non-integer scales, longer Rips scales, cycle length below seven for general trees, or non-tree fibers. It does not assert that the nerve equivalence is a simplicial collapse of the whole Rips complex. The primitive-square description is at the level of integral first homology; no assertion of a canonical functorial basis under every automorphism is made. Exhaustive finite computations cannot prove the universal theorem; the written argument provides the proof. Published and indexed comparisons are necessarily bounded, and independent validation has not been performed.

## References
1. M. Adamaszek, H. Adams, E. Gasparovic, M. Gommel, E. Purvine, R. Sazdanovic, B. Wang, Y. Wang, L. Ziegelmeier, *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224, first publicly posted 2017-12-18, https://arxiv.org/abs/1712.06224.
2. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040, first publicly posted 2021-03-01, https://arxiv.org/abs/2103.01040 (different Cartesian graph family).
3. *A uniform scale-two Vietoris–Rips collapse for prisms over graphs of girth at least seven*, published research record `4061be6b33be`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-uniform-scale-two-vietoris-rips-collapse-for-prisms-over-graph--4061be6b33be (single-edge tree fiber).
4. *Clique-fiber Rips stability for every high-girth base graph*, published research record `c8f696aa7300`, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-clique-fiber-rips-stability-for-every-high-girth-base-graph--c8f696aa7300 (complete-graph, not tree, fiber).
5. *A sharp one-circle-to-sphere-wedge transition for clique-fiber cyclic Rips complexes*, published research record `e28e5da49d34`, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-one-circle-to-sphere-wedge-transition-for-clique-fiber-c--e28e5da49d34 (cycle with clique fiber).
6. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134, first posted 2025-02-10, https://arxiv.org/abs/2502.07134 (torus-grid comparison, not the qualifying dated source).
