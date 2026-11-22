# Sharp consecutive-star decomposition thresholds for complete bipartite graphs at sizes four and five

## Finding

For \(k\in\{4,5\}\), define \(c_k^{\mathrm{bip}}\) as the least integer \(c\) for which **every** complete bipartite graph \(K_{a,b}\) with \(a,b\ge1\) and \(a+b\ge c\) has an edge partition into stars isomorphic to \(K_{1,k}\) or \(K_{1,k+1}\). Then
\[
 c_4^{\mathrm{bip}}=15,\qquad c_5^{\mathrm{bip}}=24.
\]
For every \(k\ge2\), the analogous threshold, if finite, is at least \(k^2-1\). Thus the two claimed thresholds meet the universal bipartite obstruction exactly. These statements allow using only one of the two permitted star sizes; no positivity condition on both star counts is imposed.

## Assumptions and scope

Graphs are finite, simple and undirected. In \(K_{a,b}\), the two parts have respectively \(a,b\) vertices, and \(a,b\) are arbitrary positive integers. A decomposition is a partition of *all* edges, with each part a copy of one of the permitted stars. The adjacent-degree sum of \(K_{a,b}\) is \(a+b\). The result is restricted to two partite classes and \(k\in\{4,5\}\); it does not imply any threshold for general or three-part complete multipartite graphs.

## Proof

**Orientation equivalence.** Put \(S_k=\{ki+(k+1)j:i,j\in\mathbb Z_{\ge0}\}\). A partition into the specified stars induces an orientation: orient each edge away from the centre of its star. Every outdegree then belongs to \(S_k\). Conversely, if an orientation has all outdegrees in \(S_k\), write the outgoing degree at each vertex as a sum of \(k\)'s and \(k+1\)'s, and partition its outgoing edges into groups of these sizes. Every edge belongs to precisely one group, proving the equivalence without any additional constraint on the leaves.

**Semigroup conductor.** If \(t\ge k(k-1)\), express \(t=kq+r\) with \(0\le r<k\) and \(q\ge k-1\ge r\). Then \(t=(q-r)k+r(k+1)\in S_k\). Conversely \(k(k-1)-1\notin S_k\): any putative representation forces \(j\equiv k-1\pmod k\), hence \(j\ge k-1\) and \((k+1)j\ge k^2-1>k(k-1)-1\). It follows that the conductor is exactly \(k(k-1)\).

**Sharp obstruction.** Consider \(K_{k-1,k(k-1)-1}\), whose adjacent-degree sum is \(k^2-2\). Every vertex in the larger part has degree \(k-1<k\), and hence cannot be the centre of any allowed star. Every edge must therefore be centred in the smaller part, where the degree is \(k(k-1)-1\notin S_k\). No decomposition exists; consequently \(c_k^{\mathrm{bip}}\ge k^2-1\) whenever the threshold exists.

**The exhaustive exceptional reduction.** Let \(k\in\{4,5\}\), suppose \(a+b\ge k^2-1\), and assume \(a\le b\). If either \(a\in S_k\) or \(b\in S_k\), centre every star on the opposite shore: orient all edges away from vertices of degree equal to that representable shore size. This gives a decomposition immediately. Otherwise both \(a\) and \(b\) lie among the finite positive gaps below the conductor. Exactly these gaps occur:
\[
 H_4=\{1,2,3,6,7,11\},\qquad
 H_5=\{1,2,3,4,7,8,9,13,14,19\}.
\]
Filtering the ordered pairs \(a\le b\) in \(H_k^2\) by \(a+b\ge k^2-1\) leaves exactly:
\[
 \begin{aligned}
 k=4:&\quad (6,11),(7,11),(11,11);\\
 k=5:&\quad (7,19),(8,19),(9,19),(13,13),(13,14),\\
     &\quad (13,19),(14,14),(14,19),(19,19).
 \end{aligned}
\]
The gap lists follow by enumerating nonnegative \(ki+(k+1)j\) below \(k(k-1)\); the finite pair comparison is arithmetically explicit and independently checked in the accompanying verifier.

