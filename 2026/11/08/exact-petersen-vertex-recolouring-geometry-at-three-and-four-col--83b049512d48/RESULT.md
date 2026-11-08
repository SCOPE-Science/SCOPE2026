# Exact Petersen vertex-recolouring geometry at three and four colours

## Finding
Let \(P=\operatorname{KG}(5,2)\) be the Petersen graph, with its ten vertices the two-element subsets of \(\{0,1,2,3,4\}\), adjacent precisely when disjoint. For \(k\in\{3,4\}\), let \(R_k(P)\) have as vertices all proper assignments of the individually named colours \(\{0,\ldots,k-1\}\) to \(V(P)\); two assignments are adjacent if they differ at precisely one vertex. Colours need not all be used.

**Finite classification theorem.** The three-colour graph is \(R_3(P)\cong 60K_2\). The four-colour graph has \(12{,}960\) vertices and \(53{,}280\) edges, is connected, and satisfies
\[
\operatorname{rad}(R_4(P))=13,\qquad \operatorname{diam}(R_4(P))=14.
\]
Precisely \(3{,}360\) four-colourings have eccentricity \(13\), and precisely \(9{,}600\) have eccentricity \(14\). Exactly \(44{,}400\) unordered pairs are at distance \(14\). The complete distance-count vector for *unordered* distinct pairs at distances \(1,\ldots,14\), respectively, is
\[
(53{,}280,230{,}400,712{,}320,1{,}761{,}120,3{,}643{,}320,
6{,}485{,}040,10{,}147{,}920,13{,}978{,}920,16{,}470{,}960,
15{,}343{,}920,10{,}156{,}080,4{,}113{,}840,832{,}800,44{,}400).
\]

Under the graph-automorphism and named-colour-permutation action, the four-colour configurations form exactly eleven orbits. Using the vertex order \(01,02,03,04,12,13,14,23,24,34\), the following table lists a representative digit word, its orbit cardinality, eccentricity, and number of configurations at that eccentricity from any orbit member. Digit words are encodings, not unnamed-colour quotients.

| Representative | Orbit size | Eccentricity | Outermost shell |
|---|---:|---:|---:|
| `0000111222` | 480 | 13 | 131 |
| `0000111223` | 1,440 | 13 | 59 |
| `0000112123` | 1,440 | 14 | 2 |
| `0000112323` | 960 | 13 | 79 |
| `0001221213` | 1,440 | 14 | 13 |
| `0001221233` | 1,440 | 14 | 18 |
| `0001221313` | 2,880 | 14 | 4 |
| `0001221333` | 1,440 | 14 | 7 |
| `0001222311` | 480 | 13 | 88 |
| `0001223233` | 240 | 14 | 13 |
| `0011022331` | 720 | 14 | 23 |

## Assumptions and scope
Graphs are finite, simple and undirected. Vertex labels and colour names are fixed. The Petersen graph here is the Kneser graph on two-subsets of a five-element set; this removes possible ambiguity with its ten-vertex circular drawings. Recolourings change one vertex to another colour in the same palette and keep all fifteen edges properly coloured. Distances and eccentricities refer to this *single-vertex* recolouring graph, not to Kempe-chain swaps, proper edge-colourings, or the ordinary graph distance in \(P\).

The result makes an exact assertion about this one canonical ten-vertex graph. The known chromatic-polynomial values \(120\) and \(12{,}960\), and the general subcubic recolouring connectivity theorem, are not claimed as new.

## Proof
**Exhaustive finite proof with two independently structured implementations.** There is no approximation or statistical inference in the finite steps below.

1. Construct the vertices in the lexicographic order above. The simple edge test is set disjointness, producing exactly fifteen edges and degree three at each of the ten vertices. For each palette size \(k\), enumerate every word of length ten over its \(k\) symbols and retain exactly those words whose entries differ on all fifteen edges. The C++ implementation scans all \(4^{10}=1{,}048{,}576\) two-bit words and filters the three-colour subcase. Its output gives \(120\) three-colour and \(12{,}960\) four-colour words. The independent Python program instead uses incremental proper-colouring backtracking, and obtains the same state counts.
2. For every retained word \(c\), examine every coordinate \(i\) and every replacement symbol different from \(c(i)\). Keep the replacement if none of the three neighbours of \(i\) has that symbol. This constructs *all and only* the legal undirected recolouring edges: every permissible one-coordinate difference is considered, and the reverse change is also permissible. The C++ program verifies reverse edges explicitly. The degree sum is \(120\) for \(k=3\) and \(106{,}560\) for \(k=4\), yielding \(60\) and \(53{,}280\) undirected edges respectively. In the three-colour case every state has degree one; symmetry of adjacency therefore gives \(60\) components, each a two-vertex edge.
3. The C++ program performs breadth-first search from **every** one of the \(12{,}960\) four-colour states, using the explicit graph. Each search reaches all states, proving connectivity; each search's farthest distance is exactly \(13\) or \(14\). It counts \(3{,}360\) states with eccentricity \(13\) and \(9{,}600\) with eccentricity \(14\). Counting an unordered pair only when its target index exceeds its source index gives the displayed distance vector, summing to \(\binom{12{,}960}{2}=83{,}974{,}320\). In particular, the last entry proves there are \(44{,}400\) pairs at the maximum distance, and no distance exceeds \(14\).
4. An independent symmetry reduction checks the same results. The action of the symmetric group on the five underlying points induces \(120\) graph automorphisms, and all \(24\) permutations of the four named colours preserve recolouring distances. Canonicalising each word by renaming its first encountered colour as \(0\), its next new colour as \(1\), and so forth yields \(540\) canonical proper four-colouring words. Every canonical word uses three or four colours, hence has exactly \(24\) distinct named-colour realisations. Applying the \(120\) graph automorphisms partitions these \(540\) words into eleven orbits; multiplying their canonical sizes by \(24\) gives the orbit sizes in the table. Breadth-first search from one representative of each orbit produces the listed eccentricities. Weighting each distance shell by the orbit size and dividing by two reproduces the independently calculated unordered-pair distribution. This argument proves that no unsearched vertex can have a different eccentricity, because the two symmetry actions are isometries.

