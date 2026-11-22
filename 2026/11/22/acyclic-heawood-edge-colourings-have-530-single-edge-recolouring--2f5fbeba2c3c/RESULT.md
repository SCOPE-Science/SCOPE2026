# Acyclic Heawood edge-colourings have 530 single-edge-recolouring sectors

## Finding

Let \(H\) denote the simple Heawood graph, the incidence graph of the Fano plane. Fix a palette of four colors. An *acyclic edge-colouring* is a proper edge-colouring whose edges in any two colours form a forest. Let \(\mathcal A\) be the space of acyclic four-colour edge-colourings modulo global permutations of colour names. Define its *single-edge recolouring graph* \(\mathcal R\) by connecting two distinct elements of \(\mathcal A\) if representatives can be chosen that differ on exactly one Heawood edge and are both acyclic proper colourings.

**Theorem.** The acyclic edge chromatic index of \(H\) is four, and \(|\mathcal A|=119784\). The graph \(\mathcal R\) has exactly \(299880\) edges and \(530\) connected components, distributed as follows:

| Component order | Number of components |
|---:|---:|
| 1 | 392 |
| 14 | 112 |
| 42 | 24 |
| 40040 | 1 |
| 76776 | 1 |

In particular, exactly \(392\) palette-unlabelled acyclic optimum edge-colourings are frozen under any legal single-edge recolouring. Every frozen colouring has three colour classes of size five and one of size six (the converse does not hold). With the four colours regarded as individually named, there are exactly \(2874816\) valid edge-colourings.

## Assumptions and scope

This is a theorem about one finite graph and the precise move rule above. The four colours are available on every edge, all four are actually used in every acyclic colouring, and a recolouring must change exactly one edge (no intermediate invalid colourings). Global colour renaming identifies configurations, but a legal move is tested between actual named representatives. The count is not a statement about Kempe exchanges, full colour-class trades or ordinary proper edge-colourings without the acyclicity constraint.

Model the Fano plane with points \(p\in\{0,\ldots,6\}\) and lines \(L_j=\{j,j+1,j+3\}\) modulo seven. The bipartite incidence graph has fourteen vertices, comprising seven points and seven lines, and exactly twenty-one edges (flags) \((p,L_j)\) with \(p\in L_j\). Index those edges in lexicographic order by point and line; hence the first three indexed edges are the three flags incident to point zero.

## Proof

**Optimal palette size.** In a cubic graph, a proper three-edge-colouring decomposes its edges into three perfect matchings. The union of any two is a 2-regular spanning subgraph, so it contains a cycle and cannot be acyclic. Thus \(H\) cannot have an acyclic three-edge-colouring. The exhaustive recurrence below explicitly constructs acyclic four-edge-colourings, thereby establishing the optimum four directly, without relying on the known general cubic-graph theorem.

**Canonicalization and exhaustive generation.** Every proper acyclic colouring uses all four colours by the preceding argument. The three edges incident with point zero have three distinct colours. Every orbit under the free global action of the permutation group on four colour names therefore has exactly one representative whose first three indexed edges carry colours \(0,1,2\), in that order. To generate all these representatives, process point vertices in order. At each point assign an injective sequence of three distinct colours chosen from the four palette colours to its three incident flags; refuse a choice if the resulting colour repeats at an already partially coloured line vertex. At the end accept precisely when the union of every pair of colour classes contains no cycle. This is an exhaustive finite search: every proper colouring appears exactly once as a sequence of local injections, and the pairwise forest test is equivalent to acyclicity by definition. The independent point-injection implementation finds \(230336\) canonical proper colourings before the forest tests, and exactly \(119784\) afterwards. In parallel, a distinct edge-by-edge backtracking implementation rejects a new coloured edge whenever it closes a path in one of its two-colour subgraphs. This independent search also enumerates exactly \(119784\) canonical acyclic colourings. Each local rejection is necessary and cannot discard a completed valid colouring.

**Exact recolouring adjacency.** Encode each canonical colouring as twenty-one consecutive two-bit values. For each of the \(119784\) states and each of its twenty-one graph edges, try the three other named colours. Discard a candidate if a colour repeats at a graph vertex or if any of the six unordered two-colour subgraphs contains a cycle. For every surviving candidate, uniquely rename its three colours at point zero to \(0,1,2\), assigning its remaining colour to \(3\). Look up the resulting canonical state. This generates precisely all edges of the quotient reconfiguration graph: any two named representatives for a quotient move differ from a fixed named representative by a single global renaming, and the algorithm tries all changes of its one selected edge. Both implementations check that all accepted neighbors are in the enumerated state set and that no quotient self-loop appears.

