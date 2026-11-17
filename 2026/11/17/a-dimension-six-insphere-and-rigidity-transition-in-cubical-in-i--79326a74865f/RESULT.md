# A dimension-six insphere and rigidity transition in cubical in-in zonotopes

## Finding
Let \(d\ge1\) be an integer, \(N=2^d\), and \(Q_d\) the graph on the binary strings \(V=\{0,1\}^d\), with edges between strings differing in exactly one coordinate. Consider the **unit in-in zonotope** in the standard ambient Euclidean space \(\mathbb R^V\):
\[
\mathcal I_d=\sum_{v\in V}[-e_v,e_v]
+\sum_{\{v,w\}\in E(Q_d)}[-(e_v-e_w),e_v-e_w].
\]
Its maximum inscribed Euclidean ball has exactly the radius
\[
\boxed{r_d=\min\{2^{d/2},d+1\}
=\begin{cases}2^{d/2},&1\le d\le5,\\ d+1,&d\ge6.\end{cases}}
\]
Every maximum ball has a center in an explicit convex set \(\mathcal C_d\), whose affine dimension has the sharp transition
\[
\boxed{\dim\mathcal C_d=\begin{cases}2^d-1,&1\le d\le5,\\0,&d\ge6.\end{cases}}
\]
For \(d\le5\), the affine hull of \(\mathcal C_d\) is the hyperplane \(\sum_{v\in V}c_v=0\), and the origin is in its relative interior. For \(d\ge6\), the origin is the **unique** center. The origin-centered radius-\(r_d\) ball touches precisely two facets for \(d\le5\), namely those with outward normals \(\pm\mathbf1_V\). For \(d\ge6\), it touches precisely \(2N=2^{d+1}\) facets, with outward normals \(\pm e_v\) for \(v\in V\).

The unique minimum enclosing Euclidean ball is centered at the origin and has radius
\[
\boxed{R_d=(d+1)2^{d/2}.}
\]
Its only points of contact with vertices (in fact, with the entire zonotope) are the two antipodes \(\pm(d+1)\chi\), where \(\chi_v=(-1)^{\sum_{i=1}^d v_i}\). Thus the diameter is \(2(d+1)2^{d/2}\), attained by exactly one unordered pair. The exact radius ratio is
\[
\boxed{R_d/r_d=\max\{d+1,2^{d/2}\}.}
\]

## Assumptions and scope
All edge and coordinate generators have coefficient one, as displayed; the norm is the standard Euclidean norm in \(\mathbb R^{2^d}\). In particular this polytope is not the graphical zonotope of \(Q_d\) alone (which lies in a codimension-one hyperplane), nor a symmetric edge convex hull. A contacting facet means a genuine codimension-one face whose supporting hyperplane is tangent to the **origin-centered** maximal inscribed ball. The complete center set is a different object from the individual contact set. A graph subset \(S\subseteq V\) is called connected when the induced graph \(Q_d[S]\) is connected; \(\partial S\) denotes the edge boundary between \(S\) and its complement.

## Proof
**1. Support function, facet normals, and the optimal center.** The zonotope is full-dimensional and centrally symmetric, with support function
\[
h(u)=\sum_{v\in V}|u_v|+\sum_{\{v,w\}\in E(Q_d)}|u_v-u_w|.
\]
If balls of radius \(r\) about \(c\) and \(-c\) are contained in the zonotope, convexity also contains the radius-\(r\) ball about the origin. Hence a largest-ball center may be taken to be zero, and \(r_d=\inf_{\|u\|_2=1}h(u)\).

