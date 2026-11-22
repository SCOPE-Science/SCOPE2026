# Three pinned opinions on the Petersen graph: exact consensus basins and a sharp forcing threshold

## Finding

Let \(P=KG(5,2)\) be the Petersen graph and let \(S\) be any three of its ten vertices, permanently held at opinion one. Every other vertex synchronously adopts the strict binary majority of its three neighbors at each update. All initial opinions on \(S\) are one; the remaining seven initial opinions are arbitrary. The exact eventual outcomes depend only on the three-edge shape of \(S\) under the identification of Petersen vertices with edges of \(K_5\):

| Shape of the three pinned edges in \(K_5\) | Number of labelled pin sets | Initial states reaching unanimous one, out of \(128\) | Initial states reaching a genuine two-cycle | Initial states reaching a different fixed point | Sharp first-periodic-entry time |
| --- | ---: | ---: | ---: | ---: | ---: |
| Three-edge star | 20 | 128 | 0 | 0 | 3 |
| Triangle | 10 | 98 | 28 | 2 | 2 |
| Three-edge path | 60 | 124 | 0 | 4 | 5 |
| Two-edge wedge plus a disjoint edge | 30 | 94 | 30 | 4 | 4 |

**Forcing theorem.** A set of exactly three permanently one-valued vertices drives **every** compatible initial configuration to unanimous one if and only if its edges in \(K_5\) are a three-edge star. Consequently, the minimum number of permanently one-valued vertices necessary to guarantee unanimity for all compatible initial configurations is exactly three, and there are precisely twenty optimal labelled placements. Each of those placements reaches consensus by time three, sharply. This is a statement about synchronous, *reversible-opinion* majority with stubborn pinned vertices, not an irreversible bootstrap process.

As a secondary check, two permanently one-valued vertices never guarantee unanimous one: for each of the fifteen adjacent Petersen pairs, exactly \(141\) of its \(256\) compatible initial states converge to unanimous one; for each of the thirty nonadjacent pairs, exactly \(188\) of \(256\) do. Neither number equals \(256\).

## Assumptions and scope

The vertex set is the ten two-element subsets of \(\{0,1,2,3,4\}\), listed lexicographically, and two such vertices are adjacent precisely when the subsets are disjoint. Every vertex has degree three. Fix any set \(S\) of three vertices. The map \(F_S:\{0,1\}^{10}\to\{0,1\}^{10}\) is restricted to states satisfying \(x_v=1\) for \(v\in S\), with updates
\[
 (F_S(x))_v=\begin{cases}1,&v\in S,\\
 \mathbf1\{\sum_{u\sim v}x_u\ge2\},&v\notin S.
 \end{cases}
\]
The **first-periodic-entry time** is the least nonnegative \(t\) such that \(F_S^t(x)\) is on a temporal orbit. An eventual two-cycle means a primitive temporal orbit of least period two. All counts are for labelled configurations and include periodic starting configurations. A consensus basin comprises initial states eventually reaching the all-one fixed point. The four pin shapes are exactly the four isomorphism classes of three-edge simple graphs on five vertices, with isolated vertices ignored in their names.

## Proof

**1. Monotonicity converts universal forcing into a single trajectory.** Each coordinate of \(F_S\) is a nondecreasing Boolean function of the initial state. Therefore \(x\le y\) coordinatewise implies \(F_S^t(x)\le F_S^t(y)\) for every integer \(t\ge0\). Among all compatible initial states, \(\mathbf1_S\), equal to one at exactly the pinned sites, is the least. If \(F_S^T(\mathbf1_S)=\mathbf1\) for some finite \(T\), then \(F_S^T(x)=\mathbf1\) for every compatible \(x\). Conversely, universal consensus includes the seed-only initial state. This proves the claimed equivalence without assuming the update preserves one-valued free opinions.

**2. Exactly the stars force consensus.** Write \(ij\) for the Petersen vertex \(\{i,j\}\). For the three-edge star \(S=\{01,02,03\}\), the successive sets of vertices with opinion one when started from \(\mathbf1_S\) are
\[
\begin{aligned}
 A_0&=\{01,02,03\},\\
 A_1&=A_0\cup\{14,24,34\},\\
 A_2&=A_1\cup\{12,13,23\},\\
 A_3&=A_2\cup\{04\}=V(P).
\end{aligned}
\]
Every equality follows directly from the disjointness neighborhoods and threshold two. This is sharp since \(04\notin A_2\). Relabelling \(\{0,1,2,3,4\}\) preserves the dynamics, so every three-edge star placement behaves the same.

The other three edge types fail universal forcing because their seed-only states reach a nonunanimous equilibrium. For the triangle \(S=\{01,02,12\}\), the next active set is \(\{01,02,12,34\}\) and is fixed. For the path \(S=\{01,12,23\}\), the next active set is \(\{01,04,12,23,34\}\) and is fixed. For the wedge plus disjoint edge \(S=\{01,02,34\}\), the seed-only configuration is already fixed. Direct neighbor counting verifies each listed fixed-state claim.

