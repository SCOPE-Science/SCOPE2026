# Complete component and distance geometry of cube recolouring at two through five colours

## Finding
Let \(Q_3\) be the three-dimensional Boolean cube with vertices \(\{0,1\}^3\), and let \(\mathcal R_k(Q_3)\) be the graph of proper vertex-colourings by \(k\) *named* colours, adjacent when one vertex changes colour. The exact component, radius, and pair-distance classification for \(2\le k\le5\) is as follows. An entry \(1^{24}+2628\) means twenty-four singleton components and one component of order \(2628\). The radius and diameter in the table refer to each nonsingleton component.

| Palette \(k\) | States | Recolouring edges | Component orders | Radius and diameter of nonsingleton components | Unordered pairs at distance \(12\) |
|---|---:|---:|---|---|---:|
| \(2\) | 2 | 0 | \(1+1\) | not applicable | 0 |
| \(3\) | 114 | 240 | \(114\) | \(12,12\) | 279 |
| \(4\) | 2652 | 11808 | \(1^{24}+2628\) | \(12,12\) | 15198 |
| \(5\) | 29660 | 217440 | \(29660\) | \(12,12\) | 85870 |

In particular **every colouring in every nonsingleton component has eccentricity exactly \(12\)**. The \(24\) isolated four-colourings are precisely those with all six square faces rainbow; they form a single orbit under cube automorphisms and colour renaming.

For \(k=3,4,5\), the full unordered pair-distance distributions, indexed by distances \(1,\ldots,12\), are respectively

\[
\begin{aligned}
 k=3:\;&(240,552,768,756,576,576,528,558,528,552,528,279),\\
 k=4:\;&(11808,54432,159984,327600,491616,573336,558720,486936,385368,263040,123840,15198),\\
 k=5:\;&(217440,1582320,7294800,23206920,52774080,86982840,104067840,89599740,53018760,18418440,2593920,85870).
\end{aligned}
\]

The distributions count pairs connected by a finite recolouring sequence. Each distribution sums to the number of unordered pairs lying in a common component; singleton pairs contribute nothing.

## Assumptions and scope
The graph has exactly eight vertices, labelled by the binary integers \(0,\ldots,7\), with adjacent labels differing in one bit. The palette is exactly the finite set \(\{0,\ldots,k-1\}\); colours are allowed to remain unused. Recolouring changes exactly one vertex and preserves properness. The radius is the minimum, and eccentricity the maximum, of finite shortest-path distances within each connected component. An isolated vertex has eccentricity zero. The theorem makes no claim about higher-dimensional cubes, palettes outside \(\{2,3,4,5\}\), or mixing components.

## Proof
This is an exact computer-assisted finite classification, with the entire exhaustive algorithm supplied in `verify_q3_recolouring.py`. Its completeness follows from the following steps.

1. **Exhaustive states and edges.** The program loops over each of the \(k^8\) functions from cube vertices into the palette and retains exactly those with unequal colours at all twelve cube edges. From every retained colouring it tests each of the eight possible changed vertices and each alternative colour, adding an edge exactly when no neighbour has the replacement colour. Conversely, every legal single-vertex recolouring occurs in this loop. It checks symmetry of the resulting adjacency lists.
2. **Exact symmetry quotient for metric checking.** Every automorphism of the Boolean cube is a permutation of its three coordinates followed by a three-bit translation: exactly \(3!\cdot2^3=48\) maps. Independently permuting named colours also preserves properness and recolouring adjacency. For each colouring the program forms a canonical key by taking the lexicographic minimum of its first-occurrence palette-normalisations under all \(48\) cube automorphisms. Two colourings have the same key **if and only if** they lie in the same joint graph-and-palette symmetry orbit: the first-occurrence normalisation identifies precisely the palette-permutation orbits, and taking minima identifies the graph-automorphism orbits. It enumerates \(1,4,13,23\) such orbits for palettes \(2,3,4,5\), respectively.
3. **Complete exact distances.** The connected components are obtained by a full graph traversal. An ordinary queue-based breadth-first search from one representative of each symmetry orbit computes its distance to every colouring in the component, with no heuristics or truncated search. Since every permitted symmetry is a graph automorphism of the entire recolouring graph, the same distance profile and eccentricity apply to every member of that orbit. Thus all vertices are covered, including disconnected singleton components. Multiplying every representative's distance-shell counts by its orbit size and dividing the nonzero-distance totals by two gives the exact unordered-pair distance distributions above. The checker verifies the weighted sums against \(\sum_C\binom{|C|}{2}\), and checks that the distance-one total is the independently enumerated edge count.
4. **Independent component and boundary checks.** For \(k=4\) the program also performs an ordinary, unquotiented breadth-first search from **each** nonisolated colouring, verifying that all \(2628\) mobile states are reachable with eccentricity \(12\). For \(k=3\) it similarly checks every state without orbit reduction. It enumerates all six square faces and verifies that the set of \(24\) isolated four-colourings agrees exactly with the rainbow-on-every-face condition. All comparisons use integer equality.