Each coordinate generator \(e_v\) is free in the exposed face of normal \(u\) exactly when \(u_v=0\); each edge generator \(e_v-e_w\) is free exactly when \(u_v=u_w\). At each nonzero level of \(u\), edge differences span a codimension-one subspace in every connected component; at level zero the free coordinate generators span all zero coordinates. Therefore the exposed-face dimension is \(N\) minus the number of connected components across the nonzero levels. This dimension is \(N-1\) precisely when \(u\) is a nonzero scalar multiple of \(\mathbf1_S\) for one nonempty connected subset \(S\). Every such \(S\) indeed yields a facet pair
\[
\left|\sum_{v\in S}x_v\right|\le |S|+|\partial S|.
\tag{1}
\]
Thus the inradius and every optimal-center constraint are exactly
\[
r_d=\min_{\substack{\varnothing\ne S\subseteq V\\Q_d[S]\ \mathrm{connected}}}
\frac{|S|+|\partial S|}{\sqrt{|S|}},
\tag{2}
\]
\[
\mathcal C_d=\left\{c\in\mathbb R^V:
\left|\sum_{v\in S}c_v\right|+r_d\sqrt{|S|}
\le |S|+|\partial S|\text{ for each nonempty connected }S\subseteq V\right\}.
\tag{3}
\]
The minimum in (2) is unchanged if disconnected subsets are included: if \(S\) has disjoint connected components \(S_j\), its numerator is the sum of their numerators, whereas \(\sqrt{\sum_j|S_j|}\le\sum_j\sqrt{|S_j|}\); the quotient is at least the smallest component quotient, strictly if there are several components.

**2. Cubical edge-isoperimetry without a black box.** For \(S\subseteq\{0,1\}^d\), let \(k=|S|\ge1\) and \(e(S)\) count its induced edges. The elementary sharp inequality
\[
e(S)\le\frac{k\log_2 k}{2},\qquad |\partial S|=dk-2e(S)\ge k(d-\log_2 k)
\tag{4}
\]
has an induction proof. Split the cube in one coordinate into two \((d-1)\)-cubes, with occupancy counts \(a\le b\), \(a+b=k\). The cross edges form a matching, giving
\(e(S)\le(a\log_2a+b\log_2b)/2+a\) by induction (with \(0\log_20=0\)). The inequality \(a\log_2a+b\log_2b+2a\le k\log_2k\) is exactly \(H_2(a/k)\ge2a/k\), which follows by concavity of binary entropy on \([0,1/2]\) and its endpoint values. This proves (4) for all \(d\).

**3. Endpoint rigidity and the sharp threshold.** Using (4), every nonempty \(S\), with \(t=\log_2k\in[0,d]\), satisfies
\[
\frac{k+|\partial S|}{\sqrt{k}}
\ge 2^{t/2}(d+1-t)=g_d(t).
\tag{5}
\]
The derivative of \(g_d\) has the sign of \((\ln2)(d+1-t)/2-1\), a strictly decreasing affine function of \(t\). Thus \(g_d\) first increases and then decreases (or is monotone) and its strict minimum occurs at an endpoint, never in the open interval. The endpoint values are \(g_d(0)=d+1\) and \(g_d(d)=2^{d/2}\), attained by singleton sets and by \(S=V\), respectively. Direct checks for \(1\le d\le5\) and monotonicity of \(2^{d/2}/(d+1)\) for \(d\ge6\) show \(2^{d/2}<d+1\) exactly through \(d=5\). Therefore (2) gives the asserted inradius and precisely its minimizing sets: only \(V\) for \(d\le5\), and precisely the \(N\) singleton sets for \(d\ge6\). These are connected, and every corresponding inequality (1) is a genuine facet, proving the contact counts.

**4. The entire incenter locus.** Each active opposite facet pair in (3) forces its normal to annihilate the center \(c\). Hence for \(d\le5\) all centers satisfy \(\sum c_v=0\), while for \(d\ge6\) the singleton pairs force every \(c_v=0\). For \(d\le5\), all other facet inequalities in (3) have strict slack at the origin. There are finitely many such inequalities, so a sufficiently small neighborhood of zero *inside* \(\sum c_v=0\) obeys all of them. Therefore the center locus has affine dimension exactly \(N-1\) and contains zero in its relative interior; for \(d\ge6\) it is a singleton.

