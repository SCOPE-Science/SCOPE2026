# Universal intersection-area hierarchy of contact-uniform parallelogram inellipses

## Finding

Let \(P\subset\mathbb R^2\) be any nondegenerate closed parallelogram, and fix one of its four sides. For every interior point of that side there is a unique ellipse contained in \(P\) and tangent to all four sides that touches the selected side at that point. Choose \(m\ge 1\) of these ellipses independently by choosing their selected-side tangency points uniformly in Euclidean arclength. If \(I_m\) is their common intersection, then the exact affine-universal normalized mean area is

\[
\boxed{\frac{\mathbb E\operatorname{area}(I_m)}{\operatorname{area}(P)}=\frac14 B\!\left(\frac12,1+\frac m2\right)^2=\frac\pi4\left[\frac{\Gamma(1+m/2)}{\Gamma(3/2+m/2)}\right]^2.}
\]

Consequently the one-ellipse fraction is \(\pi^2/16\), the two-ellipse fraction is exactly \(4/9\), and, as the positive integer \(m\) tends to infinity,
\[
\frac{\mathbb E\operatorname{area}(I_m)}{\operatorname{area}(P)}=\frac\pi{2m}\left(1-\frac{3}{2m}+O(m^{-2})\right).
\]

There is also an elementary exact kernel for every ordered pair of distinct four-side-tangent inellipses. Map \(P\) affinely to \(Q=[-1,1]^2\), choosing the map so the selected side becomes \(x=1\). Write \(E_k\) for the unique inellipse touching that side at \((1,k)\), with \(-1<k<1\). For \(-1<k\le l<1\), set \(\alpha=\arccos k\) and \(\beta=\arccos l\). Then
\[
\boxed{\frac{\operatorname{area}(E_k\cap E_l)}{\operatorname{area}(Q)}=\frac14\left[\beta\sin\alpha+(\pi-\alpha)\sin\beta\right].}
\]

For distinct parameters the two inellipse boundaries cross at exactly four real, transverse points strictly inside the square; the statement transfers affinely to \(P\). This is a family-specific closed formula, not a claim about arbitrary ellipses.

## Assumptions and scope

The parallelogram has positive area and is fixed, and all ellipses are genuine, positive-area ellipses, not degenerate limiting segments. The sampling measure is normalized *Euclidean arclength on one fixed side applied to the tangency point*, not a uniform measure on eccentricity, orientation, center or area. Each chosen tangency point is independent. Area is ordinary planar Lebesgue area. The displayed mean formula holds for every positive integer \(m\), with the same constant for every nondegenerate parallelogram and every choice of fixed side.

A nondegenerate affine map transforms the fixed side's normalized arclength measure into the uniform linear parameter on the corresponding side of \(Q\), and preserves ratios of planar areas. It therefore suffices to work in \(Q\). For any \(k\in(-1,1)\) define
\[
E_k=\{(x,y):x^2-2kxy+y^2\le1-k^2\}.
\]
The covariance matrix \(\begin{psmallmatrix}1&k\\k&1\end{psmallmatrix}\) is positive definite. Its support function is \(h_k(u)=\sqrt{u^\mathsf{T}\begin{psmallmatrix}1&k\\k&1\end{psmallmatrix}u}\), so \(E_k\) is tangent to the square's lines \(x=\pm1\) and \(y=\pm1\). Its contact point with \(x=1\) is exactly \((1,k)\). Conversely every four-side-tangent inellipse has center at the square center, diagonal covariance entries one and some off-diagonal entry \(k\in(-1,1)\); equivalently this is the classical full square-inellipse parametrization. Thus all are counted once and \(K\sim\operatorname{Unif}(-1,1)\).

## Proof

