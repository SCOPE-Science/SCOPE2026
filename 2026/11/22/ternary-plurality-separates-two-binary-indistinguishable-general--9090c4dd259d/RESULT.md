# Ternary plurality separates two binary-indistinguishable generalized Petersen graphs

## Finding

The pentagonal prism \(GP(5,1)\) and the Petersen graph \(GP(5,2)\) have identical numbers of binary strict-majority fixed points and primitive temporal two-cycles: \(14\) and \(55\), respectively. Under the deterministic **three-opinion** synchronous plurality rule with incumbent retention when all three neighbor colors are different, the corresponding exact populations diverge sharply. The following counts refer to indexed vertex configurations, with phases identified only when counting primitive temporal cycles.

| Exact quantity | Pentagonal prism \(GP(5,1)\) | Petersen graph \(GP(5,2)\) |
| --- | ---: | ---: |
| Binary fixed configurations | 14 | 14 |
| Binary primitive two-cycle orbits | 55 | 55 |
| Ternary fixed configurations | 219 | 579 |
| Ternary primitive two-cycle orbits | 1,410 | 2,175 |
| Ternary initial states eventually fixed | 17,049 | 37,899 |
| Ternary initial states eventually two-periodic | 42,000 | 21,150 |
| Ternary initial states reaching a unanimous fixed configuration | 12,063 | 33,543 |
| Sharp maximal first-periodic-entry time | 5 | 7 |

Both ternary state spaces contain exactly \(3^{10}=59{,}049\) configurations. The Petersen graph has **more** primitive two-cycle orbits (\(2{,}175>1{,}410\)) but **fewer** initial configurations attracted to them (\(21{,}150<42{,}000\)): an exact attractor-count versus basin-volume inversion. Among the fixed configurations, the three monochromatic and the \(36\) exactly bichromatic states are identical in number for the two graphs. The full equilibrium discrepancy comes from genuinely trichromatic equilibria: \(180\) on the prism versus \(540\) on the Petersen graph.

## Assumptions and scope

Let \(k\in\{1,2\}\). The graph \(GP(5,k)\) has vertices \(u_i,v_i\) for \(i\in\mathbb Z/5\mathbb Z\), with edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+k}\), indexing modulo five. There are ten labelled vertices, fifteen undirected edges, and exactly three distinct neighbors per vertex. Use the palette \(\{0,1,2\}\). For a configuration \(x\), its synchronous successor \(F_k(x)\) at vertex \(v\) is the most frequent neighbor color when that most frequent color is unique; when the three neighbor colors are all different, retain \(x_v\). No self-neighbor is included, and no spatial or color relabellings are identified in the counts. In the binary comparison the update is ordinary strict neighbor majority on the same graph, with the palette \(\{0,1\}\).

Let \(T(x)\) be the least nonnegative integer such that \(F_k^{T(x)}(x)\) is periodic, and \(p(x)\) the least eventual period. An orbit is one directed cycle in the full state-transition graph. A basin includes the orbit itself and all configurations eventually reaching it. A unanimous equilibrium assigns a single color to all ten vertices.

## Proof

**Exact transition construction.** Order the vertices as \((u_0,\ldots,u_4,v_0,\ldots,v_4)\). Every ternary configuration is encoded exactly once by the integer \(s=\sum_{j=0}^{9}x_j3^j\) in the complete range \(0\le s<59{,}049\). Write the three neighbor colors at vertex \(v\) as \((a,b,c)\). Then the update digit is \(a\) if \(a=b\) or \(a=c\), otherwise \(b\) if \(b=c\), and otherwise the current digit \(x_v\). This is precisely the stated plurality-with-incumbent-ties rule, since with three neighbors a unique plurality occurs if and only if at least two agree. The standalone C++ source `verification/peeling.cpp` constructs the two adjacency lists from the displayed edges and computes the entire function \(F_k\) on all \(59{,}049\) integers, using only exact integer operations.

**Why the classification is exhaustive.** Any finite function \(f:S\to S\) defines a directed graph with exactly one outgoing edge per state. Recursively remove every vertex of indegree zero, recording removal order. A removed vertex cannot belong to a directed cycle. Conversely, if a noncycle vertex remained, its finite upstream transient tree would have an indegree-zero vertex, a contradiction. Thus the remaining vertices are precisely the recurrent cycles. The C++ checker performs this complete peeling, traverses all remaining cycles, sets \(T=0\) on them, and processes deleted vertices in reverse order with the recurrences \(T(x)=1+T(f(x))\) and \(p(x)=p(f(x))\). Every one of the \(59{,}049\) states therefore receives exactly one eventual period, one first-entry time, and one orbit identifier; counting these integer arrays proves the theorem's finite values. The source is the executable complete certificate, not a Monte Carlo sample or an inference from some bounded trajectory sample.

