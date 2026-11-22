# Parity and optimum-set rigidity for strong edge geodetic covers of crown graphs

## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M_n\), where the removed perfect matching consists of the pairs \(a_i b_i\) for \(1\le i\le n\). For all integers \(n\ge5\), the strong edge geodetic number and the **complete family of minimum vertex sets** satisfy
\[
\operatorname{sg}_e(\operatorname{Cr}_n)=\begin{cases}n,&n\text{ odd},\\n+1,&n\text{ even},\end{cases}
\qquad
\#\{S:|S|=\operatorname{sg}_e(\operatorname{Cr}_n)\}=\begin{cases}2,&n\text{ odd},\\2n,&n\text{ even}.\end{cases}
\]
For odd \(n\), the only minimum sets are the two entire bipartition shores. For even \(n\ge6\), the only minimum sets are an entire shore together with one arbitrarily chosen vertex from the opposite shore. Thus deletion of the perfect matching reduces the known strong edge geodetic minimum of \(K_{n,n}\) by two when \(n\) is odd, but leaves it unchanged for even \(n\).

## Assumptions and scope
The graph is simple and undirected, its vertices are \(\{a_1,\ldots,a_n,b_1,\ldots,b_n\}\), and its edges are \(a_i b_j\) for \(i\ne j\). A set \(S\) is **strong edge geodetic** when at most one shortest path may be selected for each unordered pair of distinct vertices of \(S\), and the union of selected paths covers all edges. The result is for integers \(n\ge5\). It does not assert the formula at orders three and four; direct finite checks give respectively \(14\) minimum sets of size \(3\) and \(32\) minimum sets of size \(5\).

## Proof
Write \(a=|S\cap A|\), \(b=|S\cap B|\), \(k=a+b\), and let \(c\) be the number of matched index pairs with both endpoints in \(S\). Every shortest path has length at most three: between distinct vertices on the same shore, paths have length two; between \(a_i\) and \(b_j\) with \(i\ne j\), the unique path has length one; between \(a_i\) and \(b_i\), paths have length three. Thus the total number of *distinct edges* coverable by the chosen paths is bounded above by the sum of their lengths:
\[
U(a,b,c)=2\binom a2+2\binom b2+(ab-c)+3c=k(k-1)-ab+2c.
\]
There are \(n(n-1)\) edges. Since \(2c\le k\), for \(k\le n-1\) we have \(U\le k^2\le(n-1)^2<n(n-1)\); thus \(|S|\ge n\). When \(k=n\) and both \(a,b>0\), the larger shore size is at least three (as \(n\ge5\)), so \(ab\ge3\min(a,b)>2c\), implying \(U<n(n-1)\). Therefore a size-\(n\) solution, if one exists, is necessarily a complete shore.

A complete shore \(A\) can cover the incident edges of every omitted vertex \(b_t\) only by geodesics \(a_i-b_t-a_j\), each covering two of the \(n-1\) incident edges. These geodesics correspond to pairs in \(A\setminus\{a_t\}\). When \(n\) is even, at least \(n/2\) different shore pairs are required for each \(b_t\). Across all \(n\) omitted vertices this requires \(n^2/2>\binom n2\) pairs, an impossibility.

When \(n\) is odd, a near-one-factorization of the complete graph on the \(n\) indices partitions its edge set into \(n\) matchings, one indexed by each \(t\), each matching covering every index other than \(t\). For every matching pair \(\{i,j\}\) in class \(t\), assign the unique geodesic \(a_i-b_t-a_j\). All required edges are covered and each selected pair receives exactly one path. This constructs the two complete-shore solutions for odd \(n\).

It remains to consider even \(n\ge6\). A size-\(n+1\) set containing \(a\ge2\) vertices of \(A\) and \(b\ge2\) vertices of \(B\) cannot work. Indeed, \(a+b=n+1\) and the shared-index count \(c\ge1\), so there are exactly \(c-1\) indices with neither endpoint selected. The number of graph edges whose *two endpoints* are omitted is therefore
\[
(b-1)(a-1)-(c-1).
\]
An edge with both endpoints omitted can belong to a geodesic between selected vertices only when that geodesic has length three, joining a selected matched pair \(a_t,b_t\). Each such selected matched pair is assigned at most one geodesic, and that geodesic contains at most one edge with both endpoints omitted (its middle edge). Hence
\[
(a-1)(b-1)+1\le2c\le2\min(a,b).
\]
This is impossible for \(a+b=n+1\ge7\) and \(a,b\ge2\): putting \(2\le a\le b\), for \(a=2\) the left side equals \(b\ge5>4\), and for \(a\ge3\) it is at least \(3(a-1)+1>2a\). Consequently any size-\(n+1\) solution consists of one entire shore and exactly one vertex from the other shore.

