# Exact joint contagion and completion-time law on the cuboctahedral network

## Finding
Let \(G=L(Q_3)\), the cuboctahedral graph, and apply synchronous three-neighbor irreversible bootstrap activation. Write \(C_{k,t}\) for the number of initial active vertex sets of cardinality \(k\) that completely activate \(G\) after exactly \(t\) rounds. All nonzero values are:

| \(k\) | \(t=0\) | \(t=1\) | \(t=2\) | \(t=3\) | \(t=4\) |
|---|---:|---:|---:|---:|---:|
| 5 | 0 | 0 | 0 | 0 | 72 |
| 6 | 0 | 0 | 108 | 192 | 0 |
| 7 | 0 | 36 | 336 | 120 | 0 |
| 8 | 0 | 177 | 240 | 0 | 0 |
| 9 | 0 | 164 | 48 | 0 | 0 |
| 10 | 0 | 66 | 0 | 0 | 0 |
| 11 | 0 | 12 | 0 | 0 | 0 |
| 12 | 1 | 0 | 0 | 0 | 0 |

All other \(C_{k,t}\) vanish. There are exactly 72 minimum contagious five-sets. They are the complements, in the twelve edges of \(Q_3\), of the edge sets of its undirected Hamiltonian paths. These 72 choices fall into three orbits of size 24 under cubical symmetry. Every minimum contagious set has the activation profile \((5,7,9,11,12)\), so the sharp minimum-seed completion time is four synchronous updates.

If each site is initially active with probability \(p\), independently of the other sites, the exact probability of eventual complete activation is
\[
\begin{aligned}
P_{\mathrm{full}}(p)&=\sum_{k,t}C_{k,t}p^k(1-p)^{12-k}\\
&=72p^5-204p^6+204p^7-63p^8-16p^9+12p^{11}-4p^{12}.
\end{aligned}
\]
At \(p=1/2\), the probability is \(393/1024\). For \(0<p\le1\), the conditional probability of completion at round \(t\), given eventual complete activation, is \(\sum_k C_{k,t}p^k(1-p)^{12-k}/P_{\mathrm{full}}(p)\), with the numerator evaluated as a polynomial at \(p=1\). At \(p=0\), there is no activation and the conditional law is undefined; the unconditional law has \(T=\infty\) almost surely.

## Assumptions and scope
The ordinary three-cube \(Q_3\) has vertex set \(\{0,1\}^3\), with one edge between binary words at Hamming distance one. The twelve vertices of its line graph \(G\) represent the twelve cube edges; two vertices of \(G\) are adjacent exactly when their corresponding cube edges meet. Thus \(G\) is a four-regular graph with twelve vertices and 24 edges.

Starting from an arbitrary active set \(A_0\subseteq V(G)\), define \(A_{t+1}=A_t\cup\{v\notin A_t:|N_G(v)\cap A_t|\ge3\}\). Define \(T(A_0)=\min\{t:A_t=V(G)\}\), or \(\infty\) when no such time exists. These are synchronous, permanent activations with no recovery. The random-seed probability is independent across sites, with one common parameter \(p\). All 4,096 labelled initial subsets are included.

## Proof
**Leaf-pruning equivalence.** Put \(B_t=V(G)\setminus A_t\). Every vertex has degree four, so an inactive vertex survives a synchronous step exactly when it still has at least two inactive neighbors. Thus \(B_{t+1}\) is obtained from \(G[B_t]\) by deleting all vertices of degree zero or one, simultaneously. Iterating removes the entire graph exactly when the initial induced subgraph \(G[B_0]\) is a forest. If there is a cycle, its vertices all have degree at least two within the cycle and survive forever. Conversely every nonempty forest has a leaf or isolated vertex, so the successive leaf-pruning process empties it.

**Translation into cube paths.** For any edge subset \(F\subseteq E(Q_3)\), the induced subgraph of \(L(Q_3)\) on \(F\) is a forest if and only if \(F\) is a linear forest in \(Q_3\), meaning each component is a path. Indeed, three selected edges incident to one cube vertex create a triangle in the line graph; with no such triple the selected cube-edge degrees are at most two. Any cycle among selected cube edges creates a cycle in the line graph. Conversely a disjoint union of cube paths yields a disjoint union of line-graph paths. Therefore an initial active set succeeds precisely when the complementary cube-edge set is a linear forest.

