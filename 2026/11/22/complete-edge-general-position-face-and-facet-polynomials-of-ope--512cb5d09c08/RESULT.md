# Complete edge-general-position face and facet polynomials of open ladders

## Finding

For every integer \(n\ge2\), let \(L_n=P_n\square K_2\) be the *open ladder* with \(n\) columns, \(2n\) vertices and \(3n-2\) edges. An edge set is *edge-general-position* if no geodesic (shortest path) contains three of its edges. Define \(\Psi_n(z)=\sum_{S}z^{|S|}\), summed over all edge-general-position edge sets, and \(\Phi_n(z)=\sum_{S\text{ inclusion-maximal}}z^{|S|}\). Then
\[
\boxed{\begin{aligned}
\Psi_n(z)={}&(1+z)^n\big(1+2(n-1)z+(n-1)z^2\big)\\
&+2(n-2)z^2\sum_{k=1}^{n-1}(1+z)^k\\
&+\frac{(n-1)(n-2)(n+3)}3z^3+\binom{n-1}{2}z^4,
\end{aligned}}
\]
and
\[
\boxed{\Phi_n(z)=(n-1)z^{n+2}+2(n-2)\sum_{k=3}^{n+1}z^k+2\binom{n-1}{3}z^3+\binom{n-1}{2}z^4.}
\]
The usual empty-sum and zero-binomial conventions apply. In particular, for every \(n\ge3\), **every cardinality from 3 through \(n+2\) occurs among inclusion-maximal configurations**. The complex is nonpure; its minimum facet size remains 3 while the maximum grows with \(n\). At \(n=2\), all 16 subsets are permitted and the unique facet consists of all four edges.

The total number of feasible edge sets is
\[
\boxed{\Psi_n(1)=(5n-6)2^n-4(n-2)+\frac{(n-1)(n-2)(2n+9)}6.}
\]
For instance, the face totals at \(n=2,3,4,5,6,7\) are respectively \(16,73,233,634,1590,3807\). The coefficient of \(z^{n+2}\) is \(n-1\); the previously known maximum size and extremizer classification are **not claimed as new**. The new contribution is the complete size distribution and all inclusion-maximal configurations, including their full spectrum and counts.

## Assumptions and scope

All graphs are finite, simple, undirected and labelled by columns. Use column indices \(0,1,\ldots,n-1\). Let \(h_i^+\) and \(h_i^-\), for \(0\le i\le n-2\), be the upper and lower horizontal edges joining columns \(i\) and \(i+1\), and let \(r_i\), for \(0\le i\le n-1\), be the vertical rung at column \(i\). Every edge set \(S\) determines three index sets
\[
A=\{i:h_i^+\in S\},\quad B=\{i:h_i^-\in S\},\quad R=\{i:r_i\in S\}.
\]
We count labelled edge subsets, not graph-isomorphism classes. Inclusion-maximality refers to single-edge augmentation within the hereditary family, not to maximum cardinality.

## Proof

**1. The exact obstruction table.** Every shortest path in a Cartesian ladder is monotone in its column coordinate and crosses at most one rung. Every monotone path changing rails crosses exactly one rung. A triple of distinct edges lies on a geodesic if and only if it has one of the following shapes:

- Three horizontal edges from the same rail.
- Two horizontal edges from one rail, at positions \(a<c\), and one horizontal edge of the other rail at position \(b<a\) or \(b>c\).
- Two horizontal edges from one rail at positions \(a<c\), and a rung \(r_j\) with \(j\le a\) or \(j>c\).
- One horizontal edge from each rail at distinct positions \(a,b\), and a rung \(r_j\) with \(\min(a,b)<j\le\max(a,b)\).

For each listed pattern, choose endpoints beyond the indicated edges in the appropriate monotone direction to realize a geodesic. Conversely, any geodesic has at most two rail segments, each monotone, and at most one rung; its triple intersections have one of these shapes. In particular, triples containing two rungs cannot obstruct.

This yields an exact, useful structural description. A triple \((A,B,R)\) is permitted precisely when:

(i) \(|A|,|B|\le2\);

(ii) if \(A=\{a,c\}\) with \(a<c\), then \(B\subseteq[a,c]\); if \(B=\{b,d\}\) with \(b<d\), then \(A\subseteq[b,d]\);

