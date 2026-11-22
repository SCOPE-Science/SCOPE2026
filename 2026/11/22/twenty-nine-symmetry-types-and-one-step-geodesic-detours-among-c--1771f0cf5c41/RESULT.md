# Twenty-nine symmetry types and one-step geodesic detours among Coxeter-graph metric bases

## Finding

Let \(G\) denote the 28-vertex Coxeter graph, and let \(\mathcal B\) be its family of minimum vertex-metric resolving sets (metric bases). The metric dimension \(\dim(G)=4\) was already known [1]. There are exactly \(7{,}728\) bases, in \(29\) orbits under the 336-element automorphism group: \(18\) orbits of size \(336\), \(9\) of size \(168\), and \(2\) of size \(84\).

Form \(\mathcal R\) with vertex set \(\mathcal B\), joining two different bases precisely when replacing one landmark by one new landmark turns one into the other. This exchange graph is connected, has \(155{,}904\) edges, radius \(4\), and diameter \(5\); it has \(1{,}680\) vertices of eccentricity \(4\) and \(6{,}048\) of eccentricity \(5\). Its degrees are not constant.

For every pair \(S,T\in\mathcal B\), their exact exchange distance satisfies

\[
 d_{\mathcal R}(S,T)\in\{4-|S\cap T|,\ 5-|S\cap T|\}.
\]

Of the \(29{,}857{,}128\) unordered pairs of distinct bases, precisely \(449{,}820\) need the additional move. The unordered-pair graph-distance distribution is \(155{,}904\), \(2{,}210{,}880\), \(11{,}718{,}084\), \(15{,}762{,}852\), and \(9{,}408\), at distances \(1,2,3,4,5\) respectively. The extra-move pairs occur at graph distances \(3,4,5\), with counts \(161{,}196\), \(279{,}216\), and \(9{,}408\), respectively. The family of metric bases is therefore **not** the family of bases of any rank-four matroid on the vertex set.

## Assumptions and scope

The graph is finite, simple, unweighted and undirected. A vertex set \(S\) *resolves* \(G\) when the vectors \((d_G(v,s))_{s\in S}\) are distinct for all \(v\in V(G)\), with any fixed ordering of \(S\). In the exchange graph, the landmark being removed and its replacement can be any distinct vertices; they need not be adjacent in the original graph. One exchange costs one step. The results concern precisely the 28-vertex Coxeter graph and its minimum four-landmark sets, not the 30-vertex Tutte–Coxeter graph.

One explicit graph construction used in the verification labels 21 vertices by triples \((j,r)\), where \(j\in\{1,2,3\}\) and \(r\in\mathbb Z/7\mathbb Z\), and introduces seven hubs \(h_r\). It joins \((j,r)\) to \((j,r+j)\) for every \(j,r\), and joins each \(h_r\) to the three \((j,r)\). All cycle indices are modulo \(7\); undirected edges are recorded once. A second construction takes the 28 three-subsets of \(\mathbb Z/7\mathbb Z\) that are not Fano lines \(\{r,r+1,r+3\}\), joining disjoint triples. The second program checks an explicit isomorphism between these two labeled constructions.

## Proof

The finite assertions below are exact exhaustive statements, with full standalone source code and reproducible enumerations rather than extrapolation from a sample.

**Minimum and completeness.** Construct the \(28\)-by-\(28\) shortest-path matrix by breadth-first search from each graph vertex. A subset \(S\) is resolving if and only if the 28 rows restricted to the columns \(S\) are distinct. The programs enumerate all \(\binom{28}{3}=3{,}276\) triples and establish that none resolves; monotonicity excludes smaller resolving sets. They enumerate all \(\binom{28}{4}=20{,}475\) four-subsets and find exactly \(7{,}728\) whose restricted distance rows are distinct. Thus these are *all* minimum bases and independently recover the known value \(\dim(G)=4\).

**Exchange graph.** The exact four-subset list is indexed by vertex-bit masks (first implementation) or sorted tuples (second implementation). For each basis, remove each of its four members in turn and insert each of the 24 other graph vertices; retain a neighbor if and only if its resulting four-subset occurs in the complete basis list. The resulting undirected graph has exactly \(155{,}904\) edges and the degree distribution shown below, which also proves it is nonregular.

| Exchange degree | Number of bases |
|---:|---:|
| 28 | 168 |
| 32 | 168 |
| 34 | 672 |
| 36 | 1,344 |
| 38 | 336 |
| 39 | 672 |
| 40 | 504 |
| 41 | 672 |
| 42 | 168 |
| 43 | 1,680 |
| 46 | 336 |
| 47 | 672 |
| 50 | 168 |
| 54 | 168 |

**Distances and completeness of the all-pairs test.** The C++17 verifier performs breadth-first search in the exact exchange graph from *every one* of the 7,728 bases; each search reaches all 7,728, proving connectivity. For all 29,857,128 unordered distinct pairs, it compares the BFS distance with the Johnson lower bound \(4-|S\cap T|\). Every difference is exactly 0 or 1. Directly aggregating all BFS runs gives the 449,820 detour pairs, radius 4, diameter 5, eccentricity counts and complete distance histogram stated above.

