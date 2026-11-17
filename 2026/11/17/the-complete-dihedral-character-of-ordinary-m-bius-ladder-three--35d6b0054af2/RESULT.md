# The complete dihedral character of ordinary Möbius-ladder three-cut homology

## Finding
For every integer \(n\ge5\), let \(M_{2n}\) be the Möbius ladder with vertices \(\mathbb Z/(2n)\), cycle edges \(\{i,i+1\}\), and antipodal edges \(\{i,i+n\}\). Let \(X_n=\Delta_3(M_{2n})\) be the **ordinary** three-cut complex: its facets are the complements of the triples inducing disconnected subgraphs. The natural dihedral group \(D_{2n}=\langle r,s\mid r^{2n}=s^2=1,\ srs=r^{-1}\rangle\), acting by \(r(i)=i+1\) and \(s(i)=-i\), acts on the unique nonzero reduced rational homology
\[
H_n=\widetilde H_{2n-4}(X_n;\mathbb Q),\qquad \dim H_n=B_n=2n^2-8n+1.
\]
The dimension and nonequivariant sphere-wedge homotopy type are known from prior work [2]. **The new assertion is the complete dihedral character** \(\chi_n(g)=\operatorname{tr}(g\mid H_n)\): for \(0\le a<2n\),
\[
\boxed{\chi_n(r^a)=\begin{cases}B_n,&a=0,\\(-1)^a,&1\le a<2n,\end{cases}}
\]
and
\[
\boxed{\chi_n(r^as)=\begin{cases}
4-n,&n\text{ odd},\ a\text{ even},\\
n-2,&n\text{ odd},\ a\text{ odd},\\
n-3,&n\text{ even},\ a\text{ even},\\
3-n,&n\text{ even},\ a\text{ odd}.
\end{cases}}
\]
These values determine the isomorphism class of \(H_n\) as a rational \(D_{2n}\)-representation. Averaging yields the exact invariant dimension
\[
\boxed{\dim_{\mathbb Q}H_n^{D_{2n}}=\left\lfloor\frac{n-3}{2}\right\rfloor.}
\]
Equivalently, the top rational Betti number of the quotient \(X_n/D_{2n}\) equals this integer; for quotient homology take a barycentric subdivision before applying the usual finite-group rational-transfer argument.

## Assumptions and scope
Indices are always modulo \(2n\). The graph is finite, simple, and cubic for \(n\ge5\); it is triangle-free and has exactly \(n\) four-cycles, the squares \(S_i=\{i,i+1,i+n,i+n+1\}\), indexed by \(i\) modulo \(n\). The theorem concerns the specified dihedral subgroup of graph automorphisms, not an assertion about a potentially larger full automorphism group. The complex is the **ordinary** cut complex, not the total cut complex defined through independent triples. Homology and characters are rational; the already known integral homotopy type is used only to identify the single homological degree.

## Proof
**1. The Alexander dual and its homological concentration.** Put \(N=2n\) and \(K_n=X_n^{\vee}\). A subset belongs to \(K_n\) exactly when all its triples induce connected graphs in \(M_{2n}\). All \(N\) vertices and all \(\binom N2\) edges belong to \(K_n\). As the graph is triangle-free, its connected triples are precisely paths of length two; each of the \(N\) cubic vertices is the unique center of three such paths. Thus \(K_n\) has exactly \(3N=6n\) triangles. A four-vertex set has all triples connected if and only if it induces a four-cycle. The only such squares are the \(n\) listed above, yielding exactly \(n\) tetrahedra. No set of five or more vertices is a face: in a triangle-free five-vertex graph, ten connected triples would require at least seven edges, contradicting Mantel's six-edge bound.

