# A parity-defective involution law for maximal induced threshold subgraphs of triangular graphs

## Finding
For every integer \(n\ge3\), let \(T_n=L(K_n)=J(n,2)\). A vertex set of \(T_n\) is *threshold-admissible* if its induced subgraph has none of \(P_4,C_4,2K_2\) as an induced subgraph. Write \(M_n(z)\) for the sum of \(z^{|S|}\) over all inclusion-maximal threshold-admissible vertex sets \(S\). Put \(m=n-3\), \(R=\lfloor m/2\rfloor\), and
\[
b_{m,r}=\frac{m!}{(m-2r)!\,2^r r!}\qquad(0\le r\le R).
\]
Then the **complete cardinality polynomial** is
\[
\boxed{M_n(z)=\binom n3\left(3\sum_{r=0}^{R}b_{m,r}z^{n-r}
-2\mathbf1_{\{m\,\mathrm{even}\}}b_{m,R}z^{n-R}\right).}
\]
Its exponential generating function is
\[
\boxed{\sum_{n\ge3}\frac{M_n(z)t^n}{n!}=
\frac{z^3t^3}{2}e^{zt+zt^2/2}-\frac{z^3t^3}{3}e^{zt^2/2}.}
\]
The attainable maximal-set cardinalities are exactly
\[
\left\{\left\lceil\frac{n+3}{2}\right\rceil,
\left\lceil\frac{n+3}{2}\right\rceil+1,\ldots,n\right\}.
\]
Whenever at least three coefficients are positive (equivalently \(n\ge7\)), those coefficients are **strictly log-concave**. The total is \(\binom n3(3I_{n-3}-2P_{n-3})\), where \(I_j\) counts involutions on \(j\) labels and \(P_j=j!/(2^{j/2}(j/2)!)\) for even \(j\), and \(P_j=0\) for odd \(j\). Thus a uniform maximal set has the ordinary involution fixed-point count distribution when \(n\) is even; for odd \(n\), the zero-fixed-point class is downweighted by a factor of three.

## Assumptions and scope
All graphs are finite, simple, labeled graphs. \(n\) is an arbitrary integer at least three. The vertices of \(T_n\) are the two-element subsets of \([n]\), and two such vertices are adjacent precisely if they intersect. Inclusion-maximal means that no single unselected vertex can be added while retaining the hereditary threshold property. The polynomial counts actual labeled vertex subsets, not isomorphism classes. An involution here is a permutation consisting only of fixed points and disjoint transpositions, with \(I_0=P_0=1\).

## Proof
**1. Translation and structural antecedent.** For a selected vertex set \(S\subseteq V(T_n)\), regard its members as edges of a graph \(F=([n],S)\). The induced subgraph \(T_n[S]\) is exactly \(L(F)\). A threshold graph is precisely a graph with no induced \(P_4,C_4,2K_2\). Behr, Sivaraman and Zaslavsky (Proposition 41 of *Mock Threshold Graphs*) characterized the underlying graphs with threshold line graphs: at most one nontrivial component can have adjacent edges, and that component is a star with at most one additional edge, equivalently a connected subgraph of a triangle with pendant edges at one triangle vertex; other nontrivial components are isolated edges. This existing classification is an antecedent, not asserted as new here.

**2. Maximality.** For \(n\ge3\), a maximal \(F\) must contain a triangle in its exceptional component. Indeed, a star with at least two edges can be enlarged by joining two leaves; a star with an additional edge to a new vertex can be enlarged by joining that vertex to the star center; a component with fewer edges, or a pure matching, can first be extended to either of these configurations. Each addition respects the classification above. Once a triangle exists, any other edge of that component must be a pendant edge at a common one of its three vertices. If a base vertex is unused, it can be joined by an edge to that center while preserving the threshold property; therefore a maximal \(F\) uses every vertex of \([n]\).

Conversely, take a triangle with any number of pendant edges incident to one of its vertices and put a matching on all remaining vertices. This is threshold-admissible by the structural characterization. Every absent base edge is either a second chord inside the triangle-plus-spokes component (creating another cycle), an edge from that component to a matching edge (creating a path of length two from the triangle), or an edge joining two matching components (creating a second component with adjacent edges). Each violates the characterization. Thus such an \(F\) is maximal. When at least one pendant spoke is present the triangle center is uniquely determined by its base degree at least three; when no spoke is present, the triangle has three indistinguishable choices of center. This exhausts the maximal subsets.

