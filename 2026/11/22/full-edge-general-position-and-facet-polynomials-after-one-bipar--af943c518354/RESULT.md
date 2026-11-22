# Full edge-general-position and facet polynomials after one bipartite edge deletion

## Finding

Let \(m,n\ge3\) be integers and let \(G_{m,n}=K_{m,n}-e\) be a complete bipartite graph with exactly one edge deleted. Let \(\mathcal P_{m,n}(z)\) count edge-general-position edge sets by cardinality and let \(\mathcal F_{m,n}(z)\) count **inclusion-maximal** edge-general-position sets (facets) by cardinality. Put \(r=m-1\) and \(s=n-1\). Then
\[
\mathcal P_{m,n}(z)=\sum_{a=0}^{s}\sum_{b=0}^{r}\binom{s}{a}\binom{r}{b}z^{a+b}(1+z)^{rs-ab},
\]
\[
\mathcal F_{m,n}(z)=z^{rs+s}+z^{rs+r}+\sum_{a=1}^{s}\sum_{b=1}^{r}\binom{s}{a}\binom{r}{b}z^{rs+a+b-ab}.
\]
Thus there are exactly \(2+(2^r-1)(2^s-1)\) inclusion-maximal sets and
\[
\operatorname{gp}_{\mathrm e}(G_{m,n})=rs+\max(r,s).
\]
There is exactly one maximum set if \(r\ne s\), and exactly two if \(r=s\).

The deletion is a sharp structural perturbation: in the undeleted \(K_{m,n}\), every edge subset is edge-general-position, and the only facet is its full edge set. Deleting one edge lowers the optimum by precisely \(\min(m,n)\) and creates exponentially many inclusion-maximal edge sets. For the balanced family \(m=n=k+1\) and \(k\ge3\), the sizes \(k^2+2,k^2+3,\ldots,k^2+k-1\) are **all absent from the facet spectrum** although facets of sizes \(k^2+1\) and \(k^2+k\) exist. The gap has length \(k-2\).

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted. An edge set \(X\subseteq E(G)\) is in *edge general position* if no shortest path in \(G\) contains three edges from \(X\). A facet is an inclusion-maximal such edge set, not necessarily one of greatest size. The polynomial \(\mathcal P\) includes the empty set, while \(\mathcal F\) counts each vertex-labelled edge subset once. The two shore sizes satisfy \(m,n\ge3\); neither graph edges nor vertices are assigned labels beyond their distinct identities for counting.

Write the left shore as \(\{u_0,u_1,\ldots,u_r\}\), the right shore as \(\{v_0,v_1,\ldots,v_s\}\), and delete only \(u_0v_0\).

## Proof

**Geodesic lemma.** Every pair of adjacent vertices is at distance one, every pair in the same shore has distance two, and the single missing cross-shore pair \((u_0,v_0)\) is at distance three. The assumptions \(m,n\ge3\) guarantee the needed common neighbors. Thus the only geodesics with at least three edges, and specifically every length-three geodesic, are
\[
u_0-v_j-u_i-v_0\qquad(1\le i\le r,\ 1\le j\le s).
\]
Their three edges are \(u_0v_j\), \(u_iv_j\), and \(u_iv_0\). No longer geodesic exists. Consequently a selected edge subset is legal precisely if it never selects all three edges in any of these indexed triples.

**All-set polynomial.** Let \(A\subseteq[s]\) index the selected star edges \(u_0v_j\) and let \(B\subseteq[r]\) index the selected star edges \(u_iv_0\). Put \(a=|A|\), \(b=|B|\). Every interior edge \(u_iv_j\), with \(i\in B\), \(j\in A\), is forbidden; the other \(rs-ab\) interior edges can be selected independently. For fixed \(A,B\), these choices contribute \(z^{a+b}(1+z)^{rs-ab}\). Choosing \(A\) and \(B\) and summing proves the first polynomial with no double count.

**Facet classification.** An inclusion-maximal legal set must select *every* interior edge whose endpoints do not lie in the Cartesian product \(B\times A\), because adding any such allowed edge cannot create a forbidden triple. If \(A=B=\varnothing\), some star edge can be added and the set is not maximal. If \(B=\varnothing\) and \(A\ne\varnothing\), maximality requires \(A=[s]\): otherwise adding a missing \(u_0v_j\) is legal. The resulting selected set consists of all \(rs\) interior edges plus the \(s\) left-star edges; it is maximal because adding any right-star edge would complete a forbidden geodesic triple. The symmetric case \(A=\varnothing\), \(B=[r]\) supplies the second exceptional facet.

