# Square-root arclength cusps and inverse geometry at a Villarceau torus section

## Finding
Let \(R>r>0\), and let \(L(\beta)\) denote the total Euclidean arclength of the intersection of the *boundary* of the standard circular ring torus with a central plane inclined by \(\beta\in[0,\pi/2]\) to its equatorial plane. Write
\[
a=\sqrt{R^2-r^2},\qquad \beta_*=\arcsin(r/R),
\]
and use *modulus* (rather than parameter) conventions for the complete elliptic integrals:
\[
K(k)=\int_0^{\pi/2}\frac{du}{\sqrt{1-k^2\sin^2u}},\qquad
E(k)=\int_0^{\pi/2}\sqrt{1-k^2\sin^2u}\,du,\qquad
F(k)=E(k)-(1-k^2)K(k).
\]
At the classical Villarceau transition the boundary is the union of two circles of radius \(R\), intersecting at two points, and \(L(\beta_*)=4\pi R\). The following are *sharp two-sided arclength cusp laws*, for \(\epsilon\downarrow0\):
\[
L(\beta_*-\epsilon)=4\pi R-C_-\sqrt\epsilon+o_{R,r}(\sqrt\epsilon),
\quad C_-={8R\over r}\sqrt{2ra}\,F(r/R),
\]
\[
L(\beta_*+\epsilon)=4\pi R-C_+\sqrt\epsilon+o_{R,r}(\sqrt\epsilon),
\quad C_+={8R\over r}\sqrt{2ra}\,F(a/R).
\]
Both coefficients are positive, so the critical section is a **strict local maximum** of total boundary length. They are equal exactly for \(R/r=\sqrt2\); the side with the larger loss reverses there. More strongly, \((C_-,C_+)\) uniquely determines the two radii: writing \(t=r/R\), the ratio
\[
\frac{C_+}{C_-}=\frac{F(\sqrt{1-t^2})}{F(t)}
\]
is strictly decreasing from infinity to zero on \(0<t<1\). After its unique solution \(t\) is obtained, the absolute scale is
\[
R=\frac{C_-}{8\sqrt{2\sqrt{1-t^2}/t}\,F(t)},\qquad r=tR.
\]
This does not claim that the critical section is globally perimeter-maximizing: for example, the equatorial section has the same total arclength \(4\pi R\).

## Assumptions and scope
The ring torus is the boundary of the solid
\[
T_{R,r}=\big\{(x,y,z)\in\mathbb R^3:(\sqrt{x^2+y^2}-R)^2+z^2\le r^2\big\},\quad 0<r<R.
\]
The central plane can be parametrized orthonormally by \((x,y,z)=(u,v\cos\beta,v\sin\beta)\), since rotational symmetry makes its azimuth irrelevant. The measured length is the total one-dimensional Hausdorff measure of \(\partial T_{R,r}\) in this plane, not a projected shadow perimeter, not the area of the solid section, and not the total length with any positive multiplicity at self-crossings. The limiting little-oh is pointwise in fixed nondegenerate radii; no uniformity near \(r/R=0,1\) is claimed.

