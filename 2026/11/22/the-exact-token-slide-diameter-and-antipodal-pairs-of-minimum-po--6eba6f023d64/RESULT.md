# The exact token-slide diameter and antipodal pairs of minimum power domination on square rook graphs

## Finding
For every integer \(n\ge3\), let \(G_n=K_n\square K_n\), with vertices the \(n^2\) cells of an \(n\)-by-\(n\) square board. Let \(R_n\) be the graph whose vertices are *minimum power-dominating sets* of \(G_n\), with two sets adjacent if one occupied cell can be moved along an edge of \(G_n\) to an unoccupied cell while the new set remains minimum power dominating. Thus a move changes either the row or the column, but not both, of one token.

**Theorem.** The graph \(R_n\) is connected, and
\[
\boxed{\begin{aligned}
|V(R_n)|&=2n^n-n^2(n-1)!,\\
|E(R_n)|&=n(n-1)\bigl(n^n-n!\bigr),\\
\operatorname{diam}(R_n)&=2n-2.
\end{aligned}}
\]
There are exactly \(n^2\) unordered pairs at distance \(2n-2\). For each row \(r\) and column \(c\), one such pair is
\[
\boxed{\left\{\,\{(i,c):i\ne r\},\quad\{(r,j):j\ne c\}\,\right\},}
\]
and **these are all** the diameter pairs. In particular, every one-column placement missing one row has a unique farthest placement, namely the complementary one-row placement, and no other placement pair attains the diameter.

The minimum power-domination number \(n-1\), the characterization of all feasible placements, and the count of minimum placements are established prior results. The contribution here is the optimality-preserving **adjacent-slide graph**, its exact edge count and sharp metric with a complete extremal-pair classification.

## Assumptions and scope
All graphs are finite, undirected, simple, and labeled by the indicated board coordinates. Two cells of \(G_n\) are adjacent precisely when they share a row or a column and are distinct. A selected set \(S\) power dominates if, after observing its closed neighborhood, repeatedly letting any observed cell with exactly one unobserved neighbor force that neighbor eventually observes the whole board. Parallel and sequential forcing give the same closure. Each reconfiguration vertex is an unordered subset of exactly \(n-1\) distinct cells; a slide replaces exactly one selected cell by an adjacent, previously unselected cell and must preserve power domination. The theorem holds for every integer \(n\ge3\); it makes no assertion about a two-by-two board or arbitrary rectangular boards.

Let \(\mathcal R\) be all sets with exactly one selected cell in each of \(n-1\) rows, and let \(\mathcal C\) be the transposed family with exactly one selected cell in each of \(n-1\) columns. Their overlap \(\mathcal B=\mathcal R\cap\mathcal C\) is the family of partial permutation matrices of size \(n-1\).

## Proof
**1. Reconstruct the monitoring criterion and the optimum states.** Given any selection \(S\), denote the empty rows by \(U\) and the empty columns by \(W\). After the initial closed-neighborhood observation the *only* unobserved cells are \(U\times W\). If both \(|U|\) and \(|W|\) are at least two, each observed cell has zero or at least two unobserved neighbors, so no force can start. Conversely, if \(|U|=1\), each unobserved cell in its sole empty row can be forced by the observed cell directly above it in any occupied row; the empty-column-one case is symmetric, and an empty complement needs no forcing. Thus
\[
S\text{ power dominates }G_n\ \Longleftrightarrow\ |U|\le1\text{ or }|W|\le1.
\]
Consequently no set with fewer than \(n-1\) cells works, while every set in \(\mathcal R\cup\mathcal C\) works. Every minimum set lies in that union. Choose the missing row and a column independently for each occupied row to obtain \(|\mathcal R|=n\,n^{n-1}=n^n\); likewise \(|\mathcal C|=n^n\). A set in both families has a missing row, a missing column, and a bijection between their \(n-1\) remaining indices, so \(|\mathcal B|=n^2(n-1)!\). Inclusion-exclusion gives the stated vertex count. This derivation is included to verify the previously known premise independently, not to claim it as new.

**2. Count all legal slides without double counting.** Within \(\mathcal R\), every placement permits \((n-1)^2\) moves changing the column of a token within its currently occupied row, and another \(n-1\) moves carrying one token within its column to the unique empty row. Every move preserves the \(n-1\) occupied rows. Hence the graph induced on \(\mathcal R\) is \(n(n-1)\)-regular; the same holds for \(\mathcal C\).

Inside \(\mathcal B\), each selected token can move within its row to the unique currently empty column or within its column to the unique currently empty row. These are exactly the slides that keep both coordinate sets of cardinality \(n-1\), so the graph induced on \(\mathcal B\) is \(2(n-1)\)-regular.

There is no slide from \(\mathcal R\setminus\mathcal B\) directly to \(\mathcal C\setminus\mathcal B\). A within-row move retains all occupied rows and therefore remains in \(\mathcal R\); a within-column move retains the set of occupied columns, which initially has fewer than \(n-1\), so its endpoint cannot belong to \(\mathcal C\). All slides are therefore in the two induced families. Subtracting the duplicated edges internal to \(\mathcal B\) gives
\[
\begin{aligned}
|E(R_n)|
&=2\cdot\frac{n^n n(n-1)}2
 -\frac{n^2(n-1)!\cdot2(n-1)}2\\
&=n(n-1)(n^n-n!).
\end{aligned}
\]

**3. Construct universal short routes.** Put \(k=n-1\). If both configurations belong to \(\mathcal R\), either they have the same missing row, in which case at most \(k\) within-row slides align all their columns, or their missing rows differ. In the latter case, move the token currently in the *target's missing row* to the *source's missing row* without changing its column, then align at most \(k\) columns. All intermediate configurations belong to \(\mathcal R\). Thus their distance is at most \(k+1<2k\). The argument transposes to two configurations in \(\mathcal C\).

