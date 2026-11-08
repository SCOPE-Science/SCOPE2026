# The Pappus two-independence complex is a mixed wedge of nine five-spheres and one six-sphere

## Finding
Let \(P\) be the eighteen-vertex Pappus graph, the cubic Levi graph of the Pappus \((9_3)\) incidence configuration. Let \(\operatorname{Ind}_2(P)\) be the simplicial complex on graph vertices whose simplices are precisely subsets that induce connected components of order at most two. Then
\[
\operatorname{Ind}_2(P)\simeq \bigvee^{9}S^5\vee S^6.
\]
This is an integral homotopy equivalence. In particular, the reduced integral homology is free of rank nine in degree five, free of rank one in degree six, and zero in every other degree.

## Assumptions and scope
Fix the simple graph \(P\) on vertices \(\{0,1,\ldots,17\}\). Include the cycle edges joining \(i\) to \(i+1\pmod{18}\) and the nine distinct chords determined by the standard Hamiltonian LCF sequence `[5,7,-7,7,-7,-5]` repeated three times: for each \(i\), join \(i\) to \(i+s_i\pmod{18}\), where \(s_i\) is the corresponding sequence entry. Duplicated undirected chords are counted only once. The resulting graph has twenty-seven edges and is cubic.

A subset \(U\) is admissible exactly if every vertex in its induced graph has at most one neighbor inside \(U\). This equivalent local condition follows because an undirected graph of maximum degree one consists only of isolated vertices and isolated edges. The empty subset is used in the augmented face-poset enumeration but not as an ordinary CW cell. No claim is made for any graph other than this labeled Pappus graph or for any other higher-independence parameter.

## Proof
**Exact enumeration.** The supplied verifier constructs all subsets of the eighteen vertices. A direct test counts induced degrees; a second independent dynamic construction inserts the lowest-numbered present vertex only when its addition leaves all induced degrees at most one. Both enumerate identical sets. Counting by simplex dimension \(-1,0,\ldots,9\), with the empty face in degree \(-1\), yields
\[
(1,18,153,762,2394,4806,6027,4428,1728,308,27).
\]
Thus there are exactly \(20{,}652\) augmented faces, and the geometric complex has dimension nine.

**Complete acyclic discrete-Morse reduction.** In the augmented face poset, process graph vertices in the fixed order \(0,1,\ldots,17\). At stage \(v\), pair each still-unmatched face \(\sigma\) lacking \(v\) with the also-unmatched admissible face \(\sigma\cup\{v\}\), then remove both from further stages. This is a pairing of \(10{,}321\) covering incidences, leaving precisely nine critical five-simplices and one critical six-simplex. It pairs the empty face with a vertex.

For completeness the verifier constructs the *entire* directed augmented Hasse diagram. All \(120{,}240\) incidences between codimension-one faces are oriented downward except for the matched incidences, which are reversed. Its exhaustive topological sort visits all \(20{,}652\) faces, proving acyclicity rather than merely exhibiting a potential matching. The augmented empty-face pair contributes the usual implicit basepoint when converting this matching to an ordinary Morse CW model. There are no critical cells of dimensions one through four or seven through nine.

**Integral attaching maps.** Give each simplex the increasing-vertex orientation. The Morse boundary from the single critical six-cell to the nine critical five-cells is computed by signed elimination of all matched five-six pairs; the result is exactly the nine-entry zero column. The verifier obtains the *same matrix* by two separate exact procedures: forward elimination of unit incidence coefficients and reverse gradient projection in a verified acyclic dependency ordering. Each operation has incidence coefficient \(\pm1\), so no rational or modular approximation occurs.

The five-skeleton of the Morse CW model is \(\bigvee^9S^5\), since it has one basepoint and precisely nine five-cells. The six-cell is attached by a map from \(S^5\) to that wedge. By the Hurewicz isomorphism, \(\pi_5(\bigvee^9S^5)\cong\mathbb Z^9\), and an attaching map is nullhomotopic exactly if its degree vector vanishes. Its computed degree vector is zero, hence the six-cell contributes a freely attached six-sphere. Forman's discrete-Morse theorem proves the claimed integral homotopy equivalence.

