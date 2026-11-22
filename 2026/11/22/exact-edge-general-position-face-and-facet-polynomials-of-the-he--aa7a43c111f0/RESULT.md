# Exact edge-general-position face and facet polynomials of the Heawood graph

## Finding

Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano projective plane. For an edge set \(S\subseteq E(H)\), call \(S\) *edge-general-position* (EGP) when no shortest path in \(H\) contains three distinct edges of \(S\). Define the labelled-graph cardinality polynomial
\[
P_H(z)=\sum_{\substack{S\subseteq E(H)\\S\text{ is EGP}}} z^{|S|}.
\]
Then the complete exact polynomial is
\[
\boxed{P_H(z)=1+21z+210z^2+1246z^3+4725z^4+11592z^5+17962z^6+16446z^7+7875z^8+1617z^9+84z^{10}.}
\]
If \(F_H(z)\) instead counts the *inclusion-maximal* EGP subsets by their cardinalities, then
\[
\boxed{F_H(z)=66z^7+546z^8+861z^9+84z^{10}.}
\]
Consequently there are exactly \(61779\) EGP edge subsets and \(1557\) inclusion-maximal EGP sets. The edge-general-position number is \(10\); there are exactly \(84\) maximum subsets; every inclusion-maximal subset has size \(7,8,9\), or \(10\). The enumeration keeps the 21 edges distinguished; it does not quotient by graph automorphisms.

## Assumptions and scope

The graph is the unique connected bipartite point-line incidence graph of the order-two projective plane, with 7 point vertices and 7 line vertices, hence 21 edges. Fix the points as \(\mathbb Z/7\mathbb Z\) and define, for each \(j\in\mathbb Z/7\mathbb Z\),
\[
L_j=\{j,j+1,j+3\}\pmod 7.
\]
The edge set is the 21 flags \(\{(p,L_j):p\in L_j\}\). All paths and distances are taken in the unweighted simple graph; *geodesic* means shortest path between its endpoints. Inclusion-maximal means no additional single edge can be added while preserving EGP, not necessarily maximum cardinality.

## Proof

**Step 1: Geodesic triples have a projective-plane description.** Any two distinct points determine a unique line, and any two distinct lines meet in a unique point. Point-point or line-line distances are \(2\), incident point-line distances are \(1\), and nonincident point-line distances are \(3\). Therefore the diameter is \(3\). A shortest path containing three edges must have length exactly \(3\); its ends must be a nonincident point \(p\) and line \(L\). Every such path is uniquely of the form
\[
p\;--\;L(p,q)\;--\;q\;--\;L,
\]
where \(q\in L\), and \(L(p,q)\) is the unique line through \(p,q\). Conversely every such sequence is a shortest three-edge path. There are exactly \(7(7-3)=28\) nonincident ordered point-line pairs and three choices of \(q\) for each; the resulting \(28\cdot3=84\) *distinct unordered triples of edges* are all the forbidden triples. Distinctness follows because the three-edge path is determined by its edge set (the graph has girth \(6\)) and an undirected path has a unique point endpoint and line endpoint in this case.

**Step 2: An exact finite recurrence decides every subset.** Enumerate the 21 graph edges as \(e_0,\ldots,e_{20}\) by increasing line index and then by the displayed order of the three points on the line. Identify a subset \(S\) with a 21-bit mask. Construct the collection \(\mathcal B\) of the 84 forbidden 3-bit masks from Step 1. Let \(v(\varnothing)=1\) and let \(v(S)\in\{0,1\}\) be its EGP indicator. For nonempty \(S\), set \(h=\max\{i:e_i\in S\}\), \(S'=S\setminus\{e_h\}\), and compute
\[
v(S)=v(S')\prod_{\substack{B\in\mathcal B\\\max(B)=h}}\Bigl(1-\mathbf1\bigl[(B\setminus\{e_h\})\subseteq S'\bigr]\Bigr).
\]
Indeed every forbidden triple in \(S\) either already lies in \(S'\) or contains its highest-index edge \(e_h\). This recurrence is exact for all \(2^{21}=2097152\) masks, in ascending integer order: \(S'\) is always an earlier mask. Its 22 cardinality sums are exactly
\[
(1,21,210,1246,4725,11592,17962,16446,7875,1617,84,0,\ldots,0).
\]
These are the coefficients of \(P_H\). The first three values also follow independently from \(\binom{21}{0}\), \(\binom{21}{1}\), and \(\binom{21}{2}\); the degree-three count is \(\binom{21}{3}-84=1246\).

