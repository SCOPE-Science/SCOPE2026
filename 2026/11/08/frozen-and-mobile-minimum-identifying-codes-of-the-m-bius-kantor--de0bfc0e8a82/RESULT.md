# Frozen and mobile minimum identifying codes of the Möbius–Kantor graph

## Finding
Let \(M=GP(8,3)\) be the Möbius–Kantor graph. Consider all minimum **closed-neighborhood identifying codes** of \(M\). There are \(584\) such codes, each containing \(8\) vertices; these two census figures are previously known and are not the new claim here. Put an edge between two codes when one selected vertex is replaced by another, retaining the identifying-code property. Let \(\mathcal T\) require the replacement vertices to be adjacent in \(M\) (token sliding), and let \(\mathcal J\) allow any distinct replacement vertices (token jumping).

The new exact **reconfiguration classification** is as follows.

* The token-slide graph \(\mathcal T\) has exactly \(864\) edges and \(97\) connected components: one component of order \(488\) and \(96\) isolated states. The nontrivial component has radius \(8\) and diameter \(10\).
* The \(96\) isolated configurations split evenly into \(48\) sets inducing exactly \(5\) edges of \(M\) and \(48\) sets inducing exactly \(7\) edges of \(M\).
* The slide-degree distribution \((d:\#\text{states})\) is \((0:96),(2:240),(4:168),(6:48),(8:30),(24:2)\). The two degree-\(24\) states are the two bipartition classes of \(M\). Among the \(488\) mobile states, the eccentricity distribution is \((8:104),(9:192),(10:192)\).
* By contrast, \(\mathcal J\) is connected, with \(2{,}496\) edges, radius \(7\), and diameter \(8\). Its degree distribution is \((4:96),(6:48),(8:48),(9:192),(10:144),(12:48),(24:8)\).

In particular, unrestricted movement connects every minimum identifying code, while edge-constrained movement strands \(96\) of the same optimal configurations. The remaining \(488\) configurations all lie in a single, comparatively large component.

## Assumptions and scope
Vertices are \(u_i,v_i\) for \(i\in\{0,\ldots,7\}\). Edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+3}\), where subscripts are modulo \(8\). The machine encoding is \(u_i=i\) and \(v_i=8+i\). The graph is finite, undirected, and simple, with \(16\) vertices and \(24\) edges. The set \(S\subseteq V(M)\) is an identifying code precisely when all sets \(N_M[x]\cap S\), for \(x\in V(M)\), are nonempty and pairwise different. All replacement moves preserve cardinality \(8\) and must result in an identifying code. Distances, radii, and diameters refer to shortest paths within each connected component; the isolated components have eccentricity \(0\) and no finite distance to other components.

## Proof
**Exact finite feasibility certificate.** For each vertex \(x\), encode its closed neighborhood as a \(16\)-bit mask \(B_x\). For distinct \(x,y\), the signatures \(B_x\cap S\) and \(B_y\cap S\) differ exactly when \(S\) intersects \(B_x\mathbin{\triangle}B_y\). Therefore \(S\) is identifying if and only if it intersects each of the \(16\) nonempty-neighborhood constraints \(B_x\) and all \(\binom{16}{2}=120\) difference constraints \(B_x\mathbin{\triangle}B_y\). This is a necessary-and-sufficient test, not a heuristic. `verify_cpp.cpp` visits **all** \(2^{16}=65{,}536\) bitmasks and applies every one of these \(136\) conditions. It finds no solutions of cardinality at most \(7\), and precisely \(584\) solutions of cardinality \(8\). The separately structured `verify_python.py` enumerates every subset by cardinality and directly constructs the nonempty distinct signature sets. The two independent code lists agree exactly. These census facts are rechecked here only to establish the state space of the new graph classification.

**Exhaustion of moves.** For two different weight-eight masks \(a,b\), they differ by one replacement if and only if \(a\oplus b\) has exactly two set bits and exactly one of those bits belongs to \(a\). This proves that the pair scan in `verify_cpp.cpp` includes every token jump exactly once. Requiring the two changed positions to be adjacent in the explicitly defined host graph gives exactly all token slides. Independently, `verify_python.py` enumerates every ordered choice of one occupied and one unoccupied position, tests code feasibility against the complete code set, and retains undirected pairs once. Both methods produce the identical `jumps.txt` (\(2{,}496\) lines) and `slides.txt` (\(864\) lines) certificates.

