# Sharp decagon mobility and local pentagons among Desargues Hamiltonian cycles

## Finding

Let \(D=\operatorname{GP}(10,3)\) be the cubic twenty-vertex Desargues graph. Its vertices are \(u_i,v_i\), with indices modulo ten, and its thirty edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\). Let \(\mathcal H(D)\) be the set of undirected, unrooted Hamiltonian cycles, regarded as twenty-edge sets. For even \(\ell\), join two *distinct* elements of \(\mathcal H(D)\) if their entire edge-set symmetric difference is one simple alternating cycle of length exactly \(\ell\), the two configurations both being Hamiltonian. Denote the resulting graph by \(\mathcal R_\ell(D)\).

**Theorem.** The first nonempty such move graph occurs at length ten. The graph \(\mathcal R_{10}(D)\) has exactly 24 vertices, 84 edges and degree seven at every vertex. It is connected and every vertex has the same distance profile \((1,7,16)\). In particular,
\[
\operatorname{rad}(\mathcal R_{10}(D))=\operatorname{diam}(\mathcal R_{10}(D))=2.
\]
The subgraph induced on the seven neighbours of **each** vertex is the disjoint union \(C_5\sqcup 2K_1\). It follows that the trade graph has exactly 40 triangles, and each nonadjacent pair has exactly two common neighbours. The natural action of the 240 coordinate permutations and point-set complementation symmetries is transitive on the 24 cycles. Its action on the 84 ten-trade edges has exactly two orbits, of sizes 60 and 24, distinguished by whether their endpoints have two or zero common neighbours.

Among the 276 unordered pairs of Hamiltonian cycles, 84 have a single ten-edge alternating-cycle difference, 60 have a single eighteen-edge difference, and 132 have a disconnected difference. Therefore the ten-edge threshold is **sharp**: no smaller even alternating-cycle exchange between distinct Hamiltonian cycles is possible.

## Assumptions and scope

All vertices and edges are labelled as given above; no quotient by graph automorphisms or reversal creates additional states. Hamiltonian cycles are *unoriented edge sets* and have length twenty. A legal trade means that the **entire** symmetric difference is a single alternating simple cycle; the intermediate operation is one simultaneous replacement of half of its edges. This is not a sequential series of individual edge replacements, nor a Kempe switch of a three-edge-colouring. Both endpoints must be Hamiltonian. The claim concerns this fixed graph and this explicitly defined move, not an infinite family of generalized Petersen graphs.

An isomorphic second presentation uses the ten two-element subsets and ten three-element subsets of a five-element set, with containment edges. Complementing a three-element subset identifies the graph with the bipartite double cover of the Petersen graph. Both presentations are independently used below.

## Proof

**1. Perfect matching–Hamilton cycle bijection.** In any cubic graph, the complement of a perfect matching is a spanning two-regular graph, and conversely. Such a complement is Hamiltonian precisely when it has one connected component. Enumerate all perfect matchings of \(D\) by choosing the least unmatched vertex and trying each unmatched neighbour, then recursing on the remaining vertices. Every matching appears on exactly one branch: its partner at the chosen vertex is forced, after which induction applies to the remainder. The first included verifier executes this exhaustive recursion. It obtains 60 perfect matchings, of which 36 have complementary two-factor type \((10,10)\) and 24 have type \((20)\). Thus there are exactly 24 undirected Hamiltonian cycles. This static count is background; the contribution below is the movement geometry.

**2. Detecting the complete move relation.** Complementation preserves symmetric difference. For any two perfect matchings, their symmetric difference is a disjoint union of simple even cycles, each alternating between the two matchings. In particular, there is a legal one-cycle move exactly when the difference-edge subgraph is connected and two-regular on its nonisolated vertices. Comparing every one of the \(\binom{24}{2}=276\) unordered pairs, the first verifier gets difference cardinalities
\[
10:84,\qquad 12:60,\qquad16:60,\qquad18:60,\qquad20:12.
\]
The complete difference component test certifies that the 84 ten-edge differences and the 60 eighteen-edge differences are the only single cycles; all other 132 differences have more than one connected component. Hence there is no shorter nontrivial trade, and the ten-trade graph has exactly 84 edges.

