# Exact mutual-visibility and maximal-set census of the triangular eight-torus

## Finding

**Theorem.** Let \(G=C_3\square C_8\) be the Cartesian product of a triangle and the eight-cycle. For every subset \(S\subseteq V(G)\), call \(S\) *mutually visible* when every two vertices in \(S\) can be joined by at least one shortest path with no other member of \(S\) in its interior. Count subsets on the fixed labeled vertex set of \(G\), not up to automorphisms. The complete mutual-visibility polynomial is

\[
\begin{aligned}
P_G(z)={}&1+24z+276z^2+1952z^3+8808z^4\\
&+24720z^5+40256z^6+33000z^7\\
&+9960z^8+928z^9.
\end{aligned}
\]

The polynomial counting **inclusion-maximal** mutually visible subsets is exactly

\[
\boxed{F_G(z)=4608z^7+4656z^8+928z^9.}
\]

Consequently, the lower ordinary mutual-visibility number is \(\mu^-(G)=7\), and there are exactly \(4608\) sets attaining this smallest inclusion-maximal size. The only sizes of inclusion-maximal sets are \(7,8,9\); there are \(10192\) such sets altogether. There are \(119925\) mutually visible subsets of all sizes, including the empty set. The maximum ordinary mutual-visibility number \(\mu(G)=9\) was known from earlier results on Cartesian products of cycles; its exact multiplicity \(928\) here is part of the census.

## Assumptions and scope

Take vertices \((j,r)\), with \(j\in\mathbb Z/8\mathbb Z\) and \(r\in\mathbb Z/3\mathbb Z\), and give each vertex integer index \(3j+r\). Vertices are adjacent when they are in the same column with distinct rows (the triangle factor), or when they occupy adjacent cyclic columns and the same row (the eight-cycle factor). There are \(24\) vertices. All paths and distances are in this finite simple undirected graph; the definition is *ordinary*, not total, dual, outer, or fault-tolerant, mutual visibility. Maximal means maximal by inclusion, not maximum cardinality.

## Proof

**Geodesic classification.** The Cartesian product distance between \((j,r)\) and \((k,s)\) is the shorter cyclic distance from \(j\) to \(k\), plus \(0\) when \(r=s\) and \(1\) otherwise. Every shortest path follows a shortest cyclic arc, and changes row exactly once if its endpoint rows differ; otherwise it stays in one row. For antipodal columns \(j\) and \(j+4\), there are two shortest cyclic arcs; otherwise the shortest arc is unique. When the rows differ, the single vertical change may take place at any vertex of the chosen arc, in order, and every such interleaving is a shortest path. These statements follow directly by counting horizontal and vertical steps; an unnecessary step or a second vertical change would make the path longer. Hence this list is exhaustive.

For vertices \(a<b\), let \(\mathcal I_{ab}\) consist of the sets of internal vertices of all the classified shortest \(a,b\)-paths. By definition, \(S\) is mutually visible if and only if for each \(a,b\in S\) with \(a<b\) there exists \(I\in\mathcal I_{ab}\) with \(I\cap S=\varnothing\). These finitely many sets can be represented by \(24\)-bit masks, so each test is exact integer arithmetic without tolerances. This predicate is hereditary under taking subsets.

**Complete finite enumeration.** Order vertices as integers \(0,\ldots,23\). Traverse all mutually visible sets recursively: starting at the empty set, append an integer vertex \(v\) greater than the last appended integer only when the enlarged set satisfies the above pair test. Every mutually visible subset appears exactly once, since its elements have a unique increasing order and all its prefixes are mutually visible. No nonvisible subset needs exploration, by heredity. For each visited \(S\), test all vertices \(v\notin S\). Again by heredity, \(S\) is inclusion-maximal if and only if **none** of the single-vertex extensions \(S\cup\{v\}\) is mutually visible. Thus, counters incremented by \(|S|\), and a second family of counters incremented only on this maximality test, compute exactly the coefficients of \(P_G\) and \(F_G\).

The resulting exhaustive integer counts by size are:

