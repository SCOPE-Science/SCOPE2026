# A twenty-one-step excitation transient on the asymmetric Frucht graph

## Finding

For the 12-vertex Frucht graph with the exact labeled edge set below, the synchronous three-state Greenberg–Hastings excitation rule has exactly \(3^{12}=531441\) labeled initial configurations. Their eventual least periods are exactly \(1,3,4,5,6,7,8\); the complete orbit and first-periodic-entry census is given here and in `census.json`. The sharp maximum entry time is \(21\), attained by exactly three initial configurations, all entering primitive period-three orbits. There are precisely 74 nonempty pairs of entry time and eventual least period.

The numbers of primitive periodic orbits, periodic states, and all states eventually entering that period are:

| Least period | Primitive orbits | Periodic states | Entire attracting population |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 1 | 52563 |
| 3 | 1912 | 5736 | 282990 |
| 4 | 22 | 88 | 64448 |
| 5 | 10 | 50 | 90432 |
| 6 | 2 | 12 | 24636 |
| 7 | 28 | 196 | 12840 |
| 8 | 4 | 32 | 3532 |

The number of periodic states is \(6115\), distributed among \(1979\) distinct primitive orbits. The entry-time maximum is larger than the graph's vertex count and diameter; the latter is \(4\). The maximizing initial configurations, in the vertex order defined below, have integer encodings \(190008\), \(190010\), and \(436809\). Their exact 25-step trajectories are in `extremal_witnesses.json`.

## Assumptions and scope

The graph has vertex set \(\{0,1,\ldots,11\}\) and edges

```
(0,1) (0,6) (0,7) (1,2) (1,7) (2,3)
(2,8) (3,4) (3,9) (4,5) (4,9) (5,6)
(5,10) (6,10) (7,11) (8,9) (8,11) (10,11)
```

This edge list is isomorphic to the standard Frucht graph represented by LCF offsets
`(-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)`; an explicit isomorphism is checked by the independent verifier. The graph is cubic, has twelve vertices, and has trivial automorphism group.

The state at vertex \(v\) is \(0\) (resting), \(1\) (excited), or \(2\) (refractory). A resting site becomes excited precisely if at least one neighbor is excited; a site in state \(1\) becomes \(2\), and state \(2\) becomes \(0\). All vertices update synchronously. Encode a configuration \((c_0,\ldots,c_{11})\) by the integer \(s=\sum_{i=0}^{11}c_i3^i\). Define \(T(s)\) to be the smallest \(t\ge0\) for which \(F^t(s)\) is periodic; \(P(s)\) is the least positive period of that eventual periodic state. A configuration already on a cycle has \(T=0\).

## Proof

There are exactly \(3^{12}\) distinct encodings, with no collision or omission. `verify_functional_graph.py` constructs the transition function explicitly for every encoding and counts the indegree of each target. It repeatedly removes vertices of indegree zero in the functional digraph. A finite directed graph of outdegree one has a unique eventual directed cycle in every weak component, and indegree peeling deletes exactly the vertices not on directed cycles. Hence each remaining vertex belongs to one of the genuine primitive periodic orbits; traversing each such cycle once determines its exact least period.

The reverse deletion order ensures that the successor of each removed state has already been classified, so the recurrences \(T(s)=T(F(s))+1\) and \(P(s)=P(F(s))\) uniquely determine its first periodic entry and eventual least period. Each encoded initial configuration contributes exactly one unit to one table cell. The program counts all states, verifies the peeled-plus-cycle partition, and checks that every state received a positive eventual period. The computed table contains exactly the following nonzero entries:

