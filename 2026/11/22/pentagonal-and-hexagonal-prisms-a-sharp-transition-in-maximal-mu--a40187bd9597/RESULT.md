# Pentagonal and hexagonal prisms: a sharp transition in maximal mutual-visibility mobility

## Finding

Let \(G_t=C_t\square K_2\), with two labelled cycle layers and \(t\in\{5,6\}\). A mutual-visibility set is a vertex subset for which each pair of selected vertices admits a shortest path with no other selected vertex internally. Write \(V_t(z)\) for the polynomial counting **all** such sets and \(F_t(z)\) for the polynomial counting the **inclusion-maximal** ones, by their number of vertices. Then

\[
\begin{aligned}
V_5(z)&=1+10z+45z^2+110z^3+115z^4+30z^5,\\
F_5(z)&=10z^4+30z^5,\\
V_6(z)&=1+12z+66z^2+208z^3+351z^4+252z^5+2z^6,\\
F_6(z)&=240z^5+2z^6.
\end{aligned}
\]

In particular, the lower mutual-visibility numbers are \(\mu^-(G_5)=4\) and \(\mu^-(G_6)=5\). All ten four-vertex maximal sets in \(G_5\) are exactly

\[
S_{i,\epsilon}=\{(0,i),(0,i+1),(1,i+2+\epsilon),(1,i+3+\epsilon)\},
\quad i\in\mathbb Z/5\mathbb Z,\ \epsilon\in\{0,1\}.
\]

There are exactly two six-vertex mutual-visibility sets in \(G_6\), namely the two alternating-column classes \(B_0,B_1\) given by \(c\equiv0,1\pmod2\), each containing both layer vertices in three alternating columns. Of the 252 mutually visible five-sets, precisely the twelve obtained by deleting one vertex from one of these two classes are **not** inclusion-maximal. The other 240 are all the minimum inclusion-maximal sets. These 240 optima form eleven orbits under the dihedral rotations/reflections of the cycle and interchange of the two layers: two orbits of size twelve and nine of size twenty-four. The ten optima in \(G_5\) form a single orbit.

Define the *optimal token-slide graph* to have the minimum-cardinality inclusion-maximal mutual-visibility sets as vertices, with an edge whenever one selected vertex can be moved along an edge of the underlying prism to an unselected vertex and the resulting set remains minimum-cardinality inclusion-maximal. The optimal token-jump graph similarly allows a move to any empty vertex. For \(G_5\), the slide graph consists of ten isolated vertices, while the jump graph is a ten-cycle. For \(G_6\), the slide graph is connected, has 240 vertices and 816 edges, radius six and diameter seven; its vertex eccentricities are six (120 vertices) and seven (120 vertices). The jump graph on those same 240 configurations is connected with 1842 edges and is self-centered of radius and diameter five.

## Assumptions and scope

All graphs are simple, finite and labelled; layer \(r\in\{0,1\}\) and cycle coordinate \(c\in\mathbb Z/t\mathbb Z\) give vertices \((r,c)\). Each vertex \((r,c)\) is adjacent to \((r,c-1)\), \((r,c+1)\), and \((1-r,c)\). Sets are distinct as labelled subsets, with no identification under graph automorphisms except when the orbit statement explicitly says so. A maximal set is maximal by inclusion, not maximum by cardinality. All statements are exactly for \(t=5\) and \(t=6\), not for general cycle lengths.

## Proof

The proof is a complete finite enumeration with explicit, independently recomputed predicates and complete saved code. Put \(N=2t\) and identify \((r,c)\) with integer \(rt+c\). For every ordered vertex pair \(u,v\), breadth-first search computes graph distance \(d(u,v)\). Starting at \(u\), recurse only to neighbors \(w\) satisfying \(d(w,v)=d(u,v)-1\), thus listing **every** shortest path to \(v\) and no non-shortest path. Represent each such path by the bitmask of its internal vertices. A subset mask \(S\) is mutual-visible if and only if, for each pair of vertices \(u,v\in S\), at least one listed internal mask has empty intersection with \(S\). This is an equivalence from the definition: every path produced is shortest, and every shortest path decreases distance at each step.

The predicate is hereditary under taking subsets. Consequently, a feasible set is inclusion-maximal exactly when none of its one-vertex supersets is feasible: any larger feasible superset would contain a feasible one-vertex extension. This characterizes all maximal sets without relying on a greedy choice. Enumerating **every** mask from zero through \(2^N-1\), and sorting by popcount, gives the following exact tables:

| Cycle length | Feasible by cardinality, starting at zero | Maximal by cardinality | Total feasible |
|---|---|---|---|
| \(5\) | \(1,10,45,110,115,30\) | \(10\) at four, \(30\) at five | \(311\) |
| \(6\) | \(1,12,66,208,351,252,2\) | \(240\) at five, \(2\) at six | \(892\) |

