# Parity-controlled token mobility of minimum dominating sets on cyclic prisms

## Finding

Write \(P_n=C_n\square K_2\), with vertex set \(\{t_i,b_i:i\in\mathbb Z/n\mathbb Z\}\), horizontal edges \(t_it_{i+1}\), \(b_ib_{i+1}\), and rungs \(t_ib_i\), for integers \(n\ge3\). A *dominating set* is a set \(S\) such that every vertex belongs to \(S\) or has a neighbor in \(S\). A *minimum* dominating set has cardinality \(\gamma(P_n)\).

The **token-slide graph** \(\mathcal T_n\) has the minimum dominating sets as vertices, and joins two when one replaces a selected vertex by an adjacent unselected vertex of \(P_n\), remaining minimum dominating. The **token-jump graph** \(\mathcal J_n\) uses the same replacement rule without requiring adjacency.

**Theorem (zero-or-one-defect regimes).** For all integers \(n\ge3\) with \(n\not\equiv2\pmod4\),

\[
\mathcal T_n\cong
\begin{cases}
K_3\square K_3,&n=3,\\
4K_1,&n\equiv0\pmod4,\\
2nK_1,&n\equiv1\pmod4,\ n\ge5,\\
C_{2n},&n\equiv3\pmod4,\ n\ge7,
\end{cases}
\]

and

\[
\mathcal J_n\cong
\begin{cases}
K_3\square K_3,&n=3,\\
4K_1,&n\equiv0\pmod4,\\
C_{2n},&n\text{ odd},\ n\ge5.
\end{cases}
\]

For every odd \(n\ge5\), there are exactly \(2n\) optimal states and \(2n\) token-jump edges. The token-jump graph has radius and diameter \(n\); when \(n\equiv3\pmod4\), the same holds for the token-slide graph. When \(n\equiv1\pmod4\), **every optimal state is slide-frozen although the jump graph is one long cycle**. For \(n\equiv0\pmod4\), both reconfiguration graphs have four isolated states.

## Assumptions and scope

Graphs are finite, simple, undirected and vertex-labeled; \(C_3\) is a triangle. A token replacement changes precisely one member of the selected set. We classify ordinary (closed-neighborhood) domination, not total or independent domination; jumps are not necessarily edges of the host graph. The result covers every odd cycle length and every length divisible by four; the two-defect regime \(n\equiv2\pmod4\) is deliberately **not** claimed. The optimal-state count itself is background from the cyclic-prism literature; the transition graphs and exact movement distances are the contribution.

## Proof

**1. Optimal cardinality and absence of double columns.** Every vertex of \(P_n\) has closed neighborhood of size four, so \(\gamma(P_n)\ge\lceil n/2\rceil\). For \(n\equiv0\pmod4\), placing alternating top and bottom tokens at alternate columns achieves \(n/2\). For odd \(n\ge5\), the cyclic singleton construction in Step 2 achieves \((n+1)/2\). For \(n=3\), one top and one bottom token dominate both triangles and attain two. Thus the lower bound is sharp in every claimed case.

Call a column \(A\) if only its top vertex is selected, \(B\) if only its bottom is selected, \(C\) if neither is, and \(D\) if both are. If \(n\equiv0\pmod4\), an optimal set has exactly \(n/2\) tokens and its closed neighborhoods have total cardinality \(4(n/2)=2n\). They must therefore be pairwise disjoint. In particular no \(D\)-column is possible.

Now let \(n\ge5\) be odd, and write \(m=(n+1)/2\). An optimal set has \(m\) tokens and the sum of the cardinalities of their closed neighborhoods is \(4m=2n+2\). Thus any such covering has exactly two excess incidences above one coverage per vertex. Suppose it has both tokens in column zero. Their closed neighborhoods already have exactly two repeated incidences (at \(t_0,b_0\)) and together cover both rows of columns \(-1,0,1\). Every further token would have to contribute a closed neighborhood disjoint from this six-vertex union and from all other token neighborhoods. Consequently no further token may lie in columns \(-2,-1,1,2\): each such token's closed neighborhood intersects that union. Yet both vertices of column 2 still require domination. If \(n=5\), their only possible selected neighbors lie in forbidden columns 1, 2, or 3 (where 3 is \(-2\)), a contradiction. If \(n\ge7\), their only possible selected neighbors are respectively \(t_3\) and \(b_3\); both would have to be selected, creating further repeated incidences and contradicting the exhausted excess budget. Thus no minimum set contains \(D\) for odd \(n\ge5\).

**2. Exact minimum words.** With no \(D\), two adjacent \(C\)-columns are impossible: each of the two rows in the first empty column must then be covered from the preceding column, forcing a \(D\) there. For \(n=4k\), there are exactly \(2k\) singleton columns and \(2k\) empty columns, so the word alternates singleton and \(C\). Every \(C\) must be flanked by one \(A\) and one \(B\), since both row vertices need horizontal coverage. There are precisely four words, specified by the parity of occupied columns and the color of the first singleton.

For odd \(n=2m-1\ge5\), there are \(m\) singleton columns and \(m-1\) empty columns. With no consecutive \(C\)'s, exactly one gap between consecutive \(C\)'s contains two consecutive singletons, and every other gap contains exactly one. Let that distinguished pair be \(x,y\) at columns \(i,i+1\), with \(x,y\in\{A,B\}\). All remaining letters are forced by the rule that each \(C\) has complementary singleton neighbors. The singleton at column \(i-2\) has the color opposite to \(x\); the singleton at \(i+3\) has the color opposite to \(y\). Between these two outer singletons lie exactly \(m-3\) isolated \(C\)'s, each reversing the singleton color. Therefore \(x=y\) precisely when \(m\) is odd, namely \(n\equiv1\pmod4\), and \(x\ne y\) precisely when \(m\) is even, namely \(n\equiv3\pmod4\). Choosing the index \(i\) and \(x\in\{A,B\}\) uniquely constructs a feasible minimum word. This gives exactly \(2n\) states.

