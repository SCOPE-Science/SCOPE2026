# Optimal connected domination in the ternary Hamming three-cube: one connected jump graph, 504 slide islands

## Finding
Let \(G=K_3\square K_3\square K_3\) be the graph on the \(27\) ternary triples, with adjacent vertices differing in precisely one coordinate. A *connected dominating set* \(D\) satisfies \(N_G[D]=V(G)\) and induces a connected graph. Write \(\mathcal D\) for all connected dominating sets of smallest cardinality.

The connected domination number is exactly \(\gamma_c(G)=8\), and there are exactly \(|\mathcal D|=11\,340\) such sets. Define the **token-jump graph** \(J\) on \(\mathcal D\), with two sets adjacent if one vertex is removed and one new vertex inserted. Define the **token-slide graph** \(S\) by requiring, additionally, that the removed and inserted vertices were adjacent in \(G\). Every intermediate state must belong to \(\mathcal D\).

The jump graph is connected, with exactly \(73\,386\) undirected edges, and **every vertex has eccentricity nine**, so
\[
\operatorname{rad}(J)=\operatorname{diam}(J)=9.
\]
Its unordered distinct-pair shortest-path distance distribution is exactly:

| Distance | Number of unordered pairs |
|---:|---:|
| 1 | 73,386 |
| 2 | 448,416 |
| 3 | 1,964,574 |
| 4 | 5,972,616 |
| 5 | 12,581,730 |
| 6 | 19,397,880 |
| 7 | 17,513,334 |
| 8 | 6,099,786 |
| 9 | 240,408 |

The slide graph has \(14\,094\) undirected edges but **504 connected components**, none isolated. There are precisely \(162\) components of order \(2\), \(72\) of order \(9\), \(108\) of order \(18\), and \(162\) of order \(52\); their respective diameters are \(1,4,9,11\). The 504 slide components form exactly four orbits under the natural coordinate-permutation and ternary-symbol-permutation automorphism group, one orbit per component order. The 11,340 optimal sets form eleven automorphism orbits with orbit-size multiplicities \(324:1\), \(648:3\), and \(1296:7\).

This is a sharp finite all-state and all-pair classification for this particular graph; no infinite-family theorem is asserted.

## Assumptions and scope
Each vertex of \(G\) is an ordered triple in \(\{0,1,2\}^3\); the three coordinate factors are ordinary simple complete graphs of order three. Thus each vertex has exactly six distinct neighbors. Domination includes the selected vertices themselves. Connectedness refers to the **induced** subgraph on selected vertices. Both reconfiguration graphs are unlabelled-token, undirected, fixed-cardinality graphs, and they do not permit temporary loss of connected domination or spare tokens. No equivalence with the token-addition/removal model is assumed.

For unambiguous reproducibility, the C++ verifier labels a triple by the integer \(a+3b+9c\). The independent Python verifier uses the lexicographic `itertools.product` enumeration instead. Both generate the graph from the coordinate difference test rather than loading external graph data.

## Proof
**1. Minimum size and complete state set.** A selected vertex dominates at most seven vertices (itself and its six neighbors). Therefore at least four vertices are needed to dominate all 27 vertices, irrespective of connectivity. Enumerate **every** \(k\)-element subset for each \(k\in\{4,5,6,7,8\}\), using its 27-bit characteristic mask. Domination is the equality of the union of seven-vertex closed-neighborhood masks with the full 27-bit mask. Connectedness is tested by a traversal restricted to the selected mask, requiring the traversed mask to equal the selected mask. Both supplied programs perform these checks exhaustively, obtaining no connected dominating sets at sizes four through seven and exactly \(11\,340\) at size eight. Since a size-eight set exists and all smaller possibilities have been excluded, this proves both the optimum size and exact number of optimum configurations.

**2. Exhaustion of legal transitions.** Index the complete set of 11,340 accepted masks. For every accepted mask \(D\), every selected \(u\in D\), and every unselected \(v\notin D\), look up \((D\setminus\{u\})\cup\{v\}\) in that index. An accepted neighbor is a jump edge; it is also a slide edge if and only if the original triples \(u\) and \(v\) differ in exactly one coordinate. Each unordered edge is recorded once, by increasing configuration index. The resulting exact counts are \(|E(J)|=73\,386\) and \(|E(S)|=14\,094\).

