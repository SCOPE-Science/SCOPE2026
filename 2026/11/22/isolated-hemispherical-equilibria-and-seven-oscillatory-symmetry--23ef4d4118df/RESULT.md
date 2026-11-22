# Isolated hemispherical equilibria and seven oscillatory symmetry types in icosahedral majority dynamics

## Finding

Let \(I\) be the ordinary twelve-vertex icosahedral graph and \(F\) the synchronous binary strict open-neighbor majority map on \(I\). Every state reaches a periodic orbit within five updates, sharply, and
\[
F^7=F^5\quad\text{on all }2^{12}\text{ labelled configurations}.
\]
There are exactly **14 fixed configurations**, consisting of the two unanimous opinions and the **12 closed vertex neighborhoods** \(N[v]\) regarded as binary supports. Every nonunanimous fixed configuration has a **singleton attraction basin**, while each unanimous fixed configuration has an attraction basin of size **1586**.

There are exactly **156 primitive temporal two-cycle orbits**, with no other recurrent periods. Their individual basin-size distribution is
\[
\begin{array}{c|rrrr}
\text{basin size}&2&4&6&14\\\hline
\text{number of two-cycle orbits}&16&60&60&20.
\end{array}
\]
Under the full 120-element automorphism group of the icosahedron, the 156 two-cycles split into **seven geometric classes**, characterized by the pairs (number of temporal orbits in class, basin size per temporal orbit):
\[
(6,2),\ (10,2),\ (20,14),\ (30,4),\ (30,4),\ (30,6),\ (30,6).
\]
The 14 fixed configurations form three geometric classes of sizes 1, 1, and 12. The full first-periodic-entry table is

| First entry \(t\) | Eventual period one | Eventual period two |
| ---: | ---: | ---: |
| 0 | 14 | 312 |
| 1 | 386 | 600 |
| 2 | 984 | 0 |
| 3 | 1080 | 0 |
| 4 | 480 | 0 |
| 5 | 240 | 0 |
| Total | 3184 | 912 |

Thus the largest entrance time is five, achieved by exactly 240 configurations, all eventually unanimous. In particular, an initially uniformly random configuration becomes unanimously fixed with probability \(793/1024\), enters a two-cycle with probability \(57/256\), and remains forever in a nonunanimous fixed state with probability \(3/1024\).

## Assumptions and scope

The graph has vertices \(0,1,\ldots,11\). Vertex 0 is the north pole, vertex 11 the south pole, \(u_j=1+j\) and \(\ell_j=6+j\) for \(j=0,\ldots,4\) are the staggered pentagonal rings. Subscripts on the two rings are reduced modulo five. The edges are the five edges of each ring, the edges \(0u_j\) and \(11\ell_j\), and the two cross-ring edges \(u_j\ell_j\) and \(u_j\ell_{j-1}\) for every \(j\). This gives twelve vertices, 30 edges, and five distinct neighbors per vertex, and is the ordinary icosahedral graph. The complete edge set is regenerated in `check_majority.py`, and the equivalent independent adjacency array is in `verify_majority.cpp`.

Every configuration is a map \(x:V(I)\to\{0,1\}\), encoded as \(s(x)=\sum_{v=0}^{11}2^vx_v\). The update is simultaneous, with
\[
(Fx)_v=1\quad\Longleftrightarrow\quad\sum_{w\sim v}x_w\ge3.
\]
There are no ties because every vertex has odd degree five. A temporal orbit identifies cyclic shifts in time; its basin is the set of all labelled initial configurations that eventually visit it. A geometric class additionally identifies graph automorphisms but does not identify global opinion complementation. The first periodic entry time is the least \(t\ge0\) for which \(F^t(x)\) belongs to a cycle.

## Proof

**1. Exact finite-state transition.** For each binary integer \(0\le s<4096\), let \(B_v\) be the bitmask of the five neighbors of vertex \(v\). Then the successor integer is exactly
\[
F(s)=\sum_{v=0}^{11}2^v\bigl[\operatorname{popcount}(s\mathbin{\&}B_v)\ge3\bigr].
\]
`check_majority.py` independently constructs the edge set by the ring definition and evaluates this formula for every one of the \(4096\) inputs. `verify_majority.cpp` hardcodes the independently specified adjacency list and evaluates the five-input threshold by explicitly checking all ten triples of neighbors; it does not use the popcount formula. Both complete calculations reproduce the same period, basin, and entrance tables.

