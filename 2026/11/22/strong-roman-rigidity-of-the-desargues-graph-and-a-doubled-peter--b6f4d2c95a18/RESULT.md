# Strong Roman rigidity of the Desargues graph and a doubled Petersen exchange geometry

## Finding

Let \(G=H(5,2)\) be the graph whose vertices are all two-element and three-element subsets of \(\{0,1,2,3,4\}\). A two-subset is adjacent to a three-subset exactly when it is contained in the latter. The graph has 20 vertices, 30 edges and is cubic.

The strong Roman domination number is
\[\gamma_{\mathrm{StR}}(G)=14.\]
There are exactly **40** minimum-weight functions \(f:V(G)\to\{0,1,2,3\}\). Every one has twelve zeros, two ones and six twos. Both bipartition classes contain exactly one one-label and three two-labels. The two one-labeled vertices are complementary subsets in exactly ten functions; in the other thirty the one-labeled two-subset is contained in the one-labeled three-subset.

Connect two different minimum functions when their 20 labels differ in at most \(k\) positions. No pair differs on fewer than six positions. At \(k=6\), the resulting connected graph has ten degree-six vertices, thirty degree-two vertices and sixty edges, and is the **doubled subdivision of the Petersen graph**: take \(\operatorname{KG}(5,2)\) and replace every edge by two internally vertex-disjoint paths of length two (distinct edges get distinct internal vertices). Its radius is five and its diameter is six. Hence the sharp connectivity threshold is \(k=6\).

## Assumptions and scope

All vertices are labeled and the inclusion representation fixes their coordinates. A strong Roman dominating function is a map \(f:V(G)\to\{0,1,2,3\}\) such that each zero-labeled vertex \(v\) has a neighbor \(u\) with
\[f(u)\ge 1+\left\lceil |N(u)\cap f^{-1}(0)|/2\right\rceil.\]
The weight is \(w(f)=\sum_{v\in V(G)}f(v)\). Hamming distance counts vertices on which two entire labelings differ; all intermediate vertices of the exchange graph must themselves be optimum labelings. No claim is made about other graphs or other reconfiguration rules.

## Proof

**A sharp lower bound.** In any cubic graph on \(n\) vertices, let \(a,b,c,z\) count labels one, two, three, zero. Assign each zero to a qualifying neighbor. A two-label can qualify for at most two zeros and a three-label for at most three. Thus \(z\le 2b+3c\) and \(n\le a+3b+4c\). With \(w=a+2b+3c\), this implies \(3w-2n\ge a+c\ge0\). At \(n=20\), \(w\ge14\). Equality at weight 14 forces \(a+c\le2\); since \(a+3c\) is even, the only four possible triples \((a,b,c)\) are
\[(0,7,0),\quad(2,6,0),\quad(1,5,1),\quad(0,4,2).\]
These four cases are disjoint and exhaustive for weight 14. Hence an exhaustive inspection of them proves the minimum and the full equality classification, not merely a bound.

**Finite exhaustive equality classification.** Represent subsets by five-bit words, in increasing integer order within the two- and three-element shores. The standalone file `verify.cpp` recursively enumerates all ways to assign the specified numbers of one-, two-, and three-labels to twenty vertices; remaining labels are zero. The four cases contain, respectively, \(77{,}520\), \(3{,}527{,}160\), \(3{,}255{,}840\), and \(581{,}400\) assignments: \(7{,}441{,}920\) in total. For each candidate the checker independently evaluates the displayed neighborhood condition for every zero vertex. Precisely forty survive, all in the \((2,6,0)\) case. This simultaneously proves existence and excludes all other weight-fourteen assignments.

**Geometric classification and exchange graph.** The same checker proves that every surviving labeling has exactly one one-label on each shore and exactly three twos on each shore. It verifies directly that the one-label pair is complementary in ten cases and incident in thirty. All two-labeled vertices have exactly two zero neighbors, and all zero-labeled vertices have exactly one two-labeled neighbor.

The ten complementary cases are indexed by their one-labeled two-subset \(A\), with the other one-label at \(A^{c}\). Denote these states \(h_A\). Every incident case has one-labels at \(A\) and \(B^{c}\) for an **ordered pair of disjoint** two-subsets \(A,B\); denote it \(e_{A,B}\). There are exactly thirty such ordered pairs. Direct comparison of the forty complete label strings proves: every Hamming-six pair consists of \(h_A\) and \(e_{A,B}\), or \(h_B\) and \(e_{A,B}\); no other pair has distance six. Consequently each unordered disjoint pair \(\{A,B\}\) has two intermediate configurations \(e_{A,B}\) and \(e_{B,A}\), yielding the doubled subdivision of \(\operatorname{KG}(5,2)\), which is the Petersen graph. Breadth-first search of this explicit forty-vertex graph gives radius five and diameter six. The complete pairwise Hamming-distance distribution (unordered pairs) is \((6:60,\ 8:60,\ 10:180,\ 12:360,\ 14:120)\). In particular the threshold six is sharp.

The independent script `verify_geometry.py` reconstructs the 40 configurations by applying all permutations of the five ground elements to one representative of each type. It validates each label's strong Roman condition from the incidence definition, checks distinctness, and independently recomputes the Hamming graph and its Petersen contraction.

## Verification

Compile and execute `verify.cpp` using `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify`. Run `python3 verify_geometry.py`. Both scripts have no external dependencies. The C++ program exhausts the four possible weight-fourteen label multiplicities, validates every survivor, checks the orbit split, verifies the full pairwise Hamming histogram, and proves the reconfiguration statement by exact adjacency tests. The Python program regenerates the forty configurations from two representatives using the 120 permutations of five points, independently checks admissibility, and verifies the doubled Petersen incidence structure. The printed `PASS` results are assertions backed by explicit executable loops, not substitutes for them.

## Relationship to prior work

Álvarez-Ruiz, González Yero, Mediavilla-Gradolph, Sheikholeslami and Valenzuela-Tripodoro introduced strong Roman domination in a preprint first made public on 13 February 2015. Their definitions, general bounds, complexity results, and tree arguments provide the invariant but not this Desargues-graph equality or reconfiguration classification. The ordinary Roman domination of the Desargues graph is a different optimization model. More recent exact-value results for other graph families do not imply the present forty-state structure or the doubled Petersen exchange geometry. The full accessible prior-text and index comparisons have not ruled out every unindexed finite computation.

## Limitations

This is an exact result about one canonical twenty-vertex graph, rather than an arbitrary cubic or incidence graph. The number forty is supported by a finite exhaustive certificate; the general lower bound is analytic. The two orbit representatives and permutation argument provide a second construction of all forty survivors but alone would not exclude unknown minimizers; the exhaustive C++ search supplies that missing exclusion. No independent scholarly audit or priority certification has been performed.

## References

1. M. P. Álvarez-Ruiz, I. González Yero, T. Mediavilla-Gradolph, S. M. Sheikholeslami, and J. C. Valenzuela-Tripodoro, *On the Strong Roman Domination Number of Graphs*, arXiv:1502.03933, first posted 13 February 2015. https://arxiv.org/abs/1502.03933
2. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera López, and M. P. Álvarez-Ruíz, *Complexity and Exact Values for [k]-Roman and Strong Roman Domination for Specific Graph Families*, Mathematics 14 (2026), 1535. https://doi.org/10.3390/math14091535
