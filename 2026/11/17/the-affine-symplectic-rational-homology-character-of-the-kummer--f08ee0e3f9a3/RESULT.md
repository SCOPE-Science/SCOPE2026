# The affine-symplectic rational homology character of the Kummer biplane complex

## Finding
Let \(V=\mathbb F_2^4=\mathbb F_2^2\oplus\mathbb F_2^2\). Write \(a=(a_0,a_1)\), let \(f(a)=a_0+a_1+a_0a_1\) in \(\mathbb F_2\), and define \(q(a,b)=f(a)+f(b)\). Set \(D=\{x\in V:q(x)=1\}\), with \(|D|=6\), and let \(K\) be the simplicial complex whose facets are the sixteen translates \(u+D\), \(u\in V\). This is the Kummer biplane block complex, also the open-neighborhood complex of the \(4\times4\) rook graph.

Put \(B(v,w)=q(v+w)+q(v)+q(w)\). The affine symplectic group \(G=V\rtimes\operatorname{Sp}(V,B)\), of order \(11520\), preserves \(K\). Its action on the already-known 55-dimensional rational second homology is determined completely by the following explicit character formula. For \(g\in G\), let \(f_g\) be the number of fixed vertices and \(t_g\) the number of two-cycles of its permutation of the sixteen vertices. For every block \(C=u+D\) fixed setwise by \(g\), let \(f_{g,C}\) be the number of its fixed vertices and \(t_{g,C}\) the number of its internal two-cycles. Then
\[
\boxed{\operatorname{tr}\!\left(g\mid H_2(K;\mathbb Q)\right)
=f_g-\binom{f_g}{2}+t_g-1
+\sum_{gC=C}\!\left(1-f_{g,C}+\binom{f_{g,C}}2-t_{g,C}\right).}
\]

Among all \(11520\) elements, the character values and their frequencies are, respectively,
\[
(-5,240),\quad(-1,4230),\quad(0,2304),\quad(1,4640),\quad(7,105),\quad(55,1).
\]
Every one of the fifteen nonidentity translations has trace \(7\), whereas the identity has trace \(55\). It follows that
\[
\boxed{\dim H_2(K;\mathbb Q)^V=10,\qquad
\dim H_2(K;\mathbb Q)^G=0.}
\]
Consequently, the geometric translation quotient has rational second Betti number \(10\), whereas the full affine-symplectic quotient is rationally acyclic in positive degrees. No assertion of contractibility of the latter quotient is made.

## Assumptions and scope
The complex contains all subsets of its sixteen six-point blocks, including the empty face. The arithmetic defining \(q\) and \(B\) is modulo two. The group acts by affine maps \(x\mapsto Ax+t\), where \(t\in V\) and \(A\in\operatorname{Sp}(V,B)\). A block is fixed only when its vertex set is invariant; a two-cycle inside a block means a two-element orbit of the full permutation contained in that block. The character is over \(\mathbb Q\), so integer two-torsion in first homology does not contribute.

The previously established nonequivariant homotopy classification is \(K\simeq\mathbb{RP}^2\vee\bigvee^{55}S^2\). Its homology is independently recomputed by the included integral checker, but that homotopy classification is not claimed as new. The result does not concern the distinct Rips complex of the bipartite incidence graph, nor the closed-neighborhood complex.

## Proof
**Geometry and symmetry.** The polar form \(B\) of \(q\) is a nondegenerate alternating bilinear form. The six elements of \(D\) are the three nonzero vectors in each coordinate two-plane. The sixteen translates are the six rook-neighbors of each point. Every unordered pair of vertices lies in precisely two blocks, while every triple belongs to at most one. The latter assertion follows from the fact that two distinct blocks meet in exactly two points. The family of blocks is determined by its facial triples: it comprises exactly the maximal sets all of whose triples are faces. Equivalently, a triple \(\{x,y,z\}\) is facial exactly when \(B(x+y,x+z)=1\). Thus every affine symplectic transformation preserves the family of facets and acts simplicially on \(K\). The group order is \(16\cdot|\operatorname{Sp}_4(2)|=16\cdot720=11520\).

**Independent homology premise.** The exact face vector by simplex dimension is \((16,120,320,240,96,16)\). The provided collapse program successively removes 256 genuine free-face/coface pairs, leaving a two-dimensional complex with 16 vertices, 120 edges and 160 triangles. Eliminating the 15 edges of a spanning tree in its connected one-skeleton leaves a signed integral triangle-boundary matrix of size \(105\times160\). Its Smith invariant factors are 104 copies of \(1\) and one copy of \(2\). Hence \(H_1(K;\mathbb Z)\cong\mathbb Z/2\), \(\widetilde H_2(K;\mathbb Z)\cong\mathbb Z^{55}\), and every other reduced integral homology group is zero. Thus rational homology occurs only in degree zero and degree two, as required for the Lefschetz calculation.

