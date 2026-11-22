# A sharp four-landmark dichotomy and 162 joint edge-identification bases in the Petersen graph

## Finding
Let \(P\) be the Petersen graph. A vertex landmark set \(S\subseteq V(P)\) is *edge resolving* if distinct edges of \(P\) have distinct ordered vectors of vertex-to-edge distances over \(S\). It is *vertex–edge dominating* if each edge has distance at most one from some vertex of \(S\). The following three exact statements hold.

1. Among the \(\binom{10}{4}=210\) four-vertex subsets, exactly fifteen are edge resolving, and these are **exactly the fifteen that are not vertex–edge dominating**. Consequently no four-vertex set satisfies both conditions.
2. The minimum size of a set satisfying both conditions is \(\gamma_{emd}(P)=5\), and precisely \(162\) labelled five-vertex sets attain it. Under the natural automorphism group \(S_5\), the minimum sets form four orbits of sizes \(60,60,30,12\). Viewed as five-edge subgraphs of \(K_5\), the types are respectively a four-cycle with one pendant edge, a triangle with two pendant leaves attached at *different* triangle vertices, \(K_4\) with one edge removed together with an isolated ground vertex, and a five-cycle.
3. The complete cardinality polynomial of joint sets is
\[
J_P(z)=162z^5+195z^6+120z^7+45z^8+10z^9+z^{10}.
\]
The ordinary edge-resolving polynomial is \(15z^4+J_P(z)\), and the vertex–edge dominating polynomial is \(60z^3+195z^4+252z^5+210z^6+120z^7+45z^8+10z^9+z^{10}\).

The already-known ordinary edge metric dimension \(\operatorname{edim}(P)=4\) is not asserted as a new result. The new result is the exact four-set incompatibility, the sharp joint size, the full optimum classification and the counting polynomials.

## Assumptions and scope
Model \(P\) as the Kneser graph \(\mathrm{KG}(5,2)\): its vertices are the ten two-subsets of the ground set \(\{0,1,2,3,4\}\); two distinct vertices are adjacent exactly when the two-subsets are disjoint. This model is isomorphic to the usual generalized Petersen model \(GP(5,2)\). Every Petersen edge joins disjoint root edges \(a,b\) of \(K_5\).

For \(v\in V(P)\) and an edge \(e=ab\in E(P)\), set \(d(v,e)=\min\{d_P(v,a),d_P(v,b)\}\). For a fixed increasing ordering \(S=(v_1,\ldots,v_k)\), its edge signature is \(\rho_S(e)=(d(v_1,e),\ldots,d(v_k,e))\). Being edge resolving means that the fifteen signatures are pairwise distinct. Being vertex–edge dominating means \(\min_{v\in S}d(v,e)\le1\) for all fifteen graph edges. The numerical counts concern labelled vertex subsets, not ordered landmark lists.

## Proof
**Step 1: exact obstruction to domination.** In \(\mathrm{KG}(5,2)\), two distinct vertices represented by intersecting two-subsets have graph distance two, and disjoint two-subsets have graph distance one. For a Petersen edge \(e=ab\), the root pairs \(a,b\) are disjoint and together use four ground labels. The vertices at edge distance *two* from \(e\) are precisely the four cross-pairs each taking one label from \(a\) and one from \(b\). Call this four-set \(C_e\). Thus \(S\) fails domination if and only if \(S\subseteq C_e\) for some \(e\). All fifteen \(C_e\) are different: as four root edges they form a four-cycle with the fifth ground label isolated, and their opposite root-pair partition uniquely specifies \(e\). Consequently every landmark set of size at least five dominates, and exactly fifteen four-sets fail domination.

**Step 2: finite exhaustive edge separation and orbit representatives.** There are only ten landmark positions and fifteen edges. The direct verifier `census_symbolic.py` constructs all fifteen columns \(d(v,e)\) from the preceding exact distance rule, iterates every one of the \(2^{10}=1024\) landmark subsets, and tests pairwise distinctness of the fifteen signatures. This is exhaustive, not a statistical sample. It establishes the edge-resolving counts by size \((4,15),(5,162),(6,195),(7,120),(8,45),(9,10),(10,1)\), and no resolving subset of smaller cardinality.

For additional structural reconstruction, it generates all \(5!=120\) permutations of ground labels, acts on all \(\binom{10}{4}=210\) and \(\binom{10}{5}=252\) landmark subsets, and finds their distinct orbit decompositions. A representative below is written as a comma-separated list of two-digit root edges, e.g. `02,03,12,13`. All entries are certified by the exact fifteen-edge signature test.