For completeness, a uniform collapse explains the homology rather than relying on a numerical computation. Of the \(6n\) triangles, \(2n\) are the consecutive path triples \(\{i-1,i,i+1\}\); each has a unique nonedge \(\{i-1,i+1\}\) appearing in no other triangle or tetrahedron. Collapse these pairs. The remaining \(4n\) triangles are grouped four per square. Each square tetrahedron can be collapsed along one triangular face, then the triangle sharing the same diagonal can be collapsed along that now-free diagonal. The two surviving triangles triangulate the square along its other diagonal. No diagonal occurs in a different square. Each resulting square has two boundary cycle edges, and each such edge belongs to that square only (different squares may share antipodal edges, not cycle edges). Collapse one of its remaining triangles along a boundary cycle edge, then the last triangle along its newly free diagonal. The procedure uses exactly \(6n\) elementary pairs and leaves a connected graph on \(N\) vertices with \(\binom N2-5n=2n(n-3)\) edges. Therefore
\[
K_n\simeq\bigvee^{B_n}S^1,\qquad B_n=\binom N2-5n-N+1=2n^2-8n+1.
\]
By combinatorial Alexander duality, \(X_n\) has reduced integral homology only in degree \(N-4\), where it is free of rank \(B_n\). Furthermore every five vertices contain a disconnected triple, so \(X_n\) has the full \((N-6)\)-skeleton of the simplex. Its low-degree connectivity and the absence of other homology, followed by Hurewicz and Whitehead, give the sphere-wedge homotopy statement already recorded in [2]. For the new equivariant result we need only that the sole nonzero reduced rational group is \(H_n\).

**2. The signed equivariant Alexander-duality relation.** Let \(C_j(K_n;\mathbb Q)\) denote oriented simplicial chains. For any vertex permutation \(g\), the chain traces are signed counts of setwise fixed simplices. Since \(K_n\) is connected and has no reduced homology beyond degree one,
\[
\operatorname{tr}\bigl(g\mid H_1(K_n;\mathbb Q)\bigr)=1-\operatorname{tr}(g\mid C_0)+\operatorname{tr}(g\mid C_1)-\operatorname{tr}(g\mid C_2)+\operatorname{tr}(g\mid C_3).
\]
Naturality of combinatorial Alexander duality with chosen orientation of the ambient \((N-2)\)-sphere gives the sign twist
\[
\chi_n(g)=\operatorname{sgn}(g)\,\operatorname{tr}\bigl(g\mid H_1(K_n;\mathbb Q)\bigr).
\]
The sign is the sign of \(g\) on all \(N\) vertices, not the sign on an individual fixed simplex. It can also be obtained by the complementary-face chain pairing with the ambient ordered vertex set.

**3. Rotations.** The identity traces on \((C_0,C_1,C_2,C_3)\) are \((N,\binom N2,6n,n)\), giving \(B_n\) in degree one. A nonidentity rotation has no fixed vertices or path-triangle centers. Unless it is the antipodal half-turn \(r^n\), no edge or square tetrahedron is setwise fixed, so the degree-one trace is \(1\). The half-turn reverses each of the \(n\) antipodal edges and preserves each of the \(n\) squares with even induced permutation, yielding chain traces \((0,-n,0,n)\) and again degree-one trace \(1\). The full vertex permutation \(r^a\) has sign \((-1)^a\), which proves the stated rotation character.

**4. Reflections.** Write \(g=r^as\), so \(g(i)=a-i\). When \(a\) is even, \(g\) fixes exactly two graph vertices and swaps \(n-1\) vertex pairs. Its chain traces in dimensions zero, one, and two are \((2,2-n,-2)\): at either fixed center the reflection swaps its two cycle neighbors and fixes the antipodal neighbor, giving local oriented triangle trace \(-1\). When \(a\) is odd, the permutation has no fixed vertices and swaps \(n\) pairs, giving chain traces \((0,-n,0)\) in these dimensions.

The reflection permutes squares by \(S_i\mapsto S_{a-1-i}\). Its setwise fixed squares solve \(2i\equiv a-1\pmod n\); on each such square it induces an even permutation of the four vertices, so every fixed tetrahedron contributes \(+1\). The number of solutions is one for odd \(n\); for even \(n\), it is zero if \(a\) is even and two if \(a\) is odd. Substitution gives degree-one traces \(4-n\) and \(2-n\) when \(n\) is odd (even/odd \(a\), respectively), and \(3-n\) for both classes when \(n\) is even. The full vertex-permutation signs are \((-1)^{n-1}\) for even \(a\) and \((-1)^n\) for odd \(a\). Multiplication by these signs gives precisely the four claimed reflection values.

