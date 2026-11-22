# Three-torsion in the integral rotation lattice of the six-rung prism perfect-matching complex

## Finding
Write \(P=C_6\square K_2\) for the hexagonal prism graph and \(X=\mathcal M_p(P)\) for its **perfect-matching complex**: vertices of \(X\) are edges of \(P\), and a nonempty set of these edges is a simplex exactly when it is contained in some perfect matching of \(P\). Let \(r\) rotate the six prism columns by one step without interchanging the two layers. Then \(H_2(X;\mathbb Z)\) is a free abelian group of rank six, and
\[
\boxed{H_2(X;\mathbb Z)/(r_*-1)H_2(X;\mathbb Z)\cong\mathbb Z\oplus\mathbb Z/3\mathbb Z.}
\]
However, the rotation representation on \(H_2(X;\mathbb Q)\) is the six-dimensional **regular rational representation** of \(C_6\). In particular, the integral lattice \(H_2(X;\mathbb Z)\) is not isomorphic to the regular integral permutation lattice \(\mathbb Z[C_6]\): the latter has torsion-free coinvariants \(\mathbb Z\).

## Assumptions and scope
The graph's twelve vertices are \((i,s)\), for \(i\in\mathbb Z/6\mathbb Z\) and \(s\in\{0,1\}\). Its eighteen edges are six rungs \(\{(i,0),(i,1)\}\) and the twelve rim edges \(\{(i,s),(i+1,s)\}\). The rotation is \(r(i,s)=(i+1,s)\). All chain groups have their ordinary orientations determined by lexicographic ordering of graph edges; homology is unreduced in degree two, and all integral groups and maps use integral simplicial chains. The statement concerns exactly the six-rung prism, not the ordinary matching complex and not longer circular ladders. A graph matching is a perfect matching when it contains exactly six disjoint edges covering all twelve vertices.

## Proof
**1. Exhaustive finite chain model.** Enumerate all perfect matchings by selecting the least uncovered graph vertex and branching over all edges incident to it. This procedure considers every perfect matching exactly once and returns \(20\) perfect matchings of size six. Take all subsets of these matchings to form \(X\). In nonempty simplex dimensions \(0,1,2,3,4,5\), the face counts are respectively \(18,117,276,270,120,20\). Thus the signed boundary matrices required for degree-two homology have dimensions
\[
\partial_2:\mathbb Z^{276}\longrightarrow\mathbb Z^{117},\qquad
\partial_3:\mathbb Z^{270}\longrightarrow\mathbb Z^{276}.
\]
The included standalone checker reproduces all faces and boundary entries from the twelve labelled graph vertices, rather than importing a face table.

**2. Integral kernel and image, with no hidden torsion.** Apply integral column changes to \(\partial_2\), repeatedly selecting a unit pivot \(\pm1\) of minimum current pivot-row support, with lexicographic tie-breaking. Exactly \(100\) pairs are eliminated, and all remaining columns of \(\partial_2\) are zero. The same changes are propagated to the \(\partial_3\) target coordinates, leaving its entries in the \(100\) paired coordinates zero, as required by \(\partial_2\partial_3=0\). In the remaining \(176\) kernel coordinates, perform integral row and column operations using the same deterministic unit-pivot rule. Exactly \(170\) unit pairs are eliminated and the residual matrix is identically zero, leaving six free homology coordinates. Every operation is unimodular. The checker maintains both the \(276\)-dimensional basis matrix \(V\) and its inverse \(W\), and checks \(WV=I\), \(\partial_2V_{\mathrm{free}}=0\), and \(W_{\mathrm{free}}\partial_3=0\) against the original signed matrices. Hence the quotient is integrally \(\mathbb Z^6\); a rank computation over a field alone would not imply this.

