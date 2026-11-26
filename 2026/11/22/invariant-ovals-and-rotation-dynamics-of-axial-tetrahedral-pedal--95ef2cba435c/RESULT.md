# Invariant ovals and rotation dynamics of axial tetrahedral pedal iteration

## Finding
Let \(P\) be an axisymmetric tetrahedron with an equilateral base and an apex on its symmetry axis. Fix a point \(O\) on this axis strictly between the base plane and the apex, and repeatedly take the convex hull of the perpendicular feet from \(O\) onto the four facet planes. The family stays nondegenerate, with all feet actually lying in their facets. After rigidly orienting and scaling each iterate, its complete marked shape/point-position data lie on a compact invariant oval, except for the unique regular tetrahedron with coincident incenter and circumcenter.

More precisely, choose base circumradius \(\rho>0\), signed base height \(-p\rho\) and apex height \(q\rho\), with \(p,q>0\). After each pedal step, negate coordinates and rotate the base if needed to restore this normalization. The parameter map is
\[
(p,q)\longmapsto\left(\frac1{2(p+q)},\frac{2p((p+q)^2+1/4)}{q(p+q)}\right).
\]
Put \(u=1/(2p)\), \(v=p+q\). This conjugates the shape map to the birational diffeomorphism
\[
T(u,v)=\left(v,\frac{u+2v}{2uv-1}\right)
\quad\text{on}\quad
\Omega=\{u>0,\ v>0,\ 2uv>1\}.
\]
It preserves the nonconstant first integral and positive area form
\[
H(u,v)=\frac{2uv-1}{(1+u^2)(1+v^2)},\qquad
\omega=\frac{du\wedge dv}{(1+u^2)(1+v^2)}.
\]
The range of \(H\) is \((0,1/3]\). Its unique maximum \(H=1/3\), at \(u=v=\sqrt2\), represents the regular centered tetrahedron. Every level \(H=c\), \(0<c<1/3\), is one smooth compact embedded oval. On every such oval the pedal map is conjugate to a rigid circle rotation using a smooth positive weighted arclength measure. Consequently, on each level either every marked orbit is periodic of one common least period or every marked orbit is dense on that oval. There are no nonconstant marked orbits of periods one, two, or three. Nonperiodic dense marked orbits exist arbitrarily close to the regular centered tetrahedron. The distinct contribution is this invariant-oval description and its dynamical consequences; the underlying recurrence and linear multipliers are also covered by [4].

## Assumptions and scope
The operation is **fixed-point facet-foot iteration**, not the different operation that projects each vertex onto its opposite facet. The point \(O\) is fixed in Euclidean space; the four feet are computed from the entire planes supporting the facets. Here the feet, in fact, belong to the triangular facets, and the tetrahedron stays full-dimensional with \(O\) strictly inside. The parameter \(\rho\) is immaterial under uniform scaling. A central reflection and a rotation are allowed when identifying consecutive normalized marked shapes; the original unnormalized tetrahedra need not literally coincide or repeat in space. No statement is made for scalene tetrahedra or for off-axis projection points.

## Proof
**1. The geometric map.** Translate \(O\) to the origin, orient the symmetry axis vertically, and place the base vertices at \((\rho\cos(2\pi j/3),\rho\sin(2\pi j/3),-p\rho)\) for \(j=0,1,2\), with apex \((0,0,q\rho)\). Write \(s=p+q\) and \(E=s^2+1/4\). A lateral-face plane has normal \(s e_j+e_z/2\) and offset \(q\rho/2\), where \(e_j\) is the radial unit vector pointing to the midpoint of its base edge. Its foot is
\[
F_j=\frac{q\rho}{2E}\left(s e_j+\tfrac12e_z\right).
\]
The base-face foot is \((0,0,-p\rho)\). Thus the three lateral feet form an equilateral base at height \(q\rho/(4E)>0\), of circumradius \(q\rho s/(2E)>0\); the other foot is below the origin. Reflecting through the origin and rotating the equilateral base identifies a new normalized tetrahedron with
\[
p'=\frac{1}{2s},\qquad q'=\frac{2pE}{qs}.
\]
The lateral foot lies on the segment between the apex and the midpoint of its base edge, because its vertical coordinate is strictly between \(0\) and \(q\rho\) and the plane intersection is that segment; the base foot is the base centroid. Every subsequent iterate therefore remains admissible, and these formulas hold indefinitely.

