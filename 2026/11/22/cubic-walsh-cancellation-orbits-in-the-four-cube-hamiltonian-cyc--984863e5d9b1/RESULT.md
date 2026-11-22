# Cubic Walsh cancellation orbits in the four-cube Hamiltonian cycle codebook

## Finding

Let \(Q_4\) be the graph whose vertices are the four-bit strings, represented by the integers \(0,\ldots,15\), and whose edges join vertices with Hamming distance one. It has 32 edges. Let \(\mathcal H\) be the collection of its undirected, unrooted Hamiltonian cycles, counted once per 16-edge incidence set. For an edge set \(S\), put

\[
W(S)=\sum_{C\in\mathcal H}(-1)^{|C\cap S|}.
\]

**Theorem.** There are precisely \(1344\) such Hamiltonian cycles. All 32 one-edge Walsh coefficients vanish, none of the \(496\) two-edge coefficients vanish, and exactly \(1120\) of the \(4960\) three-edge coefficients vanish. The 1120 cancelling triples comprise six orbits under the full cube-automorphism group \(\mathbb F_2^4\rtimes S_4\), of respective sizes \(64,96,192,192,192,384\). Exactly 64 of them arise by replacing a one-edge frequency with the complementary three-edge subset of a four-edge vertex star. The remaining 1056 are not obtained from one-edge frequencies by any even-cut equivalence of support size at most four.

The full two-edge coefficient distribution, with notation `coefficient: number of supports`, is

```
-448: 96; -216: 48; -56: 96; 136: 192; 168: 16; 176: 48
```

The full three-edge distribution is

```
-120: 64; -56: 96; -40: 192; -32: 384; -24: 32;
-16: 1152; 0: 1120; 16: 1152; 24: 192; 32: 384; 88: 192
```

For orbit representatives, order the 32 edges lexicographically by their integer endpoints \((u,v)\) with \(u<v\). The six zero-orbit representatives, written as lists of three edges, are:

| Orbit size | Edge representative |
|---:|---|
| 64 | \((0,1),(0,2),(0,4)\) |
| 96 | \((0,1),(2,3),(12,14)\) |
| 192 | \((0,1),(0,2),(7,15)\) |
| 192 | \((0,1),(0,2),(13,15)\) |
| 192 | \((0,1),(2,6),(13,15)\) |
| 384 | \((0,1),(2,6),(11,15)\) |

The six pair-support orbits have coefficient–orbit-size pairs \((-448,96),(-216,48),(-56,96),(136,192),(168,16),(176,48)\). Altogether, the \(4960\) triple supports form 24 symmetry orbits, exactly six of which have zero coefficient.

## Assumptions and scope

Every cycle is a connected, spanning, 2-regular undirected subgraph of \(Q_4\); its traversal direction, its initial vertex, and cyclic shifts of its vertex list do not create new cycles. The Fourier group is the additive Boolean edge cube \((\mathbb F_2)^{32}\). Its Walsh characters are indexed by edge subsets. Coefficients are **unnormalized** integer sums over Hamiltonian cycles. The statements above concern all and only characters with support size one, two, or three. No restriction to coordinate-axis change-number classes is imposed.

## Proof

**Step 1: complete cycle enumeration.** Fix the starting vertex 0. Depth-first search over adjacent unused vertices produces each Hamiltonian traversal starting at 0, and checks the closing edge back to 0. A Hamiltonian cycle has exactly two such traversals (opposite orientations), so this procedure is exhaustive without losing or repeating edge sets. The code `verify_dfs.py` obtains 2688 rooted traversals and exactly 1344 distinct 16-edge masks; it checks that each mask occurs twice.

**Step 2: independent cycle enumeration.** A Hamiltonian cycle on 16 vertices decomposes into two alternating, disjoint perfect matchings. Conversely, two edge-disjoint perfect matchings whose union is connected form a Hamiltonian cycle. Each undirected Hamiltonian cycle has exactly one unordered pair of alternating matchings. The program `verify_matching.py` enumerates all 272 perfect matchings by recursive pairing of the smallest unmatched vertex, inspects every unordered pair, checks edge-disjointness and connectedness, and obtains the same 1344 cycles. These are mathematically exhaustive constructions by the stated bijections.

**Step 3: exact coefficients.** For each subset \(S\subseteq E(Q_4)\) of size at most three, both programs sum \((-1)^{|S\cap C|}\) directly over their independently generated collections of 1344 cycle edge masks, using integer bit counts. They agree on the entire coefficient distributions written in the Finding section. Consequently, no pair character vanishes and exactly 1120 triple characters vanish.

