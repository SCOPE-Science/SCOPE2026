# A two-term density-gradient law for rare three-point spherical cap clusters

## Finding
Let \(S^2\) be the unit sphere with geodesic distance \(d\), area measure \(dA\), and its round metric. Let \(f\in C^2(S^2)\) be strictly positive, with \(\int_{S^2}f\,dA=1\). Choose \(X_1,X_2,X_3\) independently with density \(f\,dA\), and let \(E_\varepsilon\) be the event that **some** geodesic cap of radius \(\varepsilon\) contains all three points. Define
\[
I_3(f)=\int_{S^2}f^3\,dA,\qquad
D_3(f)=\int_{S^2}f\,\|\nabla_{S^2}f\|^2\,dA.
\]
For \(\varepsilon\downarrow0\),
\[
\boxed{\Pr_f(E_\varepsilon)=9\pi^2 I_3(f)\varepsilon^4-\pi^2\bigl(4I_3(f)+\tfrac{45}{4}D_3(f)\bigr)\varepsilon^6+o(\varepsilon^6).}
\]
In particular, if \(A_f\) and \(B_f\) denote the coefficients of \(\varepsilon^4\) and \(\varepsilon^6\), respectively, then
\[
\boxed{B_f+\frac49 A_f=-\frac{45\pi^2}{4}D_3(f)\le0,}
\]
with equality exactly when \(f\equiv1/(4\pi)\). The second coefficient therefore identifies a weighted spatial-roughness invariant after the leading cluster-mass integral is removed. Moreover, conditional on \(E_\varepsilon\), the anchor \(X_1\) converges in distribution to density \(f^3/I_3(f)\), and its scaled logarithmic-coordinate offsets for \(X_2,X_3\) converge jointly to the uniform law on
\[
\mathcal D=\{(u,v)\in(\mathbb R^2)^2:\text{the smallest Euclidean disk containing }0,u,v\text{ has radius at most }1\}.
\]
Here \(\operatorname{vol}_4(\mathcal D)=9\pi^2\); the tangent-plane axes can be chosen measurably without changing the rotation-invariant limit. Equivalently, this event is that the spherical covering radius of these three points exceeds \(\pi-\varepsilon\), with equality events negligible.

## Assumptions and scope
The dimension is two, the sphere radius and curvature are one, the three points are independent with the **same** positive normalized \(C^2\) density relative to spherical area, and caps are intrinsic geodesic caps with freely chosen centers. The expansion is for a fixed density as \(\varepsilon\to0\), not a uniform expansion over varying density families. All gradients and Hessians use the round metric. When \(f=1/(4\pi)\), the exact uniform probability, valid for \(0\le\varepsilon\le\pi/2\), is
\[
F_0(\varepsilon)=\frac{(1-\cos\varepsilon)^2(4+5\cos\varepsilon)}4.
\]
This uniform formula is a previously known special case of the large-cap coverage result of Miles, reproduced in Bürgisser--Cucker--Lotz (2010), and is **not** claimed as new. The new statement is the arbitrary-density second coefficient and its weighted-Dirichlet rigidity and local clustering interpretation.

