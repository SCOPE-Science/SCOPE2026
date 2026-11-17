# Homotopy of three-tuplings of triple graph joins and an equal-face-vector separation

## Finding
Let \(G_1,G_2,G_3\) be finite, connected, simple, **one-dimensional simplicial complexes**, each with at least one edge. Their vertex and edge counts are \(v_i\) and \(e_i\). Put \(X=G_1*G_2*G_3\), and let \(D^3(X)\) be the three-tupling: vertices are the three-element faces of \(X\), and two vertices are adjacent exactly when their disjoint six-element union is a face of \(X\). Then there is a **canonical graph isomorphism**
\[
D^3(X)\cong (G_1\times G_2\times G_3)\;\sqcup\;\bigsqcup_{i=1}^{3}(G_i\times K_{e_j,e_k}), \qquad \{i,j,k\}=\{1,2,3\},
\]
where \(\times\) denotes the categorical/direct product of *graphs*, and the two shores of \(K_{e_j,e_k}\) are indexed by the individual edges of \(G_j\) and \(G_k\). In particular, the three-tupling is a graph (it has no higher simplices).

The formula below determines the **complete integral homotopy type, component by component**, including cases with unequal bipartition sizes. Let \(B=\{i:G_i\text{ is bipartite}\}\), \(b=|B|\), \(P=e_1e_2e_3\), and \(t=2^{\max\{b-1,0\}}\). The first product has \(t\) connected components. If \(b=0\), it has one component with \(V=v_1v_2v_3\) and \(E=4P\). Otherwise choose a two-coloring \(V(G_i)=B_i^0\sqcup B_i^1\) for every \(i\in B\). Each equivalence class \([\eta]\in\{0,1\}^B/(\eta\sim1-\eta)\) labels one component, whose counts are
\[
 V_{[\eta]}=\Bigl(\prod_{i\notin B}v_i\Bigr)\left(\prod_{i\in B}|B_i^{\eta_i}|+\prod_{i\in B}|B_i^{1-\eta_i}|\right),\qquad E_{[\eta]}=\frac{4P}{t}.
\]
For each \(i\) with \(\{i,j,k\}=\{1,2,3\}\), the other factor \(G_i\times K_{e_j,e_k}\) has one connected component if \(G_i\) is nonbipartite; it has counts \(V=v_i(e_j+e_k)\), \(E=2P\). If \(G_i\) is bipartite with color class sizes \(a_i,c_i\), it has two components, with respective counts
\[
(V,E)=(a_i e_j+c_i e_k,P),\qquad (V,E)=(a_i e_k+c_i e_j,P).
\]
**Every** listed component is homotopy equivalent, integrally, to a wedge of \(E-V+1\) circles (a zero-fold wedge is a point). In particular, the total number of components is \(t+3+b\), and the total first Betti number is
\[
\beta_1=10P-\left(v_1v_2v_3+\sum_{i=1}^{3}v_i(e_j+e_k)\right)+(t+3+b),\qquad\{i,j,k\}=\{1,2,3\}.
\]
All higher integral homology groups vanish and every component has free fundamental group.

A **fixed-face-vector separation** follows. Let \(L=C_5\) with one pendant edge attached to a vertex, regarded as a one-dimensional simplicial complex, and let \(C_3\) be the unfilled triangle boundary. The three complexes
\[
X_0=C_6*C_6*C_3,\quad X_1=L*C_6*C_3,\quad X_2=L*L*C_3
\]
are all homotopy equivalent to \(S^5\), have identical face vectors, and satisfy
\[
\#\pi_0(D^3(X_0))=7,\qquad\#\pi_0(D^3(X_1))=5,\qquad\#\pi_0(D^3(X_2))=4.
\]
Their three-tuple graphs all have exactly 252 vertices and 1080 edges. Thus neither the homotopy type nor the entire face vector of the original complex determines the connectedness of its three-tupling. The componentwise ranks, in ascending order, are respectively \((82,82,82,82,163,163,181)\), \((82,82,163,181,325)\), and \((163,163,181,325)\).

## Assumptions and scope
Each factor is a one-dimensional abstract simplicial complex: in particular, even if its underlying graph contains a triangle, that three-set is **not** a face. The three vertex sets are disjoint. Every factor is finite, connected, loopless and has at least one edge. A graph product contains a vertex for every tuple, with adjacency when all corresponding coordinates are adjacent. The convention \(\bigvee^0 S^1\) means one point. The theorem is **not** a statement about the clique complex of an arbitrary graph join, since triangles inside factors would alter the face set.

## Proof
**1. Dimension and decomposition.** Every simplex of \(X\) contains at most two vertices of each graph factor; hence \(\dim X=5\), and a simplex of \(D^3(X)\) would need at least nine distinct original vertices to have dimension two, which is impossible. The vertices of \(D^3(X)\) are of exactly two sorts: one vertex in each factor, called type \((1,1,1)\); or an edge in one factor and a vertex in another, called type \((2,1,0)\). Every six-element face of \(X\) consists of one edge in each factor. The complement of a type \((1,1,1)\) triangle within a six-face is another triangle of that type, and adjacency requires an edge in **each** \(G_i\), precisely the direct product \(G_1\times G_2\times G_3\). The complement of type \((2,1,0)\), with the singleton in factor \(i\), is type \((0,1,2)\) with the same singleton factor; their two singleton vertices must form an edge of \(G_i\), while the two edge choices in the other factors may be arbitrary. These vertices and edges form exactly \(G_i\times K_{e_j,e_k}\). Neither sort is adjacent to the other, and distinct singleton factors cannot meet. This proves the displayed disjoint graph decomposition without omissions.

