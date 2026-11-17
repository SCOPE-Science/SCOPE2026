# Dom-forcing and zero-forcing polynomials after matching deletion in complete bipartite graphs

## Finding

**Theorem.** Fix integers \(a,b\ge4\) and \(0\le t\le\min\{a,b\}\). Let \(G_{a,b,t}=K_{a,b}-M_t\), where \(M_t\) is any matching of \(t\) edges. Put \(N=a+b\) and define
\[
A_2=\binom a2-\binom{a-t}2,\qquad B_2=\binom b2-\binom{b-t}2,
\]
\[
C=A_2B_2-t(a-t)(b-t)-\binom t2.
\]
Every zero forcing set of \(G_{a,b,t}\) is a dominating set. Hence its zero-forcing polynomial and dom-forcing polynomial coincide, and their common value is
\[
\boxed{\mathcal Z(G_{a,b,t};z)=\mathcal F_d(G_{a,b,t};z)=z^N+Nz^{N-1}+(ab+A_2+B_2)z^{N-2}+(aB_2+bA_2)z^{N-3}+Cz^{N-4}.}
\]
In particular, both minimum parameters are
\[
\boxed{Z(G_{a,b,t})=F_d(G_{a,b,t})=\begin{cases}N-2,&t=0,\\N-3,&t=1,\\N-4,&2\le t\le\min\{a,b\}.\end{cases}}
\]
The numbers of labelled minimum sets are \(ab\) if \(t=0\), \(a(b-1)+b(a-1)\) if \(t=1\), and \(C\) if \(t\ge2\).

## Assumptions and scope

All graphs are finite, simple and undirected. A set \(S\subseteq V(G)\) is **zero forcing** if, starting with \(S\) black and its complement white, iteratively recoloring the unique white neighbor of any black vertex can make all vertices black. It is **dominating** if each vertex outside \(S\) has at least one neighbor in \(S\), and **dom-forcing** if it is both dominating and zero forcing. The polynomials \(\mathcal Z\) and \(\mathcal F_d\) count these respective sets by their cardinalities. The minimum size of a zero forcing (respectively dom-forcing) set is \(Z\) (respectively \(F_d\)).

Write the two parts as \(A=\{a_1,\ldots,a_a\}\) and \(B=\{b_1,\ldots,b_b\}\), with precisely the edges \(a_ib_i\) for \(1\le i\le t\) deleted. The theorem includes the undeleted case \(t=0\) for comparison; the matching-deleted cases \(t\ge1\) supply the new formula. No assertion is made for part sizes below four.

## Proof

**Step 1 (the complete forcing criterion).** For a proposed initial black set \(S\), let \(U=A\setminus S\) and \(V=B\setminus S\) be its initially white vertices. Put \(q=|U|\) and \(p=|V|\). Let \(I=\{i\le t:a_i\in U\}\) and \(J=\{j\le t:b_j\in V\}\). We claim that \(S\) is zero forcing **if and only if** precisely one of the following four conditions holds:

1. \(p\le1\) and \(q\le1\).
2. \(p=2\), \(q\le1\), and \(J\ne\varnothing\).
3. \(q=2\), \(p\le1\), and \(I\ne\varnothing\).
4. \(p=q=2\), \(I\ne\varnothing\), \(J\ne\varnothing\), and \(I\ne J\).

First, no set leaving at least three white vertices in one part can force them all. Indeed, as long as \(q\ge3\), each black vertex in \(B\) has at least \(q-1\ge2\) white neighbors in \(A\), since it misses at most one edge to \(A\). Thus no black \(B\)-vertex can perform the **first** force into \(A\), even if all white vertices of \(B\) have already been removed. The number \(q\) therefore cannot decrease. The same argument applies to \(p\ge3\).

If \(p,q\le1\), each white vertex has a black neighbor across the bipartition that sees it as its unique white neighbor (there are at least three black vertices on the opposite side, and at most one missing adjacency), so all whites force. If \(p=2\) and \(q\le1\), first force the possible one white vertex of \(A\) using a black vertex in \(B\); this exists because \(b\ge4\) and only one cross-edge can be missing. Thereafter \(q=0\). A black \(A\)-vertex sees exactly one of the two white \(B\)-vertices precisely when its missing matched neighbor is in \(V\), namely when \(J\ne\varnothing\); it then forces the other white \(B\)-vertex, and the last white vertex is forced by an ordinary adjacent black vertex. If \(J=\varnothing\), no force into \(B\) is ever possible while \(p=2\), even after the possible white \(A\)-vertex becomes black. This proves condition 2 and, symmetrically, condition 3.

Finally suppose \(p=q=2\). A black \(A\)-vertex can perform a force into \(B\) exactly when its deleted matched edge ends in \(V\), but its own endpoint is not in \(U\). Equivalently, \(J\setminus I\ne\varnothing\). Likewise a black \(B\)-vertex can force into \(A\) exactly when \(I\setminus J\ne\varnothing\). If \(I=J\), no initial force exists. If \(I\) or \(J\) is empty, the corresponding two-white side cannot be reduced, as already shown. If both are nonempty and different, there is a first force in at least one direction. For instance, if \(j\in J\setminus I\), then black \(a_j\) forces the other white vertex of \(B\), reducing \(p\) to one. Since \(I\ne\varnothing\), condition 3 then ensures completion (the symmetrical case uses condition 2). Thus the four conditions are necessary and sufficient.

