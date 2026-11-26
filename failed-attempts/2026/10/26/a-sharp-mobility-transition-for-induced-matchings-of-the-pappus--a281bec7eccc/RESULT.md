# A sharp mobility transition for induced matchings of the Pappus graph

## Finding

Let \(P\) be the Pappus graph and \(\mathcal J_k(P)\) the graph whose vertices are all size-\(k\) induced edge matchings in \(P\), with two vertices adjacent when their edge sets differ by exactly one edge. Then the maximum induced matching cardinality is \(5\), with exactly \(27\) maximizers. Their exchange graph is \(27K_1\), so all optima are frozen.

At deficiency one, all \(135\) induced matchings of size \(4\) are mobile: \(\mathcal J_4(P)\) is connected with \(486\) edges, radius \(8\), diameter \(9\), and degree distribution consisting of \(27\) vertices of degree \(4\) and \(108\) of degree \(8\). Every size-four matching extends to exactly one maximum matching. Its extension partitions \(\mathcal J_4(P)\) into \(27\) disjoint induced copies of \(K_5\). Contracting these blocks and ignoring multiplicity produces the line graph \(L(P)\); exactly four exchange edges run between each adjacent pair of blocks and none between nonadjacent blocks. Thus deleting just one edge from an optimum exactly removes the connectivity obstruction.

## Assumptions and scope

All graphs are simple, finite, undirected, with labeled vertices. For a set \(M\) of edges of \(P\), 'induced matching' means the endpoints of distinct edges of \(M\) are disjoint and mutually nonadjacent. An exchange replaces one edge by an arbitrary new edge, keeping the same cardinality and the induced-matching condition; the replacement edges need not meet. The graph \(P\) has vertices indexed \(0,\ldots,17\), cyclic edges \(\{i,i+1\}\) modulo \(18\), and LCF chords \(\{i,i+s_{i\bmod6}\}\) with signed shifts \(s=(5,7,-7,7,-7,-5)\), all indices modulo \(18\). Duplicate undirected edges are counted once. This is the standard Pappus graph, with \(18\) vertices and \(27\) edges. All counts refer to distinct labeled edge subsets, with no quotient by graph symmetry.

## Proof

Write the \(27\) graph edges in lexicographic order as \(e_0,\ldots,e_{26}\). Declare distinct edge indices compatible when their four endpoints are distinct and no edge of \(P\) joins an endpoint of one to an endpoint of the other. A subset of edge indices is an induced matching **if and only if** all its pairs are compatible. Hence exact examination of the \(\binom{27}{4}\), \(\binom{27}{5}\), and \(\binom{27}{6}\) subsets tests the entire relevant finite search space. The exhaustive procedure `check_lcf.py` obtains respectively \(135\), \(27\), and \(0\) valid subsets. Since any matching larger than \(6\) contains a six-element submatching, this proves the maximum is \(5\) and proves both counts. The independent recursive compatibility search `check_incidence.py` reconstructs the same objects from the nine point-line triples of the Pappus configuration; its compatible-edge extension visits every induced matching in increasing index order and arrives at exactly the same counts.

Every valid four-set has exactly one valid five-set extension (checked for all \(135\) four-sets by both programs). Consequently, the \(5\) four-subsets of each five-set form a complete graph \(K_5\) and no two five-sets share a four-subset. Thus \(\mathcal J_5(P)\) has no edges. The pairwise intersections of its \(27\) five-sets have sizes \(0,1,3\) with multiplicities \(189,108,54\). Inter-block exchanges occur precisely when the parent five-sets share three edges: for a common triple, exchanging either of the two remaining edges in the first parent for either remaining edge in the second yields exactly four exchanges. Therefore the block quotient has \(27\) vertices and \(54\) edges, each with cross-block multiplicity \(4\).

For a fully checkable identification of the quotient, number maximum matchings lexicographically by their five edge indices and define the permutation

```
(0,1,2,3,4,21,22,20,23,6,13,14,12,15,11,18,26,25,16,17,9,5,8,7,10,19,24)
```