**Character formula.** For a simplicial automorphism \(g\), the chain trace in dimension \(j\) is the sum, over setwise-fixed \(j\)-simplices, of the sign of the vertex permutation induced on the simplex. The alternating traces on all nonempty faces equal the Lefschetz number. The contribution of the vertices is \(f_g\). Fixed edges are either pairs of individually fixed vertices, each contributing \(-1\), or two-cycles, each contributing \(+1\); their combined contribution is \(-\binom{f_g}{2}+t_g\).

Every face with at least three vertices is contained in a **unique** six-point block. A setwise-fixed such face necessarily lies in a setwise-fixed block. For each fixed block \(C\), the alternating signed chain trace of its entire nonempty simplex equals \(1\): a simplex is contractible. Subtracting its vertex and edge contributions leaves \(1-f_{g,C}+\binom{f_{g,C}}2-t_{g,C}\). Summing over fixed blocks counts every face of size at least three exactly once. Thus the alternating total chain trace is the displayed expression before the final subtraction of one. Since \(H_0(K;\mathbb Q)\) is a trivial line and other positive-degree rational homology vanishes outside degree two, the simplicial Lefschetz formula subtracts that line, proving the character identity.

**Full-group and subgroup consequences.** Enumerating basis images subject to the six independent symplectic pairings yields all 720 invertible symplectic linear transformations; adjoining sixteen translations yields all 11520 distinct affine symmetries. The accompanying code independently computes the formula and the direct oriented-face trace for every group element, then counts the six displayed character values. Their multiplicity-weighted sum is zero. For nonidentity translations, the fixed-point and block-cycle terms yield trace seven (also verified individually). Averaging traces over a subgroup gives the dimension of its invariant subspace in characteristic zero, producing dimensions \(0\) and \(10\). For a finite group acting simplicially, barycentric subdivision removes simplex inversions; the rational homology of the geometric quotient equals the invariant rational homology. This gives the quotient statements without implying integral torsion-freeness or contractibility.

## Verification
Execute `python3 verify_integral_homology.py` (Python with SymPy) and `python3 verify_character.py` (Python standard library). The first program constructs the full face complex, performs and validates the 256 elementary collapses, and computes the exact integer Smith normal form after tree-edge elimination. The second independently generates all 11520 affine symplectic transformations, verifies block preservation, calculates the closed character formula, and independently checks it by signed traces on **all 808 nonempty faces for every group element**. Both programs assert the published numerical results and produce the included `verification_output.txt` when run sequentially. The finite enumeration exhausts the entire stated finite group, rather than extrapolating from samples.

## Relationship to prior work
Classical Kummer biplane incidence geometry gives the sixteen-point symmetric design and its 11520-element point automorphism group. Previously published calculations established the nonequivariant homotopy type \(\mathbb{RP}^2\vee\bigvee^{55}S^2\) for the open neighborhood complexes of the rook and Shrikhande graphs. Another published investigation of this exact Kummer block complex determines the 240 minimum-support nontrivial mod-two one-cycles and their affine symplectic orbit. These results identify neither the rational degree-two character on all 11520 group elements nor the dimensions of both symmetry-invariant subspaces. In particular, an orbit computation for missing triangles in degree one over \(\mathbb F_2\) does not determine the degree-two rational representation. A separate homology-character result for the **closed-ball Čech complex** of rook graphs treats different simplices and is not equivalent.

## Limitations
The result is a finite complete character classification of the natural affine-symplectic subgroup; the rational character is given without a decomposition into named irreducible constituents. No integral module decomposition, geometric fixed-set classification, or contractibility of any quotient is asserted. Other biplanes need not have the same character. An unindexed equivariant computation of this complex may exist; independent mathematical validation has not been performed. The known nonequivariant classification is used solely as context and is not credited as a new result.

## References
- *Projective-plane summands in the open-neighborhood complexes of the Shrikhande and rook graphs*, publicly indexed mathematical study (2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-projective-plane-summands-in-the-open-neighborhood-complexes-of--8347d3b6f02e.
- *The 240 shortest mod-two one-cycles of the Kummer biplane and its sharp seven-vertex support threshold*, publicly indexed mathematical study (2026-10-25), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-240-shortest-mod-two-one-cycles-of-the-kummer-biplane-and-it--5ecd94cdc2b8.
- T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803v1 (2012-10-10), https://arxiv.org/abs/1210.2803.
- A. T. White, *Modelling biplanes on surfaces*, *European Journal of Combinatorics* 25 (2004), 899–909, https://doi.org/10.1016/j.ejc.2003.05.004.
- R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145.
