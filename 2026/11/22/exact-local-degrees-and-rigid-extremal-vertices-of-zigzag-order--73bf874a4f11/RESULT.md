# Exact local degrees and rigid extremal vertices of zigzag order polytopes

## Finding
For every integer \(n\ge3\), let \(Z_n\) be the zigzag poset \(a_1<a_2>a_3<a_4>\cdots\), and let \(Q_n\) be its order polytope, with coordinates the indicators of order ideals. Flip all odd-indexed coordinates, so that a vertex of \(Q_n\) becomes the binary indicator \(w\) of an independent set of the path on \(n\) vertices.

Partition the positions of the ones of \(w\) into maximal clusters of consecutive ones separated by precisely one zero; distinct clusters are separated by at least two zeros. For cluster \(i\), let \(k_i\) be its number of ones, and let \(a_i,b_i\in\{0,1\}\) indicate whether it has a preceding/following zero within the word. Then the exact vertex degree in the one-skeleton is
\[
\deg_{Q_n}(w)=n+\sum_i\binom{k_i+a_i+b_i-1}{2}.
\]
The empty word has degree \(n\) (empty sum).

In every dimension \(n\ge3\), **exactly four vertices are simple**: the words with one-sets \(\varnothing,\{1\},\{n\},\{1,n\}\). The exact maximum graph degree is
\[
\Delta(Q_n)=n+\binom{\lceil n/2\rceil}{2}.
\]
If \(n\) is odd, exactly one word maximizes it: ones at \(2,4,\ldots,n-1\). If \(n\) is even, exactly four words maximize it: ones at all odd positions, ones at all even positions, ones at odd positions \(3,5,\ldots,n-1\), or ones at even positions \(2,4,\ldots,n-2\). The maximum grows quadratically while the fraction of simple vertices is \(4/F_{n+2}\), which tends to zero exponentially (\(F_1=F_2=1\)).

## Assumptions and scope
The poset has cover relations \(a_{2j-1}<a_{2j}\) and \(a_{2j+1}<a_{2j}\) whenever indices exist; no others except transitivity. The order polytope here is \(\operatorname{conv}\{\mathbf1_I:I\text{ an order ideal of }Z_n\}\), so that \(x_{2j-1}\ge x_{2j}\) and \(x_{2j+1}\ge x_{2j}\). Set \(y_{2j-1}=1-x_{2j-1}\) and \(y_{2j}=x_{2j}\). This is a Euclidean isometry sending \(Q_n\) to the stable-set polytope \(\{y\in\mathbb R_{\ge0}^n:y_i+y_{i+1}\le1\}\) of the path \(P_n\). Here vertex degree means the number of one-dimensional faces incident to that vertex, not the path degree. The stated classification is for all \(n\ge3\), not an asymptotic or sample result.

## Proof
**1. The edge rule.** The stable sets of a path are exactly its binary words with no adjacent ones. For two such words \(u,v\), let \(D=\{j:u_j\ne v_j\}\). They are joined by a polytope edge exactly when \(D\) is a nonempty interval. For necessity, if \(D\) has two separated components, swap one component between \(u\) and \(v\) to obtain two other stable-set words \(r,s\) with \(u+v=r+s\), so the original segment is not an edge. For sufficiency, the coordinates outside the interval are fixed on the common face: common zero coordinates are fixed by \(y_j\ge0\), while common one coordinates are fixed by a tight inequality \(y_j+y_{j\pm1}\le1\) with an adjacent common zero (the neighbor cannot belong to \(D\), since both endpoints are independent). Inside a connected difference interval, the bits of both words alternate, and all consecutive edge inequalities are tight, leaving exactly one affine free parameter. Consequently their common face has dimension one.

**2. Count the edges at a word.** A nontrivial flippable interval must be an alternating word; it can contain ones from only one cluster. For a cluster with \(k\) ones, it may begin at any of its \(k\) one-positions or, if \(a=1\), at the zero directly preceding its first one. Likewise it may end at a one-position or, if \(b=1\), at the zero directly following its last one. Counting permissible start–end pairs gives
\[
T=\frac{k(k+1)}2+k(a+b)+ab.
\]
Every other flippable interval is a singleton zero with zero (or boundary) on both sides. These free zeros number \(n-2\sum_i k_i+c-\sum_i(a_i+b_i)\), where \(c\) is the number of clusters: each cluster occupies its \(k_i\) ones and touches \(k_i-1+a_i+b_i\) zeros. Combining these disjoint classes, then simplifying for the three possibilities \(a_i+b_i=0,1,2\), gives exactly
\[
\deg(w)=n+\sum_i\binom{k_i+a_i+b_i-1}{2}.
\]
Each binomial is nonnegative, since \(k_i\ge1\).

