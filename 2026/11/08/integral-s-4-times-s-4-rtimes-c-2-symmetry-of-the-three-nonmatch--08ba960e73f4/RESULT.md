# Integral \((S_4\times S_4)\rtimes C_2\)-symmetry of the three-nonmatching complex of \(K_{4,4}\)

## Finding
Let \(K_{4,4}\) have row and column vertex sets \(R=C=\{0,1,2,3\}\), and write \(E=R\times C\) for its sixteen edges. Let \(X\) be the simplicial complex on \(E\) in which a subset is a face if the associated bipartite graph has **no matching of size three**. Thus \(X=\operatorname{BNM}_3(4,4)=\operatorname{NM}_3(K_{4,4})\); this is not a complex of degree-at-most-two edge sets.

Put \(L_4=\ker(\mathbb Z^{4}\xrightarrow{\mathrm{sum}}\mathbb Z)\). Then
\[
\widetilde H_j(X;\mathbb Z)\cong
\begin{cases}
\bigwedge^2 L_4\otimes_{\mathbb Z}\bigwedge^2 L_4,&j=3,\\
0,&j\ne3.
\end{cases}
\]
This is an **integral** isomorphism, equivariant under independent permutations of rows and columns. The full graph automorphism group is \((S_4\times S_4)\rtimes C_2\). Its extra part-interchange involution acts on the displayed tensor product by the **positive** factor flip \(u\otimes v\mapsto v\otimes u\), without a minus sign.

For \(p\in S_4\), write \(\psi(p)=\operatorname{tr}(p\mid\bigwedge^2 L_4\otimes\mathbb Q)\). On cycle types \(1^4,2\,1^2,2^2,3\,1,4\), its values are respectively \((3,-1,-1,0,1)\). The complete rational character of \(\widetilde H_3\) is
\[
\chi(p,q)=\psi(p)\psi(q),\qquad
\chi((p,q)\tau)=\psi(pq),
\]
where \(\tau\) exchanges the two parts. In particular, \(\operatorname{tr}(\tau)=3\) and no nonzero rational third-homology class is fixed by the entire automorphism group.

## Assumptions and scope
The assertion concerns precisely four rows, four columns, and avoidance of three *pairwise vertex-disjoint* edges. A face may have large vertex degrees; imposing degree at most two defines a different complex. Orient a simplex by the ascending order of its edge indices \(4i+j\). All integral chains use this orientation. The theorem does not cover other board sizes or matching thresholds.

## Proof
**(1) Complete face poset and integral Morse homology.** There are \(\binom43(4)_3=96\) three-edge matchings; a face is exactly a subset containing none of them. Direct exhaustive enumeration gives \(3017\) faces including the empty face. By face cardinality from zero through eight, the numbers are \((1,16,120,464,932,912,448,112,12)\). Sort the sixteen edges lexicographically. Starting from the whole augmented face poset, for each edge in this order pair every still-unpaired face not containing that edge to the face obtained by adjoining it, whenever that larger face is still unpaired. This gives \(1504\) disjoint pairs and precisely nine unpaired four-edge faces. Direct the \(13504\) Hasse covers upward on matched pairs and downward otherwise. An exhaustive topological sort visits all \(3017\) faces, so the matching is acyclic. Every matched integral simplicial incidence is \(+1\) or \(-1\), and no critical face has dimension other than three. Integral algebraic/discrete Morse cancellation therefore gives \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^9\) and zero reduced integral homology in every other degree.

**(2) Explicit cycles.** For sorted triples \(I=(i_0,i_1,i_2)\subset R\) and \(J=(j_0,j_1,j_2)\subset C\), take the two disjoint perfect matchings
\[
M_0=\{(i_0,j_0),(i_1,j_1),(i_2,j_2)\},\quad
M_1=\{(i_0,j_1),(i_1,j_2),(i_2,j_0)\}.
\]
Their union is a six-cycle. On these six edge-vertices, avoiding a three-matching is exactly the join \(\partial\Delta^2*\partial\Delta^2\cong S^3\), because its only perfect matchings are \(M_0,M_1\). The oriented join of the two triangular boundary cycles defines an integral three-cycle \(z_{I,J}\) consisting of nine signed tetrahedra. Select the nine \(z_{I,J}\) with \(0\in I\) and \(0\in J\).

