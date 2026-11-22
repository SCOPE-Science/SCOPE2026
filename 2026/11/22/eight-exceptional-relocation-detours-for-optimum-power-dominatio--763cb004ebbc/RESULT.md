# Eight exceptional relocation detours for optimum power domination of the McGee seven-cage

## Finding

Let \(M\) be the 24-vertex McGee graph, the unique cubic graph of girth seven. Its ordinary power-domination number is \(\gamma_P(M)=3\), and it has precisely \(576\) minimum power-dominating three-vertex sets. On these sets, let \(J\) allow an exchange of one selected vertex for any unselected vertex, and let \(T\) allow the same exchange only when the old and new vertices are adjacent in \(M\). Only minimum power-dominating sets are permitted as intermediate configurations.

Both reconfiguration graphs are connected. The jump graph has \(6{,}184\) edges, radius four and diameter four; the slide graph has \(1{,}328\) edges, radius eight and diameter nine. Every pair \(S,U\) of minimum configurations satisfies

\[
0\le d_T(S,U)-d_J(S,U)\le7.
\]

The upper bound is **sharp for exactly eight unordered pairs**, each of which has \(d_J(S,U)=1\) and \(d_T(S,U)=8\). These eight pairs are disjoint: they form a matching on sixteen configurations. Thus a relocation that appears to require a single unrestricted exchange can require eight optimum-preserving edge slides.

The slide eccentricity distribution is \(432\) configurations of eccentricity eight and \(144\) of eccentricity nine. Among the \(576\) optima, \(144\) complete observation after two synchronous forcing waves, \(272\) after three, and \(160\) after four, counting waves **after** the initial closed-neighborhood observation.

## Assumptions and scope

The labelled graph is defined without external data. Its vertices are \(\{0,\ldots,23\}\). Add each cycle edge from \(i\) to \(i+1\pmod{24}\), and one chord from \(i\) to \(i+c_i\pmod{24}\), where the period-three chord sequence is \((c_0,c_1,c_2)=(12,7,-7)\). This is the standard LCF representation of the McGee graph; each undirected edge is counted once. The graph has 24 vertices, 36 edges, degree three, girth seven, and diameter four.

For a selected set \(S\), put \(B_0=N_M[S]\). Given the observed set \(B_t\), obtain \(B_{t+1}\) by adding every unobserved vertex \(w\) for which some observed vertex \(v\) has \(N_M(v)\setminus B_t=\{w\}\). The set \(S\) power dominates when some \(B_t\) is all of \(V(M)\). A *minimum* set is of smallest possible cardinality, not merely inclusion-minimal.

An exchange between triples is legal in \(J\) precisely when the triples have intersection of cardinality two. It is legal in \(T\) precisely when, in addition, their two exchanged vertices are adjacent in \(M\). Distances and eccentricities are ordinary unweighted graph distances in these two finite graphs.

## Proof

**Finite exhaustive reduction and minimum.** There are \(24\) singleton sets, \(\binom{24}{2}=276\) two-sets, and \(\binom{24}{3}=2024\) three-sets. The procedures in `verify_direct.py` and `verify_bitsets.py` enumerate every one of these subsets, apply exactly the simultaneous neighborhood/forcing operator above until no further vertex can be observed, and compare the terminal observed set against all 24 vertices. Neither implementation finds a successful set of cardinality one or two; both find exactly \(576\) successful triples. Thus \(\gamma_P(M)=3\) and there are exactly \(576\) optima. Their successful forcing-wave counts are \(144,272,160\) at two, three and four waves respectively. The enumeration is exhaustive because combinations are generated with all entries strictly increasing from the full 24-vertex list; the forcing iteration is monotone and strictly grows on any nonterminal round, so it terminates in at most 24 rounds.

**Exact exchange graphs.** Both programs create an edge only when two of the \(576\) distinct valid triple masks differ in exactly one selected vertex. The slide program independently tests the underlying graph adjacency of the exchanged vertices. The undirected exchange counts are \(|E(J)|=6184\) and \(|E(T)|=1328\). The direct implementation checks edge symmetry explicitly. Its degree counts in \(T\) are \(320\) of degree four, \(176\) of degree five, \(64\) of degree six, and \(16\) of degree seven.