**3. Jump metric.** The C++ verifier runs breadth-first search from **every** one of the 11,340 jump configurations over their complete exact edge lists. Every search reaches all 11,340 states, and the maximal distance is nine from every root. Counting only target indices greater than the root yields the nine distance frequencies in the table. Their sum is \(64\,292\,130=\binom{11\,340}{2}\), ensuring all unordered distinct pairs are included. This proves connectedness, self-centeredness, the sharp radius and diameter, and the entire distance table. The second verifier independently reconstructs the state graph and uses automorphism orbits to test jump eccentricity: it produces eleven orbits and BFS from one representative of each yields eccentricity nine. Automorphisms preserve distances, so this independent test covers every vertex's eccentricity.

**4. Slide decomposition.** Exhaustive BFS over the complete slide adjacency lists gives exactly 504 components and the stated four order multiplicities. Within **each** component, the C++ program runs BFS from **each** of its vertices and computes its exact diameter, yielding the four claimed diameter values. The independent verifier separately rebuilds the slide graph and obtains the same 504-component order distribution. It applies eight elementary automorphisms (two coordinate transpositions and two symbol transpositions in each of the three coordinates) to components and verifies that components of each given order form a single automorphism orbit. The Python verifier also reconstructs and verifies each of the four component diameters from a representative component. This proves the component-orbit statement, including that components of the same order are mutually isomorphic.

All algorithm loops run through their entire explicitly finite combinatorial domains. Thus the computations are exhaustive proofs of the stated fixed-graph claims, not sampled numerical evidence or an extrapolation to larger ternary products.

## Verification
The complete standalone artifacts `verify_fast.cpp` (C++17, standard library) and `verify_independent.py` (Python 3, standard library) are included, along with `fast_output.txt` and `independent_output.txt` captured from successful executions. From the directory containing the files, execute:

```sh
g++ -std=c++17 -O3 verify_fast.cpp -o verify_fast
./verify_fast
python3 verify_independent.py
```

The programs use separately generated vertex labels and neighbor representations. The C++ enumerator uses Gosper's bit-combination successor and bitwise flood-fill; the Python enumerator uses `itertools.combinations`, set-based induced connectivity, and independently generated coordinate automorphisms. Assertions test the exact counts, the C++ all-pairs jump histogram, and the two independent slide component decompositions. Neither program relies on precomputed graph files or network services. The captured outputs are convenient witnesses, but the full source computations are the operative verification evidence.

## Relationship to prior work
Abu-Khzam et al. (2022) developed general efficient algorithms and extremal bounds for enumerating inclusion-minimal connected dominating sets; those are not the minimum-cardinality reconfiguration metrics computed here. Lokshtanov et al. (2019) analyzed parameterized complexity of connected-dominating-set reconfiguration under **token addition/removal** and a size cap; that feasible-state graph is different from the fixed-size minimum-only token-jump and token-slide graphs here. The published exact exchange graph for connected domination in the *binary four-cube* concerns \(Q_4\) on 16 vertices, with 192 size-six configurations, jump diameter seven, and no legal slides. It neither contains nor determines this 27-vertex ternary-cube answer: in particular, it has different graph adjacency, optimum cardinality, and move structure. Results on circular ladders and Cartesian-product domination are likewise on different graph families or domination variants.

The contribution claimed here is the **entire ternary three-cube optimum configuration space and its contrasting complete jump and slide routing geometries**, not the novelty of the general definitions, breadth-first search, or the existence of connected domination. Indexed semantic searches and inspection of these closest primary claims found no earlier theorem implying the exact statements. Search absence is not a proof of historical priority, and unindexed exact computations remain a genuine possibility.

## Limitations
The findings are entirely about the fixed 27-vertex graph \(K_3\square K_3\square K_3\); they do not establish formulas for higher-dimensional or different-alphabet Hamming graphs. The correctness proof is finite exhaustive computation rather than a closed-form structural classification of all optimal sets. Component types of order 52 are identified by order, diameter and automorphism equivalence, not by an abstract canonical graph name. All findings were reviewed within this package, but an independent external scientific audit and exhaustive historical priority review have not been performed.

## References
1. F. Abu-Khzam, H. Fernau, B. Gras, M. Liedloff and K. Mann, “Enumerating Connected Dominating Sets,” arXiv:2205.00086, first publicly posted 2022-04-29. https://arxiv.org/abs/2205.00086
2. D. Lokshtanov, A. E. Mouawad, F. Panolan and S. Siebertz, “On the Parameterized Complexity of Reconfiguration of Connected Dominating Sets,” arXiv:1910.00581, first publicly posted 2019-10-01. https://arxiv.org/abs/1910.00581
3. “The Cayley exchange graph of minimum connected dominating sets in the four-cube,” published exact finite computation, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-the-cayley-exchange-graph-of-minimum-connected-dominating-sets-i--24a2261a2118
