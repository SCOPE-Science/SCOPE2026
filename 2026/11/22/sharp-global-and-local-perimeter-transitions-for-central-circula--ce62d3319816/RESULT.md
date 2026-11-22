# Sharp global and local perimeter transitions for central circular-cylinder sections

## Finding

Let \(C_{R,H}=\{(x,y,z)\in\mathbb R^3:x^2+y^2\le R^2,\ |z|\le H/2\}\), where \(R,H>0\), and let \(P(\theta)\) be the Euclidean perimeter of its section by a plane through the center whose normal makes angle \(\theta\in[0,\pi/2]\) with the cylinder axis. Put \(h=H/(2R)\) and \(h_0=\pi/2-1\). Then

\[
\min_{0\le\theta\le\pi/2}P(\theta)
=\min\{2\pi R,\ 4R+2H\}=4R\min\{\pi/2,1+h\}.
\]

Every global minimizer is axial (the section plane contains the cylinder axis) when \(0<h<h_0\); every global minimizer is perpendicular to the axis when \(h>h_0\); exactly these two kinds minimize at \(h=h_0\). In particular, no strictly oblique central section globally minimizes perimeter.

There is a separate, sharp **local** stability threshold: the axial section is a strict local minimum if \(0<h<1\) and a strict local maximum if \(h\ge1\). The perpendicular-to-axis section is always a strict local minimum. At the axial critical aspect \(h=1\), with \(w=\cot^2\theta\),
\[
P(\theta)=8R-\frac{R}{3}w^2+O_R(w^3)
\qquad(\theta\uparrow\pi/2).
\]
Thus the local transition occurs at \(H=2R\), while the global transition occurs at \(H=(\pi-2)R\).

The exact perimeter is analytic in \(\theta\) away from the cap-contact angle \(\theta_c=\arctan h\), is continuously differentiable across that angle, and has a sharp one-sided \(3/2\)-order contact loss relative to the analytic full-ellipse extension. More precisely, if \(P_{\mathrm{ell}}(\theta)\) denotes the complete ellipse perimeter,
\[
P_{\mathrm{ell}}(\theta)-P(\theta)
=\frac{2^{5/2}R(1+h^2)^{5/2}}{3h^{3/2}}
(\theta-\theta_c)^{3/2}+O_{R,h}((\theta-\theta_c)^{5/2})
\quad(\theta\downarrow\theta_c,\ \theta>\theta_c).
\]
Consequently the section perimeter is not twice differentiable at cap contact.

## Assumptions and scope

All sections are intersections of the *solid* finite right circular cylinder with two-dimensional affine planes **through the center**. The section perimeter includes its straight portions on the end caps. Up to rotation around the axis and reflection, the plane has equation \(z=-x\tan\theta\). The angle \(\theta=0\) gives the horizontal disk, and \(\theta=\pi/2\) the axial rectangle. There is no randomness and no assumption about the relative magnitude of \(H\) and \(R\).

## Proof

**1. Exact perimeter.** Set \(t=\tan\theta\) for \(0<\theta<\pi/2\). Use dimensionless transverse coordinate \(X=x/R\). The section has \(X^2+(y/R)^2\le1\) and \(|X|\le k\), where \(k=\min(1,h/t)\). On an elliptical quarter-boundary put \(X=\sin\varphi\), \(y/R=\cos\varphi\), and \(z/R=-t\sin\varphi\). Its line element is \(R\sqrt{1+t^2\cos^2\varphi}\,d\varphi\). The four symmetric boundary arcs, together with two straight end-cap chords if \(k<1\), yield
\[
P(\theta)=4R\left[\int_0^{\arcsin k}
\sqrt{1+t^2\cos^2\varphi}\,d\varphi+\sqrt{1-k^2}\right].\tag{1}
\]
At \(t\le h\), one has \(k=1\) and the entire ellipse; its perimeter is strictly larger than \(2\pi R\) for \(t>0\), since the integrand strictly exceeds one on a set of positive measure. At the endpoints, \(P(0)=2\pi R\), \(P(\pi/2)=4R(1+h)\).

