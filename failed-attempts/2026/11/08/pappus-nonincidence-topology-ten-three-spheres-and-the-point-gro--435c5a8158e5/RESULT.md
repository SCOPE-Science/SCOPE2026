# Pappus nonincidence topology: ten three-spheres and the point-group homology character

## Finding
Let \(P\) be the Pappus point-line configuration with nine points and nine lines, and let \(B\) be its bipartite **nonincidence** graph (a point and a line are adjacent when they are not incident). The ordinary open-neighborhood complex has two isomorphic components. With \(W=\bigvee^{10}S^3\), its integral homotopy type is
\[
\mathcal N(B)\simeq W\sqcup W.
\]
Each component is a pure five-dimensional simplicial complex with nonzero reduced homology only in degree three, where it is \(\mathbb Z^{10}\). Consequently neither component is shellable.

On either component the point/line-preserving automorphism group of the Pappus incidence graph has order \(108\). Its rational degree-three homology character has the following values, with multiplicities over the group: \(10\) once, \(2\) eighteen times, \(-2\) twenty-one times, \(1\) thirty-two times, and \(-1\) thirty-six times. In particular its invariant subspace is zero. Two elements with the same cycle type on the nine points can have different character values, so the character is not determined by point cycle type alone.

## Assumptions and scope
All graphs are finite, undirected, simple and loopless. For a graph \(B\), the open-neighborhood complex \(\mathcal N(B)\) consists of sets of vertices having a **common adjacent vertex**. The empty face is included in face counting, and connected components refer to the realization of nonempty faces. The Pappus configuration's nine point triples, as sets of one-indexed point labels, are
\[
\{125,236,134,458,569,467,278,389,179\}.
\]
Here, for example, \(125\) abbreviates the set \(\{1,2,5\}\), not an integer. The nine lines are exactly these triples; no additional incidences are present. This labelled triple system is isomorphic to that displayed in Example 3.5 of Abdallah--Schenck (2022); the explicit bijection is independently checked in the accompanying verifier.

For a component with point vertices, a subset \(F\) is a face exactly when there is a line triple \(L\) disjoint from \(F\). Thus this component is precisely the **noncover complex** of the three-uniform Pappus incidence hypergraph. Its nine maximal faces are the complements of the nine triples and therefore have six vertices each. The second component is the corresponding complex on the nine line vertices. No claim of an equivariant wedge decomposition is made.

## Proof
The underlying incidence graph is represented by the eighteen-cycle on vertices \(0,1,\ldots,17\), together with nine chords listed in the standalone verifier. Even vertices are points and odd vertices are lines. It has twenty-seven incidences and degree three at every vertex. The published Pappus triple system is matched by an explicit point relabelling, and an explicit automorphism swapping the two bipartite sides demonstrates that the neighborhood-complex components are isomorphic.

For each side, independently enumerate the face set both as the down-closure of the nine six-element nonincidence neighborhoods and by testing all \(2^9=512\) subsets for a common nonincidence witness. The two definitions give exactly 298 faces including the empty face, with face-count vector indexed by cardinality
\[
(1,9,36,81,108,54,9).
\]
The standard Morse matching is constructed by successively toggling the vertices in increasing order: at each stage match each still-unmatched nonempty face not containing the current vertex with its union with that vertex, whenever the latter face is still unmatched. The empty face is never matched. This produces exactly 143 disjoint pairs, one critical vertex, and ten critical three-simplices; no other nonempty critical faces survive. Reverse vertex order gives the same critical-cell dimensions and counts.

Crucially, the matching is **acyclic**: orient all 1,080 covering relations in the augmented face poset downwards, except matching relations oriented upwards. Exhaustive topological sorting visits all 298 face nodes, so there is no directed cycle. Removing the empty node leaves a valid acyclic matching of the ordinary face poset. By the discrete Morse theorem, each component is homotopy equivalent to a CW complex having exactly one zero-cell and ten three-cells. Since there are no positive-dimensional cells below dimension three, every three-cell attaches to the unique point; the CW complex is \(\bigvee^{10}S^3\). This proves the **integral homotopy equivalence**, not just its Euler characteristic.