**2. Components of a direct product.** For finite connected graphs with at least one edge, two vertices have walks of all sufficiently large admissible lengths: in a bipartite factor the parity is uniquely prescribed by the endpoint colors; in a nonbipartite factor both parities become possible by detouring through an odd cycle. Lengths can always be increased by two by retracing an edge. An edge of a direct product advances all coordinates simultaneously, so a product walk exists exactly when its coordinate walks can have one common length. Consequently, if there are \(b\) bipartite factors, the relative color parity vector is the complete component invariant. It gives \(2^{b-1}\) components for \(b\ge1\) and one when \(b=0\). For the first threefold product these classes are the stated \([\eta]\), with two complementary color patterns per component. For \(G_i\times K_{e_j,e_k}\), the complete bipartite factor supplies one bipartition, so there is one component for nonbipartite \(G_i\), and two for bipartite \(G_i\). The walk argument proves connectivity within every listed class, including graphs with leaves and nonuniform degrees.

**3. Exact edges and vertices per component.** The first product has \(v_1v_2v_3\) vertices. Every triple of unoriented factor edges produces exactly four distinct edges in this product, giving \(4P\) edges. For a fixed triple, exactly \(4/t\) of its product edges lie in each parity class, so each component has \(4P/t\) edges. The displayed \(V_{[\eta]}\) formula counts precisely the two compatible color patterns. The product \(G_i\times K_{e_j,e_k}\) has \(v_i(e_j+e_k)\) vertices and \(2e_i e_j e_k=2P\) edges; when \(G_i\) is bipartite, one edge from every pair of factor edges belongs to each parity class and the vertex counts are \(a_ie_j+c_ie_k\) and \(a_ie_k+c_ie_j\). Summation gives the total \(f\)-vector and component count. A connected finite graph contracts a spanning tree to a wedge of \(E-V+1\) loops, with no torsion or higher homotopy except that inherited from circles. This proves the entire integral homotopy classification.

**4. Equal-face-vector separation.** Both \(C_6\) and \(L=C_5\) with one attached leaf have six vertices, six edges and exactly one cycle, so each realizes a circle up to homotopy. The unfilled \(C_3\) also realizes a circle. Their joins all realize the join of three circles, hence \(S^5\); face polynomials multiply under simplicial joins, so all three \(X_i\) have face polynomial \((1+6z+6z^2)^2(1+3z+3z^2)\). The first two graph factors in \(X_0\) are bipartite and in \(X_1\) only one is bipartite; none is bipartite in \(X_2\). Hence \(b=2,1,0\), giving exactly \(7,5,4\) components by the proved formula. Substitution of \((v_1,e_1,v_2,e_2,v_3,e_3)=(6,6,6,6,3,3)\) yields the common graph face numbers \((252,1080)\). The full rank lists follow by the component counts above.

## Verification
The self-contained `verify.py` (Python standard library, no network or external packages) constructs every three-element face of the join **independently** from its factor edge lists. For every triple of selected factor edges it enumerates all complementary pairs of triangles and inserts those edges into the directly reconstructed three-tupling. It then determines components by breadth-first search and compares their complete \((V,E,E-V+1)\) triples to an independent formula based on graph two-coloring. It checks nine parameter instances, including all three equal-face-vector witness complexes, the all-square case, disconnected-factor boundary cases of the categorical product, and unequal-bipartition trees. Expected terminal line: `THREE_GRAPH_JOIN_TRIPLING_PASS`. This exhaustive testing is confined to those finite examples; the universal proof is the preceding walk argument and exact face classification.

## Relationship to prior work
Lesh, Schreiner and Wahl defined simplicial \(r\)-tupling and proved weak Cohen–Macaulay connectivity estimates in *The double of a simplicial complex*, arXiv:2506.10436, initial public release June 12, 2025, Definition 2.1 and Theorem A. Their theorem does not classify the components of triple graph joins or give an equal-face-vector separation. Weichsel's classical connectedness theorem for direct graph products, and the later analysis of possible nonisomorphic bipartite-product components by Jha, Klavžar and Zmazek, supply standard context; the proof here rederives the needed component criterion by synchronized walks. An existing classification of \(D^3(C_m*C_n*C_\ell)\) concerns only three polygon boundaries. The formula here contains that family as the special case of connected 2-regular graphs but extends to **all** connected one-dimensional factors; unequal bipartition sizes produce component ranks unavailable in the cycle case, and the three equal-face-vector examples involve non-cycle factors. A published result on the tupling of a join of discrete color classes with \(2r+1\) classes has different face constraints and cannot imply this classification; cyclic-polytope triple-tuplings similarly use a different six-face family.

## Limitations
The factors must be connected, one-dimensional simplicial complexes each with an edge; disconnected graphs or factors containing filled triangles are not covered. This is ordinary integral, nonequivariant homotopy; it does not classify automorphism representations or functorial maps between components. The witness complexes have the homotopy type of spheres but the two examples with pendant edges are not triangulated manifolds. The literature comparison cannot rule out unindexed or differently worded equivalent theorems; independent validation has not been conducted.

## References
1. K. Lesh, B. Schreiner and N. Wahl, *The double of a simplicial complex*, arXiv:2506.10436v1 (12 June 2025), Definition 2.1 and Theorem A. https://arxiv.org/abs/2506.10436; author-hosted full text https://web.math.ku.dk/~wahl/Doubling.pdf.
2. P. M. Weichsel, *The Kronecker product of graphs*, Proceedings of the American Mathematical Society **13** (1962), 47–52, DOI:10.1090/S0002-9939-1962-0133816-6.
3. P. K. Jha, S. Klavžar and B. Zmazek, *Isomorphic components of Kronecker product of bipartite graphs*, Discussiones Mathematicae Graph Theory **17** (1997), 301–309, DOI:10.7151/dmgt.1057.
