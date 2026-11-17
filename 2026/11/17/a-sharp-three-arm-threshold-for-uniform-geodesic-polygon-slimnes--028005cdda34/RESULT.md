# A sharp three-arm threshold for uniform geodesic-polygon slimness

## Finding
Let \(\Theta(a,b,c)\) be the compact metric graph consisting of three internally disjoint arcs joining the same two poles, with positive lengths \(0<a\le b\le c\), equipped with its intrinsic shortest-path metric. The arcs are continuously parametrized: every interior point, not only branch vertices, is part of the metric space. A geodesic \(n\)-gon, for \(n\ge3\), is a cyclic list of shortest-path sides. Let \(\Delta_{\mathrm{poly}}(X)\) be the smallest real \(\delta\ge0\) for which, for every \(n\ge3\) and every geodesic \(n\)-gon in \(X\), each side lies within distance \(\delta\) of the union of the other sides.

**Theorem.** For every positive real triple \(0<a\le b\le c\),
\[
\boxed{\Delta_{\mathrm{poly}}(\Theta(a,b,c))=\frac{c+\min\{b,3a\}}4.}
\]
Equivalently, the constant equals \((b+c)/4\) for \(b\le3a\), and \((c+3a)/4\) for \(b\ge3a\). The equality at the threshold is continuous. A geodesic polygon with finitely many sides attains the sharp constant for every real triple, even when the lengths are not commensurable.

## Assumptions and scope
All three arcs have strictly positive real lengths; their interiors are pairwise disjoint, and exactly their two pairs of endpoints are identified. The metric is intrinsic length distance in the geometric realization. Polygons may have arbitrarily many sides and may repeat vertices or intersect; each individual side must be a globally shortest path between its endpoints. The theorem is about the smallest **uniform polygon** slimness constant, not the four-point Gromov hyperbolicity constant, not only the sharp geodesic-**triangle** constant, and not the combinatorial vertex-only graph metric. These distinct invariants must not be conflated.

## Proof
Write \(A\) and \(B\) for the common poles; measure positions on each arm from \(B\). A simple path on a theta graph cannot revisit a pole.

**1. Reduction of an arbitrary polygon to one geodesic arc and one alternate arc.** Fix a geodesic side \(S\) of a polygon, and put \(Y\) equal to the union of the remaining sides. Then \(Y\) is compact and path connected and contains both endpoints of \(S\). For any connected component of the open subset \(S\setminus Y\), denote its closure by \(T\) and its endpoints by \(x,y\in Y\). The arc \(T\) is itself a geodesic, because it is a subarc of \(S\); its interior is disjoint from \(Y\). Choose a simple arc \(Q\subseteq Y\) joining \(x\) to \(y\). It is internally disjoint from \(T\). Thus \(T\cup Q\) is an embedded circle, namely the union of two of the three pole-to-pole arms. Moreover, \(d(z,Y)\le d(z,Q)\) for \(z\in T\). If \(S\subseteq Y\), its contribution is zero, so it suffices to bound such components.

**2. Components avoiding a pole, or containing both poles.** If \(T\) lies inside a single arm of length \(L\), its length \(\ell\) cannot exceed the competing route obtained using the shortest other arm. If \(h\) denotes that other arm's length, \(2\ell\le L+h\le c+a\): if \(L=a\), then \(h=b\le c\), while otherwise \(h=a\). Since both endpoints of \(T\) belong to \(Y\), every point of \(T\) has distance at most \(\ell/2\le(c+a)/4\) from \(Y\).

If \(T\) contains both poles, the fact that \(T\cup Q\) is a simple circle forces the two endpoints into the same arm and the middle portion of \(T\) to traverse a second arm from pole to pole. This second arm must have minimum length \(a\): replacing it by a strictly shorter arm would contradict global shortestness; an arm of length greater than \(a\) also cannot occur when the endpoint arm itself has length \(a\), because the direct endpoint arc would be shorter. Let \(L\le c\) be the endpoint-arm length, and \(\ell\) the length of \(T\). Since its complementary arc on that endpoint arm has length \(L+a-\ell\), shortestness implies \(2\ell\le L+a\le c+a\). Again all its points are at distance at most \((c+a)/4\) from \(Y\).

In both cases, \((c+a)/4\le(c+\min\{b,3a\})/4\), using \(a\le b\) and \(a\le3a\).