## Proof
**1. The uniform geometric normalization.** By rotation invariance fix \(X_1\). Set \(c=\cos\varepsilon\), \(s=\sin\varepsilon\). The separation \(\theta=d(X_1,X_2)\) has density \(\frac12\sin\theta\). For \(0\le\theta\le2\varepsilon\), the possible cap centers for \(X_1,X_2\) form the spherical convex lens \(L_\theta=B_\varepsilon(X_1)\cap B_\varepsilon(X_2)\). The allowed third points are its geodesic outer parallel set at distance \(\varepsilon\). Define
\[
\beta(\theta)=\arccos\!\left(\cot\varepsilon\tan\frac\theta2\right),\quad
\gamma(\theta)=\arccos\!\left(\frac{\cos\theta-c^2}{s^2}\right).
\]
Spherical triangle geometry gives \(\operatorname{area}(L_\theta)=2\pi-2\gamma-4c\beta\), and its boundary length is \(4s\beta\). The spherical Steiner formula for an outward parallel of this convex lens (valid here since \(0<\varepsilon\le\pi/2\)) gives
\[
\operatorname{area}((L_\theta)_\varepsilon)=
\operatorname{area}(L_\theta)c+\operatorname{length}(\partial L_\theta)s+2\pi(1-c)
=2\pi-2c\gamma-4\cos(2\varepsilon)\beta.
\]
The two angular integrals evaluate to
\[
\int_0^{2\varepsilon}\!\sin\theta\,\beta(\theta)\,d\theta=\pi(1-c),\qquad
\int_0^{2\varepsilon}\!\sin\theta\,\gamma(\theta)\,d\theta=\pi(1-c^2).
\]
For the first, substitute \(t=\tan(\theta/2)/\tan\varepsilon\), integrate by parts, and evaluate the elementary integral \(\int_0^{\pi/2}(1+\tan^2\varepsilon\sin^2u)^{-1}du=\pi c/2\). For the second, substitute \(z=(\cos\theta-c^2)/s^2\). Thus
\[
F_0(\varepsilon)=\frac1{8\pi}\int_0^{2\varepsilon}\sin\theta\,\operatorname{area}((L_\theta)_\varepsilon)\,d\theta
=\frac{(1-c)^2(4+5c)}4
=\frac9{16}\varepsilon^4-\frac14\varepsilon^6+O(\varepsilon^8).
\]
The exact equality also follows from the 2010 published large-cap coverage formula; the lens calculation fixes all normalizations without appealing to it.

**2. The planar cluster moments.** Fix the first point at the origin in \(\mathbb R^2\), and define the four-dimensional indicator \(K_0(u,v)=\mathbf1_{\mathcal D}(u,v)\). For a given \(u\) of norm \(r\le2\), the centers of feasible unit disks form \(L_r=B_1(0)\cap B_1(u)\). Hence the admissible \(v\)-set is exactly \(L_r+B_1\), whose area is, by planar Steiner,
\[
G(r)=2\arccos(r/2)-\frac r2\sqrt{4-r^2}
+4\arccos(r/2)+\pi,\qquad 0\le r\le2.
\]
It follows, by elementary one-dimensional integrations, that
\[
\int_{\mathcal D}du\,dv=2\pi\int_0^2 rG(r)\,dr=9\pi^2,
\quad T:=\int_{\mathcal D}\|u\|^2du\,dv=2\pi\int_0^2r^3G(r)\,dr=15\pi^2.
\]
Indeed, integration by parts and the substitution \(r=2\sin t\) give \(\int_0^2 r\arccos(r/2)\,dr=\pi/2\), \(\int_0^2r^3\arccos(r/2)\,dr=3\pi/4\), \(\frac12\int_0^2r^2\sqrt{4-r^2}\,dr=\pi/2\), and \(\frac12\int_0^2r^4\sqrt{4-r^2}\,dr=\pi\). The domain is invariant under interchanging \(u,v\) and under reanchoring the triangle \((0,u,v)\) at \(u\), which sends \((u,v)\) to \((-u,v-u)\) with Jacobian one. Consequently
\[
\int_{\mathcal D}\|u-v\|^2du\,dv=T,
\qquad \int_{\mathcal D}u\cdot v\,du\,dv=T/2.
\]
Rotational invariance then implies, for any orthonormal tangent basis,
\[
\int_{\mathcal D}u_i u_j\,du\,dv=\int_{\mathcal D}v_i v_j\,du\,dv=\tfrac T2\delta_{ij},
\qquad \int_{\mathcal D}u_i v_j\,du\,dv=\tfrac T4\delta_{ij}.
\]