**Exact finite certificates and lifting.** For each of these twelve graphs an orientation is supplied by the complete integer row-mask list in `certificates.json`. Index the \(a\) left vertices by \(i\in\{0,\dots,a-1\}\) and the \(b\) right vertices by \(j\in\{0,\dots,b-1\}\). A set bit \(j\) of row mask \(m_i\) means that the edge between \(i\) and \(j\) points from right to left; a clear bit means it points from left to right. Therefore the outdegrees are
\[
 d^+_L(i)=b-\operatorname{popcount}(m_i),\qquad
 d^+_R(j)=\sum_{i=0}^{a-1}\bigl((m_i\mathbin{\mathrm{div}}2^j)\bmod2\bigr).
\]
The independent, dependency-free `verify.py` parses the supplied row masks, checks these equalities and membership of **every** outdegree in \(S_k\), and recomputes the full exceptional-pair coverage. This is an exhaustive finite certificate for the last step, not an extrapolation from sample graphs. By orientation equivalence all twelve graphs decompose. Thus the adjacent-degree-sum condition \(a+b\ge k^2-1\) suffices for \(k=4,5\); combined with the sharp obstruction this gives exactly \(15\) and \(24\).

## Verification

Run `python3 verify.py` in the directory containing the supplied `certificates.json`. The program uses only the Python standard library. It checks the twelve orientations vertex by vertex, the gap lists and exceptional-pair coverage, the conductor's finite nonrepresentation boundary, and the two obstruction values. Expected output: `SEMIGROUP_AND_EXCEPTION_COVERAGE_PASS`, `TWELVE_EXPLICIT_ORIENTATIONS_PASS`, `SHARP_OBSTRUCTIONS_PASS`, `VERIFY_OK`. The unrestricted case reduction and the orientation equivalence are proved in the text; computation supplies only the explicitly bounded twelve-case certificate.

## Relationship to prior work

Hemalatha and collaborators (online May 8, 2026) study decomposing bicliques into trees on five vertices, including four-edge stars alongside paths and branched trees. Their decomposition problem does not impose exactly the consecutive star sizes \(k\) and \(k+1\), so neither threshold follows from that theorem. Hung-Chih Lee and Yen-Po Chu (2013) study equal-edge-size path/star multidecompositions of balanced bicliques, again with different allowed pieces.

Juho Lee's arXiv preprint dated November 17, 2026 studies **the identical consecutive-star decomposition problem** for wider graph classes; its orientation equivalence and nondecomposable examples are directly relevant. Its complete-multipartite lower bound \(k^2\) uses a tripartite graph, and the published sufficiency result is for \(k=3\) only. The paper reports \(K_{11,3}\) and \(K_{19,4}\) as nondecomposable bicliques, consistent with the sharp obstructions above, but does not state or prove the all-biclique sufficiency at \(15\) and \(24\). Thus the new content is these two **biclique-only** sharp thresholds together with their explicit finite orientation certificates, not the general orientation equivalence or the obstruction examples.

## Limitations

The result proves no all-graph or general complete-multipartite threshold. The finite certificates are fully specified and checkable, but their provenance is computational; the accompanying proof reduces all infinite instances to these finitely many cases. Older literature not discoverable through the examined mathematical search indexes may contain equivalent biclique classifications, so historical priority is not independently certified. Independent external mathematical validation has not been performed.

## References

1. P. Hemalatha and A. Chaadhanaa, *Decomposition of graphs into trees of order five*, Journal of Combinatorial Mathematics and Combinatorial Computing 130, published online May 8, 2026, https://doi.org/10.61091/jcmcc130-20 ; https://combinatorialpress.com/jcmcc-articles/volume-130/decomposition-of-graphs-into-trees-of-order-five/ .
2. H.-C. Lee and Y.-P. Chu, *Multidecompositions of the Balanced Complete Bipartite Graph into Paths and Stars*, 2013, https://doi.org/10.1155/2013/398473 .
3. J. Lee, *Decomposition of Graphs into Stars*, arXiv:2611.24973v1, first public November 17, 2026, https://arxiv.org/html/2611.24973v1 .