| Size | Representative root edges | Orbit size | Resolving? |
|---|---|---:|---|
| 4 | `01,02,03,04` | 5 | no |
| 4 | `04,12,13,23` | 10 | no |
| 4 | `02,03,12,13` | 15 | yes |
| 4 | `01,02,03,12` | 60 | no |
| 4 | `01,03,04,12` | 60 | no |
| 4 | `02,04,12,13` | 60 | no |
| 5 | `01,04,12,13,23` | 60 | no |
| 5 | `02,03,04,12,13` | 60 | yes |
| 5 | `01,02,04,12,13` | 60 | yes |
| 5 | `01,02,03,04,12` | 30 | no |
| 5 | `01,02,03,12,13` | 30 | yes |
| 5 | `03,04,12,14,23` | 12 | yes |

The orbit-size totals are \(210\) and \(252\), respectively, proving no orbit was omitted. The unique resolving four-set orbit is exactly the \(C_e\) orbit found in Step 1, proving the four-landmark dichotomy. At size five the four resolving orbits give \(60+60+30+12=162\). Since every five-set dominates, precisely these sets are joint optima. The four root-graph types stated above are read directly from the four yes representatives and are invariant under relabelling.

**Step 3: all-size enumeration and independent check.** Step 1 makes domination automatic for sets of size at least five; therefore the exact resolving cardinality census of Step 2 gives every coefficient of \(J_P\) and both other polynomials. As an independent computational derivation, `census_bfs.cpp` constructs the graph using the *different* outer-cycle, spoke and inner-pentagram representation \(GP(5,2)\), computes all ten-vertex distances by breadth-first search, constructs its fifteen edge-distance columns and repeats the exhaustive \(1024\)-subset checks. It independently asserts the identical three polynomial coefficient arrays. This supplies a separate graph construction and metric computation rather than a mere replay of the same formulas.

## Verification
From the directory containing the embedded files, run `python3 census_symbolic.py`, or `g++ -std=c++17 -O2 census_bfs.cpp -o census_bfs && ./census_bfs`. The first outputs the complete six-orbit-by-six-orbit classification, three polynomials and `PET_X5_SYMBOLIC_OK`; the second outputs `PET_X5_BFS_OK`. Recorded exact outputs are embedded in `symbolic_output.txt` and `bfs_output.txt`. Both were executed successfully for this finding. Enumeration covers all ten-vertex subsets, so there is no untested larger finite instance inside the claim.

## Relationship to prior work
Ikhlaq, Hayat and Siddiqui (first posted 17 November 2022, arXiv:2211.09327) introduced vertex–edge dominant edge metric dimension, combining edge resolution with distance-one vertex–edge coverage. Their described graph families do not include the Petersen sharp dichotomy and four-orbit census. Filipović, Kartelj and Kratica (first posted 2 July 2018, arXiv:1807.00580) studied ordinary edge metric dimension in generalized Petersen graphs; their Petersen value four is compatible with, but does not imply, the stronger joint answer of five. The 2023 *dominant edge metric dimension* of Tavakoli et al. requires a **vertex cover**, a stronger and different domination predicate than distance-one vertex–edge coverage; results for that different invariant cannot automatically identify the joint sets here. The finite classification is supported by complete, reproducible calculations, not an assertion that absence from searches proves publication priority.

## Limitations
The classification concerns the ten-vertex Petersen graph only. No formula for arbitrary generalized Petersen graphs is asserted. The orbit classification relies on a fully specified and reproducible exact finite enumeration, checked independently with a second graph representation, rather than a short purely handwritten enumeration of all \(1024\) subsets. A paper or computational census not found in the accessible literature could affect historical novelty; independent mathematical review has not been performed.

## References
1. H. M. Ikhlaq, S. Hayat and H. M. A. Siddiqui, *Unique identification and domination of edges in a graph: The vertex-edge dominant edge metric dimension*, arXiv:2211.09327 (first posted 2022-11-17). https://arxiv.org/abs/2211.09327
2. V. Filipović, A. Kartelj and J. Kratica, *Edge metric dimension of some generalized Petersen graphs*, arXiv:1807.00580 (first posted 2018-07-02); *Results in Mathematics* 74 (2019), 182. https://arxiv.org/abs/1807.00580
3. M. Tavakoli, M. Korivand, A. Erfanian, G. Abrishami and E. T. Baskoro, *The dominant edge metric dimension of graphs*, *Electronic Journal of Graph Theory and Applications* 11 (2023), DOI:10.5614/ejgta.2023.11.1.16. https://doi.org/10.5614/ejgta.2023.11.1.16