**3. Localizing the three-point event.** Use spherical exponential coordinates about the first point \(x\): \(X_2=\exp_x(\varepsilon u)\), \(X_3=\exp_x(\varepsilon v)\). On the event both tangent vectors lie in the compact ball \(\|u\|,\|v\|\le2\). Let \(K_\varepsilon(u,v)\) be the exact cap-containment indicator in these coordinates, and let \(j_\varepsilon(u)=\sin(\varepsilon\|u\|)/(\varepsilon\|u\|)\), with value one at zero. For all sufficiently small \(\varepsilon\),
\[
\Pr_f(E_\varepsilon)=\varepsilon^4\int_{S^2}f(x)\!\int K_\varepsilon(u,v)j_\varepsilon(u)j_\varepsilon(v)
 f(\exp_x(\varepsilon u))f(\exp_x(\varepsilon v))\,du\,dv\,dA(x).
\]
By ordinary geodesic scaling \(K_\varepsilon\to K_0\) almost everywhere; the exceptional configurations have planar minimal enclosing radius exactly one and form a null set. Each \(j_\varepsilon\to1\) uniformly on the compact integration domain. Spherical point reflection about \(x\) is an isometry sending \((u,v)\) to \((-u,-v)\), so the entire first-order Taylor term integrates to zero **exactly** for each \(\varepsilon\). The \(C^2\) Taylor expansion is uniform for the compact sphere and these bounded vectors. Its second-order terms are
\[
\frac f2\bigl(\operatorname{Hess}f[u,u]+\operatorname{Hess}f[v,v]\bigr)
+\langle\nabla f,u\rangle\langle\nabla f,v\rangle.
\]
By dominated convergence and the moments in Step 2, the second-order contribution after multiplication by the outside \(f(x)\) is
\[
\frac T2\int_{S^2} f^2\Delta f\,dA+\frac T4\int_{S^2}f\|\nabla f\|^2dA
=-\frac{3T}{4}D_3(f)=-\frac{45\pi^2}{4}D_3(f).
\]
Here integration by parts uses the absence of boundary: \(\int f^2\Delta f=-2\int f\|\nabla f\|^2\).

**4. Curvature contribution without an unproved local-boundary expansion.** Put
\[
M_\varepsilon=\int K_\varepsilon(u,v)j_\varepsilon(u)j_\varepsilon(v)\,du\,dv.
\]
Spherical homogeneity makes this independent of the anchor. Applying Step 3 with the constant density \(f_0=1/(4\pi)\) shows **exactly** that \(F_0(\varepsilon)=\varepsilon^4 M_\varepsilon/(16\pi^2)\). Thus the proven uniform formula in Step 1 gives
\[
M_\varepsilon=9\pi^2-4\pi^2\varepsilon^2+O(\varepsilon^4).
\]
Inserting this exact geometric mass into the leading term \(f^3\), and adding the Step 3 density variation, proves the stated expansion with a uniform \(o(\varepsilon^6)\) remainder for each fixed \(f\). This separation avoids assuming smoothness of the boundary where the two-support and three-support enclosing disks meet.

**5. Rigidity and marked localization.** The displayed coefficient identity follows algebraically. Positivity of \(f\) makes \(D_3(f)=0\) equivalent to \(\nabla f\equiv0\), hence to the unique normalized constant density. Dividing the localized formula by its leading mass \(9\pi^2 I_3(f)\varepsilon^4\) and applying dominated convergence yields the marked conditional convergence: the anchor has density \(f^3/I_3(f)\), and \((u,v)\) has density \(\mathbf1_{\mathcal D}/(9\pi^2)\), independently in the limit.

## Verification
The standalone `CHECK.py` recomputes both four-dimensional planar moments through independent one-dimensional lens quadratures and checks the spherical lens integrals against exact polynomial formulas at five radii. It also checks two distinct anisotropic Legendre families.

For the axial dipole density \(f_a(x)=(1+a x_3)/(4\pi)\), \(|a|<1\), rotational averaging of the cubic product gives the **exact** finite-radius identity
\[
\Pr_{f_a}(E_\varepsilon)=F_0(\varepsilon)+a^2\frac{c(1+c)(1-c)^2(13c+5)}{16},\quad c=\cos\varepsilon.
\]
Expanding it yields \(\frac9{16}(1+a^2)\varepsilon^4-(\frac14+\frac{23}{32}a^2)\varepsilon^6+O(\varepsilon^8)\), agreeing with \(I_3(f_a)=(1+a^2)/(16\pi^2)\) and \(D_3(f_a)=a^2/(24\pi^2)\).

