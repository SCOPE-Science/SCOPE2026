# Exact majority attractor basins and a six-update clock on the Herschel graph

## Finding
For synchronous binary strict-neighbor majority with tie retention on the eleven-vertex Herschel graph, there are exactly **20 fixed configurations** and **61 primitive temporal two-cycle orbits**. Every one of the \(2^{11}=2048\) labelled configurations first enters its eventual periodic orbit after at most six updates. This is sharp: exactly 48 configurations require six updates, all ultimately reaching a fixed point. Equivalently, the global map satisfies \(F^8=F^6\), but not \(F^7=F^5\).

The **complete orbit-level attraction-basin spectrum** is:

| Eventual least period | Basin size | Number of distinct attractors |
|---|---:|---:|
| 1 | 1 | 6 |
| 1 | 7 | 12 |
| 1 | 501 | 2 |
| 2 | 4 | 24 |
| 2 | 8 | 12 |
| 2 | 14 | 6 |
| 2 | 25 | 6 |
| 2 | 27 | 12 |
| 2 | 206 | 1 |

The two basins of size 501 belong to the unanimous fixed states. The unique two-cycle basin of size 206 is strictly larger than all other two-cycle basins. Under the 12 graph automorphisms, the 20 fixed states form six spatial classes and the 61 temporal two-cycle orbits form eleven spatial classes.

The exact population indexed by *first periodic-entry time* \(t\) and *eventual least period* is:

| \(t\) | Eventually period 1 | Eventually period 2 | Total |
|---:|---:|---:|---:|
| 0 | 20 | 122 | 142 |
| 1 | 270 | 570 | 840 |
| 2 | 226 | 240 | 466 |
| 3 | 228 | 24 | 252 |
| 4 | 252 | 0 | 252 |
| 5 | 48 | 0 | 48 |
| 6 | 48 | 0 | 48 |
| Total | 1092 | 956 | 2048 |

## Assumptions and scope
Let \(H\) be the simple undirected graph with vertex labels \(1,\ldots,11\) and the following complete 18-edge list:

```text
1-2  1-4  1-5  2-3  2-6  2-7  3-4  3-8  4-9
4-10  5-6  5-10  6-11  7-8  7-11  8-9  9-11  10-11
```

This is the Herschel graph as depicted in the referenced 2011 instructional illustration; the edge list is independently checked to be connected, planar, bipartite, 3-vertex-connected, and to have degree multiset eight 3s and three 4s. No graph isomorphism ambiguity enters the claim, because all calculations use the above explicit labels.

For \(x\in\{0,1\}^{11}\), write \(d_i\) for the degree of vertex \(i\) and \(s_i(x)=\sum_{j\sim i}x_j\). Define the synchronous update simultaneously at every vertex by

\[
F(x)_i=\begin{cases}
1,&2s_i(x)>d_i,\\
0,&2s_i(x)<d_i,\\
x_i,&2s_i(x)=d_i.
\end{cases}
\]

There are no self-loops. Every initial state is counted separately with the stated vertex labels, and an attractor basin includes the recurrent orbit itself. A primitive two-cycle is an unordered pair \(\{x,F(x)\}\) with \(F^2(x)=x\ne F(x)\). The first periodic-entry time is the least nonnegative \(t\) for which \(F^t(x)\) is on a periodic orbit.

## Proof
This is an **exhaustive, finite, fully specified computational proof** on 2048 states, not an extrapolation from samples. The two embedded checker programs are independently written and each traverses every possible initial state.

**Construction of the complete functional digraph.** Represent a state uniquely as an integer \(a\) in \(\{0,\ldots,2047\}\), with vertex \(i\) storing bit \(i-1\). For every such \(a\), `check_functional.py` computes the 11 output bits by the displayed majority rule, using the hard-coded adjacency tuples, and stores the resulting integer \(f[a]\). The program asserts that the adjacency relation is symmetric and has exactly 18 edges.

**Exhaustive orbit decomposition.** For each of the 2048 starting states, follow successive values of \(f\), keeping a dictionary of states already encountered along the current path. If the path hits a state with an already resolved root, propagate that root backward and increase its first-entry depth by one at every preceding edge. If it repeats a state within the current path, exactly the repeated suffix is a directed cycle; mark each cycle member as depth zero, then propagate the new cycle root and first-entry depths backward along the preceding path. The finite functional-graph argument guarantees that every state is resolved and assigned its *unique* eventual orbit and least entry time. The code asserts completion, confirms that every cycle has length one or two, and aggregates all attractor basins and entry-time populations.

