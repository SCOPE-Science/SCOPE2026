# Strict annular-hole monotonicity for sharp affine least-squares projection

## Finding

For each \(0\le a<1\), let \(\Omega_a=\{x\in\mathbb R^2:a\le |x|\le1\}\), with normalized planar area, and let \(P_a\) be real \(L^2(\Omega_a)\)-orthogonal projection onto \(\operatorname{span}_{\mathbb R}\{1,x_1,x_2\}\). Define, for \(z\ge0\),
\[
h(z)=\begin{cases}1,&0\le z\le1,\\ \frac2\pi\left(\sqrt{z^2-1}+\arcsin(1/z)\right),&z>1,\end{cases}
\]
and, for \(q\ge0\),
\[
\Phi(q)=q\,h(\sqrt q)-\frac{2}{3\pi}(q-1)_+^{3/2}.
\]
Set \(t=a^2\), \(A_t=16t/(1+t)^2\), \(B_t=16/(1+t)^2\). The **exact** sharp endpoint operator norm is
\[
\boxed{\Lambda(a)=\|P_a\|_{L^\infty\to L^\infty}=\frac{\Phi(B_t)-\Phi(A_t)}{B_t-A_t}.}
\]
It is strictly decreasing as the hole radius \(a\) increases on \([0,1)\). Precisely the outer-circle evaluation points \(|x|=1\) are norming, including when the inner boundary is present. The exact minimum of \((P_af)(x)\) over \(0\le f\le1\) almost everywhere and \(x\in\Omega_a\) is \((1-\Lambda(a))/2\).

The disk and vanishing-width annulus constants, and their first nonzero corrections, are
\[
\Lambda(0)=\frac{11\sqrt{15}}{8\pi}+\frac2\pi\arcsin\frac14,
\qquad\lim_{a\uparrow1}\Lambda(a)=\frac13+\frac{2\sqrt3}{\pi},
\]
\[
\Lambda(a)=\Lambda(0)-\left(1-\frac{\sqrt{15}}{8\pi}-\frac2\pi\arcsin\frac14\right)a^2+O(a^4)\quad(a\downarrow0),
\]
\[
\Lambda(a)=\frac13+\frac{2\sqrt3}{\pi}+\frac{\sqrt3}{\pi}(1-a)+O((1-a)^2)\quad(a\uparrow1).
\]
In particular, both leading coefficients of norm loss when enlarging the hole are strictly positive.

## Assumptions and scope

The domain is a closed concentric annulus with outer radius one, inner radius \(a\in[0,1)\), and its **area probability** measure; there is no arclength mass on either circle. The functions and projection are real. The output of \(P_a\) is evaluated through its unique continuous affine representative; the essential supremum equals the supremum on the closed annulus. Inputs belong to real \(L^\infty(\Omega_a)\), interpreted as classes modulo area-null sets. For any other positive outer radius, scaling leaves the same formula with \(a\) interpreted as the inner-to-outer radius ratio.

## Proof

**1. Exact reproducing kernel.** Rotational symmetry gives \(\mathbb E_{\Omega_a}X_i=0\), \(\mathbb E X_iX_j=\delta_{ij}(1+a^2)/4\). Hence the affine \(L^2\) projector has kernel
\[
K_a(x,y)=1+\frac{4}{1+a^2}x\cdot y,
\qquad (P_af)(x)=\int_{\Omega_a}K_a(x,y)f(y)\,d\mu_a(y).
\]
Its evaluation norm at \(x\) is \(L_a(x)=\int|K_a(x,y)|d\mu_a(y)\); the operator norm is \(\max_{x\in\Omega_a}L_a(x)\). For fixed \(y\), the angular average of \(|1+z\cos\theta|\) is \(h(z)\) as above, by splitting at its two zero angles. The function \(h\) is even after extending to real \(z\), nondecreasing for \(z\ge0\), and convex; it is strictly increasing for \(z>1\).

**2. Localization of norming points.** By rotational invariance, \(L_a(x)\) depends only on \(r=|x|\) and equals
\[
L_a(r)=\mathbb E_S\,h\!\left(\frac{4rS}{1+a^2}\right),
\]
where \(S^2\) is uniform on \([a^2,1]\). Thus \(L_a(r)\) is nondecreasing in \(r\). Since \(4/(1+a^2)>1\), there is positive mass of radii for which the argument exceeds one at \(r=1\), and the preceding expression is **strictly smaller** whenever \(r<1\). Therefore precisely \(|x|=1\) are norming evaluation locations.

**3. Closed-form norm.** Fix an outer point \(x\) of unit length. The random variable \(Q=(4S/(1+a^2))^2\) is uniform on \([A_t,B_t]\). Set \(g(q)=h(\sqrt q)\). Direct differentiation on \(q>1\), together with constancy on \([0,1]\), gives
\[
g'(q)=\begin{cases}0,&q<1,\\\sqrt{q-1}/(\pi q),&q>1,\end{cases}\qquad \Phi'(q)=g(q).
\]
The derivative of \(\Phi\) matches continuously across \(q=1\). Integrating \(g\) over the uniform interval proves the boxed formula. Strictness of the norming input follows from the sign of the kernel: for an outer unit vector \(u\), the unit-norm extremizers are precisely \(\pm\operatorname{sgn}(1+4u\cdot y/(1+a^2))\), up to null sets.

