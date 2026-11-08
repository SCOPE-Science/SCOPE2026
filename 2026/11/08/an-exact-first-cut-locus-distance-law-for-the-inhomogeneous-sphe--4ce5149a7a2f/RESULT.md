# An exact first-cut-locus distance law for the inhomogeneous spherical lens space \(L(5,2)\)

## Finding

Consider the round, curvature-one lens space
\[
M=L(5,2)=S^3/\langle g\rangle,\quad S^3=\{(z_1,z_2)\in\mathbb C^2:|z_1|^2+|z_2|^2=1\},\quad g(z_1,z_2)=(\zeta z_1,\zeta^2 z_2),\quad\zeta=e^{2\pi i/5}.
\]
Let \(X,Y\) be independent normalized-Riemannian-volume-uniform points of \(M\), \(D=d_M(X,Y)\), and \(F(r)=\Pr(D\le r)\). Set
\[
a=\pi/5,\quad b=\tfrac12\arccos(-1/4),\quad F_{\mathrm{sphere}}(r)=\frac5\pi(r-\sin r\cos r),
\]
\[
B_a(r)=(r-a)(1+\cos(2a)+\cos(2r))+\sin(2a)-\sin(2r)-\tfrac12\sin(2(r-a)).
\]
**Theorem.** For every \(0\le r\le b\),
\[
F(r)=\begin{cases}
F_{\mathrm{sphere}}(r),&0\le r\le a,\\
F_{\mathrm{sphere}}(r)-\dfrac{20}{\pi\sqrt5}\,B_a(r),&a\le r\le b.
\end{cases}
\]
The first departure from the spherical-ball law is of exact cubic order:
\[
\lim_{\varepsilon\downarrow0}\frac{F_{\mathrm{sphere}}(a+\varepsilon)-F(a+\varepsilon)}{\varepsilon^3}
=\frac{10(\sqrt5-1)}{3\pi}>0.
\]
Consequently \(F\) is twice continuously differentiable, but not three times differentiable, at the first cut-locus radius \(a\). Its third derivative has a right-minus-left jump of \(-20(\sqrt5-1)/\pi\). The homogeneous lens space \(L(5,1)\), by comparison, first departs at quadratic order, so its distance CDF is only \(C^1\) at this radius.

## Assumptions and scope

Distances are intrinsic Riemannian geodesic distances of the indicated curvature-one quotient, not ambient chord distances. Uniform means normalized Riemannian volume. Radii in the exact formula are bounded by \(b\approx0.911738291\), and \(a\approx0.628318531\). Nothing is claimed for the CDF beyond \(b\), where additional cap overlaps enter. The asserted \(C^2\)/non-\(C^3\) regularity is local at \(a\) only. Singularities at other radii are not classified.

## Proof

**1. Orbit displacements and the Haar coordinate.** Write \(t=|z_1|^2\). For a Haar-uniform \((z_1,z_2)\in S^3\), the variable \(t\) is exactly uniform on \([0,1]\). Put \(c_1=\cos(2\pi/5)\), \(c_2=\cos(4\pi/5)\), \(\Delta=c_1-c_2=\sqrt5/2\). The two nontrivial orbit-distance classes are
\[
 d_1(t)=\arccos(tc_1+(1-t)c_2),\qquad d_2(t)=\arccos(tc_2+(1-t)c_1).
\]
Each class corresponds to one pair of inverse group elements. Every displacement is at least \(2a\), with equality at one of the two Hopf core circles. The classes obey \(d_2(t)=d_1(1-t)\).

**2. Exact inclusion-exclusion window.** The five orbit points make a five-cycle with distances \(d_1\) along cycle edges and \(d_2\) along its complement. Any three distinct orbit points have at least one pair of each class. Since \(\max(d_1(t),d_2(t))\ge\arccos((c_1+c_2)/2)=2b\), there can be no triple intersection among radius-\(r\) balls for \(r<b\). This also holds almost everywhere at \(r=b\) by continuity. The lift of an \(r\)-ball about \([z]\in M\) is the union of five radius-\(r\) balls centered on the orbit. Dividing the union's volume by five gives, when \(r\le b\),
\[
\operatorname{Vol}_M B_M([z],r)=V_3(r)-I(r,d_1(t))-I(r,d_2(t)),\quad V_3(r)=2\pi(r-\sin r\cos r),
\]
where \(I(r,d)\) is the intersection volume of two radius-\(r\) balls in \(S^3\) whose centers are separated by \(d\). The counting is exact: among the ten unordered orbit pairs, five have distance \(d_1\), and five have distance \(d_2\).

