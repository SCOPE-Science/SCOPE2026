# Sharp token-slide connectivity thresholds for minimum total domination in complete-graph direct products

## Finding

Let \(G_{m,n}=K_m\times K_n\) be the **categorical (tensor, direct) product**, not the Cartesian product, with \(m,n\ge 3\). Write a vertex as \((r,c)\); distinct vertices are adjacent if and only if both their row indices and their column indices differ. A total dominating set \(S\) meets the open neighborhood of every vertex. A minimum total dominating set has the least possible cardinality. Define \(\mathcal T_{m,n}\) by taking every minimum total dominating set as a vertex and joining two sets if one selected vertex slides along an edge of \(G_{m,n}\) to an unselected vertex, while preserving minimum total domination. Define \(\mathcal J_{m,n}\) similarly, but permit an unrestricted one-vertex replacement (token jumping).

**Theorem.** For all integers \(m,n\ge3\), the minimum total domination number of \(G_{m,n}\) is \(3\). Its minimum total dominating sets are exactly the sets of three cells with pairwise different rows and pairwise different columns. Put \(N_{m,n}=6\binom m3\binom n3\). Both reconfiguration graphs have \(N_{m,n}\) vertices, and \(\mathcal T_{m,n}\) is regular of degree \(3(m-3)(n-3)\), hence has exactly \(3N_{m,n}(m-3)(n-3)/2\) edges. Its complete connectivity classification is

\[
\mathcal T_{m,n}\cong
\begin{cases}
N_{m,n}K_1,&\min(m,n)=3,\\
24K_4,&m=n=4,\\
\text{one connected graph},&\min(m,n)\ge4,\ \max(m,n)\ge5.
\end{cases}
\]

The token-jump graph \(\mathcal J_{m,n}\) is connected whenever \((m,n)\ne(3,3)\); for \(m=n=3\) it consists of six isolated vertices. It is regular of degree \(3((m-2)(n-2)-1)\). Thus the first nontrivial sliding components appear at the four-by-four tensor product, where the 96 optima form 24 disjoint four-cliques; a single extra column suffices to connect all 240 optima on the four-by-five tensor product.

## Assumptions and scope

Graphs are finite, simple, and undirected; indices are labeled. The tensor product \(K_m\times K_n\) has vertex set \([m]\times[n]\), with adjacency between \((r,c)\) and \((s,d)\) exactly when \(r\ne s\) and \(c\ne d\). Total domination includes the requirement that selected vertices themselves have selected neighbors. A slide uses **one edge of this tensor-product graph**; this differs from an ordinary rook move (the latter changes just one coordinate). All statements concern **minimum-cardinality** total dominating sets; no intermediate nonminimum configurations are admitted. No statement is made about factor sizes below three or other products.

## Proof

**1. Minimum configurations.** No two-vertex set totally dominates. If two chosen vertices are not adjacent, they fail to dominate one another or themselves. If they are adjacent, say \((r,c)\) and \((s,d)\) with \(r\ne s,c\ne d\), then \((r,d)\) is adjacent to neither. A set of three vertices in distinct rows and distinct columns totally dominates: at most one selected vertex shares the row of an arbitrary vertex and at most one shares its column, so at least one of the three is adjacent to that vertex. Conversely, if a three-vertex total dominating set had two selected vertices in the same row \(r\), then either all three lie in row \(r\) (which cannot dominate a vertex in that row) or its third vertex is \((s,d)\) with \(s\ne r\); in the latter case \((r,d)\) is adjacent to none of the three. The analogous argument excludes repeated columns. Therefore the minimum sets are precisely the partial permutation matrices of weight three. Choosing three rows, three columns and a bijection proves \(N_{m,n}=6\binom m3\binom n3\).

**2. Slide and jump degrees.** In a valid three-cell configuration, an individual selected cell can be slid to another valid cell only if the new row is entirely unoccupied and the new column is entirely unoccupied: adjacency requires that both coordinates change, while the other two selected cells already occupy two rows and two columns. There are \((m-3)(n-3)\) possibilities for each of the three selected cells, and distinct replacements give different configurations. This gives the regular degree and edge formula. For token jumping, after removing one selected cell there are \((m-2)(n-2)\) permissible row-column pairs, including the cell just removed; removing this one choice gives degree \(3((m-2)(n-2)-1)\).

**3. Frozen boundary and four-by-four fibers.** If either factor has size three, every configuration uses all its row indices or all its column indices, so no slide is possible. For \(m=n=4\), a partial matching of three row-column pairs has a unique unoccupied row and a unique unoccupied column. Appending their pair produces a uniquely determined full permutation matching of four pairs. Each legal slide replaces a selected pair by the appended pair; upon completing the new configuration, the removed pair becomes the new appended pair, so the full matching is invariant. Conversely, for a fixed full matching, all four ways to omit one pair are legal configurations, and any two are adjacent by a single slide. As there are \(4!=24\) full permutation matchings, \(\mathcal T_{4,4}=24K_4\).

**4. Constructive connectivity with one spare row and two spare columns.** It suffices to treat \(m\ge4,n\ge5\); the other unequal orientation follows by transposing indices. Every size-three partial matching can be carried into any other by permutations of the row labels and column labels. Transpositions of two occupied rows, an occupied and an unoccupied row, two occupied columns, or an occupied and an unoccupied column generate the relevant actions; exchanges of two unoccupied labels do not change a matching. Fix three selected cells \(\{(0,0),(1,1),(2,2)\}\), one unoccupied row \(3\), and two unoccupied columns \(3,4\). The following three sequences are legal slides, each preserving a partial matching of size three at every intermediate step (each arrow specifies the single removed cell and its replacement):