The two independent algorithms each obtain exactly \(599760\) directed transitions, paired symmetrically into \(299880\) undirected edges. Breadth-first search over the complete adjacency lists gives component sizes \(1\) (392 times), \(14\) (112 times), \(42\) (24 times), \(40040\) and \(76776\) (once each). The weighted sum of these sizes is exactly \(119784\), so every state is assigned to a component. The common exact degree histogram is \(0:392,\ 1:1344,\ 2:8400,\ 3:17248,\ 4:21168,\ 5:26880,\ 6:19264,\ 7:12768,\ 8:7728,\ 9:2744,\ 10:1008,\ 11:840\). Recounting colour-class sizes of the \(392\) degree-zero states shows the sorted profile \((5,5,5,6)\) for all of them, proving the additional one-way assertion. This completes an exact, finite enumeration proof of the stated classification.

**A witness.** In the stated flag order, the twenty-one-digit word `012102103210213203201` encodes one valid acyclic proper colouring using four named colours; the verifiers construct many others. No inference about unrelated graphs is needed.

## Verification

Two standalone C++17 implementations accompany the result. The first enumerates edge-by-edge with incremental two-colour cycle tests; the second enumerates independent local injective colourings point-by-point and checks all two-colour forests only after completing a colouring. They separately construct the recolouring graph and independently reproduce all component and degree counts above. Compile and run `verify_incremental.cpp` and `verify_incidence.cpp` with any standard-conforming C++17 compiler. The exact command lines and observed outputs are in `VERIFICATION.md` and `VERIFY_OUTPUT.txt`. The checks establish an exhaustive finite theorem, not an extrapolation from random or bounded experiments.

## Relationship to prior work

Ito, Kamiński and Demaine (2009) developed one-edge-at-a-time reconfiguration theory for *proper list edge-colourings*, but the additional all-bichromatic-forests condition and this specific graph's component spectrum are not established in their accessible abstract. Andersen, Máčajová and Mazák (2011) prove existence of acyclic four-edge-colourings for general connected cubic graphs other than two exceptions; their general index theorem proves the known minimum, not the precise Heawood optimal-state count or one-edge mobility decomposition. The accessible full published Heawood strong-edge-colouring result entitled *A sharp two-to-three-class trade threshold for optimal strong edge-colourings of the Heawood graph* classifies \(416\) seven-colour induced-matching partitions and whole-colour-class trades; neither its constraint nor its move rule is the one studied here. published-finding corpus queries also found work on proper *vertex* recolouring of the Heawood graph and proper edge recolouring of the Petersen graph, which do not logically imply the present classification.

## Limitations

Only the palette-unlabelled single-edge move graph and its exact components are claimed. No global diameter is claimed for either of the two large components; a few sampled eccentricities are not maximum-distance certificates. Absolute priority in unindexed work cannot be proved from the searches. The full text of the Andersen–Máčajová–Mazák journal paper was not available through the accessible public interface, though its abstract and publication metadata were inspected; any unpublished enumeration buried in its full text is a residual originality risk. The classification relies on the stated exhaustive algorithms as finite certificates and has not undergone independent scholarly audit.

## References

1. T. Ito, M. Kamiński and E. D. Demaine, *Reconfiguration of List Edge-Colorings in a Graph*, IEICE COMP2009-19, public issue date 22 June 2009, https://ken.ieice.org/ken/paper/20090629taNc/eng/ ; author's accepted manuscript https://dspace.mit.edu/entities/publication/bb785ce8-54b8-410f-9221-e28f5a647d36 .
2. L. D. Andersen, E. Máčajová and J. Mazák, *Optimal acyclic edge-coloring of cubic graphs*, first published 6 December 2011, https://doi.org/10.1002/jgt.20650 .
3. E. Máčajová and J. Mazák, *An Algorithm for Optimal Acyclic Edge-Colouring of Cubic Graphs*, 2011, https://doi.org/10.1007/978-3-642-21204-8_17 .
4. *A sharp two-to-three-class trade threshold for optimal strong edge-colourings of the Heawood graph*, accessible published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-two-to-three-class-trade-threshold-for-optimal-strong-ed--4b64a4175adc .