**Component and distance certificate.** Each checker constructs the complete undirected adjacency lists and visits every vertex in each component by depth-first or breadth-first search. It then starts an independent breadth-first shortest-path search from **every** state to all reachable states. Both obtain the component, degree, and eccentricity distributions displayed above. In particular, the slide graph has one \(488\)-vertex component and \(96\) singletons, and the maximum finite slide distance is exactly \(10\). Filtering the \(96\) degree-zero masks by the number of host-graph edges with both endpoints selected produces exactly \(48\) of induced size \(5\) and \(48\) of induced size \(7\). These tests establish all enumerated invariants because they visit the entire finite state space and every possible transition, not a subset or random sample.

**Extremal mobile states.** The original graph is bipartite with the classes \(\{u_i:i\text{ even}\}\cup\{v_i:i\text{ odd}\}\) and its complement. Each class is a weight-eight identifying code (the four-neighbor signatures on one side are distinct). Each vertex of such a class can be slid to any of its three unoccupied neighbors, giving \(8\cdot3=24\) candidate moves; direct signature checking confirms all are legal. Complete enumeration establishes that no other state has degree \(24\).

The executable certificates, not output transcripts alone, constitute a finite exhaustive proof. Both independent implementations directly reconstruct the problem from the stated \(GP(8,3)\) edges.

## Verification
Run from the directory containing the supplied artifacts:

```sh
python3 verify_python.py
g++ -std=c++17 -O2 -Wall -Wextra verify_cpp.cpp -o verify_cpp
./verify_cpp
```

The Python program emits the exact sorted code list and both edge lists; the C++17 program independently recomputes every code and edge and requires byte-independent equality of their parsed entries. Each also checks component sizes, degrees, all-pairs eccentricities, and the two frozen-code induced-edge classes. The exact output of these executions is recorded in `python_execution.txt` and `cpp_execution.txt`.

## Relationship to prior work
Balbuena, Foucaud, and Hansberg [1] study identifying codes and location-domination for graphs of girth at least five, including cubic-graph bounds and explicit small examples; their classification does not supply the above host-specific transition graph. Mynhardt and Teshima [2] define the minimum identifying-code slide graph and prove a universal realizability theorem for such reconfiguration graphs; a realizability theorem does not determine the slide graph of \(GP(8,3)\). They explicitly motivate questions of connectivity and frozen configurations. The Möbius–Kantor graph is the canonical cubic symmetric graph on sixteen vertices [3]. A separate earlier exact census of the identifying codes of this host already established the minimum size, the number \(584\), the full code polynomial, and thirteen automorphism orbits. Those previously known results are **not** asserted to be novel; the new claim is the exact adjacency, connectivity, rigidity, and distance structure under the two move rules.

## Limitations
This is a complete, but **finite**, theorem for the specified sixteen-vertex host graph, not an infinite-family statement. There is no claim that the degree or distance distributions extend to other generalized Petersen graphs. Existence of a broad equivalent unpublished analysis remains possible; computational equality and complete enumeration are not proof of historical priority. No independent external scholarly audit is asserted.

## References
[1] C. Balbuena, F. Foucaud, A. Hansberg, “Locating-dominating sets and identifying codes in graphs of girth at least 5,” arXiv:1407.7263, first public version 2014-07-27; *Electronic Journal of Combinatorics* 22(2), #P2.15, 2015. https://arxiv.org/abs/1407.7263

[2] C. M. Mynhardt, L. E. Teshima, “A note on some variations of the \(\gamma\)-graph,” arXiv:1707.02039, 2017-07-07, especially Section 2 and Section 5. https://arxiv.org/abs/1707.02039

[3] “Möbius-Kantor Graph,” Wolfram MathWorld. https://mathworld.wolfram.com/Moebius-KantorGraph.html
