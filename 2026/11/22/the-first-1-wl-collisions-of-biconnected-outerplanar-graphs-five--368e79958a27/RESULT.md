# The first 1-WL collisions of biconnected outerplanar graphs: five doublets at ten vertices

## Finding

For \(n\ge 3\), let \(\mathcal B_n\) be the set of isomorphism classes of simple biconnected (2-connected) outerplanar graphs with exactly \(n\) vertices. Give every vertex the same initial color and run the ordinary one-dimensional Weisfeiler--Leman algorithm (1-WL, or color refinement), comparing graphs by the exact stable color histograms computed in their disjoint union.

**Exact finite theorem.** For \(3\le n\le9\), no two nonisomorphic graphs in \(\mathcal B_n\) are 1-WL equivalent. At \(n=10\), the \(1117\) graph isomorphism types have exactly \(1112\) distinct 1-WL signatures, consisting of five doubletons and \(1107\) singletons. In particular, the least order for a biconnected outerplanar intergraph color-refinement collision is ten.

The complete ten-vertex list, in the canonical chord-mask convention defined below, is:

| Pair | First graph | Second graph |
| --- | --- | --- |
| 1 | `0x8020` | `0x100040` |
| 2 | `0x8028` | `0x100048` |
| 3 | `0x108060` | `0x20100041` |
| 4 | `0x108068` | `0x20100049` |
| 5 | `0x128060` | `0x20120041` |

The numerical counts of graph types at each order are classical; the claims here are the *sharp 1-WL cutoff and its complete equivalence-class census*, not the known outerplanar isomorphism counts or the existence of some ten-vertex ambiguous pair.

## Assumptions and scope

All graphs are finite, simple, undirected and have at least three vertices. Biconnected means that deletion of any vertex leaves a connected graph. Outerplanar means embeddable with all vertices on the outer face. These hypotheses imply a **unique Hamiltonian outer-face cycle**. Consequently, up to isomorphism, every graph in \(\mathcal B_n\) is exactly a cyclic outer polygon with a set of pairwise noncrossing diagonals, identified up to the \(2n\) rotations and reversals of the polygon.

Label its outer cycle \(0,1,\ldots,n-1,0\). List all possible chord pairs \((i,j)\) with \(0\le i<j<n\), \(j-i>1\), excluding \((0,n-1)\), in lexicographic order. The integer bit mask for a chord set has bit \(t\) set exactly when the \(t\)-th listed chord is present. Represent an isomorphism class by its *minimum integer bit mask* over all dihedral relabellings. The displayed five pairs use this convention, at \(n=10\).

For a family of graphs, start with one global color for every vertex of their disjoint union. At each round, the new color of a vertex is an injective encoding of the pair consisting of its previous color and the multiset of neighbor colors. Two graphs are 1-WL equivalent precisely if their color histograms agree after stabilization of this common refinement.

## Proof

**Step 1 (exhaustive isomorphism representatives).** For each \(3\le n\le10\), the verifier constructs the complete finite set of possible chords. Two distinct chords \((a,b)\) and \((c,d)\) intersect in their interiors exactly when their endpoints alternate in the cyclic order, expressed in increasing-label coordinates by \(a<c<b<d\) or \(c<a<d<b\). Its recursion visits each chord once: omit it, or include it if none of its crossing chords has been included. Induction on the recursion index proves that every noncrossing chord subset occurs at exactly one leaf and no crossing subset occurs. Taking the minimum under all rotations and reflections gives exactly one canonical representative of every isomorphism class: every isomorphism preserves the *unique* outer Hamiltonian cycle, so it is a dihedral relabelling.

**Step 2 (exact color-refinement equivalence).** Build the adjacency-bitset graph of each canonical representative. Run refinement on the disjoint union of these graphs. For every vertex store the exact key consisting of the previous color and the sorted tuple of neighbor colors. Sort the finite set of distinct keys and give each key its integer rank. This is an **injective exact encoding**, with no random hashing, floating-point approximation, or representation collisions. Repeating until the color vector stops changing computes the stable equitable refinement. The sorted color vector on each graph is its exact stable histogram. Grouping graphs by this histogram partitions the complete representative set into precisely the 1-WL equivalence classes: any differing histogram distinguishes its graphs, whereas equal histograms mean refinement could not distinguish them by definition. Termination is observed for all of these enumerated graphs; no extrapolation beyond ten vertices is needed.

