# Integral homology of Möbius ladders after one rim-edge deletion

## Finding
For each integer \(n\ge4\), let \(M_{2n}\) be the simple graph on \(\mathbb Z/(2n)\) whose edges join cyclic neighbors and antipodal pairs. Delete exactly one **cycle (rim) edge** \(e\), not an antipodal rung, and set \(X_n=\operatorname{Ind}(M_{2n}-e)\). Its reduced integral homology is completely determined by \(n\bmod4\):

\[
\widetilde H_j(X_n;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&n=4k,\ k\ge1,\ j=2k-1,\\
\mathbb Z,&n=4k+1,\ k\ge1,\ j=2k,\\
\mathbb Z^2,&n=4k+2,\ k\ge1,\ j=2k,\\
0,&\text{otherwise}.
\end{cases}
\]

In particular, every reduced integral homology group is torsion-free; every \(n\equiv3\pmod4\) with \(n\ge7\) yields an **acyclic** complex. Acyclicity is not asserted to imply contractibility, and this result does not claim a complete homotopy decomposition of \(X_n\).

## Assumptions and scope
For any finite simple graph \(G\), \(\operatorname{Ind}(G)\) consists of all independent vertex sets, including the empty face. For a graph with no vertices its augmented independence complex represents \(S^{-1}\); only cases with \(n\ge4\) are used in the theorem. All chains and homology groups in the theorem are integral. All cycle-edge choices are equivalent by rotation. Put \(L_n=P_n\square K_2\), with upper vertices \(t_0,\ldots,t_{n-1}\), lower vertices \(b_0,\ldots,b_{n-1}\), horizontal edges in each row and vertical rungs \(t_i b_i\). Under a cyclic rotation and a relabeling, \(M_{2n}-e\) is \(L_n\) plus the edge \(t_0b_{n-1}\). Write \(K_n=\operatorname{Ind}(L_n)\), \(Y_n=\operatorname{Ind}(L_n+t_0b_{n-1})\); thus \(Y_n\cong X_n\).

## Proof
**1. Ladder fold.** The graph-fold lemma says that if the open neighborhoods satisfy \(N(w)\subseteq N(v)\), deleting \(v\) induces a homotopy equivalence of independence complexes. In the first two columns of \(L_n\), \(N(b_0)\subseteq N(t_1)\), so remove \(t_1\). Afterward \(N(t_0)\subseteq N(b_1)\), so remove \(b_1\). This leaves an isolated rung \(t_0b_0\) disjoint from \(L_{n-2}\). Repeat on subsequent pairs. The surviving graph is exactly the disjoint union of \(\lceil n/2\rceil\) rungs, whence
\[
K_n\simeq (S^0)^{*\lceil n/2\rceil}\simeq S^{\lceil n/2\rceil-1}.
\]
In particular, this is an **integral** equivalence, not an inference from field Betti numbers.

**2. The added-edge relative complex.** In \(L_n\), put \(u=t_0\), \(v=b_{n-1}\); they are nonadjacent. Define \(B_n=\operatorname{Ind}(L_n-(N[u]\cup N[v]))\). Every simplex of \(K_n\) missing from \(Y_n\) has the unique form \(\{u,v\}\cup\sigma\), where \(\sigma\) is a face of \(B_n\). Deleting \(u\) or \(v\) from such a face lands in \(Y_n\). Hence the integral relative chain complex is the augmented chain complex of \(B_n\) shifted by two, giving
\[
H_j(K_n,Y_n;\mathbb Z)\cong\widetilde H_{j-2}(B_n;\mathbb Z).
\]
The graph defining \(B_n\) has upper vertices \(t_2,\ldots,t_{n-2}\) and lower vertices \(b_1,\ldots,b_{n-3}\), with the inherited horizontal edges and all available vertical rungs.

**3. Exact link reduction.** For \(n=4\) this graph consists of two isolated vertices, and for \(n=5\) it is a four-vertex path; both independence complexes are contractible. For \(n=6,7\), successive graph folds remove \(t_2\), \(b_3\), and (if \(n=7\)) \(t_5\), \(b_4\), leaving two disjoint edges. Therefore \(B_6\simeq B_7\simeq S^1\). For every \(n\ge8\), the four folds deleting \(t_2,b_3,t_5,b_4\), witnessed respectively by \(b_1,b_1,t_3,t_3\), leave precisely two disjoint edges \(b_1b_2\) and \(t_3t_4\), together with a graph isomorphic to the graph underlying \(B_{n-4}\). Each neighborhood containment follows directly from the displayed rail-and-rung adjacency; no other edge meets these two isolated edges. Thus
\[
B_n\simeq \Sigma^2 B_{n-4}\quad(n\ge8).
\]
By induction, \(B_n\) is contractible for \(n\equiv0,1\pmod4\) and is homotopy equivalent to \(S^{2k-1}\) for \(n=4k+2\) or \(4k+3\), \(k\ge1\).

**4. The degree-one boundary case.** For \(n=4k+3\), \(k\ge1\), the relative group \(H_{2k+1}(K_n,Y_n)\) and \(\widetilde H_{2k+1}(K_n)\) are both \(\mathbb Z\); the map between them needs an integral degree calculation. For each even column let the reduced zero-cycle on its rung be \([t_i]-[b_i]\). Their iterated join \(z\) over \(i=0,2,\ldots,n-1\) is an integral cycle in \(K_n\) of degree \(2k+1\). The alternating choice \(T=\{t_0,b_2,t_4,b_6,\ldots,b_{n-1}\}\) is a maximal independent set in \(L_n\); thus the cochain taking value \(1\) on \(T\) and \(0\) on the other oriented top-dimensional faces is a cocycle evaluating \(\pm1\) on \(z\). As \(\widetilde H_{2k+1}(K_n)\cong\mathbb Z\), \([z]\) is a primitive generator.

The quotient chain map to \(C_*(K_n,Y_n)\) retains exactly the summands of \(z\) containing \(t_0\) and \(b_{n-1}\). After removing these two vertices the image is, up to sign, the iterated join \(z'\) of the rung zero-cycles at even columns \(2,4,\ldots,n-3\). The alternating independent set \(T'=T\setminus\{t_0,b_{n-1}\}\) is maximal in the graph defining \(B_n\): the two terminal leaves and each intermediate odd-column vertex are adjacent to a selected vertex. Its indicator cochain is a cocycle evaluating \(\pm1\) on \(z'\). Because \(\widetilde H_{2k-1}(B_n)\cong\mathbb Z\), the relative map is multiplication by \(\pm1\), rather than zero or a nonunit integer. The integral long exact sequence of \((K_n,Y_n)\) therefore makes every reduced homology group of \(Y_n\) vanish in this residue class.

**5. The remaining degrees.** If \(n\equiv0,1\pmod4\), the relative groups vanish and the ladder sphere's homology carries over unchanged to \(Y_n\). If \(n=4k+2\), the only relative homology is \(H_{2k+1}(K_n,Y_n)\cong\mathbb Z\), while \(\widetilde H_{2k}(K_n)\cong\mathbb Z\). The long exact sequence gives \(0\to\mathbb Z\to\widetilde H_{2k}(Y_n)\to\mathbb Z\to0\), which splits over \(\mathbb Z\). All remaining reduced groups vanish. This proves the claim, including integrality and absence of torsion.

## Verification
The standalone Python file `checks/verify.py` independently builds the original cyclic graph and the twisted-terminal ladder graph and confirms graph equality after choosing an equivalent rim edge. It exhaustively enumerates independent faces for \(4\le n\le10\), computes the reduced boundary ranks over \(\mathbb F_2\), checks all four graph-fold neighborhood containments and the complete recurrence edge sets, and verifies maximal-face primitive certificates for \(n=7,11,15\). It reports `RIM_DELETION_HOMOLOGY_CHECK_PASS`; raw output is embedded as `checks/output.txt`. These finite computations corroborate the unrestricted integral proof and do not independently certify all integers or integral torsion.

## Relationship to prior work
Agarwal and Basak, arXiv:2608.30601, first submitted August 31, 2026, classify the independence complexes of **intact** Möbius and circular ladders and their perfect-matching complexes. The 19-page primary PDF was inspected in its introduction and its full independence-complex results (Lemmas 10–14 and Theorems 12, 15, pages 6–10), with a visual check of page 6. Those statements classify intact graphs and vertex-deleted graphs, not deletion of a rim edge. The present complex has one rim edge removed, so its homology need not follow from that classification. Previously published results on the different operation of deleting an antipodal **rung** were compared by statement: a rim edge and an antipodal rung belong to different automorphism orbits, and the established rung result covers different complexes. No identified result proves the rim-deleted homology formula; unindexed equivalent work remains an originality risk. The graph-fold method is standard and is not claimed as new.

## Limitations
Only ordinary independence complexes, a single deleted **rim** edge, and integer \(n\ge4\) are classified. The theorem determines integral homology, not simple homotopy, the full homotopy type, persistence maps, or simultaneous multiple-edge deletions. Mod-two finite checks do not prove torsion-freeness; the relative integral chain argument does.

## References
- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public 2026-08-31, https://arxiv.org/abs/2608.30601.
- S. Goyal, S. Shukla and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926, https://arxiv.org/abs/1905.06926 (general background on graph reductions and suspensions; not a premise of the proof).
