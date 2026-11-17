# Rim-edge deletion in Möbius-ladder perfect-matching complexes: an integral periodic classification

## Finding
For each integer \(n\ge 2\), let \(M_{2n}\) have vertices \(0,1,\ldots,2n-1\), perimeter edges \(\{i,i+1\}\) (indices modulo \(2n\)), and antipodal edges \(\{i,i+n\}\) for \(0\le i<n\). Delete any **perimeter** edge \(e\), obtaining \(G_n=M_{2n}-e\). Write \(\mathcal P(G)\) for the simplicial complex whose faces are edge sets extendible to a perfect matching of \(G\), with all perfect matchings as facets. Then the *integral homotopy type* is

\[
|\mathcal P(G_n)|\simeq
\begin{cases}
 S^{n/2-1},&n\text{ even},\\
 S^{(n-1)/3},&n\equiv1\pmod6,\\
 S^{(n/3)},&n\equiv3\pmod6,\\
 *,&n\equiv5\pmod6.
\end{cases}
\]

In the second branch \(n\ge7\); in the third \(n\ge3\). The case \(n=2\) gives the disconnected zero-sphere. For odd \(n\), more precisely, there is an exact union of simplicial complexes
\[
\mathcal P(G_n)=\mathcal P(P_n\square K_2)\cup 2^F,
\qquad
\mathcal P(P_n\square K_2)\cap 2^F\cong\operatorname{Ind}(P_{n-1}),
\]
where \(F\) is the unique perfect matching using the remaining twisted cross-edge. Consequently \(|\mathcal P(G_n)|\simeq\Sigma|\operatorname{Ind}(P_{n-1})|\). For even \(n\), the extra cross-edge belongs to no perfect matching, and \(\mathcal P(G_n)=\mathcal P(P_n\square K_2)\) as complexes.

## Assumptions and scope
The perimeter edge removed is arbitrary: cyclic rotations act transitively on perimeter edges. The graph is a finite simple one-dimensional graph, not its filled clique complex. We use ordinary, nonequivariant homotopy and integral coefficients; contractible means the geometric realization has the homotopy type of a point. The square-ladder notation \(P_n\square K_2\) denotes the graph on two rows of \(n\) columns with horizontal edges within consecutive columns and one vertical rung per column. The simplicial complex \(2^F\) consists of every subset of the edge set \(F\).

## Proof
**Step 1 (normal form).** By rotation, choose the deleted edge to be \(\{0,2n-1\}\). Set \(u_i=i-1\) and \(v_i=n+i-1\), for \(1\le i\le n\). The surviving graph consists of the ordinary ladder \(L_n=P_n\square K_2\), together with precisely one extra cross-edge \(q=\{u_n,v_1\}\). The other perimeter cross-edge \(\{u_1,v_n\}\) was deleted.

**Step 2 (perfect matchings through the cross-edge).** Suppose a perfect matching uses \(q\). It consumes \(u_n\) and \(v_1\). The remaining endpoint \(u_1\) must be matched to \(u_2\), since the rung at its column ends at the already used \(v_1\). This forces \(v_2v_3\), since \(u_2\) is now used, then \(u_3u_4\), then \(v_4v_5\), and so forth. The forced alternating chain closes with a perfect matching *exactly when \(n\) is odd*. In that case it produces exactly one such matching
\[
F=\{q\}\cup \{u_i u_{i+1}:i\text{ odd},1\le i<n\}\cup\{v_i v_{i+1}:i\text{ even},1\le i<n\}.
\]
For even \(n\), the chain finishes with an unmatched endpoint; no matching contains \(q\). In either parity, perfect matchings not using \(q\) are exactly those of the open ladder \(L_n\).

**Step 3 (open-ladder homotopy, proved independently).** Let \(A_n=\mathcal P(L_n)\). A perfect matching of a two-row ladder begins either with the leftmost rung \(a_1\), leaving a perfect matching of the last \(n-1\) columns, or with both horizontal edges joining the first two columns, leaving a perfect matching of the last \(n-2\) columns. Thus
\[
A_n=(\{a_1\}*A_{n-1})\cup (2^{\{b_1,c_1\}}*A_{n-2}),
\]
where each factor is embedded in its natural edge coordinates and the intersection is precisely \(A_{n-2}\). Indeed, every matching of \(L_{n-2}\) extends to \(L_{n-1}\) by using the rung in the newly added column, so that intersection is literal. The two pieces are contractible cones, and hence \(A_n\simeq\Sigma A_{n-2}\) for every \(n\ge3\). Since \(A_1\) is a point and \(A_2\) is the disjoint union of the rung-pair simplex and horizontal-pair simplex, \(A_2\simeq S^0\). Therefore \(A_n\) is contractible if \(n\) is odd, and \(A_n\simeq S^{n/2-1}\) if \(n\) is even. In particular this establishes the even case of the theorem without assuming any earlier classification.