The explicit formula for the ten four-sets follows by comparing the complete optimum-mask list against the ten distinct \(S_{i,\epsilon}\); this is an equality of finite sets, not merely an equal cardinality. Likewise, the only two feasible six-masks for \(t=6\) equal the two alternating-column classes (not the graph bipartition classes). Each of their six five-subsets is feasible and they are disjoint, giving twelve nonmaximal feasible five-subsets; because the exhaustive census finds no feasible seven-set, all other feasible five-sets are maximal.

The relocation graphs are computed on the **complete** optimum-mask lists. An edge is present exactly when the symmetric difference has two vertices, one leaving and one entering; for slides these must additionally be adjacent in the underlying prism. Exhaustive graph traversal gives the claimed connected components. A breadth-first search from **every** optimum configuration gives both radius and diameter and the complete eccentricity distributions. A direct group action generated by rotations, reflections and layer exchange gives the stated orbits; the listed orbit sizes add up to the exact optimum counts.

The completely separate recomputation in `verify_bfs.py` does not enumerate geodesics. Instead, it tests each selected pair by BFS in the original graph and in the graph with other selected vertices forbidden, requiring the two distances to match. It independently reconstructs all subset masks and relocation graph distances. It matches the shortest-path implementation's entire feasibility bitmap and entire optimum-mask list by their SHA-256 digests, not only the displayed aggregate counts. Thus the finite enumeration is exhaustive and is supported by two logically distinct, executable tests.

## Verification

The artifact paths `verify_paths.py`, `verify_bfs.py`, `paths_results.txt` and `bfs_results.txt` are included in the same package. With Python 3 and no nonstandard packages, in one directory run:

```bash
python3 verify_paths.py > paths_results.txt
python3 verify_bfs.py
```

The first command concludes with `PATH_ENUMERATION_OK`; the second with `BFS_RECOMPUTATION_OK`. In both implementations the exhaustive universe has exactly \(2^{10}=1024\) subsets for \(G_5\) and \(2^{12}=4096\) for \(G_6\). Hashes of the full binary feasibility vectors are, respectively, `a811e6159098e59184985a2a331e0694c030b2c68229784ffe2c6ceef5d0f36e` and `931490a850a177ac2458c13b456a772dff950f3a0964f1e9db25589d4441c411`. The second program checks these full vectors against the first, as well as all optimal masks.

## Relationship to prior work

Brešar and Yero introduced the lower mutual-visibility number, including the smallest-cardinality *maximal* condition, and explicitly asked for this parameter on Cartesian cylinders; their publicly posted version dates to July 6, 2023. The present two exact cylinder cases refine that question. Korže and Vesel determined the *largest* mutual-visibility sets of \(P_2\square C_t\) in 2024, including cardinalities five and six for the present graphs, but largest feasible size does not determine the least size of a maximal feasible set, the complete maximal-set polynomial or relocation geometry. Cicerone, Di Stefano and Klavžar studied ordinary mutual visibility and Cartesian products but not the lower parameter and the enumerations here. Kuziak and Rodríguez-Velázquez's work studies the *total* mutual-visibility requirement, which quantifies over all pairs of graph vertices rather than pairs of selected vertices. Related record searches included aliases \(GP(5,1)\), \(GP(6,1)\), pentagonal/hexagonal prism, maximal mutual visibility, facet polynomial, lower number and token sliding; no theorem covering these specific statements was identified. This does not establish exhaustive historical priority.

## Limitations

This is a verified finite result only for two specific cubic prism graphs, not a proof of a parity law or a general-cylinder classification. The relocation vertices must remain **inclusion-maximal** at every step; a weaker reconfiguration graph allowing nonmaximal intermediate configurations is a different problem. The exhaustive computational certificates cover exactly the stated finite search spaces. Independent scholarly validation and a complete search of every publication are not claimed.

## References

1. B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951, v1 posted 2023-07-06, https://arxiv.org/html/2307.02951v2 .
2. D. Korže and A. Vesel, *Mutual-Visibility Sets in Cartesian Products of Paths and Cycles*, Results in Mathematics 79 (2024), article 116, https://doi.org/10.1007/s00025-024-02139-x .
3. S. Cicerone, G. Di Stefano, and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, Applied Mathematics and Computation 438 (2023), article 127619, https://arxiv.org/abs/2112.13024 .
4. D. Kuziak and J. A. Rodríguez-Velázquez, *Total Mutual-Visibility in Graphs with Emphasis on Lexicographic and Cartesian Products*, Bulletin of the Malaysian Mathematical Sciences Society 46 (2023), article 197, https://doi.org/10.1007/s40840-023-01590-3 .
