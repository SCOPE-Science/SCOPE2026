# Kneser strong-resolving geometry and a cubical exchange exception for subdivided complete graphs

## Finding

For each integer \(n\ge4\), let \(S(K_n)\) be obtained by subdividing **every** edge of the labeled complete graph \(K_n\) exactly once. Write \(m=\binom n2\). A vertex set is *strongly resolving* if, for any two different graph vertices, at least one selected vertex lies on a shortest path through one of the two, with the other as an endpoint. Its *strong metric dimension* is the smallest size of such a set.

The strong resolving graph, on the \(n+m\) graph vertices, is exactly the Kneser graph \(KG(n,2)\) on the \(m\) subdivision vertices, with the \(n\) original vertices isolated. Thus the full enumerator \(F_n(x)=\sum_{R\text{ strongly resolving}}x^{|R|}\) has the closed form
\[
 F_n(x)=(1+x)^n x^m I_n(x^{-1}),\qquad
 I_n(z)=1+mz+n\binom{n-1}{2}z^2+\binom n3z^3+\sum_{k=3}^{n-1} n\binom{n-1}{k}z^k.
\]
All inclusion-minimal strong resolving sets are the complements, among subdivision vertices, of (a) the \(n\) full stars of edges incident to a vertex of \(K_n\) or (b) the \(\binom n3\) three-edge triangles of \(K_n\). Hence
\[
 \operatorname{sdim}(S(K_n))=\binom n2-n+1=\binom{n-1}{2}.
\]
There are \(8\) minimum strong resolving sets when \(n=4\), and precisely \(n\) when \(n\ge5\). For \(n\ge5\), the other inclusion-minimal sets, corresponding to triangles, have size \(\binom n2-3\), strictly larger than the minimum.

Define the budget-\(r\) **minimum-basis exchange graph** by joining two minimum bases if they differ by replacing at most \(r\) selected vertices simultaneously, with no requirement on uncompleted intermediate replacements. When \(n=4\), the budget-one graph is the \(3\)-cube \(Q_3\), of diameter three. For every \(n\ge5\), all the minimum bases are isolated for \(r<n-2\), and at the sharp threshold \(r=n-2\) they form \(K_n\), of diameter one.

## Assumptions and scope

The input is the simple unweighted graph with original vertices \(u_i\), indexed by \(i\in[n]\), and subdivision vertices \(w_{ij}=w_{ji}\) for \(1\le i<j\le n\), with precisely the edges \(u_iw_{ij}\) and \(u_jw_{ij}\). All distances are ordinary shortest-path lengths; the strong resolving graph here is defined on **all** input vertices, including its isolated vertices. An inclusion-minimal set need not have minimum cardinality. In the exchange graph, distinct minimum strong resolving sets are unlabeled vertex subsets of this fixed graph; the batch budget counts vertices removed and therefore also vertices added.

## Proof

**1. Mutual maximal distances.** The original-to-original distances are two. An original vertex \(u_i\) and a nonincident subdivision vertex \(w_{jk}\) have distance three, while incident original/subdivision vertices have distance one. Subdivision vertices \(w_{ij}\) and \(w_{kl}\) are distance two if their index edges intersect and distance four if they are disjoint. For \(n\ge4\), every original vertex has a neighbor *farther* from any distinct vertex with which it might form a mutual-maximal-distance pair: for \(u_i,u_j\) choose a subdivision neighbor \(w_{ik}\) with \(k\ne j\); for \(u_i,w_{jk}\) with \(i\notin\{j,k\}\), choose \(w_{i\ell}\) with \(\ell\notin\{j,k\}\) (possible because \(n\ge4\)); for incident pairs choose a distinct neighbor from the other endpoint when needed. Similarly, for two subdivision vertices whose index edges meet, one nonshared endpoint of the first subdivision vertex is distance three from the second, exceeding their mutual distance two. By contrast any two disjoint-index subdivision vertices are at graph diameter four, so they are mutually maximally distant. These are exactly the Kneser edges, and no other mutual-maximal-distance pairs exist.

**2. Strong resolving sets and all-set enumeration.** The classical strong-resolving-graph theorem identifies strong resolving sets with vertex covers of that graph. The complement inside the subdivision-vertex ground set is therefore an independent set of \(KG(n,2)\), namely a pairwise-intersecting family of edges of \(K_n\). Any such family of at least two edges has a common incident vertex unless exactly three edges form a triangle: if \(ab\) and \(ac\) lie in the family and some other edge avoids \(a\), it must be \(bc\), after which every family edge must be one of \(ab,ac,bc\). Thus every intersecting family is an edge-star subfamily or a complete triangle.

