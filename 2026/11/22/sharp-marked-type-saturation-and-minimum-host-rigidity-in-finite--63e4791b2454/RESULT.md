# Sharp marked-type saturation and minimum-host rigidity in finite chain graphs

## Finding

For any finite simple bipartite chain graph \(G=(L\sqcup R,E)\) and a marked set \(A=A_L\sqcup A_R\) with \(|A_L|=a\), \(|A_R|=b\), and \(m=a+b\ge1\), let
\[
\mathcal T_G(A)=\{N_G(v)\cap A:v\in V(G)\}.
\]
Then the sharp one-variable, quantifier-free open-adjacency type capacity is
\[
\boxed{|\mathcal T_G(A)|\le a+b+1.}
\]
For every \((a,b)\) this upper bound is attained. The least number of vertices of an attaining graph is
\[
\boxed{h(a,b)=\max\{2\max(a,b),a+b+1\}.}
\]
If the host must be connected, the least order is
\[
\boxed{h_{\mathrm{conn}}(a,b)=
\begin{cases}
2\max(a,b),&a\ne b,\\
a+b+2,&a=b\ge1.
\end{cases}}
\]
Up to isomorphism preserving \(L\), \(R\), and the two marked subsets as sets (individual marks are not named when counting isomorphism classes), the number of minimum-order attaining hosts is exactly
\[
\boxed{c(a,b)=
\begin{cases}
\binom{\max(a,b)-1}{\min(a,b)},&a\ne b,\\
2,&a=b\ge1.
\end{cases}}
\]
Equality in the trace bound occurs precisely when (i) the left-vertex traces include all \(b\) nonempty levels of a strictly increasing chain of subsets of \(A_R\), (ii) the right-vertex traces include all \(a\) nonempty levels of a strictly increasing chain of subsets of \(A_L\), and (iii) the empty trace occurs. The finite-chain-graph neighborhood family has sharp growth function \(m+1\) and VC dimension one.

## Assumptions and scope

Graphs are finite, simple, undirected and bipartite, with two **distinguished, ordered side names** \(L\) and \(R\). Isolated vertices are allowed except in the connected-host assertion. A chain graph is an induced-\(2K_2\)-free bipartite graph, equivalently a Ferrers graph, equivalently a bipartite graph whose neighborhoods on either side are totally ordered by inclusion. Both marked subset sizes may be zero, but their sum is positive. A trace uses the **open** neighborhood, with no self-adjacency. The counting concerns adjacency atoms only, not the complete quantifier-free logical type including equalities to named parameters. For the class census, side-preserving isomorphisms preserve the two marked subsets setwise and may freely permute vertices within them; this is not a count of individually labelled structures.

## Proof

**Trace and saturation bound.** Every left-vertex trace lies wholly in \(A_R\), and the family of such traces is a chain under inclusion. A strictly nested family of nonempty subsets of a \(b\)-element set contains at most \(b\) members. Dually, the distinct nonempty right-vertex traces (on \(A_L\)) number at most \(a\). Because \(A_L\cap A_R=\varnothing\), no nonempty trace can occur on both sides. There is at most one distinct empty trace. Thus \(|\mathcal T_G(A)|\le b+a+1\), with equality exactly under the three conditions in the finding. When a chain has \(b\) nonempty levels on a \(b\)-point base, its cardinalities are necessarily \(1,2,\dots,b\); a similar statement holds on the other side.

**Host-size lower bound.** In a saturated host, \(b\) distinct nonempty types must be witnessed in \(L\), and \(a\) distinct nonempty types in \(R\). But the marks already force \(|L|\ge a\), \(|R|\ge b\). Consequently each side has at least \(\max(a,b)\) vertices. Independently, \(m+1\) distinct traces require at least \(m+1\) witnessing vertices. This proves \(|V(G)|\ge h(a,b)\).

**Unbalanced construction and exact census.** Suppose \(a>b\). Take \(L=\{\ell_1,\dots,\ell_a\}\), all marked, and \(R=\{r_1,\dots,r_a\}\). Join \(r_j\) exactly to \(\ell_1,\dots,\ell_j\). Mark any \(b\) right vertices \(r_j\) with indices in \(\{1,\dots,a-1\}\). The distinct nonempty right-side traces on \(A_L\) have sizes \(1,\dots,a\), the left-side traces on \(A_R\) have the \(b\) nonempty suffix levels plus an empty level. Every vertex has a neighbor; the construction is connected and has \(2a=h(a,b)\) vertices. Swapping the sides handles \(b>a\), including a zero mark count on one side.

Conversely, in an unbalanced minimum host with \(a>b\), both sides must have exactly \(a\) vertices and all left vertices are marked. The \(a\) right vertices must realize all \(a\) nonempty chain levels on \(A_L\). After side-preserving isomorphism, the bipartite matrix is therefore the unique staircase \(N(r_j)=\{\ell_1,\dots,\ell_j\}\). The \(b\) marked right columns select a subset \(J\subseteq\{1,\dots,a\}\). The \(b\) nonempty left trace levels automatically occur; the empty trace occurs precisely if \(a\notin J\). Thus precisely \(\binom{a-1}{b}\) distinct selections remain. The strictly differing right-column degrees and left-row degrees rule out further identifications. The swapped case is symmetric.

