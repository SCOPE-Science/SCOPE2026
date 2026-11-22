# A one-landmark gap and connected edge-sensor mobility on the Heawood graph

## Finding

Let \(H\) be the point–line incidence graph of the Fano plane (the Heawood graph). A vertex set \(S\subseteq V(H)\) is *edge resolving* if the vectors of graph distances from the selected vertices to all \(21\) edges are pairwise distinct. It is *vertex–edge dominating* if every edge has an endpoint at graph distance at most one from some selected vertex. Call a set satisfying both conditions an *edge-identifying and locally covering set* (the vertex-edge dominant edge resolving set of Ikhlaq–Hayat–Siddiqui).

The minimum possible cardinality is exactly \(6\). There are exactly \(1{,}386\) such minimum sets. Their one-vertex token-jump reconfiguration graph is connected, with \(17{,}514\) edges and radius and diameter \(6\). Their adjacency-constrained token-slide reconfiguration graph is also connected, with \(5{,}040\) edges, radius \(7\) and diameter \(9\). Thus the edge-local reconfiguration graph is connected despite the stricter edge-coverage requirement.

More precisely, all \(168\) minimum five-landmark *edge-resolving* sets leave exactly one edge outside the closed radius-one vertex-to-edge coverage region; none is vertex–edge dominating. Among the \(1{,}386\) qualifying six-sets, exactly \(574\) contain **no** five-vertex edge-resolving subset; \(672\) contain one such subset, \(84\) contain two, and \(56\) contain three. Under the full \(336\)-element incidence-graph automorphism group, the qualifying sets form exactly \(11\) orbits of sizes \(14,28,28,56,84,168,168,168,168,168,336\).

## Assumptions and scope

All graphs here are finite, simple, undirected and unweighted; no other projective plane or larger graph is in scope. Write vertices as seven points \(p_i\) and seven lines \(\ell_j\), with \(i,j\in\{0,\ldots,6\}\), where \(p_i\ell_j\in E(H)\) exactly when \((i-j)\bmod7\in\{0,1,3\}\). This yields \(14\) vertices and \(21\) incidence edges. For graph distance \(d_H\) and incidence edge \(e=uv\), define

\[
\delta(s,e)=\min\{d_H(s,u),d_H(s,v)\}.
\]

The edge resolving requirement is: for every two distinct incidence edges \(e\ne f\) there exists \(s\in S\) with \(\delta(s,e)\ne\delta(s,f)\). Vertex-edge domination means that for every incidence edge \(e\), some \(s\in S\) satisfies \(\delta(s,e)\le1\): this includes a sensor on an endpoint or at an endpoint's neighbor. These are simultaneous, not alternative, requirements.

A *token jump* exchanges one selected vertex for one unselected vertex; a *token slide* additionally requires those two vertices to be adjacent in \(H\). Every intermediate set must be a *minimum six-vertex set satisfying both conditions*. Distances, radii and diameters refer to these reconfiguration graphs, not to the original incidence graph. The classification is for unordered sets of sensor locations, not labeled tokens.

## Proof

**1. Exact vertex-to-edge distance matrix.** Let \(e=p_i\ell_j\) be an incidence edge. For a point sensor \(p_a\), its distance to \(e\) is \(0\) if \(a=i\), \(1\) if \(a\ne i\) but \(p_a\in\ell_j\), and \(2\) otherwise. For a line sensor \(\ell_b\), its distance is \(0\) if \(b=j\), \(1\) if \(b\ne j\) but \(p_i\in\ell_b\), and \(2\) otherwise. Indeed distinct points (or lines) of the Fano plane are at graph distance two and a nonincident point–line pair is at distance three. Both programs implement this matrix, one through breadth-first searches and one directly through incidence formulas in a different, binary model.

**2. Exhaustive finite certificate.** There are exactly \(\binom{21}{2}=210\) unordered pairs of distinct incidence edges. For each sensor \(s\), define a 210-bit *separation mask*, whose bit for \(\{e,f\}\) is one precisely if \(\delta(s,e)\ne\delta(s,f)\), and a 21-bit *coverage mask*, whose bit for \(e\) is one precisely if \(\delta(s,e)\le1\). A set \(S\) satisfies the joint predicate if and only if the bitwise union of its separation masks has all 210 bits and the union of its coverage masks has all 21 bits. This is an exact equivalence to the definitions, with no numerical tolerance.

Enumerate all unordered \(S\subseteq V(H)\) of sizes \(0,1,\ldots,6\); there are exactly \(\sum_{k=0}^6\binom{14}{k}=6{,}476\) candidates. The edge-resolving subset counts by size are \(0,0,0,0,0,168,1890\), and the joint-predicate subset counts are \(0,0,0,0,0,0,1386\). Hence no smaller qualifying set exists and all \(1{,}386\) minimizers are known. The first script independently verifies these counts using BFS distance codes rather than the 210-bit separation masks; the second directly constructs and checks the masks. Both are complete exhaustive finite certificates.

For each of the \(168\) five-element edge-metric bases, unioning its 21-bit coverage masks leaves exactly one zero bit. For each qualifying six-set, deletion of each of its six vertices and lookup in the complete five-base list yields the exact containment counts \(574,672,84,56\) for zero, one, two, and three five-bases respectively. These checks use the entire listed candidate universes, not sampled representatives.