The empty family contributes one, the single edges contribute \(m\), the pairs have a unique center and contribute \(n\binom{n-1}2\); for \(k\ge3\), a size-\(k\) star has a unique center and contributes \(n\binom{n-1}k\), with an additional \(\binom n3\) whole triangles at \(k=3\). This gives \(I_n(z)\). The original vertices impose no cover constraints and may be independently selected, giving the factor \((1+x)^n\). The maximum independent-family size is \(n-1\); at \(n=4\), triangles also attain three, while for \(n\ge5\) only the full stars attain \(n-1\). The full stars and triangles are exactly the maximal intersecting families, proving both inclusion-minimal classification and dimension.

**3. Sharp exchange threshold.** Every minimum base excludes all original vertices. For \(n\ge5\), two distinct star complements omit the \(n-1\) incident edges at different original vertices. Distinct stars share exactly one edge and therefore the corresponding bases differ by precisely \(n-2\) removals and \(n-2\) additions. Below this batch budget no move is possible; at the threshold every pair is adjacent, giving \(K_n\). For \(n=4\), four star complements and four triangle complements exist. A star and a triangle have two omitted subdivision vertices in common exactly when the center of the star is a vertex of the triangle. This occurs for the 12 pairs with distinct indexing vertex and omitted triangle vertex, yielding \(K_{4,4}\) minus one perfect matching, isomorphic to \(Q_3\). It is connected of diameter three under one-for-one exchanges.

## Verification

`verify_subdivision_mmd.py` directly computes every shortest-path distance, tests mutual maximal distance against all neighbors, and independently enumerates all pairwise-intersecting edge-subsets for \(n=4,5,6\). It verifies the complete independent-family coefficient sequences, minimum-basis numbers, exact sharp batch thresholds, and exchange diameters.

`verify_subdivision_resolving.py` uses the original geodesic equality defining strong resolution, without using a strong-resolving-graph reduction. For every vertex subset of \(S(K_4)\) and \(S(K_5)\) it checks all graph-vertex pairs and independently reconstructs the exact strong-resolving polynomial, minimum sizes and single-exchange edges. Reproduce with `python3 verify_subdivision_mmd.py` and `python3 verify_subdivision_resolving.py`; their reference output files are embedded. These finite calculations cross-check the formulas but do not replace the universal proof.

## Relationship to prior work

The strong-resolving-graph/vertex-cover correspondence is due to Oellermann and Peters-Fransen (2007); it is a required known ingredient and is not claimed as new. The star/triangle structure of pairwise-intersecting edges is classical. Wagner–Schmitz–Wanke give a general strong-metric decomposition by biconnected components, while the earlier strong-metric literature studies Cartesian/direct products and cactus graphs. The present result combines the exact Kneser identification for the **full subdivision of a complete graph** with the complete strong-resolving-set enumerator, all inclusion-minimal-set sizes and the exceptional cubical basis-exchange transition. The comparison was not an exhaustive proof of publication priority.

## Limitations

Only the once-subdivided complete graph, for \(n\ge4\), is covered. No assertion is made about partial subdivisions, arbitrary subdivision lengths, or larger Kneser ranks. The geometric/identification reduction is elementary; the result's scope is the complete classification and sharp minimum-basis exchange behavior, not a claim of new general strong-metric theory. Equivalent previously published results under other terminology or derived from independent-set tables remain possible. The original 2007 publisher paper and some otherwise relevant references were not available as fully inspected texts; they are not declared non-covering on snippets alone. Independent external audit has not been performed.

## References

1. O. R. Oellermann and J. Peters-Fransen, *The strong metric dimension of graphs and digraphs*, Discrete Applied Mathematics **155** (2007), 356–364, doi:10.1016/j.dam.2006.06.009.
2. J. A. Rodríguez-Velázquez, I. G. Yero, D. Kuziak and O. R. Oellermann, *On the strong metric dimension of Cartesian and direct products of graphs*, arXiv:1307.4722v1 (2013).
3. M. Wagner, Y. Schmitz and E. Wanke, *On the strong metric dimension of composed graphs*, arXiv:2212.04166v1 (2022).
4. D. Kuziak, *The Strong Resolving Graph and the Strong Metric Dimension of Cactus Graphs*, Mathematics **8** (2020), 1266.
