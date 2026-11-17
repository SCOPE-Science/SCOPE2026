# Integral homotopy and block symmetries of rooted biclique bouquets at higher robust thresholds

## Finding
Fix integers \(m\ge1\), \(t_i\ge2\) for \(1\le i\le m\), and \(k\ge4\). Form the connected bipartite graph \(G(\mathbf t)\) from distinct vertices \(h,b_1,\ldots,b_m\) and pairwise disjoint leaf sets \(L_i\) with \(|L_i|=t_i\). Join each leaf of \(L_i\) to \(h\) and \(b_i\), and introduce no other edges. Thus the graph is a one-vertex union of complete bipartite blocks \(K_{2,t_i}\), with their distinguished high-side vertex \(h\) identified.

For a finite graph \(G\), write \(R_k(G)=\{S\subseteq V(G):\alpha(G[S])<k\}\), a simplicial complex. Put \(r=k-1\) and \(a_i=t_i-1\). The main claims are
\[
 R_k(G(\mathbf t))\simeq\bigvee^{\sum_{I\subseteq[m],\,|I|=r}\prod_{i\in I}a_i} S^{2r-1},
 \qquad \widetilde H_j(R_k(G(\mathbf t));\mathbb Z)=0 \quad (j\ne 2r-1).
\]
In degree \(2r-1\), the homology is free, with its canonical integral action under the block-preserving automorphisms described below given by
\[
 \widetilde H_{2r-1}(R_k(G(\mathbf t));\mathbb Z)
 \cong\bigoplus_{\substack{I\subseteq[m]\\|I|=r}}
 \bigotimes_{i\in I}\ker\bigl(\mathbb Z[L_i]\xrightarrow{\,\mathrm{sum}\,}\mathbb Z\bigr).
\]
The summands are permuted by permutations of equal-size blocks; the tensor factors are exchanged without any additional sign.

