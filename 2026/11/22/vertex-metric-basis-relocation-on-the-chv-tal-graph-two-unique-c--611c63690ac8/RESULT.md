# Vertex-metric-basis relocation on the Chvátal graph: two unique centers and sharp four-move detours

## Finding

Let \(H\) be the labelled Chvátal graph defined by the edge list in the included verification programs. A *metric basis* is a smallest vertex set whose vectors of graph distances distinguish all vertices. Consider two relocation rules on the metric bases: **jump** replaces one landmark with any other vertex, while **slide** replaces it only with an adjacent vertex of \(H\); the destination must again be a metric basis.

The vertex metric dimension of \(H\) is \(4\), with exactly \(146\) metric bases. The jump graph has \(928\) edges and is connected, with radius and diameter both \(4\). The slide graph has \(452\) edges and is connected, with radius \(4\) and diameter \(6\). Its eccentricity counts are \(2\) at eccentricity \(4\), \(104\) at eccentricity \(5\), and \(40\) at eccentricity \(6\). The only two slide centers, for the stated vertex labels, are \(\{2,8,9,11\}\) and \(\{3,6,7,10\}\).

For either relocation graph, let \(\delta(S,T)=4-|S\cap T|\) be the unavoidable number of landmark replacements. Among all \(\binom{146}{2}=10585\) unordered distinct basis pairs, the number of pairs with *jump distance* exceeding \(\delta\) by \(0\) or \(1\) is respectively \(10367\) or \(218\); no larger excess occurs. For *slide distance*, the excess values \(0,1,2,3,4\) have exact multiplicities \(4463,4944,1070,92,16\), respectively. Thus the maximum additional cost imposed by local adjacency is four steps over the elementary exchange lower bound.

## Assumptions and scope

The graph has vertex set \(\{0,1,\ldots,11\}\) and exactly the following undirected edges:

```text
(0,1) (0,4) (0,6) (0,9) (1,2) (1,5) (1,7) (2,3)
(2,6) (2,8) (3,4) (3,7) (3,9) (4,5) (4,8) (5,10)
(5,11) (6,10) (6,11) (7,8) (7,11) (8,10) (9,10) (9,11)
```

This is a finite result for this **vertex** distance-resolving problem; it does not concern resolving *edges* or arbitrary twelve-vertex graphs. All vertex labels are essential only for the explicit identity of the two central sets; unlabeled numerical metrics are graph invariants. All results use a **single simultaneous replacement** and maintain minimum basis size \(4\) at every intermediate step. There is no implication about larger sets, simultaneous exchanges, or other resolving variants.

## Proof

**Finite exhaustive proof with complete reproducible decision procedures.** The graph adjacency list has \(12\) rows of degree \(4\) and \(24\) undirected edges. For each pair of graph vertices \(u,v\), a breadth-first search in the original graph computes the exact shortest graph distance \(d_H(u,v)\). A vertex set \(S\) resolves precisely when the \(12\) vectors \((d_H(v,s):s\in S)\), indexed by \(v\), are pairwise distinct. Complete enumeration of all sets with sizes \(0,1,2,3\) yields no resolving set; enumeration of the \(\binom{12}{4}=495\) four-sets yields exactly \(146\) resolving sets. Therefore \(4\) is the true minimum, and the candidate list of all metric bases is complete.

For distinct bases \(S,T\), a single jump is legal if and only if \(|S\triangle T|=2\), where \(\triangle\) denotes symmetric difference. It is a legal slide precisely when, additionally, the removed and inserted vertices form an edge of \(H\). These equivalences are exact: there are no undiscovered legal transitions. Applying them to every unordered pair of the complete 146-state list yields respectively \(928\) and \(452\) edges.

From each basis, breadth-first search in each finite reconfiguration graph explores all reachable bases and assigns their minimal move distances (every edge has unit weight). All \(146\) bases are reached from every start in each graph. The maximum row entries determine the stated eccentricity distributions and the two centers. All \(10585\) unordered distance entries are then compared with \(\delta(S,T)\) to produce the exact detour spectra. The lower bound \(\delta\) holds because one replacement removes at most one element of \(S\setminus T\). Exhaustive reachability and breadth-first minimality provide both existence and optimality for every recorded distance; no unexamined state remains.

A second implementation independently expresses vertex-resolution as intersection with all \(66\) pair-separator masks, constructs transitions by bitwise symmetric differences, and computes graph shortest paths with Floyd–Warshall instead of breadth-first search. Its full all-pairs output agrees. Together the two complete implementations certify the finite conclusion without extrapolating from a partial sample.

## Verification

Run with a Python 3 interpreter using only the standard library:

```text
python3 src/verify_bfs.py
python3 src/verify_floyd.py
```

Both scripts contain the exact same public input graph's edge list, independently generate all eligible bases, assert the fixed numerical claims, and print their own summaries. The first method checks all distances with repeated breadth-first search and tuple-valued distance profiles. The second uses landmark-separator bitmasks and Floyd–Warshall. They agree on \(146\) states, \(928\) versus \(452\) edges, all eccentricity counts, the two centers and every excess-distance multiplicity. The complete slide distance histogram for unordered pairs at lengths \(1,2,3,4,5,6\) is \((452,1700,3444,3577,1344,68)\). The complete jump histogram at lengths \(1,2,3,4\) is \((928,3328,4486,1843)\).

## Relationship to prior work

Metric bases are the minimum resolving-landmark sets studied by Hakanen, Junnila, Laihonen and González Yero (2021 online), while the token-jump and token-slide rules follow the standard reconfiguration framework described by Nishimura (2018). The Chvátal graph is a classical twelve-vertex, four-regular, triangle-free, four-chromatic graph, not a newly constructed graph. These definitions, the original graph and generic reconfiguration concepts are not claimed as new.

An indexed related calculation titled *Complete edge-metric basis mobility of the Chvátal graph* concerns edge-distance resolution by five landmarks, with 192 edge-metric bases. This is a different feasibility predicate from the present vertex-distance resolving problem, which has four landmarks and 146 bases. No inference of the vertex-metric reconfiguration census follows solely from the quoted edge-metric numbers. The full text of that related calculation was not accessible in this examination, so undocumented coverage is a residual risk.

## Limitations

This is a complete finite census, not an infinite-family theorem or a new polynomial-time algorithm. Numerical claims are conditional on the explicitly displayed standard Chvátal graph edge list and one-landmark relocation rules. The proof relies on independently reproducible finite enumeration rather than a compact closed-form structural classification. An independently conducted mathematical audit has not been performed. Older or unindexed equivalent exact computations, or an uninspected appendix of a closely related paper, might have priority.

## References

1. A. Hakanen, V. Junnila, T. Laihonen, and I. G. Yero, *On vertices contained in all or in no metric basis*, Discrete Applied Mathematics **319** (2022), 407–423. First available online 2021-12-21. https://doi.org/10.1016/j.dam.2021.12.004 . Open full text: https://rodin.uca.es/handle/10498/29356 .
2. N. Nishimura, *Introduction to Reconfiguration*, Algorithms **11** (2018), 52. https://doi.org/10.3390/a11040052 .
3. V. Chvátal, *The smallest triangle-free 4-chromatic 4-regular graph*, Journal of Combinatorial Theory **9** (1970), 93–94. https://doi.org/10.1016/S0021-9800(70)80057-6 .