**Numerical exactness and finite completeness.** All operations are on small nonnegative integers, exact bit tests, finite sets, and integer counters; no tolerance, numerical approximation, Monte Carlo sampling or stochastic assumption occurs. The first checker asserts every displayed entry and spectrum, including the global identities \(F^8=F^6\) and \(F^7\ne F^5\), by evaluating both sides for all 2048 inputs. The second checker, `check_trajectory_symmetry.py`, builds the graph from an independently recorded edge list and evaluates each trajectory directly in 11-bit tuples until its first repeated state. It verifies the same event-time/period counts and basin spectra without using the first checker's transition table or functional-graph propagation.

**Geometric orbit classes.** The second program independently enumerates all graph automorphisms by graph isomorphism backtracking. It checks the graph is planar, bipartite and 3-connected; exactly 12 automorphisms result. It acts on each complete attractor, explicitly constructs its orbit under automorphisms, and verifies that each resulting temporal orbit is present and has the same period and basin size. The class-size/multiplicity/basin-size signatures are:

```text
(period, orbit-class size, basin size) : number of spatial classes
(1,1,501):2; (1,3,1):2; (1,6,7):2
(2,1,206):1; (2,3,14):2; (2,3,25):2
(2,6,8):2; (2,6,27):2; (2,12,4):2
```

These signatures sum to 20 fixed attractors and 61 two-cycle attractors and therefore establish the six and eleven class totals.

## Verification
Run from the directory containing the three files:

```bash
python check_functional.py
python check_trajectory_symmetry.py
```

The first program uses only the Python standard library. The second requires `networkx` for graph and automorphism checks; its trajectory update and traversal are otherwise independent of that library. Both were executed and passed from the complete candidate package. They agree on all 2048 states, all 81 attractors, all displayed basin spectra and entry times; the second additionally certifies graph symmetry classes. The first-entry histogram sums to 2048, the period-one basins sum to 1092, and the period-two basins sum to 956.

## Relationship to prior work
Goles and Olivos established the general eventual period-one-or-two phenomenon for finite synchronous symmetric threshold dynamics. Kuhlman, Mortveit, Murrugarra, and Kumar extended the corresponding structural discussion to synchronous bi-threshold graph systems; see their Corollary 3.6 and Sections 3–5. Those general results do not themselves determine any of the Herschel-specific recurrent counts, full basin-size spectrum, first-entry cutoff or automorphism orbit classes reported here.

The Herschel graph is the smallest non-Hamiltonian polyhedral graph and is a natural canonical eleven-vertex test network. Earlier graph-specific exhaustive majority results for the Heawood, Pappus, Chvátal and other networks concern different graphs, not an exhaustive dynamics on this explicit 18-edge Herschel network. Search comparisons cannot exclude unindexed earlier computations.

## Limitations
The theorem concerns **only** the explicitly listed eleven-vertex graph, synchronous binary updates, strict open-neighbor majority, and retention of the current bit on a tie. It does not assert an all-graph theorem, a bound for other polyhedral graphs, robustness under edge modifications, or new general period-two theory. The finite-state proof is reproducible but does not constitute an independently performed audit. Historical priority is assessed against accessible literature and records, not certified uniquely.

## References
1. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, and V. S. A. Kumar, *Bifurcations in Boolean Networks*, first public preprint 2011-08-15, arXiv:1108.2974, https://arxiv.org/abs/1108.2974. See Section 3.1, Corollary 3.6, and Appendix A.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, *Discrete Mathematics* (1980), https://doi.org/10.1016/0012-365X(80)90121-1.
3. *Herschel Graph*, graph diagram and vertex labels in the University of Washington 2011 instructional collection, https://faculty.washington.edu/moishe/hanoi-2011/DO-2011/Week-8/Supplements/Herschel%20Graph.pdf.
4. *Herschel graph*, MathWorld, https://mathworld.wolfram.com/HerschelGraph.html (background on the canonical graph, not an orbit-census source).
