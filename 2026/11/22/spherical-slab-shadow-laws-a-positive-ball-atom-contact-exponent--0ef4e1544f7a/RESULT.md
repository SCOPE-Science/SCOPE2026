# Spherical-slab shadow laws: a positive ball atom, contact exponents, and an endpoint logarithm

## Finding
For an integer \(d\ge3\) and a relative half-height \(0<a<1\), form the centrally symmetric spherical slab
\[
K_{d,a}=\{x\in\mathbb R^d:\lVert x\rVert\le1,\ |x_d|\le a\},\qquad b=\sqrt{1-a^2}.
\]
Let \(E=n^\perp\) be a Haar-uniform hyperplane, and define the *normalized mean support* of its orthogonal shadow by
\[
W(E)=\frac{1}{|S^{d-2}|}\int_{S^{d-2}\cap E}h_{\operatorname{proj}_E K_{d,a}}(u)\,d\sigma(u).
\]
Since the body is centrally symmetric, this is half its directional mean width. In dimension three, the planar shadow perimeter is exactly \(2\pi W\).

Write \(\theta\in[0,\pi/2]\) for the acute angle between the viewing normal \(n\) and the slab axis, and set \(\theta_c=\arcsin a\). The complete law has a nonzero atom
\[
\Pr(W=1)=I_{a^2}\!\left(\frac{d-1}{2},\frac12\right),
\]
where \(I_x(p,q)\) is the regularized incomplete beta function. Exactly for \(\theta\le\theta_c\), the projected body is the full unit \((d-1)\)-ball, even though \(K_{d,a}\) is not a ball.

Below the atom the law is continuous and uniquely parameterized by \(W=M_{d,a}(\theta)\), where \(M_{d,a}\) is given in the proof below and decreases strictly on \((\theta_c,\pi/2)\). Let
\[
\alpha=\frac{d-2}{2},\qquad
\kappa_{d,a}=\frac{2^\alpha\Gamma((d-1)/2)}{\sqrt\pi\,\Gamma(\alpha+3)}\left(\frac ba\right)^\alpha.
\]
The onset of shadow shrinkage has the sharp dimension-dependent exponent
\[
1-M_{d,a}(\theta_c+\eta)
=\kappa_{d,a}\,\eta^{(d+2)/2}+o_{d,a}(\eta^{(d+2)/2})\quad(\eta\downarrow0).
\]
Consequently the non-atomic mass in a deficit interval obeys
\[
\Pr(0<1-W\le\varepsilon)
\sim g_d(\theta_c)\left(\frac{\varepsilon}{\kappa_{d,a}}\right)^{2/(d+2)},\quad
 g_d(t)=\frac{2\Gamma(d/2)}{\sqrt\pi\Gamma((d-1)/2)}\sin^{d-2}t.
\]
Thus the continuous density has an integrable singularity of exponent \(-d/(d+2)\) next to the atom.

There is a second, dimension-sensitive endpoint phenomenon at the minimum \(w_{d,a}=M_{d,a}(\pi/2)\). When \(d=3\),
\[
w_{3,a}=\frac2\pi\bigl(\arcsin a+b\bigr),\qquad
M_{3,a}(\pi/2-\eta)-w_{3,a}
=\frac b\pi\eta^2\log(1/\eta)+O_a(\eta^2).
\]
Hence
\[
\Pr(w_{3,a}<W\le w_{3,a}+\varepsilon)
\sim\sqrt{\frac{2\pi\varepsilon}{b\log(1/\varepsilon)}}.
\]
For every \(d\ge4\), define the finite positive constant \(L_{d,a}=-\frac{d}{ds}\,M_{d,a}(\arcsin s)|_{s=1^-}\), explicitly specified in the proof. Then
\[
M_{d,a}(\pi/2-\eta)-w_{d,a}=\frac{L_{d,a}}2\eta^2+o_{d,a}(\eta^2),
\quad \Pr(w_{d,a}<W\le w_{d,a}+\varepsilon)
\sim g_d(\pi/2)\sqrt{\frac{2\varepsilon}{L_{d,a}}}.
\]
In \(d=3\) the upper-endpoint perimeter law is the concrete \(5/2\)-power rule
\[
2\pi-P(\theta_c+\eta)\sim\frac{16\sqrt2}{15}\sqrt{\frac ba}\,\eta^{5/2},\qquad
P(\pi/2)=4(\arcsin a+b).
\]