**2. Sharp global lower bound.** Consider \(t>h\), so \(k=h/t\in(0,1)\), and put \(\alpha=\arcsin k\). In (1), substitute \(x=\sin\varphi\). The arc integral becomes \(\int_0^k\sqrt{t^2+(1-x^2)^{-1}}\,dx\). The integral triangle inequality for the Euclidean norm gives
\[
\int_0^k\sqrt{t^2+\frac1{1-x^2}}\,dx
\ge\sqrt{(tk)^2+\left(\int_0^k\frac{dx}{\sqrt{1-x^2}}\right)^2}
=\sqrt{h^2+\alpha^2}.
\]
Therefore
\[
\frac{P(\theta)}{4R}\ge g_h(\alpha):=
\sqrt{h^2+\alpha^2}+\cos\alpha.\tag{2}
\]
For \(\alpha\in(0,\pi/2)\), the sign of \(g_h'(\alpha)\) is the sign of \(\alpha\cot\alpha-h\). The function \(\alpha\cot\alpha\) decreases strictly from one to zero, because its derivative has numerator \(\sin\alpha\cos\alpha-\alpha<0\). Hence \(g_h\) has no interior minimum and
\[
g_h(\alpha)\ge\min\left\{1+h,\sqrt{h^2+\pi^2/4}\right\}.\tag{3}
\]
If \(h\le h_0\), then \(1+h\le\pi/2\), so the second member in (3) is strictly larger than \(1+h\); hence \(P(\theta)\ge4R(1+h)\). If \(h\ge h_0\), the function \(g_h(\alpha)\) is increasing in \(h\), and (3) at \(h_0\) gives \(g_h(\alpha)\ge g_{h_0}(\alpha)\ge1+h_0=\pi/2\). All finite strictly oblique clipped cases are in fact strict, because the vector integrand in the integral triangle inequality changes direction on a positive-length interval. Including the full-ellipse and endpoint cases proves the claimed minimum and **all** equality orientations.

**3. Endpoint local stability.** In a sufficiently small neighborhood of \(\theta=0\) the section is a complete ellipse. Taylor expansion of (1) gives
\[
P(\theta)=2\pi R+\frac{\pi R}{2}\theta^2+O_{R,h}(\theta^4),
\]
so the horizontal section is always a strict local minimum. Near \(\pi/2\), put \(w=\cot^2\theta=1/t^2\). For \(t>h\), the substitution \(u=tx\) in the arc integral gives the independent exact representation
\[
\frac{P(\theta)}{4R}
=\int_0^h\sqrt{1+\frac{w}{1-u^2w}}\,du+\sqrt{1-h^2w}.\tag{4}
\]
For fixed \(h>0\), expansion at \(w=0^+\) yields
\[
P(\theta)=4R(1+h)+2Rh(1-h)w
+R\left(\frac{2h^3}{3}-\frac h2-\frac{h^4}{2}\right)w^2
+O_{R,h}(w^3).\tag{5}
\]
The \(w\)-coefficient is positive for \(h<1\) and negative for \(h>1\). At \(h=1\) it vanishes but the quadratic \(w\)-coefficient equals \(-R/3\), proving the endpoint classification.

**4. Cap-contact singularity.** Let \(P_{\mathrm{ell}}(t)=4R\int_0^{\pi/2}\sqrt{1+t^2\cos^2\varphi}\,d\varphi\). For \(t>h\), set \(a=\sqrt{1-h^2/t^2}\). The missing ellipse arcs minus the end-cap chord lengths equal
\[
P_{\mathrm{ell}}(t)-P(t)
=4R\int_0^a\left[\sqrt{\frac{1+t^2v^2}{1-v^2}}-1\right]dv
=\frac{2R}{3}(1+t^2)a^3+O_{R,h}(a^5).\tag{6}
\]
As \(t\downarrow h\), \(a^2=2(t-h)/h+O_h((t-h)^2)\); as \(\theta\downarrow\theta_c\), \(t-h=(1+h^2)(\theta-\theta_c)+O_h((\theta-\theta_c)^2)\). Substitution yields the asserted positive \(3/2\)-power coefficient. The correction is zero on the left and has zero first derivative but unbounded negative second derivative on the right, proving the claimed regularity.

## Verification

Running `python3 check_section.py` with the Python standard library performs deterministic quadrature comparisons against **independent Euclidean polygonal arclengths**, checks the strict global bound at a broad collection of angles and heights, and tests the analytic tangency and side-on expansions. It prints `PASS: 1344 independent numerical assertions` in the supplied environment. The proof of the global minimum and exponents is analytic; floating-point checks are diagnostic, not a substitute for the inequalities, Taylor expansions, or equality classification.

## Relationship to prior work

Finite-cylinder sections are classical: a plane sufficiently near horizontal produces an ellipse; when it encounters the end caps, that ellipse is clipped by two parallel chords. Steven R. Finch's *Oblique Circular Cones and Cylinders* (arXiv:1212.5946, first posted December 24, 2012) studies oblique-cylinder surface area and mean width and the circumference of a perpendicular ellipse, not the orientation optimization of finite centered **plane-section perimeter**. Dirksen, *Hyperplane Sections of Cylinders* (arXiv:1602.07854v1, first posted February 25, 2016), gives the exact ellipse-versus-truncated-ellipse geometry and a sharp **maximum area** transition for central cylinder sections (Lemma 2.1 and Theorem 3). Its full primary text treats area, not the present perimeter global minimum, equality cases, local angle stability, or contact singularity. Previously published work on affine random-cylinder sections addresses cap incidence probabilities rather than the perimeter of a centered section. A least-perimeter theorem for centered cuboctahedron sections concerns a different polytope; its oblique minimizer does not imply the present axial/perpendicular classification. These distinctions do not constitute a historical uniqueness theorem; the exact priority of this combined perimeter optimization and cap-contact law remains open to independent assessment.

## Limitations

Only centered planes through a finite **right circular** cylinder are covered; neither displaced planes nor noncircular/oblique cylinders are classified. The theorem identifies global minimizers and local behavior at the two endpoints, but does not classify all interior critical points or prove global uniqueness of a possible interior maximum. The cap-contact expansion is for fixed \(R,h>0\), and is not uniform as \(h\to0\) or \(h\to\infty\). No independent mathematical validation has been performed.

## References

1. S. R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946 (first version December 24, 2012), https://arxiv.org/abs/1212.5946 . Background on elliptic section perimeters and related cylinder geometry.
2. H. Dirksen, *Hyperplane Sections of Cylinders*, arXiv:1602.07854v1 (first posted February 25, 2016), https://arxiv.org/abs/1602.07854 . Exact central-section **area** law and its maximum, distinct from the present perimeter minimum.
3. L. A. Santaló, *Integral Geometry and Geometric Probability*, Addison-Wesley, 1976. General geometric-background reference; not asserted to contain the present theorem.
