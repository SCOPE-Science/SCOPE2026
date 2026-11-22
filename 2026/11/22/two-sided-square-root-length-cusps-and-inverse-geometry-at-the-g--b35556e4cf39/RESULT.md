# Two-sided square-root length cusps and inverse geometry at the generalized Viviani node

## Finding

The Euclidean length of the complete intersection of a sphere and an offset circular cylinder has two different, explicitly elliptic square-root deficits at the nodal topology change. Their ratio passes through unity at precisely the classical Viviani aspect ratio and determines the radius ratio. Together with the critical length, it determines both physical radii. The far outer contact has a third exact square-root coefficient.

Let \(K(t)\) and \(E(t)\) denote the complete elliptic integrals of first and second kind with *parameter* \(t\), not modulus:
\[
K(t)=\int_0^{\pi/2}\frac{du}{\sqrt{1-t\sin^2u}},\qquad
E(t)=\int_0^{\pi/2}\sqrt{1-t\sin^2u}\,du.
\]
Define \(F(t)=E(t)-(1-t)K(t)\) for \(0<t<1\).

For \(R>r>0\), put \(d_*=R-r\) and \(m=d_*/R\). The total (not per-component) intersection-curve length satisfies
\[
L(d_*)=8\sqrt{rR}\,E(m).
\]
The two one-sided laws, for \(\varepsilon\downarrow0\), are
\[
\begin{aligned}
L(d_*-\varepsilon)&=L(d_*)-A_-\sqrt\varepsilon+o(\sqrt\varepsilon),\\
L(d_*+\varepsilon)&=L(d_*)-A_+\sqrt\varepsilon+o(\sqrt\varepsilon),\\
A_-&=4R\sqrt{\frac2{R-r}}F(m),\\
A_+&=4R\sqrt{\frac2{R-r}}F(1-m).
\end{aligned}
\]
Both coefficients are strictly positive. They satisfy \(A_->A_+\) if \(r<R/2\), \(A_-=A_+\) if \(r=R/2\), and \(A_-<A_+\) if \(r>R/2\).

The ratio \(\rho=A_-/A_+=F(m)/F(1-m)\) maps \(0<m<1\) continuously and strictly increasingly onto \((0,\infty)\). The two scalar observations \((\rho,L(d_*))\) therefore recover \(m\), then \(R=L(d_*)/[8\sqrt{1-m}E(m)]\), and finally \(r=R(1-m)\).

At the *outer* contact \(d^*=R+r\),
\[
L(d^*-\varepsilon)=4\sqrt{2R}\,E\!\left(\frac{R}{R+r}\right)\sqrt\varepsilon+o(\sqrt\varepsilon).
\]

## Assumptions and scope

The sphere is the two-dimensional surface \(S=\{(x,y,z):x^2+y^2+z^2=R^2\}\), while the cylinder is the infinite lateral surface \(C_d=\{(x,y,z):(x-d)^2+y^2=r^2\}\), where \(R>r>0\), \(d\ge0\). The object whose length is measured is \(S\cap C_d\), not a solid intersection, projected curve, cylinder surface area, spherical enclosed area, or dynamical period. Its length \(L(d)=\mathcal H^1(S\cap C_d)\) counts intersections or nodes only once; a finite number of common points has zero length.

For \(0\le d<d_*\), the intersection is two disjoint closed curves (two circles at \(d=0\)). At \(d=d_*\) these meet in a nodal figure-eight (generalized Viviani/hippopede). For \(d_*<d<d^*\) the intersection is one smooth closed loop; at \(d=d^*\) it reduces to one point, and for \(d>d^*\) it is empty. All asymptotics keep \(R,r\) fixed strictly in the above range.

## Proof

**1. Exact parametrization and critical length.** Use the cylinder angle \(t\):
\[
x=d+r\cos t,\quad y=r\sin t,\quad z=\pm\sqrt{Q_d(t)},\qquad Q_d(t)=R^2-d^2-r^2-2dr\cos t.
\]
Let \(D_d=\{t\in[0,2\pi]:Q_d(t)\ge0\}\). Away from finitely many branch points the two signs give distinct arcs, and the speed of either is
\[
v_d(t)=\sqrt{r^2+\frac{d^2r^2\sin^2 t}{Q_d(t)}}.
\]
Consequently, for \(0<d<d^*\), \(L(d)=2\int_{D_d}v_d(t)\,dt\). At \(d=d_*\), set \(A=rd_*\). Then \(Q_{d_*}(t)=2A(1-\cos t)\) and \(v_{d_*}(t)=\sqrt{r^2+A\cos^2(t/2)}\), with continuous limiting values at the node. Since \(r^2+A=rR\), substituting \(u=t/2\) and using symmetry gives \(L(d_*)=8\sqrt{rR}\,E(A/(rR))=8\sqrt{rR}\,E(m)\).

