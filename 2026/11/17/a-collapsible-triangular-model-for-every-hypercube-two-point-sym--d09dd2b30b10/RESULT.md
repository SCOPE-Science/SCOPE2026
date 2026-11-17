# A collapsible triangular model for every hypercube two-point symmetry quotient

## Finding
For every integer \(d\ge 2\), let \(Q_d\) be the graph with vertex set \(\{0,1\}^d\), two vertices adjacent when their Hamming distance is one. Let \(G_d=(C_2)^d\rtimes S_d\) act by independent bit flips and coordinate permutations. Write
\[
X_d=\operatorname{UConf}_2(|Q_d|)
=\{\{x,y\}: x,y\in |Q_d|,\ x\ne y\}.
\]
Then **the ordinary orbit space \(X_d/G_d\) is contractible for every \(d\ge2\)**. More precisely, it strongly deformation retracts onto a compact quotient \(D_d/G_d\) that is PL-homeomorphic to the following explicit two-dimensional simplicial complex \(T_d\).

The vertices of \(T_d\) are \(a_1,\ldots,a_d,c_1,\ldots,c_{d-1}\). Its facets are
\[
\{a_r,c_r,a_{r+1}\}\quad(1\le r\le d-1),\qquad
\{a_r,a_{r+1},a_{r+2}\}\quad(1\le r\le d-2).
\]
Thus \(T_d\) has \((2d-1,4d-5,2d-3)\) vertices, edges, and triangles; it simplicially collapses onto the path \(a_1-a_2-\cdots-a_d\), then to a point. For \(d=2,3\), \(T_d\) is a closed disk. For \(d\ge4\), each of the \(d-3\) path edges \(a_r a_{r+1}\), \(2\le r\le d-2\), belongs to three triangles, displaying a sharp branching/nonmanifold transition even while contractibility persists.

## Assumptions and scope
An edge of \(Q_d\) is the geometric unit interval between adjacent binary vertices. Particles are unordered, distinct, and may lie in edge interiors. The symmetry group \(G_d\) is the **full graph automorphism group**, not just coordinate permutations or determinant-positive symmetries. The quotient is the ordinary orbit space, not the Borel/homotopy quotient. The notation \(D_d\) denotes the compact unordered cubical deleted product: a cell corresponds to an unordered pair of vertices or closed edges of \(Q_d\) whose closed supports are disjoint. A square cell means two particles move independently in disjoint closed edges. The homeomorphism asserted above is \(D_d/G_d\cong |T_d|\); the generally noncompact \(X_d/G_d\) is asserted to be homotopy equivalent to \(T_d\), not homeomorphic to it.

## Proof
**1. Equivariant strong deformation retraction from continuous to cubical configurations.** Represent a point of the geometric graph by its nonnegative barycentric vector \(\alpha=(\alpha_v)_{v\in V(Q_d)}\) of total mass one, supported on one edge or one vertex. For distinct points \(\alpha\ne\beta\) put
\[
\delta=\alpha-\beta,\qquad
s=\sum_v(\delta_v)_+=\sum_v(-\delta_v)_+>0,
\qquad
\alpha'_v=\frac{(\delta_v)_+}{s},\quad
\beta'_v=\frac{(-\delta_v)_+}{s}.
\]
Here \((t)_+=\max(t,0)\). The supports of \(\alpha'\) and \(\beta'\) are disjoint subsets of the original supports, so each remains on its original closed edge (or vertex), and the endpoint configuration lies in \(D_d\). The straight-line homotopy
\[
H_u(\alpha,\beta)=((1-u)\alpha+u\alpha',\ (1-u)\beta+u\beta'),\qquad0\le u\le1,
\]
has nonzero coordinate difference \((1-u+u/s)(\alpha-\beta)\) at every time and therefore never collides. It fixes \(D_d\) pointwise because disjoint supports give \(s=1\). The formula commutes with vertex permutations and with swapping the two particles, hence descends to a strong deformation retraction \(X_d/G_d\searrow D_d/G_d\). This verifies the symmetry requirement directly rather than assuming that a nonequivariant retraction descends.

**2. Orbits of zero- and one-cells.** The stated signed-coordinate group is the full automorphism group of the cube graph: the image of the zero word has at most \(2^d\) choices and its \(d\) neighbors can be permuted in at most \(d!\) ways, which determine every further image by preservation of graph distances and squares; all those choices are realized by bit flips and coordinate permutations. Translate one of two distinct vertices to the zero word; coordinate permutations classify the other by its Hamming weight \(r\in\{1,\ldots,d\}\). Denote the resulting zero-cell orbit by \(a_r\). A one-cell is an unordered edge-vertex pair with disjoint supports. After translating and permuting coordinates, its edge is \([0,e_i]\) and the other vertex is a binary word with exactly \(r\) ones outside coordinate \(i\), where \(1\le r\le d-1\). Flipping coordinate \(i\) interchanges the possible values of that word's \(i\)-th bit, so this is one orbit \(b_r\). Its endpoints have Hamming distances \(r\) and \(r+1\), so \(b_r\) joins \(a_r\) to \(a_{r+1}\) without folding. The one-skeleton quotient is therefore exactly the path
\[
a_1\mathbin{-}a_2\mathbin{-}\cdots\mathbin{-}a_d.
\]

**3. Exhaustive classification of square-cell orbits and their stabilizers.** A square of \(D_d\) corresponds to two disjoint edges. Two edges have either the same coordinate direction or different directions, a dichotomy preserved by every member of \(G_d\).

