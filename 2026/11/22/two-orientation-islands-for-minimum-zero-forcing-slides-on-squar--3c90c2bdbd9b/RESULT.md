# Two orientation islands for minimum zero-forcing slides on square rook graphs

## Finding

Let \(R_n=K_n\square K_n\) be the rook graph on the cells of an \(n\)-by-\(n\) board. For a blue vertex set \(B\), ordinary zero forcing permits a blue vertex with exactly one white neighbor to turn that neighbor blue. Let \(\mathcal Z_n\) be the family of minimum-cardinality zero-forcing sets. In the **token-slide** graph \(\mathcal T_n\), two members of \(\mathcal Z_n\) are adjacent if one blue token is moved to an unoccupied *adjacent* rook-graph vertex and the result remains in \(\mathcal Z_n\). In the **token-jump** graph \(\mathcal J_n\), the removed and inserted rook-graph vertices need not be adjacent.

**Theorem.** For every integer \(n\ge3\), the token-slide graph \(\mathcal T_n\) has exactly **two connected components**. One consists of the blue complements of bipartite spanning trees on all column labels and all but one row label; the other is its row-column transpose. Each component has exactly
\[
n(n-1)^{n-1}n^{n-2}
\]
vertices. The token-jump graph \(\mathcal J_n\) on the same minimum sets is connected. For \(n=2\), the four minimum zero-forcing sets instead give four isolated vertices under token sliding, while their token-jump graph is connected (indeed, a four-cycle).

The known minimum cardinality is \(Z(R_n)=n^2-2n+2\), and the already-published exact count of minimum sets is \(2n(n-1)^{n-1}n^{n-2}\). **Neither the scalar minimum nor that enumeration is claimed as new.** The claim concerns the sharp and uniform difference between local and unrestricted reconfiguration.

## Assumptions and scope

All graphs are finite, simple and undirected. Board cells are labelled ordered pairs \((r,c)\) with \(r,c\in\{1,\ldots,n\}\); two distinct cells are adjacent exactly when they share a row or column. Construct the auxiliary bipartite graph \(H_B\) with \(n\) labelled row vertices and \(n\) labelled column vertices, taking one edge \(rc\) for each initially white board cell \((r,c)\). All row and column vertices, including isolates, remain present. A spanning tree on \(n-1\) row labels and all \(n\) column labels is understood as a tree covering all those \(2n-1\) auxiliary vertices. The moves keep the number of blue vertices fixed and every intermediate set must remain zero forcing. A slide is a single blue-token replacement along one edge of \(R_n\), not an arbitrary sequence of zero-forcing propagation steps.

## Proof

**1. Identify the optimum supports directly.** If a rook cell \((r,c)\) is blue, its number of white neighbors is \(d_H(r)+d_H(c)\), where \(d_H\) is degree in the auxiliary white-edge graph. Thus a blue cell can force exactly when one of its row/column endpoints is isolated in \(H\) and the other is a leaf. If there is no isolated row or column, no force is possible. A white-edge cycle can never be broken: every blue cell adjacent to any of its edges already has at least two white neighbors from that cycle. Hence every nonempty successful initial white support is an acyclic bipartite graph with an isolate.

With \(2n\) auxiliary vertices and at least one isolate, any such forest has at most \(2n-2\) edges. Therefore every zero-forcing set has at least \(n^2-2n+2\) blue cells. Conversely, take a spanning tree \(T\) on \(n-1\) rows and all \(n\) columns, leaving exactly one isolated row. Its \(2n-2\) edges distribute among \(n\) columns, so some column has degree one. A blue cell in the isolated row and that leaf column forces the unique white cell incident with the column. At this point there is both an isolated row and an isolated column, and the remaining forest can be eliminated edge by edge: choose any leaf and use the already isolated vertex on the opposite side to force its sole edge. Thus every such tree complement is zero forcing. The transposed construction works as well.