**2. Local blowup at the node.** Write \(B=2R\) and use \(t=\sqrt{B\varepsilon/A}\,u\) in a signed local angular coordinate near \(t=0\), i.e. near both ends of the angular period. If \(d=d_*-\varepsilon\), then \(Q_d(t)=B\varepsilon+A t^2+O(\varepsilon^2+\varepsilon t^2+t^4)\). The rescaled speed tends pointwise to
\[
v_{<}(u)=\sqrt{r^2+\frac{A u^2}{1+u^2}},\qquad u\in\mathbb R.
\]
If \(d=d_*+\varepsilon\), the sign of the leading constant reverses and the admissible domain tends to \(|u|\ge1\), with
\[
v_{>}(u)=\sqrt{r^2+\frac{A u^2}{u^2-1}},\qquad |u|>1.
\]
The limiting critical speed at the node is \(s=\sqrt{rR}\). Subtracting the critical curve length before rescaling, one obtains
\[
\begin{aligned}
\lim_{\varepsilon\downarrow0}\frac{L(d_*-\varepsilon)-L(d_*)}{\sqrt\varepsilon}&=2s\sqrt{B/A}\,I_<,\\
I_<&=\int_{\mathbb R}\left(\sqrt{1-\frac{m}{1+u^2}}-1\right)du,\\
\lim_{\varepsilon\downarrow0}\frac{L(d_*+\varepsilon)-L(d_*)}{\sqrt\varepsilon}&=2s\sqrt{B/A}\,I_>,\\
I_>&=\int_{|u|>1}\left(\sqrt{1+\frac{m}{u^2-1}}-1\right)du-2.
\end{aligned}
\]
The factor two accounts for both \(z\)-branches, while the term \(-2\) subtracts the critical length of the missing rescaled interval \((-1,1)\). To justify these limits, fix a small angular cutoff \(\gamma>0\). Outside it, the integrand is differentiable in \(d\) and changes by \(O_\gamma(\varepsilon)\). Inside it, rescaling gives convergence on compact subsets of the respective allowed \(u\)-domains. For \(|u|\ge M>2\), the normalized difference from critical speed is bounded by \(C/u^2\) uniformly for sufficiently small \(\varepsilon\) (with an \(O(\varepsilon)\) regular term); near \(|u|=1\) in the plus-displacement branch the bound \(C(|u|-1)^{-1/2}\) is integrable. Split into compact, near-endpoint, and tails, then let \(M\to\infty\), \(\gamma\to0\). These bounds yield the displayed \(o(\sqrt\varepsilon)\) errors and do not assert a uniform remainder in the aspect ratio.

**3. Elliptic evaluation.** Substituting \(u=\tan\theta\) and integrating by parts yields
\[
I_<=-2\big[E(m)-(1-m)K(m)\big]=-2F(m).
\]
For the second integral set \(w=\sqrt{u^2-1}\) on \(u\ge1\). Its half-line expression minus the missing interval becomes
\[
\frac{I_>}{2}=\int_0^\infty\frac{\sqrt{w^2+m}-w}{\sqrt{w^2+1}}\,dw-1.
\]
It equals \(-1\) at \(m=0\); differentiating under the integral for \(0<m<1\) gives \(K(1-m)/2\). The same value and derivative hold for \(mK(1-m)-E(1-m)=-F(1-m)\), hence \(I_>=-2F(1-m)\). Since \(s\sqrt{B/A}=R\sqrt{2/(R-r)}\), the coefficients follow exactly.