**4. Strict hole monotonicity.** Write \(\mathcal L(t)=\Lambda(\sqrt t)\). Since \(h\) is convex, for \(q\in[A_t,B_t]\) it lies below its endpoint chord in the variable \(\sqrt q\):
\[
g(q)\le g(A_t)+\frac{\sqrt q-\sqrt{A_t}}{\sqrt{B_t}-\sqrt{A_t}}\bigl(g(B_t)-g(A_t)\bigr).
\]
The uniform mean of the chord coefficient is
\[
\frac{2\sqrt{B_t}+\sqrt{A_t}}{3(\sqrt{B_t}+\sqrt{A_t})}\le\frac23.
\]
Consequently,
\[
\mathcal L(t)<\frac{g(A_t)+2g(B_t)}3,
\qquad 0\le t<1.
\]
The inequality is strict because the interval \([\sqrt{A_t},\sqrt{B_t}]\) has positive length, its upper endpoint is at least two, and \(h\) is not affine on the entire interval. Differentiation of the moving-interval average, using \(A_t'=16(1-t)/(1+t)^3\) and \(B_t'=-32/(1+t)^3\), yields
\[
\mathcal L'(t)=\frac{(3-t)\mathcal L(t)-(1-t)g(A_t)-2g(B_t)}{(1-t)(1+t)}.
\]
The numerator is bounded **strictly** above by
\[
\frac{2t}{3}\bigl(g(A_t)-g(B_t)\bigr)\le0.
\]
Thus \(\mathcal L'(t)<0\) on \([0,1)\); equivalently \(\Lambda\) is strictly decreasing in \(a\).

**5. Endpoints, corrections, and positivity.** At \(a=0\), \((A_t,B_t)=(0,16)\), giving the disk formula. As \(a\uparrow1\), the endpoints coalesce at four and the mean tends to \(g(4)=1/3+2\sqrt3/\pi\). Differentiating at \(t=0\) gives
\[
\mathcal L'(0)=\frac{\sqrt{15}}{8\pi}+\frac2\pi\arcsin\frac14-1<0.
\]
At \(t=1\), the collapsing interval has midpoint \(8/(1+t)\), so its average derivative tends to \(-2g'(4)=-\sqrt3/(2\pi)\). Taylor expansion and \(t=a^2\) give the displayed error laws. Finally, \(\int K_a(x,y)d\mu_a(y)=1\). For \(0\le f\le1\), the minimum at \(x\) is the negative-kernel integral \((1-L_a(x))/2\), attained by the indicator \(f(y)=\mathbf1_{\{K_a(x,y)<0\}}\). Optimizing in \(x\) proves the stated sharp positivity defect.

## Verification

The standalone `checks/annular_projection_check.py` verifies the Gram-derived endpoints and moving-boundary algebra symbolically; independently compares the \(\Phi\)-formula with high-precision direct radial quadrature at ten ratios; and tests the endpoint asymptotics. Its successful diagnostic ends `ALL_ANNULAR_AFFINE_PROJECTION_CHECKS_PASSED`. Finite samples do not certify strict monotonicity for every ratio: the analytical chord/derivative argument above does.

## Relationship to prior work

Hangelbroek–Narcowich–Sun–Ward (arXiv:1005.2424, first public May 13, 2010) establishes broad stability criteria for \(L^2\) projectors onto spaces spanned by localized kernels; its Theorem 5.1 and the sphere example do not contain the present real affine, area-uniform annulus norm or strict hole monotonicity. The known disk constant, recovered at \(a=0\), is not a new claim. A polynomial or Laurent projection on a complex annulus concerns a different function space and projection norm and does not imply this real area-orthogonal statement. Existing full-domain disk and general stability results therefore serve as benchmarks, not proof of the new radial comparison.

## Limitations

No higher-degree polynomial, boundary-arclength, nonconcentric-annulus, complex-valued projector, or irregular perforated domain claim is made. The limiting circle at \(a=1\) is a weak-limit comparison, not an area-probability annulus. The novelty comparison is evidence-based rather than a proof of uniqueness in all literature; older unindexed polynomial-approximation sources remain a bibliographic risk. Independent mathematical validation has not been performed.

## References

- T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424 (first submitted May 13, 2010), https://arxiv.org/abs/1005.2424; Theorem 5.1, Section 5.
- L. Brutman, *On the Polynomial and Rational Projections in the Complex Plane*, SIAM Journal on Numerical Analysis (1979), DOI:10.1137/0717030 (distinct holomorphic annulus projection setting; abstract-level comparison only).