The atom and the upper endpoint also solve an inverse problem: for the physical family \(R K_{d,a}\) of unknown \(R>0\) and \(a\), the largest shadow mean support is \(R\), and the atom mass determines \(a\) uniquely by the strictly increasing beta CDF. In \(d=3\), if the largest observed perimeter is \(P_{\max}\) and its atom mass is \(p\), then
\[
R=\frac{P_{\max}}{2\pi},\qquad
\text{physical slab half-height}=R\sqrt{2p-p^2}.
\]
These are population-distribution identities, not finite-sample estimation guarantees.

## Assumptions and scope
The dimension is an integer \(d\ge3\). The body is the *solid* intersection of a Euclidean unit ball and the centered closed slab \(|x_d|\le a\), with \(0<a<1\) fixed. Hyperplanes are drawn from rotation-invariant probability measure on the Grassmannian \(G(d,d-1)\). A single viewing direction and its negative represent the same hyperplane. All asymptotic constants are for fixed \(d\) and fixed nondegenerate \(a\); no claimed uniformity as \(a\to0\), \(a\to1\), or \(d\to\infty\). The normalized support is distinct from projected \((d-1)\)-volume. In \(d=3\) it equals perimeter divided by \(2\pi\).

## Proof
**1. Constrained support.** For a unit vector \(u\in\mathbb R^d\), write \(t=|u_d|\). Maximizing \(u\cdot x\) over \(K_{d,a}\) first along spheres of fixed last coordinate gives the exact support
\[
H_a(t)=h_{K_{d,a}}(u)=
\begin{cases}
1,&0\le t\le a,\\
a t+b\sqrt{1-t^2},&a<t\le1.
\end{cases}
\]
Indeed the unconstrained unit-ball maximizer is \(x=u\), feasible precisely when \(t\le a\). Otherwise the maximizing last coordinate is the signed slab boundary and the orthogonal component is aligned with that of \(u\). On \(t>a\),
\[
H'_a(t)=a-\frac{bt}{\sqrt{1-t^2}}<0
\]
because its negativity is equivalent to \(t>a\). Further, \(1-H_a(t)>0\) for \(t>a\), and the contact expansion is
\[
1-H_a(a+v)=\frac{v^2}{2b^2}+O_a(v^3)\quad(v\downarrow0).
\]
The exact stable identity \(1-H_a(t)=[bt-a\sqrt{1-t^2}]^2/[1+H_a(t)]\) will also be used for computation.

**2. Hyperplane support quadrature and strictness.** The projection of \(e_d\) onto \(E\) has length \(s=\sin\theta\). If \(U\) is uniform on the unit sphere of \(E\), then \(|U_d|=s|Z|\), where \(Z\) is one coordinate of a uniform point on \(S^{d-2}\). Writing
\[
c_d=\frac{\Gamma((d-1)/2)}{\sqrt\pi\,\Gamma((d-2)/2)},
\]
one obtains the following full profile, with no approximation:
\[
M_{d,a}(\theta)=
\begin{cases}
1,&0\le s\le a,\\
1-2c_d\displaystyle\int_0^{\arccos(a/s)}
 [1-a s\cos\varphi-b\sqrt{1-s^2\cos^2\varphi}]
 \sin^{d-3}\varphi\,d\varphi,&s>a.
\end{cases}
\]
The integrand is nonnegative and is positive except at its upper integration limit. Strict decrease of \(H_a(t)\) for \(t>a\) makes \(M_{d,a}\) strictly decreasing in \(s\in(a,1]\), hence in \(\theta\in(\theta_c,\pi/2]\). The equality of the support to one in every direction of \(E\) is exactly the statement that the shadow is a unit ball. If \(s>a\), positive-measure in-plane directions have support below one, while directions orthogonal to the projected slab axis retain support one; therefore the shadow is not any ball.

