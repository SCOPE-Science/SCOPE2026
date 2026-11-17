# Sharp quintic realization of a circular attracting limit cycle under an invariant unit circle in Kolmogorov flows

## Finding

The least degree of a real planar polynomial Kolmogorov vector field that preserves the unit circle and also has a strictly positive, circular, hyperbolic attracting limit cycle is **five**. The two circles are distinct: the invariant unit circle is not required to be a periodic orbit. A two-parameter damping-and-speed construction provides a quintic witness for every off-axis circle lying strictly in the positive quadrant and entirely outside the unit disk.

Precisely, let \(a,b,r,\kappa,\varepsilon>0\) satisfy
\[
a>r,\qquad b>r,\qquad \sqrt{a^2+b^2}-r>1.
\]
Define
\[
f(x,y)=(x-a)^2+(y-b)^2-r^2,\qquad
g(x,y)=x^2+y^2-1,
\]
and \(J(u,v)=(-v,u)\). The polynomial vector field
\[
\boxed{\quad
X(x,y)=(1+\kappa x)xy\bigl(gJ\nabla f-fJ\nabla g\bigr)
+\varepsilon fg\,(x,0)\quad}
\]
is of degree exactly five, has the invariant coordinate axes and the invariant unit circle \(g=0\), and has the circle \(f=0\) as a **hyperbolic attracting limit cycle**. Its nontrivial transverse Floquet multiplier is \(M=\exp(\mathcal L)\), where
\[
\boxed{\quad
\mathcal L=-2\varepsilon\kappa r^2
\int_{-\pi/2}^{\pi/2}
\frac{\cos^2\theta\,d\theta}{
(b+r\sin\theta)
\bigl[(1+\kappa a)^2-\kappa^2r^2\cos^2\theta\bigr]}
<0.\quad}
\]
Thus the attracting circular orbit is isolated and normally hyperbolic. A concrete rational-coefficient example is \(a=b=2\), \(r=1/2\), \(\kappa=\varepsilon=1\); its transverse multiplier is approximately \(0.955732097667886\).

## Assumptions and scope

The vector field is a polynomial field on \(\mathbb R^2\). A Kolmogorov field means \(\dot x=xP(x,y)\), \(\dot y=yQ(x,y)\) for real polynomials \(P,Q\). An invariant circle is a circle whose defining polynomial has a polynomial cofactor; this need not mean every point on it lies on a periodic orbit. A circular limit cycle is an isolated nonconstant periodic orbit whose image is a Euclidean circle. A hyperbolic attracting limit cycle has a transverse Floquet multiplier strictly between zero and one.

The inequalities ensure that \(f=0\) lies strictly in \(\{x>0,y>0,g>0\}\). The theorem gives existence and a sharp minimal degree, **not** a complete census of all periodic orbits or a global basin description. The lower-degree impossibility invokes the published cubic and quartic Kolmogorov no-go theorems stated below, together with the standard degree-one and degree-two cases.

## Proof

**1. Polynomial order and invariance.** Set \(V=xy(gJ\nabla f-fJ\nabla g)\) and \(K_0=4xy(bx-ay)\). The highest homogeneous terms in \(gJ\nabla f-fJ\nabla g\) cancel, so \(V\) has degree four. Direct expansion gives
\[
\nabla f\cdot V=K_0f,\qquad \nabla g\cdot V=K_0g.
\]
For the full field \(X\), therefore,
\[
\nabla f\cdot X=f\bigl[(1+\kappa x)K_0+2\varepsilon x(x-a)g\bigr],
\]
\[
\nabla g\cdot X=g\bigl[(1+\kappa x)K_0+2\varepsilon x^2f\bigr].
\]
This proves both circular invariances. Every term in the first component contains \(x\), and every term in the second contains \(y\); hence \(X\) is a Kolmogorov vector field. The degree-five homogeneous component of the second component contains \(\kappa x\) times the nonzero degree-four homogeneous part \(2xy[a(x^2-y^2)+2bxy]\) of \(V_2\); since \(a,b,\kappa>0\), the full degree is exactly five.

**2. The off-axis circle is a periodic orbit.** Parametrize \(f=0\) by \(x=a+r\cos\theta\), \(y=b+r\sin\theta\). The term containing \(fg\) vanishes on this curve, and \(J\nabla f=2r(-\sin\theta,\cos\theta)\). Consequently
\[
\frac{d\theta}{dt}=2xyg(1+\kappa x)>0.
\]
The closed circle contains no stationary point and is traversed in finite positive time, so it is a periodic orbit.

