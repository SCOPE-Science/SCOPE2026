# Majority dynamics on the Folkman graph: a sharp seven-step clock and 26 basin sizes

## Finding

On the twenty-vertex **Folkman graph** under simultaneous binary open-neighbor majority with incumbent tie retention, the global update \(F\) satisfies the sharp identity
\[
\boxed{F^{9}=F^{7},\qquad F^{8}\ne F^{6}.}
\]
Of the \(2^{20}=1{,}048{,}576\) labelled initial states, exactly **4,036** are fixed configurations and **351** are primitive two-cycle orbits. There are no longer periodic orbits. The entire basin of eventual fixed points has **959,624** starting states; the aggregate two-cycle basin has **88,952**. The two unanimous configurations each attract exactly **207,670** starting states, so eventual unanimity occurs for **415,340** initial states.

The exact first-periodic-entry census, with entry time the smallest \(t\ge0\) such that \(F^{t+2}(x)=F^t(x)\), is

| \(t\) | Eventually fixed | Eventually two-periodic | Total |
| ---: | ---: | ---: | ---: |
| 0 | 4,036 | 702 | 4,738 |
| 1 | 190,408 | 14,210 | 204,618 |
| 2 | 228,340 | 57,720 | 286,060 |
| 3 | 321,920 | 16,320 | 338,240 |
| 4 | 178,600 | 0 | 178,600 |
| 5 | 33,440 | 0 | 33,440 |
| 6 | 1,920 | 0 | 1,920 |
| 7 | 960 | 0 | 960 |
| **Total** | **959,624** | **88,952** | **1,048,576** |

Exactly **960** states attain the sharp maximum entry time seven, all ending at fixed points. Initial bitmask `64030` is an explicit maximum-depth witness. The precise individual-basin catalog has 4,387 rows (one per attractor), embedded as `basin_catalog.tsv`, and its complete size-multiplicity spectrum is:

| Basin size | Fixed-point basins | Two-cycle basins |
| ---: | ---: | ---: |
| 1 | 384 | 0 |
| 2 | 0 | 60 |
| 3 | 480 | 0 |
| 4 | 120 | 0 |
| 16 | 0 | 240 |
| 18 | 160 | 0 |
| 21 | 120 | 0 |
| 25 | 120 | 0 |
| 28 | 120 | 0 |
| 30 | 240 | 0 |
| 38 | 60 | 0 |
| 55 | 720 | 0 |
| 56 | 720 | 0 |
| 72 | 120 | 0 |
| 76 | 240 | 0 |
| 86 | 120 | 0 |
| 124 | 120 | 0 |
| 152 | 60 | 0 |
| 284 | 20 | 0 |
| 899 | 0 | 40 |
| 1,368 | 60 | 0 |
| 4,038 | 0 | 10 |
| 4,249 | 40 | 0 |
| 8,652 | 0 | 1 |
| 12,190 | 10 | 0 |
| 207,670 | 2 | 0 |

The full spatial automorphism group has order **3,840** and partitions the recurrent attractors, with temporal phases identified, into **44 geometric fixed-point classes and eight geometric two-cycle classes**.

## Assumptions and scope

The graph uses the classical subdivided-double realization of the Folkman graph. Start with \(\{0,1,2,3,4\}\). For each \(i\), create two twin vertices \(u_{i,0}\) and \(u_{i,1}\). For each unordered pair \(\{i,j\}\), create an edge vertex \(e_{ij}\). Connect \(e_{ij}\) to \(u_{i,0},u_{i,1},u_{j,0},u_{j,1}\), and add no other edges. The resulting bipartite graph has ten twin vertices, ten edge vertices, 40 edges and degree four at every vertex. It is the standard smallest semisymmetric graph described by Folkman [1].

The **labelled bit encoding** is \(u_{i,0}\mapsto i\), \(u_{i,1}\mapsto5+i\), and \(e_{ij}\mapsto10+k\), with pairs \((i,j)\) enumerated lexicographically for \(0\le i<j<5\), beginning with \((0,1)\). Each state \(x\) is an integer in \([0,2^{20})\), with the value at vertex \(v\) given by bit \(v\). For any vertex \(v\), let \(c_v(x)=\sum_{w\sim v}x_w\). The update rule is exactly
\[
F(x)_v=\begin{cases}0&c_v(x)\le1,\\x_v&c_v(x)=2,\\1&c_v(x)\ge3.\end{cases}
\]
Every vertex is updated simultaneously. A temporal two-cycle \(\{a,b\}\) is counted once, not twice. Graph automorphisms are not identified when counting the 4,036 fixed states, 351 two-cycles, individual basins or initial states. They are identified only in the separate geometric-class census.

## Proof

**1. Exhaustive transition definition.** Both `verify_folkman.cpp` and `verify_folkman_functional.cpp` generate the stated twenty-vertex graph from the displayed pair construction; each checks that all twenty degrees are exactly four. The first independently builds adjacency arrays and computes every successor by summing four bits. The second constructs 20 integer neighbor masks and evaluates each successor with integer population counts. Each algorithm visits all integers \(0\le x<1{,}048{,}576\) without sampling. Their displayed local conditions implement the piecewise definition of \(F\), and hence determine the entire finite map.

**2. Two independent exhaustive orbit arguments.** The first program constructs \(F(x)\) for every state and compares \(F^t(x)\) against \(F^{t+2}(x)\) for successive \(t\). The first match at a state gives its entry time, and comparison to \(F^{t+1}(x)\) determines whether the orbit is fixed or two-periodic. This procedure finds the table above and that every state first satisfies two-step equality by \(t=7\), with 960 first doing so at seven. It also computes a representative \(\min\{F^7(x),F^8(x)\}\) for each attractor and counts its basin.

