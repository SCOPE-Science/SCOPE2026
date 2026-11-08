# Parity and a sharp facet transition in biclique graphical-zonotope incenter loci

## Finding
Let integers \(4\le p\le q\), let \(N=p+q\), and let \(A\sqcup B\) be a disjoint vertex set of sizes \(|A|=p\), \(|B|=q\). The centered graphical zonotope of the complete bipartite graph is
\[
Z_{p,q}=\sum_{i\in A,\,j\in B}\left[-\tfrac12(e_i-e_j),\tfrac12(e_i-e_j)\right]
\subset H=\{x\in\mathbb R^N:\sum_i x_i=0\}.
\]
All balls and radii are intrinsic Euclidean balls in \(H\). The optimal radius is
\[
\rho_{p,q}=\frac p2\sqrt{\frac{N}{N-1}}.
\]
If \(p=q\), the origin is the unique center of a ball of radius \(\rho_{p,q}\).

If \(q>p\), put \(\delta=(q-p)/2\) and
\[
E_{p,q}=\left\{x\in H:x_j=0\ (j\in B),\quad |x_i|\le\delta\ (i\in A)\right\}.
\]
When \(p\ge5\) is odd, the **entire** optimal-incenter locus is \(\mathcal I_{p,q}=E_{p,q}\). For even \(p\ge4\), define
\[
L_{p,q}=\frac{pq}{4}-\frac p2\sqrt{\frac{\lfloor N^2/4\rfloor}{N-1}}.
\]
Then its complete incenter locus is
\[
\mathcal I_{p,q}=\left\{x\in E_{p,q}:\left|\sum_{i\in T}x_i\right|\le L_{p,q}
\text{ for every }T\subset A\text{ with }|T|=p/2\right\}.
\]
This is an exact, finite, all-parameter classification, not merely a necessary condition. For even \(p\), the middle-cardinality inequalities are redundant exactly when
\[
N\le p^2-1\quad\bigl(\text{equivalently }q\le p^2-p-1\bigr),
\]
and properly truncate \(E_{p,q}\) exactly when \(N\ge p^2\). Hence increasing the larger part through \(q=p^2-p\) creates **exactly \(\binom p{p/2}\) distinct new middle-subset facets** only for even smaller-part order. For all \(q>p\) the affine dimension of \(\mathcal I_{p,q}\) is \(p-1\).

In every case where \(q>p\) and \(\mathcal I_{p,q}=E_{p,q}\), the exact vertex number is
\[
f_0(\mathcal I_{p,q})=\begin{cases}
\binom p{p/2},&p\text{ even},\\
p\binom{p-1}{(p-1)/2},&p\text{ odd}.
\end{cases}
\]

## Assumptions and scope
The graph is unweighted, simple, complete bipartite; the generating segments are centered and have Euclidean length \(\sqrt2\). The distance is inherited from the standard scalar product in the codimension-one space \(H\). The integers obey \(4\le p\le q\); the smaller part has size \(p\). The classification describes **every** center of a maximum-radius inscribed Euclidean ball, not only centers constrained by graph symmetries.

## Proof
**1. Exact cut halfspaces.** For a proper nonempty vertex subset \(S\subsetneq A\sqcup B\), write \(s=|S|\), \(x(S)=\sum_{i\in S}x_i\), \(v_S=\mathbf1_S-(s/N)\mathbf1\), and \(d(S)=|\partial S|\). Then \(\|v_S\|=\sqrt{s(N-s)/N}\), and
\[
Z_{p,q}=\left\{x\in H:|x(S)|\le\frac{d(S)}2\text{ for every proper nonempty }S\right\}.
\]
Necessity follows directly from the segment support function. For sufficiency, order the coordinates of any \(u\in H\); telescope them along the nested superlevel sets. The support of the claimed halfspace intersection in direction \(u\) is bounded by \(\tfrac12\sum_{ij\in E}|u_i-u_j|\), the zonotope support, by the discrete coarea identity. Thus the two convex sets agree. A ball of radius \(r\) centered at \(x\in H\) lies in \(Z_{p,q}\) exactly when
\[
|x(S)|+r\sqrt{\frac{s(N-s)}N}\le\frac{d(S)}2
\quad\text{for every proper nonempty }S.\tag{1}
\]
Since \(Z_{p,q}\) is centrally symmetric, averaging any feasible radius-\(r\) balls at centers \(x\) and \(-x\) gives a radius-\(r\) ball at the origin. Hence the optimal radius is the smallest origin-to-cut-plane distance.