**2. Conjugacy and invariant.** The change of variables \((p,q)\mapsto(u,v)=(1/(2p),p+q)\) bijects the positive quadrant onto \(\Omega\), with inverse \(p=1/(2u)\), \(q=v-1/(2u)\). The geometric formulas give \(u'=v\) and \(v'=(u+2v)/(2uv-1)\). If \(w=(u+2v)/(2uv-1)\), direct expansion yields
\[
2vw-1=\frac{1+4v^2}{2uv-1},\qquad
1+w^2=\frac{(1+u^2)(1+4v^2)}{(2uv-1)^2}.
\]
These identities show \(T(\Omega)\subset\Omega\), \(H(v,w)=H(u,v)\), and
\[
\det DT=\frac{1+4v^2}{(2uv-1)^2}
=\frac{1+w^2}{1+u^2}>0.
\]
They also imply \(T^*\omega=\omega\). The inverse is \(T^{-1}(v,w)=((w+2v)/(2vw-1),v)\), so the map is a global smooth bijection of \(\Omega\).

**3. Exhaustive structure of the levels.** The exact sum-of-squares identity
\[
\frac13-H(u,v)=\frac{(uv-2)^2+(u-v)^2}{3(1+u^2)(1+v^2)}
\]
shows the unique maximum and its equality case. For \(c\in(0,1/3)\), the level equation is quadratic in \(v\):
\[
c(1+u^2)v^2-2uv+1+c(1+u^2)=0.
\]
Its discriminant divided by four is \(Q_c(z)=z-c(1+z)-c^2(1+z)^2\), with \(z=u^2\). It has exactly two strictly positive roots
\[
z_\pm(c)=\frac{1-c-2c^2\pm\sqrt{(1+c)(1-3c)}}{2c^2}.
\]
For \(z\in(z_-,z_+)\) the equation has two positive roots in \(v\); the two branches meet at the two simple-discriminant endpoints. There are no other critical points of \(H\) in \(\Omega\): setting both partial derivatives to zero yields \(u^2v=u+v=uv^2\), hence \(u=v=\sqrt2\). Thus the two branches join smoothly into a single compact oval for every \(c\in(0,1/3)\), and no further components exist.

**4. Dynamics on each oval.** The map preserves both \(H\) and the positive area form \(\omega\), and is orientation preserving. By the coarea formula, the resulting smooth positive invariant measure on the regular level \(\Gamma_c=\{H=c\}\) has density, up to normalization,
\[
d\mu_c=\frac{d\ell}{(1+u^2)(1+v^2)\lVert\nabla H(u,v)\rVert},
\]
where \(d\ell\) denotes Euclidean arclength. This formula can alternatively be obtained by contracting \(\omega\) with any vector field \(X\) satisfying \(dH(X)=1\) near \(\Gamma_c\). Normalized cumulative \(\mu_c\)-length around the oval is a circle coordinate: since \(T\) preserves its orientation and this measure, it acts as a fixed translation in that coordinate. A circle translation has either all points periodic or all orbits dense.

A fixed point of \(T\) must have \(u=v\), and solving \(u=(3u)/(2u^2-1)\) gives \(u=\sqrt2\). For a two-cycle with alternating values \(u,v\), the recurrence \(s_{k-1}+2s_k+s_{k+1}=2s_{k-1}s_ks_{k+1}\) yields \(u+v=u^2v=uv^2\); hence \(u=v=\sqrt2\). For a three-cycle \(u,v,w\), its three cyclic recurrence equations have the same cubic right-hand side and left-hand sides \(u+w+2v\), \(u+v+2w\), \(v+w+2u\); subtraction forces \(u=v=w=\sqrt2\).

