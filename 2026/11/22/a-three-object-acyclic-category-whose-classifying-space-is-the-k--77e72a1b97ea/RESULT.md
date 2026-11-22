# A three-object acyclic category whose classifying space is the Klein bottle

## Finding
Let \(K\) be the closed Klein bottle. In the object-complexity notation of Carcacía-Campos,
\[\nu(K)=3.\]
An explicit model has three objects, twelve nonidentity arrows and nine 2-simplices. Its nerve collapses onto a six-triangle \(\Delta\)-complex homeomorphic to \(K\). This is a homotopy equivalence of the original nerve, not a claim that its original nine-triangle realization is a manifold.

## Assumptions and scope
Work in the category of finite acyclic small categories and their ordinary nerve realizations. The objects of \(\mathcal C\) are \(0,1,2\). There are precisely three distinct arrows \(a_i:0\to1\), three \(b_j:1\to2\), and six \(c_k:0\to2\); indices are \(i,j\in\{0,1,2\}\) and \(k\in\{0,1,2,3,4,5\}\). In addition, there are identity arrows, and no other arrows. Define
\[
b_j\circ a_i=c_{T(i,j)},\qquad
T=\begin{pmatrix}3&0&1\\0&4&2\\2&1&5\end{pmatrix}.
\]
There are no strings of three nonidentity arrows, so these definitions are automatically associative. There are precisely nine nondegenerate triangles \(t_{ij}=(a_i,b_j)\), with oriented cellular boundary \(\partial t_{ij}=b_j-c_{T(i,j)}+a_i\).

## Proof
**Three collapses.** The arrows \(c_3,c_4,c_5\) each occur as the long edge of exactly one triangle: \(t_{00},t_{11},t_{22}\), respectively. Each is a free 1-face, so collapse these three triangle-edge pairs in any order. Let \(Y\) be the resulting connected 2-dimensional \(\Delta\)-complex. Its six triangles are \(t_{ij}\) with \(i\ne j\), it has exactly three vertices and nine edges (three each of types \(a,b,c\), with only \(c_0,c_1,c_2\) retained), and hence
\[\chi(Y)=3-9+6=0.\]

**Surface links.** Each retained arrow occurs in exactly two triangles: each \(a_i\) belongs to the two entries of its row away from the diagonal, each \(b_j\) to the two off-diagonal entries of its column, and each \(c_k\), for \(0\le k\le2\), occurs twice in the table away from the diagonal. The link at object \(1\) is the bipartite graph on the three \(a\)-arrows and three \(b\)-arrows with edges \((a_i,b_j)\) for \(i\ne j\), a 6-cycle. The link at object \(0\) has edges \((a_i,c_{T(i,j)})\), and that at object \(2\) has edges \((b_j,c_{T(i,j)})\), all with \(i\ne j\). Each of these graphs is connected, has six vertices and degree two at every vertex, so each is a 6-cycle. It follows that \(Y\) is a closed connected surface (a genuine manifold despite its non-simplicial \(\Delta\)-structure).

**Nonorientability.** If \(Y\) were orientable, assigning coefficients \(\pm1\) to the six triangles in a fundamental 2-cycle would make the coefficients opposite on every two triangles sharing any edge; this follows from the uniform vertex ordering \(0<1<2\) and the displayed boundary convention. Around the six off-diagonal row/column adjacencies, the triangle signs must alternate. In particular, using the cycle
\[t_{01},\ t_{02},\ t_{12},\ t_{10},\ t_{20},\ t_{21},\ t_{01},\]
the signs of \(t_{02}\) and \(t_{21}\) must agree. But these two triangles both use the retained long edge \(c_1\), so their signs must be opposite. Contradiction. Thus \(Y\) is nonorientable. A connected closed nonorientable surface of Euler characteristic zero is the Klein bottle, proving \(B\mathcal C\simeq K\).

**Sharp object count.** A finite acyclic category with at most two objects has no composable pair of nonidentity arrows. Its nerve realization is therefore at most one-dimensional and has torsion-free integral first homology. Since
\[H_1(K;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/2\mathbb Z,\]
no such category models \(K\), whereas the explicit category above has three objects. Therefore \(\nu(K)=3\).

An independent fundamental-group consistency check follows by collapsing the tree edges \(a_0,b_0\). Write the remaining \(a_1,a_2,b_1,b_2\) as generators. The off-diagonal table relations imply \(b_1=a_1\), \(a_2=a_1b_2\), and \(b_2=a_2b_1\), hence \(b_2=a_1b_2a_1\), the standard Klein bottle presentation \(\langle x,y\mid y^{-1}xy=x^{-1}\rangle\).

## Verification
The embedded `checker.py` exhaustively constructs the nine table entries, verifies the three unique free-face collapses, checks the incidence multiplicities and connected 6-cycle links, computes Euler characteristic zero, and checks the absence of a global orientation assignment. It also tests the algebraic relations identifying the Klein bottle group. Separately, an exact Smith normal form of the full cellular degree-two boundary matrix has nine nonzero invariant factors, eight equal to one and one equal to two; consequently \(H_2=0\) and \(H_1\cong\mathbb Z\oplus\mathbb Z/2\mathbb Z\). The surface-link and orientability proof, rather than homology alone, supplies the homeomorphism classification.

## Relationship to prior work
Carcacía-Campos (2026) defines the object-complexity invariant, studies arbitrary three-object acyclic categories via a sink-cone description, and gives exact values for spheres, bouquets, Moore spaces, real projective spaces and lens spaces. Its explicit three-object classification with two first-stage arrows yields Moore-space/sphere-wedge types, rather than this example with three arrows at both stages. The paper does not state the Klein-bottle case; this is a concrete new evaluated surface type, not a new definition of the invariant. Classical triangulations and finite-poset models of the Klein bottle do not directly imply that a three-object category with associative composition has the required nerve. Related finite-poset models involve a different, more restrictive notion of categorical model.

## Limitations
Only the Klein bottle and the number of objects are classified. The result does not minimize the number of morphisms, classify all three-object models, or establish a formula for other nonorientable genera. The three free-face collapses give a homotopy equivalence, not a claim that the original nine-triangle nerve is homeomorphic to the Klein bottle. Published-priority searches cannot exclude unindexed equivalent categorical tables, and the mathematical review is not independent.

## References
1. Isaac Carcacía-Campos, *How many points does it take to see the homotopy of a space? Minimal acyclic categorical models*, arXiv:2611.09718v1 (first public November 6, 2026), https://arxiv.org/html/2611.09718v1.
2. Kohei Tanaka, *Strong homotopy types of acyclic categories and \(\Delta\)-complexes*, Applied Categorical Structures 27 (2019), 245–260, https://arxiv.org/abs/1707.01179.
3. Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002, Chapter 1 (surface groups, homology, and CW arguments).
