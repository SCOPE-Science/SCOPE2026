# Exact random-shadow law and first spherical-cap contact for the rhombic dodecahedron

## Finding
Let \(K\subset\mathbb R^3\) be the regular rhombic dodecahedron with vertices
\[
\{(\pm1,\pm1,\pm1)\}\;\cup\;\{(\pm2,0,0),(0,\pm2,0),(0,0,\pm2)\}.
\]
For \(U\) uniformly distributed on the unit sphere, let \(B(U)\) be the area of the orthogonal projection of \(K\) onto \(U^\perp\). Let \(a\ge b\ge c\ge0\) be the ordered absolute coordinates of \(U\). Then
\[
B(U)=4(2a+b),\qquad 4\sqrt3\le B(U)\le4\sqrt5.
\]
The eight unit directions \((\pm1,\pm1,\pm1)/\sqrt3\) are exactly the least-bright directions; the twenty-four signed permutations of \((2,1,0)/\sqrt5\) are exactly the most-bright directions.

The complete distribution \(F(x)=\Pr(B(U)\le x)\) is the explicit one-dimensional algebraic quadrature in the proof below. At its endpoints,
\[
F(4\sqrt3+\varepsilon)=\frac{\sqrt3}{8\pi}\varepsilon^2+O(\varepsilon^3),
\]
and the **exact** upper-tail formula is
\[
\Pr(B(U)\ge4\sqrt5-\varepsilon)=\frac3{\sqrt5}\varepsilon
\quad(0\le\varepsilon\le4\sqrt5-6\sqrt2).
\]
The upper-tail interval is maximal among intervals ending at \(4\sqrt5\) on which this single-cap linear formula holds. Put \(b_*=6\sqrt2\) and \(b_+=4\sqrt5\). Immediately below the first contact threshold,
\[
\Pr(B(U)\ge x)=\frac3{\sqrt5}(b_+-x)
-\frac{2^{5/4}\sqrt3}{\pi}(b_*-x)^{3/2}
+O((b_*-x)^{5/2})\qquad(x\uparrow b_*).
\]
Thus the tail has a first-overlap singularity of order \(3/2\) at the **mean projected area** \(\mathbb E B(U)=6\sqrt2\). Conditioned on the event \(B(U)\le4\sqrt3+\varepsilon\), the two normalized successive ordered-coordinate deficits and their remaining slack converge to a uniform Dirichlet\((1,1,1)\) simplex law, with the eight least-bright directions equally weighted.

## Assumptions and scope
All areas are ordinary Euclidean planar areas; the shape is full-dimensional with the specified scale. A viewing direction is Haar-uniform on \(\mathbb S^2\), and antipodal directions represent the same plane. No independent point-sampling or perspective optics is involved. Every asserted asymptotic is for positive real \(\varepsilon\downarrow0\), at fixed \(K\). The CDF uses \(\Pr(B\le x)\); equality conventions have no effect because the law has no atoms.

## Proof
**Facet formula and projection body.** Each of the twelve rhombic facets has area \(2\sqrt2\) and its unit outward normal is one of the twelve signed versions of \((1,1,0)/\sqrt2\) and its coordinate permutations. Cauchy's exact polyhedral projection formula, including the factor \(1/2\), gives
\[
B(U)=\frac12\sum_{\text{facets }f} \operatorname{area}(f)|\langle U,n_f\rangle|
=2\sum_{i<j}(|u_i+u_j|+|u_i-u_j|)
=4(2a+b).
\]
Here \(|v+w|+|v-w|=2\max(|v|,|w|)\). Equivalently, if \(Q\) is the convex hull of the twenty-four signed permutations of \((2,1,0)\), then \(B(U)=4h_Q(U)\). Thus the projection body \(\Pi K\) is precisely \(4Q\), a scaled regular truncated octahedron. This gives a finite cap representation of every superlevel set, not merely its tails.

**Extrema.** Since \(a^2+b^2+c^2=1\) and \(a\ge b\ge c\ge0\),
\[
(2a+b)^2-3=(a-b)(a+5b)+3(b^2-c^2)\ge0,
\]
with equality only when \(a=b=c=1/\sqrt3\). Cauchy–Schwarz gives \(2a+b\le\sqrt5\sqrt{a^2+b^2}\le\sqrt5\), with equality only for \((a,b,c)=(2,1,0)/\sqrt5\). All multiplicities follow by signs and permutations.

