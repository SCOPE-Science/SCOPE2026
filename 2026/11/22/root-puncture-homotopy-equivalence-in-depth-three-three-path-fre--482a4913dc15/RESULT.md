# Root-puncture homotopy equivalence in depth-three three-path-free tree complexes

## Finding
Let \(T\) be a finite rooted tree of height three, with root \(r\), first-level vertices \(a_1,\ldots,a_m\), second-level vertices \(b_{ij}\) for \(1\le i\le m\), \(1\le j\le s_i\), and \(q_{ij}\) leaves \(c_{ijk}\) below \(b_{ij}\). Assume \(m\ge2\), every \(s_i\ge2\), and every \(q_{ij}\ge2\). All edges connect consecutive indicated levels, with no others. Put
\[
M=\sum_{i=1}^m s_i,\qquad B=\prod_{i=1}^m\prod_{j=1}^{s_i}(q_{ij}-1).
\]
For the two-independence simplicial complex \(K=\operatorname{Ind}_2(T)\) of all vertex sets inducing components of at most two vertices, write \(D=\operatorname{del}_r K=\operatorname{Ind}_2(T-r)\) and \(L=\operatorname{lk}_r K\). Then
\[
K\simeq *,\qquad D\simeq\bigvee^{B}S^{2M-1},\qquad L\simeq\bigvee^{B}S^{2M-1}.
\]
More strongly, the *actual simplicial inclusion* \(L\hookrightarrow D\) is a homotopy equivalence. The two complexes \(L\) and \(D\) both simplicially collapse onto the same subcomplex consisting of faces with none of the first-level vertices. Hence deleting the root creates exactly \(B\) nonzero primitive integral homology generators in dimension \(2M-1\), while the original complex is contractible.

For the perfect \(b\)-ary rooted tree of height three, \(b\ge2\), this gives \(M=b^2\) and \(B=(b-1)^{b^2}\). Its full complex is contractible and its root deletion is \(\bigvee^{(b-1)^{b^2}}S^{2b^2-1}\), with the root link having the same homotopy type and the inclusion a homotopy equivalence.

## Assumptions and scope
All complexes are finite abstract simplicial complexes and all homotopy equivalences refer to geometric realizations. The complex \(\operatorname{Ind}_2(G)\) admits precisely vertex subsets inducing maximum graph degree at most one; that characterization follows because a connected graph with at least three vertices contains a vertex of degree at least two or a path of length two. Here \(\operatorname{lk}_r K=\{\sigma\subseteq V(T)\setminus\{r\}:\sigma\cup\{r\}\in K\}\), and \(\operatorname{del}_r K=\{\sigma\in K:r\notin\sigma\}\). A simplicial collapse means a finite sequence of elementary free-face/coface removals. The wedge convention has \(B\) copies and the parameters guarantee \(B\ge1\). No orientation, automorphism character, or higher independence threshold is claimed.

## Proof
**1. A star calculation.** For a star on center \(b\) and leaf set \(C\) of size \(q\ge2\), let \(S_q=\operatorname{Ind}_2(K_{1,q})\). A face omitting \(b\) is an arbitrary subset of \(C\); a face containing \(b\) contains at most one leaf. Consequently
\[
S_q=\Delta(C)\cup\bigl(b*\operatorname{sk}_0\Delta(C)\bigr).
\]
Here \(\Delta(C)\) is the full simplex and the second term is the cone on its \(q\) vertices. Contract \(\Delta(C)\) to a point, obtaining \(q\) edges with common endpoints and hence \(S_q\simeq\bigvee^{q-1}S^1\). The argument uses only homotopy equivalences of CW pairs, so the conclusion holds over the integers.

**2. A common subcomplex.** Delete the first-level vertices \(a_i\) and the root \(r\), leaving the disjoint union of \(M\) stars centered at all \(b_{ij}\). Set
\[
U=\operatorname{Ind}_2\bigl(T-\{r,a_1,\ldots,a_m\}\bigr)
=\mathop{*}_{i,j} S_{q_{ij}}.
\]
The standard join equivalence \(X*Y\simeq\Sigma(X\wedge Y)\) for based connected CW complexes, applied to wedges of circles, gives \(U\simeq\bigvee^B S^{2M-1}\). In particular its integral reduced homology is free of rank \(B\) in exactly degree \(2M-1\).

**3. Root deletion collapses onto \(U\).** Fix \(i\). Write \(Q_i\) for the subtree rooted at \(a_i\), and \(C_i=\bigsqcup_j C_{ij}\) for all leaves within it. Put \(Y_i=\operatorname{Ind}_2(Q_i)\), \(U_i=\operatorname{Ind}_2(Q_i-a_i)=\mathop{*}_jS_{q_{ij}}\). Its vertex link at \(a_i\) is exactly
\[
E_i=\Delta(C_i)\cup\bigcup_{j=1}^{s_i}\left(b_{ij}*\Delta(C_i\setminus C_{ij})\right).
\]
Indeed, a face containing \(a_i\) contains at most one second-level \(b_{ij}\); if it contains that vertex, all leaves under it are excluded, while leaves belonging to all other second-level vertices are free. Because \(s_i\ge2\), each complement \(C_i\setminus C_{ij}\) has a leaf \(w_j\). Within the cone on \(b_{ij}\), pair each face containing \(b_{ij}\) but not \(w_j\) with that face plus \(w_j\), in descending cardinality order. These are elementary collapses *relative to* \(\Delta(C_i)\); cones for distinct \(j\) intersect only in that simplex. Thus \(E_i\searrow\Delta(C_i)\).

