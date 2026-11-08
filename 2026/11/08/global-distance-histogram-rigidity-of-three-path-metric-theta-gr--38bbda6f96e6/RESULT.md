# Global distance-histogram rigidity of three-path metric theta graphs

## Finding
Let \(G(a,b,c)\) consist of three internally disjoint paths of positive lengths \(0<a\le b\le c\), joined at the same two endpoints, with the intrinsic shortest-path metric. Sample \(X,Y\) independently from normalized arclength measure and let \(D=d_G(X,Y)\). Write \(L=a+b+c\), \(F(r)=\Pr(D\le r)\), and let \(f=F'\), interpreted by its one-sided continuous polynomial pieces.

The complete distribution determines \(a,b,c\), including all coincidences and without any genericity assumption. Specifically,
\[
 f(0+)=\frac{2}{L},\qquad
 \operatorname{Jump}_d(f):=f(d+)-f(d-)<0
\]
precisely at the **distinct** members of
\[
 \left\{\frac{a+b}{2},\frac{a+c}{2},\frac{b+c}{2}\right\}.
\]
Before merging coincident radii, their respective signed contributions are
\[
 \begin{array}{c|c}
 \text{radius}& L^2\operatorname{Jump}(f)\\ \hline
 (a+b)/2&-2(a+b)\\
 (a+c)/2&-2(a+c)\\
 (b+c)/2&-4a
 \end{array}.
\]
Contributions at equal radii add; all are strictly negative. In particular, at the longest of the three cycle half-circumferences, the coefficient depends on the **shortest** connecting path rather than on that cycle's circumference. The number of distinct discontinuities is one, two, or three according as all three lengths are equal, exactly two lengths are equal, or all lengths are distinct.

## Assumptions and scope
A path is a copy of a compact interval with positive real length, and its endpoints are identified with the same two common poles. All edges are counted once in total arclength \(L\); subdivisions of paths do not matter. The measure assigns probability \(\operatorname{length}(B)/L\) to each measurable network subset \(B\). There are exactly three paths; no pendant edges or additional parallel paths are assumed. Distances are geodesic shortest-path distances and the sampling is independent. Since the distance law is absolutely continuous, one-sided values of the density refer to its canonical piecewise-polynomial representative, rather than arbitrary representatives differing on null sets.

## Proof
**Step 1: an exact geometric tail formula.** Label the three path lengths \(u,v,w\) in turn. For two points on the same length-\(u\) path, let \(t\in[0,u]\) be their coordinate separation and \(m\) the shorter length of the other two paths. Their intrinsic distance is
\[
 d=\min\{t,u+m-t\}.
\]
For \(r\ge0\), the (unnormalized, ordered-pair) area of same-path pairs at distance greater than \(r\) is
\[
 T_{u,m}(r)=\begin{cases}
 \displaystyle\int_{r}^{\min\{u,u+m-r\}}2(u-t)\,dt,&r<\min\{u,(u+m)/2\},\\
 0,&\text{otherwise},
 \end{cases}
\]
where the integral is understood as zero when its upper bound is at most its lower bound.

For points on two different paths of lengths \(u,v\), use coordinates \(x\in[0,u]\) and \(y\in[0,v]\) from their common initial pole. Their shortest distance is the minimum of the following four lengths:
\[
 x+y,\quad u+v-x-y,\quad x+v-y+w,\quad u-x+y+w.
\]
Consequently the (unnormalized, *unordered path-pair*) area of pairs at distance greater than \(r\) is the Euclidean area \(B_{u,v;w}(r)\) of the convex region
\[
 P_{u,v;w}(r)=\left\{(x,y)\in[0,u]\times[0,v]:
 r<x+y<u+v-r,\quad r-v-w<x-y<u+w-r\right\}.
\]
With the three path lengths forming a multiset \(\{a,b,c\}\), the exact tail law is
\[
 \Pr(D>r)=\frac{1}{L^2}\left(\sum_{u\in\{a,b,c\}}T_{u,m_u}(r)
 +2\sum_{\{u,v\}\subset\{a,b,c\}}B_{u,v;w}(r)\right),
\]
where the sums are over labeled paths even when their lengths coincide; \(m_u\) is the minimum of the two other lengths and \(w\) is the remaining labeled path length. All terms are areas of polygons with boundaries affine in \(r\), hence are continuous, piecewise quadratic functions. Therefore \(F\) is absolutely continuous and its canonical density is piecewise affine.

**Step 2: same-path jumps.** If \(u>m\), then for \(r\) immediately below \(d=(u+m)/2\), the interval of integration in \(T_{u,m}(r)\) has length \(2(d-r)\), and its integrand tends to \(u-m\). Thus
\[
 T_{u,m}(d-\varepsilon)=2(u-m)\varepsilon+O(\varepsilon^2),\qquad
 T_{u,m}(d+\varepsilon)=0
\]
for sufficiently small \(\varepsilon>0\). The corresponding density jump is \(-2(u-m)/L^2\). If \(u\le m\), its endpoint integral vanishes at least quadratically at \(r=u\) and produces no density jump. At the intermediate switch \(r=m\), both derivative formulas agree; hence there are no additional same-path jumps.

**Step 3: different-path jumps.** The two moving parallel boundaries on \(x+y\) coalesce precisely at \(d=(u+v)/2\). At \(r=d\), the remaining constraints cut out a segment of the line \(x+y=d\), centered at \((u/2,v/2)\) and of length \(\sqrt2\min\{u,v,w\}\) in Euclidean length. Since the \(x+y\)-strip just below \(d\) has coordinate width \(2\varepsilon\), its intersection has area
\[
 B_{u,v;w}(d-\varepsilon)=2\min\{u,v,w\}\varepsilon+O(\varepsilon^2),\qquad
 B_{u,v;w}(d+\varepsilon)=0.
\]
The factor of two for ordered choices of which path contains \(X\) gives the density jump \(-4\min\{u,v,w\}/L^2\).

There are no other jumps from the moving polygon. Indeed, its boundary lines and the fixed rectangle may change combinatorial type when a boundary reaches a vertex, but at a nonparallel crossing the modified triangular area is \(O(\varepsilon^2)\), leaving first derivatives continuous. The only other pair of parallel moving boundaries, those involving \(x-y\), could meet at \(r=(u+v)/2+w\), strictly after the \(x+y\) strip is empty. Other parallel pairs have at most one moving boundary. Thus the preceding jump list is exhaustive.

**Step 4: collect contributions.** Since \(a\le b\le c\), the cross-path pairs \(\{a,b\}\), \(\{a,c\}\), \(\{b,c\}\) each contribute \(-4a/L^2\) at their half-sum radius. The length-\(b\) same-path pairs add \(-2(b-a)/L^2\) at \((a+b)/2\), and the length-\(c\) same-path pairs add \(-2(c-a)/L^2\) at \((a+c)/2\). This gives the three labeled coefficients stated above. All terms are negative, so their merger at coincident radii cannot hide a jump.

**Step 5: reconstruction including ties.** Because points close enough along the interior of any path have intrinsic ball length \(2r\), integrating their contributions gives \(F(r)=2r/L+O(r^2)\) as \(r\downarrow0\), and hence \(L=2/f(0+)\). If the observed jump locations are distinct \(r_1<r_2<r_3\), then
\[
 a=r_1+r_2-r_3,\quad b=r_1+r_3-r_2,\quad c=r_2+r_3-r_1.
\]
If just two distinct locations \(s<t\) occur, either \(a=b=s\), \(c=2t-s\) and \(L=s+2t\), or \(a=2s-t\), \(b=c=t\) and \(L=2s+t\). Because \(s<t\), these total lengths differ and distinguish the cases. If only one jump at \(r\) occurs, then \(a=b=c=r\) (and \(L=3r\)). Thus the distribution recovers the length multiset in every case and therefore the intrinsic theta graph up to isometry. \(\square\)

## Verification
The accompanying independent Python 3 standard-library program `verify.py` evaluates the exact tail areas by rational polygon clipping and rational integral identities. It verifies jump groups and reconstructed lengths for ten rational test triples (including all tie patterns) and independently samples 320,000 uniformly arclength-distributed point pairs to check twenty CDF values. Executing `python verify.py` produced:

`THETA_VERIFY_OK exact_rational_cases=10 jump_groups=24 recovered=10 independent_pair_samples=320000 cdf_comparisons=20 max_abs_cdf_error=0.0026625`

These finite checks are not a proof of the statement for arbitrary real lengths; the proof is Steps 1–5.

## Relationship to prior work
Bose and collaborators (2013, 2014) developed algorithms for farthest-point queries in continuous geometric networks, including cactus graphs. Mémoli and Needham (initial preprint 2018, Remark 4.6 of `arXiv:1810.09646v5`) already observed the piecewise-linear structure and qualitative jump phenomena of global graph distance distributions, and posed broad inverse questions. Their result is a principal baseline: piecewise linearity or the mere existence of jumps is **not** asserted as new here. Baptista and coauthors (2023–2024) study metric-graph mean distances, a weaker scalar invariant than the complete law. The contribution here is the explicit all-parameter triple of jump coefficients and a global length-reconstruction proof for a two-cycle network with a shared path, including equal-length degeneracies. The qualitative results just cited do not supply these coefficients or imply this particular full metric reconstruction. Historical priority is provisional pending independent literature review.

## Limitations
The theorem is restricted to a three-path theta graph with positive lengths, normalized continuous arclength sampling, and the exact population distribution. It neither establishes stability under sampling noise nor reconstructs arbitrary metric graphs. It makes no general claim that jump locations uniquely determine an arbitrary graph. The historical novelty assessment is limited to the accessible scientific sources identified below; it is not independent priority certification.

## References
1. Bose et al., *Network Farthest-Point Diagrams and Their Application to Feed-Link Network Extension*, `arXiv:1304.1909v1` (publicly available April 6, 2013), https://arxiv.org/abs/1304.1909.
2. Bose et al., *Optimal Data Structures for Farthest-Point Queries in Cactus Networks*, `arXiv:1411.1879v1` (2014), https://arxiv.org/abs/1411.1879.
3. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, `arXiv:1810.09646v5`, especially Section 4 and Remark 4.6 (initial preprint 2018), https://arxiv.org/abs/1810.09646.
4. Baptista et al., *Mean Distance on Metric Graphs*, `arXiv:2312.04952v2` (2023–2024), https://arxiv.org/abs/2312.04952.