**3. The exact Haar law.** By rotational invariance, the acute polar angle has density
\[
g_d(\theta)=\frac{2\Gamma(d/2)}{\sqrt\pi\Gamma((d-1)/2)}\sin^{d-2}\theta,
\quad0<\theta<\pi/2.
\]
Equivalently \(\sin^2\theta\) has distribution \(\mathrm{Beta}((d-1)/2,1/2)\). The plateau \(\theta\le\theta_c\) therefore gives the stated atom. If \(w_{d,a}<x<1\), let \(\theta_x\) be the unique solution of \(M_{d,a}(\theta_x)=x\). The full continuous CDF is explicitly
\[
\Pr(W\le x)=I_{\cos^2\theta_x}\!\left(\frac12,\frac{d-1}{2}\right).
\]
It is zero for \(x\le w_{d,a}\), and jumps to one at \(x=1\). Differentiation and the strictness above show there are no additional atoms in the interior.

**4. Sharp contact onset.** Put \(\alpha=(d-2)/2\) and \(s=a+\delta\). In the equivalent coordinate integral
\[
1-M_{d,a}=2c_d\int_{a/s}^1 [1-H_a(sz)](1-z^2)^{\alpha-1}\,dz,
\]
make the exact change of variables \(z=(a+\delta v)/s\) for \(0\le v\le1\). After factoring out \(\delta^{\alpha+2}\), the integrand tends, uniformly on compact subintervals and with an integrable beta majorant for fixed \(a,d\), to a constant times \(v^2(1-v)^{\alpha-1}\). Thus
\[
1-M_{d,a}=\frac{2^\alpha\Gamma((d-1)/2)}{\sqrt\pi\Gamma(\alpha+3)b^2a^\alpha}\,\delta^{\alpha+2}(1+o(1)),
\]
using \(\int_0^1 v^2(1-v)^{\alpha-1}\,dv=B(3,\alpha)=2\Gamma(\alpha)/\Gamma(\alpha+3)\). Since \(\delta=\sin(\theta_c+\eta)-a=b\eta+O_a(\eta^2)\), the coefficient simplifies to \(\kappa_{d,a}\) and exponent \(\alpha+2=(d+2)/2\). Multiplying the inverse \(\eta\sim(\varepsilon/\kappa_{d,a})^{2/(d+2)}\) by the positive viewing density at \(\theta_c\) proves the continuous probability onset.

**5. The side-on endpoint and the exceptional logarithm.** Write \(\mathcal M(s)=M_{d,a}(\arcsin s)\). For \(d\ge4\), differentiating the coordinate integral is justified at \(s=1^-\) by the integrable endpoint majorant \((1-z)^{(d-5)/2}\). The strict positive endpoint derivative magnitude is
\[
L_{d,a}=2c_d\int_a^1\left(\frac{bz^2}{\sqrt{1-z^2}}-az\right)(1-z^2)^{(d-4)/2}\,dz>0.
\]
The integrand is positive for \(z>a\). Hence \(\mathcal M(s)-\mathcal M(1)=L_{d,a}(1-s)+o(1-s)\). With \(s=\cos\eta=1-\eta^2/2+O(\eta^4)\), the quadratic endpoint follows.