At equality, \(H_B\) has \(2n-2\) edges and is a forest with an isolate. A forest with \(2n\) vertices and \(2n-2\) edges has exactly two connected components. Because one is an isolate, the other is a spanning tree. It follows that precisely one row or precisely one column is isolated, never both. This proves the needed optimum-support classification independently of the existing literature.

**2. Count the two types.** The classical labelled bipartite spanning-tree formula gives \(\tau(K_{p,q})=p^{q-1}q^{p-1}\). There are \(n\) choices of the isolated row and \(\tau(K_{n-1,n})=(n-1)^{n-1}n^{n-2}\) trees on the remaining labels. Transposition gives the equally numerous isolated-column type, without overlap. This recovers the existing enumeration as a consistency check.

**3. A slide cannot change the isolated side.** A single blue token slide corresponds, on the white support, to deleting a white edge \(e\) and adding a white edge \(f\) sharing a row or column with \(e\). Suppose the initial tree has an isolated row \(a\) and no isolated column. To change the orientation, \(f\) would have to touch \(a\). Since \(e\) does not touch \(a\), the shared endpoint must be a column \(c\). Deletion and addition both touch \(c\), so no column can become isolated; every other column's degree is unchanged. The resulting minimum configuration, if valid, still has an isolated row. Hence no slide crosses between the row-isolate and column-isolate classes.

**4. Every fixed-orientation class is connected.** First fix the missing row \(a\), choose an active row \(r_*\ne a\) and a column \(c_*\). Any spanning tree \(T\) of \(K_{n-1,n}\) can be converted to the *double star* consisting of all \((r_*,c)\) and all \((r,c_*)\) with \(r\ne a,r_*\), using only shared-endpoint tree exchanges. For each column \(c\) not yet adjacent to \(r_*\), insert \((r_*,c)\), forming a unique cycle, and delete the last edge of the original path from \(r_*\) to \(c\). These exchanged edges share column \(c\), and the number of columns adjacent to \(r_*\) increases. Once \(r_*\) meets all columns, any other active row has degree one (otherwise there is a cycle). Move its sole edge from column \(c\) to column \(c_*\), sharing that row. Every intermediate support remains a tree with the same isolated row and hence corresponds to a legal blue-token slide.

To connect trees with different isolated rows \(a\ne b\), choose an active row \(r_*\) distinct from both, possible since \(n\ge3\), and the same \(c_*\). Convert both trees to their double stars centered at \((r_*,c_*)\). Move the sole white edge \((b,c_*)\) of the first tree to \((a,c_*)\), preserving the column and replacing the isolated row \(a\) by \(b\). This one move is legal and produces the second double star. Reversing the previous transformations connects the two original configurations. Thus the entire row-isolate class is connected. By transposition, so is the column-isolate class. Together with step 3, this proves exactly two slide components for \(n\ge3\).

**5. One jump joins the components.** From any row-isolate tree let \(a\) be its missing row. It has a leaf column \(c\), with unique incident white edge \(e=(r,c)\). Choose another column \(d\ne c\), delete \(e\), and insert the edge \(f=(a,d)\). The remaining original tree without its leaf column is connected, and adding the formerly missing row as a leaf at \(d\) gives a tree spanning all rows except the now isolated column \(c\). The two changed cells \((r,c)\) and \((a,d)\) lie in different rows and columns, so their replacement is a permitted *jump* but not a slide. Since both slide components are connected, the full jump graph is connected.

**6. Boundary.** For \(n=2\), there are exactly four optimum supports, the two row-isolate and two column-isolate two-edge stars. All four are frozen under slides: changing either of the two white edges to another cell in its row or column destroys the spanning-tree-with-isolate support. Any row-isolate optimum is one token jump from a column-isolate optimum; the four states form a cycle under jumps.

## Verification