**One-dimensional formula for the entire CDF.** Restrict to the Weyl chamber \(u_1\ge u_2\ge u_3\ge0\), which has \(1/48\) of the sphere's area. Apart from its null boundary, set \(s=u_2/u_1\) and \(t=u_3/u_2\), with \(0<s,t<1\). Then
\[
U=\frac{(1,s,st)}{\sqrt{1+s^2+s^2t^2}},\quad
B=\frac{4(2+s)}{\sqrt{1+s^2+s^2t^2}},\quad
\mathrm d\omega=\frac{s\,\mathrm ds\,\mathrm dt}{(1+s^2+s^2t^2)^{3/2}}.
\]
For positive \(x\) and \(0<s\le1\), define the clipped threshold
\[
T_x(s)=\operatorname{clip}_{[0,1]}\left(
\sqrt{\max\left(0,\frac{16(2+s)^2/x^2-1-s^2}{s^2}\right)}\right).
\]
(The value at \(s=0\) can be arbitrary.) At fixed \(s\), the event \(B\le x\) is exactly \(t\ge T_x(s)\). Integrating its spherical Jacobian in \(t\) gives the full exact law
\[
\boxed{F(x)=\frac{12}{\pi}\int_0^1\frac{s}{1+s^2}
\left[\frac1{\sqrt{1+2s^2}}
-\frac{T_x(s)}{\sqrt{1+s^2+s^2T_x(s)^2}}\right]\mathrm ds.}
\]
For \(x\le4\sqrt3\), the formula is zero; for \(x\ge4\sqrt5\), it is one. This is an exact single bounded algebraic integral, not an approximation or a numerical inversion. It yields, for example, the median \(8.57159\ldots\), from deterministic quadrature.

**Lower tail and marked limit.** Write \(s=1-\alpha\), \(t=1-\beta\) near the unique chamber minimum. Direct differentiation of the displayed brightness function gives
\[
B-4\sqrt3=\frac4{\sqrt3}(\alpha+\beta)
+O((\alpha+\beta)^2),\qquad
\mathrm d\omega=\left(\frac1{3\sqrt3}+O(\alpha+\beta)\right)\mathrm d\alpha\,\mathrm d\beta.
\]
The allowed first-order triangle is \(\alpha,\beta\ge0\), \(\alpha+\beta\le\sqrt3\varepsilon/4\), of area \(3\varepsilon^2/32\). Multiplying by the chamber density \(48/(4\pi)=12/\pi\) gives \(\sqrt3\varepsilon^2/(8\pi)+O(\varepsilon^3)\). After dividing \(\alpha,\beta\) by \(\sqrt3\varepsilon/4\), their pair and residual \(1-4(\alpha+\beta)/(\sqrt3\varepsilon)\) converge to uniform area measure on the unit two-simplex, i.e. Dirichlet\((1,1,1)\). Sign-and-permutation symmetry makes all eight minimizing directions equally likely.

**Exact upper tail, maximality, and first overlap.** Let \(\mathcal W\) contain the twenty-four unit signed permutations of \((2,1,0)/\sqrt5\); put \(R=4\sqrt5\). The support identity gives the exact set equality
\[
\{U:B(U)\ge x\}=\bigcup_{w\in\mathcal W}
\{U:U\cdot w\ge x/R\}.
\]
Distinct centers have largest inner product \(4/5\); precisely \(36\) unordered pairs attain it, and the resulting adjacency graph is the triangle-free edge graph of the regular truncated octahedron. Let \(\alpha=\tfrac12\arccos(4/5)\); then \(\sin\alpha=1/\sqrt{10}\) and \(\cos\alpha=3/\sqrt{10}\). The twenty-four caps with angular radius \(\delta=\arccos(x/R)\) have disjoint interiors for \(\delta\le\alpha\), or \(x\ge R\cos\alpha=6\sqrt2\). Each cap has area \(2\pi(1-x/R)\), so its union has probability \(24\cdot2\pi(1-x/R)/(4\pi)=12(1-x/R)\), yielding the asserted exact terminal law. Below this threshold, the 36 nearest-neighbor cap pairs have nonempty open overlaps, so the linear formula strictly overcounts; hence its interval is maximal.

