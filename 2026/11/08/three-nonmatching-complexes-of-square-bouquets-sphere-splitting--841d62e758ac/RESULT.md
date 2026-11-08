# Three-nonmatching complexes of square bouquets: sphere splitting and integral symmetry

## Finding
For an integer \(m\ge 1\), let \(B_m\) be the graph consisting of \(m\) four-cycles with exactly one common vertex, and otherwise disjoint vertex and edge sets. For a graph \(G\), let \(\operatorname{NM}_3(G)\) be the simplicial complex on \(E(G)\) whose faces are edge subsets with matching number at most two. Then
\[
\left|\operatorname{NM}_3(B_m)\right|\simeq \bigvee^{\binom{m}{2}}S^3.
\]
The empty wedge is a point, including \(m=1\). In particular, the only nonzero reduced integral homology is
\[
\widetilde H_3(\operatorname{NM}_3(B_m);\mathbb Z)\cong\mathbb Z^{\binom{m}{2}}
\quad(m\ge2).
\]
There is also a canonical signed-permutation description of the entire integral homology action of the graph automorphism group. Fix a direction on each four-cycle (equivalently, an ordering of its two neighbors of the shared vertex). An automorphism \(g\) permutes the cycle blocks by \(\sigma_g\), and induces a sign \(\epsilon_i(g)\in\{+1,-1\}\) according as the directed path of block \(i\) defined below is preserved or reversed when sent to block \(\sigma_g(i)\). There is an integral basis \(z_{ij}=z_{ji}\), indexed by unordered pairs of distinct blocks, satisfying
\[
 g_*z_{ij}=\epsilon_i(g)\epsilon_j(g)z_{\sigma_g(i),\sigma_g(j)}.
\]
For \(m\ge2\), the graph automorphism group is \((C_2)^m\rtimes S_m\). In particular, permutations of blocks act by the unsigned permutation module on their two-element subsets, and a reflection of a single block changes the signs of precisely the generators indexed by pairs containing that block.

## Assumptions and scope
All graphs are finite, simple, and undirected. The symbol \(B_m\) means *one-vertex* identification of \(m\) distinct unfilled four-cycles; it does not mean an edge-glued square book. Write their vertices as \(o,a_i,b_i,c_i\), with shared vertex \(o\), and their edges, in this order, as
\[
 p_i=oa_i,\qquad q_i=a_ib_i,\qquad r_i=b_ic_i,\qquad s_i=c_io,
 \qquad 1\le i\le m.
\]
The vertices of \(\operatorname{NM}_3(B_m)\) are the \(4m\) graph edges. A face is an arbitrary selection of those edges without three pairwise disjoint selected graph edges. A topological join is denoted by \(*\). All homotopy and homology statements are integral and nonequivariant except for the explicitly stated integral group action.

## Proof
**Step 1: classify all faces.** The selected outer edges \(q_i,r_i\) from any one block share \(b_i\), whereas outer edges belonging to distinct blocks are pairwise disjoint. Let \(T(F)\) be the set of indices whose outer edges occur in a selection \(F\). If \(|T(F)|\ge3\), the selection contains a matching of size three and is not a face. If \(|T(F)|\le1\), it is a face: at most one selected outer edge and at most one selected spoke \(p_i,s_i\) can belong to any matching, because all spokes contain \(o\). If \(T(F)=\{i,j\}\), a selected spoke outside these two blocks is disjoint from an outer edge of each block and is forbidden. Within block \(i\), the spoke \(p_i\) is allowed precisely when its only selected outer edge is \(q_i\); likewise \(s_i\) is allowed precisely when its only selected outer edge is \(r_i\). The same holds in block \(j\). These conditions are also sufficient: every possible three-matching would need both distinct outer blocks and one selected spoke disjoint from their selected outer edges, which the conditions exclude.

**Step 2: express the complex as a contractible core with three-balls.** Let \(U\) be the simplex on all \(2m\) spoke vertices \(p_i,s_i\). Let \(L\) be the simplicial disjoint union of the \(m\) edges \(\{q_i,r_i\}\) (including the empty simplex), and set \(A=U*L\). This is precisely the subcomplex of selections with at most one active outer block. Since \(U\) is a nonempty simplex, \(A\) is contractible.

For each block \(i\), define a simplicial path \(Y_i\) whose consecutive vertices are \(p_i,q_i,r_i,s_i\). Thus \(Y_i\) is a closed interval subdivided into three edges, with boundary subcomplex \(\partial Y_i=\{p_i,s_i\}\) consisting of its two endpoints. For each pair \(i<j\), put \(D_{ij}=Y_i*Y_j\). The join of two closed intervals is a closed three-ball. Step 1 gives the **exact equality of simplicial complexes**
\[
 \operatorname{NM}_3(B_m)=A\cup\bigcup_{1\le i<j\le m}D_{ij}.
\]
Furthermore,
\[
 A\cap D_{ij}=(\partial Y_i*Y_j)\cup(Y_i*\partial Y_j)
 =\partial D_{ij}\cong S^2.
\]
For two distinct pairs of block indices, any simplex in the intersection of their corresponding joins uses outer edges from at most one block, so their intersection is contained in \(A\). This verifies that distinct interiors of the attached three-balls are disjoint outside \(A\).