## Proof
**Exact complete arclength quadrature.** Parametrize the central plane by \(u=\rho\cos\varphi\), \(v=\rho\sin\varphi\), put \(s=\sin\beta\), and define
\[
q(\varphi)=\sqrt{1-s^2\sin^2\varphi},\qquad
w(\varphi)=\sqrt{r^2-R^2s^2\sin^2\varphi}.
\]
On the admissible angular set \(D_\beta=\{\varphi\in[0,2\pi):|R s\sin\varphi|\le r\}\), the two positive radial solutions of the torus equation are \(\rho_\pm=Rq\pm w\); they remain positive because \((Rq)^2-w^2=R^2-r^2=a^2>0\). Therefore the complete total length is the convergent improper integral
\[
L(\beta)=\sum_{\sigma\in\{+,-\}}\int_{D_\beta}
\sqrt{\rho_\sigma(\varphi)^2+(\rho'_\sigma(\varphi))^2}\,d\varphi,
\quad q'=-\frac{s^2\sin\varphi\cos\varphi}{q},\quad
w'=-\frac{R^2s^2\sin\varphi\cos\varphi}{w}.
\tag{1}
\]
For \(Rs\le r\) every ray is admissible, whereas for \(Rs>r\) only the two bands around \(\varphi=0,\pi\) are admissible. At their endpoints \(w=0\), the singular derivatives are integrable (the full curve is smooth away from the transition). At \(\beta=0\), the section is the pair of concentric circles of radii \(R\pm r\), so \(L(0)=4\pi R\). At \(\beta=\pi/2\), it is two circles of radius \(r\), so \(L(\pi/2)=4\pi r\).

**Node normal form.** Eliminating the square root from the torus boundary equation gives the exact section quartic
\[
Q_\beta(u,v)=(u^2+v^2-a^2)^2-4r^2u^2+4k v^2=0,\quad
k=R^2\sin^2\beta-r^2.
\tag{2}
\]
At \(k=0\), this factors as
\[
\big((u-r)^2+v^2-R^2\big)\big((u+r)^2+v^2-R^2\big)=0.
\]
Hence there are two circles with transverse nodes at \((u,v)=(0,\pm a)\). Each has radius \(R\) and the sum of their arclengths is \(4\pi R\). Near either node use scaled variables \(U=ru\), \(V=a(v\mp a)\). Equation (2) becomes
\[
\frac{Q_\beta}{4}=V^2-U^2+a^2k+
O_{R,r}\big((|U|+|V|)^3+|k|(|U|+|V|)\big).
\tag{3}
\]
The plane arclength metric is exactly \(ds^2=r^{-2}dU^2+a^{-2}dV^2\). If \(k>0\), the regularized crossing is the pair of hyperbolas \(U^2-V^2=a^2k\); if \(k<0\), it is \(V^2-U^2=a^2|k|\). Their axes exchange precisely across the topology transition.

**Universal arclength deficit.** For positive \(p,q\), define \(m=\sqrt{p^2+q^2}\) and the convergent improper integral
\[
J(p,q)=\int_1^\infty\left(\sqrt{p^2+\frac{q^2x^2}{x^2-1}}-m\right)dx-m.
\tag{4}
\]
This is the scaled length difference of one outgoing branch of a hyperbola and its asymptotic ray, including the omitted ray from the node to the hyperbola vertex. Setting \(x=\sqrt{1+z^2}\) yields
\[
\frac{J(p,q)}m=\int_0^\infty\frac{\sqrt{z^2+\lambda^2}-z}{\sqrt{1+z^2}}\,dz-1,
\quad \lambda=q/m.
\]
Call the integral on the right \(I(\lambda)\). Since \(I(0)=0\), differentiation under the integral gives \(I'(\lambda)=\lambda K(\sqrt{1-\lambda^2})\). The complete-elliptic derivative identities give \(F'(t)=tK(t)\). Taking \(t=\sqrt{1-\lambda^2}=p/m\) and evaluating the endpoint proves
\[
J(p,q)=-mF(p/m).
\tag{5}
\]
In particular \(J<0\), since \(F'(t)>0\), \(F(0)=0\), and \(t\in(0,1)\).

**Transfer from local model to exact curve.** For each fixed pair \(R>r>0\), choose disjoint neighborhoods of the two transverse nodes. Away from them the quartic boundary is a smooth deformation and contributes \(O_{R,r}(|k|)\) to total length. In each neighborhood the two approaching strands are smooth coordinate perturbations of the hyperbolas in (3), and their tangent metric approaches the fixed diagonal metric. Rescale \((U,V)=a\sqrt{|k|}(\widehat U,\widehat V)\) in the inner region. On every fixed scaled compact interval the difference of exact and model arclengths divided by \(a\sqrt{|k|}\) vanishes by (3) and smoothness. In the outer region the regularized length *difference* relative to the two nodal rays has an integrable \(O(|k|/\text{distance}^2)\) tail, and the cubic-coordinate errors are bounded by \(O_{R,r}(|k|\log(1/|k|))=o_{R,r}(\sqrt{|k|})\). Thus dominated matching establishes the universal leading term (5), with the smooth multiplicative metric perturbations only in the little-oh remainder. There are four outgoing half-branches per node and two nodes. In the \(k>0\) region the longitudinal/transverse metric weights are \((p,q)=(1/r,1/a)\); for \(k<0\), they are \((p,q)=(1/a,1/r)\). With \(a m=R/r\), this gives
\[
\begin{aligned}
L(\beta)-4\pi R&=-\frac{8R}{r}\,a\sqrt{k}\,F(a/R)+o_{R,r}(\sqrt k),&&k\downarrow0,\\
L(\beta)-4\pi R&=-\frac{8R}{r}\,a\sqrt{-k}\,F(r/R)+o_{R,r}(\sqrt{-k}),&&k\uparrow0.
\end{aligned}
\tag{6}
\]
Note carefully that the factor \(a\sqrt{|k|}\) here has length-squared dimension while the metric weights have reciprocal length; the total length dimension is consistent. Finally
\[
k=2ra(\beta-\beta_*)+O_{R,r}((\beta-\beta_*)^2),
\]
which yields the stated \(C_-\) and \(C_+\). Both are strictly positive, proving strict local maximality.

**Sharp equality and shape reconstruction.** The identity \(F'(t)=tK(t)>0\) makes \(F\) strictly increasing, with \(F(0)=0\) and \(F(1)=1\). Hence equality of the two coefficients occurs if and only if \(r=a\), namely \(R/r=\sqrt2\). The quotient \(F(\sqrt{1-t^2})/F(t)\) is strictly decreasing from infinity to zero for \(t\in(0,1)\). It uniquely determines \(t\). Substitution \(a=R\sqrt{1-t^2}\) into \(C_-\) proves the stated scale-reconstruction expression.

## Verification
The supplied self-contained program `checks/torus_section_checker.py` (requires `numpy`, `scipy`) evaluates the *independent exact arclength quadrature* (1), independently approximates selected sections from sampled implicit quartic contours, tests both limits for five nondegenerate radius ratios, compares the analytic elliptic coefficients to numerical approach ratios, checks endpoint lengths, and tests the proposed inverse ordering. Run it using `python checks/torus_section_checker.py`. It passed 174 deterministic assertions at the packaged precision. Numerical experiments test, but do not replace, the analytic derivation. Reproducibility of its specific finite checks does not certify the absence of previous work.

## Relationship to prior work
The Villarceau double-tangent planes and their decomposition into circular sections are classical. Hirsch (2002) analyzes Villarceau sections for surfaces generated by conics, and García Monera and Monterde (2011) derive the tangent-plane geometry and a torus construction from the two circular sections. Moroni (2017) studies general toric-section algebraic forms and special circles. The inspected original texts do not establish the **two-sided total-boundary-arclength square-root coefficients**, their equality transition at \(R/r=\sqrt2\), or reconstruction of \((R,r)\) from those coefficients.

A separate published study, *Logarithmic area cusp and Haar topology law at the Villarceau transition*, derives a \((\beta-\beta_*)\log|\beta-\beta_*|\) singularity for the **area of the solid central section**. That does not imply the present square-root asymptotics for the length of its boundary: the observables and exponents differ, and the inverse length-coefficient result is additional. The earlier sphere-cylinder nodal-length theory concerns another intersection of quadrics with different defining parameters; sharing the hyperbola mechanism does not imply the torus-specific coefficients or their shape inversion. Potential older equivalent geometric-arclength results remain a priority risk.

## Limitations
The local arclength expansion is for a fixed nondegenerate ring torus and central sections. No global maximality of the critical section is asserted, and no statements cover noncentral sections, horn/spindle tori, general surfaces of revolution or numerical stability under noisy estimates. The exact elliptic coefficients are analytic consequences of the given local model, but older obscure material might contain an equivalent result; no independent mathematical audit or conclusive historical priority certification was performed.

## References
1. A. Hirsch, *Extension of the “Villarceau-Section” to Surfaces of Revolution with a Generating Conic*, Journal for Geometry and Graphics **6** (2002). https://www.heldermann-verlag.de/jgg/jgg06/jgg0610.pdf
2. M. García Monera and J. Monterde, *Building a Torus with Villarceau Sections*, Journal for Geometry and Graphics **15** (2011), 93–99. https://www.heldermann-verlag.de/jgg/jgg15/j15h1mone.pdf
3. L. Moroni, *The toric section: intersection of a torus with a plane* (2017). https://www.lucamoroni.it/toric-sections/
4. M. Macho Stadler, *El toro visto por Villarceau*, published 26 November 2011. https://ztfnews.wordpress.com/2011/11/26/el-toro-visto-por-villarceau/
5. *Logarithmic area cusp and Haar topology law at the Villarceau transition* (published 2026), scientific comparison of a distinct section-area statistic. https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-logarithmic-area-cusp-and-haar-topology-law-at-the-villarceau-tr--3f2e0b5e194a/RESULT.md
