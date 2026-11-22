# The icosahedral geodesic general-position complex is \(\bigvee^{6}S^{1}\vee\bigvee^{21}S^{2}\)

## Finding

Let \(I\) be the graph of the regular icosahedron. The simplicial complex \(\operatorname{GP}(I)\) comprises precisely those subsets \(S\subseteq V(I)\) for which no three distinct elements of \(S\) lie on a common shortest path in \(I\). Then
\[
\left|\operatorname{GP}(I)\right|\simeq \bigvee^{6}S^{1}\vee\bigvee^{21}S^{2}.
\]
In particular, all reduced integral homology vanishes apart from \(\widetilde H_1\cong\mathbb Z^6\) and \(\widetilde H_2\cong\mathbb Z^{21}\). The complete face vector in dimensions zero to three is \((12,66,100,30)\).

## Assumptions and scope

All graph distances are shortest-path distances in the **original** finite simple undirected graph, not distances in an induced subgraph. A triple of distinct vertices \(\{a,b,c\}\) is prohibited exactly when one of the triangle inequalities among the three distances is an equality. Because this is a downward-closed condition, all higher faces are determined by the prohibited triples. A zero-dimensional simplex is counted as a vertex, and homotopy equivalence means ordinary nonequivariant homotopy equivalence of the geometric realizations.

For an unambiguous labeled graph, use vertices \(0,1,\ldots,11\), with poles \(0,11\) and two belts \(1,\ldots,5\), \(6,\ldots,10\). Indices on each belt are reduced modulo five. The pole \(0\) joins every upper vertex, pole \(11\) joins every lower vertex; each belt forms a pentagon. Upper vertex \(1+j\) joins lower vertices \(6+j\) and \(6+(j-1\bmod5)\). This gives 30 edges, degree five throughout and diameter three.

## Proof

**1. An embedded spherical core.** Let \(K\) contain all 12 vertices, the 30 unordered pairs at graph distance two, and the 20 triples whose three pairwise distances are all two. Such triples are admissible, so \(K\subseteq\operatorname{GP}(I)\). Every edge of \(K\) occurs in precisely two triangles and every vertex link is a connected five-cycle. Its one-skeleton is connected and \(\chi(K)=12-30+20=2\). Consequently \(K\) is a connected closed combinatorial surface of Euler characteristic two, hence \(|K|\cong S^2\). These complete finite combinatorial assertions are checked by `verify_icosa_gp.py`.

**2. All graph edges can be added without introducing loops.** Each of the 30 original graph edges \(uv\) admits a vertex \(w\) at graph distance two from both endpoints. The triple \(uvw\) has distance pattern \((1,2,2)\), hence is admissible. The two edges \(uw,vw\) already lie in \(K\). Form a subcomplex \(K'\) by adjoining to \(K\), for each original graph edge \(uv\), its edge and one such triangle. Within \(K'\), the edge \(uv\) is a free face of that single chosen triangle, so the pairs collapse successively to \(K\). In particular, \(K'\) is simply connected.

**3. The remaining higher cells cannot create fundamental-group generators.** The full complex has 66 edges: the 30 distance-two core edges, 30 original adjacency edges, and six distance-three (antipodal) pairs. Every pair at distance three belongs to no admissible triple: any third vertex lies on a shortest path between its antipodes. Remove those six isolated-from-higher-faces edges to obtain \(X\). The subcomplex \(K'\subseteq X\) has the entire one-skeleton of \(X\). Since every simplex of \(X\setminus K'\) has dimension at least two, attaching them cannot increase \(\pi_1\). Therefore \(X\) is simply connected.

**4. Collapse to two dimensions.** The full complex has 30 tetrahedra. Each tetrahedron possesses exactly two triangular faces lying in no other tetrahedron. Choose one such triangle per tetrahedron. The chosen triangles are all distinct, and each pair is an elementary free-face collapse; none of the six antipodal edges lies in a tetrahedron. Hence \(X\) simplicially collapses onto a connected, simply connected two-dimensional CW complex.

**5. Homotopy type and antipodal edges.** Exhaustive face enumeration gives the face vector \((12,66,100,30)\). After deleting the six antipodal edges, \(\chi(X)=12-60+100-30=22\). For a connected, simply connected two-complex, \(H_2(X;\mathbb Z)\) is free of rank \(\chi(X)-1=21\). By Hurewicz, a basis lifts to \(\pi_2\); the associated map \(\bigvee^{21}S^2\to X\) is a homology equivalence between simply connected CW complexes and hence a homotopy equivalence. Finally, the six pairwise distinct antipodal edges attach as one-cells with both endpoints in connected \(X\), and no higher simplex meets them. Attaching each such edge wedges on one circle. Thus
\[
\left|\operatorname{GP}(I)\right|\simeq\bigvee^6S^1\vee\bigvee^{21}S^2.
\]

## Verification

Execute `python3 verify_icosa_gp.py` using the Python standard library. It independently generates the labeled icosahedral graph, checks the complete 4096-subset face census, confirms all 120 forbidden triples and all face dimensions, checks every incidence of the spherical distance-two core, records 30 witnesses for the free triangle-edge pairs and checks 30 free triangular faces for the tetrahedral collapses. It also checks that the six antipodal edges occur in no triangle. The listed finite assertions, together with the explicit topological deductions above, establish an integral homotopy equivalence, not just field-valued Betti numbers.

## Relationship to prior work

The graph general-position condition is from Manuel and Klavžar [1]. The characterization of general-position vertex sets in Anand and collaborators [2] supplies general structural context. Published work on the **ordinary independence** complex of the icosahedral graph gives a two-sphere with six antipodal one-cells, homotopy equivalent to \(S^2\vee\bigvee^6S^1\); that is a different subcomplex and does not determine the extra 20 two-sphere summands introduced here. The icosahedral two-independence/dissociation complex and distance-neighborhood complexes also have different admissible simplices, so their homotopy calculations do not imply this claim. Searches and available primary texts revealed no full general-position-complex calculation for \(I\).

## Limitations

The result concerns only the ordinary icosahedral graph, with its **intrinsic graph** geodesics. It does not determine the full automorphism representation on integral homology or generalize to other polyhedral graphs. Indexed discovery cannot rule out all unindexed equivalent publications. No independent external audit has been performed.

## References

1. P. Manuel and S. Klavžar, *Graph theory general position problem*, original public arXiv posting 2017-08-30, https://arxiv.org/abs/1708.09130.
2. B. S. Anand, U. Chandran S. V., M. Changat, S. Klavžar, and E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460, https://arxiv.org/html/1812.08460v2.
3. E. W. Weisstein, *Icosahedral Graph*, MathWorld, https://mathworld.wolfram.com/IcosahedralGraph.html (structural graph data).
