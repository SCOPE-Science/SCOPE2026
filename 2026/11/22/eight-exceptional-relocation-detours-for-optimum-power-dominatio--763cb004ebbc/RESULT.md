# Eight exceptional relocation detours for optimum power domination of the McGee seven-cage

## Finding

Let \(M\) be the 24-vertex McGee graph, the unique cubic seven-cage (minimum-order cubic graph of girth seven). Its ordinary power-domination number is \(\gamma_P(M)=3\), and it has precisely \(576\) minimum power-dominating three-vertex sets. On these sets, let \(J\) allow an exchange of one selected vertex for any unselected vertex, and let \(T\) allow the same exchange only when the old and new vertices are adjacent in \(M\). Only minimum power-dominating sets are permitted as intermediate configurations.

Both reconfiguration graphs are connected. The jump graph has \(6{,}184\) edges, radius four and diameter four; the slide graph has \(1{,}328\) edges, radius eight and diameter nine. Every pair \(S,U\) of minimum configurations satisfies
\[
0\le d_T(S,U)-d_J(S,U)\le7.
\]
The upper bound is sharp for exactly eight unordered pairs, each with \(d_J(S,U)=1\) and \(d_T(S,U)=8\). These pairs are disjoint: they form a matching on sixteen configurations.

The slide eccentricity distribution is \(432\) configurations of eccentricity eight and \(144\) of eccentricity nine. Among the \(576\) optima, \(144\) complete observation after two synchronous forcing waves, \(272\) after three, and \(160\) after four, counting waves after the initial closed-neighborhood observation.

## Assumptions and scope

On vertices \(\{0,\ldots,23\}\), add each cycle edge from \(i\) to \(i+1\pmod{24}\) and a chord from \(i\) to \(i+c_i\pmod{24}\), with period-three sequence \((c_0,c_1,c_2)=(12,7,-7)\). Count each undirected edge once. This is the McGee LCF representation; the graph has 36 edges, degree three, girth seven and diameter four. The calculation uses this explicit graph, not a classification of cubic graphs.

For selected set \(S\), put \(B_0=N_M[S]\). Obtain \(B_{t+1}\) from \(B_t\) by adding every unobserved vertex \(w\) for which some \(v\in B_t\) has \(N_M(v)\setminus B_t=\{w\}\). The set power dominates if some \(B_t\) is the whole graph. Minimum means smallest cardinality. Distances in the two exchange graphs are unweighted.

## Proof

**Exact enumeration.** There are \(24\) singleton sets, \(276\) two-sets and \(2024\) triples; the empty set cannot start observation. `verify_direct.py` and `verify_bitsets.py` enumerate every set at these sizes by generating increasing lists of labels. From its closed neighborhood each set is evaluated by synchronous forcing, using the previous wave's observed set for all tests within a wave. This monotone iteration strictly increases until a fixed point, within at most 24 growth rounds. There are no successes of size one or two and precisely \(576\) at size three. The wave distribution is \(\{2:144,3:272,4:160\}\).

**Exchange graphs.** For each pair of distinct minimum triples the programs admit a jump precisely when the two triples have two labels in common, and a slide precisely when the two remaining labels also form an edge of \(M\). Equivalently one can generate destinations by replacing each chosen label in turn and testing whether the resulting triple is in the optimum set. This yields 6,184 jump edges and 1,328 slide edges. Slide degree multiplicities are \(\{4:320,5:176,6:64,7:16\}\).

**Exact metrics.** Breadth-first exploration from each of the 576 seeds in each exchange graph reaches all 576 vertices; layers compute minimum numbers of exchanges because the graphs are unweighted. A second computation propagates whole frontiers as integer masks. The distance counts over all \(165{,}600\) unordered distinct pairs are:

| Distance | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jump | 6,184 | 44,944 | 109,672 | 4,800 | 0 | 0 | 0 | 0 | 0 |
| Slide | 1,328 | 4,048 | 10,816 | 24,744 | 42,752 | 48,752 | 27,624 | 5,400 | 136 |

All jump-source eccentricities are four; slide-source eccentricities are eight or nine, with multiplicities \(432\) and \(144\). Since every slide is a jump, the excess is nonnegative. The joint distance computation gives the exact excess table:

| Excess | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Pairs | 8,856 | 21,048 | 41,056 | 50,216 | 35,568 | 8,600 | 248 | 8 |

The eight extremal pairs all have distance pair \((d_J,d_T)=(1,8)\). In the stated LCF labelling they are:

```text
(0,4,18) <-> (0,14,18)
(0,6,10) <-> (0,6,20)
(1,15,21) <-> (11,15,21)
(2,6,12) <-> (6,12,16)
(3,7,21) <-> (3,17,21)
(3,9,13) <-> (3,9,23)
(5,9,15) <-> (9,15,19)
(8,12,18) <-> (12,18,22)
```

These have sixteen distinct endpoints. The computation is exhaustive over placements and pairs, without pruning or sampling.

## Verification
Run `python3 verify_direct.py` and `python3 verify_bitsets.py` in the original artifact directory using Python 3.10 or later and the standard library. They rebuild the same explicit graph, enumerate all subsets of the needed sizes, and obtain complete distances by respectively queue-based and bitset-layer exploration. The expected terminal markers are `VERIFY_DIRECT_OK` and `VERIFY_BITSETS_OK`. The calculation is specific to the labelled McGee graph; it gives neither an infinite-family theorem nor an electrical-grid deployment claim.

## Relationship to prior work
Bjorkman and coauthors study the general power-domination reconfiguration framework, including token addition/removal and token jumping. Those rules do not specify the McGee graph's optimum configurations, their slide-versus-jump distance distribution, or the eight exceptional exchanges. The LCF specification and the graph's uniqueness as a minimum-order cubic graph of girth seven are standard graph facts. Relocation problems for packings or other subsets of the same graph differ in the underlying feasible families.

## References
1. B. Bjorkman et al., *Power domination reconfiguration*, arXiv:2201.01798v1, https://arxiv.org/abs/2201.01798v1.
2. E. W. Weisstein, *McGee Graph*, MathWorld, https://mathworld.wolfram.com/McGeeGraph.html.
3. L. Kang and N. Wormald, *Minimum Power Dominating Sets of Random Cubic Graphs*, Journal of Graph Theory 85 (2017), 152–171, https://doi.org/10.1002/jgt.22053.
