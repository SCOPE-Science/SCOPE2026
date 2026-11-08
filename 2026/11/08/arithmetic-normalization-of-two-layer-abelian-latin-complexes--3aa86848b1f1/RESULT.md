# Arithmetic normalization of two-layer abelian Latin complexes

## Finding
Let \(A\) be a finite abelian group of order \(N\), let \(t\in A\setminus\{0\}\), and put \(H=\langle t\rangle\), \(m=|H|\) and \(d=[A:H]\). Assume **\(d\ge2\)**, so the two sum levels are separated by a non-generating element. Define the two-dimensional simplicial complex \(X(A,t)\) on three labelled copies of \(A\): its triangles are exactly
\[
\{(0,a),(1,b),(2,c)\}\quad\text{for }a+b+c\in\{0,t\}.
\]
Every colorful pair is an edge (each extends to exactly two allowed triangles); no face contains two vertices of one color. Write \(\Sigma_g\) for the closed, connected, orientable surface of genus \(g\). Set
\[
 g=\frac{(m-1)(m-2)}2,\qquad
 b=3N(d-1)-d^2+1.
\]
**Theorem (integral homotopy classification).** For all such \(A,t\),
\[
 |X(A,t)|\simeq\left(\bigvee^{d^2}\Sigma_g\right)\vee\left(\bigvee^{b}S^1\right).
\]
More strongly, splitting the complex at its singular vertices gives **exactly \(d^2\) closed orientable surface sheets**, each of genus \(g\). Thus
\[
 H_1(X(A,t);\mathbb Z)\cong\mathbb Z^{N^2+d^2-3N+1},\qquad
 H_2(X(A,t);\mathbb Z)\cong\mathbb Z^{d^2},
\]
with reduced homology zero in all other degrees. Its fundamental group is the free product of \(d^2\) genus-\(g\) surface groups and a free group of rank \(b\). All integral homology is torsion-free.

For example, on \(A=\mathbb Z/6\mathbb Z\), the shifts \(t=2\) and \(t=3\) yield, respectively, \(4\) tori wedged with \(15\) circles and \(9\) two-spheres wedged with \(28\) circles. Both have exactly \(18\) vertices, \(108\) edges and \(72\) triangles. The unit-shift case \(t=1\), already within classical connected Latin-square biembeddings, instead triangulates a genus-\(10\) surface.

## Assumptions and scope
All group operations are additive. There are exactly three colors, every colorful pair is included, and all \(2N^2\) triangles are present as specified. Because \(t\ne0\), its order \(m\ge2\), and the two values \(0,t\) are distinct. The theorem concerns **proper-subgroup shifts** \(d>1\), not the previously studied cyclic generator case. The relevant group may be any finite abelian group, not necessarily cyclic. For \(m=2\) the surfaces \(\Sigma_0\) are two-spheres; for \(m\ge3\) they have positive genus. The homotopy decomposition is nonequivariant and makes no assertion about a canonical choice of wedge points.

The natural map of simplicial complexes \(X(A,t)\to\Delta^2\) sending a vertex to its color is nondegenerate and surjective. Its fiber-assignment sheaf is not flabby: a compatible assignment on the boundary of \(\Delta^2\) permits every triple of group values, but only triples of sum \(0\) or \(t\) extend over the full triangle. This is a natural nonflabby generalized inflation.

## Proof
**1. Arithmetic partition into sheets.** Let \(Q=A/H\), of order \(d\). For each ordered pair \((\alpha,\beta)\in Q^2\), define a subcomplex \(S_{\alpha,\beta}\) consisting of triangles whose three vertex cosets are \(\alpha\) in color \(0\), \(\beta\) in color \(1\), and \(-\alpha-\beta\) in color \(2\), and all their faces. Every allowed triangle lies in exactly one of these \(d^2\) subcomplexes: its sum is in \(H\), so its third coset is forced. Moreover **each edge belongs to exactly one sheet**, since any two vertex cosets uniquely determine the required third coset. Different sheets can therefore intersect only in vertices.

For a fixed sheet choose representatives \(a_0\in\alpha\), \(b_0\in\beta\), and \(c_0=-a_0-b_0\) in the third coset. Translating its three color classes by these representatives identifies it with \(X(H,t)\). As \(t\) generates \(H\), every sheet is isomorphic to the cyclic two-level complex on \(\mathbb Z/m\mathbb Z\) with sum values \(0,1\).

**2. The sheets are orientable surfaces.** In \(X(H,t)\), each colorful pair extends uniquely to a sum-zero triangle and uniquely to a sum-\(t\) triangle. Hence every edge lies in exactly two triangles. Fixing a vertex, its link is a bipartite graph on the other two colors. Its edges are the two perfect matchings \(b+c=-a\) and \(b+c=t-a\). Alternating between these matchings translates one coordinate by \(t\), which runs through all \(m\) elements of \(H\). Consequently the link is one cycle on \(2m\) vertices. This holds also when \(m=2\). Every sheet is thus a connected closed triangulated surface, with complete tripartite one-skeleton.

Give each sum-zero triangle the cyclic color orientation \((0,1,2)\), and each sum-\(t\) triangle the opposite orientation. Because triangles sharing any edge have opposite sum labels, their induced edge orientations cancel. Hence the surface is orientable. Its face vector is
\[
 (f_0,f_1,f_2)=(3m,3m^2,2m^2),
\]
so \(\chi=3m-m^2\). The classification of connected closed orientable surfaces gives \(\chi=2-2g\), i.e. \(g=(m-1)(m-2)/2\). This proves the asserted exact normalization sheets. (The connected generator-shift case itself belongs to established Latin-square embedding theory.)

