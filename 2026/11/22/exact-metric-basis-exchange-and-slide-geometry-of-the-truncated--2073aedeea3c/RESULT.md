# Exact metric-basis exchange and slide geometry of the truncated tetrahedral graph

## Finding

Let \(T\) be the twelve-vertex truncated tetrahedral graph, whose vertices are the ordered pairs \((a,b)\) of distinct members of \(\{0,1,2,3\}\). Vertices \((a,b)\) and \((c,d)\) are adjacent exactly when \(a=c\) and \(b\ne d\), or when \((c,d)=(b,a)\). Thus \(T\) is the cubic skeleton of the truncated tetrahedron and has 18 edges. A *metric basis* is a smallest vertex subset \(B\) for which all twelve graph vertices have distinct vectors of distances to members of \(B\).

The metric dimension of \(T\) is \(3\). It has exactly \(156\) metric bases, comprising nine orbits under the natural \(S_4\)-action permuting the original tetrahedron corners. There are two reconfiguration rules on metric bases: a *jump* replaces one selected vertex by any unselected vertex, and a *slide* does so only along an edge of \(T\). Every intermediate triple must remain a metric basis.

**Exact metric theorem.** The jump graph \(J\) is connected with \(156\) vertices, \(1446\) edges, and, for every two bases \(A,B\),
\[
 d_J(A,B)=3-|A\cap B|.
\]
In particular, \(J\) is an isometric induced subgraph of the Johnson graph \(J(12,3)\), despite the fact that its vertex family does **not** satisfy the matroid basis-exchange axiom.

The slide graph \(L\) is also connected, has \(450\) edges, and has **radius \(6\), diameter \(7\)**. Exactly \(108\) bases have slide eccentricity \(6\), while the remaining \(48\) have eccentricity \(7\). Exactly \(36\) unordered base pairs are at slide distance \(7\), in two \(S_4\)-orbits of sizes \(24\) and \(12\). For any bases \(A,B\), the extra moves beyond the unrestricted jump lower bound satisfy
\[
 0\le d_L(A,B)-(3-|A\cap B|)\le 4,
\]
and the upper bound is attained by **exactly \(204\)** unordered pairs.

The complete unordered-pair distance and penalty distributions are:

| Slide distance | Pair count | Extra slides beyond \(3-|A\cap B|\) | Pair count |
|---:|---:|---:|---:|
| 1 | 450 | 0 | 2050 |
| 2 | 1356 | 1 | 3708 |
| 3 | 2812 | 2 | 4104 |
| 4 | 3660 | 3 | 2024 |
| 5 | 2964 | 4 | 204 |
| 6 | 812 | | |
| 7 | 36 | | |

Each distribution totals \(\binom{156}{2}=12090\) unordered distinct pairs.

## Assumptions and scope

All statements concern this **single fixed**, undirected simple graph \(T\) with its twelve labelled ordered-pair vertices; there is no variable graph size. Graph distance is ordinary unweighted shortest-path distance. An unordered three-element landmark set resolves if the twelve distance vectors, with a fixed but arbitrary order on its landmarks, are all distinct. Reconfiguration moves preserve the set size and resolving property; tokens/landmarks are indistinguishable. For radius and diameter the distances are taken in the respective reconfiguration graph, not in \(T\). Pairs in the distance distributions are unordered and distinct.

For reproducibility, the indices \(0,1,\ldots,11\) mean the lexicographically sorted ordered pairs:

| Index | Vertex | Index | Vertex | Index | Vertex |
|---:|---|---:|---|---:|---|
| 0 | \((0,1)\) | 4 | \((1,2)\) | 8 | \((2,3)\) |
| 1 | \((0,2)\) | 5 | \((1,3)\) | 9 | \((3,0)\) |
| 2 | \((0,3)\) | 6 | \((2,0)\) | 10 | \((3,1)\) |
| 3 | \((1,0)\) | 7 | \((2,1)\) | 11 | \((3,2)\) |

## Proof