Three-edge graphs on five vertices comprise exactly stars, triangles, three-edge paths and wedges plus disjoint edges. Their numbers of labelled edge selections are respectively \(5\binom{4}{3}=20\), \(\binom53=10\), \(60\) and \(30\), summing to \(\binom{10}{3}=120\). Thus the twenty stars are exactly the universal forcing triples.

**3. Three is the minimum pin budget.** Every pair of Petersen vertices can be extended to some nonstar three-vertex set. If the two Kneser edges are disjoint as edges of \(K_5\), extend by a third edge sharing an endpoint with one edge, giving a three-edge path or wedge plus disjoint edge; if they intersect, choose an edge between their other endpoints to form a triangle. The seed-only state for each such nonstar extension does not reach consensus by Step 2. Since adding more fixed-one sites can only raise every later coordinate, forcing by the original pair would imply forcing by *each* extension, a contradiction. The same argument rules out singleton and empty pin sets. Hence three is necessary and sufficient.

**4. Exact class-by-class basin and entry-time census.** For every three-element subset \(S\) of the ten Petersen vertices, enumerate the \(2^7=128\) initial states consistent with its pins. Each update uses precisely the threshold rule in the assumptions. Because this is a deterministic map on a set of \(128\) states, the first repeated state occurs no later than step \(128\); retaining the first occurrence index distinguishes transient length and least period exactly. Classify eventual period one according to whether the repeated state is unanimous one, and period two separately. The supplied `check_bitmask.py` enumerates all \(120\cdot128=15{,}360\) state/pin instances using integer neighborhood bitmasks, records the entire first-entry/period table for each representative, and checks that all labelled pin sets in each geometric class have the tabulated outcomes. The independent program `check_tuples.py` reconstructs disjointness neighborhoods from five alphabetic labels, updates direct ten-element tuples, and independently enumerates the same \(15{,}360\) state/pin instances. Both verify the complete table and exact pin-class multiplicities. Exhaustion here is a complete finite proof on this specified graph, not an extrapolation from experimental samples.

The supplementary two-pin figures similarly result from examining all \(45\cdot2^8=11{,}520\) compatible two-pin initial states, with the 15/30 pair orbit partition established by disjointness. All state and pin multiplicities are exact integers.

## Verification

With Python 3 and no third-party packages, from this directory run `python3 check_bitmask.py` and `python3 check_tuples.py`. The former outputs a complete first-entry/period profile for each pin type and additional two-pin counts; the latter independently recomputes the type profiles, checks all 120 possible forcing triples and proves by finite extension checks that no pair can force consensus. Their expected outputs are in `bitmask_results.json` and `tuple_results.json`. Both checkers terminate with `"all_assertions": "passed"` only after completing every stated exhaustive assertion. The human proof of the forcing threshold uses the independently explicit trajectories in Step 2; the exact fractional basins rely on exhaustive, checkable integer computation.

## Relationship to prior work

The 2012 strict-majority dynamic-monopoly study of Khoshkhah, Soltani and Zaker treats *irreversible activation*, in which an activated vertex remains active. That cannot establish the dynamics or basin census of unpinned vertices here, which may change in either direction. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014) establish broad facts for synchronous majority dynamics including period-one-or-two behavior, but their graph-class theorems do not provide these four Petersen pin-shape distributions or identify the universal forcing triples.

The closest inspected unpinned Petersen calculation, *A four-step Petersen majority projection and the Desargues double-cover basin spectrum*, determines the four-step projection and recurrent fibers of the **unmodified** Petersen map and of its bipartite double. Freezing chosen vertices to one changes the update map; those projection-fiber numbers do not imply any of the four pinned basin counts. Work on two-neighbor bootstrap percolation of odd graphs concerns irreversible growth; the small Petersen graph is related by its underlying graph, not by its update rule. All standard graph identification and threshold principles are credited, not claimed as new.

## Limitations

The exact numerical basin table concerns only the ten-vertex Petersen graph, strict open-neighbor majority and permanently one-valued pins, not arbitrary Kneser graphs, noisy voting, asynchronous updating or independently pinned zero-valued opinions. The minimum pin budget and star characterization are exact for this dynamics. The two separately implemented checkers support exhaustive reproducibility but are not independent external mathematical review. Historical priority beyond the inspected texts and searched public records cannot be guaranteed; an unindexed computation or a general theorem with a nonobvious specialization could cover the claim.

## References

1. K. Khoshkhah, H. Soltani, and M. Zaker, *On dynamic monopolies of graphs: the average and strict majority thresholds*, arXiv:1202.1146v1, first public 2012-02-06. https://arxiv.org/html/1202.1146v1
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first public 2014-05-11. https://arxiv.org/html/1405.2486v1
3. *A four-step Petersen majority projection and the Desargues double-cover basin spectrum*, public full result and finite proof, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-four-step-petersen-majority-projection-and-the-desargues-doubl--b8bcbb0b4dff
4. *2-Neighbor Bootstrap Percolation on Odd Graphs*, arXiv:2606.03687, https://arxiv.org/abs/2606.03687 (different irreversible rule).
