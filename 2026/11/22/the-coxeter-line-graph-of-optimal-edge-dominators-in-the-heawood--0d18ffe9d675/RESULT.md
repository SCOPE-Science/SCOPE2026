# The Coxeter line graph of optimal edge dominators in the Heawood graph

## Finding

Let \(H\) be the Heawood graph, the point–line incidence graph of the Fano plane. For \(S\subseteq E(H)\), call \(S\) *edge dominating* if every edge of \(H\) has an endpoint in common with some member of \(S\). An edge-dominating set is *inclusion-minimal* if no proper subset is edge dominating. The full inclusion-minimal cardinality polynomial is
\[
F_H(z)=42z^5+1246z^6+24z^7.
\]
Consequently the edge domination number is \(\gamma_e(H)=5\); its \(42\) minimum sets are all matchings. In fact the polynomial of inclusion-maximal matchings is
\[
M_H(z)=42z^5+168z^6+24z^7.
\]

Let \(\mathcal X\) have these \(42\) minimum edge-dominating sets as vertices, two adjacent exactly when two selected edges can be removed and two different edges inserted to obtain another minimum set (equivalently, their symmetric difference has size four). Then
\[
\boxed{\mathcal X\cong L(\mathrm{Cox})},
\]
where \(\mathrm{Cox}\) is the classical \(28\)-vertex cubic Coxeter graph and \(L\) is the line-graph operation. Thus \(\mathcal X\) is connected, has \(42\) vertices and \(84\) edges, is \(4\)-regular with diameter \(5\), and has the same distance profile \((1,4,8,16,12,1)\) at every vertex. No two distinct optima admit a one-edge replacement: two simultaneous replacements are the sharp threshold for connectivity.

For completeness, the number \(a_j\) of *all* edge-dominating sets of cardinality \(j\) is zero for \(j<5\), and for \(j=5,\dots,21\) is, in increasing order,
\[
(a_5,\dots,a_{21})=(42,1918,15186,58044,137522,226422,276192,259518,192318,113802,53928,20328,5985,1330,210,21,1).
\]
This is a fixed-graph, exact theorem, not a family-wide statement for arbitrary projective planes.

## Assumptions and scope

The Fano plane has seven points and seven lines, three points per line, three lines per point, and exactly one line through any two points. Its Levi graph \(H\) has \(14\) vertices and \(21\) edges. An *edge dominating set* need not be a matching; a *maximal matching* is a matching that cannot be extended by another graph edge; these notions coincide only after restricting to matching edge sets. The polynomial \(F_H\) counts all inclusion-minimal edge dominators, including nonmatchings. Every graph edge and every configuration is treated as a distinct labelled edge subset; no division by graph automorphisms is performed.

The Coxeter graph is used in its classical Fano model: its \(28\) vertices are the noncollinear three-point subsets of the Fano plane and two are adjacent when disjoint. Equivalently it is the disjointness graph on the \(28\) hexagons of the Heawood graph; this classical description is not asserted as new. The new assertion is the identification of its **line graph with the two-edge exchange graph of minimum edge-dominating sets**.

## Proof

**Lower bound and rigidity at equality.** Suppose \(S\) edge dominates and \(|S|\le4\). On each bipartition shore at most four vertices meet the chosen edges, leaving at least three uncovered points and three uncovered lines. Since any three Fano points meet at least six of its seven lines, at most one line avoids those points. Hence three uncovered lines are impossible. Thus \(\gamma_e(H)\ge5\).

For \(|S|=5\), let \(P_0\) and \(L_0\) denote respectively the unused points and unused lines. Both have cardinality at least two and there are no incidences between them. A pair of distinct Fano points is incident with five lines, so exactly two lines miss the pair. Three points meet at least six lines; hence \(|P_0|=|L_0|=2\). Thus precisely five points and five lines are covered by the five chosen flags, which must form a matching. Choosing the two unused points uniquely fixes the two unused lines. The remaining incidence subgraph has exactly two perfect matchings. To see this for one representative pair in the binary model, label the nonzero vectors by \(1,\dots,7\), with point \(x\) on line \(a\) when their binary dot product is zero. For omitted points \(1,2\), the remaining point–line adjacency lists are
\[
3\mapsto\{4\},\quad4\mapsto\{1,2\},\quad5\mapsto\{2,5\},\quad6\mapsto\{1,6\},\quad7\mapsto\{5,6\}.
\]
The edge from \(3\) to \(4\) is forced, and the remaining bipartite cycle of length eight has two perfect matchings. Linear automorphisms of the binary Fano plane act transitively on unordered point pairs; hence there are exactly \(\binom72\cdot2=42\) minimum edge dominators, and an explicit construction attains five.

**All inclusion-minimal sizes.** Write the \(21\) distinct flags as \(e_0,\dots,e_{20}\), and let \(B_i\) be the indices of graph edges sharing an endpoint with \(e_i\), including \(i\) itself. For each binary mask \(S\), define
\[
D(0)=\varnothing,\qquad D(S)=D(S\setminus\{i\})\cup B_i,
\]
where \(i\) is the least index in \(S\). By induction, \(D(S)\) is **exactly** the set of graph edges dominated by \(S\). Consequently \(S\) is edge dominating if and only if \(D(S)=E(H)\); it is inclusion-minimal if and only if, additionally, \(D(S\setminus\{i\})\ne E(H)\) for every \(i\in S\). This yields an exhaustive certificate consisting of exactly \(2^{21}\) masks, and two implementations with distinct incidence presentations independently compute
\[
\sum_{S\text{ inclusion-minimal}}z^{|S|}=42z^5+1246z^6+24z^7.
\]
Testing whether a qualifying \(S\) is a matching also gives \(M_H(z)=42z^5+168z^6+24z^7\). The complete \(a_j\) coefficients stated above arise by the same recurrence without the minimality test.

