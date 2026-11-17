# A ten-collapse torus core and symmetry character for the pentagonal-bipyramid matching complex

## Finding

Let \(B\) be the graph of a pentagonal bipyramid (Johnson solid \(J_{13}\)), and let \(K=\mathcal M(B)\) be its ordinary matching complex. There is an explicit sequence of **ten elementary simplicial collapses**
\[
\mathcal M(B)\searrow S,
\]
where \(S\) is a connected, orientable, closed simplicial surface with fifteen vertices, forty-five edges, and thirty triangles. Consequently,
\[
\boxed{\mathcal M(B)\simeq T^2},\qquad
\widetilde H_i(\mathcal M(B);\mathbb Z)\cong
\begin{cases}\mathbb Z^2&i=1,\\\mathbb Z&i=2,\\0&\text{otherwise}.\end{cases}
\]
The original complex is two-dimensional but is **not** itself a simplicial manifold, even with boundary: it has ten edges with a unique triangular coface, and the link of \(r_0\) has four vertices of degree three rather than being a circle or interval. Its torus type is therefore not an instance of the classification of *matching complexes which themselves are manifolds*.

Moreover, the graph automorphism group is \(D_5\times C_2\). Write \(\rho\) for rotating the rim, \(\sigma\) for a rim reflection, and \(\tau\) for exchanging the apices. The full rational homology characters are determined by
\[
\begin{array}{c|rrrr}
 g&\rho^a&\rho^a\sigma&\rho^a\tau&\rho^a\sigma\tau\\\hline
 \operatorname{tr}(g\mid H_1)&2&0&0&-2\\
 \operatorname{tr}(g\mid H_2)&1&-1&-1&1
\end{array}\quad(0\le a<5).
\]
Equivalently, denoting the two one-dimensional characters of \(D_5\times C_2\) trivial on \(\rho\) by their signs on \((\sigma,\tau)\), the first rational homology is \(\chi_{+,-}\oplus\chi_{-,+}\), while second rational homology is \(\chi_{-,-}\). No nonzero positive-degree rational homology class is fixed by all symmetries.

## Assumptions and scope

All graphs are finite simple undirected graphs, and the matching complex has a vertex for **each graph edge** and a simplex for every collection of vertex-disjoint graph edges. Label the five rim graph vertices by \(i\in\mathbb Z/5\mathbb Z\) and the two apex graph vertices by \(u,v\). The graph has fifteen edges: five rim edges \(r_i=\{i,i+1\}\), five spokes \(a_i=\{u,i\}\), and five spokes \(b_i=\{v,i\}\); \(\{u,v\}\) is not an edge. The letters \(r_i,a_i,b_i\) name vertices of the matching complex, not graph vertices. Unless otherwise stated homology is reduced integral simplicial homology. The automorphism character is over \(\mathbb Q\).

## Proof

**1. Entire complex and ten free pairs.** Any matching of \(B\) uses at most three edges. Direct disjointness counting gives the complete face vector \((f_0,f_1,f_2)=(15,55,40)\). For each \(i\in\mathbb Z/5\mathbb Z\), the two matching-complex edges
\[
 e_i^+=\{a_i,b_{i+2}\},\qquad e_i^-=\{a_i,b_{i+3}\}
\]
have exactly one triangular coface, respectively
\[
 t_i^+=\{r_{i+3},a_i,b_{i+2}\},\qquad
 t_i^-=\{r_{i+1},a_i,b_{i+3}\}.
\]
For example, to extend a pair containing spokes \(a_i,b_j\), any third graph edge must be a rim edge disjoint from the two distinct rim vertices \(i,j\); for \(j=i+2\) or \(i+3\), precisely one of the five rim edges qualifies. All ten free edges and ten cofaces are distinct. Because no triangle contains two of these edges, removing their pairs sequentially preserves the free-face property. The resulting subcomplex \(S\) has \((15,45,30)\) faces.

**2. Closed connected surface.** An explicit enumeration of residual triangles shows every residual edge is in exactly two triangles. Every vertex link is a single simple cycle: the five \(r_i\) have eight-edge links, and the ten \(a_i,b_i\) have five-edge links. Two representative links, sufficient under the rotation and apex-exchange symmetries, are
\[
\begin{split}
 \operatorname{lk}_S(r_0)&=(r_2,b_4,a_3,b_2,r_3,a_2,b_3,a_4),\\
 \operatorname{lk}_S(a_0)&=(r_1,b_4,r_2,b_1,r_3),
\end{split}
\]
with cyclic order indicating link edges and closing at the starting vertex. The residual one-skeleton is connected. Consequently \(S\) is a connected closed triangulated surface, with Euler characteristic \(15-45+30=0\).

**3. Explicit integral orientation.** Let \([x,y,z]\) denote an oriented two-simplex and let \(\rho\) act by incrementing each rim index. Define
\[
\begin{split}
 z_0={}&[r_0,r_2,a_4]-[r_0,r_2,b_4]+[r_2,a_0,b_1]\\
 &-[r_3,a_0,b_1]+[r_1,a_0,b_4]-[r_2,a_0,b_4],\\
 z={}&\sum_{i=0}^{4}\rho^i z_0.
\end{split}
\]
The thirty summands are precisely the thirty residual triangles, each with coefficient \(\pm1\), and direct cancellation gives \(\partial_2 z=0\) **over the integers**. Thus \(S\) is orientable. The classification of connected closed surfaces with Euler characteristic zero identifies \(S\cong T^2\). Elementary simplicial collapses are strong deformation retractions, giving the claimed homotopy type and torsion-free homology. The original ten free edges and the branching vertex link \(\operatorname{lk}_K(r_0)\) show that \(K\) is not itself a triangulated surface, even with boundary; since its first integral homology is nonzero, its two-dimensional pure complex is also not shellable.