**Step 2 (domination).** By Step 1 a zero forcing set leaves at most two white vertices in either part. Any white vertex in \(A\) therefore has at least \(b-2\) black candidates in \(B\), of which at most one can be its missing matched neighbor. This leaves at least \(b-3\ge1\) black neighbors. Symmetrically each white vertex in \(B\) has at least \(a-3\ge1\) black neighbors. Hence every zero forcing set is dominating, establishing equality of the two polynomials and minimum parameters.

**Step 3 (enumeration).** The number of unordered two-vertex choices from \(A\) containing at least one matched endpoint is
\(A_2=\binom a2-\binom{a-t}2\); the analogous number from \(B\) is \(B_2\). For white-set sizes \(p+q=0,1,2,3\), the forcing criterion yields respectively \(1\), \(a+b\), \(ab+A_2+B_2\), and \(aB_2+bA_2\) possibilities.

When \(p=q=2\), there are \(A_2B_2\) pairs \((U,V)\) with nonempty \(I,J\). Those with \(I=J\ne\varnothing\) have either (i) the same one matched index, allowing \(t(a-t)(b-t)\) choices of their unmatched second elements, or (ii) the same two matched indices, allowing \(\binom t2\) choices. These disjoint forbidden cases leave exactly \(C\) possibilities. No other initial white-set sizes can force. Complementation changes white-set size \(h\) to black-set size \(N-h\), proving the displayed polynomial.

For \(t=0\), \(A_2=B_2=C=0\). For \(t=1\), \(A_2=a-1\), \(B_2=b-1\), and \(C=0\), so the first additional coefficient occurs at degree \(N-3\). For \(t\ge2\) the coefficient \(C\) is positive: for \(t=2\) choose a white pair in each part consisting of different matched indices plus one unmatched vertex, available since \(a,b\ge4\); for \(t\ge3\) choose two different two-element subsets of three matched indices. Thus degree \(N-4\) is present exactly when \(t\ge2\), completing the minimum-size and minimum-set-count claims. \(\square\)

## Verification

Run `python3 verify.py` with Python 3.9 or newer. The standalone program independently enumerates every vertex subset, applies the exact color-change rule using graph adjacency bitmasks, tests domination separately, and compares the complete size-distribution with the symbolic formula. It tests every \((a,b,t)\) with \(4\le a,b\le6\) and \(0\le t\le\min\{a,b\}\), a total of \(50\) graph profiles. The terminal message is `VERIFY_OK`. The machine check is finite corroboration: the all-parameter theorem is established by the proof above.

For illustration, when \(a=b=4\), the minimum sizes as \(t=0,1,2,3,4\) are \(6,5,4,4,4\), with respectively \(16,24,16,30,30\) minimum sets. There is a genuine small-part boundary: in \(K_{3,4}\) with \(a_1b_1,a_2b_2\) deleted, the black set complementary to \(\{a_2,a_3,b_1,b_3\}\) is zero forcing but not dominating (white \(b_1\) has no initially black neighbor). Thus the domination implication cannot simply be extended to \(a=3\).

## Relationship to prior work

Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, and Reinhart (2018) introduced the zero-forcing polynomial and explicitly determined the complete-multipartite polynomial when every part has size at least two (their Proposition 4); this covers \(t=0\) and is **not** claimed new. Susanth, Dominic, and Premodkumar (2024) studied dom-forcing sets and established the scalar value for undeleted complete bipartite graphs. Jiang and Wan (2026, Proposition 5.3) likewise treat undeleted complete bipartite graphs; their Proposition 5.6 supplies the general numerical equivalence \(F_d=Z\) whenever a minimum zero forcing set dominates. These results do not imply that **every** zero forcing set of a matching-deleted biclique dominates, or give the matching-deleted polynomial and its \(t=1,2\) transitions. The present statement supplies those structural and enumerative facts.

Related mathematical records treat all forcing sets on complete multipartite graphs, or matching-deleted bicliques under other invariants (CIS pairs and geodesic subpaths). Neither statement implies an enumeration of the zero forcing process for \(t\ge1\). This source comparison does not certify historical priority: additional unindexed or inaccessible work may exist.

## Limitations

The proof assumes both part sizes at least four and removal of a **matching** only. It does not describe arbitrary patterns of removed edges, small-part exceptional polynomials, or connected variants of zero forcing. Independent mathematical audit and exhaustive literature coverage are not claimed. The code tests only finite instances and is not a computer-certified proof for all parameter triples.

## References

1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910 (first version 2018-01-26), Proposition 4. https://arxiv.org/abs/1801.08910
2. P. Susanth, C. Dominic, K. P. Premodkumar, *Dom-forcing sets in graphs*, arXiv:2411.00580 (first version 2024-11-01). https://arxiv.org/abs/2411.00580
3. H. Jiang and H. Wan, *Forcing and domination in graphs*, AIMS Mathematics **11** (2026), 19772–19783; published 2026-07-07, doi:10.3934/math.2026802. https://www.aimspress.com/article/doi/10.3934/math.2026802