from their indices to the lexicographically numbered original graph edges. For **every** pair of distinct maximum-match indices, the corresponding quotient vertices are adjacent exactly when the two original edges selected by this permutation share an endpoint. These \(351\) equivalences are directly checked by `check_lcf.py`. This proves the quotient is \(L(P)\). Since \(P\) is connected, the quotient is connected; every block is \(K_5\), so \(\mathcal J_4(P)\) is connected as well. Counting its internal and external edges gives \(27\binom{5}{2}+4(54)=486\).

To determine the metric exactly, construct all exchange neighbors by one-edge replacement and run breadth-first search from **each of the 135 states**. The resulting unordered-pair distance histogram for distances \(1\) through \(9\) is

```
(486,648,918,1296,1836,2160,1242,432,27)
```

which totals \(\binom{135}{2}=9045\), proving diameter \(9\) and connectedness directly as well. The eccentricity distribution is \(108\) states with eccentricity \(8\) and \(27\) with eccentricity \(9\), proving radius \(8\). Direct neighbor enumeration gives degrees \(4\) for \(27\) states and \(8\) for \(108\), and sums to twice the previously calculated edge count. This finite exhaustive argument makes no assertion about arbitrary graph sizes.

## Verification

Both standalone programs use only Python's standard library and run without input files. Invoke `python3 check_lcf.py` or `python3 check_incidence.py`. Their captured outputs are `lcf_results.json` and `incidence_results.json`. The first program constructs \(P\) from LCF notation and enumerates all relevant fixed-cardinality edge subsets. The second constructs the Pappus configuration as a nine-line incidence graph, enumerates compatible edge sets recursively using bit masks, and tests exchange neighbors by edge replacement. The second independently recovers \(18\) triangles in the quotient and checks a separate explicit isomorphism from their line-graph root to the Pappus incidence graph. Every claimed count, degree, metric, and quotient statement is checked by executable assertions; the recorded outputs are reproducibility aids, not substitutes for executed checks.

## Relationship to prior work

Kamiński, Medvedev, and Milanič introduce token-jumping reconfiguration of independent sets and study its general complexity. Because an induced matching of \(P\) corresponds to an independent set in the square of its line graph, their framework motivates the exchange rule, but their general results do not determine these Pappus-specific exchange graphs. Dabrowski, Demange, and Lozin study the maximum induced matching problem in bipartite and regular graphs, but their examined primary text gives complexity results and a hypercube classification, rather than this Pappus configuration-space theorem. The classical Pappus-graph entry supplies the LCF graph and its identification with the Pappus configuration, not the matching exchanges. Distinct previous investigations of the *ordinary* matching complex of the Pappus graph count all matchings, not necessarily induced matchings, and do not imply the present theorem without new calculation. Targeted literature and mathematical-record searches have not produced an implication covering the quotient or distance classification.

## Limitations

This is an exact finite theorem for the 18-vertex Pappus graph only; it does not classify other cubic symmetric graphs or promise a polynomial-time formula for arbitrary input graphs. The result does not assert that the exchange graph is itself a line graph: only the quotient by the 27 parent blocks is identified with \(L(P)\). The numerical exhaustive proof is contingent on correct complete code execution and graph normalization; the standalone second construction mitigates but cannot eliminate implementation risk. Relevant unindexed published classifications or computational tables may exist. Priority has not been independently established, and independent external scientific validation has not been performed.

## References

1. M. Kamiński, P. Medvedev and M. Milanič, *Shortest paths between shortest paths and independent sets*, arXiv:1008.4563 (first posted 2010-08-26), https://arxiv.org/abs/1008.4563 .
2. K. K. Dabrowski, M. Demange and V. V. Lozin, *New results on maximum induced matchings in bipartite graphs and beyond*, Theoretical Computer Science 478 (2013), 33–40, https://doi.org/10.1016/j.tcs.2013.01.027 ; author manuscript https://www.konraddabrowski.co.uk/nrim-v7.pdf .
3. E. W. Weisstein, *Pappus Graph*, MathWorld, https://mathworld.wolfram.com/PappusGraph.html .
