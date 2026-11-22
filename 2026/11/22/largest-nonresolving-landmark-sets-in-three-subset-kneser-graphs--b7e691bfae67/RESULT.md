# Largest nonresolving landmark sets in three-subset Kneser graphs: a sharp odd-graph exception

## Finding

For every integer \(n\ge7\), let \(G_n=\operatorname{KG}(n,3)\) be the graph whose vertices are the three-subsets of \([n]\), two vertices adjacent precisely when disjoint. A vertex landmark set \(S\) *resolves* the graph if, for every distinct vertices \(A,B\), some \(W\in S\) satisfies \(d(W,A)\ne d(W,B)\). Define \(\operatorname{dim}_{\mathrm{th}}(G_n)\) as the smallest integer \(t\) for which **every** set of \(t\) vertices resolves.

Then

\[
\operatorname{dim}_{\mathrm{th}}(G_n)=
\begin{cases}
16,&n=7,\\
\binom n3-2\binom{n-4}{2}-1,&n\ge8.
\end{cases}
\]

More strongly, the number of **largest** nonresolving sets of graph vertices (under fixed ground labels) is exactly \(21\) when \(n=7\), and

\[
\binom n2\binom{n-2}{2}
\]

when \(n\ge8\). At the exceptional order seven, these \(21\) sets are indexed by the pairs \(T\in\binom{[7]}2\): each consists of all three-subsets containing both or neither elements of \(T\). For every \(n\ge8\), each largest nonresolving set is the distance bisector of exactly one unordered pair of vertices of the form \(K\cup\{c\},K\cup\{d\}\) with \(|K|=2\) and distinct \(c,d\notin K\).

## Assumptions and scope

All graphs are finite, simple, undirected, and connected. The domain is the full connected rank-three Kneser family \(n\ge7\); no assertion is made for the disconnected cases \(n\le6\). Ground points \([n]\) are labelled, while the pair of unresolved vertices is unordered. Every distance is graph-shortest-path distance. "Largest" always means maximum cardinality among *all* nonresolving landmark sets, not merely inclusion-maximal cardinality; smaller inclusion-maximal nonresolving sets are not classified here.

For a vertex pair \(A\ne B\), write

\[
E(A,B)=\{W:d(W,A)=d(W,B)\},\qquad
R(A,B)=V(G_n)\setminus E(A,B).
\]

The set \(S\) is nonresolving exactly when \(S\subseteq E(A,B)\) for at least one pair \(A,B\). Thus, with \(N=\binom n3\), the largest possible nonresolving size is \(N-\min_{A\ne B}|R(A,B)|\), and the universal threshold is exactly one larger. These general reductions are elementary, and are not claimed as new.

## Proof

**The seven-point odd-graph case.** For \(n=7\), the graph distance between distinct triple-vertices \(A,W\) is \(1,3,2\), according as \(|A\cap W|\) equals \(0,1,2\); distance to itself is zero. For intersection zero there is an edge. For intersection two, a common neighbor is the complementary triple of \(A\cup W\). For intersection one, no common neighbor exists, but there is a length-three walk through two disjoint triples (choose one outside point alongside the two elements exclusive to the second endpoint, then the complementary triple to the first intermediate endpoint and the second original endpoint). Hence these four intersection categories give four **distinct** distances.

Take distinct triples \(A,B\), put \(r=|A\cap B|\) and \(k=3-r\). Equality of distances to a third triple \(W\) is equivalent to equality of intersection sizes with \(A,B\), or to \(|W\cap(A\setminus B)|=|W\cap(B\setminus A)|\). Choosing \(j\) points from each exclusive part yields

\[
|E(A,B)|=\sum_{j=0}^{k}\binom{k}{j}^{2}\binom{7-2k}{3-2j},
\]

with out-of-range binomial coefficients interpreted as zero. At \(r=0,1,2\), respectively, these values are \(9,13,15\). Thus the maximum nonresolving cardinality is \(15\) and the threshold is \(16\), attained only by pairs with overlap two.

Such a pair is \(A=K\cup\{c\}\), \(B=K\cup\{d\}\), where \(|K|=2\). The equality condition reduces to \(W\) containing **both or neither** of \(c,d\), independently of \(K\). This gives one maximum bisector \(E_T\) per switch pair \(T=\{c,d\}\). In \(E_T\), either switch point occurs in exactly five triples, while every other ground point occurs in seven. Thus distinct \(T\) give distinct bisectors. There are precisely \(\binom72=21\) of them, and each is witnessed by the \(\binom52=10\) possible choices of \(K\) outside \(T\).

**All \(n\ge8\).** Any two distinct triples intersecting in one or two points have a common disjoint triple, hence distance two; disjoint triples have distance one. Put \(q=\binom{n-3}{3}\). For two triples intersecting in \(r\) points, the number of their common neighbors is \(c_r=\binom{n-6+r}{3}\). Their resolving-neighborhood cardinalities therefore are

\[
D_0=2(q-c_0),\qquad
D_1=2+2(q-c_1),\qquad
D_2=2+2(q-c_2).
\]