For \(S\in\mathcal R\), \(T\in\mathcal C\), arbitrarily biject the \(k\) source tokens (each on a different row) with the \(k\) target columns (each distinct). First move each source token within its row to its assigned target column, requiring at most \(k\) slides and remaining in \(\mathcal R\). These new positions lie in \(\mathcal B\). Then move each token along its now unique column to the corresponding target row, requiring at most \(k\) slides and remaining in \(\mathcal C\). Thus \(d_{R_n}(S,T)\le2k\). These routes prove connectivity and the diameter upper bound.

Moreover, if some cell of \(S\) and some cell of \(T\) share a column, choose the bijection to pair them. The corresponding token needs no column move, so the path uses at most \(2k-1\) slides. If some source and target cells share a row, pair those two instead: that token needs no row move, again saving at least one slide.

**4. Identify and attain every diameter pair.** Suppose two states have distance \(2k\). By the preceding paragraph they cannot both be in \(\mathcal R\) or both in \(\mathcal C\). After interchanging their order if necessary, take \(S\in\mathcal R\), \(T\in\mathcal C\). No source cell can share a row *or a column* with any target cell, since such an overlap provides a route of at most \(2k-1\) slides. As \(S\) occupies every row except one, say \(r\), every cell of \(T\) must lie in row \(r\). Because \(T\) occupies \(k\) columns, it has one cell in every column except one, say \(c\). No cell of \(S\) may lie in a column of \(T\), so every cell of \(S\) lies in column \(c\). The configurations must therefore have the asserted form.

Conversely, take this pair for any \(r,c\). The \(k\) source tokens all begin outside row \(r\) and in column \(c\), whereas the \(k\) final positions all lie in row \(r\) and outside column \(c\). Follow tokens across any legal sequence. Each token must change its row at least once and its column at least once, and one slide changes only one coordinate of one token. Every sequence therefore needs at least \(2k\) slides. Step 3 gives a sequence of exactly \(2k\), proving the sharp lower bound. The choices of \(r,c\) produce \(n^2\) distinct unordered pairs. No other pairs can be extremal by the previous argument.

## Verification
Two independently written standalone standard-library Python programs accompany this theorem.

Run `python3 verify_direct.py` to build the board graph from adjacency, enumerate all subsets up to the first feasible cardinality for \(n=3,4,5\), run actual closed-neighborhood and zero-forcing propagation on every candidate, build all optimal slide edges, and compare the counts to the theorem. This code performs complete all-pairs breadth-first searches for \(n=3,4\), and checks 45 selected sources (including the claimed extremal family) at \(n=5\).

Run `python3 verify_structural.py` to generate the two optimum families independently as integer-bitmask representations, construct all local slides by bit operations, and count edges. It runs complete all-pairs distance searches for \(n=3,4\) and breadth-first searches from all 25 column-star sources at \(n=5\). The two scripts agree on the numerical triples \((|V|,|E|,\operatorname{diam})\): \((36,126,4)\), \((416,2784,6)\), and \((5650,60100,8)\), with respectively 9, 16 and 25 extremal pairs in the searched domains. These finite checks corroborate, but do not replace, the proof for all \(n\).

## Relationship to prior work
Power domination of Cartesian products of complete graphs, including their minimum number, was studied by Soh and Koh (2014). The exact row-or-column feasibility criterion and complete minimum-set enumeration were established in *Complete power-domination-set classification and polynomial of rectangular rook graphs* (2026) and also in *Complete ordinary and connected power-domination enumerators of rook graphs* (2026). The proof above reconstructs their shared premise but does not assert it as original.

Bjorkman and collaborators, *Power domination reconfiguration* (arXiv:2201.01798, first public 2022-01-05), define the token-sliding and token-jumping models and develop general power-domination reconfiguration. Their accessible text addresses the general TAR and TJ frameworks, not this family-specific sliding diameter or complete set of antipodal pairs. The 2026 finding *Exact reconfiguration components of power-dominating sets in rook graphs* studies **bounded token-addition/removal** components; that different state space and move rule do not determine the present fixed-cardinality adjacent-slide distances. Searches for rook-graph, complete-bipartite line-graph, and row/column sensor-slide formulations did not identify a stronger published result implying the displayed formulas. This is a best-knowledge comparison, not proof of global priority.

## Limitations
The exact claims are for square boards and fixed-cardinality, one-edge, single-token slides. The result does not determine every pairwise shortest-path distance, shortest-path multiplicities, or the corresponding unrestricted token-jumping metric. The verification programs fully cover all sources only at orders three and four; the all-order statements rest on the proof, not on finite enumeration. Unindexed or inaccessible equivalent literature remains a priority risk. No independent mathematical validation is represented by these computations.

## References
1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798v1 (2022-01-05), https://arxiv.org/html/2201.01798v1.
2. F. Soh, K. M. Koh, *A note on Power Domination Problem in Diameter Two Graphs*, AKCE Int. J. Graphs Comb. **11** (2014), 51–55, https://doi.org/10.1080/09728600.2014.12088762.
3. *Complete power-domination-set classification and polynomial of rectangular rook graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-complete-power-domination-set-classification-and-polynomial-of-r--48ce98e1f82f.
4. *Complete ordinary and connected power-domination enumerators of rook graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-ordinary-and-connected-power-domination-enumerators-of--e4946fa80078.
5. *Exact reconfiguration components of power-dominating sets in rook graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-reconfiguration-components-of-power-dominating-sets-in-roo--99dbf6bd21a3.
