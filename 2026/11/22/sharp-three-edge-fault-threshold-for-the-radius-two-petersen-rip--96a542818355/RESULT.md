# Sharp three-edge fault threshold for the radius-two Petersen Rips complex

## Finding

Let \(P\) be the Petersen graph, represented as the Kneser graph \(KG(5,2)\) on the ten two-subsets of \(\{0,1,2,3,4\}\), adjacent when disjoint. For a set \(F\) of edges, let \(P-F\) retain all ten vertices and delete the indicated edges. When \(P-F\) is connected, give it its **recomputed** shortest-path metric and write \(X_F=\operatorname{VR}_{\le2}(V(P-F),d_{P-F})\).

**Theorem.** For every edge set \(F\) with \(|F|\le2\), the complex \(X_F\) is contractible. Among the \(\binom{15}{3}=455\) three-edge sets, exactly ten disconnect \(P-F\), and the remaining 445 give the following **integral homotopy classification**:

| Homotopy type of \(X_F\) | Number of three-edge sets |
|---|---:|
| Contractible | 380 |
| \(S^2\) | 60 |
| \(\bigvee^4 S^2\) | 5 |

In particular, three deleted edges are necessary and sufficient to create nontrivial radius-two Rips homology while preserving connectedness. All the nonzero reduced integral homology groups occur in degree two, with rank one or four as indicated. No claim about other Rips scales or successive-deletion persistence maps is made.

## Assumptions and scope

The ten vertices, in their fixed order \(v_0,\ldots,v_9\), are the two-subsets

`(0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)`.

An edge is a pair of these **vertex indices** (not a pair of underlying ground-set elements). The fifteen edges are exactly the pairs of disjoint two-subsets. Deleted edges are unordered and distinct. The radius-two complex includes a face if every two of its vertices have recomputed graph distance at most two. The underlying graph must be connected to obtain the stated finite shortest-path metric; the ten disconnected three-edge cases are explicitly excluded from the homotopy table.

## Proof

**Step 1: small fault sets have cone vertices.** Enumerate the \(1+15+105=121\) edge sets of cardinality zero, one or two. For each, perform breadth-first search from each of the ten vertices. In all 121 cases the graph is connected and at least one vertex has distance at most two to all the others. Such a vertex is adjacent in the radius-two graph to every other vertex, so the flag complex \(X_F\) is a cone. The executable enumeration appears in `check_petersen_faults.py`.

**Step 2: orbit partition of every three-edge set.** Every permutation of the five ground-set elements acts on their two-subsets, preserving disjointness and hence the Petersen graph. The \(5!=120\) explicitly generated permutations act on the \(455\) triples of edges. The complete disjoint orbit partition consists of the nine rows below. Each edge written as `ab` denotes the original Petersen edge between indexed vertices \(v_a\) and \(v_b\). The order column specifies the ten pivot vertex indices in the matching described in Step 3.

| Removed-edge representative | Orbit size | Pivot order | Critical cells: vertex, two-faces |
|---|---:|---|---|
| `07 08 09` | 10 | disconnected | — |
| `07 08 15` | 120 | `8 7 3 5 1 2 9 4 0 6` | \((1,0)\) |
| `07 08 19` | 60 | `8 0 4 7 9 3 6 1 5 2` | \((1,0)\) |
| `07 08 26` | 60 | `3 2 0 9 8 7 4 6 1 5` | \((1,0)\) |
| `07 08 28` | 60 | `7 1 4 6 2 9 0 8 5 3` | \((1,0)\) |
| `07 15 24` | 5 | `3 5 8 7 1 4 6 2 9 0` | \((1,4)\) |
| `07 15 26` | 60 | `7 3 0 8 5 4 9 6 2 1` | \((1,1)\) |
| `07 16 28` | 60 | `5 3 4 6 7 9 1 0 2 8` | \((1,0)\) |
| `07 16 58` | 20 | `9 1 6 4 0 7 3 2 5 8` | \((1,0)\) |

For the disconnected orbit, the three deleted edges are exactly the three edges incident to vertex \(v_0\); the generated orbit has ten elements, and breadth-first search independently confirms disconnection for all ten. For the eight connected orbits, their cardinalities sum to 445. The code checks that their images are disjoint and exhaust every three-element subset of the fifteen edges; no assertion about an unverified classification of automorphisms is necessary.