For an explicit sharp witness, the following legal sequence uses the indicated vertex and colour encoding. Consecutive words differ in one position and the initial and final words have distance \(14\), as checked independently by both breadth-first search methods:

```text
3222111000 -> 1222111000 -> 1232111000 -> 1233111000
-> 1233111003 -> 1033111003 -> 1033011003 -> 1033021003
-> 1031021003 -> 1031022003 -> 1011022003 -> 1011022303
-> 1011022333 -> 0011022333 -> 0011022331
```

## Verification
The two required, standalone source files are `verify_exhaustive.cpp` and `verify_orbits.py`. Compile the former using `g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive` and run `./verify_exhaustive`. Run the latter using `python3 verify_orbits.py` (standard library only). Both reconstruct the graph from the Kneser definition, without external inputs, databases or files.

The first implementation performs exhaustive all-source breadth-first searches and checks edge reversibility, state counts and aggregate pair counts. The second independently generates proper colourings by backtracking, applies \(S_5\) vertex permutations and colour canonicalisation, checks all eleven orbit representatives, and reconstructs the aggregate pair counts from orbit-weighted distance shells. They agree on all claimed numbers. The complete algorithms, not only their output logs, are part of the proof of this finite classification.

## Relationship to prior work
Cereceda, van den Heuvel and Johnson establish the general three-colouring reconfiguration framework and a connectivity criterion; the exact two-vertex components here are an elementary special census, not the principal novelty claim. Bonamy and Bousquet give general mixing and diameter bounds via treewidth and the Grundy number. Johnson, Kratsch, Kratsch, Patel and Paulusma study the algorithmic complexity of shortest recolouring paths. Most directly, Feghali, Johnson and Paulusma prove that the \((\Delta+1)\)-colouring graph of a connected graph of maximum degree at least three has isolated frozen colourings and at most one additional component, with a polynomial diameter bound. Thus general **connectivity structure** at four colours is prior theory and is not claimed as a new general theorem.

The proposed new contribution is the **sharp exact metric** for this particular graph: radius \(13\), diameter \(14\), the eccentricity counts, eleven orbit profiles, and the exact pair-distance spectrum. These are not numerical consequences of the cited polynomial bounds or the classical chromatic polynomial. No matching complete Petersen-specific metric classification was identified in the inspected primary texts or targeted searches; this is qualified evidence, not a proof that no earlier calculation exists.

## Limitations
This is a finite, computer-verifiable theorem about the ten-vertex Petersen graph only. It does not establish analogous values for arbitrary cubic graphs, Kneser graphs, or graph-colouring sampling times. The two implementations are different enumeration and reduction methods but are not independent human audits. Historical novelty is qualified: a specialized, unpublished or unindexed prior enumeration might exist, and the month-dated 2007 research report supplies no verified day of first release. The earliest fully date-specific cited online publication used for the archival source metadata is December 16, 2010; no day is inferred for the 2007 report.

## References
1. L. Cereceda, J. van den Heuvel and M. Johnson, *Finding Paths Between 3-Colourings*, CDAM Research Report LSE-CDAM-2007-31 (December 2007, month-level evidence); *Journal of Graph Theory* 67 (2011), 69–82; first online December 16, 2010. DOI: 10.1002/jgt.20514. Full research report: https://matthewjohnsondurham.github.io/papers/cdam-2007-31.pdf.
2. M. Bonamy and N. Bousquet, *Recoloring bounded treewidth graphs*, arXiv:1302.3486, initial public submission February 14, 2013; https://arxiv.org/abs/1302.3486.
3. M. Johnson, D. Kratsch, S. Kratsch, V. Patel and D. Paulusma, *Finding Shortest Paths between Graph Colourings*, arXiv:1403.6347, initial public submission March 25, 2014; https://arxiv.org/abs/1403.6347.
4. C. Feghali, M. Johnson and D. Paulusma, *A Reconfigurations Analogue of Brooks' Theorem and its Consequences*, arXiv:1501.05800, initial public submission January 23, 2015; https://arxiv.org/abs/1501.05800.
5. P. J. Cameron, *Counting colourings of graphs*, April 12, 2012; https://cameroncounts.wordpress.com/2012/04/12/counting-colourings-of-graphs/ (records the known Petersen chromatic-polynomial values).