**4. Symmetry character.** The five rim vertices of \(B\) have graph degree four and the apices degree five, hence every automorphism preserves these two parts. It is therefore precisely \(D_5\times C_2\), generated by \(\rho,\sigma,\tau\). The ten collapse pairs are preserved as a family by the group, so the action restricts to the torus subcomplex \(S\). The explicit fundamental cycle \(z\) shows that the action on \(H_2(S;\mathbb Q)\) is orientation preserving exactly when the reflection indicator and apex-swap indicator have the same parity; thus its sign is \((-1)^{\mathrm{reflection}+\mathrm{swap}}\).

For a simplicial automorphism \(g\), let \(C_k(g)\) be the *signed* number of matching simplices of dimension \(k\) fixed setwise, with their induced orientation signs. The reduced Lefschetz identity yields
\[
 \operatorname{tr}(g\mid H_2)-\operatorname{tr}(g\mid H_1)
 = C_0(g)-C_1(g)+C_2(g)-1.
\]
For representatives \(\sigma,\tau,\sigma\tau\), the three signed chain traces \((C_0,C_1,C_2)\) are respectively \((3,1,-2)\), \((5,5,0)\), and \((1,-5,-2)\). In combination with the above orientation signs they give first-homology traces \(0,0,-2\). The action of \(\rho\) on the two-dimensional rational space \(H_1\) is trivial: its order is five, and every nontrivial rational irreducible representation of \(C_5\) has dimension four. The rotation also preserves \(z\). Hence every element has the character values in the table. Since \(\sigma\) and \(\tau\) are commuting involutions and each has zero trace on the two-dimensional first homology while their product has trace \(-2\), their eigenspaces yield exactly \(\chi_{+,-}\oplus\chi_{-,+}\). The top homology is \(\chi_{-,-}\). Neither module has a trivial summand.

## Verification

The accompanying `verify.py` independently constructs all matchings from the fifteen graph edges and asserts the full face vector; it checks every unique free coface, distinctness of all ten pairs, the original branching vertex link, the complete residual surface, each edge incidence, both link types and connectedness. It then constructs the explicit signed integral orientation cycle and checks the thirty coefficients and **every** integer boundary coefficient. All twenty graph automorphisms are checked on the full original complex and collapsed torus, including signed Lefschetz traces and the orientation action. Independent mod-two boundary ranks are \(14\) and \(39\), recovering Betti numbers \((0,2,1)\). Execute `python3 verify.py` in a directory containing the file. The recorded output is provided as `verification_output.txt` and ends in `VERIFY_OK`.

The key topological conclusion follows from the explicit free pairs and exact surface proof; finite-modular homology checks are redundant corroboration, not a substitute for the integral argument. The verifier requires only the Python standard library.

## Relationship to prior work

Bayer, Goeckner, and Jelić Milutinović, *Manifold Matching Complexes* (arXiv:1906.03328), characterize graph matching complexes that are **themselves** homology manifolds; their Theorem 4.2 contains a torus realized by the matching complex of \(K_{3,4}\). That theorem does not classify complexes merely **homotopy equivalent** to a torus, and the original present complex has ten free edges and branching vertex links, so it does not meet their manifold hypotheses, even allowing boundary.

Goeckner, Herr, Jones, and Rowlands, *A characterization of two-dimensional Buchsbaum matching complexes* (arXiv:2110.11302), classify Buchsbaum matching complexes but do not provide this free-collapse torus core or the complete symmetry character. Bayer, Jelić Milutinović, and Vega, *Matching Complexes of Outerplanar Graphs* (arXiv:2411.04601), consider outerplanar graphs; the present bipyramid contains a \(K_{2,3}\) subgraph (two apices and any three rim vertices) and is not outerplanar. The previously published seven-vertex torsion census (published-finding corpus, identifier below) characterizes first-homology torsion, not complete homotopy types or dihedral homology characters; its theorem neither states nor implies this torus equivalence.

## Limitations

This is a statement about one canonical seven-vertex graph and its ordinary matching complex, not a classification of all bipyramid matching complexes or all complexes homotopy equivalent to surfaces. The rational character computation does not classify integral equivariant modules. The combinatorial surface proof is exhaustive for this explicitly defined graph; it should not be extrapolated to larger graphs. No claim is made that no other graph has a matching complex homotopy equivalent to a torus. Equivalent observations in unindexed literature remain possible, and independent external validation has not been performed.

## References

1. M. Bayer, B. Goeckner, M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328 (first public 2019-06-07), especially Theorem 4.2. https://arxiv.org/abs/1906.03328
2. B. Goeckner, F. Herr, L. Jones II, R. Rowlands, *A characterization of two-dimensional Buchsbaum matching complexes*, arXiv:2110.11302 (first public 2021-10-21), Theorem 4.1. https://arxiv.org/abs/2110.11302
3. M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (first public 2024-11-07), Theorem 2. https://arxiv.org/abs/2411.04601
4. *Sharp edge threshold for torsion in matching complexes of seven-vertex graphs*, public mathematical record, identifier `2026/10/11/SCOPE-sharp-edge-threshold-for-torsion-in-matching-complexes-of-seven--f0ba41f16bfb`, Results and Proof. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-edge-threshold-for-torsion-in-matching-complexes-of-seven--f0ba41f16bfb