| First entry \(T\) | Least period \(P\) | Configurations |
| ---: | ---: | ---: |
| 0 | 1 | 1 |
| 0 | 3 | 5736 |
| 0 | 4 | 88 |
| 0 | 5 | 50 |
| 0 | 6 | 12 |
| 0 | 7 | 196 |
| 0 | 8 | 32 |
| 1 | 1 | 4095 |
| 1 | 3 | 4520 |
| 1 | 4 | 1768 |
| 1 | 5 | 4082 |
| 1 | 6 | 1268 |
| 1 | 7 | 1166 |
| 1 | 8 | 388 |
| 2 | 1 | 15763 |
| 2 | 3 | 18684 |
| 2 | 4 | 8922 |
| 2 | 5 | 21012 |
| 2 | 6 | 6005 |
| 2 | 7 | 3554 |
| 2 | 8 | 1248 |
| 3 | 1 | 15136 |
| 3 | 3 | 44113 |
| 3 | 4 | 14230 |
| 3 | 5 | 26272 |
| 3 | 6 | 7370 |
| 3 | 7 | 4076 |
| 3 | 8 | 1513 |
| 4 | 1 | 8780 |
| 4 | 3 | 58867 |
| 4 | 4 | 12943 |
| 4 | 5 | 17608 |
| 4 | 6 | 3660 |
| 4 | 7 | 2601 |
| 4 | 8 | 351 |
| 5 | 1 | 7284 |
| 5 | 3 | 54818 |
| 5 | 4 | 10435 |
| 5 | 5 | 12766 |
| 5 | 6 | 3075 |
| 5 | 7 | 1117 |
| 6 | 1 | 1504 |
| 6 | 3 | 39256 |
| 6 | 4 | 6553 |
| 6 | 5 | 7790 |
| 6 | 6 | 2135 |
| 6 | 7 | 130 |
| 7 | 3 | 22255 |
| 7 | 4 | 3013 |
| 7 | 5 | 852 |
| 7 | 6 | 1111 |
| 8 | 3 | 13868 |
| 8 | 4 | 2197 |
| 9 | 3 | 8590 |
| 9 | 4 | 1268 |
| 10 | 3 | 5270 |
| 10 | 4 | 652 |
| 11 | 3 | 3196 |
| 11 | 4 | 647 |
| 12 | 3 | 1801 |
| 12 | 4 | 561 |
| 13 | 3 | 908 |
| 13 | 4 | 492 |
| 14 | 3 | 478 |
| 14 | 4 | 323 |
| 15 | 3 | 285 |
| 15 | 4 | 252 |
| 16 | 3 | 168 |
| 16 | 4 | 104 |
| 17 | 3 | 101 |
| 18 | 3 | 52 |
| 19 | 3 | 15 |
| 20 | 3 | 6 |
| 21 | 3 | 3 |

Summing all 74 table entries gives \(531441\). The rows show that no initial configuration has entry time above \(21\); the cell \((T,P)=(21,3)\) has population exactly \(3\). The three configurations are listed explicitly above and in the witness file. The 25 successive states recorded for each witness certify a least-period-three state reached at time \(21\) and no earlier periodic state, independently of the aggregate sums.

`verify_trajectories.py` recomputes the same exhaustive classification by an independent path-memoization algorithm instead of indegree peeling. It constructs the Frucht graph from the Hamiltonian-cycle/LCF description, not from the edge list used in the first program, checks an explicit graph isomorphism, and independently computes every transient and every primitive least period. Its complete 74-cell census has the same SHA-256 digest as the first enumeration. The two algorithms agree on the exact three maximizing initial configurations after relabeling, and on all periodic-orbit counts.

## Verification

From this directory, on Python 3 with only the standard library:

```
python3 verify_functional_graph.py
python3 verify_trajectories.py
```

Both print `VERIFY_OK`; captured outputs appear in `functional_graph_output.txt` and `trajectories_output.txt`. The canonical serialization of the 74-element `entrance_census` array is JSON with no inter-item whitespace, and both independent implementations yield SHA-256 `4952acb8915363cd777640d517b5e4db0dfb3d3692357ca7c4f92d30f1d052a7`.

The proof is finite and exhaustive for this one fixed graph, not an extrapolation from sampling or a claim about all asymmetric cubic graphs. Both programs examine all \(531441\) configurations, either directly or by memoized deterministic trajectories.

## Relationship to prior work

The Frucht graph is a canonical cubic graph with a trivial automorphism group. The graph is described in MathWorld and the NetworkX graph catalog. Gravner, Lyu, and Sivakoff (arXiv:1610.07320v1, October 24, 2016) develop circulation/synchronization criteria for three-color Greenberg–Hastings dynamics on arbitrary graphs. Their Theorem 3 characterizes whether a trajectory synchronizes and an asymptotic activity parameter, but does not enumerate exact primitive periods, all first-periodic-entry classes, or the twenty-one-step extremal population for this graph. The present finite-state enumeration supplements rather than contradicts these general statements.

## Limitations

The result concerns the specified graph and the specified simultaneous three-state excitation rule only. No assertion is made that the transient is extremal among all 12-vertex or cubic graphs. No explanation of the value \(21\) in terms of a universal structural formula, and no asymptotic family theorem, is claimed. The full enumeration is a reproducible computer-assisted finite proof, not a manually derived closed form. The available literature comparison does not exclude an unindexed previously published census of this graph, and an independent audit has not been performed.

## References

1. R. Frucht, "Herstellung von Graphen mit vorgegebener abstrakter Gruppe," *Compositio Mathematica* **6** (1939), 239–250. Historical description of graph symmetry realizations; day-resolved public access date is not asserted.
2. E. W. Weisstein, "Frucht Graph," MathWorld, https://mathworld.wolfram.com/FruchtGraph.html . Frucht graph structure and LCF labeling.
3. NetworkX, `frucht_graph` graph catalog documentation, https://networkx.org/documentation/networkx-3.4.1/reference/generated/networkx.generators.small.frucht_graph.html .
4. J. Gravner, H. Lyu, D. Sivakoff, "Limiting behavior of 3-color excitable media on arbitrary graphs," arXiv:1610.07320v1 (first public 2016-10-24), https://arxiv.org/abs/1610.07320 .