Independently, the second program constructs all \(1{,}048{,}576\) transitions using bit masks, removes zero-indegree vertices iteratively in the resulting functional digraph, and directly traverses each residual directed cycle. Every non-cycle vertex is removed because the forward orbit of a vertex not on a directed cycle eventually enters a cycle, while vertices on cycles always retain a predecessor on the same cycle. The residual cycles all have length one or two, giving 4,036 and 351 distinct cycles respectively. Processing removed vertices in reverse order assigns exactly one attractor and its distance to every starting state. This independent computation yields the same complete entry-period table, all 4,387 basin sizes and the exact 26-size spectrum. The sources hard-check the expected counts and sharp witness.

It follows for **every** state that \(F^7(x)\) lies on a cycle of period dividing two, i.e. \(F^9=F^7\). Since `64030` has first entry seven, \(F^8(64030)\ne F^6(64030)\); thus the cutoff is sharp. No claim about larger graph families follows from this finite enumeration.

**3. Complete basin identities.** The two unanimous bits `0` and `1048575` are fixed. The function-graph algorithm counts precisely 207,670 antecedents for each. Summing the sizes of all fixed attractor basins gives 959,624; summing the 351 oscillating basins gives 88,952; their sum is all \(2^{20}\) states. `basin_catalog.tsv` records for each attractor its least numerical periodic phase, least period, and number of initial states leading to it. The first checker rederives every representative and compares its basin count to the catalog, while the second generates the catalog directly.

**4. Geometric classes.** An automorphism must permute the five unique twin pairs, and can independently flip the members of each pair. Conversely every permutation of the five indices and every selection of flips preserves adjacency. The ten edge vertices are then uniquely determined by their four neighbors. Thus
\[
\operatorname{Aut}(G)\cong (C_2)^5\rtimes S_5,\qquad|\operatorname{Aut}(G)|=2^5\cdot5!=3{,}840.
\]
The second checker verifies adjacency preservation by three generators: the transposition \((0\ 1)\), the five-cycle \((0\ 1\ 2\ 3\ 4)\), and the flip of the twins at index zero. It traverses their action on all 4,387 labelled attractors, taking the smaller of two temporal phases as the oscillating-orbit representative, and finds 44 fixed and eight oscillating geometric classes. Since the generators produce all of \((C_2)^5\rtimes S_5\), this is the complete symmetry census.

## Verification

In a directory containing the embedded files, with any C++17 compiler, replay:

```sh
g++ -O3 -std=c++17 verify_folkman_functional.cpp -o check_functional
./check_functional
g++ -O3 -std=c++17 verify_folkman.cpp -o check_iterate
./check_iterate
```

The first run writes `basin_catalog.tsv` from the direct functional decomposition and validates all 26 spectrum entries and 52 spatial classes. The second independently reconstructs all successors and all first-entry and basin assignments, and cross-checks the catalog. Exact recorded standard output is embedded in `verification_functional.txt` and `verification_iterate.txt`. No floating-point arithmetic, stochastic sampling, oracle output or numerical extrapolation is used. The proof is a **complete finite exhaustive computation**, not a hand-derived closed form for arbitrary graph orders.

## Relationship to prior work

Folkman's original work [1] establishes the classical semisymmetric graph construction, not an opinion-dynamics classification. Goles and Olivos [2] proved the general eventual-period-one-or-two property of undirected threshold networks; Benjamini et al. [3] present that fact and investigate infinite and random graphs, including random quartic graphs, not this labelled twenty-vertex graph's fixed points, transients or attraction basins. The previously published dodecahedral majority census [4] concerns the nonisomorphic **three-regular** dodecahedron, and the prism/Desargues comparison [5] concerns two other **three-regular** twenty-vertex graphs. Their orbit and basin totals do not imply the graph-specific numbers here. No transfer or covering argument was found that supplies the Folkman calculations automatically. These antecedents are credited rather than claimed new.

## Limitations

The result applies only to this specifically defined twenty-vertex graph and tie-retaining synchronous rule. It provides no general theorem for all semisymmetric or four-regular graphs. A full computational proof requires executing the included exhaustive sources and preserving their integer arithmetic and indexing. Scholarly and published-record searches cannot rule out unindexed earlier exact enumerations or nomenclature variants. The original 1967 article was available at abstract level during the comparison, not in full text; it predates the cited majority-dynamics results and concerns symmetry rather than this dynamic rule. Independent external validation has not been performed.

## References

1. J. Folkman, *Regular line-symmetric graphs*, Journal of Combinatorial Theory 3 (1967), 215–232. https://doi.org/10.1016/S0021-9800(67)80069-3.
2. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. https://doi.org/10.1016/0012-365X(80)90121-1.
3. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486v1, first public preprint 2014-05-11, https://arxiv.org/abs/1405.2486.
4. *Dodecahedral majority dynamics: an exact recurrent, basin and symmetry census*, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-dodecahedral-majority-dynamics-an-exact-recurrent-basin-and-symm--095dfb0decea.
5. *Equal attractor counts but unequal basins for majority on the prism and Desargues graphs*, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-equal-attractor-counts-but-unequal-basins-for-majority-on-the-pr--fb9765d5d984.
6. M. Kovács, *Symmetry and Structure of Graphs*, CEU thesis (2014), Chapter 3, https://www.etd.ceu.edu/2014/kovacs_mate.pdf (Folkman graph's role in graph symmetry, not an opinion-dynamics census).
