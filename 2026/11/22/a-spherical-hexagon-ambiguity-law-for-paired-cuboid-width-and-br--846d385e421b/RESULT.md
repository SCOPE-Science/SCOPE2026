# A spherical-hexagon ambiguity law for paired cuboid width and brightness

## Finding

Let a rectangular cuboid have three pairwise distinct, ordered positive edge lengths \(0<a<b<c\). For a uniformly distributed unoriented viewing direction \(U\in S^2\), record both its **directional width** \(W\), between supporting planes orthogonal to \(U\), and its **brightness** \(B\), the area of orthogonal projection onto \(U^\perp\). Put
\[
 v=(a,b,c),\qquad w=(bc,ac,ab),\qquad L=\begin{pmatrix}v\\w\end{pmatrix},\qquad G=LL^{\mathsf T},\qquad N=\sqrt{\det G}.
\]
Write \(k=N^{-1}(v\times w)=(-p,q,-r)\), where
\[
 p=\frac{a(c^2-b^2)}N,\quad q=\frac{b(c^2-a^2)}N,\quad r=\frac{c(b^2-a^2)}N.
\]
Then \(p,q,r>0\), \(p^2+q^2+r^2=1\), and \(q^2>1/2\).

For \(t=(x,y)^{\mathsf T}\in\mathbb R^2\), let \(s(t)=t^{\mathsf T}G^{-1}t\). When \(s(t)<1\), define the two lifted directions
\[
 z(t)=L^{\mathsf T}G^{-1}t,\qquad u_\pm(t)=z(t)\pm\sqrt{1-s(t)}\,k.
\]
For almost every \(t\), the **complete joint density** of \((W,B)\) is
\[
 f_{W,B}(t)=\frac{2}{\pi N\sqrt{1-s(t)}}\left(\mathbf1_{\{u_+(t)\in(0,\infty)^3\}}+\mathbf1_{\{u_-(t)\in(0,\infty)^3\}}\right)
\]
for \(s(t)<1\), and zero outside that ellipse. This specifies the complete support without implicit integrations. In the interior of the accessible elliptical boundary arc, the density has a \((1-s)^{-1/2}\) divergence with coefficient \(4/(\pi N)\).

The pair \((W,B)\) reconstructs the absolute viewing coordinates up to **at most two** possibilities, except on a probability-zero fold/boundary set. A direction has two compatible absolute-coordinate triples precisely when its reflection across the row plane of \(L\) remains in the positive octant. The exact probability of this ambiguity is
\[
 \boxed{\quad P_{\mathrm{amb}}(a,b,c)=\frac4\pi\left[\arcsin(2pq)+\arcsin(2qr)-\arcsin p-\arcsin r\right].\quad}
\]
It lies strictly between zero and one for \(a<b<c\). Its infimum over such boxes is zero, approached along \((a,b,c)=(1,t,t^2)\), \(t\to\infty\); its supremum is one, approached as either adjacent pair of edges coalesces while the other edge remains distinct. Thus no shape-independent positive lower bound or uniform upper bound below one is possible for the reconstruction ambiguity.

## Assumptions and scope

The cuboid is fixed, axis-aligned for notation, and its edge lengths are known, strictly ordered and nonzero. The direction is Haar-uniform on \(S^2\); sign changes of its coordinates are considered trivial geometric reflection symmetries. Brightness means geometric orthogonal projection area, not photometric illumination. The probability of ambiguity refers to a uniformly sampled direction whose two real-valued paired observations are given exactly. The joint density is defined off a null set (the image of coordinate great circles and the folding ellipse); assigning values on that null set does not affect the law.

## Proof

**1. Geometric reduction.** Width adds across the three edge directions: \(W=a|U_1|+b|U_2|+c|U_3|\). Cauchy's elementary face projection formula gives \(B=bc|U_1|+ac|U_2|+ab|U_3|\). The absolute-coordinate vector \(u=(|U_1|,|U_2|,|U_3|)\) is uniform in surface area on the positive spherical octant \(O=S^2\cap[0,\infty)^3\), which has area \(\pi/2\), and \((W,B)^{\mathsf T}=Lu\). Because the edge lengths are pairwise distinct, the rows of \(L\) are linearly independent and \(G\) is positive definite.

**2. Rank-two pushforward and density.** The unit normal to the row plane is \(k=(v\times w)/N\). Every solution of \(Lu=t\) with \(\|u\|=1\) is \(u=z(t)\pm\sqrt{1-s(t)}\,k\), provided \(s(t)\le1\); there are no other solutions. In orthonormal coordinates on the row plane, the spherical area Jacobian of each sheet over its disk projection is \((1-s)^{-1/2}\). The linear coordinate change from those planar coordinates to \(t\) has absolute determinant \(N\). Multiplying the sheet Jacobian by the octant's normalized density \(2/\pi\), and retaining only lifts with positive coordinates, yields the stated joint density. In a neighborhood of any positive vector in \(k^\perp\cap S^2\), both sheets lie in the octant, giving the stated square-root boundary coefficient.

**3. Shape inequality and reflection.** Direct calculation gives
\[
 N^2=a^2(c^2-b^2)^2+b^2(c^2-a^2)^2+c^2(b^2-a^2)^2,
\]
\[
 b^2(c^2-a^2)^2-a^2(c^2-b^2)^2-c^2(b^2-a^2)^2
 =(b^2-a^2)(c^2-b^2)(a^2+c^2)>0.
\]
Hence \(q^2>1/2\), as required. The two candidates in step 2 are interchanged by the orthogonal reflection \(R=I-2kk^{\mathsf T}\), and therefore are simultaneously in the octant exactly when \(u\in O\cap RO\). Since \(L\) has rank two, two is the maximum number of absolute-coordinate preimages. The sets with a zero coordinate or \(s=1\) have spherical area zero.