**Step 4 (exact attaching complex for odd width).** When \(n\) is odd, every matching facet of \(G_n\) is either a facet of \(A_n\) or the unique facet \(F\); hence \(\mathcal P(G_n)=A_n\cup2^F\). The cross-edge \(q\) is not a vertex of \(A_n\). Map the other \(n-1\) edges of \(F\) bijectively to positions \(i=1,\ldots,n-1\): the edge at position \(i\) is \(u_i u_{i+1}\) for odd \(i\), or \(v_i v_{i+1}\) for even \(i\). Each horizontal edge in an open-ladder perfect matching appears jointly with the parallel edge in the opposite row: the columns are tiled by width-one rung blocks or width-two paired-horizontal blocks. Therefore a subset of \(F\setminus\{q\}\) extends to a perfect matching of \(L_n\) **if and only if** no two selected positions are consecutive. Necessity follows because adjacent width-two blocks overlap a column; sufficiency follows by inserting paired horizontals at all selected positions and vertical rungs at all unoccupied columns. Consequently, the attaching subcomplex is literally \(A_n\cap2^F\cong\operatorname{Ind}(P_{n-1})\).

**Step 5 (homotopy type and boundaries).** For odd \(n\), \(A_n\) is contractible, so attaching the contractible simplex \(2^F\) along \(\operatorname{Ind}(P_{n-1})\) gives the homotopy cofiber of a nullhomotopic inclusion; thus \(\mathcal P(G_n)\simeq\Sigma\operatorname{Ind}(P_{n-1})\). By the standard path-independence classification, \(\operatorname{Ind}(P_m)\simeq S^{k-1}\) if \(m=3k\) or \(m=3k-1\), and is contractible if \(m=3k+1\). Substituting \(m=n-1\) produces the three odd branches. These are homotopy equivalences of finite CW spaces, hence establish all integral homology groups and fundamental groups, rather than merely mod-two Betti numbers. \(\square\)

## Verification
The standalone file `VERIFY.py` reconstructs all graph edges, exhaustively enumerates perfect matchings of the defective and open ladders by recursive unmatched-vertex elimination, verifies the parity-specific count of matchings containing the cross-edge, and checks the exact path-independence attaching condition for all odd widths \(3\le n\le13\). For widths \(2\le n\le12\), it independently generates every face and performs deterministic lexicographic face-poset matching, leaving precisely the critical cells predicted by the theorem. The gradient matching is acyclic: in a supposed closed alternating path, take the smallest pivot edge used by a matched pair; earlier coordinate bits cannot decrease, while an unmatched downward move that removes that pivot cannot connect two faces surviving to its pairing stage. Hence that pivot can increase but cannot decrease, ruling out a cycle. For a single critical vertex and one critical \(d\)-cell (or just a vertex), Forman's theorem gives \(S^d\) (or a point); at \(n=2\), two critical vertices give \(S^0\). Finite checks are supporting evidence, not the proof of the uniform classification. Run `python3 VERIFY.py` in the same directory as `verification_output.txt`.

## Relationship to prior work
Agarwal and Basak (2026), *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (first publicly posted 2026-08-31), determine perfect-matching complexes of **intact** Möbius and circular ladders. In contrast, the theorem above concerns deleting one **perimeter** edge of the Möbius ladder, changing the homotopy ranks to at most one sphere and yielding a contractible congruence class. Chandrakar and Singh (2024/2025), arXiv:2407.05809, analyze open two-row ladder perfect matching complexes; the open-ladder homotopy recurrence used here is proved again in Step 3. The standard path-independence result appears in Kozlov's work on independence complexes of paths and cycles. Earlier classifications for deletion of an **antipodal rung** concern a different edge orbit; results for the **ordinary** matching complex (all matchings) likewise do not determine perfect-matching extendibility. None of these statements by itself supplies the one-surviving-cross-edge decomposition and its path attaching complex.

## Limitations
The statement concerns deletion of exactly one perimeter edge, not an antipodal rung or more than one edge. It does not assert equivariant homotopy classifications, isomorphisms of the simplicial complexes, or homotopy behavior for different graph families. A differently formulated earlier classification not captured by accessible indexing remains possible; independent mathematical validation has not been performed.

## References
1. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601, first public version 2026-08-31; relevant v2 Sections 3 and 5, especially Theorem 21. https://arxiv.org/abs/2608.30601
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809, first public version 2024-07-08; Ann. Comb. 29 (2025), 1211–1233. https://arxiv.org/abs/2407.05809
3. D. N. Kozlov, *Complexes of directed trees*, J. Combin. Theory Ser. A 88 (1999), 112–122; path-independence classification as recalled in Agarwal–Basak, Proposition 7.
4. R. Forman, *Morse Theory for Cell Complexes*, Adv. Math. 134 (1998), 90–145; classical acyclic face-poset matching criterion.
