# Repeated disconnection windows in dominating-set reconfiguration of two-token stars

## Finding

Let \(G_n=F_2(K_{1,n})\) be the two-token graph of the star with \(n\ge 2\) leaves. For each integer budget \(k\ge0\), form the token-addition/removal graph \(\mathcal T_n(k)\): its vertices are all ordinary dominating sets \(D\subseteq V(G_n)\) with \(|D|\le k\); two states are adjacent precisely when one is obtained from the other by adding or deleting a single vertex. Write \(c_n(k)\) for its number of connected components, with the empty graph having zero components, and put \(b_r=n-r+\binom r2\).

**Theorem.** For every integer \(n\ge 2\) and budget \(k\ge0\),

\[
c_n(k)=\begin{cases}
0,&0\le k<n-1,\\
\binom n2,&k=n-1,\\
1+\binom n2+\binom n3,&k=n,\\
1+\displaystyle\sum_{r=4}^n\binom nr\,\mathbf1_{\{k=b_r\}},&k\ge n+1.
\end{cases}
\]

In the last line, the component not counted by the sum contains every dominating set with a deletion path to a minimum-by-inclusion set of size strictly below \(k\). All other components are isolated single vertices, corresponding to minimal dominating sets of cardinality exactly \(k\).

For every \(n\ge4\), the sequence of budgets exhibits a sharp **repeated loss and recovery of connectivity**: the graph first becomes connected at \(k=n+1\), is disconnected at exactly the \(n-3\) distinct budgets
\[
b_4=n+2,\ b_5=n+5,\ \ldots,\ b_n=\binom n2,
\]
and is connected at every budget \(k\ge\binom n2+1\). At the exceptional budget \(k=b_r\), there are exactly \(\binom nr\) isolated dominating sets in addition to the connected core. The first connectivity and permanent connectivity budgets therefore have different orders of growth: linear and quadratic, respectively.

## Assumptions and scope

All graphs are finite, simple, undirected and labelled. The star has \(n\) leaves and one centre; the token graph has vertices consisting of unordered pairs of distinct star vertices and adjacencies obtained by moving one token along one star edge. Equivalently \(G_n\) is the once-subdivided \(K_n\). Denote its original vertices by \(u_i\), and its subdivision vertices by \(e_{ij}\) for \(1\le i<j\le n\). Then \(e_{ij}\) is adjacent exactly to \(u_i\) and \(u_j\). Domination includes a selected vertex dominating itself. The reconfiguration move is add/delete (TAR), **not** a token jump, token slide or simultaneous exchange. We count components even at budgets exceeding the number of vertices; no artificial cap is assumed.

## Proof

**1. A complete dominating-set criterion.** For any vertex selection \(D\), let \(A=\{i:u_i\in D\}\), \(R=[n]\setminus A\), and \(B=\{ij:e_{ij}\in D\}\). Put \(r=|R|\). A subdivision vertex \(e_{ij}\) is undominated precisely when \(ij\notin B\) and \(i,j\in R\). Thus, when \(r\ge2\), all edges within \(R\) must be in \(B\). These mandatory selected subdivision vertices also dominate all omitted original vertices. When \(r=1\), the one omitted original vertex requires a selected incident subdivision vertex; when \(r=0\), there is no additional condition. We obtain the exact alternatives: (i) \(r=0\), arbitrary \(B\); (ii) \(r=1\), \(B\) contains an edge incident with the unique element of \(R\); (iii) \(r\ge2\), \(\binom R2\subseteq B\).

**2. All inclusion-minimal dominating sets.** Define \(U=\{u_1,\ldots,u_n\}\). For \(R\subseteq[n]\) with \(|R|=r\ge2\), define
\[
D_R=\{u_i:i\notin R\}\cup\{e_{ij}:i,j\in R,\ i<j\}.
\]
Each is dominating by (iii), of size \(b_r=n-r+\binom r2\). Every included subdivision vertex is essential to dominate itself when both endpoints are omitted; every included original \(u_i\) is essential to dominate any \(e_{ij}\) with \(j\in R\), which would be left undominated after deleting \(u_i\). The set \(U\) is minimal since deleting any \(u_i\) leaves it undominated. Conversely, with \(r\ge2\), any extra selected subdivision vertex is removable, so inclusion minimality forces precisely \(D_R\); with \(r=0\), all subdivision vertices are removable, leaving \(U\). With \(r=1\), select an incident edge \(e_{ij}\in D\), where \(i\in R\) and \(j\in A\). Deleting \(u_j\) preserves the criterion for the new omitted pair \(\{i,j\}\), so such a selection is never minimal. This proves the list exhaustively. Since \(b_2=n-1\), \(b_3=n\), and \(b_{r+1}-b_r=r-1>0\) for \(r\ge2\), the domination number is \(n-1\) and exactly \(\binom n2\) sets attain it. The numerical minimum and its standard construction are known previously; they are used here rather than claimed as new.

