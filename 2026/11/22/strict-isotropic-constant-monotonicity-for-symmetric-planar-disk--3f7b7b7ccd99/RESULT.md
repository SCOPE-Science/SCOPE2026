# Strict isotropic-constant monotonicity for symmetric planar disk lenses

## Finding
For \(0\le a<1\), let \(K_a\subset\mathbb R^2\) be the intersection of the two closed unit disks centered at \((a,0)\) and \((-a,0)\). If \(U_a\) is uniform by area on \(K_a\), define the affine-invariant planar isotropic constant by
\[
L(K_a)^4=\frac{\det\operatorname{Cov}(U_a)}{\operatorname{area}(K_a)^2}.
\]
Then \(a\mapsto L(K_a)^4\) is **strictly increasing on \((0,1)\)** and satisfies the sharp family-specific inequality
\[
\boxed{\frac{1}{16\pi^2}\le L(K_a)^4<\frac9{1400}.}
\]
Equality on the left occurs exactly at \(a=0\), the disk; the right bound is not attained by a nondegenerate lens, but is the isotropic constant of the affine-rescaled parabolic lens \(\{(X,Y):|X|+Y^2\le1\}\). The exact expression is the product of the two moment formulas given below. In particular, separation of the generating centers is completely ordered by this **affine-invariant covariance determinant**, not merely by the covariance eigenvalue ratio.

## Assumptions and scope
The separation of the unit-disk centers is \(2a\); \(a<1\) ensures positive area. For two disks of any common radius, the same values hold with \(a\) interpreted as half their center separation divided by that radius. At \(a=1\) the unscaled intersection degenerates to a point; the right endpoint is only a limit of full-dimensional bodies or, equivalently, the invariant of the indicated affine blow-up. The body is symmetric under both coordinate reflections, so its centroid vanishes and its covariance is diagonal. The result concerns uniform two-dimensional **interior** measure, not boundary sampling, a polar volume product or covariance anisotropy alone.

## Proof
**1. Exact moments.** Set \(s=\sqrt{1-a^2}\) and \(\theta=\arccos a\). A point \((x,y)\) belongs to both disks precisely when \(|x|\le1-a\) and \(|y|\le\sqrt{1-(a+|x|)^2}\). Thus its area and its unnormalized axial and transverse second moments are
\[
\begin{aligned}
A&=4\int_a^1\sqrt{1-u^2}\,du=2(\theta-as),\\
X&=4\int_a^1(u-a)^2\sqrt{1-u^2}\,du
=\frac{3(1+4a^2)\theta-as(13+2a^2)}6,\\
Y&=\frac43\int_a^1(1-u^2)^{3/2}\,du
=\frac{3\theta+as(2a^2-5)}6.
\end{aligned}
\]
Every integral is positive for \(0\le a<1\). The covariance eigenvalues are \(X/A\) and \(Y/A\), so \(F(a)=L(K_a)^4=XY/A^4\). These expressions may be differentiated in the open interval, using \(\theta'=-1/s\) and \(s'=-a/s\).

**2. Reduce strictness to one trigonometric inequality.** Direct differentiation and collection give
\[
F'(a)=\frac{-4a}{9sA^5}\,P(\theta),
\]
where, with \(a=\cos\theta\), \(s=\sin\theta\),
\[
\begin{aligned}
P(\theta)={}&-9\theta^3s+18\theta^2a^5-18\theta^2a^3
+2\theta a^6s-45\theta a^4s+21\theta a^2s+22\theta s\\
&+6a^7-54a^5+90a^3-42a.
\end{aligned}
\]
Consequently it suffices to prove \(P(\theta)<0\) for \(0<\theta<\pi/2\). This sign is delicate: the Maclaurin series vanishes identically through degree \(14\), so a plot or a low-order sign test would not suffice.