**2. The strictly nearest cut planes.** The graph Laplacian of \(K_{p,q}\) has eigenvalues \(0\), \(p\) with multiplicity \(q-1\), \(q\) with multiplicity \(p-1\), and \(N\) once. Its spectral gap is \(p\). Consequently, for every proper cut with \(t=s(N-s)\),
\[
d(S)=\mathbf1_S^\top L\mathbf1_S\ge\frac{pt}{N}.
\]
If \(2\le s\le N-2\) then \(t\ge2(N-2)>N^2/(N-1)\) for \(N\ge8\); hence
\[
d(S)>p\sqrt{\frac{t}{N-1}}.
\]
In contrast, a singleton in \(B\) has cut size \(p\), and singleton norm \(\sqrt{(N-1)/N}\); a singleton in \(A\) has cut size \(q\). Therefore the least cut-plane distance is exactly \(\rho_{p,q}\). When \(p=q\), every singleton is tight at the origin, forcing every coordinate of every optimal center to vanish in (1). When \(q>p\), precisely the \(B\)-singletons (and complements) are tight, so all optimal centers satisfy \(x_j=0\) for \(j\in B\) and \(\sum_{i\in A}x_i=0\).

**3. Singleton bounds and the cut reduction.** For \(q>p\), the singleton inequalities in \(A\) at \(r=\rho_{p,q}\) give the **necessary** coordinate bounds \(|x_i|\le(q-p)/2=\delta\). To prove all other cuts except possibly balanced \(A\)-subsets automatically follow, let \(a=|S\cap A|\), \(b=|S\cap B|\). Then
\[
d(S)=a(q-b)+b(p-a),\qquad s=a+b.
\]
When \(1\le a<p/2\), the cube bounds imply \(|x(S)|\le a\delta\). The required inequality (1) follows from
\[
d(S)-a(q-p)=ap+(p-2a)b
\ge p\sqrt{a+b}\ge p\sqrt{\frac{s(N-s)}{N-1}}.\tag{2}
\]
For completeness, the nontrivial middle inequality in (2) holds for **all integers** \(p\ge4\), \(1\le a<p/2\), \(b\ge0\). Put \(c=p-2a\ge1\) and square both nonnegative sides. The difference is
\[
c^2b^2+(2apc-p^2)b+p^2a(a-1).
\]
If \(2ac\ge p\), every coefficient is nonnegative. Otherwise \(c(2a-1)<2a\); because \(p\ge4\), this forces \(a\ge2\), \(c=1\), \(p=2a+1\). The quadratic discriminant is \(p^2(p^2-8a^2)<0\) for \(a\ge2\), proving (2). Subsets with \(a>p/2\) reduce by complementation; subsets with \(a=0\) or \(a=p\) have \(x(S)=0\) and follow from Step 2. This proves sufficiency of the cube bounds for odd \(p\).

**4. Only the even middle cuts can survive.** For even \(p\) and \(a=p/2\), the boundary count is independent of \(b\): \(d(S)=pq/2\). Among integers \(0\le b\le q\), the normal norm is maximized when \(s=a+b\) is closest to \(N/2\); its squared maximum is \(\lfloor N^2/4\rfloor/N\). The tightest remaining inequalities (1) are precisely the balanced-subset bounds with right side \(L_{p,q}\), proving the claimed necessary-and-sufficient description.