**The Coxeter exchange identification.** In the cyclic incidence model take point labels \(0,\dots,6\) and seven lines \(\{j,j+1,j+3\}\) modulo \(7\); order the \(21\) flags lexicographically by point then line, and enumerate the \(42\) qualifying five-edge matchings by increasing their \(21\)-bit masks. Join two states if the XOR of their masks has exactly four set bits. The exact finite certificates verify that this exchange graph has \(28\) triangles, that each of its \(42\) vertices belongs to exactly two of those triangles, and that each exchange edge belongs to exactly one triangle. Form a quotient \(Q\) with a vertex for each triangle and an edge for each original matching shared by two triangles. Then \(Q\) has \(28\) vertices, \(42\) edges and is cubic, while the original exchange graph is exactly \(L(Q)\).

Order the \(28\) triangles lexicographically by their increasing state-index triples. Order the \(28\) noncollinear Fano point triples lexicographically and join two when disjoint. An explicit isomorphism from the quotient triangles to those Coxeter triples is the index permutation
\[
(0,25,6,15,17,27,19,26,13,10,7,2,23,20,21,9,3,24,22,1,16,5,18,4,14,11,12,8).
\]
The standalone certificate `verify_coxeter.py` constructs the two graphs without calling any external graph software and tests the adjacency equivalence for all \(28^2\) ordered vertex pairs. It separately checks that a pair of optimum matchings is exchange-adjacent exactly when their corresponding two quotient edges meet. This proves \(Q\cong\mathrm{Cox}\) and \(\mathcal X\cong L(\mathrm{Cox})\). Exhaustive breadth-first searches establish the claimed diameter and full distance profile. A direct XOR check shows that all distinct optimum matching masks differ in at least four bits, excluding one-edge replacement.

## Verification

Three complete standalone programs and their recorded deterministic outputs accompany this statement. Compile `verify_binary.cpp` with `g++ -O2 -std=c++17 verify_binary.cpp -o verify_binary` and run `./verify_binary`. Also run `python3 verify_cyclic.py` and `python3 verify_coxeter.py`; the Python implementations use only the standard library. Their success markers are respectively `VERIFY_BINARY_OK`, `VERIFY_CYCLIC_OK`, and `VERIFY_COXETER_OK`.

The C++ program directly enumerates all \(2^{21}\) edge subsets in a vector-space Fano model and records every coefficient of both domination polynomials. The cyclic Python program independently builds the Fano lines, uses a distinct point/line vertex-cover dynamic representation, enumerates every subset, and reproduces all counts and exchange distances. The third program enumerates all \(\binom{21}{5}\) candidate five-matchings, computes the exchange triangles and quotient, and checks the explicit Coxeter permutation and all pairwise adjacencies. These are finite exhaustive certificates for this fixed \(21\)-edge graph; they are not an inference from sampling or a claim about unbounded graph orders.

## Relationship to prior work

Spiro, Adriaensen and Mattheus introduced a general incidence-free-set approach to edge domination in incidence graphs and studied projective-plane incidence structures. Their results provide the motivating reduction and general extremal bounds, but the inspected full text does not state the present exact full inclusion-minimal polynomial or the optimum exchange graph. Classical sources already identify the Coxeter graph as the disjointness graph of Heawood hexagons; that old identification is explicitly **not** claimed as new here. The present contribution links **minimum edge-dominating matchings** to the line graph of that Coxeter graph and supplies the complete minimal and all-dominator censuses.

The published fixed-graph study *The minimum-maximal-matching exchange graph of the Möbius–Kantor graph* studies a different \(16\)-vertex host and one-edge moves. *The Fano induced-matching exchange graph: a tripartite triangle geometry with diameter five* concerns **maximum induced** matchings of size three in the Heawood graph, not minimum maximal ordinary matchings of size five. These descriptions are not equivalent: induced matching restricts all edges between selected endpoints, while maximal ordinary matching only requires no edge between two unselected vertices. Neither cited result determines this polynomial or two-edge exchange graph.

## Limitations

The result concerns only the \(14\)-vertex Heawood graph and does not claim analogous formulas for incidence graphs of larger projective planes. The classical Coxeter graph and its previously known Heawood-hexagon interpretation are not novel. While two independent enumeration formulations and a separate explicit graph-isomorphism certificate corroborate the fixed-graph theorem, they do not constitute independent external mathematical review. The literature comparison may miss unindexed older domination tables or results under alternate terminology; publication priority is therefore provisional.

## References

1. S. Spiro, S. Adriaensen and S. Mattheus, *Incidence-free sets and edge domination in incidence graphs*, first public preprint 2022-11-25, arXiv:2211.14339, https://arxiv.org/abs/2211.14339; *Journal of Combinatorial Designs* 32 (2024), 55–87, https://doi.org/10.1002/jcd.21925.
2. M. Yannakakis and F. Gavril, *Edge dominating sets in graphs*, *SIAM Journal on Applied Mathematics* 38 (1980), 364–372, https://doi.org/10.1137/0138030.
3. I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960, especially Section 1 on Coxeter–Heawood hexagon duality, https://arxiv.org/html/1002.1960v9.
4. E. W. Weisstein, *Coxeter Graph*, MathWorld, https://mathworld.wolfram.com/CoxeterGraph.html.
5. *The minimum-maximal-matching exchange graph of the Möbius–Kantor graph*, public scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-minimum-maximal-matching-exchange-graph-of-the-m-bius-kantor--68d0d1e90545.
6. *The Fano induced-matching exchange graph: a tripartite triangle geometry with diameter five*, public scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-fano-induced-matching-exchange-graph-tripartite-triangles-an--15f94095f8d3.