**1. A bounded, symmetry-reduced resolving-set certificate.** The graph description supplies all 18 edges without a hidden input. Let \(D(i,j)\) be its ordinary shortest-path distance. For each candidate landmark set \(C\), define
\[
 q(C)=\left|\left\{(D(v,c))_{c\in C}:v\in V(T)\right\}\right|.
\]
Then \(C\) resolves if and only if \(q(C)=12\). The full \(S_4\)-action on ordered pairs preserves graph distances, so a candidate's \(q(C)\) is constant along its orbit. There are only five orbits of unordered vertex pairs; their representative index pairs and signature counts \(q\) are respectively \((0,1):9\), \((0,3):7\), \((0,4):10\), \((0,7):10\), and \((0,8):9\). Hence no two-vertex set resolves. No one-vertex set resolves either.

Exactly thirteen \(S_4\)-orbits partition the \(\binom{12}{3}=220\) triples. The following table lists every orbit representative, orbit size, and number of distinct distance signatures. In the last two columns, entries for resolving representatives are their token-slide degree and eccentricity.

| Triple index representative | Orbit size | \(q\) | Slide degree | Slide eccentricity |
|---|---:|---:|---:|---:|
| \((0,1,2)\) | 4 | 9 | — | — |
| \((0,1,3)\) | 24 | 11 | — | — |
| \((0,1,4)\) | 24 | 12 | 6 | 7 |
| \((0,1,5)\) | 24 | 12 | 6 | 6 |
| \((0,1,9)\) | 12 | 11 | — | — |
| \((0,1,10)\) | 24 | 12 | 5 | 6 |
| \((0,3,6)\) | 24 | 12 | 6 | 7 |
| \((0,3,8)\) | 12 | 12 | 5 | 6 |
| \((0,4,6)\) | 8 | 12 | 9 | 6 |
| \((0,4,8)\) | 24 | 12 | 6 | 6 |
| \((0,4,10)\) | 12 | 12 | 5 | 6 |
| \((0,4,11)\) | 24 | 11 | — | — |
| \((0,7,10)\) | 4 | 12 | 3 | 6 |

For each row, apply all 24 corner permutations to the representative and count distinct images; direct distance-vector comparison supplies \(q\). This is an exhaustive finite proof of the list, not a sampling argument: orbit images are disjoint and their sizes total 220. The nine qualifying rows sum to \(156\), proving both the minimum size and the complete classification of bases.

**2. Reconfiguration and shortest paths.** For two classified bases, a jump edge is present precisely when their intersection has size two. Such an edge is a slide edge precisely when the removed and added vertices are adjacent in \(T\). Thus both reconfiguration graphs are completely and uniquely defined from the 156 certified triples. The attached `verify_ordered_pairs.py` enumerates this set, constructs the two adjacency lists and performs breadth-first searches from **each** base, recording all 12,090 distances. It checks graph connectivity by confirming reachability of all 156 bases from each source and proves the stated edge counts, eccentricities, and distance/penalty histograms using exhaustive integer assertions. The independent `verify_lcf.py` constructs the same graph using its Hamiltonian-cycle LCF presentation \([2,6,-2]^4\), uses bitmasks to classify bases, and computes base and reconfiguration distances with Floyd–Warshall rather than breadth-first search. It includes an explicit 12-label graph isomorphism and independently asserts the same integers. Both are standalone standard-library Python files. The complete search is finite and exhaustive, so the upper bounds are proved by explicit routes and the lower bounds by the verified absence of shorter routes.

Any jump changes at most one vertex of a basis, so \(3-|A\cap B|\) is always a distance lower bound. The exhaustive jump-distance histogram agrees with this bound on **every** pair, yielding the claimed isometric embedding. The slide eccentricity table, confirmed by the complete all-pairs search, gives radius \(6\), diameter \(7\), and the 108/48 partition. The slide-distance histogram has 36 pairs at distance seven. The 24 corner permutations partition these 36 pairs into two orbits, represented by \(\{0,1,4\},\{5,8,11\}\) and \(\{0,1,4\},\{7,10,11\}\), of sizes 24 and 12. Computing and tabulating \(d_L-(3-|A\cap B|)\) across all pairs proves the sharp extra-cost statement and 204 count.

