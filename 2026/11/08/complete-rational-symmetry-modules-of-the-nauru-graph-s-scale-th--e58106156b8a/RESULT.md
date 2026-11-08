# Complete rational symmetry modules of the Nauru graph's scale-three Rips complex

## Finding
Let \(G=GP(12,5)\) be the 24-vertex Nauru graph with its unit-edge shortest-path metric, and put \(X=\operatorname{VR}_{\leq3}(V(G))\). Identify the graph automorphism group with \(A=S_4\times S_3\): a vertex is a permutation \((b_1,b_2,b_3,e)\) of four box labels, with \(e\) denoting an empty box, and adjacent vertices exchange \(e\) with one \(b_i\). The first factor permutes box labels; the second factor permutes the three object positions. Write \(V_m^\lambda\) for the rational Specht module indexed by a partition \(\lambda\) of \(m\), and \(\boxtimes\) for the external tensor product. Then the complete positive-degree rational homology representations are
\[
\begin{aligned}
H_3(X;\mathbb Q)&\cong \bigl(V_4^{(4)}\boxtimes V_3^{(3)}\bigr)\oplus\bigl(V_4^{(4)}\boxtimes V_3^{(1,1,1)}\bigr)\oplus\bigl(V_4^{(2,2)}\boxtimes V_3^{(3)}\bigr),\\
H_4(X;\mathbb Q)&\cong \bigl(V_4^{(2,2)}\boxtimes V_3^{(3)}\bigr)\oplus\bigl(V_4^{(2,2)}\boxtimes V_3^{(1,1,1)}\bigr),\\
H_5(X;\mathbb Q)&\cong V_4^{(1,1,1,1)}\boxtimes V_3^{(1,1,1)}.
\end{aligned}
\]
All other positive-degree rational homology vanishes. The degrees \(3,4,5\) have dimensions \(4,4,1\), respectively; their full \(A\)-fixed dimensions are \(1,0,0\). In particular the top homology is the sign character of the action on the two graph bipartition classes, while degree three has exactly one globally invariant class. The complete character is also specified on all 15 product conjugacy classes in `character_table.json`.

## Assumptions and scope
The Nauru graph is specified by the geometric graph \(GP(12,5)\), whose vertex set consists of outer vertices \(u_i\) and inner vertices \(v_i\), for \(i\in\mathbb Z/12\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+5}\). Equivalently it is the star-transposition graph of \(S_4\). The included verifier checks an explicit bijection between these models. Rips simplices are all nonempty vertex subsets of pairwise **graph distance at most three**; Euclidean distance in a drawing is not used. The full graph-automorphism group really is \(A\), not merely a selected subgroup: the 144 displayed actions are distinct graph automorphisms, and fixing a vertex and its three neighbors fixes every vertex, as certified by iterative neighbor-color refinement. Thus \(|\operatorname{Aut}(G)|\le24\cdot3!=144\), establishing equality.

## Proof
**1. The two canonical tori.** The Cayley graph is bipartite by permutation parity. Write \(U\) and \(W\) for its two 12-element bipartition classes. Its diameter is four; all cross-class distances are one or three, while nonzero within-class distances are two or four. Hence every cross-class pair is adjacent in the scale-three Rips graph, and each induced factor \(T_U=X[U]\), \(T_W=X[W]\) is a clique complex on the distance-two pairs within its class. The resulting simplicial identity is \(X=T_U*T_W\). The exact enumerations give, for each factor, \((f_0,f_1,f_2)=(12,36,24)\), every edge in precisely two triangles, and a connected six-cycle link at every vertex. The triangle adjacency propagation exhibits a consistent global orientation, and the entire triangle adjacency graph is connected. Each factor is therefore a connected closed orientable triangulated surface of Euler characteristic zero, hence a two-torus. In particular its integral homology is \(H_0\cong\mathbb Z\), \(H_1\cong\mathbb Z^2\), \(H_2\cong\mathbb Z\).