**4. Exact spherical-hexagon solid angle.** The intersection \(O\cap RO\) consists of the unit vectors satisfying six linear inequalities \(e_i\cdot u\ge0\) and \((Re_i)\cdot u\ge0\) for \(i=1,2,3\). It has a strictly positive interior, since the positive vector \(v/\|v\|\) is fixed by \(R\). For \(p,r>0\) and \(q^2>1/2\), checking intersections of the six bounding great circles yields exactly six feasible vertex-normal pairs:
\[
 (e_1,Re_1),\ (e_1,Re_2),\ (e_2,Re_1),\ (e_2,Re_3),\ (e_3,Re_2),\ (e_3,Re_3).
\]
For completeness, intersections of two unreflected coordinate planes give coordinate axes, none feasible (the middle axis fails because \(1-2q^2<0\), and the outer axes have a negative reflected outer coordinate). The two-reflected-plane intersections are their reflected images and also fail. Among the nine mixed pairs, \((e_1,Re_3)\), \((e_2,Re_2)\), and \((e_3,Re_1)\) are infeasible: imposing the first plane forces, respectively, the second nonnegative constraint to be strictly positive unless the candidate is zero. The remaining six mixed pairs yield positive nonzero rays. Convexity of the intersection cone proves that this is a geodesically convex spherical hexagon.

The six exterior turning angles are the angles between the relevant inward normals. They are
\[
 2\arcsin p,\quad \arccos(2pq),\quad \arccos(2pq),\quad
 \arccos(2qr),\quad \arccos(2qr),\quad 2\arcsin r.
\]
Spherical Gauss–Bonnet (or Girard's formula) makes its area \(2\pi\) minus their sum, namely
\[
 \operatorname{area}(O\cap RO)=2\left[\arcsin(2pq)+\arcsin(2qr)-\arcsin p-\arcsin r\right].
\]
Dividing by \(\operatorname{area}(O)=\pi/2\) gives \(P_{\mathrm{amb}}\).

**5. Strictness and sharp range.** The positive vector \(v/\|v\|\) lies in the interior of \(O\cap RO\), so \(P_{\mathrm{amb}}>0\). The middle coordinate of \(Re_2\) equals \(1-2q^2<0\); a neighborhood of \(e_2\) in \(O\) therefore fails the reflected-octant condition, giving \(P_{\mathrm{amb}}<1\). For \((1,t,t^2)\) with \(t\to\infty\), the normalized components satisfy \(p=r\to0\), \(q\to1\), and the arcsine formula tends to zero. If \(b\downarrow a<c\), then \(k\to(-1,1,0)/\sqrt2\), and \(R\) becomes the coordinate swap \(u_1\leftrightarrow u_2\), leaving the octant invariant; hence the ambiguity probability tends to one. The analogous conclusion holds for \(a<b\uparrow c\).

## Verification

The accompanying `checker.py` numerically checks the six-vertex cone enumeration, reproduces the spherical-hexagon area independently by oriented spherical-triangle solid-angle triangulation, verifies both inverse branches, and compares the predicted exact ambiguity probability with \(2^{17}\) deterministic quasi-Monte-Carlo spherical samples for each of six distinct side triples. The checker reports six agreement checks within \(0.0025\), with much smaller observed discrepancies. Its numerical tests are diagnostics only: the preceding analytic steps prove the law for all real \(0<a<b<c\).

## Relationship to prior work

Finch, *Width Distributions for Convex Regular Polyhedra* (public 2011), computed regular-solid width moments; the cubic case is a one-variable marginal, not this two-measurement inverse law. Finch, *Planar Projections and Second Intrinsic Volume* (public 2012), studies the paired **projected area and projected perimeter** for regular solids, including the cube; its visible calculations and Section 5 do not give the joint area–axial-width distribution for triaxial boxes or the exact ambiguity solid angle. General Cauchy projection formulas and spherical co-area are used rather than claimed new. Later work on rectangular-box width distributions and width–brightness covariance concerns marginals or low-order dependence, not the explicit six-vertex reconstruction-ambiguity probability shown here. The 2026 study *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability* may contain related general machinery; its full text was not accessible here, so priority beyond the inspected statements is provisional.

## Limitations

This is an exact noiseless inverse-observation statement. It does not prove statistical stability under measurement error, handle arbitrary oblique parallelotopes, or give the joint law for a non-Haar viewing distribution. The density expression is restricted to the pairwise-distinct three-dimensional case; repeated-length limits may change rank or multiplicity and are not claimed as the same density theorem. The reconstructed direction is only specified up to coordinate reflections even in one-preimage regions. Historical priority is provisional pending access to every relevant general source and independent review.

## References

1. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first submitted 2011-10-04, https://arxiv.org/abs/1110.0671 .
2. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464, first submitted 2012-03-12, https://arxiv.org/abs/1203.2464 .
3. O. Abas, *Width distributions for rectangular boxes*, arXiv:2608.03305, first submitted 2026-08-04, https://arxiv.org/abs/2608.03305 .
4. O. Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, first submitted 2026-08-10, https://arxiv.org/abs/2609.26202 .
5. S. Finch, *Planar Projections and Second Intrinsic Volume*, §5, for explicit cube shadow formulas and related projection literature (Reference 2).