**3. Rational certificate for all angles.** Elementary trigonometric product-to-sum identities rewrite \(P\) as
\[
\begin{aligned}
32P(\theta)={}&-159\cos\theta+243\cos3\theta-87\cos5\theta+3\cos7\theta\\
&+\theta(697\sin\theta-93\sin3\theta-85\sin5\theta+\sin7\theta)\\
&+\theta^2(-72\cos\theta+36\cos3\theta+36\cos5\theta)
-288\theta^3\sin\theta.
\end{aligned}
\]
Write the Taylor polynomial through degree \(44\) as \(T_{44}(\theta)=\sum_{m=8}^{22}c_m\theta^{2m}\). The first eight even coefficients vanish **exactly**; the first four nonzero ones are
\[
c_8=-\frac{64}{55125},\quad c_9=\frac{1312}{1819125},\quad
c_{10}=-\frac{25304}{118243125},\quad
c_{11}=\frac{302476}{7449316875}.
\]
Put \(b=121/49\), \(z=\theta^2\) and \(H(z)=c_8+c_9z+c_{10}z^2+c_{11}z^3\). The quadratic \(H'\) has positive leading coefficient, positive value at zero and discriminant
\[
-\frac{4490550016}{26691833527734375}<0.
\]
Thus \(H\) is increasing for nonnegative \(z\), and direct rational evaluation yields
\[
H(z)\le H(b)=-\frac{5858491732}{79673152820625}<0\qquad(0\le z\le b).
\]
For each even \(m\in\{12,14,16,18,20\}\), exact rational coefficient arithmetic verifies \(c_m<0<c_{m+1}\) and \(b c_{m+1}<-c_m\); also \(c_{22}<0\). Grouping these terms into five negative pairs and a negative final term gives
\[
T_{44}(\theta)\le\theta^{16}H(\theta^2)
\quad\text{whenever}\quad 0<\theta\le11/7.
\]
To control all subsequent terms, use Taylor's theorem with the fact that every derivative of sine or cosine is bounded in absolute value by one. In the Fourier expansion, each summand \(q\theta^p\sin(k\theta)\) or \(q\theta^p\cos(k\theta)\) contributes at most \(|q|k^{45-p}\theta^{45}/(45-p)!\) after truncation at total degree \(44\). Let \(E\) be the sum of these twelve explicit nonnegative rational bounds; the supplied verifier reconstructs them exactly and checks
\[
E(11/7)^{29}<\frac{5858491732}{79673152820625}.
\]
Because \(\theta<\pi/2<11/7\), it follows that
\[
P(\theta)\le\theta^{16}\bigl(H(b)+E(11/7)^{29}\bigr)<0.
\]
This is a continuum sign proof with exact rational bounds; finite sampling is not used to infer the sign. Hence \(F'(a)>0\) for every \(0<a<1\).

**4. Sharp endpoints.** At \(a=0\), the disk has \(A=\pi\), \(X=Y=\pi/4\), so \(F(0)=1/(16\pi^2)\). At the other end set \(\varepsilon=1-a\) and apply \((x,y)\mapsto (x/\varepsilon,y/\sqrt{2\varepsilon})\). Its image satisfies
\[
|u|\le1,\qquad v^2\le(1-|u|)\left(1-\frac\varepsilon2(1-|u|)\right).
\]
It converges in Hausdorff distance to \(C=\{(u,v):|u|+v^2\le1\}\). The corresponding zeroth and second interior moments converge by dominated convergence to
\[
\operatorname{area}(C)=\frac83,\quad
\int_Cu^2\,du\,dv=\frac{64}{105},\quad
\int_Cv^2\,du\,dv=\frac8{15}.
\]
The affine invariance and continuity of \(L^4\) under convergence to a full-dimensional compact convex body give \(F(a)\to (64/105)(8/15)/(8/3)^4=9/1400\). Strict monotonicity establishes both sharp bounds and equality conditions.

## Verification
Run `python verify.py` in the directory containing this report (Python 3 with `sympy` and `mpmath`). The verifier independently reconstructs every Fourier coefficient from power-to-sum identities, checks the Taylor vanishing and all rational coefficient comparisons, proves the rational remainder strictly smaller than the negative margin, checks the derivative and moment identities symbolically, and compares the three closed moment formulas to 28 high-precision one-dimensional quadratures. It also checks the exact limiting beta integrals. In the supplied execution, **150 assertions passed**, including the all-angle rational sign certificate. The mathematical proof is above; sampled values alone do not establish a theorem.

## Relationship to prior work
K. Bezdek, *Volumetric bounds for intersections of congruent balls* (first public version 2019-12-11), studies lens extremality under volume and intrinsic-volume constraints, not isotropic constants or the separation-dependent covariance-determinant quotient. S. R. Finch, *Mutually Equidistant Spheres that Intersect* (2013), provides three-dimensional lens volume, area and mean-width formulas, not the present planar determinant monotonicity. C. Kipp, *Isotropic constants and regular polytopes* (first posted 2024-07-01), studies local extremality conditions, especially for polytopes and zonotopes, without this lens theorem.

A publicly available 2026 mathematical note, *Sharp covariance anisotropy law for symmetric Euclidean ball lenses* (identifier `dbb6d001c487`), gives exact **individual uniform-volume covariance eigenvalues** and a monotonicity theorem for their **ratio** in all dimensions. Its formulas do allow the displayed moments to be recovered (so the formulas alone are not novel). But strict monotonicity of the normalized determinant \(XY/A^4\) does not follow from monotonicity of the eigenvalue ratio: the two eigenvalues and area have competing variations. The separate all-angle sign certificate is the new assertion here. Another available 2026 note, *Sharp Mahler-product monotonicity of symmetric planar circular lenses* (identifier `b079d50aa217`), orders area times **polar area** in the reverse direction, a distinct functional not implying the covariance-determinant monotonicity. Searches of published mathematical records for normalized inertia determinant, isotropic constant and circular-lens aliases returned no stronger covering statement; this is bounded, provisional priority evidence, not proof of absolute novelty.

## Limitations
This theorem concerns **only** the intersection of two congruent planar Euclidean disks with uniform interior measure. It does not prove an analogous law for unequal radii, intersections of three disks, or balls in higher dimension. It does not imply that every nested family of convex bodies has increasing isotropic constant. The classical disk-minimality inequality by itself provides the lower bound, but not strict monotonicity or the sharp upper bound. A historically unindexed mechanical-inertia calculation could contain an equivalent derivative inequality; priority remains provisional pending independent literature review. No independent mathematical validation has been performed.

## References
1. K. Bezdek, *Volumetric bounds for intersections of congruent balls*, arXiv:1912.05118v1 (2019-12-11), https://arxiv.org/html/1912.05118v1 .
2. S. R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515v1 (2013-01-23), Section 1, https://arxiv.org/html/1301.5515v1 .
3. C. Kipp, *Isotropic constants and regular polytopes*, arXiv:2407.01353v1 (2024-07-01), https://arxiv.org/abs/2407.01353 .
4. *Sharp covariance anisotropy law for symmetric Euclidean ball lenses*, publicly available mathematical finding (2026-11-01), identifier `dbb6d001c487`.
5. *Sharp Mahler-product monotonicity of symmetric planar circular lenses*, publicly available mathematical finding (2026-11-02), identifier `b079d50aa217`.