- **Swap the first two occupied row assignments:** \((1,1)\to(3,3)\), \((0,0)\to(1,4)\), \((1,4)\to(0,1)\), \((3,3)\to(1,0)\). The result is \(\{(0,1),(1,0),(2,2)\}\), which also exchanges the first two occupied column assignments.
- **Replace an occupied row with a spare row, leaving its selected column unchanged overall:** \((0,0)\to(3,3)\), \((3,3)\to(0,4)\), \((0,4)\to(3,0)\). The result is \(\{(3,0),(1,1),(2,2)\}\).
- **Replace an occupied column with a spare column, leaving its selected row unchanged overall:** \((0,0)\to(3,4)\), \((3,4)\to(0,3)\). The result is \(\{(0,3),(1,1),(2,2)\}\).

Relabeling rows and columns carries these legal templates to every selected/spare position. The first template realizes all transpositions of two occupied rows or occupied columns; the other templates exchange occupied and spare rows or columns. Hence every row permutation and every column permutation can be effected by legal slide sequences. Since row and column permutations act transitively on all three-cell partial matchings, \(\mathcal T_{m,n}\) is connected for \(m\ge4,n\ge5\).

**5. Token jumping.** Changing only the row of one selected cell to an unoccupied row, or only its column to an unoccupied column, always preserves the three-cell partial matching, so it is a legal jump. If at least one of \(m,n\) exceeds three, fix all three distinct indices in the smaller coordinate and use an unused index in the larger coordinate as a temporary buffer. Such one-coordinate replacements can move any three-element injection to any other, including interchanges of two occupied images by first moving one to the spare, moving the second to its former image, then moving the spared one to the second image. Where the other coordinate also has unused indices, its active indices can be adjusted individually as well. This proves connectedness for all \((m,n)\ne(3,3)\). For \((3,3)\), all rows and columns are occupied, so even a jump cannot replace one cell and retain the matching property; its six configurations are isolated.

## Verification

The standalone script `direct_check.py` enumerates vertex subsets in the original product graph, tests total domination against *every vertex*, excludes all sets of size two, identifies every valid set of size three, and constructs both reconfiguration graphs directly. It checks component sizes, regularity, and edge counts for nine parameter pairs through \((5,6)\).

Independently, `matching_check.py` constructs size-three partial permutations rather than testing graph domination. It computes the slide graph by free-coordinate exchanges and verifies the formula and components for nine instances, through \((7,7)\), the latter having \(7,350\) states and \(176,400\) undirected slide edges. It also checks the legality, intermediate matching property and final target of all three finite generating templates. The captured outputs are `direct_check.out` and `matching_check.out`. The exhaustive computations test finite instances; the parameter-uniform assertions follow from the constructive proof above.

## Relationship to prior work

Henning and Kazemi, *k-tuple total domination in cross products of graphs* (first published online 2011-02-02), Corollary 15, established the minimum cardinality for categorical products of complete graphs. Its specialization to one-fold total domination and factor sizes at least three gives the already known numerical value \(3\). Their theorem and proof do not classify the three-cell optimal sets by reconfiguration moves or determine the sharp connectivity transition. The 2017 work of Alikhani, Fatehi and Mynhardt defines **addition/removal** total dominating graphs with configurations of size at most a threshold; its operations and state space are different. The 2020 survey by Mynhardt and Nasserasr explains the distinction between exchange and addition/removal rules. The primary-literature and mathematical-database comparisons found no statement covering the present exact slide-component classification. The tensor product must not be confused with Cartesian rook graphs or ordinary bipartite matching reconfiguration: our slides require changing **both** endpoint coordinates simultaneously.

## Limitations

The statement concerns factor sizes at least three and minimum total dominating sets only. It does not determine the diameters of the connected reconfiguration graphs, or say that the component classification is a classification of ordinary graph matchings under unrelated exchange rules. The token-jump connectedness and the scalar minimum are included for contrast, not claimed as independent new results. Historical-priority uncertainty remains because literature indexing cannot establish absolute absence of an equivalent earlier theorem. No independent mathematical review has been performed.

## References

1. M. A. Henning and A. P. Kazemi, *k-Tuple total domination in cross products of graphs*, Journal of Combinatorial Optimization 24 (2012), 339–346. Online publication 2011-02-02, DOI: [10.1007/s10878-011-9389-z](https://doi.org/10.1007/s10878-011-9389-z). Especially Theorem 14 and Corollary 15.
2. S. Alikhani, D. Fatehi, C. M. Mynhardt, *On k-Total Dominating Graphs*, arXiv:1711.04363 (2017), [full-text HTML](https://arxiv.org/html/1711.04363v2).
3. C. M. Mynhardt and S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey*, arXiv:2003.05956 (2020), [abstract](https://arxiv.org/abs/2003.05956).
4. B. Brešar, S. Klavžar and D. F. Rall, *Dominating direct products of graphs*, Discrete Mathematics 307 (2007), 1636–1642, DOI: [10.1016/j.disc.2006.09.013](https://doi.org/10.1016/j.disc.2006.09.013).