**2. Natural group action on the join.** For a graph automorphism \(g\), let \(g_U\) and \(g_W\) denote its restrictions when it preserves the classes. Put \(t_U=\operatorname{tr}(g_U\mid H_1(T_U;\mathbb Q))\) and \(\delta_U=\deg(g_U\mid H_2(T_U;\mathbb Z))\in\{\pm1\}\), with analogous notation for \(W\). The join Künneth formula gives
\[
\widetilde H_k(X;\mathbb Q)=\bigoplus_{p+q+1=k}\widetilde H_p(T_U;\mathbb Q)\otimes\widetilde H_q(T_W;\mathbb Q).
\]
For class-preserving \(g\), this implies the separate traces
\[
\chi_3(g)=t_Ut_W,\qquad \chi_4(g)=t_U\delta_W+\delta_Ut_W,\qquad \chi_5(g)=\delta_U\delta_W.
\]
If \(g\) exchanges the factors, the swap of oriented joined simplices in degrees \(p,q\) introduces sign \((-1)^{(p+1)(q+1)}\). Consequently \(\chi_4(g)=0\), \(\chi_3(g)=\operatorname{tr}(g^2\mid H_1(T_U;\mathbb Q))\), and \(\chi_5(g)=-\deg(g^2\mid H_2(T_U;\mathbb Z))\). These identities distinguish the individual homology degrees, unlike an alternating Lefschetz trace alone.

**3. Exact finite traces.** In either torus, let \(L_T(h)\) denote the signed simplicial Lefschetz number of a class-preserving automorphism. The Lefschetz identity on the oriented torus reads \(L_T(h)=1-\operatorname{tr}(h\mid H_1)+\deg(h\mid H_2)\). The sign on \(H_2\) is computed from the explicitly propagated primitive orientation cycle (the signed sum of all 24 triangular facets). The verifier enumerates all 144 automorphisms, evaluates these exact face signs, and applies the formulas of Step 2. No floating-point computation or inferred homology concentration is used.

**4. Character decomposition.** Evaluate the three character functions on representatives of the five conjugacy classes of \(S_4\) and three of \(S_3\). Their values are reproduced in `character_table.json`. Exact inner products with the tensor products of the ordinary symmetric-group irreducible character tables yield precisely the stated constituents, all with multiplicity one. As a second independent trace test, enumeration of all 5,328 nonempty faces of \(X\) verifies, for each of the 144 automorphisms, the identity \(L_X(g)=1-\chi_3(g)+\chi_4(g)-\chi_5(g)\). The rank and torsion-freeness of each integral homology group follow directly from the integral torus join formula; no Smith-normal-form inference is required.

## Verification
Execute `python3 verify_nauru_symmetry.py` using only the Python standard library. The script checks the explicit \(GP(12,5)\) isomorphism, complete graph-distance matrix, bipartition torus certificates, 144 distinct graph-automorphisms and their completeness, all 15 product conjugacy-class character values, the three rational decompositions, and the full-complex signed Lefschetz identity for **all** group elements. The exact final marker is `NAURU_COMPLETE_S4_S3_RIPS3_CHARACTER_PASS 144_AUTOMORPHISMS 5328_FACES 15_CLASSES`. The recorded `verification_output.txt` reproduces the check. No external code or precomputed hidden certificate is required.

## Relationship to prior work
Eppstein (2007) identifies this graph as \(GP(12,5)\), gives its star-transposition model, its 144-element symmetry group, and a toroidal hexagonal embedding of the original graph; a toroidal embedding is not a computation of an equivariant Rips homology representation. Adamaszek (2011) develops clique complexes of graph powers and focuses on stability and cycles; the results do not specify this graph's complete degree-wise symmetry modules. Adamaszek and Adams (first public 2015) classify Rips complexes of subsets of a metric circle, not this finite graph metric. The closest published graph-specific analysis, *Complete Rips homotopy and persistence of the Nauru graph*, proves the **nonequivariant** homotopy and persistent homology and the decomposition of \(X\) as a join of two tori. Those topological facts are acknowledged as prior and are not claimed new. Its statements do not specify the actions on the two factor homology lattices, the graded swap sign, or any of the 15 class values and irreducible constituents computed here. In particular the new character classification does not follow from the nonequivariant wedge dimensions alone.

## Limitations
The result classifies the rational \(A\)-modules in precisely one Rips filtration stage of this 24-vertex metric graph. It does not classify integral \(\mathbb Z[A]\)-module extensions, equivariant homotopy types, or actions on Rips complexes for arbitrary generalized Petersen graphs. The result is an exact finite computation plus standard surface, join, Lefschetz and character-theoretic arguments. It has not undergone independent mathematical audit; unindexed equivalent calculations, or an implicit equivariant refinement of a published torus construction, remain possible.

## References
1. D. Eppstein, *The many faces of the Nauru graph*, 2007-12-12, https://11011110.github.io/blog/2007/12/12/many-faces-of.html .
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first posted 2011-04-03, https://arxiv.org/abs/1104.0433 .
3. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669, first posted 2015-03-12, https://arxiv.org/abs/1503.03669 .
4. *Complete Rips homotopy and persistence of the Nauru graph*, publicly available mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-rips-homotopy-and-persistence-of-the-nauru-graph--18d90d4ed629 .