Let \(\Gamma=(\prod_i\mathfrak S(L_i))\rtimes\Pi\), where \(\Pi\) only permutes indices of equal leaf-set size, acting via an arbitrary choice of compatible identifications of equal-sized blocks. If \(g\in\Gamma\) induces a block permutation \(\pi\in\Pi\), then its rational character is
\[
 \chi(g)=\sum_{\substack{I\subseteq[m],\,|I|=r\\\pi(I)=I}}
 \prod_{C\in\mathrm{Cycles}(\pi|_I)}\bigl(\#\mathrm{Fix}(\rho_C)-1\bigr),
\]
where \(\rho_C\) is the return permutation of the leaves of one block after traversing the cycle \(C\). It is well defined up to conjugacy, so its fixed-point count is unambiguous.

## Assumptions and scope
All graphs are finite and simple; no linear ordering or geometric drawing of blocks is assumed. The geometric realization of a simplicial complex is understood. The empty wedge denotes a contractible space, and an elementary symmetric polynomial of degree larger than the number of variables is zero. The theorem classifies the natural subgroup \(\Gamma\), not necessarily the entire automorphism group of the underlying graph. Its scientifically new scope is \(k\ge4\) and arbitrary, possibly unequal widths; the cases in which every \(t_i=2\) and the case \(k=3\) have antecedents and are not claimed as new.

## Proof
**1. Exact independent-set formula.** For \(S\subseteq V(G)\setminus\{h\}\), define \(q_i=1\) if \(b_i\in S\) and zero otherwise, and \(\ell_i=|S\cap L_i|\). Inside the graph induced by \(S\), distinct blocks have no connecting edges. Within block \(i\), the largest independent set has size \(\max(\ell_i,q_i)\). Consequently, with
\[a(S)=\sum_i\max(\ell_i,q_i),\qquad q(S)=\sum_i q_i,\]
one has
\[\alpha(G[S])=a(S),\quad\alpha(G[S\cup\{h\}])=\max\{a(S),1+q(S)\}.\]
The second identity separates independent sets omitting \(h\) from those containing it: if \(h\) is chosen, only the selected private vertices \(b_i\) can also be chosen.

**2. Acyclic matching.** Regard the augmented face poset of \(R_k(G)\), including the empty face. First match each admissible \(S\) omitting \(h\) with \(S\cup\{h\}\). This is possible precisely when the number \(q(S)\) of selected private vertices is at most \(r-1\). Every face containing \(h\) appears in such a pair. The remaining faces therefore have exactly \(r\) selected private vertices \(\{b_i:i\in I\}\), where \(|I|=r\), and may contain at most one leaf from each \(L_i\) for \(i\in I\), with no leaves in any other block. Fix one distinguished leaf \(c_i\in L_i\) for each block. In increasing block order, match an as-yet unmatched face lacking a leaf in \(L_i\) with the face obtained by adjoining \(c_i\). The unmatched faces have one leaf in \(L_i\setminus\{c_i\}\) for every \(i\in I\). They have \(2r\) vertices, hence dimension \(2r-1\), and are indexed by \((I,(\ell_i)_{i\in I})\) with \(\ell_i\ne c_i\). The number of unmatched faces is exactly \(\sum_{|I|=r}\prod_{i\in I}(t_i-1)\). The augmented empty face is paired with \(\{h\}\); removing that single pair from the matching on the nonaugmented face poset leaves \(\{h\}\) as the unique critical vertex.

To prove acyclicity, orient matched cover relations upward and all other cover relations downward. No matching ever changes which private vertices \(b_i\) are present, so along every directed edge this set can only decrease; a directed cycle must preserve it. For a fixed private-vertex set of size below \(r\), upward matched edges only add \(h\), and no directed edge removes \(h\); all remaining edges strictly lower face dimension. For a fixed set of size \(r\), \(h\) never occurs. The remaining face poset is a product of stars whose states in coordinate \(i\) are “no leaf” or “one particular leaf.” In a directed gradient path, after a matched addition of \(c_i\), deleting a leaf from a later coordinate cannot lead to the lower endpoint of another matching pair (since \(c_i\) remains); deleting an alternative leaf from an earlier coordinate moves the first matchable coordinate strictly backward. Thus every nontrivial alternating path strictly decreases that index and cannot close. This proves the full matching acyclic.

The ordinary (nonaugmented) discrete-Morse theorem for a nonempty finite simplicial complex then yields a CW model with a single \(0\)-cell and only the \((2r-1)\)-cells counted above. Because \(2r-1\ge5\), no nontrivial attaching map has dimension \(2r-2\) into the \(0\)-skeleton. The CW model is the claimed wedge of spheres. If \(r>m\), every face is paired and the complex is contractible.

**3. Canonical integral equivariance.** Although the distinguished-leaf matching is not equivariant, a separate relative-chain model is. Let \(A\) be the deletion of \(h\), and \(L\) its simplicial link. Since \(R_k(G)=A\cup(h*L)\) and the cone is contractible, the natural exact sequence gives a \(\Gamma\)-equivariant isomorphism \(\widetilde H_j(R_k(G);\mathbb Z)\cong H_j(A,L;\mathbb Z)\). Formula 1 shows that the relative faces \(A\setminus L\) are exactly those with \(r\) selected private vertices indexed by \(I\), no leaves outside \(I\), and at most one leaf in each selected block. Every face boundary term deleting a private vertex lies in \(L\); terms deleting a leaf remain in the same \(I\)-summand. The relative chain complex thus splits over \(I\). Its \(I\)-summand is the tensor product, with degree shift, of the two-term augmented complexes \(\mathbb Z[L_i]\xrightarrow{\mathrm{sum}}\mathbb Z\). These have homology only in their positive chain degree, where it is the free augmentation lattice. Hence their tensor product has only the stated homology, with no torsion or extension ambiguity.

To fix signs, orient each top simplex by listing each \(b_i\) immediately before its selected leaf, in increasing block order. Swapping two complete two-vertex blocks changes the vertex order by four transpositions and therefore acts with positive sign. Thus \(\Gamma\) exchanges tensor factors *without* a Koszul sign. On each factor, a leaf permutation acts through the ordinary augmentation representation. A tensor factor has character \(\#\mathrm{Fix}(\rho)-1\). Under a cyclic permutation of tensor factors, the trace is the trace of the composite return map on one factor; this follows by evaluating the tensor permutation in any basis. Summing over invariant block subsets proves the displayed character formula.

## Verification
A standalone Python program in `verify.py` reconstructs adjacency matrices and all independent-set numbers by a generic subset recurrence that does not use the blockwise formula. It enumerates all faces and builds the staged matching. The checker confirms that exactly the predicted faces are critical, that every face is accounted for, and that the entire oriented face-incidence graph is acyclic by topological sorting. It also computes signed simplicial Lefschetz traces for natural automorphisms and matches them to the integral-module character formula. The record `verification_output.txt` includes 21 exact matching-and-acyclicity cases and 24 character comparisons, ending with `ROBUST_BICLIQUE_BOUQUET_ALL_EXACT_TESTS_PASS` and `EQUIVARIANT_HOMOLOGY_CHARACTER_TESTS_PASS`. These finite tests provide independent reproducible checks, not the proof for arbitrary parameters; the argument above proves that range symbolically.

## Relationship to prior work
Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs* (arXiv:2602.11365, first public February 11, 2026), introduced these complexes and treated square-sequence graphs, including certain all-threshold graph extensions. The one-vertex bouquet operation here is different from its attachment conditions, and the present statement determines arbitrary leaf-block widths and an integral equivariant module. Bayer and collaborators, *Total Cut Complexes of Graphs* (arXiv:2209.13503), provide the Alexander-dual foundations and single-complete-bipartite examples but not the all-block result. A published three-robust classification for connected bipartite graphs already covers \(k=3\). Likewise, a previously obtained uniform four-cycle-bouquet formula covers the specialization in which every \(t_i=2\). Neither special statement determines this arbitrary-width, \(k\ge4\), integral representation theorem.

## Limitations
The result does not cover arbitrary one-vertex unions of general bipartite graphs, multi-hub amalgamations, or non-robust cut-complex conventions. Only the explicitly defined natural symmetry subgroup is classified, not any larger exceptional automorphism group. All novelty assessments are limited by accessible and indexed prior literature.

## References
1. M. Filakovský, *The Topology of k-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365 (first public 2026-02-11), https://arxiv.org/abs/2602.11365 .
2. M. Bayer et al., *Total Cut Complexes of Graphs*, arXiv:2209.13503 (first public 2022-09-27), https://arxiv.org/abs/2209.13503 .
3. *A three-sphere wedge theorem for robust clique complexes of all connected bipartite graphs* (published online 2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-three-sphere-wedge-theorem-for-robust-clique-complexes-of-all--8d06720b1a2b .