**4. Strictness and inverse reconstruction.** The standard elliptic differentiation identities give \(F'(t)=K(t)/2>0\). With \(F(0)=0\), \(F(1)=1\) by continuous extension, \(A_-\) and \(A_+\) are positive. Therefore \(d_*\) is a strict local maximum of \(L\), and \(F(m)/F(1-m)\) is strictly increasing from zero to infinity. Its equality to one is equivalent to \(m=1/2\), i.e. \(r=R/2\); the inverse formulas in Finding follow.

**5. Outer tangency.** Put \(d=R+r-\varepsilon\) and write the cylinder's near-contact coordinate as \(t=\pi+u\). Its common curve obeys
\[
\varepsilon=\frac{R+r}{2Rr}y^2+\frac{z^2}{2R}+o(\varepsilon)
\]
under the scaling \((y,z)=O(\sqrt\varepsilon)\). In rescaled tangential coordinates this converges with derivative control away from the four principal-axis points to an ellipse with semiaxes \(\sqrt{2R}\) and \(\sqrt{2Rr/(R+r)}\). Standard local graph parametrizations around the four axis points give convergence of total arclength after scaling. The limiting ellipse perimeter is \(4\sqrt{2R}E(R/(R+r))\), proving the outer law.

## Verification

The included standalone \(checker.py\) executes deterministic SciPy quadrature, independently sums three-dimensional polygonal chord lengths sampled from the exact sphere-cylinder intersections, checks exact critical values and three independent limiting coefficients for four geometries, and tests coefficient-ratio monotonicity. It passed 79 deterministic assertions. The program tests finite approximations and does not replace the analytic proof or establish the infinite asymptotics on its own. Run with \(python checker.py\) after installing NumPy and SciPy.

Examples: for \((R,r)=(2,1)\), the nodal length is approximately \(15.2807911561\) and the two cusp coefficients both equal \(4.7925609389\). For \((R,r)=(3,1)\) they are approximately \(7.0183949859\) and \(3.2924480040\), respectively. The outer coefficient in the first example is approximately \(10.0894875979\).

## Relationship to prior work

The generalized Viviani-curve parametrization, one/two-loop topology, and node at internal sphere-cylinder tangency are classical and not claimed as new. Graefe–Korsch–Strzys (2013 preprint, later 2014 journal article) derive the same objects and their spherical *enclosed areas*, using them for classical action and dynamical-period calculations. Their full available preprint discusses loop topology in §2.1, area integrals in §2.2, and non-Euclidean-time periods in §3, but does not state the present two one-sided *Euclidean arclength* constants or inverse law. Standard references also record the special classical Viviani curve's length for one fixed configuration. The new claim concerns explicit displacement-variable Euclidean length cusps, their sharp asymmetry reversal, scale recovery and the external-contact coefficient.

## Limitations

No claim is made for \(r\ge R\), noncircular or oblique cylinders, higher-dimensional intersections, random viewing, finite-noise reconstruction, or an aspect-ratio-uniform error term. The asymptotic statements are pointwise in each fixed \(R>r>0\). The formula has not undergone an independent mathematical audit. Historical-priority limitations include inaccessible classical specialist treatments of generalized Viviani curves, particularly W. Kroll's 2005 and 2007 discussions, which could contain related length results.

## References

1. E.-M. Graefe, H. J. Korsch, M. P. Strzys, *Bose-Hubbard dimers, Viviani's windows and pendulum dynamics*, first preprint 2013-08-16, arXiv:1308.3569, https://arxiv.org/abs/1308.3569. Open-access preprint inspected at https://pdfs.assets.alphaxiv.org/1308.3569v3.pdf (especially §§2.1–2.2 and 3).
2. Eric W. Weisstein, *Viviani's Curve*, Wolfram MathWorld, https://mathworld.wolfram.com/VivianisCurve.html; records classical special-case parametrization and length, with reference to A. Gray, *Modern Differential Geometry of Curves and Surfaces with Mathematica* (1997), §8.6.
3. Eric W. Weisstein, *Cylinder-Sphere Intersection*, Wolfram MathWorld, https://mathworld.wolfram.com/Cylinder-SphereIntersection.html; addresses the tangent configuration and cylinder-surface area, not the moving-axis curve-length cusp.
4. F. Lamarche and C. Leroy, *Evaluation of the volume of intersection of a sphere with a cylinder by elliptic integrals*, *Computer Physics Communications* **59** (1990), 359–369, DOI 10.1016/0010-4655(90)90184-3; abstract describes the **solid volume** problem; full text not inspected.
