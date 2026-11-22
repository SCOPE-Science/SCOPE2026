# Geometric rigidity of vertex-edge dominant edge-metric bases of the four- and five-cubes

## Finding

Let \(Q_d\) be the binary \(d\)-cube, with vertex set \(\{0,1\}^{d}\) and edges joining strings at Hamming distance one. A *vertex-edge dominant edge-resolving set* \(S\) both distinguishes every pair of edges by their distance vectors to \(S\) and covers every edge within vertex-to-edge distance at most one.

For \(d=2,3,4,5\), its minimum size and number of labelled minimum sets are, respectively,

| \(d\) | Minimum size \(\gamma_{emd}(Q_d)\) | Number of minimum sets | Cube-symmetry orbit sizes |
|---|---:|---:|---|
| 2 | 2 | 4 | 4 |
| 3 | 3 | 32 | 8, 24 |
| 4 | 4 | 176 | 16, 64, 96 |
| 5 | 5 | 160 | 160 |

In particular, the ordinary edge-metric dimension is \(3\) for \(Q_4\) and \(4\) for \(Q_5\), but no minimum ordinary edge-resolving set of either cube also vertex-edge dominates the edges. Adding exactly one landmark is necessary and sufficient in both dimensions.

Every four-cube minimum set belongs to exactly one of the following three geometric families:

1. The four vertices of one parity within a three-dimensional facet (\(16\) sets).
2. Three of the four neighbors of a vertex \(c\), together with its antipode \(\bar c\) (\(64\) sets).
3. An antipodal pair \(\{u,\bar u\}\), together with two further vertices of the same bipartition class as \(u\), which are not antipodal to each other (\(96\) sets).

Every five-cube minimum set has exactly the form

\[
\{\bar c\}\cup (N(c)\setminus\{w\}),
\qquad c\in V(Q_5),\quad w\in N(c).
\]

There are exactly \(32\cdot5=160\) such sets, constituting one full automorphism orbit. For completeness, the \(Q_3\) minimum sets are the eight three-element subsets contained in a single parity class and the twenty-four vertex sets of induced length-two paths; the \(Q_2\) minima are precisely its four edges.

## Assumptions and scope

All graphs are finite, simple, undirected binary cubes of exactly the listed dimensions. For an edge \(e=ab\) and a vertex \(s\), put \(\delta(s,e)=\min\{d(s,a),d(s,b)\}\). A landmark set resolves edges when the vectors \((\delta(s,e))_{s\in S}\) are pairwise distinct as \(e\) ranges over all edges. It vertex-edge dominates when \(\min_{s\in S}\delta(s,e)\le1\) for every edge. These are distinct requirements; the vertex-edge domination condition does **not** demand a vertex cover. The cube antipode is bitwise complementation \(\bar c\); parity is the parity of Hamming weight.

## Proof

**Distance reduction.** Index vertices by integers \(0,\ldots,2^d-1\) interpreted as binary strings. Every edge is uniquely \(e=(x,x\oplus 2^j)\) with bit \(j\) of \(x\) zero. A shortest cube path changes exactly the differing coordinates. Consequently,

\[
\delta(s,e)=\sum_{i\ne j}(s_i\oplus x_i).
\]

This explicit identity fixes the full finite universe of edges (\(d2^{d-1}\) of them), all edge-distance signatures and all coverage tests, without invoking any graph-theoretic oracle. Equivalently, the conditions can be represented by masks \(M_{e,f}=\{s:\delta(s,e)\ne\delta(s,f)\}\) and \(C_e=\{s:\delta(s,e)\le1\}\). A subset \(S\) is valid exactly when it intersects every \(M_{e,f}\) for distinct edges and every \(C_e\).

**Exhaustive finite reduction.** For each \(d\in\{2,3,4,5\}\), enumerate each unordered subset of cardinality \(d-1\) and \(d\) exactly once, by strictly increasing integer tuples. A subset passes the resolving test iff no two edges share a signature; it passes coverage iff every edge has a landmark at distance zero or one. The complete exhaustive certificate gives:

| Cube | Subsets of size \(d-1\) resolving edges | Subsets of size \(d-1\) covering edges | Subsets passing both at size \(d-1\) | Subsets passing both at size \(d\) |
|---|---:|---:|---:|---:|
| \(Q_2\) | 0 | 4 | 0 | 4 |
| \(Q_3\) | 0 | 16 | 0 | 32 |
| \(Q_4\) | 64 | 112 | 0 | 176 |
| \(Q_5\) | 1280 | 80 | 0 | 160 |