**Step 3 (complete exact counts and witnesses).** Running the included standalone enumerator reports:

| Number of vertices | Polygon chord subsets | Isomorphism classes | 1-WL classes | Ambiguous unordered pairs |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 1 | 1 | 1 | 0 |
| 4 | 3 | 2 | 2 | 0 |
| 5 | 11 | 3 | 3 | 0 |
| 6 | 45 | 9 | 9 | 0 |
| 7 | 197 | 20 | 20 | 0 |
| 8 | 903 | 75 | 75 | 0 |
| 9 | 4279 | 262 | 262 | 0 |
| 10 | 20793 | 1117 | 1112 | 5 |

At ten vertices each non-singleton class contains exactly two canonical graph masks, and these are exactly the five pairs above. For each pair, an independently written two-graph refinement routine confirms identical color histograms through stabilization. The masks of the two graphs in every pair are distinct canonical dihedral representatives and therefore give nonisomorphic graphs. The complete search proves no missing class or smaller counterexample exists within the stated domain.

## Verification

Run `python3 verify.py` with Python 3 and its standard library; no datasets or other dependencies are required. The included `PAIRS.json` records the input conventions and the five witness pairs. The verifier generates all graphs afresh rather than trusting the JSON list. Its printed results include `ORDER_10 RAW_20793 ISOMORPHISM_TYPES_1117 CR_CLASSES_1112 COLLISION_PAIRS_5 PASS`, all five pair checks and `VERIFY_OK`. A separate implementation using NetworkX's Weisfeiler--Leman graph hashing was used as an auxiliary cross-check of the class counts, not as the exact certificate.

The source code, recursion, canonicalization, refinement-key construction and full loop bounds are visible in `verify.py`. Its exhaustive check spans every graph in the finite domain, not a sample. The proof's mathematical reduction from biconnected outerplanar graphs to polygonal chord sets is essential to its completeness.

## Relationship to prior work

Coste, Csikós and Viennot (2026) prove that coloring one vertex as a root suffices for 1-WL to distinguish connected rooted outerplanar graphs. Their Figure 1 **already gives** a nonisomorphic ten-vertex biconnected outerplanar pair not distinguished by *unrooted* color refinement. We do **not** claim this example or the general rooted theorem as new; the exact first-failure cutoff and *all five* ten-vertex pairs are the contribution here. Bause, Jogl, Welke and Thiessen (2023) discuss graph transformations using outerplanar unique Hamiltonian cycles, not this untransformed ten-vertex 1-WL enumeration. Bodirsky, Fusy, Kang and Vigerske (2007) determine classical outerplanar graph counts, which are not a count of 1-WL equivalence classes. An earlier mathematical study of biconnected outerplanar graphs identifies order-eight failures of **vertex-orbit recovery** by color refinement. Orbit recovery within a single graph and 1-WL distinguishing **two different graphs** are logically different properties; an order-eight orbit failure does not imply an order-eight intergraph ambiguity.

## Limitations

The claim is restricted to simple, biconnected, unrooted outerplanar graphs of order at most ten; it says nothing about all connected outerplanar graphs, about color refinement recovering automorphism orbits, or about orders greater than ten. The complete finite census is verified by executable code rather than a separately formalized proof of the program. Published and indexed sources were checked, but unindexed earlier computational tabulations may contain equivalent counts. Independent mathematical validation has not been performed.

## References

1. L. Coste, M. Csikós, L. Viennot, *Color Refinement Distinguishes Connected Rooted Outerplanar Graphs*, arXiv:2611.18391v1, first posted 2026-11-13, https://arxiv.org/abs/2611.18391v1. Relevant material: Section 1.2, Figure 1, and the rooted reconstruction theorem.
2. F. Bause, F. Jogl, P. Welke, M. Thiessen, *Maximally Expressive GNNs for Outerplanar Graphs*, Learning on Graphs (2023), https://doi.org/10.34726/5434. Relevant material: initial sections and unique Hamiltonian cycle based graph transformation.
3. M. Bodirsky, É. Fusy, M. Kang, S. Vigerske, *Enumeration and Asymptotic Properties of Unlabeled Outerplanar Graphs*, Electronic Journal of Combinatorics 14 (2007), R66, https://doi.org/10.37236/984.
4. Colbourn and Booth (1981), uniqueness of the Hamiltonian cycle in biconnected outerplanar graphs, as discussed in the papers above.