**3. At budgets at most \(n\).** No state exists below \(n-1\). At \(k=n-1\), all \(\binom n2\) optimum states \(D_R\), \(|R|=2\), are minimal and cannot be connected by additions, hence are isolated. At \(k=n\), the additional minimal states are \(U\) and \(D_R\) with \(|R|=3\); each is isolated by minimality at the budget ceiling. Every nonminimal state of size \(n\) has a deletion to a minimum state of size \(n-1\). Different minimum states cannot be in the same component: any path between two distinct size-\(n-1\) minima would require a size-\(n\) dominating set containing both, but the union of any two distinct such \(D_R\) has size at least \(n+1\). Consequently the component count is \(1+\binom n2+\binom n3\).

**4. The connected core for \(k\ge n+1\).** Every nonminimal dominating set can be reduced through successive deletions to one of the listed minimal sets. A minimal set with size \(k\) has neither a permissible deletion nor an addition within budget and is isolated. Every minimum set \(D_{\{i,j\}}\) connects to \(U\) within budget \(n+1\): add \(u_i\), then \(u_j\), and remove \(e_{ij}\). For \(r\ge3\), from \(D_R\) add any \(u_i\) with \(i\in R\) and then delete the \(r-1\) selected subdivision vertices incident with \(i\). All intermediate sets dominate: the surviving omitted set \(R\setminus\{i\}\) still has at least two elements and all its internal edges remain selected. The path ends at \(D_{R\setminus\{i\}}\), and its maximum size is \(b_r+1\). Therefore, whenever \(b_r<k\), this minimal state connects by decreasing \(r\) to a minimum state, then to \(U\), all within budget \(k\). Thus every nonisolated state belongs to a unique connected core. Its other components correspond exactly to minimal states of size \(k\).

For \(k\ge n+1\), the only possible minimal state sizes equal to \(k\) are \(b_r\) for \(4\le r\le n\); each occurs at exactly one \(r\) and is attained by \(\binom nr\) labelled choices of \(R\). Hence the fourth formula, and the claimed disconnection/recovery and permanent-connectivity thresholds. All small endpoints \(n=2,3\) are included in the formula, with the last sum empty. \(\square\)

## Verification

The included `verify.py` builds \(G_n\) directly from its adjacency list and enumerates every vertex subset for \(n=2,3,4,5\); it tests ordinary domination by closed neighbourhoods, checks the independent all-size selection criterion numerically, constructs every budget-restricted TAR graph and counts components by graph traversal. Execute `python3 verify.py` using Python 3. The test result was `VERIFY_OK`, after inspecting \(8\), \(64\), \(1024\), and \(32768\) vertex selections respectively, with \(5\), \(39\), \(513\), and \(12305\) dominating configurations. This finite enumeration is a check, **not** a proof for unbounded \(n\); the unrestricted result follows from the preceding exact classification and paths.

## Relationship to prior work

Fabila-Monroy and Gómez-Galicia (2025, Theorem 3.1) proved \(\gamma(F_2(K_{1,n}))=n-1\) and exhibited the optimum \(D_{\{i,j\}}\). Acosta Troncoso, Hernández-Cruz and Trujillo-Negrete (2026) identify two-token stars with complete-graph subdivisions and study other token-graph parameters. Benítez-Bobadilla and collaborators (2026) study domination numbers for different host families. General dominating-set reconfiguration methods and their complexity are known. The new statement here is **the complete budget-by-budget connected-component formula and its repeated nonmonotone connectivity windows**, not the minimum domination number, the optimum constructions, or the previously obtained all-size domination reliability enumeration. Results on *connected domination* of subdivided cliques or TAR domination of different graph families do not imply this particular component census directly.

## Limitations

The theorem concerns ordinary domination on two-token stars only, and single-vertex addition/deletion with a hard cardinality budget. It does not extend automatically to \(F_k(K_{1,n})\) for \(k\ge3\), to connected domination, or to token-jumping/sliding reconfiguration. Prior-art comparisons are based on accessible sources and mathematical-record searches; independent human priority verification remains outstanding. The computational checks cover only \(n\le5\).

## References

1. E. Acosta Troncoso, C. Hernández-Cruz, A. Trujillo-Negrete, *Token graphs of stars*, arXiv:2611.11191 (first public 2026-11-08), https://arxiv.org/abs/2611.11191 .
2. R. Fabila-Monroy, S. G. Gómez-Galicia, *Domination number of Token Graphs*, arXiv:2509.16448 (first public 2025-09-19), https://arxiv.org/abs/2509.16448 .
3. G. Benítez-Bobadilla, F. E. Contreras-Mendoza, S. G. Gómez-Galicia, A. Trujillo-Negrete, *Domination in token graphs of graphs with domination number two*, arXiv:2611.15124 (first public 2026-11-11), https://arxiv.org/abs/2611.15124 .
4. A. Blanché, H. Mizuta, P. Ouvrard, A. Suzuki, *Decremental Optimization of Dominating Sets Under the Reconfiguration Framework*, IWOCA 2020, https://arxiv.org/abs/1906.05163 .