**5. Sharp transition, dimension and vertices.** A balanced subset sum over \(E_{p,q}\) attains \((p/2)\delta\) at the point having \(+\delta\) on that subset and \(-\delta\) on its complement. Direct subtraction yields
\[
L_{p,q}-\frac p2\delta
=\frac p4\left(p-2\sqrt{\frac{\lfloor N^2/4\rfloor}{N-1}}\right).
\]
For odd \(N\), twice the displayed square root equals \(\sqrt{N+1}\); for even \(N\), it equals \(N/\sqrt{N-1}\). Both are strictly increasing, and for even \(p\) the successive values at \(N=p^2-1\) and \(N=p^2\) are respectively \(p\) and strictly greater than \(p\). This proves the sharp threshold and genuine truncation. In the truncated regime let \(a=p/2\) and fix a middle subset \(T\). The point with coordinates \(+L_{p,q}/a\) on \(T\), \(-L_{p,q}/a\) on \(A\setminus T\), and zero on \(B\) satisfies this one oriented middle-subset inequality with equality; all box inequalities and all other *distinct* oriented middle-subset inequalities are strict, since \(0<L_{p,q}<a\delta\). Thus each oriented middle-subset inequality is a true facet, and the \(\binom p{p/2}\) subsets index exactly that many distinct new facets. Because every nonsingleton cut was strictly farther than the optimal origin ball, \(L_{p,q}>0\); when \(q>p\), \(\delta>0\) also. Therefore the center locus has relative interior in the \((p-1)\)-dimensional space \(x_B=0\), \(\sum_A x_i=0\).

Finally, vertices of the untruncated central cube section require at least \(p-1\) box bounds to be active. For even \(p\), they have half their coordinates \(+\delta\) and half \(-\delta\). For odd \(p\), exactly one coordinate is zero and the remaining ones split equally between \(+\delta\) and \(-\delta\). Counting these choices gives the stated vertex formulas. This completes the proof.

## Verification
The standard-library script `verify_bipartite_centers.py` checks the exact cut distances across all part-intersection cardinalities and independently compares the claimed center predicates against **every** cut inequality for multiple graph sizes spanning both sides of the even-part threshold. It tests random candidate centers, boundary examples, and cube-section vertex counts. Execute with `python verify_bipartite_centers.py`; the expected success marker is `BIPARTITE_GRAPHICAL_ZONOTOPE_CENTER_CHECKS_PASSED`. The all-dimensional assertions follow from the proof above, not from finite checks.

## Relationship to prior work
Padrol--Pilaud--Poullot (2021 preprint) develops graphical zonotope structure and its deformation cone; Chapoton--Pilaud (2022 preprint) treats \(K_{p,q}\) zonotopes as shuffles and determines combinatorial data such as their face numbers. A previously published general weighted-graph cut formula determines the **radius**, which is therefore not proposed as an independent new invariant here. The distinguishing result is the complete incenter locus, its parity dichotomy, and the **sharp** transition at \(p+q=p^2\). Existing related center-locus results for cycles and Boolean-cube graph zonotopes concern different graph families and do not imply this classification from their stated conclusions.

## Limitations
The theorem is for unweighted bicliques with \(p\ge4\) and the canonical intrinsic Euclidean metric, not for weights, arbitrary graph families, or the small cases \(p=2,3\). The exact extreme-point count is asserted only in the untruncated cube-section phase; no count is claimed for the truncated even phase. Historical priority remains provisional because equivalent formulations may exist under metric-optimization terminology.

## References
1. Arnau Padrol, Vincent Pilaud and Germain Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, first posted 2021-11-24; Discrete & Computational Geometry, DOI:10.1007/s00454-023-00586-x.
2. Frédéric Chapoton and Vincent Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, first posted 2022-01-18; Annales Henri Lebesgue, DOI:10.5802/ahl.225.
3. *Euclidean inradius of weighted graphical zonotopes is a cut expansion constant*, published mathematical research record, published-finding corpus record `2026/10/11/SCOPE-euclidean-inradius-of-weighted-graphical-zonotopes-is-a-cut-expa--cb1eceb082ab`; radius comparison only.
