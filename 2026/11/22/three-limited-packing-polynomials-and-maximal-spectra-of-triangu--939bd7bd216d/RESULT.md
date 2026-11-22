# Three-limited packing polynomials and maximal spectra of triangular graphs \(T_n\)

## Finding

For every integer \(n\ge3\), let \(T_n=J(n,2)=L(K_n)\) be the triangular graph on the two-element subsets of \([n]\), adjacent when they intersect. A subset \(S\subseteq V(T_n)\) is a *three-limited packing* if every closed vertex neighborhood meets \(S\) in at most three vertices. Denote by \(P_n(z)=\sum_{S}z^{|S|}\) its all-packing polynomial and by \(M_n(z)=\sum_{S\text{ inclusion-maximal}}z^{|S|}\) its inclusion-maximal polynomial, in both cases with individually labelled original vertices.

**Structural classification.** Identify selected vertices of \(T_n\) with the edge set of a graph \(H\subseteq K_n\). Precisely the following five types occur, with unused root vertices isolated:

1. A matching.
2. A matching and one separate two-edge path (three root vertices).
3. A matching and one separate triangle (three root vertices).
4. A matching and one separate three-edge path (four root vertices).
5. One three-edge star and no other selected edges.

**Complete all-packing polynomial.** The following formal exponential generating function determines every coefficient for every \(n\ge3\):

\[
\sum_{n\ge0}P_n(z)\frac{x^n}{n!}
=e^{x+zx^2/2}\left(1+\frac{x^3z^2}{2}+\frac{x^3z^3}{6}+\frac{x^4z^3}{2}\right)
+\frac{x^4z^3}{6}e^x.
\]

**Complete inclusion-maximal polynomial.** The low-order case is \(M_3(z)=z^3\). For every integer \(m\ge2\),

\[
M_{2m}(z)=2m\binom{2m-1}{3}z^3
+\frac{4(2m)!}{6\,2^{m-2}(m-2)!}z^{m+1},
\]

and

\[
\begin{aligned}
M_{2m+1}(z)={}&(2m+1)\binom{2m}{3}z^3\\
&+\frac{(2m+1)!}{2^{m-1}(m-2)!}z^{m+1}\\
&+\frac{(2m+1)!}{6\,2^{m-1}(m-1)!}z^{m+2}.
\end{aligned}
\]

In particular, \(L_3(T_n)=\lceil n/2\rceil+1\) for every \(n\ge3\), whereas every \(T_n\) admits an inclusion-maximal packing of size three and none smaller. The complex of all three-limited packings is pure for \(n=3,4\) and nonpure for every \(n\ge5\). Its facet sizes can diverge: for even \(n\ge8\), they are **only** \(3\) and \(n/2+1\).

## Assumptions and scope

The graph \(K_n\) is finite, simple and labelled by \([n]\). A root edge is the vertex of \(T_n\) corresponding to that edge. “Maximal” always means inclusion-maximal, not maximum cardinality. Closed neighborhoods include their central vertex. All enumerated subsets are labelled, with neither automorphism quotienting nor color assignments. The formulas and structural classification apply for all integers \(n\ge3\), without asymptotic assumptions. The exponential series uses \(n\ge0\) as a formal bookkeeping convention for its combinatorial components; the graph-theoretic statement is restricted to \(n\ge3\).

## Proof

**1. Reduction to root degrees.** Let \(H\) be the graph with selected edge set \(S\subseteq E(K_n)\), and let \(d_H(u)\) denote the degree of root vertex \(u\). For any distinct roots \(u,v\), the closed neighborhood of the vertex \(uv\in T_n\) consists of all root edges incident with \(u\) or \(v\). Thus exactly

\[
|N_{T_n}[uv]\cap S|=d_H(u)+d_H(v)-\mathbf1_{\{uv\in E(H)\}}.
\]

A three-limited packing therefore is exactly a root graph satisfying

\[
\forall u\ne v:\quad d_H(u)+d_H(v)-\mathbf1_{\{uv\in E(H)\}}\le3.\tag{1}
\]

**2. Complete structural classification.** Equation (1), applied at an edge incident with a maximum-degree root vertex, forbids any vertex of degree at least four: the sum is at least \(4+1-1=4\). If \(d_H(u)=3\), every root vertex of positive degree must be adjacent to \(u\) (otherwise its degree sum with \(u\) exceeds three). Every neighbor \(v\) of \(u\) has \(d_H(v)\le1\), again by (1). Hence \(H\) is exactly the isolated three-star.

Otherwise all degrees are at most two. If two vertices have degree two, their joining edge must be selected: a missing edge would give degree sum four in (1). Consequently all degree-two vertices form a clique of size at most three. If there are three, they form a triangle and every other nonisolated component is a single edge. If there are two, they form an adjacent pair; each has one other neighbor, and if those neighbors coincide this is the triangle case, while if they are distinct the component is the three-edge path. If there is exactly one degree-two vertex, its component is a two-edge path. If none, \(H\) is a matching. The remaining components in all but the three-star case have maximum degree one and thus are single edges or isolated roots. Conversely every listed type satisfies (1): selected-edge degree sums are at most four with the required subtraction; every unselected pair has degree sum at most three. This proves necessity and sufficiency.

**3. All-packing count.** Disjoint isolated root vertices and edges contribute the labelled matching species \(\exp(x+zx^2/2)\). There are respectively three two-edge paths on three roots, one triangle on three roots, and twelve undirected three-edge paths on four roots; their respective labelled exponential weights are \(x^3z^2/2\), \(x^3z^3/6\), and \(x^4z^3/2\). One three-star has four choices of center on four roots, contributing \(x^4z^3/6\), with arbitrary isolated roots only, hence the extra \(e^x\). These disjoint cases give the displayed exponential generating function without double counting.