**Symmetry and an independent distance audit.** In the Fano nonline model, the 168 collineations of the seven-point Fano plane act on the graph. The independent Python program explicitly constructs them and 168 further distinct graph automorphisms using a displayed extra permutation; hence it verifies 336 graph automorphisms. The standard known automorphism-group order of the Coxeter graph is 336 [3], so these exhaust the group. Acting on the complete list of 7,728 metric bases yields exactly 29 orbits, with the sizes in the Finding. One exchange-graph BFS per orbit representative then independently checks the radius, diameter, eccentricity distribution, all-pairs upper bound and exact number of additional-move pairs (every pair is counted with its orbit multiplicity, dividing ordered off-diagonal pairs by two).

**The geodesic obstruction and non-matroid consequence.** In the lexicographically sorted Fano nonline triple labeling, the sets \(S=\{0,1,2,6\}\) and \(T=\{0,1,3,10\}\) are bases. They share two vertices, but each of the four candidates made by replacing one of \(\{2,6\}\) with one of \(\{3,10\}\) is *not* a basis, as a direct distance-signature check verifies. Therefore two exchanges cannot transform \(S\) into \(T\); the all-pairs certificate gives distance three, proving the sharp detour occurs. If these four-element bases formed a matroid's base family, the basis-exchange axiom would provide one of those forbidden substitutions (and repeated substitutions would always produce a Johnson-length path), a contradiction.

## Verification

The embedded file `cox_metric_a.cpp` is a standalone C++17 exhaustive verifier. From the directory containing the embedded files, run:

```sh
c++ -O3 -std=c++17 cox_metric_a.cpp -o metric_a
./metric_a
```

It checks the layered graph's size, degree and diameter; all resolving triples and quadruples; the full exchange graph; and breadth-first searches from every basis, with exact pair and degree histograms. Its expected terminal counts include `resolving_4sets=7728`, `exchange_edges=155904`, `ecc_hist=4:1680,5:6048`, and `Johnson_plus_one_pairs=449820`.

The independent stdlib file `cox_metric_b.py` runs via `python3 cox_metric_b.py`. It uses a Fano-plane nonline construction rather than the layered construction, checks an explicit label isomorphism, independently enumerates every metric basis and every exchange edge, constructs the verified automorphism action, and repeats distance and eccentricity checks with one representative per complete symmetry orbit. The expected terminal marker is `ALL_CHECKS_PASS`.

Both programs were executed successfully after compilation or interpretation. No randomized checks, heuristic cutoffs or externally assumed numerical data are needed for the enumerated graph and exchange assertions. The use of the classical full-automorphism order of 336 is explicitly cited for the word *full* in the orbit claim; the 336 permutations themselves and all their actions are checked directly.

## Relationship to prior work

Bailey [1] already calculated the Coxeter graph's metric dimension as four, including in Tables 2 and 3; neither the minimum nor its computational method is claimed as new. The inspected full paper reports metric-dimension values and how to test symmetry orbit representatives, not the complete 7,728-base count, 29 orbit sizes or one-landmark replacement geometry. Bailey and Cameron [2] address metric dimension and graph automorphism bases, especially general families. The established automorphism order 336 [3] and two constructions of the Coxeter graph are standard structural inputs. The mathematical refinement here is the precise structure and metric of the *space of all optimal resolving configurations*, not a new proof of the minimum dimension.

Searches also considered resolving-set enumeration, metric-base reconfiguration, minimum-base exchange graphs, and equivalent sensor/landmark terminology. No covering statement was identified in the accessible inspected sources. Absence of an indexed match is not a priority proof; see the limitations below.

## Limitations

This is a **finite, computer-exhaustive theorem for this specified graph**. It does not imply a Johnson-plus-one property for all distance-regular graphs, generalize automatically to other Coxeter-type graphs, or provide an all-order theorem. The all-pairs distances are certified by complete enumeration, not by a separate symbolic classification of shortest paths. An inaccessible or unindexed earlier census or a possibly relevant 2026 thesis on metric-base reconfiguration could contain overlapping information. Independent scholarly audit has not been performed.

## References

1. R. F. Bailey, *The metric dimension of small distance-regular and strongly regular graphs*, arXiv:1312.4973v1, first made public 17 December 2013. See Tables 2 and 3 and Section 3, https://arxiv.org/pdf/1312.4973 .
2. R. F. Bailey and P. J. Cameron, *Base size, metric dimension and other invariants of groups and graphs*, *Bulletin of the London Mathematical Society* 43 (2011), doi:10.1112/blms/bdq096, https://doi.org/10.1112/blms/bdq096 .
3. C. Godsil and G. Royle, *Algebraic Graph Theory*, Springer (2001), Section 4.6 (Coxeter graph constructions); for its standard 336-element automorphism group, see also https://mathworld.wolfram.com/CoxeterGraph.html .