**3. All possible jumps in the odd regime.** The occupied-column support is a minimum vertex cover of the column cycle: empty columns form an independent set and there is precisely one adjacent occupied pair. It is unchanged by a same-column row swap, but for a fixed support the coloring is one of two globally complementary words. The two colorings differ at all \(m\ge3\) selected vertices, so they are not related by one-token replacement. If the occupied-column support changes by removing a singleton outside the distinguished pair, both its neighboring columns become empty and filling only one of them leaves two adjacent empty columns, impossible. Removing the left member \(x\) of the pair must be accompanied by filling the empty column \(i-1\); removing the right member \(y\) must fill \(i+2\). In either case the newly empty column demands opposite colors on its two neighbors, uniquely determining the target row. All other empty columns retain valid flanks, so both moves are legal jumps.

Parameterize a state by \((i,x)\), with \(i\) the first column of the distinguished pair and \(x\) its color. A left jump replaces \(x\) in column \(i\) by the complementary color in column \(i-1\) when \(x=y\), or by the same color when \(x\ne y\). The new distinguished pair starts at column \(i-2\), whose color is the complement \(\bar x\). Thus the left-jump action on state parameters is

\[
F(i,x)=(i-2,\bar x),
\]

and its inverse is the right jump. Because \(n\) is odd, translation by \(-2\) visits all \(n\) column indices, and after \(n\) repetitions the color is reversed. Hence \(F\) is a single permutation cycle of length \(2n\). The two jumps are distinct for \(n\ge5\), so \(\mathcal J_n\cong C_{2n}\).

**4. Slides and remaining cases.** In the odd case, the two jumps always change the occupied column by one. They are slides along a horizontal host edge if and only if the new token stays in its original row. From the new-empty-column constraint this happens exactly when \(x\ne y\), hence exactly when \(n\equiv3\pmod4\). The other parity admits no slides. For \(n=4k\), the four minimum words differ pairwise in at least two token locations (for opposite occupied-column parity, at least \(n/2\ge2\); for the same parity but opposite singleton colors, exactly \(n/2\ge2\)). No single-token jump or slide is possible. Finally, \(P_3=K_3\square K_2\) has exactly the nine minima choosing one vertex from each of its two triangles; replacing one chosen vertex inside its triangle gives either type of move, and no other replacement works. The corresponding graph is \(K_3\square K_3\).

A cycle on \(2n\) vertices has radius and diameter \(n\), proving all metric assertions. \(\square\)

## Verification

The standalone `verification/verify_prism_direct.py` enumerates every size-\(\lceil n/2\rceil\) subset for \(3\le n\le12\), outside the explicitly excluded congruence class, independently tests coverage by bitmask unions of all closed neighborhoods, constructs every possible one-token replacement, and calculates degree distributions, edge counts and connected components. The independent `verification/verify_prism_language.py` builds the complete word families using the forced-gap characterization, tests the original domination condition, and compares **every pair** of states for token differences and host adjacency through \(n=129\). Both outputs are included and both programs can be rerun directly with Python 3 without dependencies. The finite tests corroborate, but do not replace, the infinite-family proof above.

## Relationship to prior work

Suzuki, Mouawad and Nishimura (2014) investigate addition/deletion of tokens through dominating sets of *size at most* a threshold; their adjacency changes the number of selected vertices and differs from fixed-cardinality token sliding/jumping. Bouchou and Blidia (2016) study two-rainbow domination and criticality on cycles. The correspondence between ordinary domination of \(C_n\square K_2\) and two-row labels is relevant context, but their object/claims do not determine these state-transition graphs. Allagan (2026) develops cyclic-word enumeration of *minimum* dominating sets of the same host graph and obtains the background numbers four, \(2n\), and a quadratic enumeration in separate congruence regimes. His principal theorem counts optimal configurations; it does not give the two fixed-cardinality reconfiguration graphs. The proof here reconstructs its own needed state classification, including the parity-dependent colors of the unique adjacent singleton pair, and then analyzes the allowed moves. The 2011 introduction of \(\gamma\)-graphs under sliding by Fricke and collaborators motivates the movement model. A search of the cited full-text sources and relevant bibliographic and research-record searches found no implication supplying the present exact graph isomorphisms. A negative search is not a uniqueness theorem.

## Limitations

The two-defect congruence class \(n\equiv2\pmod4\) is excluded, including the exceptional length six. The statement does not concern nonminimum dominating sets, simultaneous moves, the addition/deletion model, or general prisms \(G\square K_2\). The claimed novelty is qualified by the risk of unindexed earlier work. The result has undergone self-review only, not independent scholarly audit.

## References

1. A. Suzuki, A. E. Mouawad, N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714 (first public version January 22, 2014), https://arxiv.org/abs/1401.5714.
2. A. Bouchou, M. Blidia, *Criticality indices of 2-rainbow domination of paths and cycles*, Opuscula Mathematica 36 (2016), 563–574; first online June 29, 2016, https://doi.org/10.7494/OpMath.2016.36.5.563.
3. J. Allagan, *Exact Dominion of the Prism Graph: Enumeration by Congruence Class via Cyclic Words*, arXiv:2601.03488 (January 7, 2026), https://arxiv.org/abs/2601.03488.
4. G. H. Fricke, S. M. Hedetniemi, S. T. Hedetniemi, K. R. Hutson, *γ-Graphs of Graphs*, Discussiones Mathematicae Graph Theory 31 (2011), 517–531, https://doi.org/10.7151/dmgt.1562.