**Step 3: Maximality is a complete one-edge test.** The EGP condition is hereditary under taking subsets, so a feasible set \(S\) is inclusion-maximal if and only if *every* missing edge \(e\) makes \(S\cup\{e\}\) infeasible. Thus, using only the previously determined indicators,
\[
m(S)=v(S)\prod_{e\in E(H)\setminus S}\bigl(1-v(S\cup\{e\})\bigr),
\qquad F_H(z)=\sum_{S\subseteq E(H)}m(S)z^{|S|}.
\]
The complete exhaustive evaluation yields exactly \(66,546,861,84\) maximal sets at sizes \(7,8,9,10\), respectively, and none in any other degree. This establishes every stated extremal count and bound. In particular, no absence of larger sets is inferred from a partial search: the recurrence evaluates *every* subset.

## Verification

The package contains two standalone verification programs, with their integer outputs checked against the displayed formulas.

- `verify_fano.cpp`: derives forbidden masks directly from the Fano incidence axioms, visits every one of the \(2^{21}\) edge subsets by the recurrence in Step 2, and tests the 21 possible one-edge extensions to count maximal sets. Compile with `g++ -O2 -std=c++17 verify_fano.cpp -o verify_fano` and run `./verify_fano`.
- `verify_bfs.py`: builds the same incidence graph using an *independent edge ordering*, runs BFS from each vertex, reconstructs **all** shortest paths by decreasing distance, derives their forbidden edge triples, and independently enumerates exactly all feasible masks with a depth-first inclusion/exclusion search. Run `python3 verify_bfs.py`.

Both algorithms obtain 84 forbidden triples, 61,779 legal sets and 1,557 maximal sets with coefficientwise agreement. The C++ recurrence, geometric enumeration, and independent BFS/DFS certificate together establish a reproducible *finite exhaustive proof*, not a sampling argument or an unproved infinite extension.

## Relationship to prior work

Manuel, Prabha and Klavžar introduced the edge-general-position invariant in 2021 and solved it for hypercubes, trees, and Cartesian grids. Tian, Klavžar and Tan subsequently characterized two extremal parameter cases and obtained results for block graphs. Those results concern a different graph class or parameter regime and do not give the Heawood graph's all-subset or maximal-subset polynomials. Separate later work investigates graphs of edge-general-position number four or with edge-general-position number equal to their edge count minus two; neither numerical regime covers the present 21-edge graph, whose number is ten. Published records for Fano-plane incidence graphs concern other invariants such as induced matchings, forcing, convexity, geodetic bases, and edge-open packing; none of their stated numerical conclusions implies these EGP enumerators. This is a best-knowledge publication-priority comparison, not a proof of global literature uniqueness.

## Limitations

The polynomial claims concern only the fixed 14-vertex Heawood graph. They do **not** establish a formula for higher-order projective-plane incidence graphs, nor do they classify orbit types of the 84 maximum sets. The independent-source code checks independently reproduce one *finite* computation; they do not constitute independent human mathematical review. Full-text access to some later, potentially related edge-general-position articles was incomplete, and earlier unindexed computations may remain. A separate independent mathematical audit has not been performed.

## References

1. Paul Manuel, R. Prabha and Sandi Klavžar, *Edge General Position Problem*, arXiv:2105.04292, first submitted 10 May 2021. https://arxiv.org/abs/2105.04292
2. Jing Tian, Sandi Klavžar and Elif Tan, *Extremal Edge General Position Sets in Some Graphs*, arXiv:2302.01587, first submitted 3 February 2023; *Graphs and Combinatorics* 40, article 40 (2024). https://arxiv.org/abs/2302.01587
3. Yahan Cao, Shengjin Ji and Lihui Wang, *The Edge General Position Number of Some Graphs*, *Bulletin of the Malaysian Mathematical Sciences Society* 48, article 95 (2025). https://doi.org/10.1007/s40840-025-01873-x
4. Z. Hamed-Labbafian, M. A. Henning and M. Tavakoli, *Edge general position in graphs: Graph products, integer linear programming and some applications*, *Discrete Applied Mathematics* 386 (2026), 1–8. https://doi.org/10.1016/j.dam.2026.01.008