For \(x=b_*-h\) with \(h>0\) small, \(\delta=\alpha+h/(R\sin\alpha)+O(h^2)\). The local geodesic coordinates \((\xi,\eta)\) at a first-pair midpoint give the two-cap overlap, to leading order, as
\[
|\xi|\le (\delta-\alpha)-\frac{\cot\alpha}{2}\eta^2,
\qquad |\eta|\le\sqrt{2\tan\alpha\,(\delta-\alpha)}.
\]
The spherical area of one lens is therefore
\[
\frac83\sqrt{2\tan\alpha}\,(\delta-\alpha)^{3/2}
+O((\delta-\alpha)^{5/2})
=\frac{2^{5/4}}{3\sqrt3}h^{3/2}+O(h^{5/2}).
\]
For small \(h\), nonadjacent caps do not meet and there are no triple intersections. Subtracting all \(36\) lenses from the sum of cap areas and dividing by \(4\pi\) gives the stated \(2^{5/4}\sqrt3/\pi\) correction. In particular, the upper-tail distribution is differentiable at \(b_*\), but its second derivative is unbounded from below.

Finally, the mean projection-area identity \(\mathbb E B=\operatorname{area}(\partial K)/4\) yields \(24\sqrt2/4=6\sqrt2=b_*\); the coincidence with the first overlap threshold is exact.

## Verification
`CHECK.py` is a standalone Python 3 program using only the standard library. It independently computes hundreds of actual planar convex-hull projection areas from the fourteen vertices and compares them with the facet and support-function formulas; enumerates all 36 nearest-center pairs; and checks the single-integral CDF numerically against the exact upper law and both asymptotic coefficients. The finite diagnostic replay verifies 1,000 projection/support comparisons, 36 first-neighbor pairs, five upper-tail CDF evaluations, three lower-tail coefficient estimates and three first-overlap coefficient estimates. These tests are not a substitute for the global proofs above. The precise analytic constants rely on the inequalities, Jacobian calculation, and local cap-intersection argument, not Monte Carlo.

## Relationship to prior work
Robert W. Gray's 2007 rhombic-dodecahedron notes give the classical face areas, vertices, and angles, but do not derive this direction-dependent projected-area distribution. Finch's March 12, 2012 *Planar Projections and Second Intrinsic Volume* calculates random shadow moments for the cube, tetrahedron and octahedron and states the general surface-area/mean-projection relation, not this body's complete CDF. Horváth's 2020 survey discusses Cauchy's projection formula and the known fact that the **projection body of a tetrahedron** is a rhombic dodecahedron; this is not the projection body **of** the rhombic dodecahedron or its brightness distribution. Closest comparison topics on random projections of truncated octahedra concern the brightness of that different input body, not the rhombic-dodecahedron shadow law. Exact special-body calculations here should not be confused with the existing general Cauchy formula or general spherical coarea methods, which supply a framework without these constants. No independence or definitive historical priority is asserted.

## Limitations
This result is for the single Euclidean normalization stated above. Other scales follow trivially by multiplying projected areas by squared scale; arbitrary affine stretches do not follow from the isotropic law. The exact CDF is a one-dimensional algebraic quadrature rather than a closed antiderivative. The first-overlap expansion applies locally at \(6\sqrt2\) and does not enumerate every subsequent cap-intersection regime. The median is a reproducible numerical estimate, not a rigorously certified decimal interval. Priority remains provisional pending wider independent literature review.

## References
1. Robert W. Gray, *Rhombic Dodecahedron*, Encyclopedia Polyhedra notes (copyright 2007, last revision September 5, 2007), https://rwgrayprojects.com/rbfnotes/polyhed/PolyhedraData/RhombicDodeca/RhombicDodecahedron.pdf . The copyright/revision is not used as a verified first-publication date.
2. Steven R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, publicly dated March 12, 2012, https://arxiv.org/abs/1203.2464 .
3. Ákos G. Horváth, *On Convex Bodies that are Characterizable by Volume Function: “Old and Recent Problems for a New Generation”: A Survey*, Arnold Mathematical Journal 6 (2020), https://doi.org/10.1007/s40598-020-00132-0 .
