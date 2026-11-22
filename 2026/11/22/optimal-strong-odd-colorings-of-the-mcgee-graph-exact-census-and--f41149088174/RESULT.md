# Optimal strong odd colorings of the McGee graph: exact census and symmetry classes

## Finding

Let \(M\) denote the 24-vertex cubic McGee graph, the unique \((3,7)\)-cage. Then
\[
\chi_{\mathrm{so}}(M)=5.
\]
There are exactly \(1304\) distinct optimal color-class partitions, or \(1304\cdot5!=156480\) five-colorings with five distinct named colors. The full minimum-color census by nondecreasing class-size vector is

| Color-class sizes | Unnamed partitions |
| --- | ---: |
| \((2,4,4,7,7)\) | 16 |
| \((2,5,5,5,7)\) | 48 |
| \((3,3,4,7,7)\) | 96 |
| \((3,4,5,5,7)\) | 336 |
| \((4,4,4,5,7)\) | 400 |
| \((4,5,5,5,5)\) | 408 |
| **Total** | **1304** |

The graph automorphism group has order \(32\), and it partitions the \(1304\) optima into \(54\) orbits: five orbits of size \(8\), nineteen of size \(16\), and thirty of size \(32\). Precisely \(320\) optimal partitions are proper colorings of the square graph \(M^2\) (every vertex sees three distinct neighbor colors); the remaining \(984\) are not square colorings. These figures together constitute one complete classification of the optimal strong odd colorings of \(M\).

## Assumptions and scope

A strong odd coloring of a simple graph \(G\) is a proper vertex coloring \(c\) for which each color occurring among the neighbors of any vertex occurs an odd number of times. Colors are *named* when permutations of the palette count separately and *unnamed* when a coloring means the partition into nonempty color classes. The square graph \(G^2\) joins vertices at distance one or two.

For exact reproducibility, take vertex set \(\mathbb Z/24\mathbb Z\). Include each cycle edge \(\{i,i+1\}\) and each chord \(\{i,i+\delta_i\}\), with indices modulo \(24\) and the periodic displacement word \((\delta_0,\delta_1,\delta_2)=(12,7,-7)\). This is the McGee graph in its standard LCF representation (the first displacement is also written \(-12\), the same modulo \(24\)). The graph has \(36\) distinct edges, degree \(3\), girth \(7\), and automorphism order \(32\).

## Proof

**Local equivalence.** In a cubic graph, the three colors on the neighbors of any vertex must be either all identical or all distinct: the only partitions of three into positive odd multiplicities are \((3)\) and \((1,1,1)\). Equivalently, each nonempty color class \(S\) must be independent and intersect every open neighborhood in \(0,1,\) or \(3\) vertices, never in two. Conversely, any partition into such independent classes is a strong odd coloring.

**Complete exact enumeration.** The two independent exhaustive programs in the verification artifacts enumerate the finite object specified above. The first assigns colors in restricted-growth order, introduces at most one new color per recursive step, and uses the local cubic equivalence to prune choices: for a partially colored neighborhood, two equal colors force the third to equal them, whereas two different colors forbid both those colors at the third position. Every uncolored vertex receives every still feasible color in the recursive search, and a canonical relabeling by first appearance identifies each unnamed coloring with exactly one leaf. That search returns \(0\) feasible partitions on a palette of size \(4\), and \(1304\) on a palette of size \(5\).

Independently, the second program recursively generates **all** subsets \(S\subseteq V(M)\), retaining exactly those that are independent and have \(|S\cap N(v)|\ne2\) for every vertex \(v\). An exact-cover recursion chooses the least currently uncovered vertex and tries each retained class containing it and wholly contained in the uncovered set. This chooses the first class in a unique order determined by the remaining vertices, hence enumerates every unordered color-class partition exactly once. Its partition counts for \(k=2,3,4,5\) are respectively \(0,0,0,1304\). Its list of \(1304\) five-class partitions agrees *exactly as a set* with the first algorithm's list. Every branch is finite and no random sampling or time cutoff is used.

As \(M\) contains edges, one color cannot work. There are no strong odd colorings on fewer than five colors by the exact-cover enumeration; a five-color witness, in vertex order \(0,1,\ldots,23\), is the string `010102310143142032010341` (digits denote colors \(0\) through \(4\)). The exhaustive enumerations thus prove the chromatic minimum and the count. The listed distribution of color-class sizes is obtained by sorting the sizes of the five classes for each certified partition.

**Automorphism and square-coloring classification.** Enumerate all bijections \(g:V(M)\to V(M)\) preserving the specified edge set; the included graph-isomorphism enumeration returns all \(32\), agreeing with the standard graph description. Transform each five-class partition under these permutations, and merge all partitions in each orbit. The resulting orbit cardinalities are \(5\times8+19\times16+30\times32=1304\), establishing \(54\) orbits. For each partition, check whether all three neighbors of each of the \(24\) vertices have distinct colors. Exactly \(320\) pass, giving the stated square-coloring split.

## Verification

The package includes `search_colorings.cpp`, `exact_cover.cpp`, `analyze_orbits.py`, and `search_colorings_5.txt`. Compile the C++ sources with a conforming C++17 compiler and run:

```sh
g++ -O2 -std=c++17 search_colorings.cpp -o search_colorings
g++ -O2 -std=c++17 exact_cover.cpp -o exact_cover
./search_colorings 4
./search_colorings 5
./exact_cover
python3 analyze_orbits.py
```

The Python verification requires NetworkX and asserts that the two independently produced lists of \(1304\) unlabeled partitions agree exactly, that the automorphism group has size \(32\), and that the claimed symmetry statistics are reproduced. The provided `search_colorings_5.txt` is the complete 1304-line canonical-coloring certificate from the first enumeration; rerunning the first program recreates it as `search_colorings_5.txt`.

## Relationship to prior work

Kwon and Park introduced strong odd coloring in their January 22, 2024 preprint and studied structural bounds based on maximum average degree. Caro, Petruševski, Škrekovski, and Tuza subsequently obtained results for planar classes, trees, unicyclic graphs, and products. These establish the definition and broad bounds but do not give the above McGee-graph count in the inspected texts. The McGee graph's basic 24-vertex, girth-seven, chromatic-three structure is classical. The numerical claim here concerns the strong odd optimum and its complete partition census, not the classical graph properties or the definition of strong odd coloring. The 320-coloring square subfamily is compared explicitly so it is not conflated with the full strong odd enumeration.

## Limitations

This is a finite exhaustive theorem for the explicitly presented 24-vertex graph, not a claim for all cubic graphs or all cages. The enumeration is an ordinary computational proof requiring faithful execution of the supplied programs and interpretation of exhaustive branch coverage; independent mathematical audit has not been performed. Absence of an equivalent result in inspected literature and research indexes is not an absolute historical priority certificate. Changes to the graph representation or coloring definition would require a new check.

## References

1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653, first posted 2024-01-22. https://arxiv.org/abs/2401.11653
2. Y. Caro, M. Petruševski, R. Škrekovski, and Zs. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336, first posted 2024-10-03. https://arxiv.org/abs/2410.02336
3. E. W. Weisstein, *McGee Graph*, Wolfram MathWorld. https://mathworld.wolfram.com/McGeeGraph.html
