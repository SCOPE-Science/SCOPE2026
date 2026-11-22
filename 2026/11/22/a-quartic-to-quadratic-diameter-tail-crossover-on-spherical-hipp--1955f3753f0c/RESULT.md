# A quartic-to-quadratic diameter-tail crossover on spherical hippopedes

## Finding
Let \(E(m)=\int_0^{\pi/2}\sqrt{1-m\sin^2\theta}\,d\theta\) be the complete elliptic integral of the second kind, with **parameter** \(m\). Put
\[
C_b=\{(x,y,z):x^2+y^2+z^2=4,\ (x-b)^2+y^2=(2-b)^2\},\qquad 0<b\le1.
\]
Let \(D_b\) be the Euclidean distance between two independent points drawn uniformly with respect to the full arclength measure (counting both arcs at the node). The diameter is \(4\), and \(L_b=8\sqrt{2(2-b)}E(b/2)\).

**Fixed-shape law.** For every fixed \(0<b<1\),
\[
\Pr(D_b>4-\delta)=C(b)\delta+o_b(\delta),\qquad
C(b)=\frac{\pi(4-3b)}{16(2-b)\sqrt{b(1-b)}E(b/2)^2}.
\]

**Critical crossover and marked limit.** Fix \(\kappa\ge0\), and set \(b_\delta=1-\kappa\sqrt\delta\) for sufficiently small \(\delta>0\). Define
\[
\Omega_\kappa=\{(U,V)\in\mathbb R^2:U^2+(V^2-\sqrt2\kappa)^2<1\}.
\]
Then
\[
\boxed{\lim_{\delta\downarrow0}\delta^{-3/4}\Pr(D_{b_\delta}>4-\delta)
=F(\kappa):=\frac{2^{-15/4}}{E(1/2)^2}\operatorname{area}(\Omega_\kappa).}
\]
For each fixed \(\kappa\), conditioned on the near-diameter event, the ordered branch label is an independent fair binary mark, while the rescaled local sum/difference coordinates have a joint **total-variation** limit uniform on \(\Omega_\kappa\). The crossover region is connected for \(0\le\kappa<1/\sqrt2\) and has two components for \(\kappa\ge1/\sqrt2\). Its area is explicitly
\[
A(\kappa)=4\int_{\sqrt{\max(0,\sqrt2\kappa-1)}}^{\sqrt{\sqrt2\kappa+1}}
\sqrt{1-(v^2-\sqrt2\kappa)^2}\,dv.
\]
Moreover \(A(\kappa)\sim\pi/(2^{1/4}\sqrt\kappa)\) as \(\kappa\to\infty\), so \(F(\kappa)\sim\pi/(16E(1/2)^2\sqrt\kappa)\). These are *sequential* asymptotic limits; no uniformity in unbounded \(\kappa\) is asserted.

## Assumptions and scope
The curves are understood as immersed closed spherical curves, possibly with a transverse node; the parameterization is counted once by arclength, with the node itself of measure zero. The sphere radius is exactly \(2\); scaling all coordinates by \(R/2\) changes the distance deficit proportionally. Each endpoint is sampled independently, not through invariant random affine lines or a uniform parameter. For the critical window, \(\kappa\) is fixed before \(\delta\downarrow0\).

A full regular parameterization with \(0\le t<4\pi\) is
\[
\gamma_b(t)=\left(b+(2-b)\cos t,\ (2-b)\sin t,\ 2\sqrt{b(2-b)}\sin(t/2)\right).
\]
Its speed is \(\sqrt{(2-b)^2+b(2-b)\cos^2(t/2)}\), and integration gives \(L_b\). Every sampled point lies on the sphere of radius \(2\), so the maximum distance is at most \(4\); antipodal sampled configurations below attain \(4\).

