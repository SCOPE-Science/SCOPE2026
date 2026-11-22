# Two-jet spheroid reconstruction and distinct thin-limit laws for radial–normal deviation

## Finding
For a Euclidean-surface-area-uniform point on a spheroid, the unsigned angle between its position vector and its outward normal has an exact distribution. More specifically, two *small-angle* coefficients reconstruct the polar-to-equatorial radius ratio, and the two inequivalent ways to make a spheroid thin have different exact beta-driven limiting laws, with different heavy-tail exponents. This distinguishes prolate from oblate shapes without any signed latitude or directional labels.

Let \(r>0\) be the polar/equatorial semiaxis ratio. For \(r\ne1\), put
\[
q=(r-r^{-1})^2,\quad \delta_*=\arctan(\sqrt q/2),\quad U=\frac{\tan\delta}{\sqrt q},\quad 0\le U\le1/2.
\]
Define
\[
w_r(t)=\frac{\sqrt{r^2(1-t)+t}}{\sqrt t},\quad H_r(t)=\int_0^t w_r(s)\,ds,\quad Z_r=H_r(1),
\]
\[
t_\pm(u)=\frac{1\pm\sqrt{1-4u^2}}2.
\]
Then the **complete probability distribution** is
\[
F_r(u):=\Pr(U\le u)=\frac{H_r(t_-(u))+Z_r-H_r(t_+(u))}{Z_r},\qquad 0\le u\le\frac12.
\]
Outside this interval its CDF is zero or one. The primitive is elementary. For \(0<r<1\), with \(k=\sqrt{1-r^2}\),
\[
H_r(t)=\sqrt{t}\sqrt{r^2+k^2t}+\frac{r^2}{k}\operatorname{arsinh}\left(\frac{k\sqrt t}{r}\right).
\]
For \(r>1\), with \(k=\sqrt{r^2-1}\),
\[
H_r(t)=\sqrt t\sqrt{r^2-k^2t}+\frac{r^2}{k}\arcsin\left(\frac{k\sqrt t}{r}\right).
\]
The lower-end expansion has two geometrically distinct terms:
\[
F_r(u)=\frac{2r}{Z_r}u+\frac{1}{Z_r}u^2+O_r(u^3).
\]
Thus if \(A_r=\lim_{u\downarrow0}F_r(u)/u\) and \(B_r=\lim_{u\downarrow0}[F_r(u)-A_ru]/u^2\), then
\[
\boxed{r=\frac{A_r}{2B_r}.}
\]
In particular the unlabeled angular law uniquely determines \(r\ne1\): its upper endpoint determines \(q\), which puts the observed angle on the \(u\)-scale, while the ratio of two lower-end coefficients fixes the direction of the aspect ratio. The case \(r=1\) is characterized by \(\delta=0\) almost surely.

There is also a sharp upper-end probability:
\[
\Pr(\delta>\delta_*-\varepsilon)=\frac{\sqrt{1+r^2}}{Z_r}\sqrt{\frac{4+q}{\sqrt q}}\,\sqrt\varepsilon+O_r(\varepsilon^{3/2}),
\]
for every fixed \(r\ne1\) as \(\varepsilon\downarrow0\).

For extreme shapes, let \(V_{\rm p}\sim\operatorname{Beta}(1/2,1/2)\) and \(V_{\rm o}\sim\operatorname{Beta}(1,1/2)\). Then
\[
r(\pi/2-\delta)\ \Rightarrow\ 2/\sqrt{V_{\rm p}}\quad (r\to\infty),
\]
\[
(\pi/2-\delta)/r\ \Rightarrow\ 2/\sqrt{V_{\rm o}}\quad(r\downarrow0).
\]
Both limiting laws have support \([2,\infty)\), but their CDFs there differ:
\[
F_{\rm p}(y)=1-\frac2\pi\arcsin(2/y),\qquad F_{\rm o}(y)=\sqrt{1-4/y^2},\quad y\ge2.
\]
Their upper tails behave respectively as \(4/(\pi y)\) and \(2/y^2\).