The decomposition \(Y_i=U_i\cup(a_i*E_i)\) has intersection \(E_i\subseteq U_i\). Coning the preceding elementary pairs with \(a_i\) collapses \(Y_i\) relative to \(U_i\) onto \(U_i\cup(a_i*\Delta(C_i))\). Choose any leaf \(w\in C_i\). Pair each remaining face containing \(a_i\) but not \(w\) with the face augmented by \(w\), again in descending cardinality. This removes the whole residual cone relative to its base in \(U_i\), proving \(Y_i\searrow U_i\). Since distinct subtrees \(Q_i\) are disjoint after deleting \(r\),
\[
D=Y_1*\cdots*Y_m\searrow U_1*\cdots*U_m=U.
\]
The simplicial join preserves each relative elementary collapse by ordering its paired joined faces by descending coface size.

**4. The root link collapses onto the same \(U\).** A face of \(L\) can contain at most one \(a_i\): two first-level vertices together with \(r\) would form a forbidden three-vertex induced path. If it contains \(a_i\), it cannot contain any of its second-level neighbors \(b_{ij}\), and it may contain an arbitrary subset of the leaves \(C_i\); all other branches are unrestricted elements of \(U_h\). Therefore, with \(J_i=U_i\cup(a_i*\Delta(C_i))\),
\[
L=U\ \cup\ \bigcup_{i=1}^m\left((a_i*\Delta(C_i))*\mathop{*}_{h\ne i}U_h\right).
\]
For every \(i\), its added faces containing \(a_i\) have no overlap with added faces containing any other \(a_h\). Pair these faces by adding/removing a fixed leaf \(w_i\in C_i\) in descending dimension, leaving all faces not containing \(a_i\) untouched. Thus \(L\searrow U\). These two collapses imply the map \(L\hookrightarrow D\) is a homotopy equivalence: both inclusions from \(U\) are homotopy equivalences and \(U\hookrightarrow L\hookrightarrow D\) is the direct inclusion.

**5. Contractibility.** Finally \(K=D\cup(r*L)\), a simplicial mapping cone of the inclusion \(L\hookrightarrow D\). As that inclusion is a homotopy equivalence between CW complexes, its mapping cone is contractible. This proves every assertion, including the exact integral homology and the uniform-branching corollary.

## Verification
The included dependency-free `CHECK.py` enumerates all two-independent faces of the complete binary height-three tree (15 vertices) and one nonuniform height-three tree (16 vertices). It verifies the precise root deletion/link decomposition and independently executes actual elementary relative collapses from \(D\) and \(L\) to \(U\), checking the free-face condition at every pair. It also computes all reduced mod-two Betti numbers directly by boundary-matrix elimination. In the binary case, \((|K|_{\mathrm{faces}},|D|_{\mathrm{faces}},|L|_{\mathrm{faces}},|U|_{\mathrm{faces}})=(9298,5329,3969,2401)\), with 1464 and 784 collapse pairs. The nonuniform example gives \((16372,9344,7028,4116)\) faces, and 2614 and 1456 collapse pairs. Both show zero reduced homology for \(K\) and precisely the predicted rank in dimension seven for \(D,L,U\). The checker tests finite examples only; the symbolic elementary-collapse proof above establishes the all-parameter theorem and integral claims.

## Relationship to prior work
Deshpande and Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448, Theorem 5.6, already classify the nonequivariant homotopy type of **perfect regular branching trees**. In particular, that theorem covers contractibility of the uniform height-three example; that contractibility is not proposed as new. Their treatment does not state the deletion/link equivalence or the full irregular branch-by-branch profile above. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (first public May 24, 2026), proves vertex decomposability for all trees and all \(r\); it implies wedge-of-spheres behavior but neither this exact puncture count nor the specified inclusion equivalence. The published 2026 classification *Root-deletion equivalence and integral symmetry of two-independence complexes of height-two trees* gives the height-two branch models contributing to \(D\). It does not state the **height-three** inclusion \(L\hookrightarrow D\), which is necessary to establish contractibility for arbitrary irregular branch data. Thus existing height-two calculations and uniform-tree contractibility are explicitly credited; the new result is the fully parameterized height-three local equivalence and its contractible-to-sphere-wedge puncture profile.

## Limitations
The hypothesis requires at least two second-level children under each first-level vertex and at least two leaves below every second-level vertex. No classification for arbitrary height-three trees outside these inequalities, higher heights, or \(\operatorname{Ind}_r\) with \(r\ne2\) is claimed. The integral homology assertions follow from the explicit sphere-wedge equivalences, rather than finite mod-two computations. No independent validation or exhaustive exclusion of unindexed equivalent prior statements has been performed.

## References
1. R. Sawant, *On the Vertex Decomposability of \(r\)-Independence Complexes of Trees*, arXiv:2605.25150v1 (first posted May 24, 2026), https://arxiv.org/html/2605.25150v1.
2. P. Deshpande and A. Singh, *Higher independence complexes of graphs and their homotopy types*, arXiv:2001.05448 (first preprint 2020; inspected version v2 dated February 1, 2021), Theorems 3.8 and 5.6, https://arxiv.org/pdf/2001.05448.
3. *Root-deletion equivalence and integral symmetry of two-independence complexes of height-two trees*, published November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-root-deletion-equivalence-and-integral-symmetry-of-two-independe--4e80582ccaae.