## Proof
**1. Exact antipodal set and fixed-shape law.** For an antipodal pair \(P,-P\) to belong to \(C_b\), subtracting the two cylinder equations forces \(x(P)=0\). The four possibilities for \(0<b<1\) are
\[
P=(0,\pm 2\sqrt{1-b},\pm2\sqrt b).
\]
They constitute two unordered pairs, hence four ordered pairs. Write \(h=4(1-b)\), and use the signed \(x\) coordinate near one pair. The local arcs are
\[
P(x)=\bigl(x,\sigma\sqrt{h+2bx-x^2},\tau\sqrt{4b-2bx}\bigr),\quad
Q(y)=\bigl(y,-\sigma\sqrt{h+2by-y^2},-\tau\sqrt{4b-2by}\bigr),
\]
for signs \(\sigma,\tau\). Let \(K_b=b^2/h+b/4=b/[4(1-b)]\). Taylor expansion gives
\[
|P(x)+Q(y)|^2=(x+y)^2+K_b(x-y)^2+O_b((|x|+|y|)^3).
\]
The arclength densities in \(x,y\) converge to \(\sqrt{1+K_b}\). Since for points on the radius-two sphere \(|P-Q|^2=16-|P+Q|^2\), the event \(D_b>4-\delta\) is equivalent to \(|P+Q|^2<8\delta-\delta^2\). The ellipse \((x+y)^2+K_b(x-y)^2<8\delta\) has \((x,y)\)-area \(4\pi\delta/\sqrt{K_b}\). Compactness localizes all near-diameter pairs to exactly the four ordered antipodal pairs. Summing their weighted local areas yields
\[
\Pr(D_b>4-\delta)\sim\frac{16\pi(1+K_b)}{L_b^2\sqrt{K_b}}\delta
=\frac{\pi(4-3b)}{16(2-b)\sqrt{b(1-b)}E(b/2)^2}\delta.
\]
The estimates are valid for each fixed \(0<b<1\), not uniformly up to \(b=1\).

**2. Quartic unfolding.** For \(b\uparrow1\), the two unordered antipodal pairs coalesce into the single north–south pair of the Viviani member \(C_1\). For a north-first ordered pair write
\[
 t_N=\pi+s,\qquad t_S=3\pi+w,\qquad u=(s+w)/2,\quad v=(s-w)/2.
\]
Put \(r=2-b\). The following identity is **exact**:
\[
\gamma_b(\pi+s)+\gamma_b(3\pi+w)
=(2b-2r\cos u\cos v,\ -2r\sin u\cos v,\ -4\sqrt{br}\sin(u/2)\sin(v/2)).
\]
For \(b=1-\kappa\sqrt\delta\), rescale
\[
u=\sqrt{2\delta}U,\qquad v=(8\delta)^{1/4}V.
\]
Uniformly for \(U,V\) in fixed compact sets, the squared sum divided by \(8\delta\) tends to
\[
\frac{|\gamma_b(\pi+s)+\gamma_b(3\pi+w)|^2}{8\delta}
\longrightarrow U^2+(V^2-\sqrt2\kappa)^2.
\]
The sphere relation converts the near-diameter event exactly to this sublevel condition up to an additive threshold \(-\delta/8\). Compactness of the original parameter torus and uniqueness of the antipodal pair at \(b=1\) force all qualifying pairs into these two ordered neighborhoods. Within them the exact sum components show \(u=O_\kappa(\sqrt\delta)\), \(v=O_\kappa(\delta^{1/4})\): the second component first bounds \(\sin u\), and the first then bounds \(1-\cos v\). Therefore the rescaled qualifying sets remain in a common compact rectangle. The boundary of \(\Omega_\kappa\) has plane measure zero, so indicator convergence holds in \(L^1\) by dominated convergence.