**Point coverage and all-sample intersection.** Complete the square in the parameter:
\[
x^2-2kxy+y^2\le1-k^2\quad\Longleftrightarrow\quad (k-xy)^2\le(1-x^2)(1-y^2).
\]
For \((x,y)\in Q\), set \(s(x,y)=\sqrt{(1-x^2)(1-y^2)}\). The allowed set of contact parameters is the interval \([xy-s,xy+s]\). Crucially this entire interval lies in \([-1,1]\): the Cauchy--Schwarz inequality applied to \((|x|,\sqrt{1-x^2})\) and \((|y|,\sqrt{1-y^2})\) gives \(|xy|+s\le1\). Its length is exactly \(2s\), so a uniformly selected inellipse covers the point with probability
\[
p(x,y)=s(x,y).
\]
Independence of the \(m\) chosen inellipses gives \(\Pr((x,y)\in I_m)=s(x,y)^m\). Tonelli's theorem for the nonnegative indicator yields
\[
\mathbb E\operatorname{area}(I_m)=\int_{-1}^1\!\int_{-1}^1(1-x^2)^{m/2}(1-y^2)^{m/2}\,dx\,dy= B\!\left(\frac12,1+\frac m2\right)^2,
\]
because \(\int_{-1}^1(1-t^2)^{m/2}dt=B(1/2,1+m/2)\). Divide by \(\operatorname{area}(Q)=4\). The evaluations for \(m=1,2\) follow from \(B(1/2,3/2)=\pi/2\) and \(B(1/2,2)=4/3\). For the asymptotics, apply the standard gamma quotient expansion with \(z=m/2\):
\[
\frac{\Gamma(z+1)}{\Gamma(z+3/2)}=z^{-1/2}\left(1-\frac{3}{8z}+O(z^{-2})\right),
\]
and square. Every step is exact for fixed positive integer \(m\); no finite experiment substitutes for the proof.

**Pairwise intersection kernel.** Rotate the square axes orthogonally through \(45^\circ\), taking \(u=(x+y)/\sqrt2\), \(v=(x-y)/\sqrt2\). The ellipse becomes
\[
\frac{u^2}{1+k}+\frac{v^2}{1-k}\le1.
\]
For polar angle \(\theta\) in these coordinates its squared radial function is
\[
\rho_k(\theta)^2=\frac{1-k^2}{1-k\cos(2\theta)}.
\]
Fix \(k<l\), write \(\alpha=\arccos k\) and \(\beta=\arccos l\), so \(0<\beta<\alpha<\pi\). In the first quadrant the two radial functions cross at the unique angle \(\theta_0\in(0,\pi/2)\) satisfying
\[
\cos(2\theta_0)=\frac{k+l}{1+kl},\qquad
\tan\theta_0=\sqrt{\frac{(1-k)(1-l)}{(1+k)(1+l)}}.
\]
(The denominator is positive and \(|k+l|<1+kl\).) The smaller squared radius is \(\rho_k^2\) for \(0\le\theta<\theta_0\) and \(\rho_l^2\) for \(\theta_0<\theta\le\pi/2\). Fourfold radial symmetry therefore gives
\[
\operatorname{area}(E_k\cap E_l)=2\int_0^{\theta_0}\rho_k(\theta)^2\,d\theta+2\int_{\theta_0}^{\pi/2}\rho_l(\theta)^2\,d\theta.
\]
For \(0\le\theta\le\pi/2\), an antiderivative is
\[
\int_0^\theta\rho_c(t)^2\,dt=\sqrt{1-c^2}\,\arctan\!\left(\sqrt{\frac{1+c}{1-c}}\tan\theta\right).
\]
Substitution at \(\theta_0\) gives respectively \(\tfrac12\beta\sin\alpha\) and \(\tfrac12\alpha\sin\beta\), and at \(\pi/2\) gives \(\tfrac\pi2\sin\beta\). This yields the kernel as stated. The case \(k=l\) follows either by continuity or directly from \(\operatorname{area}(E_k)=\pi\sqrt{1-k^2}\).

**Four crossing points and transversality.** If a point lies on both boundaries for \(k\ne l\), subtracting the two defining quadratic equations gives
\[
xy=\frac{k+l}{2},\qquad x^2+y^2=1+kl.
\]
Here \((1+kl)^2-(k+l)^2=(1-k^2)(1-l^2)>0\), so there are exactly four distinct real solutions, obtained as \((\pm a,\pm b)\) and \((\pm b,\pm a)\) with paired signs, where \(a^2,b^2\) are the two distinct positive roots of the corresponding quadratic in the squared coordinates (zero is allowed for one root when \(k+l=0\)). The contact coordinates \(x,y\) lie strictly between \(-1\) and \(1\), since the only ellipse--square boundary contacts are on the four side interiors and the contact parameters differ. The Jacobian determinant of the two boundary polynomials is, up to sign, \(4(l-k)(x^2-y^2)\), nonzero at all four solutions. Thus each crossing is transverse. The argument is invariant under invertible affine maps.