The separate formula for \(D_0\) reflects that adjacent endpoints already belong to the symmetric difference of their open neighborhoods; nonadjacent endpoints instead add exactly two vertices outside that symmetric difference. Since \(c_2>c_1\), we have \(D_2<D_1\). Also

\[
D_0-D_2=2(c_2-c_0-1)>0
\]

for \(n\ge8\) (already \(c_2-c_0=4\) at \(n=8\), and it increases with \(n\)). Hence the unique orbit of *minimum-size* resolving neighborhoods has \(r=2\), with

\[
D_2=2+2\left(\binom{n-3}{3}-\binom{n-4}{3}\right)
=2+2\binom{n-4}{2}.
\]

The threshold formula follows immediately from \(N-D_2+1\).

To count the largest bisectors without overcounting, fix \(A=K\cup\{c\}\), \(B=K\cup\{d\}\) with \(|K|=2\), \(T=\{c,d\}\) disjoint from \(K\). Directly from the diameter-two distances, their resolving neighborhood is

\[
R(K,T)=\{K\cup\{c\},K\cup\{d\}\}\;\cup\;
\{W\in\tbinom{[n]\setminus K}{3}:|W\cap T|=1\}.
\]

For each ground point \(x\), count how many triple-vertices of \(R(K,T)\) contain \(x\). The count is \(2\) for \(x\in K\), is \(1+\binom{n-4}{2}\) for \(x\in T\), and is \(2(n-5)\) for every other ground point. For all \(n\ge8\),

\[
2<2(n-5)<1+\binom{n-4}{2}
\]

(the last difference equals \(1+(n-5)(n-8)/2\)). These three distinct frequencies recover \(K\) and \(T\) uniquely from \(R\), and thus from its complement \(E\). There are exactly \(\binom n2\) choices of \(K\) and \(\binom{n-2}{2}\) of \(T\). Any nonresolving set of maximum size must equal one of these maximum bisectors, completing the classification.

## Verification

Two standalone exhaustive programs independently enumerate vertex distances and all unordered pairs of potential unresolved vertices for the labelled graphs at \(n=7,8,9,10,11\). The first uses graph breadth-first search; the second uses an intersection-distance formula coded separately in C++. They compare all pair-bisector sizes, identify the minimum resolving-neighborhood sizes and deduplicate maximum bisectors. Their outputs agree exactly.

| \(n\) | \(\binom n3\) | smallest \(|R|\) | threshold | largest nonresolving size | distinct largest nonresolving sets |
|---:|---:|---:|---:|---:|---:|
| 7 | 35 | 20 | 16 | 15 | 21 |
| 8 | 56 | 14 | 43 | 42 | 420 |
| 9 | 84 | 22 | 63 | 62 | 756 |
| 10 | 120 | 32 | 89 | 88 | 1260 |
| 11 | 165 | 44 | 122 | 121 | 1980 |

Reproduce with `python3 verify_bfs.py`, `c++ -O2 -std=c++17 verify_intersection.cpp -o verify_intersection` and `./verify_intersection`. The supplied `verify_bfs.out` and `verify_intersection.out` are the corresponding complete output records; the compiled binary is intentionally not required. Finite computations cross-check the proof but do **not** establish the all-\(n\) theorem on their own.

## Relationship to prior work

The metric-dimension threshold was defined and studied by Korivand, Khashyarmanesh and Tavakoli (2022), who determine it for paths, cycles and the Petersen graph \(\operatorname{KG}(5,2)\). Their general definition and monotonicity are used here; their Petersen value is not an instance of this rank-three theorem.

Bonato, Huggan and Marbach (public preprint 2020, journal 2023) study the *minimum* metric dimension and the adaptive localization number of Kneser graphs, with bounds for fixed rank, not the worst-case landmark threshold or full maximum-bisector classification. The rank-two analogue for \(\operatorname{KG}(n,2)\) was also identified in a published research record; it does not cover triple-vertices or the seven-point exception. The present assertion is the all-order rank-three threshold and the complete family of its largest nonresolving sets. No exhaustive historical priority claim is made.

## Limitations

The classification is for rank-three Kneser graphs with \(n\ge7\) only. It does not classify all *smaller inclusion-maximal* nonresolving landmark families or provide values for higher Kneser rank. A priority search cannot eliminate the possibility of an unindexed earlier result. Self-review is not independent external mathematical verification.

## References

1. M. Korivand, K. Khashyarmanesh, M. Tavakoli, *Metric Dimension Threshold of Graphs*, Journal of Mathematics (2022), DOI: https://doi.org/10.1155/2022/1838719; first online 2022-09-14.
2. A. Bonato, M. Huggan, T. Marbach, *The localization number and metric dimension of graphs of diameter 2*, arXiv:2008.04896, first posted 2020-08-11; Contributions to Discrete Mathematics 18 (2023), https://cdm.ucalgary.ca/article/view/71209.
3. *Maximum nonresolving landmark families of triangular and two-subset Kneser graphs*, published research record https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-maximum-nonresolving-landmark-families-of-triangular-and-two-sub--290a05e93094 (summary checked; full artifact unavailable in this search environment).
