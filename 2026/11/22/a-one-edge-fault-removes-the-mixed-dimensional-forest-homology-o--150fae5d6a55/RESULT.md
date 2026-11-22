# A one-edge fault removes the mixed-dimensional forest homology of the three-cube

## Finding
Let \(Q_3\) be the ordinary three-dimensional cube graph, and let \(H=Q_3-e\) be obtained by deleting any one graph edge. Let \(\mathcal F_d(H)\) be the simplicial complex of vertex subsets whose induced subgraph is acyclic and of maximum degree at most \(d\). For all nonnegative integers \(d\), including the unrestricted stage \(d=\infty\), the complete integral homotopy classification is
\[
\mathcal F_d(H)\simeq
\begin{cases}
S^1\vee S^1,&d=0,\\
S^2,&d=1,\\
\bigvee^3S^4,&d\ge2.
\end{cases}
\]
Moreover, the actual inclusion \(\mathcal F_2(H)\hookrightarrow\mathcal F_3(H)=\mathcal F_\infty(H)\) is a simple-homotopy equivalence: ten specified elementary collapses reduce the latter complex to the former.

The intact cube is the crown graph \(K_2\times K_4\); its degree-two stage is already known to be \(S^3\vee\bigvee^4S^4\). Thus removing a single cube edge changes the degree-two homotopy type to three four-spheres, eliminating the degree-three class and lowering fourth Betti rank by one. No assertion about the inclusion-induced homology maps from the intact to the faulty graph is made.

## Assumptions and scope
Identify the vertices with integers \(0,1,\ldots,7\), representing binary triples, with an edge between distinct \(u,v\) precisely when their binary strings differ in one coordinate. Because cube automorphisms are transitive on the twelve edges, it suffices to remove the edge \(\{0,1\}\). Graphs are simple and undirected. A nonempty mask \(m\in\{1,\ldots,255\}\) represents the vertex subset whose bit positions equal one. A face is admitted if the induced edge graph has no cycle and every induced degree is at most \(d\). For the faulty graph the ambient maximum degree is three; hence all \(d\ge3\) give the unrestricted forest complex.

This is a complete classification for the single-edge-fault isomorphism class of the eight-vertex cube, not a formula for all hypercubes or all edge deletions of crown graphs.

## Proof
**Face census.** Enumerate all \(2^8\) masks, independently evaluating the induced-degree constraint and acyclicity with union–find. A second implementation uses depth-first search with the graph-theoretic identity \(e=v-c\) for acyclic finite graphs (where \(c\) is the number of components). The resulting face vectors (numbers of nonempty simplices in dimensions \(0,1,\dots\)) are
\[
\begin{array}{c|l}
d& f_0,f_1,\ldots\\\hline
0&(8,17,10,2)\\
1&(8,28,36,14)\\
2&(8,28,56,60,30,2)\\
3&(8,28,56,66,40,6).
\end{array}
\]

**Acyclic face matchings.** For each of the four stages, run the following deterministic partial matching on its nonempty face set \(F\). Initialize all faces unmatched. Process vertex labels \(v=0,1,\ldots,7\). For each such vertex and each mask \(m\) in increasing numerical order, if both \(m\) and \(m\cup\{v\}\) are currently unmatched faces and \(v\notin m\), match the pair. Orient every cover relation in the face-poset Hasse diagram downward except matched covers, which are oriented upward. Exact topological sorting of the resulting complete directed incidence graph verifies its acyclicity for each of the four finite complexes. The counts of matched pairs are respectively \(17,42,90,100\). The critical cells are, respectively:
\[
\begin{array}{c|l}
d&\text{critical dimensions with multiplicity}\\\hline
0&\{0:1,1:2\}\\
1&\{0:1,2:1\}\\
2&\{0:1,4:3\}\\
3&\{0:1,4:3\}.
\end{array}
\]
By discrete Morse theory, the geometric realization of each complex is homotopy equivalent to a CW complex with precisely these critical cells. Each model contains one zero-cell, no one-cells except in the first case, and cells only in one positive dimension. Each positive-dimensional cell is therefore attached by a constant map to the zero-skeleton, yielding exactly the wedge of spheres stated above, integrally, without any reliance on homology ranks alone.

**The stabilization map.** The ten free-face and unique-coface pairs in the successive relative collapses from degree three to degree two are, in hexadecimal mask representation,
```
(0x4f,0x6f) (0x73,0x7b) (0x8f,0x9f) (0xb3,0xb7)
(0x4d,0x6d) (0x71,0x79) (0x8e,0x9e) (0xb2,0xb6)
(0xd4,0xd6) (0xe8,0xe9)
```
After every pair is removed, the first face has precisely one strict coface remaining and it is the stated second face, of one greater dimension. The two removed faces lie outside \(\mathcal F_2(H)\). Exhaustively checking the remaining faces gives precisely \(\mathcal F_2(H)\). Hence the displayed inclusions are related by genuine elementary simplicial collapses.

## Verification
Run `python3 verify_edgefault.py` with Python 3.10 or later and the standard library. The script builds the cube and deletes exactly the edge \(\{0,1\}\), independently checks every admitted face through two cycle detectors, verifies all acyclic matching reversals by a topological sort over the complete face-poset Hasse graph, compares the exact critical cells against the statement, and reproduces all ten relative elementary-collapse pairs. Recorded console output is in `verification_output.txt`. The run terminates with `ALL_CHECKS_PASS`. Exhaustive calculations apply to this eight-vertex graph only; the reduction to any deleted edge uses graph edge transitivity, not finite sampling.

## Relationship to prior work
Carnero Bravo, *The Forest Filtration of a Graph* (first public version 2023-07-25), establishes the filtration and in Lemma 40 and Proposition 41 classifies the intact crown graphs \(K_2\times K_n\) for every number of labels, including \(Q_3\cong K_2\times K_4\). Those theorems do not apply to the non-regular edge-deleted graph \(Q_3-e\). The original intact degree-two homotopy type is previous knowledge, not a new assertion here.

The published 2026 bipartite one-edge forest theorem addresses deletion from a **complete bipartite** graph \(K_{a,b}\) and proves two-connectivity for other bipartite subgraphs; it supplies no homotopy classification of these degree-bounded damaged-crown stages. The separate published crown-graph integral-module classification applies to the intact graph, not to the fault. Searches for edge-fault cube, damaged crown graphs, forest degree constraints and equivalent formulations found no covering formula. An unindexed equivalent computation remains possible.

## Limitations
No classification is claimed for \(Q_n-e\) when \(n\ne3\), for multiple missing edges, or for the map in homology from \(Q_3\) to \(Q_3-e\). The result concerns absolute integral homotopy types and the final internal stabilization inclusion. The proof is an exhaustive finite certificate for a natural fixed graph, not an inductive theorem for larger graph classes. Originality remains subject to unindexed or inaccessible prior literature. Independent mathematical audit has not been performed.

## References
1. A. Carnero Bravo, *The Forest Filtration of a Graph*, arXiv:2307.13271, first public submission 2023-07-25, especially Lemma 40 and Proposition 41, https://arxiv.org/abs/2307.13271.
2. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
3. *A one-edge homotopy transition for induced-forest complexes of bipartite graphs* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-one-edge-homotopy-transition-for-induced-forest-complexes-of-b--e5b294bc3a20.
4. *Integral symmetry modules of crown-graph induced-forest complexes* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-integral-symmetry-modules-of-crown-graph-induced-forest-complexe--254ef80c8528.
