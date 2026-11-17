# Minimal forts of the once-subdivided complete graph: cycles, exceptional stars, and gaps

## Finding
For an integer \(n\geq 3\), let \(H_n\) be obtained from \(K_n\) by subdividing every edge exactly once. Call the original vertices \(V\), and denote the subdivision vertex on the original edge \(uv\) by \(e_{uv}\). A **fort** is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is **inclusion-minimal** if it has no proper nonempty fort subset.

**Classification theorem.** The complete collection of inclusion-minimal forts of \(H_n\) consists of precisely these three disjoint classes:

1. For each simple cycle \(C\) in \(K_n\), the set \(\{e_{uv}:uv\in E(C)\}\) of its edge-subdivision vertices.
2. The set \(V\) of all \(n\) original vertices.
3. For each \(v\in V\), the set \((V\setminus\{v\})\cup\{e_{vw}:w\in V\setminus\{v\}\}\).

Thus the full inclusion-minimal-fort cardinality polynomial is
\[
\boxed{\mathcal F_{H_n}(z)=\sum_{k=3}^{n}\frac{n!}{2k(n-k)!}\,z^k+z^n+n z^{2n-2}.}
\]
Coefficients at coinciding exponents are added. In particular, the minimum inclusion-minimal-fort size is \(3\), the largest is \(2n-2\), and the size distribution has no terms of degrees \(n+1,n+2,\ldots,2n-3\), an interval of \(n-3\) consecutive missing sizes (nonempty for \(n\geq4\)). The total number is
\[
1+n+\frac{n!}{2}\sum_{k=3}^{n}\frac{1}{k(n-k)!}
\sim\frac e2(n-1)!\quad(n\to\infty).
\]

## Assumptions and scope
All graphs are finite, simple, and undirected. Each original edge of the **complete** graph \(K_n\) is replaced by two edges through a different degree-two subdivision vertex; the result has \(n+\binom n2\) vertices. The classification does **not** claim to hold for subdivisions of arbitrary graphs or for paths obtained by multiple subdivisions. Inclusion-minimality is understood against **all** proper fort subsets, not merely sets obtained by one-vertex deletion; the fort property is not upward-closed in general.

## Proof
For a fort candidate \(F\subseteq V(H_n)\), write \(X=F\cap V\) and \(Y=\{uv\in E(K_n):e_{uv}\in F\}\). Every unselected subdivision vertex \(e_{uv}\) has exactly the original endpoints \(u,v\) as neighbors. It has precisely one neighbor in \(F\) if and only if \(uv\in\delta(X)\setminus Y\), where \(\delta(X)\) is the edge cut of \(X\) in \(K_n\). An original vertex outside \(X\) has exactly its incident selected subdivision vertices as neighbors. Consequently, \(F\) is a fort if and only if it is nonempty, \(\delta(X)\subseteq Y\), and
\[
\deg_Y(w)\ne1\qquad\text{for every }w\in V\setminus X.\tag{1}
\]
This is an equivalence, with no assumptions about minimality.

**Case \(X=\varnothing\).** Condition (1) says that the graph \((V,Y)\) has no vertices of degree one. Since \(Y\) is nonempty, some connected component contains a cycle. The edge set of any simple cycle gives a fort contained in \(F\). Conversely the edge set of a simple cycle is a fort and no proper nonempty subset of its edges can have all degrees different from one: every proper nonempty subgraph of that cycle has a degree-one vertex. Thus the inclusion-minimal forts with no original vertices are exactly the cycle sets in class 1.

**Case \(|X|=1\).** Write \(X=\{x\}\). The cut condition forces all \(n-1\) edges incident to \(x\) into \(Y\). For \(F\) to be a fort, every other original vertex has at least two incident edges of \(Y\): it already has the selected cut edge \(xw\), so (1) forbids exactly one. Furthermore, \(\deg_Y(x)=n-1\ge2\). Therefore the nonempty set consisting only of the selected subdivision vertices, namely \(\{e_{uv}:uv\in Y\}\), is itself a proper fort subset of \(F\). Hence no fort with exactly one original vertex is inclusion-minimal.

**Case \(|X|=k\ge2\).** The cut condition forces \(\delta(X)\subseteq Y\). Every vertex outside \(X\) is incident to all \(k\) cut edges joining it to \(X\), so its selected-edge degree is at least \(k\ge2\). Thus removing from \(Y\) any edge outside \(\delta(X)\) leaves a fort (the removed subdivision vertex sees either zero or two original vertices of \(X\)). Consequently inclusion-minimality forces \(Y=\delta(X)\).

