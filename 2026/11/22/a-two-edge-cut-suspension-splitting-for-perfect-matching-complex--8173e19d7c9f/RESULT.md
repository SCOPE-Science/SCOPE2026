# A two-edge-cut suspension splitting for perfect-matching complexes

## Finding and conventions

For a graph \(G\) admitting a perfect matching, let \(\mathcal P(G)\) be the simplicial complex of subsets of its perfect matchings. The empty graph has one perfect matching, the empty matching; its complex \(\{\varnothing\}\) has empty realization and is the **unit for simplicial join**. Write \(\Sigma_{\mathrm{s}}A=S^0*A\), where \(S^0\) is a complex with two vertices and no edge between them. If \(|A|\ne\varnothing\), this realizes the unreduced suspension of \(|A|\); if \(A=\{\varnothing\}\), it realizes \(S^0\). Use one suspension pole as basepoint.

Let \(G_1,G_2\) be finite simple graphs on disjoint even vertex sets. Choose distinct \(a,b\in V(G_1)\) and distinct \(c,d\in V(G_2)\), with \(ab\in E(G_1)\), \(cd\in E(G_2)\). Suppose both induced punctured graphs \(G_1-\{a,b\}\), \(G_2-\{c,d\}\) have perfect matchings; appending the respective internal edges shows the original sides do too. Form \(H\) by joining the two graphs with just \(ac\) and \(bd\). Put
\[
K_0=\mathcal P(G_1)*\mathcal P(G_2),\qquad
A=\mathcal P(G_1-\{a,b\})*\mathcal P(G_2-\{c,d\}).
\]
Then
\[
|\mathcal P(H)|\simeq |K_0|\vee |\Sigma_{\mathrm{s}}A|,
\]
with the vertex \(ab\) as wedge point in \(K_0\). The splitting identifies the inclusion of \(|K_0|\) with the first wedge inclusion up to homotopy, so it splits reduced integral homology in every degree. No connectedness assumption is needed on \(|A|\). In particular, if \(G_1=G_2=K_6\), the homotopy type is \(\bigvee^{4}S^2\vee\bigvee^{256}S^3\).

## Proof

The number of crossing edges in a perfect matching has the parity of \(|V(G_1)|\), since all internally matched vertices contribute in pairs. Thus a perfect matching uses neither crossing edge or both. With \(e=ac, f=bd\), this gives the simplicial decomposition
\[
\mathcal P(H)=K_0\cup(\Delta(\{e,f\})*A).
\]
The intersection is exactly \(A\): a face in the intersection avoids \(e,f\), and each face in \(A\) extends on the original sides by appending \(ab,cd\) to the punctured perfect matchings. Likewise each face \(\sigma\in A\) can be augmented by the vertex \(ab\) in \(K_0\), so the inclusion factors through the cone star of \(ab\) and is nullhomotopic to \(ab\).

Replace the second piece by the cone \(\{e\}*A\), interpreting \(\{e\}\) as the single-vertex simplex. The simplicial retraction sending \(f\) to \(e\) and fixing all other vertices gives a deformation retraction on realizations: on each simplex its image and the original simplex lie in one simplex, allowing a linear homotopy fixed off the simplices containing \(f\). For \(|A|\ne\varnothing\) we obtain the mapping cone of \(|A|\hookrightarrow|K_0|\). Homotoping the attachment to the constant map at \(ab\) gives a homotopy equivalence of mapping cones relative to \(|K_0|\) (equivalently, use the homotopy pushout model). The mapping cone of the constant map is \(|K_0|\) with the unreduced suspension of \(|A|\) wedged at a pole. For \(A=\{\varnothing\}\), the retraction gives \(|K_0|\) disjoint from the vertex \(e\), which is exactly the claimed wedge with \(S^0\). This covers the two \(K_2\) sides, for which \(H=C_4\) and the two perfect matchings give disjoint intervals. In all cases the reduced homology splitting follows from the inclusion of the first wedge summand.

For \(K_6\) every matching extends to a perfect matching. Its complex has 15 vertices, 45 edges and 15 triangles. Each edge of the complex belongs to just one triangle, since the two unused graph vertices have a unique pairing. Collapsing the triangles across one free edge each leaves a connected graph (the original complex has connected disjointness graph on its edge-vertices) with 15 vertices and 30 edges, hence a wedge of 16 circles. Each punctured \(K_6\) is \(K_4\), with complex three disjoint segments, homotopy equivalent to three points. Their join is homotopy equivalent to \(K_{3,3}\), a wedge of four circles. The join of the two wedges of 16 circles is the suspension of their smash product, hence a wedge of 256 three-spheres. The splitting adds the suspension of the four-circle wedge, producing four two-spheres. This proves an integral homotopy statement, not just numerical ranks.

## Scope and prior work

The general null-attachment splitting is standard; a perfect-matching-complex formulation via a vertex link and deletion appears in §2 of Chandrakar et al., [Perfect Matching Complexes of \(3\times 2n\) Grid Graph](https://arxiv.org/abs/2611.18058). The graph-specific ingredients here are the parity dichotomy, the exact punctured join as the attaching subcomplex, and the coning vertex afforded by the internal endpoint edges. The identification of ordinary and perfect-matching complexes on complete even graphs is also known (Bayer, Jelić Milutinović, and Vega, [Perfect Matching Complexes of Honeycomb Graphs](https://arxiv.org/abs/2209.02803), §1). No equivariant or canonical wedge equivalence is asserted, and no extension to general cuts or absent internal endpoint edges is claimed.