**Independent reduction order.** A second matching orders the eighteen graph vertices by the deterministic permutation produced by Python's `random.Random(0).shuffle`. It gives \(10{,}320\) pairs, ten critical five-simplices and two critical six-simplices. Its two signed Morse boundary columns are
\[
(-1,0,0,-1,-1,0,0,0,0,0)^T,
\qquad(1,0,0,1,1,0,0,0,0,0)^T.
\]
These columns have primitive rank one, with Smith invariant factors \((1,0)\), independently supporting the nine surviving five-spheres and one six-sphere. The reduced Euler characteristic is \(-8\), consistent with the stated wedge.

## Verification
Run `python3 verify_pappus_ind2.py` in the same directory; Python 3.10 or newer is sufficient and no third-party packages are needed. All graph edges, all simplices, both matchings and their complete directed-Hasse acyclicity checks are reconstructed directly. Both gradient-matrix algorithms operate over exact integers and agree entry by entry. A reproducible recorded output is provided in `verification_output.txt`; the verifier ends with `ALL_CHECKS_PASS`. These are finite *exhaustive* checks for the explicitly given eighteen-vertex complex, not evidence for analogous infinite families.

## Relationship to prior work
Deshpande and Singh introduce this exact higher-independence definition and determine homotopy types for complete multipartite, fully whiskered, cycle and rooted-tree families. Deshpande, Shukla and Singh prove general connectivity estimates and special structure for chordal graphs. The Pappus graph is cubic with no leaves and has six-cycles, so these families and the chordal hypothesis do not cover it; neither paper determines its specific two-independence type.

Previously published calculations for the Pappus graph's *ordinary independence complex* concern subsets with **no** induced edges (the smaller parameter), yielding ten four-spheres and a rational cyclic-symmetry character. Separately, its ordinary *matching complex* has graph edges rather than graph vertices as simplicial vertices, and is a wedge of forty five-spheres. Neither result implies the stated homotopy type. A published two-independence result for the Petersen graph treats a different ten-vertex graph and likewise does not imply this result. Direct statement-level comparisons and searches under the phrases “two-independence”, “higher independence”, “induced maximum degree one”, and “dissociation complex” identified no covering Pappus result in the inspected sources.

## Limitations
The theorem concerns only the Pappus graph and the indicated two-independence definition. It does not classify all cubic incidence graphs, prove a homotopy result for larger Levi graphs, give an equivariant homotopy decomposition, or rule out equivalent material in unindexed publications. The dated 2010 Pappus-graph reference establishes archive eligibility as the earliest *verified dated source used here*, not the historical first appearance of the graph. Publication priority requires wider verification, and independent mathematical review has not been performed.

## References
1. M. Abreu, D. Labbate and J. Sheehan, *Irreducible pseudo 2-factor isomorphic cubic bipartite graphs*, first arXiv version 2010-02-09. https://arxiv.org/abs/1002.1891
2. Priyavrat Deshpande and Anurag Singh, *Higher Independence Complexes of graphs and their homotopy types*, first arXiv version 2020-01-15. https://arxiv.org/abs/2001.05448
3. Priyavrat Deshpande, Samir Shukla and Anurag Singh, *Distance r-domination number and r-independence complexes of graphs*, first arXiv version 2020-01-19. https://arxiv.org/abs/2001.06775
4. Wolfram MathWorld, *Pappus Graph*, for the standard LCF presentation. https://mathworld.wolfram.com/PappusGraph.html
5. *Order-three symmetry on Pappus independence homology*, previously published exact computation of the ordinary independence complex. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-order-three-symmetry-on-pappus-independence-homology--ea65a5211f31
6. *Integral homotopy type of the Pappus graph matching complex*, previously published exact computation. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-pappus-graph-matching-complex--db6c6c11f317
7. *The 2-independence complex of the Petersen graph is a 3-sphere*, previously published exact computation for a different graph. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-2-independence-complex-of-the-petersen-graph-is-a-3-sphere--156dc9567f6a