**3. Labeled enumeration and the exceptional factor.** Choose the triangle in \(\binom n3\) ways and provisionally choose its center in three ways. On the remaining \(m=n-3\) labels, choose \(r\) disjoint pairs to form isolated matching edges and attach the remaining \(m-2r\) labels as pendant spokes. There are exactly \(b_{m,r}\) choices, yielding \(n-r\) selected edges. All objects with a spoke are counted once. The case of no spokes is possible exactly when \(m\) is even; each such object was counted three times rather than once. Subtracting two copies proves the polynomial. Since involutions consist of fixed points and transpositions, \(\sum_r b_{m,r}=I_m\), with the no-fixed-point term \(P_m\). The stated total follows. Coefficient extraction from the exponential formula for involutions, \(e^{zt+zt^2/2}\), and the correction for perfect matchings, \(e^{zt^2/2}\), proves the bivariate generating function.

**4. Support and strict log-concavity.** Every allowed \(r\) has positive coefficient, including the corrected terminal coefficient \(\binom n3 b_{m,R}\) for even \(m\), so the sizes are precisely \(n-R,\ldots,n\). Before terminal correction the successive coefficient ratio in the direction of increasing \(r\) is
\[
\frac{b_{m,r+1}}{b_{m,r}}=
\frac{(m-2r)(m-2r-1)}{2(r+1)}.
\]
These ratios strictly decrease. The only correction reduces the terminal ratio by a factor of three, preserving strict decrease. Therefore the positive coefficients, in either order, are strictly log-concave when \(R\ge2\), i.e. \(n\ge7\).

## Verification
The included standalone `verify.py` enumerates threshold-admissible induced vertex sets via forbidden four-vertex configurations and checks inclusion-maximality against every possible one-vertex extension. Its pruning is exact: the threshold property is hereditary, so an already forbidden subset cannot be made admissible by adding further vertices. Executing the script for \(3\le n\le8\) returned `VERIFY_OK n=3..8 eligible_sets=74533 maximal_sets=5501 formula_equality=true`. The six maximal-set enumerators, in increasing \(n\), have total counts \(1,12,40,240,840,4368\). These finite checks corroborate, but do not prove, the unrestricted identity; the proof above is independent of the computational cutoff.

## Relationship to prior work
Behr, Sivaraman and Zaslavsky's 2016 Proposition 41 already provides a stronger structural characterization of *all* threshold line graphs; it is the essential existing input. The present claim is specifically the labeled inclusion-maximal **cardinality enumerator**, the exponential generating function with its exceptional perfect-matching correction, and strict log-concavity for the triangular graph family. Galvin, Wesley and Zacovic (first public version October 18, 2021) enumerate labeled threshold graphs by other parameters, not the maximal induced threshold subsets of \(L(K_n)\). Cao (first public version April 21, 2020) provides general maximal-induced-subgraph enumeration algorithms, including for threshold graphs, but not these specific coefficient formulas. A general theorem for allowed subgraphs is not claimed here as a new classification. A closely related unpublished enumeration could still exist.

## Limitations
No independent mathematical audit or publication-priority certification is claimed. The exact polynomial concerns triangular graphs only, not arbitrary host graphs or all maximal induced threshold-subgraph problems. The 2016 structural classification substantially reduces the difficulty of the proof; the contribution is enumerative and does not supersede that classification. Brute-force verification stops at \(n=8\), whereas the formula and log-concavity arguments apply to every \(n\ge3\).

## References
1. R. Behr, V. Sivaraman, T. Zaslavsky, *Mock Threshold Graphs*, arXiv:1602.06622, first submitted February 22, 2016, Proposition 41 (threshold line graphs). Open full text: https://people.math.binghamton.edu/zaslav/Tpapers/mtg.pdf.
2. D. Galvin, G. Wesley, B. Zacovic, *Enumerating Threshold Graphs and Some Related Graph Classes*, arXiv:2110.08953, first submitted October 18, 2021. Primary MSC: 05C30. https://arxiv.org/abs/2110.08953.
3. Y. Cao, *Enumerating Maximal Induced Subgraphs*, arXiv:2004.09885, first submitted April 21, 2020; ESA 2023, DOI:10.4230/LIPIcs.ESA.2023.31. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2023.31.
4. V. Chvátal, P. L. Hammer, *Set packing problems and threshold graphs*, University of Waterloo CORR 73-21 (1973); classical forbidden-induced-subgraph threshold characterization.