**Step 4: complete symmetry classification.** Every automorphism of \(Q_4\) is an XOR translation of the vertices followed by a permutation of four coordinates, giving \(16\cdot24=384\) transformations. The first verifier constructs all 384 distinct edge permutations and, for every pair and triple, forms its exact orbit. It checks coefficient constancy on each orbit and that these orbits partition every pair and every triple. The result is six pair orbits, 24 triple orbits, and the six zero-orbit representatives and sizes displayed above.

**Step 5: forced versus additional cancellation.** Each Hamiltonian cycle has degree two at every vertex, so it meets the four-edge star at that vertex in an even number of edges. Thus toggling a star in a Walsh frequency does not change its coefficient. Edge transitivity and double counting give exactly half of all cycles using any fixed edge: \(1344\cdot16/32=672\); this proves every singleton coefficient is zero without computation. Toggling a vertex star turns a singleton incident edge into the other three incident edges, giving 64 vanishing triples. To check whether more triples can be obtained from singleton zeros via *any* cycle-even edge cut, observe that a cut transforming a one-edge support into a three-edge support has at most four edges. The verifier exhausts all proper vertex subsets of the 16 vertices and finds the only four-edge cuts are the 16 vertex stars; there are no smaller cuts. Hence precisely those 64 three-edge cancellations are explained by such cut symmetries, leaving 1056 others.

All enumerations are finite and exhaustive, with no floating-point operations or statistical extrapolation. These steps establish each number in the theorem.

## Verification

Use standard Python 3 (no third-party packages) and run, from the directory containing the attached programs:

```
python3 verify_dfs.py
python3 verify_matching.py
```

Expected first output lines are `DFS_PASS cycles=1344 one=32_zero two=0_zero three=1120_zero`, `MINCUT_PASS edge_connectivity=4 vertex_stars=16 forced_zero_triples=64 other_zero_triples=1056`, and `MATCHING_PASS perfect_matchings=272 Hamilton_cycles=1344`. The complete immutable output for these checked programs is supplied in `dfs.out` and `matching.out`. Assertion failures terminate the programs. The distinct constructions verify the 1344 cycle list and all low-weight integer coefficient counts independently; only the first separately checks the 384-element automorphism orbit partition and exhaustive minimum-cut census.

## Relationship to prior work

Parkhomenko [1] classifies four-cube Hamiltonian cycles using coordinate change-number sequences and explicitly obtains the already-known total 1344. Chebiryak and Kroening [2] classify cube Hamiltonian cycles by change sequences and tabulate the 1344 cycles and nine automorphism classes for \(Q_4\). Neither inspected discussion computes or classifies signed Walsh correlations of specified labelled **edge** subsets. The edge-prescription existence results of Caha–Koubek [3] and Dvořák [4] ask whether a cycle can include specified edges, not for equalities between positive and negative signed counts. These prior enumerations are compatible with the present result and might in principle support an independent nontrivial recomputation of it; their mere unsigned cycle totals or coordinate-type counts do not imply the signed low-support histogram. The theorem reports the new low-degree Fourier census, not a new enumeration of Hamiltonian cycles.

## Limitations

The present theorem says nothing about Walsh coefficients supported on four or more edges, the total Fourier-convolution rank, or any general dimension other than \(Q_4\). The independence of the two enumerators is algorithmic, not independent human validation. The precise 2001 online release day of [1] was not established; its stated publication is only year-and-issue. An unindexed calculation of low-order signed correlations, potentially in Gray-code enumeration literature, remains a historical-priority risk. The full text of [3]–[4] was not inspected, although their accessible published statements concern prescribed-edge existence rather than correlation counts.

## References

1. P. P. Parkhomenko, *Classification of the Hamiltonian Cycles in Binary Hypercubes*, Avtomatika i Telemekhanika, 2001, no. 6, 136–150; full text https://www.mathnet.ru/eng/at1807.
2. Y. Chebiryak and D. Kroening, *Towards a Classification of Hamiltonian Cycles in the 6-Cube*, Journal on Satisfiability, Boolean Modeling and Computation 4 (2008), 57–74, doi:10.3233/SAT190038, full text https://www.researchgate.net/publication/220163337_Towards_a_Classification_of_Hamiltonian_Cycles_in_the_6-Cube.
3. R. Caha and V. Koubek, *Hamiltonian cycles and paths with a prescribed set of edges in hypercubes and dense sets*, Journal of Graph Theory 51 (2006), 137–169; first publicly posted 21 October 2005, https://doi.org/10.1002/jgt.20128.
4. T. Dvořák, *Hamiltonian Cycles with Prescribed Edges in Hypercubes*, SIAM Journal on Discrete Mathematics 19 (2005), 135–144, https://doi.org/10.1137/S0895480103432805.