**Sharp minimum and geometry.** Every linear forest on the eight cube vertices has at most seven edges. Since the line graph has twelve vertices, at least five active vertices are needed. Equality forces a seven-edge linear forest on all eight cube vertices. It is a spanning tree of maximum degree two, hence a Hamiltonian path in \(Q_3\), and the converse is immediate. A Hamiltonian path consists of seven cube edges, giving an induced \(P_7\) among the initially inactive vertices of \(G\). Parallel leaf deletion takes a seven-site path through orders \(7,5,3,1,0\), which proves the common activation wave \(5,7,9,11,12\).

**Exact finite counts.** Two independent exhaustive methods supply the remaining coefficients. `verify_paths.py` enumerates all \(2^{12}\) edge subsets of \(Q_3\) using independent degree and union-find cycle tests, and separately constructs Hamiltonian paths by depth-first search of distinct cube vertices. It confirms 72 undirected Hamiltonian-path edge sets and the linear-forest count by size \((72,300,492,417,212,66,12,1)\) for five through twelve seeds. Applying all 48 cube automorphisms to these 72 paths gives three size-24 orbits. Independently, `verify_dynamics.py` explicitly runs the synchronous threshold process from each of the \(2^{12}\) initial states and records the first complete-activation time, giving the joint table. The two methods do not use each other's generated data. These finite loops check each possible subset exactly once; no sampling, limiting extrapolation, or timeout assumption enters the claim.

Summing the joint entries over times gives the Bernoulli polynomial in the statement; direct integer arithmetic at \(p=1/2\) gives \(1572/4096=393/1024\).

## Verification
Run `python3 verify_dynamics.py` and `python3 verify_paths.py` from the same directory. Both programs use only the Python standard library. The first program checks the exact joint histogram and every five-seed activation profile. The second enumerates edge-disjoint linear forests by a separate disjoint-set computation, constructs all cube Hamiltonian paths, and confirms the three automorphism orbits. Assertions terminate with an error if any claimed count fails.

## Relationship to prior work
Bootstrap percolation on general random regular graphs and thresholds was analyzed by Balogh and Pittel (2006/2007); later work of Garbe, Mycroft, and McDowell (2018) gives general degree-proportional contagious-set bounds. The existence and number of 72 Hamiltonian paths on the ordinary three-cube are previously tabulated. The reconfiguration study *Sharp six-move backbite geometry of the three-cube* also describes the 72 minimum feedback vertex sets of the cuboctahedral graph, their Hamiltonian-path correspondence, and their three 24-element orbits. Minimum feedback vertex sets are minimum contagious sets here by the forest criterion above. That shared geometry is not claimed as distinct; the contribution is the exact cuboctahedral *joint* seed-size and synchronous completion-time distribution under the three-neighbor rule. The cuboctahedral graph identity, twelve-vertex count, 24-edge count, and 48 symmetries are standard.

## Limitations
This is a finite exact result for one canonical twelve-site graph, one homogeneous deterministic threshold, and permanent synchronous activation. It is not a universal percolation threshold, large-size asymptotic law, statement about recovery, or result for other polyhedra. The minimum-seed Hamiltonian path count is known independently; historical priority of the full joint distribution is not certified.

## References
- J. Balogh and B. G. Pittel, *Bootstrap percolation on the random regular graph*, first published 13 December 2006, https://doi.org/10.1002/rsa.20158.
- F. Garbe, R. Mycroft and A. McDowell, *Contagious sets in a degree-proportional bootstrap percolation process*, first published 29 October 2018, https://doi.org/10.1002/rsa.20818.
- E. W. Weisstein, *Cuboctahedral Graph*, MathWorld, https://mathworld.wolfram.com/CuboctahedralGraph.html.
- OEIS A091299, *Number of (directed) Hamiltonian paths (or Gray codes) on the n-cube*, https://oeis.org/A091299. Its third term 144 corresponds to 72 unoriented paths.
- E. W. Weisstein, *Hamiltonian Path*, https://mathworld.wolfram.com/HamiltonianPath.html.
- *Sharp six-move backbite geometry of the three-cube and its cuboctahedral decycling dual*, Resultary, 2026-11-22, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-sharp-six-move-backbite-geometry-of-the-three-cube-and-its-cuboc--d828e9887f71.