**3. Spherical two-ball lens.** For \(0\le d<2r\) and \(r<\pi/2\), parametrizing a neighborhood of the joining great circle by
\[
(\cos\rho\cos u,\cos\rho\sin u,\sin\rho\cos v,\sin\rho\sin v)
\]
gives volume element \(\cos\rho\sin\rho\,d\rho\,du\,dv\). The two constraints imply \(|u|\le r-d/2\) and
\(\cos\rho\ge\cos r/\cos(d/2+|u|)\). Hence direct integration proves
\[
I(r,d)=2\pi\int_0^{r-d/2}\left(1-\frac{\cos^2r}{\cos^2(d/2+u)}\right)du
=2\pi\left[r-\frac d2-\cos^2r\left(\tan r-\tan\frac d2\right)\right].
\]
For \(d\ge2r\), \(I(r,d)=0\). All the relevant radii satisfy \(r\le b<\pi/2\).

**4. Averaging and elementary integration.** The quotient volume is \(\operatorname{Vol}(M)=2\pi^2/5\). Given uniform \(X\), the probability of \(d_M(X,Y)\le r\) equals the quotient-ball volume divided by this total volume. Averaging over uniform \(t\) gives, for \(a\le r\le b\),
\[
F_{\mathrm{sphere}}(r)-F(r)
=\frac5{2\pi^2}\,2\int_0^1 I(r,d_1(t))\,dt
=\frac5{2\pi^2}\,\frac2\Delta\int_{2a}^{2r}I(r,d)\sin d\,dd.
\]
The change of variable uses \(dt=-\sin d\,dd/\Delta\). Substitution of the expression in Step 3 and integration (set \(u=d/2\), use \(\sin d=2\sin u\cos u\)) gives exactly \(20 B_a(r)/(\pi\sqrt5)\). For \(r<a\), no orbit caps overlap and the correction vanishes. Both formulas agree at \(r=a\) and extend continuously to \(r=b\).

**5. Cubic transition and comparison.** Taylor expansion at \(r=a+\varepsilon\) yields
\[
B_a(a+\varepsilon)=\frac43\sin^2a\,\varepsilon^3+O(\varepsilon^4).
\]
Using \(\sin^2(\pi/5)=(5-\sqrt5)/8\) proves the displayed cubic coefficient, and the one-sided third-derivative jump follows. For \(L(5,1)\), the known homogeneous formula gives the deviation \(\frac5\pi\tan(a)\varepsilon^2+O(\varepsilon^3)\); thus the first-branch smoothness differs.

## Verification

The accompanying executable `checker.py` evaluates the elementary formula and, separately, a high-precision one-dimensional integral involving the spherical two-ball overlap. Their values agree at six test radii to at least 55 decimal places. The same code simulates 2,000,000 independently sampled Haar pairs on \(S^3\), computes each quotient distance directly by minimizing over all five deck-group translates, and compares empirical CDF values at six radii, with six-standard-deviation-plus-tolerance checks. It also verifies convergence of the cubic quotient. It prints `LENSSPACE_FIRST_CUT_LOCUS_LAW_OK` on success. These computations check the algebra and sampling numerically; the universal claim rests on Steps 1–5.

## Relationship to prior work

Aurich and Lustig (2012) study inhomogeneous spherical lens spaces through deck transformations and Voronoi cells, motivated by cosmic topology; they do not derive this pair-distance CDF. Balch, Peterson and Shonkwiler (2020), *Distributions of Distances and Volumes of Balls in Homogeneous Lens Spaces*, provide exact laws for \(L(n,1)\), including \(L(5,1)\), and display Monte Carlo histograms for \(L(5,2)\) but explicitly restrict their analytical results to the homogeneous family; their conclusion identifies analytical laws for nonhomogeneous spaces as a possible direction. Thus the present nonhomogeneous first-overlap interval is not an implication of their homogeneous theorem, although the same quotient-sphere setup is standard.

## Limitations

This is an exact partial CDF through the initial cap-overlap regime, not a full all-radius distribution on \(L(5,2)\). The normalization assumes round curvature \(+1\); rescaling changes radii and the cubic coefficient dimensionally. No claim of independent expert verification or comprehensive historical novelty is made. Older non-indexed accounts of spherical quotient ball volumes remain a priority risk.

## References

1. R. Aurich and S. Lustig, *How well-proportioned are lens and prism spaces?*, arXiv:1201.6490v1, publicly posted 2012-01-31. https://arxiv.org/abs/1201.6490
2. B. Balch, C. Peterson, and C. Shonkwiler, *Distributions of Distances and Volumes of Balls in Homogeneous Lens Spaces*, arXiv:2004.13196v1, publicly posted 2020-04-27. https://arxiv.org/abs/2004.13196