For example, one seven-slide geodesic (triples of indices) is
\[
\begin{aligned}
\{0,1,4\}&\to\{0,1,5\}\to\{0,1,10\}\to\{0,1,11\}\\
&\to\{0,6,11\}\to\{0,8,11\}\to\{3,8,11\}\to\{5,8,11\}.
\end{aligned}
\]
Each step changes one landmark along a specified graph edge and preserves the table's resolving criterion. The all-pairs distance computation shows that no shorter slide route connects its endpoints.

**3. Isometric jump geometry without a matroid.** The qualifying triples \(A=\{0,1,4\}\) and \(B=\{0,3,6\}\) fail basis exchange for the element \(4\in A\setminus B\). Neither replacement \(\{0,1,3\}\) nor \(\{0,1,6\}\) resolves, since each yields only eleven distinct vertex signatures. Therefore the family is not the bases of a matroid. The isometric jump metric just established is nevertheless valid for every pair. This distinguishes the result from an inference based on matroid basis exchange.

## Verification

Run with Python 3 from the directory containing the standalone files:

```bash
python3 verify_ordered_pairs.py
python3 verify_lcf.py
```

Each program terminates with JSON and uses assertions for the complete census, pairwise distances, extremal counts and—where appropriate—symmetry orbit classification or the LCF isomorphism. The files `check_ordered_pairs.json` and `check_lcf.json` record the actual outputs of these commands. The two programs use different constructions, data representations, and shortest-path algorithms. No proprietary packages, external datasets or network access are needed. One executable does not read the other's output.

## Relationship to prior work

Hakanen, Junnila, Laihonen and González Yero (arXiv:2103.08911, first public March 16, 2021) study vertices occurring in every or no metric basis and related structural/complexity bounds. Their accessible full text does not analyze reconfiguration distances for the truncated tetrahedral graph. Sardar and coauthors (2024) determine metric dimensions of two other claw-free cubic families, strings and rings of diamonds; these families do not include the truncated tetrahedral graph, and their published discussion does not cover the present two move graphs. Standard graph descriptions identify the truncated tetrahedral graph with LCF notation \([2,6,-2]^4\), but do not give the optimal-landmark mobility metrics. Related exact basis-reconfiguration classifications on other named graphs do not imply these counts: the base graphs and feasible triples differ. The potentially surprising contrast here is a nonmatroid family with Johnson-isometric jump distances but local-slide diameter seven and an exact four-move maximum penalty.

## Limitations

This is a finite, explicitly certified theorem for one graph, not a theorem for all truncated polyhedra or all cubic graphs. Its two checkers are mathematically inspectable finite enumerations, not external or independent expert certification. Historical priority cannot be established from negative literature searches: unpublished thesis or project material on metric-basis reconfiguration could contain an equivalent example; available project descriptions do not resolve that risk. The stated counts refer to the ordinary **vertex**-metric dimension, not edge-metric, strong-metric or fault-tolerant landmark sets. No performance guarantee is claimed for larger graphs.

## References

1. A. Hakanen, V. Junnila, T. Laihonen and I. G. Yero, *On Vertices Contained in All or in No Metric Basis*, arXiv:2103.08911v1 (2021-03-16), https://arxiv.org/abs/2103.08911.
2. M. S. Sardar, S.-J. Xu, M. Cancan, M. R. Farahani, M. Alaeiyan and S. V. Patil, *Computing Metric Dimension of Two Types of Claw-free Cubic Graphs with Applications*, *J. Combin. Math. Combin. Comput.* 119 (2024), 163–174, https://doi.org/10.61091/jcmcc119-17.
3. E. W. Weisstein, *Truncated Tetrahedral Graph*, MathWorld, https://mathworld.wolfram.com/TruncatedTetrahedralGraph.html.
4. B. Foster-Greenwood, *Student Research* (metric-basis reconfiguration topic), https://www.cpp.edu/faculty/brianaf/student-research.shtml.