For \(d=3\), use directly the angular formula and differentiate for \(s>a\):
\[
\mathcal M'(s)=\frac2\pi\int_0^{\arccos(a/s)}
\left(a-\frac{bs\cos\varphi}{\sqrt{1-s^2\cos^2\varphi}}\right)\cos\varphi\,d\varphi.
\]
The bounded \(a\)-term and angular ranges away from zero contribute \(O_a(1)\). Near \(\varphi=0\), replace \(1-s^2\cos^2\varphi\) by its leading comparable expression \((1-s^2)+\varphi^2\); the error in the divergent integral is bounded. As \(s\uparrow1\),
\[
-\mathcal M'(s)=\frac b\pi\log\frac1{1-s}+O_a(1).
\]
Integrating once and substituting \(s=\cos\eta\) proves \(M_{3,a}(\pi/2-\eta)-M_{3,a}(\pi/2)=(b/\pi)\eta^2\log(1/\eta)+O_a(\eta^2)\). The explicit minimum follows from \(H_a(\cos\varphi)=a\cos\varphi+b\sin\varphi\) for \(0\le\varphi\le\arccos a\), and one on the remaining interval. Finally the viewing-density endpoint satisfies \(g_3(\pi/2)=1\), so inversion of the logarithmic relation gives the stated \(\sqrt{\varepsilon/\log(1/\varepsilon)}\) probability law. The finite-derivative case similarly gives the square-root endpoint for \(d\ge4\).

**6. Identification.** Scaling the convex body by \(R\) scales every support by \(R\); the largest shadow value is \(R\). Since the regularized beta CDF is strictly increasing in \(a^2\in(0,1)\), the atom probability recovers \(a\) uniquely. In \(d=3\), \(\Pr(W=1)=1-\sqrt{1-a^2}\), yielding \(a=\sqrt{2p-p^2}\). This proves the stated two-parameter inversion within the spherical-slab family.

## Verification
Run `python verify_spherical_slab.py` from the same directory after installing `mpmath`. The checker independently projects grid-sampled curved spherical-zone boundaries into the plane, computes polygon-hull perimeters without a geometry library, and compares those values with the analytic support quadrature. It also checks the beta-atom identity against direct angular integration, the contact coefficients in dimensions \(3,4,5,7\), endpoint laws, and strict monotonicity on deterministic grids. The checker reports 198 passed numerical diagnostics. These are finite diagnostics, not substitutes for the analytic integrals and endpoint majorants proved above.

## Relationship to prior work
Spherical segments and their classical volume/surface-area formulas are recorded by Weisstein, with references back to Smith (1923). Finch (public arXiv version dated March 12, 2012) treats stochastic planar projections and mean widths of regular polytopes, not this truncated spherical body. Vickers and Brown (2001) develop distributions of projected area and perimeter for ellipsoids, cylinders and cones; their accessible treatment was checked for its object families and projection methodology, without relying on an unchecked assertion about every page. The present claim concerns the *specific spherical-slab support distribution*, positive ball-shadow atom, contact coefficient in every dimension, and a dimension-three logarithmic side-on endpoint. No inspected source establishes these statements, but a universal preexisting support/contact result could still contain them implicitly; historical priority is not independently certified.

## Limitations
No assertion is made about asymmetric slabs, oblique or offset cutting planes, perspective projections, non-Euclidean ambient metrics, non-Haar viewing measures, or finite-sample statistical estimation. Fixed-dimensional, fixed-aspect-ratio asymptotics need not be uniform at degenerate slab thicknesses or as dimension grows. The complete law is given by a one-dimensional integral and inverse, not by an elementary expression at every level. Numerical tests cannot establish infinite-dimensional or global novelty. Independent mathematical review and exhaustive historical-priority checking remain unperformed.

## References
1. E. W. Weisstein, “Spherical Segment,” *MathWorld*, https://mathworld.wolfram.com/SphericalSegment.html (classical definition and measures, with historical references to Smith 1923, Kern–Bland and Harris–Stocker).
2. S. R. Finch, “Planar Projections and Second Intrinsic Volume,” public version March 12, 2012, https://arxiv.org/abs/1203.2464 (random projection perimeter and integral-geometric methodology).
3. G. T. Vickers and D. J. Brown, “The distribution of projected area and perimeter of convex, solid particles,” *Proceedings of the Royal Society A* 457 (2001), 283–306, DOI 10.1098/rspa.2000.0667, https://www.academia.edu/60865860/The_distribution_of_projected_area_and_perimeter_of_convex_solid_particles (shape-class comparison).