**Balanced construction and exact census.** Suppose \(a=b=k\ge1\). Take the \(k\)-by-\(k\) Ferrers staircase \(r_j\sim\ell_i\) iff \(i\le j\), mark all \(2k\) vertices, and adjoin one isolated unmarked vertex on either side. The marked core realizes \(k\) distinct nonempty traces on each side, while the extra vertex supplies the empty trace. This attains \(2k+1=h(k,k)\). Conversely, a minimum host has exactly one extra vertex, on exactly one side. If it is on \(R\), all \(k\) left vertices are marked and must witness all \(k\) nonempty left profiles. These form levels of sizes \(1,\dots,k\), including the full marked right side; hence each marked right vertex has a nonempty trace. The extra right vertex must then witness the empty trace and is isolated because every left vertex is marked. The marked right vertices must themselves realize all \(k\) nonempty right-side chain levels. This uniquely forces the \(k\)-by-\(k\) staircase. The extra vertex may lie on either named side, giving exactly two isomorphism classes.

**Connected balanced cutoff.** An attaining host of \(2k+1\) vertices has an isolated extra vertex, so cannot be connected. Add instead one extra left vertex adjacent to all marked right vertices and one extra right vertex adjacent solely to that extra left vertex, keeping the marked \(k\)-by-\(k\) staircase. Its neighborhoods are still nested on both sides, it is connected, and it realizes the \(2k\) nonempty profiles and the empty profile (from the extra right vertex). It has \(2k+2\) vertices and is minimal connected. For unbalanced marks the previous staircase construction is already connected.

**Learning dimensions.** The formula \(m+1\) is the exact supremal shatter function in this graph class, attained for all positive \(m\). A one-point marked set is shattered by the nonempty and empty traces. No two-point marked set can be shattered, since at most three patterns occur instead of four. Thus VC dimension is exactly one.

## Verification

The standalone file `check_chain_traces.py` enumerates every binary bipartite adjacency matrix whose total number of vertices is at most seven, retains precisely those with nested neighborhoods, and tests **every** choice of nonempty marked left and right subsets. It checks the trace bound, minimum host order, all side-preserving unlabelled minimum-host class counts when witnesses occur in the enumerated range, and the connected-host minimum bound and small witnesses. It examines 3,932 side-labelled chain-graph matrices and 444,104 marked configurations. The program additionally constructs and verifies the sharp unrestricted and connected witnesses for all \(0\le a,b\le40\) with positive sum: 1,680 parameter pairs. It reports `ALL_CHECKS_OK`. These finite checks corroborate but do not replace the all-size proof above.

Reproduction: with Python 3 and no third-party packages, run `python3 check_chain_traces.py` in the directory containing the file.

## Relationship to prior work

The Ferrers/chain normal form is classical and is stated in London (2026), which studies **edge partitions into Ferrers graphs**, not the saturation of marked adjacency types. Berthe–Foucaud–Lehtilä–Parreau (2026) establishes sharp **closed**-neighborhood complexity bounds under treewidth/pathwidth restrictions and motivates determination of exact constants; those graph-width restrictions do not subsume unrestricted chain graphs. Bonnet–Foucaud–Lehtilä–Parreau (2023) proves a general bounded-twin-width open-neighborhood complexity inequality, but not the present side-sensitive minimum-host and marked-isomorphism census. The linear \(m+1\) upper bound alone follows readily from nesting (and is consistent with the standard VC-dimension-one Sauer bound); the distinctive claims here are the **sharp split-sensitive least host orders, balancing penalty, exhaustive characterization and exact binomial census of smallest saturating hosts**.

## Limitations

The result applies to finite bipartite induced-\(2K_2\)-free graphs with the two sides distinguished; it does not assert the same exact formulas for arbitrary bipartite or general cographs. The host census is unlabelled with marked sets preserved setwise; individually named marks have different counts. The connected-host result determines minimum order but does not enumerate all connected minimum-size isomorphism classes. The source comparison does not establish absolute priority against all older unindexed Ferrers-matrix literature. Finite checks are limited to the specified orders and do not constitute an independent audit.

## References

1. András London, *Edge partitions into induced-\(2K_2\)-free bipartite graphs*, arXiv:2603.00593, first posted 2026-02-28. https://arxiv.org/abs/2603.00593
2. Gaétan Berthe, Florent Foucaud, Tuomo Lehtilä, and Aline Parreau, *Neighbourhood complexity and identification problems for graphs of bounded treewidth and pathwidth*, arXiv:2607.16889v1, first posted 2026-07-18. https://arxiv.org/html/2607.16889v1
3. Édouard Bonnet, Florent Foucaud, Tuomo Lehtilä, and Aline Parreau, *Neighbourhood complexity of graphs of bounded twin-width*, arXiv:2301.04217v2, originally posted 2023-01-10. https://arxiv.org/html/2301.04217v2
