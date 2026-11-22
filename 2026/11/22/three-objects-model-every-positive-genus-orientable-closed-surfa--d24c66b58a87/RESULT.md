# Three objects model every positive-genus orientable closed surface

## Finding

Let \(\Sigma_g\) be the closed connected orientable surface of genus \(g\ge 1\). For a space \(X\), define \(\nu(X)\) to be the minimum number of objects of a finite acyclic category \(\mathcal C\) whose classifying space \(B\mathcal C\) is homotopy equivalent to \(X\). Then, for every integer \(g\ge 1\),

\[
\boxed{\nu(\Sigma_g)=3.}
\]

This equality is attained by an explicit three-object category whose nerve simplicially collapses (as a regular \(\Delta\)-complex) to a closed orientable genus-\(g\) surface. The known genus-zero case \(\nu(S^2)=3\) is not claimed as new.

## Assumptions and scope

Fix an integer \(g\ge1\), and put \(r=2g+1\), an odd integer at least three. All indices below are in \(\mathbb Z/r\mathbb Z\). A category is acyclic when its only endomorphisms are identities and no two distinct objects have morphisms in both directions. The nerve is the regular \(\Delta\)-complex of chains of nonidentity morphisms; its realization is the classifying space. A collapse in this context removes a two-simplex together with a one-simplex appearing as a face of that two-simplex alone. No assertion of homeomorphism is made for the nerve *before* these collapses.

## Proof

**Step 1: a finite three-object category.** Take objects \(0,1,2\). The nonidentity morphisms are

\[
f_i:0\to1,\qquad g_j:1\to2,\qquad h_k:0\to2\quad (i,j,k\in\mathbb Z/r\mathbb Z),
\]

and separate morphisms \(u_{ij}:0\to2\) for every ordered pair \((i,j)\) for which \(j\not\equiv i,i+1\pmod r\). Declare the complete composition table

\[
g_j\circ f_i=\begin{cases}
h_i,&j=i,\\
h_{i+2},&j=i+1,\\
u_{ij},&j\not\equiv i,i+1\pmod r.
\end{cases}
\]

Together with identities, this makes a category, because no three nonidentity arrows can be composed. All nonidentity arrows point from smaller to larger object, so the category is acyclic. There are \(3\) objects and \(r^2+r\) nonidentity arrows: \(r\) arrows of each of the \(f,g,h\) types and \(r(r-2)\) private arrows of the \(u\) type. Its nerve has \(r^2\) nondegenerate two-simplices, one for each composable pair \((f_i,g_j)\), with oriented boundary

\[
\partial[f_i,g_j]=[g_j]-[g_j\circ f_i]+[f_i].
\]

**Step 2: elementary collapses.** Each private arrow \(u_{ij}\) occurs in exactly one two-simplex, namely \([f_i,g_j]\), because its label is unique and is never a composite in the other cases. Thus the pair consisting of that two-simplex and its edge \(u_{ij}\) is a free-face pair and can be removed by an elementary collapse. Remove these \(r(r-2)\) pairs. No other cells are removed. The resulting \(\Delta\)-complex \(Y_r\) has precisely \(3\) vertices, \(3r\) edges \(f_i,g_j,h_k\), and the \(2r\) triangles

\[
A_i=[f_i,g_i],\qquad B_i=[f_i,g_{i+1}].
\]

Their boundary formulas are

\[
\partial A_i=g_i-h_i+f_i,\qquad
\partial B_i=g_{i+1}-h_{i+2}+f_i.
\]

**Step 3: the surface condition, including every vertex link.** Every edge of \(Y_r\) is incident to exactly two triangles: \(f_i\) to \(A_i,B_i\), \(g_j\) to \(A_j,B_{j-1}\), and \(h_k\) to \(A_k,B_{k-2}\). For a triangulated \(\Delta\)-complex with three distinct vertices on every triangle, the link of a vertex has one link vertex for each incident edge and one link edge for each incident triangle. At object \(0\), the link is the bipartite graph with vertices \(f_i,h_k\) and edges \(f_i-h_i\), \(f_i-h_{i+2}\). Because \(r\) is odd, addition by two generates all indices modulo \(r\), and this is a single \(2r\)-cycle. At object \(1\), the link has vertices \(f_i,g_j\) and edges \(f_i-g_i\), \(f_i-g_{i+1}\), a single \(2r\)-cycle. At object \(2\), the link has vertices \(g_j,h_k\) and edges \(g_j-h_j\), \(g_j-h_{j+1}\), again a single \(2r\)-cycle. Since all vertex links are circles and each edge meets two faces, the realization \(|Y_r|\) is a closed two-manifold. The one-skeleton contains paths between the three objects, so this surface is connected.

