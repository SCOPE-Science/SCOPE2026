# Exact one- and two-detector exchange graphs for minimum redundant identifying codes of the Heawood graph

## Finding

Let \(H\) be the point–line incidence graph of the Fano plane. An identifying code is a vertex set whose intersections with the closed neighborhoods are nonempty and pairwise distinct. A redundant identifying code (RED:IC) is an identifying code that remains identifying after any one selected detector is removed; the host graph and its neighborhoods are unchanged. On the set of minimum RED:ICs, let \(\mathcal R_r\) join two distinct codes if they exchange exactly \(r\) selected vertices against \(r\) unselected vertices. There is no host-adjacency constraint or requirement on intermediate sets during a move.

**Theorem.** The one-detector exchange graph \(\mathcal R_1\) has fourteen isolated vertices and one connected \(84\)-vertex component. The isolates correspond to one-shore quadrangle omissions. The component is \(4\)-regular, has \(168\) edges, and has radius and diameter \(5\). Its distance shells, listed from distance zero, are \((1,4,10,22,39,8)\) at every vertex.

The graph \(\mathcal R_2\) of **exactly** two-detector exchanges is connected, with \(1134\) edges and radius and diameter \(2\). The fourteen quadrangle codes have degree \(30\) and shells \((1,30,67)\); the other eighty-four have degree \(22\) and shells \((1,22,75)\). Thus one-at-a-time exchanges cannot connect the minimum-code space, whereas exact two-at-a-time exchanges can.

## Input classification and scope

We use the deletion classification in *Redundant identifying codes of the Heawood graph: the Fano deletion classification* [1]. All minimum codes have size \(10\). Their omitted four-sets are the fourteen quadrangles (the complement of a line on the point shore or of a pencil on the line shore) and the eighty-four endpoint sets of induced two-edge matchings. This catalogue, the minimum size, and the full RED:IC cardinality polynomial are not contributions of the exchange theorem. The counts in the theorem refer to actual vertex subsets, not orbits. No assertion is made for larger projective planes.

## Proof

Label points \(P_i\) and lines \(L_j\) modulo \(7\), with \(P_i\) incident to \(L_j\) when \(j-i\in\{0,1,3\}\). The reversal of cyclic indices maps this incidence rule to that of [1]. By the input classification, the following construction lists all and only the omitted sets of minimum codes: take the complement on each shore of each of its seven projective lines or dual pencils; then take two points and two lines whenever every one of the four vertices has exactly one incidence inside that set. The latter condition says exactly that the four vertices induce two disjoint edges. Both constructions are on four-element sets, so with omissions \(O,O'\), the corresponding codes are adjacent precisely when \(|O\cap O'|=4-r\). This follows by taking complements on the common fourteen-vertex set.

A quadrangle shares at most two vertices with every matching omission, because a matching has two vertices on each shore. Two distinct quadrangles on the same shore share two vertices: their original projective lines (or dual lines) intersect in one, so the union of the original triples has size five. Opposite-shore quadrangles have empty intersection. Thus quadrangles are isolated in \(\mathcal R_1\). In a matching omission, replacing one line while retaining the two points and the other line must keep the new line incident to the previously matched point and not the other point. Of the three lines through that point one also contains the other point and one is the current line, leaving exactly one replacement. Dually there is exactly one move per point of the matching. These four possibilities preserve the two-shore balance and account for all moves, since a single replacement across shores cannot give an allowed omission. This proves the degree and edge count in \(\mathcal R_1\).

For the remaining metric claims, the bundled `check_exchange.py` implements an exact finite construction. It enumerates the \(\binom{7}{2}^2\) pairs of point and line pairs and tests the induced matching criterion, and constructs the fourteen quadrangles directly. For each \(r=1,2\), it inspects every unordered pair of distinct omissions and connects precisely those with intersection size \(4-r\). A breadth-first search starting at each omission assigns distance zero there and then assigns the next integer distance to each previously unvisited neighbor in queue order. By induction on the layers this gives exactly shortest distances, and the resulting shell sum is the size of the start vertex's component. The full shell multiplicities are:

| Exact replacements | Omission type | Shell vector | Starting vertices |
| ---: | :--- | :--- | ---: |
| 1 | Quadrangle | \((1)\) | 14 |
| 1 | Two-edge matching | \((1,4,10,22,39,8)\) | 84 |
| 2 | Quadrangle | \((1,30,67)\) | 14 |
| 2 | Two-edge matching | \((1,22,75)\) | 84 |

In particular, all eighty-four matching omissions lie in one component for \(r=1\), and all ninety-eight omissions lie in one component for \(r=2\). The last nonzero index gives the eccentricity in the respective component. Degree is the first shell after the start vertex; in \(\mathcal R_2\) the sum of degrees divided by two is \((14\cdot30+84\cdot22)/2=1134\).

## Reproduction and related results

Run `python3 check_exchange.py` with the accompanying standard-library script. It asserts the full shell tables for both moves, including the isolated vertices. This checks the exchanges given the geometric catalogue [1]; it does not use a table of precomputed exchange edges or assume transitivity to reduce the searches.

The one-offline-detector model is the RED:IC model of Jean and Seo [2]. The ordinary minimum identifying codes of the same host, with token slides [3], have a different feasible family and a more restrictive move. The one-edge exchange graph on *maximum three-edge induced matchings* [4] uses different configurations and a move on whole matching edges, not the point or line exchanges here. In particular its six-regular 84-vertex graph is not the four-regular component of \(\mathcal R_1\).

## References

1. [*Redundant identifying codes of the Heawood graph: the Fano deletion classification*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-redundant-identifying-codes-of-the-heawood-graph-the-fano-deleti--821f7bebe27a/RESULT.md), deletion classification in the Finding.
2. D. C. Jean and S. J. Seo, [*Fault-tolerant Identifying Codes in Special Classes of Graphs*](https://arxiv.org/abs/2112.01685).
3. [*The token-slide graph of minimum identifying codes of the Heawood graph*](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-the-token-slide-graph-of-minimum-identifying-codes-of-the-heawoo--f9533412f5d1/RESULT.md).
4. [*The Fano induced-matching exchange graph: a tripartite triangle geometry with diameter five*](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-the-fano-induced-matching-exchange-graph-tripartite-triangles-an--15f94095f8d3/RESULT.md).