**3. Simple vertices.** This formula gives \(\deg(w)=n\) precisely when each cluster has \(k_i+a_i+b_i-1\le1\). An interior singleton one has \(a=b=1\) and contributes a positive binomial; so does a cluster with two or more ones. The only possible ones are isolated at the two endpoints. Each of the four listed independent sets has degree \(n\). As \(Q_n\) is full-dimensional, a vertex is simple exactly when it has degree \(n\).

**4. Maximum and equality.** Put \(t_i=k_i+a_i+b_i-1\ge1\). The augmented span of cluster \(i\) (from the preceding zero, if present, to the following zero, if present) has \(r_i=2k_i-1+a_i+b_i\) positions. The augmented spans are pairwise disjoint and satisfy \(r_i\ge2t_i-1\). Therefore \(n\ge2\sum_i t_i-c\). For \(T=\sum_i t_i\), the convexity/merging inequality for positive integers gives
\[
\sum_i\binom{t_i}{2}\le\binom{T-c+1}{2}\le\binom{\lceil n/2\rceil}{2}.
\]
The upper bound is attained by the displayed words. To classify equality, if \(n=2m+1\), two or more clusters force \(T-c+1\le m\), strictly below the target \(m+1\); one cluster must have \(t=m+1\), whence \(a=b=1\) and its augmented span occupies all \(n\) sites. If \(n=2m\), three or more clusters again force strict inequality. Two clusters could only give equality if \(T=m+1\), their augmented spans fill all \(n\) positions, and equality holds in the merging inequality; the latter requires one \(t_i=1\), whereas the span equality forces both \(a_i=b_i=1\), hence both \(t_i\ge2\). This is impossible. For the single remaining cluster, equality is \(t=m\); its augmented span has length \(2m+1-(a+b)\le2m\). Thus either \(a+b=1\) and the span fills all \(n\), producing the two endpoint-alternating words, or \(a+b=2\) and the span has length \(n-1\), producing the two words with one extra endpoint zero. This exhausts the equality cases.

**5. Vertex count.** Independent sets of \(P_n\) satisfy the Fibonacci recurrence, so \(|\operatorname{vert}(Q_n)|=F_{n+2}\). The four simple vertices therefore form an exponentially vanishing fraction, while \(\Delta(Q_n)=n^2/8+O(n)\).

## Verification
The included standalone standard-library script `CHECK.py` independently enumerates all independent-set words for \(3\le n\le11\), constructs every neighbor from the connected-difference criterion, and checks the entire degree formula, all four simple vertices, the exact maxima and all maximizing words. For \(3\le n\le7\) it additionally checks every vertex pair against exact rational ranks of their common tight facet equations, not merely the combinatorial adjacency rule. Its success marker is `FENCE_LOCAL_DEGREE_EXACT_PASS`. The infinite theorem rests on the proof above, not these finite tests.

## Relationship to prior work
Mori (arXiv:2307.08447, publicly posted 2023-07-17) records the general edge criterion for order polytopes and develops higher simplex faces; this supplies known background and is not claimed as novel. Lee (arXiv:2610.07413, publicly posted 2026-10-05) classifies edges into connected-convex-subset classes and gives global edge counts for zigzag order polytopes. Its refined edge theorem is stronger at the level of edge-class incidence and would allow computing degrees by summing individual incidences. The new contribution assessed here is the evaluated **per-vertex cluster formula and exact, globally sharp local-degree equality classification**, not the adjacency criterion, total edge counts, or edge-length census. The degree formula and extremizers were not located in the inspected portions of those sources or targeted record searches. This is a best-knowledge priority assessment, not a guarantee of historical uniqueness.

## Limitations
The result concerns the standard zigzag poset (equivalently the path stable-set polytope) and does not determine the full univariate degree-distribution polynomial, edge-Laplacian spectrum, or results for arbitrary posets. No independent human mathematical audit or comprehensive all-database priority certification has been performed. Any inaccessible or unindexed derivation of the same cluster formula or extremal classification would affect originality.

## References
- A. Mori, *Simplex faces of order and chain polytopes*, arXiv:2307.08447 (first public version 2023-07-17), https://arxiv.org/abs/2307.08447.
- J. Lee, *A refinement of the edge theorem for order and chain polytopes*, arXiv:2610.07413 (first public version 2026-10-05), https://arxiv.org/abs/2610.07413.