Run `python3 verify_bruteforce.py` and `python3 verify_trees.py`, using only the Python standard library. The first program constructs the rook graph and independently applies the ordinary zero-forcing color-change rule to **all subsets of sizes up to the exact minimum** for \(n=2,3,4\), then constructs the slide and jump graphs on every minimum set and checks component sizes. The second instead enumerates white-cell bipartite supports, uses disjoint-set cycle detection to test the tree condition, and builds the legal shared-endpoint tree-exchange graph. The methods agree:

| \(n\) | minimum blue size | minimum sets | slide component sizes | slide edges | jump edges |
|---:|---:|---:|---|---:|---:|
| 2 | 2 | 4 | 1, 1, 1, 1 | 0 | 4 |
| 3 | 5 | 72 | 36, 36 | 162 | 414 |
| 4 | 10 | 3456 | 1728, 1728 | 22272 | 52368 |

The programs and their actual outputs are embedded with this report. These finite checks do not prove the all-\(n\) theorem; the six-step constructive argument above does.

## Relationship to prior work

Benson et al. (initial arXiv posting 2015-10-08) study zero forcing on graph products, and their full paper includes Cartesian-product results for two cycles rather than minimum-set slide connectivity on square rook graphs. Geneson, Haas and Hogben (arXiv initial posting 2020-09-01) establish the token-jump zero-forcing reconfiguration framework and general graph-family results, not this slide-component theorem. Montazeri and Soltankhah (2021) give the already-known scalar rook-graph forcing number. The online research note *Zero-forcing polynomials of rook graphs via bipartite forests* (2026-10-12) gives a substantially stronger classification of **which individual subsets are zero forcing** and all their counts. That prior characterization, including its extremal spanning-tree count, is credited here and not claimed as new. It does not state or calculate slide components or establish a legal slide path between all same-orientation optimizers. The additional result here is the shared-endpoint tree-pivot connectivity argument and its sharp failure to cross between the two orientations. In contrast, unrestricted one-token jumps do cross them.

A source stating only the minimum number, complete counting polynomial, or individual-set feasibility does not by itself give connectivity of the graph of *valid constrained moves*. The new theorem does follow from the prior spanning-tree characterization combined with the constructive pivot lemma proved above; it is therefore a structural reconfiguration refinement, **not** an independent new characterization or polynomial. Closely related reconfiguration work on other graphs and graph predicates does not directly assert this theorem.

## Limitations

The theorem is about **minimum ordinary** zero-forcing sets on **square** rook graphs, not all forcing sets, asymmetric rectangular boards, skew zero forcing or arbitrary graph products. It makes no claim about the exact diameters of the two infinite families of slide components. The known minimum number and spanning-tree enumeration must remain attributed to prior results. Searches of indexed mathematical work and a published exact rook-polynomial note found no explicit equivalent slide-component theorem, but historical priority cannot be proven by failed searches; an unindexed edge-pivot or graph-reconfiguration equivalent remains a residual risk. No independent scholarly audit has been performed.

## References

1. K. F. Benson, D. Ferrero, M. Flagg, V. Furst, L. Hogben, V. Vasilevska and B. Wissman, *Zero forcing and power domination for graph products* (earlier title: *Power domination and zero forcing*), arXiv:1510.02421, first posted 2015-10-08. https://arxiv.org/abs/1510.02421.
2. J. Geneson, R. Haas and L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220, first posted 2020-09-01; *Discrete Applied Mathematics* 329 (2023), 126–139. https://arxiv.org/abs/2009.00220.
3. Z. Montazeri and N. Soltankhah, *k-Forcing number for Cartesian product of some graphs*, *Contributions to Discrete Mathematics* 16 (2021), 89–97, Theorem 2.1. https://doi.org/10.55016/ojs/cdm.v16i1.68557.
4. *Zero-forcing polynomials of rook graphs via bipartite forests*, online mathematical research record, 2026-10-12. https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-zero-forcing-polynomials-of-rook-graphs-via-bipartite-forests--dd424d573692.