(iii) start with every rung index available. If \(A=\{a,c\}\), retain only indices in \(\{a+1,\ldots,c\}\), and apply the same restriction for a two-element \(B\). For each pair \(a\in A,b\in B\), remove rung indices \(\{\min(a,b)+1,\ldots,\max(a,b)\}\). The selected rung set \(R\) can be any subset of the indices remaining.

All interval notation refers to integer column/edge positions. Conditions (i)–(iii) are equivalent to avoiding the four obstruction types, so they characterize *all*, not only largest, legal sets.

**2. Enumerate all faces.** Write \(m=n-1\) and \(x=1+z\). Partition by the numbers of upper and lower selected horizontals:

| \((|A|,|B|)\) | Contribution to \(\Psi_n(z)\) |
|---|---|
| \((0,0)\) | \(x^n\) |
| \((1,0),(0,1)\) | \(2mz x^n\) |
| \((1,1)\), same position | \(mz^2x^n\) |
| \((2,0),(0,2)\) | \(2z^2\sum_{d=1}^{m-1}(m-d)x^d\) |
| \((1,1)\), different positions | \(2z^2\sum_{d=1}^{m-1}(m-d)x^{n-d}\) |
| \((2,1),(1,2)\) | \(2z^3\sum_{d=1}^{m-1}(m-d)(d+1)\) |
| \((2,2)\) | \(\binom m2z^4\) |

Indeed a two-horizontal rail with its opposite rail empty admits exactly the \(d\) intervening rungs; different singleton horizontals a distance \(d\) apart forbid exactly \(d\) rungs; a \((2,1)\) profile requires the singleton position to lie between the two same-rail positions, and then permits no rung; and a \((2,2)\) profile is possible precisely when the two rails select the identical pair of positions, again with no rung. The identities
\[
\sum_{d=1}^{m-1}(m-d)(x^d+x^{m+1-d})=(m-1)\sum_{k=1}^m x^k,
\qquad
\sum_{d=1}^{m-1}(m-d)(d+1)=\frac{m(m-1)(m+4)}6
\]
reduce this partition to the displayed face formula. Setting \(z=1\) and summing the geometric series gives \(\Psi_n(1)\).

**3. Classify every facet.** Because the family is hereditary, an admissible set is maximal exactly when no absent edge can be added. For each fixed permitted \((A,B)\), every allowed rung must therefore be selected. Testing the addition of a horizontal edge using (i)–(iii) leaves exactly four *disjoint* families:

(a) One horizontal edge on each rail, at arbitrary positions \(a,b\), plus every rung not excluded by that pair. If \(a=b\), all \(n\) rungs occur; if the positions differ by \(d\), exactly \(n-d\) rungs occur.

(b) Two horizontal edges on one rail, the opposite rail empty, plus all rungs strictly after the first and at or before the second horizontal position. With separation \(d\), there are \(d\) rungs.

(c) Two horizontal edges at positions \(a<c\) on one rail and a single opposite-rail horizontal edge at a position *strictly* between \(a\) and \(c\), with no rungs. Endpoint opposite-rail positions would allow addition of the other endpoint horizontal, so they are not facets.

(d) Two horizontal edges at the same two positions on both rails, and no rungs.

The completeness is immediate by checking the nine possible horizontal cardinality profiles: profiles with no horizontal on one or both rails and fewer than two on both can be extended; the other four families listed cannot. In (a), available rungs number at least two, so adding a second horizontal edge would violate (iii). In (b), any opposite-rail horizontal would force every rung to be absent. In (c), no more horizontal or rung can be added. In (d), both rails already contain two horizontals and every rung is forbidden.

Their enumerator is initially
\[
\begin{aligned}
\Phi_n(z)={}&mz^{n+2}+2z^2\sum_{d=1}^{m-1}(m-d)z^{n-d}
 +2z^2\sum_{d=1}^{m-1}(m-d)z^d\\
&+2z^3\sum_{d=2}^{m-1}(m-d)(d-1)+\binom m2z^4.
\end{aligned}
\]
Combining the first two sums in separation \(d\) uses \(\sum_{d=1}^{m-1}(m-d)(z^d+z^{m+1-d})=(m-1)\sum_{k=1}^m z^k\), while \(\sum_{d=2}^{m-1}(m-d)(d-1)=\binom m3\). This proves the displayed facet formula. For \(n\ge3\), its coefficients at every size \(3,4,\ldots,n+1\) are positive (at least \(2(n-2)\)), as is its coefficient at \(n+2\); at \(n=2\) the formula reduces to \(z^4\). \(\square\)