For the two higher cubes, the same certificate also checks that no \(2\)-set resolves edges of \(Q_4\) and no \(3\)-set resolves edges of \(Q_5\), establishing their ordinary edge-metric dimensions independently. Both joint properties are monotone under addition of landmarks. Thus the absence at cardinality \(d-1\) excludes **every** smaller cardinality. The existence at cardinality \(d\) proves the minima. In particular, the enumerations cover \(\binom{16}{3}+\binom{16}{4}=2380\) subsets for \(Q_4\) and \(\binom{32}{4}+\binom{32}{5}=237336\) for \(Q_5\), not a sample of selected configurations.

**Classification and orbits.** Construct explicitly the families in the Finding. Their counts follow without overcounting: a four-cube parity facet has \(4\cdot2\cdot2=16\) choices; a three-neighbors-plus-antipode set has \(16\cdot4=64\) choices, with its unique minority-parity point recovering the center; an antipodal-pair set has \(8(\binom62-3)=96\) choices, with its unique antipodal pair recovering the first choice. These three families are disjoint by their parity and antipodal signatures. In \(Q_5\), the antipodal outlier is the unique vertex at Hamming distance four from each of the other four, recovering \(c\) and the omitted neighbor, so the \(32\cdot5\) choices are distinct.

The scripts independently construct these explicit families and compare them by **set equality**, not merely cardinality, with every configuration passing both defining tests. Cube automorphisms consist of all bit translations and coordinate permutations. They act transitively on each specified geometric family; the distinct Hamming-distance and parity patterns prevent merging of the three four-cube families. Hence the orbit sizes are exactly those stated. The same explicit construction gives the two three-cube families and the four two-cube edge bases.

## Verification

The included `verify_masks.cpp` implements the integer Hamming-distance formula, precomputes an exact vertex-separating mask for every unordered edge pair and an exact coverage mask for each edge, and exhaustively tests all \((d-1)\)- and \(d\)-subsets. Independently, `verify_independent.py` constructs cube adjacency lists, computes distances by breadth-first search from every vertex, tests full distance-vector uniqueness directly and compares all passing sets with the geometric families. The two implementations have different graph-distance and validity-test algorithms.

Run from the directory containing the two source files:

```sh
python3 verify_independent.py
g++ -std=c++17 -O2 verify_masks.cpp -o verify_masks
./verify_masks
```

Each script prints the four rows in the proof table and its own final success token (`CUBE_VE_EDGE_PY_OK` or `CUBE_VE_EDGE_CPP_OK`). The explicit assertions also check family equality. No random sampling, floating-point arithmetic, external graph data, or unprovided packages are used.

## Relationship to prior work

Ikhlaq, Hayat and Siddiqui introduced the joint *vertex-edge dominant edge-metric dimension* and studied common graphs and some Cartesian products, but did not classify these binary cubes. Kelenc, Teo Masa Toshi, Škrekovski and Yero established relationships among the ordinary metric, edge-metric and mixed metric dimensions of hypercubes, including \(\operatorname{edim}(Q_4)=3\). Those results do not impose the additional edge-coverage requirement and therefore do not imply the new joint optimum or its geometric classification. A different 2023 parameter called *dominant edge metric dimension* uses a **vertex cover** as the coverage condition; it is strictly stronger than vertex-edge domination and must not be conflated with the present invariant.

## Limitations

The classification and numerical statement concern dimensions \(2\) through \(5\) only. No formula for \(\gamma_{emd}(Q_d)\) or all its optimizers for \(d\ge6\) is asserted. Exhaustive small-cube enumeration does not imply any infinite-dimensional classification. Independent mathematical validation and exhaustive historical-priority clearance remain outstanding.

## References

1. H. M. Ikhlaq, S. Hayat, H. M. A. Siddiqui, *Unique identification and domination of edges in a graph: The vertex-edge dominant edge metric dimension*, arXiv:2211.09327, first submitted 17 November 2022, https://arxiv.org/abs/2211.09327.
2. A. Kelenc, A. T. M. Toshi, R. Škrekovski, I. G. Yero, *On Metric Dimensions of Hypercubes*, arXiv:2102.10916, first submitted 22 February 2021, https://arxiv.org/html/2102.10916v1.
3. M. Tavakoli, M. Korivand, A. Erfanian, G. Abrishami, E. T. Baskoro, *The dominant edge metric dimension of graphs*, Electronic Journal of Graph Theory and Applications 11 (2023), DOI:10.5614/ejgta.2023.11.1.16, https://www.ejgta.org/index.php/ejgta/article/view/1686.