**3. A component containing exactly one pole.** Suppose \(T\) follows two distinct arms of lengths \(P,Q\) through pole \(B\); write \(u,v\ge0\) for its two lengths from \(B\) to its endpoints, and let \(K\) be the third arm's length. The alternate arc \(Q_{\mathrm{alt}}\) runs through \(A\). Shortestness of \(T\), and of each of its two pole-containing subarcs, gives
\[
 u+v\le\frac{P+Q}{2},\qquad
 u\le\frac{P+K}{2},\qquad
 v\le\frac{Q+K}{2}.
\]
For a point at distance \(t\) from \(B\) along the \(u\)-branch, its distance to \(Q_{\mathrm{alt}}\) is exactly
\[
\min\{u-t,\ t+\min(v,K)\}.
\]
The analogous formula holds for the \(v\)-branch. Maximizing these elementary piecewise-linear expressions gives
\[
\max_{z\in T} d(z,Q_{\mathrm{alt}})
 =\frac{\max(u,v)+\min\{u,v,K\}}2.
\]
This is no larger than \((u+v)/2\le(P+Q)/4\le(b+c)/4\). It is also at most \((c+3a)/4\): if \(K=a\), the larger of \(u,v\) is at most \((c+a)/2\), while \(\min\{u,v,K\}\le a\); if \(K>a\), one of the two arms \(P,Q\) has length \(a\), so the stronger bound \((P+Q)/4\le(c+a)/4\) applies. Combining both estimates gives
\[
\max_{z\in T}d(z,Y)\le \frac{c+\min\{b,3a\}}4.
\]
The three cases exhaust all possible arcs \(T\) that form a circle with an internally disjoint alternate path. This proves the universal upper bound for **every finite number of geodesic sides**.

**4. Sharp polygon for every real triple.** Choose the arms of lengths \(c\) and \(b\), with the third arm of length \(a\). Starting from pole \(B\), choose \(x\) on the \(c\)-arm and \(y\) on the \(b\)-arm at respective distances
\[
 u=\frac{c+a}{2},\qquad v=\min\left\{a,\frac{b-a}{2}\right\}.
\]
The arc \(S=x\longrightarrow B\longrightarrow y\) is a geodesic: the competing paths through the opposite pole or through the third arm are no shorter because \(u\le(c+a)/2\), \(v\le(b+a)/2\), and \(u+v\le(b+c)/2\). (The last inequality follows from \(v\le(b-a)/2\).) Let \(Q=x\longrightarrow A\longrightarrow y\) be the opposite arc on the same two arms. Split \(Q\) into finitely many sufficiently short subarcs; each is a shortest path in the metric graph (for instance, all lengths less than \(a/2\) suffice). Together with the single geodesic side \(S\), these subarcs form a geodesic polygon.

Because \(u\ge v\) and \(v\le a\), the maximum along \(S\) of the distance to the union of all other sides, which is exactly \(Q\), equals \((u+v)/2\) by the expression in step 3. This is
\[
\frac{u+v}{2}=\frac{c+\min\{b,3a\}}4.
\]
The construction remains valid at \(b=a\), when \(v=0\) and \(y=B\). This proves sharpness, including every equality boundary and arbitrary positive real lengths.

## Verification
The standalone standard-library script `verify_theta.py` independently builds meshes of seven different metric theta graphs. For each mesh, it enumerates **all simple paths** between every unordered vertex pair; each globally shortest path is tested against every internally disjoint alternate simple path using independently computed breadth-first-search distances. For all seven cases it finds exactly the predicted sharp value on the indicated mesh. The script reports 3,128 exact geodesic/alternate path comparisons. A separate rational-arithmetic witness check covers all 252 sorted integer triples in the displayed parameter loops. These are finite corroborations only: the real-length and all-polygons theorem is proved by steps 1–4 and is not inferred from a mesh.

## Relationship to prior work
Tselekidis (2026) introduces the uniform geodesic-polygon slimness condition and studies its relationship to asymptotic Assouad–Nagata dimension; his full public manuscript does not compute the sharp theta-graph constant. Dragan and Mohammed (2019) study shortest-geodesic **triangle** slimness in finite unweighted graphs. The published exact four-point hyperbolicity law for equal-arm theta graphs treats \(\delta_4\), a distinct metric invariant with a different definition and a restricted two-equal-arm family; its formula cannot imply the all-polygon formula. Another published theta-graph result counts finite-graph geodesic subpaths rather than measuring their distance from the union of polygon sides. The present argument concerns arbitrary real lengths, all points of the continuum metric graph, and arbitrarily many geodesic polygon sides.

## Limitations
Only three-arm theta metric graphs are classified; the theorem does not cover four or more parallel arms or general series-parallel networks. The constant is not claimed to equal the sharp triangle-slimness or four-point hyperbolicity constants. The proof is a direct metric argument; exact finite checks corroborate but cannot certify the continuum statement. Historical priority beyond inspected accessible literature and the cited published comparisons is not conclusively established. No independent audit has been performed.

## References
- P. Tselekidis, *Logarithmically Slim Polygons*, arXiv:2611.05429v1, first public 2026-11-03. https://arxiv.org/html/2611.05429v1
- F. F. Dragan and A. Mohammed, *Slimness of graphs*, Discrete Mathematics & Theoretical Computer Science 21 (2019), article 10. https://dmtcs.episciences.org/en/articles/4288
- *Three-phase exact four-point hyperbolicity of equal-arm metric theta graphs*, publicly available mathematical research note, 2026-11-01. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-three-phase-exact-four-point-hyperbolicity-of-equal-arm-metric-t--1d5abc43e807
- *Exact geodesic-subpath counts for all three-path theta graphs*, publicly available mathematical research note, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-geodesic-subpath-counts-for-all-three-path-theta-graphs--35cbb77ad86f