**Step 3: explicit acyclic matchings.** For each connected orbit representative, construct the full nonempty face poset of \(X_F\) by testing all 1,023 possible nonempty subsets against the distance matrix. Starting with all faces unmatched, process the pivot vertices in the row's prescribed order. At pivot \(v\), iterate the remaining faces in increasing bitmask order; whenever a face \(\sigma\) omits \(v\) and both \(\sigma\) and \(\sigma\cup\{v\}\) are still unmatched, match those two faces and remove both from the remaining pool. This gives a valid partial matching on cover relations.

The standalone code constructs **every** Hasse cover relation, directs an unmatched relation from coface to face and reverses a matched relation, then topologically sorts the resulting directed graph. Each of the eight directed graphs is acyclic. It checks the complete remaining critical-face list: precisely one critical vertex, no critical edges, no cells in dimensions three or higher, and respectively zero, one or four critical two-simplices as displayed above. The verifier also checks the full \(120\)-permutation action, exact orbit sizes and disjointness. Thus the eight matching certificates transport to every member of their orbits.

By the acyclic-matching theorem in discrete Morse theory, each \(X_F\) is homotopy equivalent to a CW complex with the specified critical cells. Such a CW complex has one zero-cell, no one-cells and only \(k\) two-cells, all attached to a point. It is exactly a wedge of \(k\) two-spheres (a point when \(k=0\)). This establishes the claimed homotopy types over the integers, not merely a finite-field homology calculation. The orbit counts give 380 contractible, 60 single-sphere and five four-sphere cases.

## Verification

Run `python3 check_petersen_faults.py` with Python 3 (standard library only). The script independently recreates all vertices, edges, group actions and breadth-first-search distance matrices. It tests every small fault pattern, all 455 triple patterns through a complete nine-orbit partition, every face and matched pair in the eight representatives, all directed Hasse cover relations, and the absence of directed cycles. An independent mod-two boundary rank check agrees with the critical-cell counts. The exact output from a fresh execution is in `verification_output.txt`. The homotopy conclusion follows from the integer-valid discrete Morse theorem, rather than being inferred from mod-two ranks.

## Relationship to prior work

Adamaszek–Adams, *On Vietoris–Rips Complexes of Hypercube Graphs* (first arXiv posting 2021-03-01), determines small-scale Rips complexes for **intact binary hypercubes**. The paper motivates the finite graph-metric thickening question but its hypercube formula does not apply to a three-edge-faulted Petersen graph.

Feng–Nukala, *On Vietoris-Rips Complexes of Finite Metric Spaces with Scale 2* (first arXiv posting 2023-02-28), treats layers of the Boolean cube with **symmetric-difference distance**. Its Theorem 10 includes two-subsets of a five-element set, but that metric makes overlapping pairs close and disjoint pairs far. Here disjoint pairs are **graph edges** at distance one, and graph distances are recomputed after deleting those edges. Thus the underlying labels coincide but the metric spaces and their complexes are different; their exact theorem does not imply this fault classification.

Published results on the Petersen **line graph**, the intrinsic graph **Čech** nerve of the intact Petersen graph, and graph-metric Rips complexes of other generalized Petersen graphs were checked for equivalence. Their objects or filtrations differ. No inspected source supplies the nine-orbit edge-fault table or the radius-two homotopy threshold. This is a source-conditional originality assessment, not a proof of global uniqueness.

## Limitations

This is a finite exact classification for at most three edge deletions on the ten-vertex Petersen graph, not a general edge-fault theorem for all regular graphs. The shortest-path metric is computed on the **surviving finite vertex set**; the result does not concern the continuous metric realization of the graph. Graph-disconnecting deletions are excluded. No behavior beyond three deleted edges, no other radii and no inclusion-induced persistence maps are determined. Exhaustive computer checks have a finite, independently replayable input universe; no claim about an infinite family is made. Relevant unindexed or inaccessible equivalent literature is a remaining originality risk.

## References

1. M. Adamaszek and H. Adams, *On Vietoris–Rips Complexes of Hypercube Graphs*, arXiv:2103.01040, first posted 2021-03-01. https://arxiv.org/abs/2103.01040
2. Z. Feng and N. C. P. Nukala, *On Vietoris-Rips Complexes of Finite Metric Spaces with Scale 2*, arXiv:2302.14664, first posted 2023-02-28. https://arxiv.org/abs/2302.14664
3. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145. Standard acyclic-matching theorem used in Step 3.