**5. Minimum outer sphere and unique diameter pair.** Every point \(x\in\mathcal I_d\) is a sum of coefficients of absolute value at most one times the coordinate generators and the edge generators. Every vertex \(v\) of \(Q_d\) has degree \(d\), so \(|x_v|\le d+1\). Hence \(\|x\|_2\le(d+1)\sqrt N\). Bipartiteness gives the sign character \(\chi_v=(-1)^{\sum_i v_i}\). Assign the coordinate-generator coefficient \(\chi_v\) and orient each edge generator with its positive contribution at the endpoint where \(\chi=+1\); the resulting point is exactly \((d+1)\chi\), so the bound is sharp. Equality in the Euclidean norm requires every coordinate to saturate its absolute bound, forcing neighboring signs to be opposite along every edge. Since \(Q_d\) is connected and bipartite, there are only two consistent sign assignments, \(\pm\chi\). Thus there are exactly two outer-sphere contacts. The two antipodes also force the minimum enclosing ball to have the stated radius and unique center zero. The triangle inequality shows that diameter can equal \(2R_d\) only between antipodal outer contacts, which gives one unordered diametral pair.

## Verification
The accompanying `verify.py` runs using Python 3.10+ with no third-party packages. It exhaustively checks all nonempty vertex subsets of \(Q_d\) for \(1\le d\le4\), samples deterministic additional subsets for \(5\le d\le9\), verifies the complete equality classifications in the exhaustive cases, evaluates the two extremal sign realizations, and independently enumerates every Minkowski generator endpoint choice for \(d=1,2\). It produced `TOTAL_ASSERTIONS= 77255` and `VERIFICATION_PASSED`. The induction, extremal-set argument, face-dimension proof and outer-sphere argument above—not finite tests—prove the assertions for every integer \(d\ge1\).

## Relationship to prior work
Glew [1] introduced the in-in zonotope and its graphical-plus-coordinate Minkowski description. The published record *Sharp Euclidean inballs and center-locus transitions of tree and cycle in-in zonotopes* [2] established the general graph cut formula and center constraints used in (2)–(3); its tree and cycle classifications include the low-dimensional cube graphs \(Q_1\) and \(Q_2\), but do not determine the family \(Q_d\) for \(d\ge3\). The published record *An exact three-phase inball and center-locus law for complete-bipartite in-in zonotopes* [3] treats a different graph class, intersecting the cubes only at \(Q_2\). The record *A Walsh-spectral collapse of the incenter locus of Boolean-cube graphical zonotopes* [4] proves the cubical induced-edge estimate in (4), but concerns a distinct, lower-dimensional graphical zonotope without coordinate generators; its metric and threshold differ. The new conclusion here is the exact **cubical in-in** inner/outer ball classification, including its sharp \(d=6\) transition, exponential facet-contact jump, center-locus collapse and two rigid antipodes. These are not claimed to be a new general cut formula or a new edge-isoperimetric inequality.

## Limitations
The polytope is the **unweighted** coordinate-plus-graphical Minkowski sum; there are no claims about general positive generator weights, other graph families, or non-Euclidean norms. The affine hull and dimension of the whole center locus are explicit, and (3) gives every defining inequality, but its face vector and volume are not classified. The originality comparison is based on the inspected public source and identified nearby research records; it is not an exhaustive theorem-priority certification. No independent mathematical audit has been performed.

## References
1. Ross Glew, *Geometry of in-in correlators*, arXiv:2601.18903v1 (first public 2026-01-26), section III, equations (10)–(14). https://arxiv.org/html/2601.18903
2. *Sharp Euclidean inballs and center-locus transitions of tree and cycle in-in zonotopes*, publicly indexed research record, 2026-10-25, record suffix `2115bd29349a`.
3. *An exact three-phase inball and center-locus law for complete-bipartite in-in zonotopes*, publicly indexed research record, 2026-10-25, record suffix `f12dc9273ea5`.
4. *A Walsh-spectral collapse of the incenter locus of Boolean-cube graphical zonotopes*, publicly indexed research record, 2026-10-11, record suffix `24f8de7b2a90`.