## Assumptions and scope
The object is the embedded spheroid \(E_r=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2/r^2=1\}\), with unit equatorial radius and polar radius \(r>0\). Points are sampled with respect to **ordinary Euclidean surface area**, not uniform latitude or an affine pushforward of sphere-uniform measure. The normal is the Euclidean outward unit normal. All probability claims include every such \(r\), with \(r=1\) explicitly treated separately. Probability boundaries and limits are understood for \(u\in[0,1/2]\), \(y\ge2\), or sufficiently small \(\varepsilon>0\) as stated. A uniformly scaled spheroid has the same angular law.

## Proof
**1. Geometric angle and area Jacobian.** Parametrize the meridian by
\[
X(\theta,\phi)=(\sin\theta\cos\phi,\sin\theta\sin\phi,r\cos\theta),\qquad 0\le\theta\le\pi.
\]
The unnormalized outward normal is \((\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta/r)\). Taking the norm of the cross product of the parameter derivatives gives area element
\[
dA=\sin\theta\sqrt{r^2\sin^2\theta+\cos^2\theta}\,d\theta\,d\phi.
\]
Their scalar product is identically one. Since all vectors lie in a radial–meridian plane and have positive dot product, their acute angle obeys
\[
\tan\delta=|r-r^{-1}|\,|\sin\theta\cos\theta|.
\]
Indeed, the ratio of the magnitude of their meridian-plane determinant to their scalar product is exactly \(|r-r^{-1}|\sin\theta|\cos\theta|\). This identity is unaffected by a common scaling of semiaxes.

**2. Exact pushforward law.** Put \(T=\cos^2\theta\). The two polar hemispheres contribute equally; using \(|d\cos\theta|=\sin\theta\,d\theta\), and normalizing by total area \(2\pi Z_r\), yields
\[
\Pr(T\in dt)=g_r(t)\,dt,\qquad g_r(t)=\frac{w_r(t)}{Z_r},\quad 0<t<1.
\]
The angle identity becomes \(U=\sqrt{T(1-T)}\). For \(0\le u\le1/2\), the event \(U\le u\) consists of the disjoint ranges \(0\le T\le t_-(u)\) and \(t_+(u)\le T\le1\). Integrating the density gives the displayed CDF, including endpoints. Elementary substitution \(t=z^2\) proves both stated primitives, and hence gives a closed elementary law, rather than just a numerical integral.

**3. Two-jet reconstruction.** As \(u\downarrow0\),
\[
t_-(u)=u^2+O(u^4),\qquad 1-t_+(u)=u^2+O(u^4).
\]
For fixed \(r>0\), \(H_r(t_-(u))=2ru+O_r(u^3)\), while \(Z_r-H_r(t_+(u))=u^2+O_r(u^4)\), because \(w_r(1)=1\). Dividing by \(Z_r\) gives the expansion and proves that both coefficients exist and are positive. Their ratio is \(r\). The end value \(\delta_*\) follows by maximizing \(T(1-T)\), with unique maximum at \(T=1/2\). Thus the measured angle law itself specifies the rescaling \(U=\tan\delta/\sqrt q\) and then uniquely reconstructs \(r\). The coefficient linear in \(u\) comes from equatorial sampling, the quadratic term from the two pole neighborhoods.

**4. Maximum-angle deficit.** The density of \(T\) is continuous and positive at \(1/2\), with \(g_r(1/2)=\sqrt{1+r^2}/Z_r\). Near the maximum, \(\Pr(U>u)=\int_{t_-(u)}^{t_+(u)}g_r(t)\,dt=g_r(1/2)\sqrt{1-4u^2}+O_r((1-4u^2)^{3/2})\); cancellation of the odd Taylor term improves the error. With \(u=\tan(\delta_*-\varepsilon)/\sqrt q\), we have \(1-4u^2=(4+q)\varepsilon/\sqrt q+O_r(\varepsilon^2)\). Substitution proves the sharp square-root tail.

