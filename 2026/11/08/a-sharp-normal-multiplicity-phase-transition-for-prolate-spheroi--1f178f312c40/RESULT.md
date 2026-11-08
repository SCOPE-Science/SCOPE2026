# A sharp normal-multiplicity phase transition for prolate spheroids

## Finding
For a prolate solid spheroid
\[
K_r=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2/r^2\le1\},\qquad r>1,
\]
choose \(P\) uniformly in its volume. Let \(N(P)\) count distinct lines through \(P\) normal to the smooth boundary \(\partial K_r\). Almost surely \(N(P)\in\{2,4\}\). Put \(t=r^2\), and write \(p(t)=\Pr(N(P)=4)\). Then
\[
\boxed{p(t)=\begin{cases}
\dfrac{8(t-1)^3}{35t},&1<t\le2,\\[5pt]
\dfrac{8(t-1)^3}{35t}-\dfrac{t^{3/2}(t-2)^{5/2}(8t^2+40t+77)}{35\sqrt{t-1}(t+1)^{7/2}},&t>2.
\end{cases}}
\]
Consequently \(\mathbb E N(P)=2+2p(r^2)\). This mean increases **strictly** and continuously from \(2\) to \(4\) as \(r\) runs from \(1\) to infinity, and therefore uniquely determines the aspect ratio \(r\). At the sharp transition \(r=\sqrt2\), \(p=4/35\); the function of \(t\) is twice but not three times continuously differentiable there. The slender-spheroid law is
\[
\boxed{\Pr(N(P)=2)=15r^{-4}+O(r^{-6}),\qquad \mathbb E N(P)=4-30r^{-4}+O(r^{-6}).}
\]
The spherical endpoint \(r=1\) has \(N(P)=2\) almost surely and is included by continuous extension.

## Assumptions and scope
The boundary normal at \(Q\in\partial K_r\) is the entire Euclidean line \(Q+\mathbb R\nu(Q)\), where \(\nu(Q)\) is its outward unit normal. The sampling measure is three-dimensional Lebesgue volume normalized by \(\operatorname{vol}(K_r)=4\pi r/3\), not surface area; the singular symmetry axis and focal boundary have zero sampling probability. A normal line is counted once for each generic normal foot (distinct feet produce distinct lines almost everywhere). The result is specific to spheroids with two equal *short* axes; it is not a statement about oblate or triaxial ellipsoids.

## Proof
**1. Reduction to an astroid.** At every point \(P=(x,y,z)\) off the axis \(x=y=0\), use a meridian plane containing \(P\) and the revolution axis. Any boundary normal passing through \(P\) is contained in this plane: the dot product with the azimuthal tangent forces the normal foot to have azimuth parallel or antiparallel to that of \(P\). The meridian section is the ellipse with short semiaxis \(1\), long semiaxis \(r\). The normal-stationarity equation in a meridian parameter \((\sin\theta,r\cos\theta)\) is
\[
\rho\cos\theta-rz\sin\theta-(r^2-1)\sin\theta\cos\theta=0,\qquad \rho=\sqrt{x^2+y^2}.
\]
For \(\rho>0\) away from the evolute, the equation has either two or four simple roots, with four exactly in the interior of the evolute astroid; the double-root discriminant parametrization is \((\rho,z)=((r^2-1)\cos^3\theta,(r^2-1)\sin^3\theta/r)\) in the first quadrant. Thus, for \(k=r^2-1\), the four-normal region (modulo a null set) is exactly
\[
\rho\ge0,\qquad (\rho/k)^{2/3}+(r|z|/k)^{2/3}<1,\qquad \rho^2+z^2/r^2<1.
\]
The count is \(2\) elsewhere, almost everywhere.

**2. The sharp intersection transition.** The caustic has maximal radial extent \(k\) at height zero. In normalized coordinates \(u=\rho\), \(v=z/r\), its radial/axial intercepts are \(k\) and \(k/t\). For \(1<t\le2\), the entire revolved astroid lies inside the spheroid (the boundary expression below is convex in \(q\), and its endpoint maximum is \((t-1)^2\le1\)): equivalently, along its parametrization with \(q=\sin^2\theta\in[0,1]\),
\[
\rho^2+z^2/t=k^2\big((1-q)^3+q^3/t^2\big)\le1.
\]
For \(t>2\) there is one nontrivial intersection latitude, because the exact factorization of the boundary equation is
\[
 t^2\Big(k^2((1-q)^3+q^3/t^2)-1\Big)
=-(qt-q-t)^2\big(q(t^2-1)-t(t-2)\big).
\]
The doubled algebraic root \(q=t/k>1\) is inadmissible. The unique physical crossing is
\[
q_*={t(t-2)\over t^2-1}\in(0,1),\qquad
z_*={k\over\sqrt t}\,q_*^{3/2}.
\]
The caustic lies outside the spheroid at low heights \(0\le|z|<z_*\), and inside at larger heights.