For parallel edges, normalize the pair to \([0,e_i]\) and \([y,y+e_i]\), with \(y_i=0\) and exactly \(r\) ones in the other coordinates, \(1\le r\le d-1\). Such pairs form one orbit \(p_r\) for each \(r\). The induced action of its stabilizer on the square parameters \((s,t)\in[0,1]^2\) is generated by
\[
(s,t)\longmapsto(t,s),\qquad (s,t)\longmapsto(1-s,1-t).
\]
The first comes from translation by \(y\), the second from flipping coordinate \(i\). No further parameter transformations are possible: an automorphism stabilizing the unordered pair of parallel edges must preserve their direction, and it can only preserve or exchange the two edges while possibly reversing their common coordinate simultaneously. The quotient square is the triangular region bounded by one original square edge and the two diagonals through its center. Its vertices are \(a_r,a_{r+1},c_r\), where \(c_r\) is the square-center orbit, and its original boundary maps homeomorphically onto \(b_r=a_ra_{r+1}\).

For perpendicular edges, normalize to \([0,e_i]\) and \([y,y+e_j]\) with \(i\ne j\), \(y_i=y_j=0\), and exactly \(r\) ones outside \(i,j\). Choosing which endpoint of each edge is called its base, followed by a bit flip in coordinate \(i\), gives this normalization. Disjointness is equivalent to \(1\le r\le d-2\). These pairs form one orbit \(q_r\) for each \(r\). The stabilizer's only nonidentity square-parameter action exchanges the two moving particles, \((s,t)\mapsto(t,s)\); it is realized by swapping coordinates \(i,j\) and translating by \(y\). Indeed, an automorphism fixing both different-direction edges separately cannot reverse either direction while preserving both edge sets; any symmetry exchanging them gives the displayed reflection up to elements acting trivially on the square. The square quotient is a triangle with vertices \(a_r,a_{r+1},a_{r+2}\). Its two original-boundary sides are exactly \(b_r\) and \(b_{r+1}\), and its remaining side is the new diagonal \(a_ra_{r+2}\).

Every square belongs to exactly one of the listed types. The interiors of distinct orbit squares cannot identify with one another or with lower-dimensional cells; incidence along their original boundaries is completely determined by the path \(b_r\). Therefore gluing the triangular square-orbit quotients along that path produces precisely \(|T_d|\), with one triangle \(\{a_r,c_r,a_{r+1}\}\) for each \(p_r\) and one triangle \(\{a_r,a_{r+1},a_{r+2}\}\) for each \(q_r\). This proves the claimed PL-homeomorphism \(D_d/G_d\cong |T_d|\) for every \(d\ge2\).

**4. Explicit collapses.** Each diagonal edge \(a_ra_{r+2}\) is a free face of exactly its \(q_r\)-triangle; remove those \(d-2\) triangle-edge pairs. Next each edge \(a_rc_r\) is free in its \(p_r\)-triangle; remove those \(d-1\) pairs. The remaining edges \(c_ra_{r+1}\) have leaf vertices \(c_r\); collapse those \(d-1\) edge-vertex pairs. The path \(a_1-\cdots-a_d\) remains and collapses by removing its terminal edges. This proves contractibility. For \(d=2,3\) the facets tile a disk (one triangle, respectively three triangles with boundary a five-cycle), while for \(d\ge4\) the middle edges \(a_ra_{r+1}\) have three incident triangles and hence nonmanifold interior points.

## Verification
A standalone Python-standard-library program `verify.py` independently enumerates all unordered cubical cells, face chains, and hypercube automorphisms for dimensions \(2\le d\le5\), computes their orbit flags, checks the predicted quotient flag counts \((4d-4,10d-15,6d-10)\), verifies complete elementary collapses of these finite orbit-flag triangulations, and checks the sizes of the effective square-stabilizer actions \(4\) for parallel pairs and \(2\) for perpendicular pairs. Running `python3 verify.py` reproduces `verification_output.txt`. The general theorem is proved by the all-dimensional normal forms and stabilizer argument above, not extrapolated from those finite checks.

## Relationship to prior work
Abrams and Ghrist (first public 2000-09-12) introduce graph discretized configuration spaces and explain deformation retract criteria. Farley and Sabalka (2004) give discrete-Morse methods for graph braids; Barnett and Farber (2009) study two-particle graph configuration cohomology and deleted products. None of these inspected treatments determines the ordinary full-symmetry orbit spaces of the binary cube graphs in all dimensions. A previously published exact result establishes the special case \(d=3\), including an equivariant retraction and a finite collapse; that result is credited as a special case and does not imply the claimed explicit all-dimensional triangle classification or its sharp nonmanifold threshold at \(d=4\). This result is about quotients by graph automorphisms, not about the ordinary nonequivariant configuration-space homology or Borel-equivariant topology.

## Limitations
This theorem concerns exactly two **unordered** particles and the **full** binary-cube graph automorphism group. It does not classify particle numbers greater than two, proper symmetry subgroups, or quotient fundamental-group orbifold structures. The continuous space is only asserted homotopy equivalent to the compact triangulation. Finite verification through \(d=5\) is supportive but does not prove the general normal forms. A statement-equivalent result in literature not identified by the searches remains a novelty risk; no independent mathematical audit has been performed.

## References
1. A. Abrams and R. Ghrist, *Finding topology in a factory: configuration spaces*, arXiv:math/0009118, first public 2000-09-12, https://arxiv.org/html/math/0009118v1.
2. D. Farley and L. Sabalka, *Discrete Morse theory and graph braid groups*, arXiv:math/0410539, first public 2004-10-25, https://arxiv.org/abs/math/0410539.
3. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180, first public 2009-03-12, https://arxiv.org/html/0903.2180v1.
4. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511, first public 2009-09-30, https://arxiv.org/abs/0909.5511.
5. *The cube's two-particle configuration space has a collapsible full-symmetry quotient*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-the-cube-s-two-particle-configuration-space-has-a-collapsible-fu--a2c7941d36bd.