**2. Sharp entrance identity and exact recurrent populations.** For each of the \(4096\) possible inputs, both implementations explicitly iterate until they find the first \(t\) satisfying \(F^{t+2}(s)=F^t(s)\). The programs verify that \(t\le5\) for every input and tabulate exactly the six entry-time rows above. At this first entrance they distinguish a fixed state from a primitive two-cycle by testing whether \(F^{t+1}(s)=F^t(s)\). Hence, for every configuration, \(F^5(s)\) lies on a cycle of length one or two, proving \(F^7=F^5\); no assumption of eventual periodicity from prior theory is needed. Sharpness is witnessed by the explicit trajectory
\[
87\longmapsto47\longmapsto23\longmapsto41\longmapsto16\longmapsto0,
\]
where the all-zero state is first reached at time five. The 14 fixed states and 312 other immediately recurrent states give \(312/2=156\) primitive temporal two-cycles.

**3. Fixed supports and basin sizes.** The exhaustive successor computation tests \(F(s)=s\) for all \(4096\) inputs and finds precisely the two constants and the twelve integer masks \(2^v\mathbin{|}B_v\). These are exactly the supports of the closed neighborhoods \(N[v]\), and the masks are pairwise distinct. Direct inspection of the neighborhood degrees shows each such mask is indeed stable: its center has five same-colored neighbors, each of the other five vertices in the cap has three same-colored neighbors, and the six outside vertices have at most two neighbors in the cap. The exhaustive test rules out additional fixed supports. For each starting state the programs take the canonical representative \(\min(F^t(s),F^{t+1}(s))\) at its first recurrent entry and count the states with each representative. This gives basin size 1 for every cap, 1586 for each constant state, and the displayed complete two-cycle basin-size distribution. The consistency identity is
\[
12+2(1586)+16(2)+60(4)+60(6)+20(14)=4096.
\]

**4. Exact spatial quotient.** `check_majority.py` enumerates all bijections of the twelve vertices that preserve every adjacency and nonadjacency: at each recursive level it tries every unused image compatible with all previously mapped pairs. This is exhaustive for graph automorphisms and returns exactly 120 permutations. Each of the 156 primitive temporal cycles is represented by the smaller of its two constituent integer states; for each of the 120 automorphisms the program permutes vertex bits and renormalizes the temporal phase. Its seven disjoint orbits have the sizes and basin values displayed above. A separate check verifies the update commutes with every one of the 120 permutations on every one of the 4096 configurations. The fixed supports similarly form geometric classes of cardinalities 1, 1, and 12.

All the finite computations exhaust a complete explicitly bounded state space, rather than a sampled subset. The independent successor formulas, explicit graph inputs, and short programs make each critical integer claim reproducible.

## Verification

From a directory containing the two files, run:

```sh
python3 check_majority.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_majority.cpp -o verify_majority
./verify_majority
```

Both programs terminate only after verifying the exact fixed-state, two-cycle, basin, and first-entry counts. The Python program additionally verifies the full 120-automorphism group and all geometric classes. `checks_output.txt` contains the exact output of both programs and the independently checked graph isomorphism result. No statistical inference, floating point calculations, third-party theorem prover, or inaccessible dependency is involved in the finite-state proof.

## Relationship to prior work

Goles and Olivos (1980) proved that symmetric binary threshold dynamics on a finite graph is eventually fixed or two-periodic; that general restriction is not new. Tošić and Agha (2004) compare configuration spaces of parallel and sequential threshold automata and derive broad properties, mostly focusing on one-dimensional cellular automata. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014) analyze majority dynamics, especially on infinite and random graphs. Kaaser, Mallmann-Trenn and Natale (2016) analyze general convergence-time bounds. None of the inspected relevant statements provides the exact icosahedral fixed-support, isolated-basin, entrance, or spatial-symmetry census here.

The previously published exact dodecahedral majority census concerns the different cubic dual graph, with twenty vertices rather than twelve and degree three rather than five. Duality of polyhedra does not conjugate their binary majority maps or imply one census from the other. A previously published icosahedral **three-state excitation** census studies a different local rule and state space. Neither is treated as a new result here, and no broad claim about all polyhedra is made.

## Limitations

The theorem concerns precisely the twelve-vertex icosahedral graph and synchronous binary neighbor-majority. The enumeration is a finite complete proof, not a closed formula for a growing graph family. The twelve cap supports and exact individual basin sizes are graph-specific. General fixed-or-two-periodicity is established prior work. Historical priority against unindexed equivalent finite tabulations remains an uncertainty; matching the dynamics under another graph labeling would be equivalent, not a new result.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1.
2. P. T. Tošić and G. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI 2004, pp. 861–870, https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, publicly posted 2014-05-11, https://arxiv.org/abs/1405.2486.
4. D. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of the Deterministic Majority Process*, MFCS 2016, https://doi.org/10.4230/LIPIcs.MFCS.2016.55.
5. E. W. Weisstein, *Icosahedral Graph*, MathWorld, https://mathworld.wolfram.com/IcosahedralGraph.html.
6. Published exact finite majority census on the dodecahedral graph, identifier `095dfb0decea` (2026); published finite icosahedral three-color excitation census, identifier `6295ce972482` (2026). These are graph- and model-specific comparison references, not sources of the present numerical conclusions.