## Verification

The attached `check_overlap.py` independently integrates the radial minimum numerically for 205 distinct parameter pairs and verifies all four algebraic intersection points. It reported maximum absolute overlap discrepancy \(1.12\times10^{-15}\) (displayed precision \(1.1102230246251565\times10^{-15}\)), maximum incidence residual \(3.3306690738754696\times10^{-16}\), and a nonzero transversality determinant in every tested pair. These are diagnostics, not substitutes for the exact proof above. The attached `check_hierarchy.py` independently integrates the factorized beta integrals for \(m\in\{1,2,3,4,5,10,20,100\}\), including the exact fractions at \(m=1,2\). Reproduce with Python 3, NumPy-compatible standard math and SciPy (`scipy.integrate.quad`).

## Relationship to prior work

The classical parametrization of all parallelogram inellipses is prior work: Horwitz, *Ellipses Inscribed in Parallelograms* (first public version, August 3, 2008), especially Lemma 2 and Proposition 1, classifies these ellipses and studies minimal eccentricity and maximal area. That result is used as background, not claimed anew. Horwitz, *Dynamics of ellipses inscribed in quadrilaterals* (May 5, 2015), proves interior-point incidence counts, not the normalized overlap kernel or the contact-uniform all-sample mean-area law. Hughes and Chraibi, *Calculating ellipse overlap areas* (2011), give a general numerical sector/quartic algorithm; the above elementary closed kernel and stochastic hierarchy for this specific tangent family do not follow as stated from that algorithm without additional arguments. Bobenko and Fairley's 2021 paper studies nets of touching inscribed conics and projective combinatorics, not this area distribution.

A previously published mathematical record on random quadrilateral inellipses establishes a stochastic **single-inellipse area** bound for **nonparallelograms** under uniform center sampling; the center is fixed for all inellipses of a parallelogram, while the present sampling measure is a uniform side-contact parameter and the statistic is the area of an intersection of arbitrarily many ellipses. A separate known formula concerns the Mahler product of the intersection of a pair of congruent perpendicular ellipses; that special geometry does not establish the present full two-parameter kernel or the uniform-contact all-sample formula. No claim of exhaustive historical priority is made.

## Limitations

The exact distributional formula requires independent uniformly chosen tangency locations on one fixed side, and ordinary planar area. It does not apply as stated to a generic nonparallelogram, to independent uniform eccentricity or angle parameters, or to arbitrary overlap of two ellipses. The kernel gives pairwise areas, whereas the beta-function formula gives only the expectation, not the complete distribution, of an \(m\)-fold overlap. A general 2024 monograph collecting quadrilateral-inellipse research was identified but its complete text was not accessible for comparison. Independent mathematical audit and exhaustive priority assessment have not been performed.

## References

1. Alan Horwitz, *Ellipses Inscribed in Parallelograms*, arXiv:0808.0297, first posted 2008-08-03. https://arxiv.org/abs/0808.0297
2. Alan Horwitz, *Dynamics of ellipses inscribed in quadrilaterals*, arXiv:1505.01048, first posted 2015-05-05. https://arxiv.org/html/1505.01048v1
3. Gary B. Hughes and Mohcine Chraibi, *Calculating Ellipse Overlap Areas*, arXiv:1106.3787, first posted 2011-06-19. https://arxiv.org/html/1106.3787v1
4. Alexander I. Bobenko and Alexander Y. Fairley, *Nets of Lines with the Combinatorics of the Square Grid and with Touching Inscribed Conics*, *Discrete & Computational Geometry* 66 (2021), 1382–1400. https://doi.org/10.1007/s00454-021-00277-5
5. Alan Horwitz, *Ellipses Inscribed in, and Circumscribed about, Quadrilaterals*, Chapman & Hall/CRC, 2024. https://www.routledge.com/link/link/p/book/9781032622590 (complete content not inspected).
