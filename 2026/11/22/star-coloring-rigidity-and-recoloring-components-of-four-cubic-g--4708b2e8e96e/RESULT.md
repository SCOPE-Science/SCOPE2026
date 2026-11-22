# Star-coloring rigidity and recoloring components of four cubic girth-six graphs

## Finding

A **star vertex coloring** is a proper vertex coloring for which no simple path on four vertices is colored alternately with only two colors. Let \(\mathcal R_4(G)\) have as vertices all proper star colorings of \(G\) using the named palette \(\{0,1,2,3\}\), and join two colorings when they differ at exactly one vertex. For the Heawood graph \(H\), the Möbius–Kantor graph \(M\), the Pappus graph \(P\), and the Desargues graph \(D\), the star chromatic number is exactly \(4\). Their entire optimal recoloring graphs, as disjoint unions, are:

\[
\begin{aligned}
\mathcal R_4(H)&\cong336Q_3,\\
\mathcal R_4(M)&\cong2280K_1\sqcup1152K_2\sqcup192C_4,\\
\mathcal R_4(P)&\cong3072K_1\sqcup1296K_2\sqcup648P_3\sqcup144Q_3,\\
\mathcal R_4(D)&\cong7200K_1\sqcup1440K_2\sqcup480Q_3\sqcup720(P_3\square P_3).
\end{aligned}
\]

Here \(Q_3\) is the three-dimensional cube, \(P_3\) the three-vertex path and \(\square\) the Cartesian graph product. In the same order the counts of optimal colorings modulo palette relabeling are \(112,223,365,850\); named-coloring counts are \(2688,5352,8760,20400\), with \(4032,1920,4320,15840\) undirected recoloring edges. The Heawood optimal recoloring graph has no frozen colorings; the three larger graphs have respectively \(2280,3072,7200\) isolated optimal colorings. All connected components have at most nine vertices.

## Assumptions and scope

All graphs are finite, undirected, simple, and labeled by the following explicit models. For \(H\), the points have labels \(0,\ldots,6\) and lines labels \(7,\ldots,13\); incidence is \(i\sim7+(i+d)\bmod7\) for \(d\in\{0,1,3\}\). For \(M=GP(8,3)\), vertices are \(u_i,v_i\) for \(i\in\mathbb Z/8\mathbb Z\), with cycle edges \(u_iu_{i+1}\), spokes \(u_iv_i\), and inner edges \(v_iv_{i+3}\). For \(P\), points are \((x,y)\in\mathbb F_3^2\) and nine lines are the families \(x=a\), \(y=b\), \(x+y=c\), with the natural incidences. For \(D\), the two shores are the two- and three-element subsets of a five-element set; inclusion is adjacency. These are standard isomorphic models of the four named graphs. All four have girth six and degree three.

All four color names are distinct, and all four appear in every vertex of \(\mathcal R_4(G)\), as follows from minimality. The graph components are on named (not color-permutation-quotiented) optimal colorings. A recoloring move changes exactly one vertex and must remain a star coloring. The empty-or-one-vertex special cases of any coloring definition are irrelevant here.

## Proof

The finite exhaustive proof uses the following complete, pruning-preserving enumeration, independently implemented in the accompanying Python and C++17 programs.

**Step 1: All constraints.** Enumerate every ordered four-tuple \((a,b,c,d)\) of distinct vertices for which \(ab,bc,cd\) are graph edges. It is sufficient to require that the colors of \(a,c\) not equal each other simultaneously with equality of the colors of \(b,d\). This enforces exactly the absence of a two-colored four-vertex path; inducedness is **not** required. Also enforce different colors on each adjacent pair.

**Step 2: Exhaustive palette reduction.** Enumerate all canonical color words on the fixed vertex order, introducing names \(0,1,2,3\) in order of their first occurrence. These restricted-growth words index colorings modulo global permutation of the four names uniquely. In a recursive search, reject a partial word immediately if it violates an already fully assigned edge or four-vertex-path constraint. Such a rejection cannot remove any valid completion, since its witness already has all vertices assigned. Both programs enumerate all valid three-color canonical words and find none, while their four-color enumerations are nonempty. Because a proper star two-coloring would also be a three-coloring with at most three available names (and can be refined to three used colors without introducing a forbidden bichromatic path), this proves the minimum palette size is exactly four. Alternatively, the absence of two-color solutions can be checked directly with the same recursion.