Finally, if \(A,B\ne\varnothing\), selecting every allowed interior edge yields a maximal set: adding a missing interior edge is forbidden by one of the selected star pairs; adding a new left-star edge would conflict with an already selected interior edge incident to any member of \(B\), and analogously for a new right-star edge. Conversely, these are all the possible facets. Their size is
\[
a+b+(rs-ab)=rs+a+b-ab.
\]
Counting all nonempty \(A,B\) gives the second polynomial and the total \(2+(2^r-1)(2^s-1)\).

**Extrema and spectrum.** For \(a,b\ge1\),
\[
a+b-ab=1-(a-1)(b-1)\le1.
\]
Since \(r,s\ge2\), the only facets with maximum cardinality are the two exceptional all-interior-plus-one-whole-star cases, of sizes \(rs+r\) and \(rs+s\). This establishes the maximum and its multiplicity. The complete graph \(K_{m,n}\) has diameter two and its full edge set has size \(mn=rs+r+s+1\); subtraction gives the sharp loss \(\min(r,s)+1=\min(m,n)\).

For \(r=s=k\ge3\), nonexceptional facets have size at most \(k^2+1\); the exceptional facets both have size \(k^2+k\). Moreover the former bound occurs whenever \(a=1\) or \(b=1\), and the latter obviously occurs, so **precisely the indicated interval** of cardinalities between them is missing. The interval contains \(k-2\) integers. This completes the proof.

## Verification

A standalone C++17 verifier constructs \(K_{m,n}-e\), computes graph distances from the adjacency matrix by Floyd–Warshall, enumerates all length-three geodesics, and tests every edge subset for legal membership and inclusion maximality. It independently computes all polynomial coefficients from the stated expressions and checks exact agreement for \((m,n)=(3,3),(3,4),(4,4),(4,5),(5,5)\). The largest direct case checks \(2^{24}=16,777,216\) subsets. It reports `DIRECT_CERTIFICATE_OK` after all tests.

A separate Python 3 integer-binomial calculator computes both polynomials for those five cases and additionally \((m,n)=(6,8)\). The independent direct and symbolic methods respectively give \(11,23,51,107,227\) facets in the five exhaustively checked cases. For the \((5,5)\) instance, the direct enumeration finds \(3,839,105\) legal sets and \(227\) facets. Both programs are included as standalone files, with no external libraries beyond the Python standard library and the C++17 standard library.

## Relationship to prior work

Manuel, Prabha and Klavžar introduced edge general position and computed it for several graph families (first public version 2021-05-10). Tian, Klavžar and Tan established extremal edge-general-position results in other graph regimes (first public version 2023-02-03). The 2022 generalization concerns related \(k\)-edge conditions. The inspected papers do not present the all-set or facet polynomials for one-edge-deleted complete bipartite graphs.

A closely related previously available crown-graph theorem determines the scalar edge general position number for \(K_{n,n}\) with a **whole perfect matching** deleted, via avoidance of transitive directed triangles. It treats a different deletion pattern, has many distance-three pairs, and explicitly does not classify maxima or arbitrary partial matching deletion. Neither its statement nor its proof supplies the present formulas for deletion of just one edge. Other comparisons include edge-general-position facet enumerators for clique graphs with pendant leaves (different objects) and vertex general-position polynomials (different definition).

## Limitations

The formulas assume exactly one deleted edge, with both original part sizes at least three. The theorem does not determine the polynomials after two or more deleted matching edges. Independent mathematical validation and exhaustive historical-priority clearance are not claimed; related publications could contain unindexed equivalent enumerations. The exhaustive finite tests corroborate but are not used as a proof of the infinite-family formulas.

## References

1. P. Manuel, R. Prabha, S. Klavžar, *Edge general position problem*, arXiv:2105.04292v1, 2021-05-10, https://arxiv.org/abs/2105.04292.
2. J. Tian, S. Klavžar, E. Tan, *Extremal Edge General Position Sets in Some Graphs*, arXiv:2302.01587v1, 2023-02-03, https://arxiv.org/abs/2302.01587.
3. P. Manuel, R. Prabha, S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357v1, 2022-07-15, https://arxiv.org/abs/2207.07357.
4. *Edge general position number of crown graphs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-edge-general-position-number-of-crown-graphs--964bdcf6d755.