## Verification

The standalone `verify_ladder.py` constructs the ladder from its adjacency lists, independently computes breadth-first-search distances from every vertex, recursively enumerates all shortest paths, and constructs the set of forbidden three-edge masks without using the interval classification. It separately constructs the predicted obstruction masks directly from the four patterns and verifies equality. It then exhaustively tests every edge subset and every single-edge augmentation, recovering both cardinality polynomials and comparing them with the formulas and with a third, independent interval-based counter.

For \(n=2,3,4,5,6,7\), the checker tests respectively \(2^4,2^7,2^{10},2^{13},2^{16},2^{19}\) edge subsets. Its total counts are \(16,73,233,634,1590,3807\), and facet counts are \(1,7,20,42,75,121\). It then compares the exact structural counts with the formulas for every \(8\le n\le40\). Execute `python3 verify_ladder.py` from the directory containing this document. The expected terminal message is `VERIFY_OK`. These finite computations complement, but do not replace, the universal combinatorial proof.

## Relationship to prior work

The defining predicate and the edge-general-position number \(\operatorname{gp}_e(P_n\square P_2)=n+2\) were established by Manuel, Prabha and Klavžar (2021 preprint; 2022 journal), who determined numerical extrema for all rectangular grids. A separate public extremizer classification for \(P_L\square K_m\) already establishes that all maximum sets at \(m=2\) consist of every rung plus both horizontal edges across a single cut, with \(n-1\) choices. Thus **neither the optimum size nor the number/shape of maximum ladder sets is asserted as original here**. This theorem instead supplies, for all ladder lengths, every face coefficient, every facet coefficient and the explicit nonpure facet-size spectrum, none of which follows from the maximum-only results without additional classification.

Manuel, Prabha and Klavžar (2022) extended the extremal problem to edge \(k\)-general-position on tori, partial cubes and Benes networks, not to an all-subset ladder enumerator. The open-access 2024 Tian–Klavžar–Tan paper characterizes selected extremal cases and discusses block graphs; an open ladder of at least two squares is not a block graph. The 2026 Hamed-Labbafian–Henning–Tavakoli paper discusses graph products and integer programming, with an accessible abstract emphasizing hierarchical and corona products. Its complete text was not inspected, and is a residual publication-priority uncertainty. Relevant indexed mathematical records for the same ladder predicate include only a maximum-set classification, while other ladder polynomials concern different admissibility predicates. Failure to find the complete face/facet formulas is not a proof of absolute novelty.

## Limitations

The formulas apply to ordinary two-rail open ladders, not cylindrical ladders or wider rectangular grids. All sizes are labelled-edge cardinalities. The result gives exact combinatorial counts and explicit maximal-set patterns but makes no topological homology, algorithmic optimality, or infinite-dimensional claim. The proof is self-contained; tests terminate at finite orders. An independent audit and exhaustive historical publication-priority clearance have not been performed.

## References

1. P. Manuel, R. Prabha, S. Klavžar, *Edge General Position Problem*, arXiv:2105.04292v1, first public 2021-05-10, https://arxiv.org/html/2105.04292 ; journal version *Bulletin of the Malaysian Mathematical Sciences Society* 45 (2022), 2997–3009.
2. P. Manuel, R. Prabha, S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357v1, first public 2022-07-15, https://arxiv.org/abs/2207.07357 .
3. J. Tian, S. Klavžar, E. Tan, *Extremal Edge General Position Sets in Some Graphs*, *Graphs and Combinatorics* 40 (2024), article 40, https://doi.org/10.1007/s00373-024-02770-z .
4. *Extremal edge-general-position sets of clique-path Cartesian graphs*, indexed mathematical record `2026/11/2/SCOPE-extremal-edge-general-position-sets-of-clique-path-cartesian-gra--b63e8d9ec050`, complete `RESULT.md` inspected, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-extremal-edge-general-position-sets-of-clique-path-cartesian-gra--b63e8d9ec050 .
5. Z. Hamed-Labbafian, M. A. Henning, M. Tavakoli, *Edge general position in graphs: Graph products, integer linear programming and some applications*, *Discrete Applied Mathematics* 386 (2026), 1–8, https://doi.org/10.1016/j.dam.2026.01.008 (abstract consulted; full paper not inspected).