**3. Exact transverse exponent.** The normal Floquet multiplier of a regular invariant algebraic curve \(f=0\) is \(\exp\int_0^T K_f\,dt\), where \(K_f\) is its cofactor and \(T\) is the orbit period. The first term in \(K_f\) has zero integral: on \(f=0\), the identity \(\dot g/g=(1+\kappa x)K_0\) makes it the total time derivative of \(\log g\), whose integral around the closed orbit vanishes. Thus
\[
\mathcal L=\int_0^{2\pi}
\frac{\varepsilon(x-a)}{y(1+\kappa x)}\,d\theta
=\varepsilon r\int_0^{2\pi}
\frac{\cos\theta\,d\theta}{(b+r\sin\theta)
(1+\kappa a+\kappa r\cos\theta)}.
\]
Pair the integrand at \(\theta\) with that at \(\pi-\theta\), for \(-\pi/2\leq\theta\leq\pi/2\), obtaining the boxed negative integral above. Every denominator factor is positive: \(b>r\) and \(1+\kappa a>\kappa r\). The numerator is positive away from isolated points. Hence \(\mathcal L<0\). The orbit is therefore a hyperbolic attractor and in particular is isolated.

**4. Sharpness of the degree.** Jana and Sarkar, *Some remarks on polynomial vector fields in* \(\mathbb R^2\), Theorems 3.2 and 3.3, rule out **any** circular limit cycle for cubic and quartic Kolmogorov fields having \(x^2+y^2-1=0\) invariant. Degree-one fields have no limit cycles, and degree-two Kolmogorov fields have none by the classical result attributed to Bautin (as recalled by Gasull and Santana, Section 3). The construction above realizes the requirement at degree five, so five is the least possible degree.

## Verification

The bundled standalone \(\texttt{verify.py}\) uses SymPy to check the polynomial cofactors identically in symbolic parameters, the coordinate-axis divisibilities, and exact degree five. It also uses 55-digit mpmath quadratures to compare both forms of the Floquet integral for the rational witness. To rerun: install SymPy and mpmath in Python 3 and execute \(\texttt{python verify.py}\). The checker reports a logarithmic multiplier approximately \(-0.04527763776819087766\) and a multiplier approximately \(0.95573209766788605\). These numerical checks supplement, but do not replace, the exact sign proof or the previously published lower-degree obstruction.

## Relationship to prior work

Jana and Sarkar (first publicly posted 2026-10-23) prove the cubic/quartic circular-limit-cycle exclusion with invariant unit circle, but do not present a degree-five hyperbolic circular realization of the constrained Kolmogorov type above. The present result supplies a constructive sharp upper bound and an exact transverse stability certificate, using their lower bound. Gasull and Santana (arXiv:2510.11705) give broad existence and degree-lifting constructions for invariant algebraic curves and Kolmogorov limit cycles; they do not state the simultaneous invariant-unit-circle/positive-off-axis-circle sharp threshold. Earlier general constructions of prescribed invariant circles and algebraic limit cycles, including Llibre, Ramírez, Ramírez and Sadovskaia (2016), are related but do not provide an inspected direct matching result. Their complete treatment could contain specializations relevant to historical priority.

The distinct earlier problems of prescribing multiple concentric **limit cycles**, or constructing a periodic annulus between a circle and ellipse, do not enforce the Kolmogorov axes plus a unit circle that necessarily contains axis equilibria. This difference is essential: the unit circle in the present theorem is invariant but is **not** a limit cycle.

## Limitations

No assertion is made about stability of the invariant unit circle, the uniqueness of the off-axis circular limit cycle, the existence or absence of other periodic orbits, or the global basin of attraction. The full 2016 specialized circular-cycle classification could not be inspected, so independent historical-priority review remains appropriate. The lower-bound portion depends on the specifically cited prior theorems; the upper-bound construction and all-parameter Floquet sign are explicitly proved here. No independent validation has been performed.

## References

1. S. Jana and S. Sarkar, *Some remarks on polynomial vector fields in* \(\mathbb R^2\), arXiv:2610.33226, first posted 2026-10-23, https://arxiv.org/abs/2610.33226, particularly Theorems 3.2 and 3.3.
2. A. Gasull and P. Santana, *Limit cycles and invariant algebraic curves*, arXiv:2510.11705, first posted 2025-10-13, https://arxiv.org/abs/2510.11705; see the Kolmogorov corollary and discussion of degrees one and two.
3. J. Llibre, R. Ramírez, V. Ramírez and N. Sadovskaia, *The 16th Hilbert problem restricted to circular algebraic limit cycles*, Journal of Differential Equations 260 (2016), 5726–5760, https://doi.org/10.1016/j.jde.2015.12.019.