**4. Characterization of maximal sets.** A selected-edge matching on at least three roots is extendible: add an edge between an isolated root and another root, or join endpoints of different matched edges. A two-edge path is extendible by its third closing edge to a triangle. The isolated three-star is never extendible, since any added edge creates a new positive-degree root outside its three leaves or raises a leaf's degree; in either case (1) fails. A three-edge path or triangle with disjoint matching edges can be extended **if and only if** there are at least two unused roots, in which case joining two such unused roots is valid. Indeed, adding any edge incident with a degree-two root creates degree three adjacent to another degree-two root or contradicts the degree-three star characterization; adding to an endpoint of the path or to a matched edge produces two nonadjacent degree-two roots, violating (1). Therefore maximality is equivalent to having zero or one isolated root. In the special case \(n=3\), the only maximal set is the full triangle; for \(n=4\), the same classification also applies and three-star, triangle-plus-one-isolate, and three-edge paths are all maximal.

**5. Maximal counts.** The number of labelled three-stars is \(n\binom{n-1}{3}\). On four specified roots there are \(4!/2=12\) undirected three-edge paths, and on three specified roots there is one triangle. When \(n=2m\), a maximal path has a perfect matching on the other \(2m-4\) roots; a maximal triangle has one isolated root and a perfect matching on the other \(2m-4\) roots. Their combined count is

\[
\frac{(2m)!}{2^{m-2}(m-2)!}\left(\frac12+\frac16\right)
=\frac{4(2m)!}{6\cdot2^{m-2}(m-2)!}.
\]

When \(n=2m+1\), maximal paths have one unused root and a perfect matching on \(2m-4\) roots, contributing \((2m+1)!/[2^{m-1}(m-2)!]\), and maximal triangles have a perfect matching on \(2m-2\) roots, contributing \((2m+1)!/[6\cdot2^{m-1}(m-1)!]\). Together with the stars, these prove both displayed formulas. The cardinality extremes and purity assertions follow immediately from their nonzero coefficients.

## Verification

Three separate executable scripts are supplied. `verify_formula.py` computes the component formulas exactly for orders 3 through 11 with arbitrary-precision integers. `verify_bruteforce.cpp` explores all feasible root-edge subsets for orders 3 through 9, checking condition (1) directly for every vertex pair and each one-edge maximality extension. `verify_incidence.py` ignores the root-degree identity and enumerates every subset directly from the closed neighborhoods of the triangular graph for orders 3 through 7. Their stored exact output tables are `formula_counts.tsv`, `exhaustive_counts.tsv` and `incidence_counts.tsv`, respectively. Each entry has three tab-separated fields: root order, nonzero all-packing coefficients as `degree:count`, and nonzero inclusion-maximal coefficients likewise. The trailing comma in the C++ columns is a display convention, not part of the integer counts.

To replay using standard Python 3 and C++17:

```bash
python3 verify_formula.py
c++ -std=c++17 -O2 verify_bruteforce.cpp -o verify_bruteforce
./verify_bruteforce 3 9
python3 verify_incidence.py
```

For example \(M_7(z)=140z^3+1260z^4+105z^5\), \(M_8(z)=280z^3+3360z^5\), and \(M_9(z)=504z^3+22680z^5+1260z^6\); these are reproduced independently. The finite checks corroborate the universal theorem, whose all-orders proof is the structural argument above, not extrapolation from small orders.

## Relationship to prior work

The closed-neighborhood capacity definition originates in the limited-packing literature. Ahmadi, Soltankhah and Samadi's 2023 preprint studies limited-packing partitions (especially capacity two) and total limited packing; the text available in its 2023 preprint does not give this structural or enumerative classification of triangular graphs. Ahmadi and Soltankhah's 2024 paper treats capacity-two total/ordinary packings, including graph products, without determining the polynomials above. Balister, Bollobás and Gunderson study general capacity bounds rather than this exact family. The present theorem works on the nonbipartite root graph \(K_n\), so the triangle component is essential; results for Cartesian products of cliques, whose root graphs are bipartite, do not imply it. Searches for line-graph, triangular-graph, closed-neighborhood packing and maximal-set equivalents found no publication containing the same coefficient and facet formulas. Search non-detection is not a proof of absolute publication priority.

## Limitations

The theorem concerns only capacity three, closed (not open) neighborhoods, and line graphs of complete graphs, with root size at least three. It does not claim a general capacity formula, a result for arbitrary line graphs, or a classification under vertex reconfiguration. It counts labelled packing sets, not automorphism orbits. The authors' published and preprint literature remains subject to independently checking unindexed or inaccessible primary sources; no independent scientific audit has been performed.

## References

1. A. S. Ahmadi, N. Soltankhah and B. Samadi, *Limited packings: related vertex partitions and duality issues*, arXiv:2308.16837, first posted 2023-08-31. https://arxiv.org/abs/2308.16837
2. A. S. Ahmadi and N. Soltankhah, *On k-(total) limited packing in graphs*, arXiv:2405.03237, first posted 2024-05-06. https://arxiv.org/abs/2405.03237
3. P. N. Balister, B. Bollobás and K. Gunderson, *Limited packings of closed neighbourhoods in graphs*, arXiv preprint (2015); available institutional abstract: https://research-information.bris.ac.uk/en/publications/limited-packings-of-closed-neighbourhoods-in-graphs/