**5. Nonperiodic orbits close to the center.** At the unique fixed point the Jacobian is
\[
DT(\sqrt2,\sqrt2)=
\begin{pmatrix}0&1\\[2pt]-1&-2/3\end{pmatrix},
\]
with determinant one, trace \(-2/3\), and eigenvalues \(e^{\pm i\vartheta}\), \(\cos\vartheta=-1/3\). Because \(2\cos\vartheta=-2/3\) is rational but not an integer, \(\vartheta/(2\pi)\) is irrational: if it were rational, \(2\cos\vartheta\) would be a rational algebraic integer, hence an integer. The two squared terms in the maximum identity have independent linear parts at the center, so \(1/3-H\) has a positive definite quadratic part \(K\). The ovals shrink to the center by the level-root formulas. In each polar direction \(e\) about the center, the radius of the level \(1/3-H=\delta\) is \(\sqrt{\delta}/\sqrt{K(e)}+O(\delta)\), uniformly in \(e\), by Taylor expansion and strict radial increase there. In these polar parametrizations, the circle maps converge uniformly to the map induced by the Jacobian on the ellipse \(K=1\). The circle rotation numbers therefore approach the irrational linear rotation number (up to orientation). If all levels in an interval \((c_0,1/3)\) had rational rotation number, continuity on that connected interval would make the number constant rational, contradicting its irrational limit. Thus dense nonperiodic marked orbits occur arbitrarily near the centered regular tetrahedron.

## Verification
The standalone `check.py` uses exact rational arithmetic with no nonstandard library. It cross-checks the conjugacy, first integral, sum-of-squares identity, invariant Jacobian density, and direct three-dimensional facet-plane projections for 128 independent rational axisymmetric tetrahedra (3,712 exact assertions in total). The proof above, rather than finite testing, establishes the universal assertions. The differentiations, discriminant factorization, and circle-rotation argument are algebraic or analytic and may be checked independently from their displayed identities.

## Relationship to prior work
Zwierzyński (2026) supplied the fixed-point facet-foot iteration and an exact tetrahedral counterexample to four-step similarity return, as well as positive two- and four-step return families. Similarity of unmarked tetrahedra there is different from periodicity of the marked shape here. The companion record [4] derives the exact axial recurrence in all dimensions \(d\ge3\) and computes the nonresonant linear multipliers at the regular centered configuration. At \(d=3\), its squared-radius and height-ratio variables are \(Q=v^{-2}\), \(\tau=(2uv-1)^{-1}\). This is a bijection from \(\Omega\) to the positive quadrant and sends \(T\) to
\[
(Q,\tau)\longmapsto \left(\frac{4Q}{(4\tau+(1+\tau)Q)^2},\frac{Q}{\tau(4+Q)}\right),
\]
the recurrence in [4]. No priority ordering between the two records is asserted. The additional result here is the invariant measure and explicit global foliation by compact regular ovals, and the consequent rotation dynamics for axial marked tetrahedra. The classical QRT biquadratic-map theory supplies the general dynamical framework; the level equation here is a symmetric biquadratic, and \(T\) swaps coordinates and switches to the other root in the second coordinate. Abu-Saris and Hajja (2009) project vertices along altitudes to their opposite facets, a different operation from projecting a *fixed point* onto all face planes.

## Limitations
The rotation increment is defined by invariant measure and is not evaluated here as a closed function of \(c\); the theorem does not enumerate all rational-rotation levels or least periods greater than three. Higher-dimensional or nonsymmetric tetrahedra and varying projection points are excluded. This is a self-review only, not an independent audit. General QRT theory and historical geometry literature may contain abstract formulations from which pieces of the dynamical conclusion follow once the conjugacy is recognized.

## References
1. M. Zwierzyński, *When Pedal Shapes Come Back: a Complex Story*, arXiv:2611.01247v1, first public 2026-10-31. https://arxiv.org/html/2611.01247v1
2. R. Abu-Saris and M. Hajja, *The Chaotic Behavior of the Sequence of Pedal Simplices*, Results in Mathematics 55 (2009), 209–220, doi:10.1007/s00025-009-0411-z. https://doi.org/10.1007/s00025-009-0411-z
3. N. Joshi and P. Kassotakis, *Re-factorising a QRT map*, Journal of Computational Dynamics 6 (2019), 325–343; arXiv:1906.00501. https://arxiv.org/html/1906.00501v1
4. *Generic absence of finite pedal-shape return for regular simplices in every dimension at least three*, 22 November 2026, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-generic-absence-of-finite-pedal-shape-return-for-regular-simplic--66896a3b5b01 .