**All-pairs shortest distances.** In the first implementation, breadth-first search from every one of the \(576\) states uses the graph's complete, exact adjacency lists. The second implementation rebuilds the original graph and optimum configurations using integer bit masks, constructs the exchange graphs by comparing all \(\binom{576}{2}=165{,}600\) pairs, and computes each distance layer by expanding bitset frontiers. Every source reaches all \(576\) states. Thus both graphs are connected, not merely connected on a sample of configurations.

The direct certificate obtains these unordered-pair distance distributions:

| Distance | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Jump | 6,184 | 44,944 | 109,672 | 4,800 | 0 | 0 | 0 | 0 | 0 |
| Slide | 1,328 | 4,048 | 10,816 | 24,744 | 42,752 | 48,752 | 27,624 | 5,400 | 136 |

Both rows sum to \(165{,}600\). The jump radius and diameter are both four; slide eccentricities are eight (432 states) or nine (144 states), proving its radius eight and diameter nine.

Finally the exact histogram of \(d_T(S,U)-d_J(S,U)\), over unordered distinct optima, is:

| Excess | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Pairs | 8,856 | 21,048 | 41,056 | 50,216 | 35,568 | 8,600 | 248 | 8 |

Again the counts sum to \(165{,}600\). The eight maximal pairs all have jump distance one and slide distance eight. Their two endpoint triples are pairwise distinct. In the stated LCF labelling, the eight unordered pairs are

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

These computations are proofs of **finite exact statements**: the graph and all candidate objects are enumerated without pruning or random sampling, and every nontrivial graph-distance claim is computed by complete shortest-path exploration. The two supplied implementations use different state representations and shortest-path routines.

## Verification

Run in the directory containing the two self-contained Python 3 standard-library programs:

```sh
python verify_direct.py
python verify_bitsets.py
```

The first prints `VERIFY_DIRECT_OK` and the second `VERIFY_BITSETS_OK` after passing their assertions. Both reconstruct the graph without external data. The direct implementation additionally checks the entire jump and slide pair-distance histograms and all eight maximal-penalty pairs; the bitset implementation independently checks the full excess histogram and eccentricities. No cached result, generated external file, or specialized solver is needed. The displayed figures were reproduced from the embedded scripts.

## Relationship to prior work

Bjorkman and coauthors introduced the graph-theoretic power-domination reconfiguration framework, including general token addition/removal and unrestricted token jumping. Their first-public version of January 5, 2022 does not give an exact McGee-graph optimum classification or its pairwise token-slide metric. The McGee graph's 24-vertex LCF specification and uniqueness as the cubic seven-cage are standard graph facts. Published work on maximum independent-set reconfiguration, identifying codes and perfect matchings of this same cage concerns other optimization conditions; none of the inspected available claims entails the power-domination census and the eight exceptional relocation detours. The general classification of reconfiguration problems does not supply these finite numerical invariants without an additional calculation.

## Limitations

The result is specific to the ordinary labelled 24-vertex McGee graph and its optimum three-sensor configurations. It does not assert an infinite-family theorem, stability under graph perturbations, or an operational electrical-grid deployment result. The finite checks are exhaustive, not a formal verification in a proof assistant. External independent mathematical audit remains unperformed. Despite the targeted literature and indexed-record comparisons, coverage by an unindexed source cannot be excluded absolutely.

## References

1. B. Bjorkman, C. Bozeman, D. Ferrero, M. Flagg, C. Grood, L. Hogben, B. Jacob, and C. Reinhart, *Power domination reconfiguration*, arXiv:2201.01798v1 (January 5, 2022). https://arxiv.org/html/2201.01798v1
2. E. W. Weisstein, *McGee Graph*, MathWorld, Wolfram Research. https://mathworld.wolfram.com/McGeeGraph.html
3. *The maximum-packing reconfiguration transition in the McGee graph*, mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-maximum-packing-reconfiguration-transition-in-the-mcgee-grap--3e5911c9aaad
4. L. Kang and N. Wormald, *Minimum Power Dominating Sets of Random Cubic Graphs*, Journal of Graph Theory 85 (2017), 152–171; first published online June 16, 2016. https://doi.org/10.1002/jgt.22053