If \(2\le k\le n-2\), both sides of the complete cut have at least two vertices. The cut contains a simple four-cycle, so its four edge-subdivision vertices form a proper fort subset of \(F\); thus such an \(F\) is not inclusion-minimal.

If \(k=n\), then \(Y=\varnothing\), giving class 2. This set is minimal because any proper nonempty subset of original vertices creates an unselected subdivision vertex with exactly one selected original endpoint.

If \(k=n-1\), write \(V\setminus X=\{v\}\). Then \(Y\) consists of the \(n-1\) edges incident to \(v\), giving class 3. It is a fort: its only unselected original vertex has \(n-1\ge2\) selected subdivision neighbors, and every unselected subdivision vertex has both endpoints in \(X\). To prove minimality, consider a purported proper fort subset. If it selects a nonempty proper subset \(X'\subsetneq X\), some edge between \(X'\) and \(X\setminus X'\) has an unselected subdivision vertex with exactly one selected original endpoint. If it selects all of \(X\), every cut subdivision vertex is forced and the entire set is selected. If it selects no original vertices, its subdivision vertices form a subset of the star at \(v\); any nonempty such subset gives degree one to some original star leaf, so it cannot be a fort. This eliminates every proper fort subset.

These cases exhaust all possibilities and prove the classification. There are \(\binom nk(k-1)!/2=n!/[2k(n-k)!]\) unoriented simple cycles of length \(k\) on labeled \(K_n\), alongside one all-original fort and \(n\) distinct exceptional forts of size \(2n-2\). This proves the polynomial and gap. Finally, after dividing the cycle count by \((n-1)!\), its sum is \(\frac12\sum_{j=0}^{n-3}\frac{n}{n-j}\frac1{j!}\). For fixed \(j\), \(n/(n-j)\to1\), and \(n/(n-j)\le j+1\) throughout the summation, so dominated convergence for series gives limit \(e/2\). The remaining \(n+1\) exceptional forts are asymptotically negligible.

## Verification
An independent finite checker is provided as `verify.py`. It builds \(H_n\) directly from incidence adjacencies, evaluates the fort definition on vertex subsets, and finds all inclusion-minimal forts in increasing cardinality, rejecting supersets of previously found minimal forts. Crucially, it does **not** assume that testing single-vertex deletions suffices. It separately enumerates the three predicted set families and compares their exact masks and polynomial coefficients.

Executing `python3 verify.py` exhaustively for \(n=3,4,5,6\) examines \(2,131,004\) nonempty vertex subsets and finds \(264\) inclusion-minimal forts. The four polynomials agree coefficientwise, including all three structural families. These finite computations are corroboration; the proof above covers every integer \(n\ge3\).

## Relationship to prior work
Becker, Cameron, Hanely, Ong, and Previte (2024) explicitly study inclusion-minimal forts and count them for several families including paths, cycles, spiders, and constructions based on graph products; the opened full-text material and its family classification do not state the complete subdivision-of-clique classification above. Cameron, Hogben, Kenter, Mojallal, and Schuerger (2023) introduce and use the minimal-fort hypergraph in fractional zero forcing and products. Barrett, Butler, Catral, Fallat, Hall, Hogben, and Young (2014) prove a general exact **zero forcing number** formula for all complete edge subdivisions, which applies to \(H_n\). That scalar theorem is acknowledged and not claimed as new; it does not give the list, size polynomial, or cardinality gaps for inclusion-minimal forts.

## Limitations
Publication priority is provisional because no literature search can exclude every unindexed result. The conclusion concerns the particular once-subdivided complete graphs and ordinary (not positive-semidefinite or skew) zero forcing forts. It does not classify fort hypergraphs for all subdivisions, enumerate all nonminimal forts, or independently verify an infinite family by computation. No independent mathematical audit has been performed.

## References
1. P. Becker, T. R. Cameron, D. Hanely, B. Ong, and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1 (first submitted 2024-04-09). https://arxiv.org/html/2404.05963v1
2. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, and H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (first submitted 2023-10-27). https://arxiv.org/abs/2310.17904
3. W. Barrett, S. Butler, M. Catral, S. M. Fallat, H. T. Hall, L. Hogben, and M. Young, *The maximum nullity of a complete subdivision graph is equal to its zero forcing number*, Electron. J. Linear Algebra 27 (2014), 444–457. https://doi.org/10.13001/1081-3810.1629