For the symmetry assertion, a point permutation extends to a color-preserving incidence automorphism if and only if it maps the set of nine incident triples to itself. All \(9!\) permutations are checked, yielding exactly 108 such automorphisms. For each, orient each simplicial face by increasing point labels and compute its oriented fixed-face sign. Their alternating sum is the simplicial Lefschetz number \(L(g)\). Because the sole nonzero rational homology groups of a connected component are \(H_0\cong\mathbb Q\) and \(H_3\cong\mathbb Q^{10}\), the trace on the latter is \(1-L(g)\). The 108 exact traces give the character multiplicities above. Their sum is zero, so averaging the character over the group gives invariant dimension zero.

## Verification
The included standard-library-only `run_verification.py` reconstructs the labelled graph, verifies the Pappus triple system and the color-swapping duality, compares independent face predicates, checks both vertex orders of the Morse matching on both components, exhaustively topologically sorts every directed Hasse diagram, computes direct degree-wise mod-two cellular boundary ranks, and enumerates all point-group automorphisms and their oriented Lefschetz traces. The actual execution record is in `verification_output.txt`.

For either component the direct mod-two boundary ranks in degrees one through five are \((8,28,53,45,9)\), yielding reduced Betti vector \((0,0,0,10,0,0)\) in degrees zero through five. This is an independent numerical check, not the proof of the integral homotopy claim. There are 594 nonempty faces across the two components.

## Relationship to prior work
Kim and Kim (arXiv:2101.01850, first public January 6, 2021) define noncover complexes and prove hypergraph domination and Leray bounds, with exact homotopy computations for tight paths and tight cycles. The Pappus nine-triple hypergraph is not one of those families, and their general bounds do not determine this homotopy type or its automorphism character.

Santhanam, Shukla and Singh (arXiv:2211.10607, first public November 19, 2022) establish broader collapsibility bounds. Such bounds are not an exact homotopy calculation and provide no character formula here.

Abdallah and Schenck (arXiv:2208.01557, first public August 2, 2022), especially their Example 3.5, explicitly identify the Pappus triple incidence structure and compute **graded algebraic Betti tables** for a monomial Orlik--Solomon ideal involving rank-two flats. That ideal and its Alexander dual are not the nine-facet noncover complex treated here; the reported algebraic Betti numbers do not state this integral wedge decomposition or the Lefschetz character. The Pappus incidence data themselves are prior art and are not claimed as new.

Adjacent recorded calculations concern a graph-metric Čech nerve of the Pappus graph, its ordinary matching complex and other incidence structures. Those have different face relations and do not imply the stated homotopy and symmetry claim. A comparison by implications, including the noncover and Alexander-dual formulations, is recorded in the review material.

## Limitations
This is an exact finite classification for the Pappus configuration, not a theorem about all nine-point configurations or all three-regular bipartite incidence structures. The rational group character is determined, but no decomposition into irreducible representations, integral group lattice, or equivariant homotopy equivalence is claimed. Independent external validation has not been performed. Undiscovered equivalent literature remains possible.

## References
1. Jinha Kim and Minki Kim, *Domination numbers and noncover complexes of hypergraphs*, arXiv:2101.01850, initially submitted 2021-01-06, https://arxiv.org/abs/2101.01850.
2. Rekha Santhanam, Samir Shukla and Anurag Singh, *Bounds for the collapsibility number of a simplicial complex and non-cover complexes of hypergraphs*, arXiv:2211.10607, initially submitted 2022-11-19, https://arxiv.org/abs/2211.10607.
3. Nancy Abdallah and Hal Schenck, *Nets in \(\mathbb P^2\) and Alexander Duality*, arXiv:2208.01557, initially submitted 2022-08-02, especially Example 3.5, https://arxiv.org/abs/2208.01557.