The executable source specifies complete loops, base cases, data structures and termination: no external solver, numerical approximations or untrusted computed tables enter the proof. The length of each search is bounded by the explicitly enumerated finite state set.

## Verification
Run `python3 verify_q3_recolouring.py` with Python 3 standard library. It independently builds the cube and all legal colourings, checks every adjacency, computes all connected components, uses the exact \(48\)-element automorphism group and palette relabelling, calculates full distance profiles, verifies all entries in the table and the distance histograms, and prints `VERIFY_OK` only if every assertion succeeds. On replay the output ended in `VERIFY_OK`. The code contains the asserted expected counts but computes the observed counts from first principles; changing an asserted value would not change the underlying state graph or distances. Every finite instance within the claimed domain is enumerated, not sampled.

## Relationship to prior work
Cames van Batenburg, *Large diameter for \((\Delta+2)\)-colouring reconfiguration*, first publicly released 2026-11-12, quotes a pre-existing theorem (Proposition 2(iv)) that for maximum degree at most three and \(k\ge\Delta+2\), the **global diameter** is \(n+\mu\). For the cube, \(n=8\), \(\mu=4\), and \(k=5\), so the diameter \(12\) is **known**, not new. That theorem does not state that **every** colouring has eccentricity \(12\), does not calculate full pair-distance counts, and does not address the critical palette \(k=4\) or the three-colour geometry. Related results for complete bipartite graphs, the Petersen graph and the Wagner graph concern different graphs. Earlier discussions of frozen colourings of cubes are acknowledged: the existence of immobile four-colourings is **not** new. This result is the complete exact, jointly metric-and-component classification for the natural base cube across the two-to-five palette transition, not a new general diameter bound.

## Limitations
The theorem is for the finite eight-vertex cube only. Its correctness is conditional on the supplied exhaustive Python algorithm implementing the definitions, so a separate formal verification or independent mathematical audit would further strengthen confidence. Neither an unrestricted theorem for higher dimensions nor a new bound for general cubic graphs follows. Historical priority is provisional; absence from the inspected sources and indexed searches does not establish absolute novelty, and closely related unpublished finite computations may exist.

## References
- W. Cames van Batenburg, *Large diameter for \((\Delta+2)\)-colouring reconfiguration*, arXiv:2611.17022v1 (first public 2026-11-12), https://arxiv.org/abs/2611.17022. Especially Proposition 2(iv), which credits earlier results.
- S. Cambie, W. Cames van Batenburg and D. Cranston, *Sharp Bounds on Lengths of Linear Recolouring Sequences*, arXiv:2412.19695, https://arxiv.org/abs/2412.19695.
- D. Galvin, *Sampling 3-colourings of regular bipartite graphs*, arXiv:1206.3202, https://arxiv.org/abs/1206.3202, for background on cube colouring dynamics and frozen configurations.