As a second independent angular-mode check, the coefficient of \(a^2\) for \(f(x)=(1+aP_2(x_3))/(4\pi)\), with \(P_2(t)=(3t^2-1)/2\), has the exact expression
\[
\frac{3c(1-c)^2(1+c)(23c^3+7c^2-10c-2)}{80}
=\frac{27}{80}\varepsilon^4-\frac{159}{160}\varepsilon^6+O(\varepsilon^8).
\]
The \(\varepsilon^6\) coefficient follows independently from \(\int f^3\) and \(\int f\|\nabla f\|^2\); these identities are diagnostic calculations, not replacements for the general proof. The script uses only the Python standard library.

## Relationship to prior work
The classical uniform large-cap noncoverage probability was evaluated by Miles and is stated explicitly as formula (3) in Bürgisser, Cucker and Lotz (2010), arXiv:0712.2816; the present proof uses its \(n=3\), \(S^2\) instance only for the homogeneous geometric normalization and also derives that instance independently. Their sample centers are uniform and their integral formula does not imply the arbitrary spatially varying density-gradient correction. Brauchart, Reznikov, Saff, Sloan, Wang and Womersley (first arXiv version 2015) examine independent uniform sphere points, large-sample empty-cap radii, and a nonuniform-density large-\(N\) weighted-hole-radius expectation in Proposition 2.1; those statements do not imply the fixed-three-point nonuniform small-enclosing-cap sixth-order law. Reznikov and Saff (first arXiv version 2015) study large-sample covering-radius asymptotics and general measure bounds, not this fixed-three-point small-containing-cap expansion. A public `spherecover` implementation provides uniform-distribution finite-sample cap statistics, including the classical three-point law, but not spatial-density gradient terms. Fodor, Hug and Ziebarth (2014) treat primary-MSC 52A22 random convex-body approximation under specified densities, not this three-point enclosing-radius rare event. These are genuine neighboring subjects, not sources for a novelty assertion about every possible work. No claim is made of a new uniform-covering formula or a universal extension to arbitrary manifolds.

## Limitations
The coefficient law is local and asymptotic for a fixed positive \(C^2\) density. It does not provide exact finite-radius probabilities for general densities, handle singular or vanishing measures, address dependent samples or higher-dimensional spheres, or give statistical finite-sample estimation guarantees. The remainder is \(o(\varepsilon^6)\) under the stated regularity, not a uniform remainder over all densities. Priority comparisons are necessarily bounded by accessible literature; independent mathematical assessment has not been performed.

## References
1. P. Bürgisser, F. Cucker, M. Lotz, *Coverage processes on spheres and condition numbers for linear programming*, Annals of Probability 38 (2010), 570–604; first arXiv appearance 2007-12-17, arXiv:0712.2816, https://arxiv.org/abs/0712.2816. See equation (3), Theorem 1.1, and their discussion of Miles's formula.
2. F. Fodor, D. Hug, I. Ziebarth, *The volume of random polytopes circumscribed around a convex body*, arXiv:1409.8105 (first posted 2014-09-29), later Mathematika 62 (2016), 283–306; primary MSC 52A22, https://arxiv.org/abs/1409.8105.
3. J. S. Brauchart, A. B. Reznikov, E. B. Saff, I. H. Sloan, Y. G. Wang and R. S. Womersley, *Random Point Sets on the Sphere—Hole Radii, Covering, and Separation*, arXiv:1512.07470 (first posted 2015-12-23); primary classification includes 52A22, https://arxiv.org/abs/1512.07470. See Proposition 2.1 and Theorem 2.2.
4. A. Reznikov, E. B. Saff, *The covering radius of randomly distributed points on a manifold*, arXiv:1504.03029 (first posted 2015-04-12), International Mathematics Research Notices 2016, 6065–6094, https://arxiv.org/abs/1504.03029.
5. *spherecover*, published code and technical notes on finite-sample uniform spherical-cap coverage, https://github.com/gmboquet/spherecover (accessed 2026-11-20 UTC).