**3. Incidence graph and homotopy type.** Replace each shared original vertex by a point node and connect it to each copy of that vertex in its sheet by a short segment. Contracting the resulting stars recovers \(X(A,t)\), and this replacement is a homotopy-equivalent graph of spaces with surface vertex spaces and point vertex spaces. Its underlying bipartite incidence graph \(B\) has \(d^2\) surface nodes and \(3N\) original-vertex nodes. Each sheet contains precisely \(3m\) vertices, so there are \(3m d^2=3Nd\) incidence edges. The graph is connected: sheet nodes \((\alpha,\beta)\) and \((\alpha,\beta')\) share color-\(0\) vertices, while \((\alpha,\beta')\) and \((\alpha',\beta')\) share color-\(1\) vertices. Every original vertex lies in some sheet. Therefore
\[
 \operatorname{rank}H_1(B;\mathbb Z)=|E(B)|-|V(B)|+1=3N(d-1)-d^2+1=b.
\]
For a connected graph of spaces with point edge spaces, move all attachments in each path-connected surface vertex space to a chosen basepoint (a homotopy of the attaching maps), then collapse a maximal tree of \(B\). The resulting space is exactly a wedge of its surface vertex spaces and one circle for every edge outside the tree. This proves the homotopy equivalence and, via van Kampen, the asserted free-product description of \(\pi_1\).

**4. Integral homology and boundary checks.** A closed orientable genus-\(g\) surface contributes one integral degree-\(2\) generator and \(2g\) free degree-\(1\) generators. Together with the \(b\) graph loops this gives \(H_2=\mathbb Z^{d^2}\), \(H_1=\mathbb Z^{2gd^2+b}\). Substitute \(N=md\) and \(2g=(m-1)(m-2)\) to simplify
\[
 2gd^2+b=N^2+d^2-3N+1.
\]
There are no cells above dimension two. The case \(d=1\), mentioned only for comparison, has a single connected orientable surface; the theorem's novel proper-subgroup range is \(d\ge2\).

## Verification
The standalone `verify.py` constructs arbitrary finite abelian groups by their cyclic-factor decomposition, enumerates every allowed triangle and edge, verifies that each edge has two cofaces, checks that every vertex link splits into exactly \(d\) cycles each of length \(2m\), reconstructs the \(d^2\) sheets and their face vectors, checks the incidence graph's connectedness and edge count, and independently computes complete reduced simplicial Betti numbers over \(\mathbb F_2\) by binary boundary-matrix elimination. It checks both proper-subgroup and unit-shift examples in cyclic and noncyclic groups. Run `python3 verify.py` from the package directory; success ends with `ALL_TWO_LEVEL_CHECKS_OK`. These finite checks corroborate the all-parameter structural proof; mod-two ranks alone do not establish its integral conclusion.

## Relationship to prior work
Ayzenberg and Khoroshavkina [1] prove sphere-wedge decompositions for **flabby** generalized inflation sheaves. Our three-color two-level assignment sheaf is explicitly nonflabby, so their conclusion cannot imply this classification. A previously published Latin-hypercube calculation [2] covers only one allowed full-sum value and yields a wedge of circles in the three-color case. A separate published two-adjacent-affine-layers calculation [3] gives integral homology for \(\mathbb Z/q\mathbb Z\) with difference **one**, and explicitly leaves nonunit differences outside its scope. Here a proper subgroup generated by the difference creates multiple positive-genus normalization sheets and extra incidence loops, and the conclusion is the **integral homotopy type** for every finite abelian group.

Classical Latin-square biembedding results [4] construct connected orientable triangular embeddings of \(K_{n,n,n}\), including the two cyclic sum levels of difference one, with genus \((n-1)(n-2)/2\). This is the already known connected-sheet ingredient in Step 2, not a new genus claim. The new statement classifies the singular complexes arising when the shift does **not** generate the ambient group. The identified older sources concern surface embeddings, not their multi-sheet vertex-gluing homotopy types. Equivalent treatments in Latin-bitrade normalization or nonflabby-sheaf literature may remain unindexed.

## Limitations
The theorem assumes exactly two distinct allowed sum levels, three colors, finite abelian addition, and a proper cyclic subgroup generated by their difference. It does not classify three or more allowed levels, nonabelian multiplication, nonuniform multiplicities, or equivariant actions on the homotopy decomposition. The wedge decomposition is not canonical. The originality comparison is limited by indexing and access to the full historical literature on Latin trades; no independent audit is asserted.

## References
[1] A. Ayzenberg and N. Khoroshavkina, *Homotopy types of finite étale spaces and generalized inflations*, arXiv:2602.08694v1, first public 2026-02-09, https://arxiv.org/html/2602.08694 . See Theorems 5.1–5.3 and Sections 4–7.

[2] *Latin-array inflations exhibit lower homotopy despite unique local lifting*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-latin-array-inflations-exhibit-lower-homotopy-despite-unique-loc--12e4d5a0c16a . See the full statement and proof in `RESULT.md`.

[3] *Two adjacent affine layers force integral homology in two neighboring degrees*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-two-adjacent-affine-layers-force-integral-homology-in-two-neighb--b693290149ba . See the exact \(\mathbb Z/q\mathbb Z\), difference-one scope and the stated nonunit limitation in `RESULT.md`.

[4] M. J. Grannell, T. S. Griggs, M. Knor, and J. Širáň, *Triangulations of orientable surfaces by complete tripartite graphs*, Discrete Mathematics 306 (2006), 600–606, lawful preprint https://grannell.net/Papers/triknnn.pdf . Sections 1–2 contain the regular cyclic biembedding construction and genus formula.

[5] M. J. Grannell and M. Knor, *Biembeddings of Abelian groups*, Journal of Combinatorial Designs 18 (2010), 71–83, https://doi.org/10.1002/jcd.20235 . Related connected biembedding background; its abstract and available introductory material were checked.