**Step 3: take a quotient by the contractible core.** The inclusion of the nonempty contractible subcomplex \(A\) is a CW cofibration; collapsing it to a point is a homotopy equivalence. After this quotient, each \(D_{ij}\) has its entire boundary collapsed and distinct balls meet only at the basepoint. Hence
\[
 \operatorname{NM}_3(B_m)/A\cong
 \bigvee_{1\le i<j\le m}(D_{ij}/\partial D_{ij})
 \cong\bigvee^{\binom m2}S^3.
\]
For \(m=1\), the union contains no three-balls and the complex is the full simplex on its four edge vertices. This proves the asserted homotopy classification and integral homology.

**Step 4: compute the integral symmetry action.** Orient each subdivided path \(Y_i\) from \(p_i\) to \(s_i\), writing its oriented relative one-chain as
\[
 c_i=[p_i,q_i]+[q_i,r_i]+[r_i,s_i].
\]
Its boundary is supported on \(\partial Y_i\). The join chain \(c_i*c_j\), for \(i<j\), consists of nine oriented tetrahedra; its boundary lies in \(\partial D_{ij}\subseteq A\). After quotienting by \(A\), it represents the oriented fundamental class \(z_{ij}\) of \(D_{ij}/\partial D_{ij}\). Reversing the direction of one path negates this class. Exchanging two one-dimensional path factors in their join has orientation sign \((-1)^{(1+1)(1+1)}=+1\), so transposing the block labels introduces no additional sign. Every automorphism is generated by block permutations and independent reversals, giving the stated signed two-subset action integrally. This argument uses actual relative fundamental cycles; it is not inferred from a rational character.

## Verification
Execute \(\texttt{python3 verify.py}\) with Python 3. The standalone script independently enumerates all edge subsets and all forbidden three-matchings for \(1\le m\le4\). It separately constructs the proposed core and all join-balls, and checks equality of the complete face sets and every claimed intersection. It computes simplicial mod-two homology directly from boundary matrices and checks the predicted ranks. It constructs explicit integral relative three-chains, checks their boundaries lie in the core, and verifies the orientation signs for generating automorphisms.

The complete results, with the empty face included in face counts, are: \(m=1\): 16 faces and no three-matching obstruction; \(m=2\): 137 faces and one sphere generator; \(m=3\): 715 faces and three sphere generators; \(m=4\): 3478 faces and six sphere generators. The executable ends with \(\texttt{ALL_VERIFY_OK}\). These finite checks test the implementation and small boundary cases; the universally quantified theorem is proved by Steps 1–4, not by finite extrapolation.

## Relationship to prior work
Shan and Wang (2026) show that a bipartite graph containing a simple cycle of length at least \(2t\) has persistent nonzero reduced homology of its \(t\)-nonmatching complex in dimension \(2t-3\). At \(t=3\), the hypothesis requires a simple cycle of length at least six. The square bouquet \(B_m\) has no such cycle: every simple cycle lies inside one square, so its circumference is four. The new result gives nonzero third homology for every \(m\ge2\) **outside** this sufficient-condition framework, and gives the exact homotopy and integral symmetry as well.

Holmsen and Lee's general bipartite Leray bound gives vanishing in degrees at least four for this \(t=3\) family, but does not give the homotopy type, the third Betti number, or the symmetry action. Linusson, Shareshian and Welker determine complexes of matching-restricted subgraphs of *complete* and *complete bipartite* graphs, not the specified sparse square bouquet. The argument here identifies an independent three-ball contribution for every unordered pair of four-cycles.

## Limitations
The construction is specific to the three-nonmatching complex and the one-vertex bouquet of unfilled four-cycles. It does not imply classifications at other matching thresholds, for edge-glued square books, or for arbitrary cactus graphs. The group action is on integral homology; no equivariant homotopy equivalence to a sphere wedge is claimed. The literature comparison is a best-knowledge originality assessment, not a proof that no equivalent unpublished or unindexed result exists.

## References
1. Jiawen Shan and Zexin Wang, *Homology of non-matching complexes under edge additions and applications to their Stanley-Reisner ideals*, arXiv:2609.02621, first posted 2026-09-02. https://arxiv.org/abs/2609.02621
2. Andreas F. Holmsen and Seunghun Lee, *Leray numbers of complexes of graphs with bounded matching number*, arXiv:2003.11270, first posted 2020-03-25. https://arxiv.org/abs/2003.11270
3. Svante Linusson, John Shareshian and Volkmar Welker, *Complexes of graphs with bounded matching size*, arXiv:math/0410345, first posted 2004-10-15, later J. Algebraic Combin. 27 (2008), 331–349. https://arxiv.org/abs/math/0410345