**3. Finite metric and local geometry.** Construct the exact adjacency set of each of the 24 configurations by the ten-edge test in step 2. Every vertex has degree seven. Run ordinary breadth-first search from **all 24 vertices**, following precisely those legal edges. Each search finds all 24 vertices with distance histogram \((1,7,16)\). Thus connectedness and the radius and diameter assertions hold without extrapolation. For each vertex, restrict the adjacency relation to its seven neighbours and examine their internal degrees: five have degree two, two have degree zero, and the five degree-two vertices form a connected subgraph. Since a connected two-regular simple graph on five vertices is \(C_5\), its full local graph is exactly \(C_5\sqcup2K_1\). The five-cycle contributes five triangles through the central vertex, and division by three gives \(24\cdot5/3=40\) triangles. The same exhaustive pair test finds exactly two common neighbours for every one of the 192 nonadjacent pairs; among the 84 adjacent pairs, 60 have two and 24 have none.

**4. Coordinate-symmetry description.** On the second graph representation, each permutation of the five underlying symbols preserves subset containment, as does exchanging each two-element subset with its three-element complement. These 240 transformations map the 24 undirected Hamiltonian edge sets to themselves. The second verifier enumerates all transformations, checks their induced state maps are bijective, proves that the orbit of one Hamiltonian cycle has size 24, and checks that the seven edges from that cycle generate two distinct edge orbits: five edges in one orbit of size 60, and two in another of size 24. Those sizes sum to the already exhausted 84 edges, proving the full asserted orbit classification.

**5. Independent enumeration.** The second verifier does not enumerate perfect matchings. It builds the twenty-vertex two-/three-subset incidence graph and recursively enumerates all simple paths starting at a fixed vertex, retaining those that return to the root after visiting all twenty vertices; duplicate orientations are removed by storing canonical edge sets. Every Hamiltonian cycle visits the fixed root, so this enumerates every one without omission. The independent connected-symmetric-difference test and all-source breadth-first searches reproduce the 24-state count, all 84 ten-flips, the seven-neighbour structure and the two-step metric. The two implementations therefore use different graph models, enumeration primitives and edge representations.

## Verification

Run `python3 verify_matching_complements.py` and `python3 verify_direct_hamiltonian_cycles.py` using Python 3 and only the standard library. Both programs must terminate normally and print four lines beginning with `PASS`. They are complete finite certificate programs: no sampling, external datasets, random choices, numerical tolerances or precomputed adjacency tables are involved. The first exhausts all 60 perfect matchings before retaining Hamiltonian complements; the second independently enumerates closed Hamiltonian paths directly. Their assertions check the graph size, exact transition graph, metric and geometry.

## Relationship to prior work

Perfect-matching complements, the generalized Petersen representation and the basic Hamiltonian-cycle count are established graph-theoretic background. Dyer, Jerrum and Müller (2015) study two-edge switches in perfect-matching Markov chains; those are a different move, and no four-edge alternating differences occur between the Hamiltonian complements here. Takaoka (2018) treats Hamiltonian-cycle reconfiguration by two-edge switches and general complexity, not this ten-edge simultaneous alternating-cycle operation. Earlier exact results for the Desargues graph describe 60 perfect matchings under six- and eight-cycle alternating flips, and 32 edge-colouring classes under bichromatic Kempe switches. Those state spaces do not determine the present 24-state, ten-edge Hamiltonian trade graph. A separate result studies ten-edge Hamiltonian trades on the thirty-vertex Tutte–Coxeter graph (144 states; diameter four), not the twenty-vertex graph treated here. The comparison is about statements and their implications, not matching terminology alone.

## Limitations

This is an exhaustive finite classification for one specific cubic graph. It does not assert a general theorem for arbitrary cubic or generalized Petersen graphs, and it does not infer uniqueness from a failed literature search. Historical novelty is a best-knowledge assessment: unindexed work under Hamiltonian switches, alternating-cycle trades, tours or one-factor complements may contain an equivalent result. Independent scholarly assessment has not been conducted.

## References

- M. Dyer, M. Jerrum and H. Müller, *On the switch Markov chain for perfect matchings*, arXiv:1501.07725, first public version 2015-01-30, https://arxiv.org/abs/1501.07725.
- A. Takaoka, *Complexity of Hamiltonian Cycle Reconfiguration*, *Algorithms* 11 (2018), article 140, https://doi.org/10.3390/a11090140.
- *Hexagon isolation and octagon bridges in Desargues perfect-matchings*, publicly released mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-hexagon-isolation-and-octagon-bridges-in-desargues-perfect-match--f46dd29846e2.
- *A Desargues component inside the Desargues edge-Kempe graph*, publicly released mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-desargues-component-inside-the-desargues-edge-kempe-graph--5e4cc13d96d8.
- *Decagon trades connect all Hamiltonian cycles of the Tutte–Coxeter graph*, publicly released mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-decagon-trades-connect-all-hamiltonian-cycles-of-the-tutte-coxet--2d918f37db93.