**(3) Primitive basis certificate.** In the acyclic matching, \(564\) lower three-simplices are paired with four-simplices, each with incidence \(\pm1\). Their dependency digraph is acyclic. Eliminate these coefficients from each of the nine cycles by subtracting the corresponding integral four-simplex boundaries in dependency order, then read the nine remaining critical-three coordinates. The resulting \(9\times9\) integer matrix is a negative signed permutation matrix with determinant \(-1\). Algebraic Morse cancellation identifies these critical coordinates with coordinates in reduced homology (the upper-three faces paired with two-simplices are subsequently eliminated). Therefore the nine cycles form a **unimodular integral basis** of \(\widetilde H_3\). This is stronger than rational independence or a rank comparison.

**(4) Full integral action.** The oriented triangle boundaries on triples of the four row labels realize \(\bigwedge^2L_4\): use \((e_j-e_0)\wedge(e_k-e_0)\) for \(0<j<k\), and use the tetrahedron relation \(u_{123}=u_{012}-u_{013}+u_{023}\). The analogous construction applies to column triples. The sixteen classes \([z_{I,J}]\) obey the product of these two triangle relations, and all \(576\) pairs \((p,q)\in S_4\times S_4\) act on the chosen nine-cycle basis by the exact integral Kronecker-product matrices for \(\bigwedge^2 L_4\otimes\bigwedge^2 L_4\). Transposing rows and columns sends \([z_{I,J}]\) to \([z_{J,I}]\) **with positive sign**. These identities are checked by oriented simplicial actions followed by the integral Morse reduction of (3); the standalone checker independently evaluates every case rather than inferring it from traces. Hence the claimed integral module and factor-interchange action hold.

**(5) Characters.** The character of \(L_4\) at \(p\) is its fixed-point count minus one. Thus \(\psi(p)=\frac12(\chi_{L_4}(p)^2-\chi_{L_4}(p^2))\), giving the stated five values. Tensor actions multiply traces. The trace of an operator followed by a tensor flip is the trace of the product of its two factors, giving the swapped formula. The absence of global invariants follows from the nontrivial irreducible rational \(S_4\)-module \(\bigwedge^2L_4\), or directly by averaging its displayed character.

## Verification
Run `python3 verify_bnm_3_44.py` from a directory containing the supplied standalone script; no third-party Python package is required. It reconstructs all faces and all directed Hasse incidences, checks an acyclic topological sort, verifies the boundaries of the nine explicitly oriented three-cycles, and proves their Morse-coordinate determinant is \(-1\). It checks \(5184\) integral sphere-cycle actions representing all \(576\) row/column permutation pairs, the nine factor-swap actions, the four-triple relations, and \(1152\) independent signed simplicial Lefschetz trace comparisons. The exact output is supplied separately in `verification_output.txt`. The finite calculation is exhaustive for this single complex and is not extrapolated to other sizes.

## Relationship to prior work
Linusson–Shareshian–Welker, arXiv:math/0410345, Theorem 1.4, already prove that \(\operatorname{BNM}_3(4,4)\simeq\bigvee^9S^3\); its nonequivariant homotopy and Betti number are *not* new here. Their Conjecture 1.14 predicts the rational \(S_r\times S_s\) hook-tensor representation for general sizes and thresholds. The result above establishes the \((r,s,k)=(4,4,3)\) case **integrally**, with explicit primitive cycles and also the bipartition exchange absent from that conjecture. Holmsen–Lee, arXiv:2003.11270, establish broader homological vanishing and Leray bounds for nonmatching complexes of arbitrary graphs, not the claimed integral group module.

The ordinary degree-bounded two-matching complex \(M_2(K_{4,4})\), the Morse complex of acyclic partial matchings, and configuration spaces of two points on \(K_{4,4}\) are distinct topological objects. Their published or indexed symmetry data do not logically give the representation here. Neither an absence of search results nor the class of this complex proves absolute priority; an equivalent calculation in unindexed literature remains possible.

## Limitations
This is a complete **finite** integral representation theorem for one canonical balanced case, not a proof of Conjecture 1.14 for arbitrary parameters. It does not determine the full equivariant homotopy type or equivariant attaching maps, and it does not imply any statement for degree-bounded matching complexes. Independent mathematical assessment and publication-priority confirmation have not been performed.

## References
- S. Linusson, J. Shareshian and V. Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345 (first public 2004-10-15), Theorem 1.4 and Conjecture 1.14. https://arxiv.org/pdf/math/0410345 .
- A. F. Holmsen and S. Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270 (first public 2020-03-25), Theorems 1.1–1.2. https://arxiv.org/pdf/2003.11270 .
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145. Standard acyclic-matching cancellation principle.