**3. Constants and total variation.** The Jacobian is \(ds\,dw=2\,du\,dv\), hence each ordered neighborhood contributes a factor \(2\sqrt{2\delta}(8\delta)^{1/4}=2^{9/4}\delta^{3/4}\) times the area integral. There are exactly two ordered neighborhoods. The product of the arclength speeds tends uniformly to \(1\), and \(L_b\to L_1=8\sqrt2E(1/2)\). Consequently the combined coefficient is \(2^{13/4}/L_1^2=2^{-15/4}/E(1/2)^2\). Convergence of these nonnegative normalized densities in \(L^1\) gives the stated conditional total-variation law and independent fair order mark.

**4. Geometric transition and matching.** At \(\kappa<1/\sqrt2\) the defining region crosses \(V=0\); at and above the threshold its two positive and negative \(V\) components are disjoint. Integrating the width in \(U\) gives \(A(\kappa)\). With \(a=\sqrt2\kappa\), substitution \(q=v^2-a\) in its positive \(v\) half gives
\[
A(\kappa)=2\int_{-1}^1\frac{\sqrt{1-q^2}}{\sqrt{a+q}}\,dq
\sim\frac{\pi}{\sqrt a}
\]
for \(a>1\), as \(a\to\infty\). This proves the stated asymptotic and its agreement with \(C(b)\sim\pi/[16E(1/2)^2\sqrt{1-b}]\) as \(b\uparrow1\). At \(\kappa=0\) the area is \(B(1/4,3/2)\), the previously known isolated Viviani critical coefficient; that isolated case is explicitly not claimed as a new theorem.

## Verification
Run `python CHECK.py` with dependencies in `requirements.txt`. The checker evaluates the independent arclength integral, the exact near-pole sum identity, the fixed-parameter constants, the critical limit, and the one-dimensional crossover integral. Direct finite-deficit quadrature at several \(\kappa\) values is compared with the derived asymptotic. Numerical checks corroborate, but do not replace, the above compactness, Taylor, and dominated-convergence proof.

## Relationship to prior work
The 2013 sphere–cylinder treatment by Graefe, Korsch, and Strzys defines the broader Viviani-window family and establishes its geometrical and dynamical context, without stating these near-diameter random-pair laws. Mathematical descriptions of Viviani's curve and hippopedes give parameterizations and lengths rather than the joint critical crossover. **The isolated Viviani curve \(b=1\) is covered by an earlier general theorem on one antipodal pair with parallel tangents (record identifier `6d5d48f1-93dd-4acb-a69c-8314b0c30bf7`): its \(\delta^{3/4}\) law is used only as an endpoint comparison, not a claimed novelty.** That theorem explicitly excludes multiple antipodal pairs and does not cover a parameter-dependent merging of antipodal pairs. Existing ball-interior, Crofton-line, and area-uniform spherical-cap near-diameter laws concern other sampling spaces and do not imply this one-dimensional arclength two-pair crossover. Historical priority beyond the inspected record remains a risk.

## Limitations
All statements use Euclidean distances between independently arclength-uniform points on the stated sphere–cylinder curves; they do not apply to arbitrary arclength densities, invariant random lines or general space curves. The \(0<b<1\) and \(b=1\) results are not uniformly interchangeable, and the critical-window theorem fixes \(\kappa\) before taking the limit. It does not provide a quantitative uniform remainder for unbounded \(\kappa\), nor certify exhaustive historical priority.

## References
- Graefe, E. M., Korsch, H. J., and Strzys, M. P., *Bose-Hubbard dimers, Viviani's windows and pendulum dynamics*, arXiv:1308.3569, first posted 2013-08-16; primary accessible PDF: https://pdfs.assets.alphaxiv.org/1308.3569v3.pdf.
- Wolfram MathWorld, *Viviani's Curve*: https://mathworld.wolfram.com/VivianisCurve.html.
- R. Ferréol, *Hippopede of Eudoxus*: https://mathcurve.com/courbes3d.gb/hippopede/hippopede.shtml.
- Earlier independently established isolated-parameter diameter-tail theorem, record ID `6d5d48f1-93dd-4acb-a69c-8314b0c30bf7` (endpoint comparison only).