**5. Dihedral invariants.** The rotation character sum is \(B_n-1=2n^2-8n\), since \(\sum_{a=0}^{2n-1}(-1)^a=0\). The sum of reflection traces is \(2n\) for odd \(n\), and zero for even \(n\). Dividing the sum by the group order \(4n\) yields \((n-3)/2\) for odd \(n\) and \((n-4)/2\) for even \(n\), equivalently \(\lfloor(n-3)/2\rfloor\). Characteristic-zero character theory guarantees that the complete character determines the rational representation up to isomorphism.

## Verification
The standalone Python 3 program `VERIFY.py` independently constructs each Alexander dual for \(5\le n\le20\), checks its face vector, and verifies by actual unique-coface deletion an elementary collapse of exactly \(6n\) pairs. It checks all \(4n\) dihedral elements per size by computing their signed chain traces and compares them against both closed formulas and the invariant dimension. For \(n=5,6,7\), it separately enumerates the **ordinary three-cut complex itself** from all disconnected triples and computes signed reduced Lefschetz traces of every dihedral element directly, thereby checking the sign twist without relying on the Alexander-dual calculation. The recorded output is `VERIFY_OK`: 16 sizes, 1,200 collapse pairs, 800 dual-chain character comparisons, and 72 independent direct-cut-complex comparisons. These bounded computations corroborate, but do not replace, the argument for all \(n\ge5\).

## Relationship to prior work
Bayer et al. [1] defined ordinary cut complexes and established homotopy and symmetry results for several graph families, including cycles and prisms over complete graphs. Their theorem and tables do not determine Möbius-ladder dihedral characters. The nonequivariant Möbius-ladder three-cut sphere-wedge classification [2] already establishes the rank \(B_n\), including the smaller case \(n=4\); **no novelty is claimed for that rank or homotopy type**. A related general theorem for triangle-free graphs with edge-disjoint squares [3] does not apply here, because neighboring Möbius-ladder squares share antipodal edges; it does not determine group actions. The complete character for ordinary *circular*-ladder cut homology [4] pertains to a nonisomorphic graph family, with different group action and, notably, no invariant classes at even ladder widths. A 2026 study [5] of Möbius-ladder independence and perfect-matching complexes does not supply ordinary three-cut character formulas. Unlike those results, the present calculation gives the full dihedral representation and exact quotient invariant rank for every \(n\ge5\).

## Limitations
The group is the natural \(D_{2n}\), not necessarily the full automorphism group. The theorem excludes \(n=4\), does not classify the integral \(\mathbb Z[D_{2n}]\)-lattice or quotient homotopy type, and does not assert a uniform equivariant homotopy equivalence. All-parameter correctness rests on the face classification, the elementary-collapse argument and signed Lefschetz calculations, not on the finite tests. Searches cannot rule out uncatalogued equivalent representation calculations. Full text of the later independence/perfect-matching preprint [5] was not accessible during the comparison; its publicly available title and abstract concern different complexes, but this remains a bounded source-access risk.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675, first public 2023-04-26, https://arxiv.org/abs/2304.13675.

[2] *Ordinary three-cut complexes of Möbius ladders are uniform sphere wedges*, earlier mathematical research record with the stated nonequivariant classification.

[3] *Three-cut complexes of triangle-free graphs with edge-disjoint squares*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-cut-complexes-of-triangle-free-graphs-with-edge-disjoint-s--8ca830284420.

[4] *Dihedral and layer-swap homology characters of cyclic-prism three-cut complexes*, earlier mathematical research record covering circular ladders.

[5] A. Agarwal, B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public 2026-08-31, https://arxiv.org/abs/2608.30601.
