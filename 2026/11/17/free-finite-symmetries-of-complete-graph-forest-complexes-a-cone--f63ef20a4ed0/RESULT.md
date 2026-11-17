# Free finite symmetries of complete-graph forest complexes: a coned-multigraph model

## Finding

Let \(H\) be a finite group acting **freely** on a finite nonempty set \(U\), and suppose that \(U\) has exactly \(m\geq1\) orbits. Put \(k=|H|\) and let \(s\) be the number of nonidentity elements of order two in \(H\). The complex \(\mathcal F(K_U)\) has as its vertices the unordered edges of the complete simple graph on \(U\), with a simplex for each acyclic edge set. The action on \(U\) induces a simplicial action on \(\mathcal F(K_U)\).

Construct a loopless multigraph \(Q_{m;k,s}\) on vertices \(\{0,1,\ldots,m\}\). Between every two distinct vertices in \(\{1,\ldots,m\}\), place \(k\) separately labeled parallel edges. Between vertex \(0\) and each other vertex, place \(s\) separately labeled parallel edges. An empty parallel class is omitted.

**Theorem.** There is a simplicial isomorphism from the edge-orbit fixed-point triangulation of \(|\mathcal F(K_U)|^H\) onto \(\mathcal F(Q_{m;k,s})\), hence a piecewise-linear homeomorphism
\[
 |\mathcal F(K_U)|^H\ \cong_{\mathrm{PL}}\ |\mathcal F(Q_{m;k,s})|.
\]
In particular the fixed space depends, up to PL homeomorphism, only on \((m,k,s)\), and not on the multiplication table or isomorphism type of \(H\).

If \(m=1\) and \(s=0\), the fixed space is empty. In every other case its integral homotopy type is a wedge of \(b_{m;k,s}\) spheres of common dimension
\[
 d=\begin{cases}m-2,&s=0,\\m-1,&s>0,\end{cases}
\]
with zero wedge summands interpreted as a point. The nonnegative integer \(b_{m;k,s}\) is \(T_{Q_{m;k,s}}(0,1)\), where \(T\) is the graphic-matroid Tutte polynomial. It has the explicit finite exponential formula
\[
 b_{m;k,s}=(-1)^r m![z^m]\exp\!\left(\sum_{t\geq1}\frac{(-1)^{t-1}k^{t-1}t^{t-2}(1-st)}{t!}\,z^t\right),
 \qquad r=\begin{cases}m-1,&s=0,\\m,&s>0.\end{cases}
\]
Here \(1^{-1}\) is interpreted as \(1\), as appropriate for the unique tree on one vertex. Coefficient extraction uses only terms through degree \(m\). For the exceptional case \(m=1,s=0\), the formula has the standard formal reduced-homology \((-1)\)-sphere convention, while the actual realization is empty.

For example, \(H=C_2\) and \(m=2,3,4\) produce respectively wedges of \(2\) circles, \(24\) two-spheres, and \(396\) three-spheres; \(H=C_3\) and \(m=2,3\) produce respectively two points and a wedge of \(19\) circles. The contrasting fixed spaces for \(C_4\) and \(C_2\times C_2\) at \(m=2\) are respectively \(\bigvee^4S^1\) and \(\bigvee^{24}S^1\).

## Assumptions and scope

All graphs and group actions are finite. The original complete graph is simple and undirected; the model is a multigraph whose distinct parallel edges are distinct vertices of its graphic-matroid independence complex. A forest of a multigraph has no cycles, including two-edge cycles made from parallel edges. A geometric fixed point is fixed in the actual realization, not necessarily a simplex vertex fixed pointwise. The hypothesis is free action on the original **graph vertices**. Every free finite \(H\)-set is a disjoint union of \(m\) copies of the left regular \(H\)-set. The group \(H\) need not be abelian.

## Proof

**1. Fixed-point triangulation.** In any finite simplicial complex with a simplicial finite-group action, a fixed point has constant barycentric coordinates on each group orbit of vertices. Thus the fixed-point realization is PL homeomorphic to the complex whose potential vertices are full vertex orbits that themselves form faces, and whose faces are collections of such orbits with facial union. Apply this to the edge-vertices of \(\mathcal F(K_U)\).

**2. Classify edge orbits.** Choose a basepoint in each of the \(m\) free orbits of \(U\), identifying it with \(H\). An edge between two distinct vertex-orbits \(i,j\) has a group orbit consisting of one perfect matching between those copies of \(H\); the matchings are indexed by the relative group element, giving exactly \(k\) orbits per pair. Each such matching is a forest. Within one vertex-orbit, a typical edge is \(\{g,gh\}\), with \(h\ne1\). Its full left-translation orbit is the undirected Cayley graph formed by the edges \(\{x,xh\}\). It is a disjoint union of cycles of length \(\operatorname{ord}(h)\), and is acyclic precisely when \(h\) has order two. In that case it is a perfect matching, and distinct involutions give distinct edge orbits. There are precisely \(s\) admissible internal orbits per base vertex. These eligible orbit classes are in bijection with edges of \(Q_{m;k,s}\).

**3. Classify unions.** Take a set of eligible edge orbits, and first select only its inter-orbit matchings. These matchings form a \(k\)-sheeted graph cover of a multigraph \(B\) on \(m\) orbit labels. If \(B\) contains a cycle, its finite cover contains a cycle: traveling around the cycle permutes the finite fiber, and repeatedly traversing it eventually returns to the starting point, producing a closed cycle. If \(B\) is a forest, the cover is the disjoint union of \(k\) copies of each tree component of \(B\).