Such solutions really exist. Select all of \(A\) and only \(b_0\) on \(B\), relabeling the indices as \(\{0,\ldots,n-1\}\). Put \(U=\{1,\ldots,n-1\}\), an odd set. Near-one-factorize \(K_U\): for each \(t\in U\), let \(M_t\) be the matching of size \((n-2)/2\) that covers \(U\setminus\{t\}\), with the classes \(M_t\) partitioning every edge of \(K_U\). Fix a derangement \(\sigma:U\to U\), for instance a cyclic shift. For each pair \(\{i,j\}\in M_t\), assign \(a_i-b_t-a_j\); for each \(t\in U\), assign \(a_0-b_t-a_{\sigma(t)}\) to the unique pair \(\{a_0,a_{\sigma(t)}\}\). These use mutually distinct selected endpoint pairs because the \(M_t\)'s partition the pairs in \(U\) and \(\sigma\) is bijective. Their paths together cover all \(n-1\) edges at every \(b_t\) with \(t\in U\). The remaining graph edges, namely those incident to \(b_0\), are covered by their selected-endpoint length-one paths. Interchanging the shores gives the other constructions. The count is therefore \(2n\) for even \(n\) and \(2\) for odd \(n\), completing the proof.

## Verification
The included standalone `crown_exact_check.py` enumerates all vertex subsets of the labeled crown graphs for \(3\le n\le7\) (up to \(2^{14}=16{,}384\) subsets). For each candidate set it generates every shortest path using graph distances, then solves the at-most-one-path-per-endpoint-pair edge-coverage constraint by exact backtracking. Its minimum-size and minimum-count pairs are \((3,14),(5,32),(5,2),(7,12),(7,2)\) for the successive orders. A separate mixed-integer path-incidence feasibility program corroborated both the successful and failed complete-shore cases for orders four through seven. These checks are finite and do not replace the preceding infinite-family proof.

## Relationship to prior work
Klavžar and Zmazek (arXiv:2312.11199; published 2024) established the strong edge geodetic minimum of complete bipartite graphs: \(n+2\) for \(K_{n,n}\) at odd \(n\) and \(n+1\) at even \(n\), together with related complete multipartite and clique–path product results. Their objects retain the perfect matching and do not imply the present parity-sensitive rigidity in the crown graph obtained by deleting it. The 2020 study of Xavier et al. treats Cartesian products of complete graphs and other products, not crown-graph strong edge coverings. Earlier ordinary edge-geodetic results allowing **all** geodesics for a fixed terminal pair are weaker and do not impose the present one-path-per-pair constraint. These comparisons support but do not certify historical priority.

## Limitations
The formula and rigidity statement are restricted to \(n\ge5\); exceptions at orders three and four are not classified theoretically here. There is no claim for arbitrary matching deletions, rectangular bipartite graphs, or minimum edge-geodetic sets under a different path-assignment convention. Independent mathematical review and exhaustive historical-priority clearance have not been performed.

## References
1. S. Klavžar and E. Zmazek, *Strong Edge Geodetic Problem on Complete Multipartite Graphs and Some Extremal Graphs for the Problem*, arXiv:2312.11199 (first version 18 December 2023), later *Bull. Iranian Math. Soc.* 50:13 (2024), DOI: 10.1007/s41980-023-00849-6.
2. D. A. Xavier, D. Mathew, S. Theresal, and E. S. Varghese, *Some Results on Strong Edge Geodetic Problem in Graphs*, *Communications in Mathematics and Applications* 11 (2020), 403–413, DOI: 10.26713/cma.v11i3.1385.
3. *The Edge Geodetic Number of Crown Graphs and Related Graphs*, *International Journal of Applied Engineering Research* 14 (2019), 1744–1749, https://www.ripublication.com/ijaer19/ijaerv14n7_47.pdf (comparison of weaker edge-geodetic convention only).