**3. Integral rotation matrix.** On an oriented simplex \([e_0,e_1,e_2]\), rotate each graph edge, reorder the images lexicographically, and multiply by the sign of that reordering. Apply this signed permutation to each of the six integral cycle generators \(V_{\mathrm{free}}\), then read their coordinates in \(W_{\mathrm{free}}\). In the deterministic basis from Step 2 the resulting integral matrix is
\[
R=\begin{pmatrix}
0&-1&-1&0&0&1\\
0&0&0&0&1&-1\\
-1&-1&0&0&0&1\\
-1&0&0&0&0&0\\
0&-1&0&0&0&0\\
0&-1&-1&1&1&0
\end{pmatrix}.
\]
Direct integer multiplication gives \(R^6=I\) and \(\det(tI-R)=t^6-1\). Equivalently \(\operatorname{tr}(R^j)=0\) for \(1\le j\le5\), with identity trace six. Since finite cyclic representations over characteristic zero are semisimple, their characters determine the rational representation; this character is that of \(\mathbb Q[C_6]\).

**4. Exact coinvariants.** Let \(e_1,\ldots,e_6\) denote the six basis vectors of Step 3. The columns of \(R-I\) are the relations in the group of coinvariants. Writing \(t=e_6\), these relations successively yield
\[
e_4=t,\qquad e_1+e_3=-t,\qquad e_2=-2t,\qquad e_5=-t,\qquad 3t=0.
\]
The sixth relation is then redundant and no further relation constrains \(e_1\). Thus the presentation consists of a free generator \(e_1\) and an order-three generator \(t\), with no coupling. Equivalently, the integer Smith diagonal of \(R-I\) is \((1,1,1,1,3,0)\). This proves the boxed group isomorphism. The regular integral representation has free rank-one coinvariants, so the two integral lattices cannot be isomorphic. \(\square\)

## Verification
Run `python3 check_integral_rotation.py` in the same directory using Python 3 with NumPy and SymPy. The program constructs the graph, enumerates all perfect matchings and every face, builds signed chain boundaries, verifies \(\partial_2\partial_3=0\), and performs both integral unit-pivot eliminations while tracking the inverse change-of-basis matrices. It checks the original chains independently after reduction, constructs the induced signed rotation action, verifies the exact displayed \(R\), its order and characteristic polynomial, and its integral Smith factors. The supplied `check_output.txt` is the actual output of a successful execution. All arithmetic in the reductions is integral with explicit entry-growth guards; the final Smith calculation uses SymPy exact integer operations. This finite exhaustive computation is an integral proof for this **fixed finite complex**, not an extrapolation from samples to infinitely many graphs.

## Relationship to prior work
Agarwal and Basak, in the public version first including circular ladders on 2026-09-14, classified the nonequivariant homotopy types. At the six-rung parameter their result gives \(X\simeq\bigvee^6 S^2\), which determines the rank and lack of torsion of absolute homology, but not the integral action of rotation, nor its coinvariant torsion. A relevant published equivariant calculation for perfect-matching complexes of \(C_{6k}\square K_2\) explicitly assumes \(k\ge2\) and works with the lower four-dimensional **rational** homology. Its parameter range excludes the six-rung case, in which the two sphere dimensions coincide, and its rational character cannot imply the nontrivial integral Smith factor three. Results for ordinary matching complexes of hexagonal prisms and for Möbius-ladder perfect-matching complexes concern different simplicial complexes. The overlap searches are recorded in the review evidence; lack of a match does not prove publication priority.

## Limitations
Only the canonical one-column rotation on the integral second homology of the six-rung circular ladder is determined. The result does not describe the full integral \(D_6\times C_2\)-module, the quotient-space homology, extensions for all widths, or a genuine equivariant wedge decomposition. The exact chain computation can be reproduced but has not been independently mathematically validated. Parts of the closest original preprint's full revised text were inaccessible in this review; equivalent unindexed literature remains a residual priority risk.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601v2, circular-ladder version first posted 2026-09-14, https://arxiv.org/abs/2608.30601v2.
2. *Dihedral and layer-exchange modules in lower homology of circular-ladder perfect-matching complexes*, public research record, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-dihedral-and-layer-exchange-modules-in-lower-homology-of-circula--1a6ec2654f11.
3. Y. Wang, *Di-Forcing Polynomials for Cyclic Ladder Graphs*, Mathematics 11 (2023), 3598, https://doi.org/10.3390/math11163598 (background on perfect matchings, not a claim about integral homology actions).