**5. Distinct degenerating-shape limits.** First, as \(r\to\infty\), the exact density in step 2 converges in \(L^1[0,1]\) to \((2/\pi)\sqrt{(1-t)/t}\), by dominated convergence and normalizing integrals, i.e. \(T\Rightarrow\operatorname{Beta}(1/2,3/2)\). As \(r\downarrow0\), \(g_r(t)\to1\) for almost every \(t\), also in \(L^1\), so \(T\Rightarrow\operatorname{Uniform}[0,1]\). For either limit, \(\sqrt q\) is asymptotic to \(r\) or \(r^{-1}\) respectively, hence the scaled complement of the angle converges in distribution to \(1/\sqrt{T(1-T)}\). With \(V=4T(1-T)\), its two inverse branches \(t_\pm(v)=(1\pm\sqrt{1-v})/2\) and Jacobian \(|dt_\pm/dv|=1/(4\sqrt{1-v})\) give, in the prolate limit,
\[
f_V(v)=\frac1{\pi\sqrt{v(1-v)}},\qquad0<v<1,
\]
and in the oblate limit,
\[
f_V(v)=\frac1{2\sqrt{1-v}},\qquad0<v<1.
\]
These are exactly the two stated beta densities. Applying the map \(V\mapsto2/\sqrt V\) gives the exact limiting CDFs; expanding the inverse sine and square root at infinity gives their different decay exponents. No interchange of the fixed-shape maximum-angle asymptotic with a thin-shape limit is asserted.

## Verification
The standalone `normal_spheroid_verify.py` checks Cartesian angle identities, closed primitives against direct quadrature, normalizations, local series coefficients and both distinct limiting CDFs. Run `python normal_spheroid_verify.py` with NumPy and SciPy; a verified run returned `PASS 820 deterministic checks`. This finite numerical test corroborates formula implementation but does not replace the preceding all-parameter proof. The exact proof uses only ordinary calculus and beta-variable changes.

## Relationship to prior work
Poelaert, Schniewind and Janssens (2011), *Surface Area and Curvature of the General Ellipsoid*, supply the ellipsoidal surface/normal geometry and deterministic relation between the radius and surface normal, and their full-text area formulas encompass the relevant differential ingredients. No novelty is claimed for spheroidal parametrization, normal/radial angle, or integration of a spheroidal surface patch. Marples and Williams (2023), *Patch area and uniform sampling on the surface of any ellipsoid*, systematically provide general surface-patch integration and exact sampling; this broad machinery can calculate the finite one-dimensional CDF by choosing the appropriate surface patches. The specific object of the finding is the *unsigned two-coefficient inverse reconstruction together with two distinct beta thin-limit classes and their tail exponents*, not the existence of an elementary surface-area integral. Similar published results on multiplicity of normal lines and section radius use different random objects and do not imply the claimed inverse angular jet or paired degenerations without additional analysis. The priority comparison is best-knowledge, not a claim that no equivalent formula exists anywhere.

## Limitations
The result concerns axisymmetric centered spheroids, Euclidean-area sampling and acute radial/normal deviation; it does not cover generic triaxial ellipsoids or nonuniform sampling. The two-jet inverse uses exact limiting CDF coefficients; stability and finite-sample estimation of those coefficients are not established. The thin-limit normalizations differ between prolate and oblate paths, and the fixed-shape endpoint expansion is not uniform in either thin limit. The finite CDF is obtainable by integrating previously known general ellipsoid patch formulas, so any historical-priority claim specifically concerns the stated inverse reconstruction and contrasting limiting laws. Independent verification has not been conducted.

## References
1. D. Poelaert, J. Schniewind and F. Janssens, *Surface Area and Curvature of the General Ellipsoid*, preprint dated 2011-04-27, arXiv:1104.5145, https://arxiv.org/html/1104.5145v1 .
2. C. R. Marples and P. M. Williams, *Patch area and uniform sampling on the surface of any ellipsoid*, *Numerical Algorithms* (2023), DOI:10.1007/s11075-023-01628-4, https://link.springer.com/article/10.1007/s11075-023-01628-4 .