| Size | All mutually visible sets | Inclusion-maximal sets |
|---:|---:|---:|
| 0 | 1 | 0 |
| 1 | 24 | 0 |
| 2 | 276 | 0 |
| 3 | 1952 | 0 |
| 4 | 8808 | 0 |
| 5 | 24720 | 0 |
| 6 | 40256 | 0 |
| 7 | 33000 | 4608 |
| 8 | 9960 | 4656 |
| 9 | 928 | 928 |

Their sums are \(119925\) and \(10192\), respectively. No larger mutually visible set occurs in the exhaustive traversal, and no smaller inclusion-maximal set occurs; this proves both polynomial identities and all stated consequences.

A concrete seven-vertex inclusion-maximal set, independently checked by the included programs, is

\[
S_0=\{(0,0),(0,1),(0,2),(1,0),(4,0),(4,1),(4,2)\}.
\]

The two complete code paths below do not use the table as input: each derives its entries by checking the visibility predicate on all recursively generated subsets. In particular, the finite computation is exhaustive rather than sampling, and the geodesic classification proves why that finite test decides the infinite quantification over all shortest paths in this specific graph.

## Verification

Two standalone implementations and their complete standard outputs are attached:

1. `verify_torus_bfs.cpp` constructs the graph adjacency, computes all-pairs distances by breadth-first search, enumerates every distance-decreasing shortest path by depth-first traversal, and counts all feasible and maximal subsets via increasing-index recursion. Build using `c++ -std=c++17 -O2 verify_torus_bfs.cpp -o torus_bfs`, then run `./torus_bfs`. Output is `bfs_results.txt`.
2. `verify_torus_geodesic.py` separately generates geodesics by their cycle arcs and placement of the single triangle-factor step; it uses Python integer masks and independently performs the exhaustive subset and maximality tests. Run `python3 verify_torus_geodesic.py`. Output is `geodesic_results.txt`.

Both complete implementations were executed from the exact supplied source files. Their ten coefficient triples and two grand totals agree exactly. The Python output additionally prints one explicit maximal set for each occurring size. This verifies the finite census reproducibly without relying on a standalone, uninspected execution log.

## Relationship to prior work

Brešar and Yero introduced the lower ordinary mutual-visibility invariant and explicitly asked for its determination on Cartesian tori in concluding Problem 1 of their 2023 preprint. Their general Neighborhood Lemma and results for Cartesian products of paths or complete graphs do not give the value for \(C_3\square C_8\). Korže and Vesel determined the **maximum** ordinary mutual-visibility number for products of cycles; their Proposition 3.9 implies \(\mu(C_3\square C_8)=9\), already known, but does not determine the minimum *inclusion-maximal* cardinality or either cardinality polynomial.

A published research record on **odd** three-row tori establishes \(\mu^-(C_3\square C_n)=5\) for odd \(n\ge5\). Its complete proof assumes odd circumference, and expressly excludes even widths. This result concerns the even eight-column torus and is not a specialization of that theorem. Other available literature on dual/total/fault-tolerant visibility investigates different conditions or largest sets, and does not imply the present full ordinary maximal-set census. None of the inspected relevant statements or exact tables covers the result claimed here.

## Limitations

The exact new census and lower value concern only the fixed \(24\)-vertex graph \(C_3\square C_8\), not all even three-row tori. Although computations for other circumferences may suggest patterns, no general even-width lower-number formula is asserted or inferred here. Both checks are finite deterministic exhaustive computations, not independent external mathematical audits. Publication priority is based on the named searches and examined sources, and an unindexed equivalent census remains possible. All coefficients count labeled vertex subsets rather than equivalence classes under automorphisms.

## References

1. B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951, v1 first public 2023-07-06, concluding Problem 1 and Neighborhood Lemma. https://arxiv.org/abs/2307.02951
2. D. Korže and A. Vesel, *Mutual-Visibility Sets in Cartesian Products of Paths and Cycles*, *Results in Mathematics* 79 (2024), article 116, Proposition 3.9, DOI: 10.1007/s00025-024-02139-x. https://doi.org/10.1007/s00025-024-02139-x
3. *Lower mutual-visibility number of odd three-row tori*, published result record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-lower-mutual-visibility-number-of-odd-three-row-tori--543189f5b94a
4. S. Cicerone, G. Di Stefano, and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, arXiv:2112.13024; maximum/independent variants. https://arxiv.org/abs/2112.13024