Consider one component of \(B\), with \(k\) lifted tree copies. A selected internal orbit at a vertex in this component contributes \(k/2\) edges connecting the lifted copies in disjoint pairs. Hence **one** such orbit introduces no cycle. Two selected internal orbits contribute \(k\) edges between the \(k\) lifted tree components, necessarily creating a cycle (a forest joining \(k\) initial components has at most \(k-1\) additional edges). Further orbits cannot restore acyclicity. Therefore the full lifted edge union is a forest if and only if \(B\) is a forest and each component of \(B\) has at most one selected internal orbit.

**4. Identify the coned multigraph.** The same exact criterion holds for edge sets of \(Q_{m;k,s}\): its edges among \(\{1,\ldots,m\}\) form a forest \(B\), and adding edges incident to apex \(0\) preserves acyclicity precisely when at most one such edge touches each component of \(B\). Thus the eligible edge-orbit face complex is isomorphic to \(\mathcal F(Q_{m;k,s})\), establishing the PL statement.

**5. Determine homotopy types.** The forest complex of any finite multigraph is the independence complex of its graphic matroid, a shellable pure simplicial complex. It is a wedge of spheres in dimension one less than its matroid rank; the number is the Tutte evaluation \(T(0,1)\), which is zero in the contractible coloop cases. If \(s=0\), apex \(0\) is isolated and the nontrivial graph has rank \(m-1\); if \(s>0\), the model is connected with rank \(m\). If \(m=1,s=0\), there are no eligible edge orbits, so its geometric realization is empty and is treated separately.

For the explicit coefficient formula, first choose the forest \(B\) on \(\{1,\ldots,m\}\). In a tree component of \(t\) labeled vertices, Cayley's tree count (with its singleton convention) and \(k\) choices for each of its \(t-1\) inter-orbit edges give \(k^{t-1}t^{t-2}\) possibilities. The optional apex edge has \(st\) choices; the alternating signed sum over this optional edge contributes \(1-st\). The selected \(t-1\) inter-orbit edges contribute \((-1)^{t-1}\). The exponential formula over set partitions gives the displayed generating function for \(\sum_{F\text{ forest}}(-1)^{|F|}\); multiplying by \((-1)^r\) yields \(T(0,1)\). This proves the formula and all claimed boundaries.

## Verification

The companion standard-library Python script `verify.py` independently enumerates actual group edge orbits on the complete graph and compares their selected unions against the predicted multigraph forests, without using the theorem to decide acyclicity. It exhaustively checks \(104557\) selections, including actions of \(C_2,C_3,C_4,C_2\times C_2,S_3\) on one through four regular orbits where feasible. It also independently calculates signed forest sums directly on the multigraph and compares them with the set-partition generating-function formula for an array of parameters. The recorded output is in `verify.out`; the final line reads `FREE_GROUP_FOREST_CONE_EQUIVALENCE_PASS`. Finite checks support, but do not prove, the universal statement.

## Relationship to prior work

Graphic matroids and shellability give the wedge-of-spheres consequence after the new fixed-orbit model has been identified. Ardila–Castillo–Samper (2014/2015), especially the introduction and Theorem 1.3, explicitly describe matroid independence-complex shellings and the \(T(0,1)\) sphere count; that classical result is not new here. Merino–Ramírez-Ibáñez–Rodríguez-Sánchez (2012) develops Tutte-polynomial computations and parallel matroid operations, not geometric fixed spaces. DeVos–Funk–Pivotto (2014) develops gain-graph balance and its lift/frame matroids, a distinct criterion permitting certain unbalanced cycles, rather than the no-cycle criterion after taking a complete finite lifted orbit union. Cranford et al. (2020) studies weighted forests and matroid \(h\)-vectors for coned and biconed graphs, but not free-group fixed loci of complete-graph forest complexes. The new claim is the canonical simplicial identification of an all-group fixed space with a coned-multigraph forest complex and its order/involution-count universality. It is not a claim that matroid shellability, Cayley's enumeration, or Tutte theory is new.

## Limitations

The complete graph and free vertex action are essential assumptions. Nonfree actions can have different orbit internal structures; arbitrary subgraphs of complete graphs need not reduce to the model. The fixed-point classification is a PL model, not an equivariant classification for normalizer actions on the fixed space. The sphere-wedge conclusion concerns ordinary homotopy after taking fixed points, not an integral representation of any residual symmetry. The cited literature search and examined full texts do not rule out all earlier formulations of this orbit-forest result, especially in older regular-cover or voltage-graph literature. No independent mathematical audit has been performed.

## References

1. F. Ardila, F. Castillo, J. A. Samper, *The topology of the external activity complex of a matroid*, arXiv:1410.3870 (first posted 2014-10-14); especially Sections 1, 2, 4.
2. C. Merino, M. Ramírez-Ibáñez, G. Rodríguez-Sánchez, *The Tutte polynomial of some matroids*, arXiv:1203.0090 (first posted 2012-03-01); especially Sections 1–3.
3. M. DeVos, D. Funk, I. Pivotto, *When does a biased graph come from a group labelling?*, arXiv:1403.7667 (first posted 2014-03-29); especially Sections 1–2.
4. P. Cranford, A. Dochtermann, E. Haithcock, J. Marsh, S. Oh, A. Truman, *Biconed graphs, weighted forests, and h-vectors of matroid complexes*, arXiv:2005.09138 (first posted 2020-05-18); especially Sections 1–3.