**Step 3: Recover every named optimum.** Every canonical four-color word uses all four colors. Apply all \(4!=24\) permutations of its four labels. The resulting named words are pairwise distinct: a permutation fixing a surjective word fixes all four symbols. Thus the complete named counts are twenty-four times the canonical counts.

**Step 4: Complete exchange adjacency.** For every named word, try each of its \(|V(G)|\) positions and each of the three alternative symbols, and retain precisely those altered words in the enumerated set. These are exactly the permitted moves. Every undirected edge is encountered twice; halve the directed neighbor count. Discover every connected component by breadth-first search, and recognize each component by its vertices, edge count, and structural degree/inclusion tests. In particular: a connected 3-regular bipartite graph on eight vertices with sides of size four is \(K_{4,4}\) with a perfect matching removed, hence \(Q_3\); the nine-vertex components have a unique degree-four center and the other eight vertices form an alternating degree-two/degree-three cycle, giving \(P_3\square P_3\). The remaining shapes follow directly from size and degree constraints. Counts in the Finding are the precise outputs from these exhaustive checks. There is no heuristic sampling or search cutoff.

**Step 5: Independent enumeration.** The two embedded programs traverse the vertex space in different orders (natural labels versus breadth-first reordered labels), independently form all path constraints, and independently construct/review the recoloring components. They reproduce every number in the claimed decomposition. These are finite computational certificates; no assertion of an infinite-family proof is being made.

## Verification

Run `python3 star_verify.py` and `g++ -O3 -std=c++17 star_cpp.cpp -o star_cpp && ./star_cpp`. Both use standalone graph construction and require no downloadable input data. Their expected terminal outputs, including the concluding `PASS` markers, appear in `verification_output.txt`. The Python program checks the complete nine-vertex component rim-cycle structure, and both programs check the bipartite cube characterization; exhaustive recoloring edges are recomputed from each generated coloring. The graph models were additionally compared with canonical constructions using exact graph isomorphisms during the scientific check. Code execution establishes a fully reproducible finite exhaustive proof, not an independent scholarly audit.

## Relationship to prior work

Albertson, Chappell, Kierstead, Kündgen, and Ramamurthi defined and studied star vertex coloring and proved broad coloring bounds for cubic graphs, not this four-graph optimal recoloring classification. Fertin, Raspaud, and Reed and later subcubic star-coloring results give general upper bounds but do not imply these exact four-color optimum or component data. Ordinary proper vertex-coloring recoloring and star **edge** coloring, including strong edge-coloring trades of the Heawood graph, are different predicates, and their recoloring graphs do not determine the enumerated optimal **star vertex** recolorings. The new claim is the exact finite component classification, not a claim of inventing star coloring.

## Limitations

The theorem is restricted to the four specified named finite graphs and exactly the four named-color optimal palette. Colorings using a larger palette, Kempe recolorings, edge colorings, or unrestricted multi-vertex recolorings are outside scope. Exhaustive programs constitute transparent finite proofs of these exact enumerations but are not substitutes for independent mathematical peer review. The relevant published and searchable research record was examined, yet possible unindexed historical numerical tables and unavailable full papers leave residual publication-priority uncertainty. The cited 2004 publication date identifies an archival source of the underlying notion; it is not a claimed first-ever invention date for the entire modern terminology.

## References

1. M. O. Albertson, G. G. Chappell, H. A. Kierstead, A. Kündgen, R. Ramamurthi, *Coloring with no 2-colored P4's*, Electronic Journal of Combinatorics 11 (2004), R26. DOI: https://doi.org/10.37236/1779. Official journal: https://www.combinatorics.org/ojs/index.php/eljc/article/view/v11i1r26 (published 2004-03-31).
2. A. Fertin, A. Raspaud, B. Reed, *Star coloring of graphs*, Journal of Graph Theory 47 (2004). DOI: https://doi.org/10.1002/jgt.20029.
3. T. Karthick, C. R. Subramanian, *Star coloring of subcubic graphs*, Discussiones Mathematicae Graph Theory 33 (2013). DOI: https://doi.org/10.7151/DMGT.1672.
4. C. M. Mynhardt, S. Nasserasr, *Reconfiguration of Colourings and Dominating Sets in Graphs*, https://arxiv.org/abs/2003.05956 (for context on recoloring, not for the exact star-vertex theorem).