**Exact output and independent check.** `verification/peeling_output.txt` gives all first-entry-by-period populations and the complete orbit-basin-size histograms for both graphs. Its fixed-point population checks also separate supports of sizes one, two, and three as \((3,36,180)\) and \((3,36,540)\). Independently, `verification/direct_trace.py` reconstructs each graph with Python sets, uses `Counter`-based local plurality rather than the C++ digitwise condition, and follows actual trajectories until the first repeated state, memorizing cycles and predecessor paths. It independently recovers the two complete period, first-entry, and basin histograms; see `verification/direct_trace_output.txt`. The same program separately enumerates all \(2^{10}=1{,}024\) binary starting states on each graph to verify the shared binary orbit counts \((14,55)\). The distinct exact algorithms agree on all reported invariants.

**Sharpness and basin inversion.** For the prism a least-encoded maximal-depth witness has successive states \(286,94,31,90,27,0,0\), becoming fixed after exactly five updates. For the Petersen graph a witness follows \(1106,26377,1105,26374,1093,28552,22963,29524,29524\), becoming fixed after seven updates. These paths are directly regenerated by the C++ transition map. No state has a larger depth because the enumerator checks the entire state set. Summing the basin populations from the complete classification gives the table; for each graph the two eventual-period populations sum to exactly \(59{,}049\). Since the update never introduces a previously absent color, the ternary fixed points supported on at most two colors amount to the three unanimous states plus \(3(14-2)=36\) exactly bichromatic ones. The remaining fixed points number \(219-39=180\) and \(579-39=540\), respectively. This proves that the extra \(360\) equilibria are necessarily genuinely three-color phenomena, not binary states under a renamed palette.

## Verification

Run from a directory containing the embedded `verification` folder:

```sh
g++ -std=c++17 -O2 -Wall -Wextra verification/peeling.cpp -o plurality_peeling
./plurality_peeling
python3 verification/direct_trace.py
```

Compare the first output with `verification/peeling_output.txt` and the second with `verification/direct_trace_output.txt`. Both programs need only standard library facilities and are deterministic. Their transition encodings and traversal algorithms are independent. All enumerated states are treated as labelled, without orbit quotienting by graph automorphisms or global palette permutations. The explicit source plus exhaustive coverage and independent output agreement constitute finite proof of these **particular** graph counts.

## Relationship to prior work

Mossel, Neeman and Tamuz (2012) study plurality/majority on social networks and establish eventual period at most two under an explicit no-ties weighted assumption. Their Section 6.2 uses rationally independent edge weights to remove ties; this does not identify the fixed points, attraction basins or sharp entry times of the present *unweighted tie-retaining* ten-vertex maps. Becchetti and collaborators (2013) study a sampled random-neighbor plurality protocol on a complete communication network, not these deterministic fixed-neighborhood transitions. The published binary generalized-Petersen majority recurrence results already give the binary \(14/55\) equality at circumference five; that equality is a **comparison baseline**, not claimed as new. Published three-state excitation results on these same two graphs use a refractory/excitation update rule and have long recurrent periods, unlike the plurality rule. Consequently neither the binary-majority recurrence results nor the excitation results imply this ternary plurality classification. No historical priority claim is made for the general finite-map peeling method or the general plurality-periodicity argument.

## Limitations

The conclusions concern exactly two ten-vertex graphs, one deterministic unweighted three-color tie-retaining update rule, and one binary comparison. No theorem is claimed for arbitrary generalized Petersen graphs, arbitrary alphabets, other tie policies, stochastic voting, or asynchronous updating. The precise finite census is established by complete executable enumeration rather than a short symbolic closed form for all basin sizes. Literature comparison cannot exclude unpublished, unindexed or differently formulated earlier calculations. Independent external scientific validation has not been performed.

## References

1. E. Mossel, J. Neeman and O. Tamuz, *Majority Dynamics and Aggregation of Information in Social Networks*, arXiv:1207.0893, first submitted 2012-07-04, https://arxiv.org/abs/1207.0893. In particular, Sections 1 and 6.2.
2. L. Becchetti, A. Clementi, E. Natale, F. Pasquale, R. Silvestri and L. Trevisan, *Simple Dynamics for Plurality Consensus*, arXiv:1310.2858, first submitted 2013-10-10, https://arxiv.org/abs/1310.2858. In particular, its random-neighbor protocol definition in Section 2.
3. *An equilibrium–oscillation entropy reversal on generalized Petersen graphs*, published mathematical result (2026); exact binary-majority transfer and circumference-five table.
4. *Exact recurrence and basins on the two ten-vertex generalized Petersen graphs*, published mathematical result (2026); the three-state refractory/excitation comparison.