**3. All optimal relocations.** Construct an adjacency dictionary on the complete family of \(1{,}386\) sets. For each \(S\), each \(u\in S\), and each \(v\in V(H)\setminus S\), create an edge to \(T=(S\setminus\{u\})\cup\{v\}\) exactly when \(T\) lies in that complete family. This enumerates every possible jump. Retain a transition as a slide if and only if \(uv\in E(H)\). The generated graphs have \(17{,}514\) jump edges and \(5{,}040\) slide edges. Exact BFS from **each** of the 1,386 states reaches all other states in both cases and yields the eccentricity distributions:

- Jumps: \(1{,}386\) states at eccentricity \(6\).
- Slides: \(210\) states at eccentricity \(7\), \(812\) at eccentricity \(8\), and \(364\) at eccentricity \(9\).

This proves both connectivity statements and the asserted sharp radius and diameter values. As a reproducibility cross-check, the complete unordered-pair distance histograms (including the 1,386 diagonal pairs at distance zero) are, for jumps at distances \(0,\ldots,6\),

\[
(1386,17514,133308,356608,332066,109620,10689),
\]

and for slides at distances \(0,\ldots,9\),

\[
(1386,5040,23940,81256,194460,296464,247891,97104,13314,336).
\]

The positive-distance entries in either row sum to \(\binom{1386}{2}\). Both independent programs produce these same numbers using distinct Fano-plane constructions and separate enumeration implementations.

**4. Automorphism orbit certificate.** The permutations of the seven point labels preserving the seven Fano lines number \(168\); each induces a permutation of the seven lines. Composing these with the point–line duality \(p_i\leftrightarrow\ell_{-i}\) doubles the group to the complete \(336\) incidence-graph automorphisms. Generate its actions on the complete set of six-vertex minimizers and partition the \(1{,}386\) sets into orbits. Their \(11\) sizes are precisely as stated in the finding. The program checks that all generated permutations preserve the 21 incidence edges and that the disjoint orbit union is exactly the certified set family. This supplements the numerical result with a complete intrinsic symmetry partition.

## Verification

Run `python3 verify_incidence.py` and `python3 verify_binary.py` using Python 3's standard library. The first builds the cyclic-difference-set Fano plane, computes shortest paths by independent BFS, checks the edge-code and coverage predicates, verifies every optimal exchange and every shortest-path distance, then enumerates all 336 automorphisms. The second builds the Fano plane from orthogonality of nonzero vectors over \(\mathbb F_2^3\), uses exact incidence formulas and 210-bit separating masks, then enumerates and verifies the same reconfiguration metrics. Companion `.out` files document the actual successful program outputs. Both were replayed from the embedded package files; no unembedded numerical input, other-run output, or precomputed data is required.

## Relationship to prior work

Ikhlaq, Hayat, and Siddiqui (arXiv:2211.09327, publicly posted November 17, 2022) define the simultaneous vertex–edge domination and edge-metric resolving condition, deriving results for paths, cycles, complete bipartite graphs, wheels, fans, and certain Cartesian products. Their inspected full text does not analyze the Fano incidence graph, let alone the minimum-state jump or slide networks. Kelenc, Tratnik, and Yero (arXiv:1602.00291, 2016) introduce edge metric dimension without the extra vertex–edge domination condition; their full-text treatment also does not compute this new combined classification.

The closely related published Heawood edge-metric-basis record `2026/11/8/SCOPE-edge-metric-bases-of-the-heawood-graph-and-octagonal-slide-recon--d4a919fbecfd` establishes exactly 168 size-five edge-resolving sets, with token slides forming 21 disjoint eight-cycles. This is respected as a prior result, not asserted anew. The present theorem imposes a strictly stronger sensor condition, proves that **all** prior five-bases fail that additional condition by one uncovered edge, and classifies the different, 1,386-state optimum family and its **connected** slide graph. Neither the prior 168-state graph nor its geometric basis classification implies the new six-state predicate, the count 1,386 or its path metrics by a relabeling or restriction argument. A published result on the vertex–edge dominant edge-metric bases of complete prisms concerns different base graphs and does not determine these Fano-plane values.

## Limitations

This is an exact finite computer-assisted theorem on one fourteen-vertex graph; it makes no claim for arbitrary projective planes, larger incidence networks, or other domination-radius definitions. Enumeration is a proof only because all 6,476 candidate sets and all potential one-token moves are generated and checked by exact predicates, with independently constructed programs; numerical logs alone are not used as evidence. The two implementations are not independent peer review. Unindexed earlier calculations, alternate terminology, and manuscripts not captured by the searched collections remain historical-priority risks. The result does not assert unique discoverability from its search terms.

## References

1. H. M. Ikhlaq, S. Hayat and H. M. A. Siddiqui, “Unique identification and domination of edges in a graph: The vertex-edge dominant edge metric dimension,” arXiv:2211.09327v1, first public November 17, 2022. https://arxiv.org/abs/2211.09327.
2. A. Kelenc, N. Tratnik and I. G. Yero, “Uniquely identifying the edges of a graph: the edge metric dimension,” arXiv:1602.00291v1, first public January 31, 2016. https://arxiv.org/html/1602.00291v1.
3. “Edge-metric bases of the Heawood graph and octagonal slide reconfiguration,” published mathematical record, identifier `2026/11/8/SCOPE-edge-metric-bases-of-the-heawood-graph-and-octagonal-slide-recon--d4a919fbecfd`, full RESULT.md consulted, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-edge-metric-bases-of-the-heawood-graph-and-octagonal-slide-recon--d4a919fbecfd.