**Step 4: orientability and genus.** The integral two-chain

\[
z=\sum_{i\in\mathbb Z/r\mathbb Z}(A_i-B_i)
\]

has zero boundary, since \(\sum_i(g_i-g_{i+1}-h_i+h_{i+2})=0\). Its coefficient is \(\pm1\) on every triangle, and the two faces incident to any edge give opposite oriented incidence. Hence it defines a global orientation. Finally,

\[
\chi(Y_r)=3-3r+2r=3-r=2-2g.
\]

The classification of connected closed orientable surfaces identifies \(|Y_r|\) with \(\Sigma_g\). Since the original nerve collapses to \(Y_r\), its classifying space is homotopy equivalent to \(\Sigma_g\). This proves \(\nu(\Sigma_g)\le3\).

**Step 5: sharpness.** An acyclic category with at most two objects has no chain of two nonidentity arrows. Therefore its classifying space is at most one-dimensional and has zero integral second homology. But \(H_2(\Sigma_g;\mathbb Z)\cong\mathbb Z\). Thus \(\nu(\Sigma_g)\ge3\), completing the proof.

## Verification

The proof is uniform for every odd \(r\ge3\) and does not use a finite-data extrapolation. The accompanying standard-library Python checker independently constructs the complete composition table for \(r=3,5,7,9,11,13,15\). It checks that each discarded composite arrow is a genuine private free edge; that the retained edges each have two incident faces; that the signed integral fundamental chain has zero boundary; that each of the three vertex links is exactly one cycle; and that the Euler characteristic matches the genus. All seven cases pass. The analytic modulo-\(r\) link descriptions and cellular-boundary cancellation prove the result for all odd \(r\).

At genus one, \(r=3\): there are nine nerve triangles, three private-edge collapses, and a six-triangle, nine-edge, three-vertex torus. At genus two, \(r=5\): there are twenty-five nerve triangles, fifteen free-face collapses, and a ten-triangle, fifteen-edge, three-vertex genus-two surface.

Run `python3 checker.py` in the directory containing the standalone checker. The checker requires only the Python standard library.

## Relationship to prior work

Carcacía-Campos [1] defines object complexity and proves the lower bound from the dimension of a finite acyclic category, as well as exact values for spheres, bouquets, Moore spaces, projective spaces, and lens spaces. His discussion of three-object composition tables (Section 2.3) gives the setting for this construction. The complete text of [1], including its Section 8 discussion of crystallizations, does not supply a three-object surface category or the all-genus equality above. In particular, the product inequality in [1] yields only the upper bound \(\nu(S^1\times S^1)\le4\), while this construction attains the homological lower bound three. This work does not reassert the known sphere calculation as new.

Tanaka [2] establishes compatibility of strong homotopy of acyclic categories and \(\Delta\)-complexes but does not, in the inspected text, give this all-genus construction. Classical crystallization produces certain three-vertex surface pseudotriangulations; not every such pseudotriangulation satisfies the nerve composition constraint. The explicit composition table and verified collapses here provide the needed additional structure. The classification of closed surfaces is used only after the manifold, orientability, and Euler-characteristic checks.

## Limitations

Only closed *orientable* connected surfaces of positive finite genus are addressed. The result minimizes the number of categorical objects, not the number of morphisms or simplices. The original nerve need not itself be a manifold; it collapses onto a manifold. It does not classify nonorientable surfaces or acyclic models up to isomorphism, and it does not give minimal finite-poset models. Although the primary paper and closely relevant indexed literature have been inspected, older or unindexed equivalent results may exist; there has been no independent expert review.

## References

[1] Isaac Carcacía-Campos, *How many points does it take to see the homotopy of a space? Minimal acyclic categorical models*, arXiv:2611.09718v1, first public 2026-11-06. https://arxiv.org/abs/2611.09718

[2] Kohei Tanaka, *Strong homotopy types of acyclic categories and Δ-complexes*, arXiv:1707.01179v1 (2017); *Applied Categorical Structures* **27** (2019), 245–260. https://arxiv.org/abs/1707.01179

[3] Allen Hatcher, *Algebraic Topology* (2002), Sections 1.2 and 2.2, for the classification of compact surfaces and cellular homology. https://pi.math.cornell.edu/~hatcher/AT/ATpage.html