**3. Exact volume integration.** By revolution symmetry, the four-normal volume is \(2\pi\int_0^{k/r}\rho_{\max}(z)^2\,dz\). If \(t\le2\), the caustic bounds the entire cross-section and the substitution \(u=rz/k\) gives
\[
 \Pr(N=4)={3k^3\over2t}\int_0^1(1-u^{2/3})^3\,du
 ={3k^3\over2t}\cdot{16\over105}={8k^3\over35t}.
\]
If \(t>2\), the ellipsoid bounds the cross-section up to \(z_*\), and the caustic bounds the rest. Therefore
\[
 p(t)={3\over2\sqrt t}\left[\int_0^{z_*}(1-z^2/t)\,dz+
 \int_{z_*}^{k/\sqrt t}k^2\left(1-(\sqrt t\,z/k)^{2/3}\right)^3dz\right].
\]
Set \(w=\sqrt{q_*}\), and let
\[
 G(w)=w^3/3-3w^5/5+3w^7/7-w^9/9,\qquad G(1)=16/315.
\]
The second height integral equals \(3k^3(G(1)-G(w))/\sqrt t\). Subtracting from the all-caustic expression and factoring \(w^3\) yields
\[
 {8k^3\over35t}-p(t)=w^3{(t-2)(t-1)(8t^2+40t+77)\over35(t+1)^2}.
\]
Substituting \(w^2=t(t-2)/(t^2-1)\) is exactly the claimed radical correction. This computation is algebraic and requires no numerical approximation.

**4. Strict monotonicity and inverse identification.** Map the spheroid volume-preservingly up to scale to the unit ball using \((x,y,z)\mapsto(x,y,z/r)\). Let \(u=\sqrt{x^2+y^2}\), \(v=z/r\). The four-normal condition becomes
\[
 \left({u\over t-1}\right)^{2/3}+
 \left({t|v|\over t-1}\right)^{2/3}<1.
\]
Both coefficients \(1/(t-1)\) and \(t/(t-1)\) decrease strictly in \(t\); thus the four-normal sets strictly increase in relative volume for \(t>1\). Strictness follows from open positive-volume neighborhoods near the moving caustic. For every interior unit-ball point with \(|v|<1\), the condition eventually holds as \(t\to\infty\). Dominated convergence then gives \(p(t)\to1\). This proves strict invertibility of the mean count.

**5. Regularity and slender limit.** The radical subtraction begins at \(t=2\) with coefficient
\[
 p(t)={8(t-1)^3\over35t}-{2\sqrt6\over15}(t-2)^{5/2}+O((t-2)^{7/2})
 \quad (t\downarrow2,\ t>2),
\]
so the second derivative is continuous there but the third derivative is unbounded from the right. For the large-\(r\) tail, write the unit-ball cross-sectional heights as \(v_e(u)=\sqrt{1-u^2}\) and \(v_c(u)=(1-r^{-2})(1-(u/(r^2-1))^{2/3})^{3/2}\). The upper intersection radius obeys \(u_*=2\sqrt2/r+O(r^{-3})\), directly from \(q_*\). The normalized probability deficit is
\[
 1-p(r^2)=3\int_0^{u_*}u\big(v_e(u)-v_c(u)\big)\,du.
\]
Putting \(u=s/r\), uniformly on the resulting bounded interval,
\[
 r^2\big(v_e(s/r)-v_c(s/r)\big)
 =1+{3\over2}s^{2/3}-{s^2\over2}+O(r^{-2})
\]
with the remainder uniformly controlled including \(s=0\). The limiting upper endpoint is \(2\sqrt2\), and
\[
 \int_0^{2\sqrt2}s\left(1+{3\over2}s^{2/3}-{s^2\over2}\right)ds=5.
\]
Hence \(1-p=15r^{-4}+O(r^{-6})\), and the mean formula follows.

## Verification
The accompanying executable `check.py` evaluates the closed form against independent one-dimensional cross-sectional quadrature for eight aspect ratios. Its deterministic volume-uniform sampling test draws 576,000 points in total, and an independent stationarity-root test checks 1,440 sampled meridians against the caustic classification. It also checks the exact transition value and the high-aspect coefficient. These computations corroborate finite numerical instances; the parameter-uniform statements follow from the proof, not the simulation.

## Relationship to prior work
Santaló's mean-normal question and general convex-body bounds are classical. Hug (1995) and Domokos–Lángi (2014) address general mean normal counts, not an explicit three-dimensional prolate-spheroid formula. The planar ellipse astroid is also classical. Aliyev (2023) discusses ellipsoid caustics, including the rotated-astroid classification for surfaces of revolution; this geometric classification is **not** claimed as new. The present contribution is its intersection-volume evaluation, sharp aspect-ratio transition, strict inverse law, and slender-limit coefficient. A previously published planar ellipse mean-normal expression does not give the three-dimensional volume-weighted law.

## Limitations
Only \(r>1\) prolate spheroids and volume-uniform sampling are covered; axis points with infinitely many normal feet have probability zero. No oblate, triaxial, or perturbed-body extension is claimed. Historical novelty is a best-knowledge comparison rather than a proof of exhaustive priority; earlier geometric or integral formulas may subsume components. Independent mathematical review has not been performed.

## References
- D. Hug, *On the Mean Number of Normals Through a Point in the Interior of a Convex Body*, Geometriae Dedicata **55** (1995), 319–340, doi:10.1007/BF01266322; openly accessible author PDF at `https://www.math.kit.edu/stoch/~hug/media/02.pdf`.
- G. Domokos and Z. Lángi, *On the average number of normals through points of a convex body*, arXiv:1406.0813v1, publicly posted 2014-06-03; `https://arxiv.org/abs/1406.0813`.
- Y. N. Aliyev, *Apollonius Problem and Caustics of an Ellipsoid*, arXiv:2305.06065 (2023); `https://arxiv.org/abs/2305.06065`.
