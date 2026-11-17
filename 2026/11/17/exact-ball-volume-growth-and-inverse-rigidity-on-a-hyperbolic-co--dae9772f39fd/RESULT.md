# Exact ball-volume growth and inverse rigidity on a hyperbolic cone

## Finding
Let \(C_\alpha\) be the complete curvature-\(-1\) two-dimensional hyperbolic metric cone of total angle \(0<\alpha<\pi\), and let \(p\) lie at cone-apex distance \(s>0\). For every \(R>0\), let \(V(R)\) be the intrinsic area of the closed radius-\(R\) ball about \(p\). Define
\[
 a=\alpha/2,\qquad d=\operatorname{arsinh}(\sinh s\sin a),\qquad h=\sinh d,\qquad B=\arctan(\cosh s\tan a).
\]
For \(R>d\), put
\[
 u_R=\arcsin(h/\sinh R),\qquad \vartheta_R=\arctan(\cosh R\tan u_R).
\]
All inverse trigonometric functions use their principal real branches. **The exact area law at every radius** is
\[
 V(R)=\begin{cases}
 2\pi(\cosh R-1),&0<R\le d,\\
 4(\cosh R\,\vartheta_R-u_R),&d<R<s,\\
 2\cosh R(B+\vartheta_R)-\alpha-2u_R,&R\ge s.
 \end{cases}
\]
The second range is empty only if excluded parameter boundaries are taken; for the stated domain, \(0<d<s\). At \(R=s\) the two nontrivial formulas agree.

The asymptotic area spectrum is **two-term and center-rigid**:
\[
 V(R)=G(s,\alpha)e^R-\alpha+O_{s,\alpha}(e^{-R}),\qquad G(s,\alpha)=B+\arctan h=2\arctan(e^s\tan(\alpha/4)).
\]
Hence the two observable coefficients \(G=\lim_{R\to\infty}e^{-R}V(R)\) and \(C=\lim_{R\to\infty}(V(R)-Ge^R)\) satisfy \(C=-\alpha\) independently of the center. They recover the cone angle and the marked point's apex distance explicitly:
\[
 \boxed{\alpha=-C,\qquad s=\log\frac{\tan(G/2)}{\tan(\alpha/4)}.}
\]
The first deviation from the ordinary hyperbolic-disk volume occurs at \(R=d\), with the sharp cut-locus onset
\[
 2\pi(\cosh(d+\varepsilon)-1)-V(d+\varepsilon)
 =\frac83\sqrt{2\tanh d}\,\varepsilon^{3/2}+o(\varepsilon^{3/2})\quad(\varepsilon\downarrow0).
\]
The precise claim includes the global formula, both large-ball coefficients, their inverse recovery, and the first-cut coefficient as one unified description of the marked ball-volume profile.

## Assumptions and scope
The model has polar line element \(\mathrm d\rho^2+\sinh^2\rho\,\mathrm d\phi^2\), with \(\rho\ge0\) and \(\phi\in\mathbb R/\alpha\mathbb Z\); the apex is included and the path metric is intrinsic. The curvature normalization is \(-1\), so all areas and lengths are dimensionless. The apex distance \(s\) is strictly positive; the cone angle is strictly between \(0\) and \(\pi\). Ball boundaries have zero area, so closed or open balls give the same \(V\). The asymptotic constants depend on fixed \((s,\alpha)\); no uniformity at degenerating cone angles or escaping marked points is asserted.

## Proof
**1. Global distance.** For angular separation \(\delta=\min_{k\in\mathbb Z}|\phi-k\alpha|\in[0,a]\), hyperbolic polar development gives
\[
 \cosh\operatorname{dist}((s,0),(\rho,\phi))
 =\cosh s\cosh\rho-\sinh s\sinh\rho\cos\delta.
\]
The wedge with opening \(\delta\le a<\pi/2\) is geodesically convex in its hyperbolic development. Any competing winding has angular change at least \(\delta\), and the passage through the apex has length \(s+\rho\), strictly larger than the displayed geodesic when both radii are positive. Thus the displayed expression is the intrinsic minimum, including arbitrarily large \(\rho\).

**2. Radial sections and exact integration.** Write \(k_\delta^2=1+\sinh^2s\sin^2\delta\) and \(b_\delta=\operatorname{artanh}(\tanh s\cos\delta)\). The distance inequality is equivalent to
\[
 k_\delta\cosh(\rho-b_\delta)\le\cosh R.
\]
For \(R<s\), the admitted radial segment, when nonempty, has endpoints \(\rho_\pm=b_\delta\pm\operatorname{arcosh}(\cosh R/k_\delta)\), both positive. It is nonempty exactly when \(\sinh s\sin\delta\le\sinh R\). Integrating \(\sinh\rho\,\mathrm d\rho\) and using \(t=\sinh s\sin\delta\) therefore yields
\[
 V(R)=4\int_0^{\min(h,\sinh R)}\frac{\sqrt{\sinh^2R-t^2}}{1+t^2}\,\mathrm dt\qquad(0<R<s).
\]
Substitution \(t=\sinh R\sin u\) has the explicit primitive
\[
 4\left[\cosh R\arctan(\cosh R\tan u)-u\right].
\]
For \(R\le d\), its upper endpoint is \(u=\pi/2\); for \(d<R<s\), its endpoint is \(u=u_R\). This proves the first two cases.

For \(R\ge s\), the apex lies in the ball and every angular ray contains the radial interval from \(0\) to \(\rho_+(\delta)\). Direct angular integration gives
\[
 V(R)=2\int_0^a(\cosh\rho_+(\delta)-1)\,\mathrm d\delta.
\]
Using \(\cosh\rho_+=(\cosh s\cosh R+\sinh s\cos\delta\sqrt{\sinh^2R-\sinh^2s\sin^2\delta})/k_\delta^2\), the first term integrates to \(2\cosh R\arctan(\cosh s\tan a)\), while the second becomes twice the integral above with upper endpoint \(h\); the constant integrates to \(-\alpha\). This proves the third case. At \(R=s\), \(u_R=a\) and \(\vartheta_R=B\), ensuring continuity and equality of the formulas.

**3. Exponential growth and inverse recovery.** As \(R\to\infty\), \(u_R=O(e^{-R})\) and \(\vartheta_R=\arctan h+O(e^{-2R})\). In the third exact formula and \(2\cosh R=e^R+e^{-R}\), these yield
\[
 V(R)=(B+\arctan h)e^R-\alpha+O_{s,\alpha}(e^{-R}).
\]
The elementary hyperbolic half-angle identity \(B+\arctan(\sinh s\sin a)=2\arctan(e^s\tan(a/2))\) holds with both sides in \((0,\pi)\). In particular \(G\in(\alpha/2,\pi)\). Reading the constant coefficient gives \(\alpha=-C\). Taking the tangent of half the leading coefficient gives \(e^s\tan(\alpha/4)=\tan(G/2)\), proving the unique reconstruction of \(s\).

**4. The first cut.** Because \(0<d<s\), a ball of radius at most \(d\) develops injectively into the hyperbolic plane. For \(d<R<s\), subtraction of the second exact case from \(2\pi(\cosh R-1)\) and the trigonometric relations \(u_R=\pi/2-\arccos(\sinh d/\sinh R)\), \(\vartheta_R=\pi/2-\arccos(\tanh d/\tanh R)\) give exactly
\[
 D(R)=4\left[\cosh R\arccos\!\frac{\tanh d}{\tanh R}-\arccos\!\frac{\sinh d}{\sinh R}\right].
\]
Geometrically this is the equal-radius hyperbolic lens at the first transverse meeting of neighboring angular sheets. At tangency, each hyperbolic circular boundary has geodesic curvature \(\coth d\). In geodesic normal coordinates about the contact point, the lens width in the normal direction is \(2\varepsilon-\coth(d)y^2+O(\varepsilon^2+\varepsilon y^2+y^4)\). Integrating the positive part on \(|y|\le\sqrt{2\varepsilon\tanh d}+O(\varepsilon^{3/2})\) gives \(D(d+\varepsilon)=\frac83\sqrt{2\tanh d}\varepsilon^{3/2}+o(\varepsilon^{3/2})\). The exact expression confirms the same coefficient by expansion. Since the deficit is strictly positive after \(d\), it is the first non-hyperbolic-volume radius.

## Verification
The accompanying `verify.py` uses only the Python standard library. It computes the stated closed expressions separately from direct numerical radial-section integration of the hyperbolic distance inequality, checks every interval in the piecewise formula for four distinct cone parameters, reconstructs the center from the leading coefficient, tests the large-radius constant term and compares the fractional-power onset. Run `python3 verify.py` from the same directory; the success line is `HYPERBOLIC_CONE_BALL_VOLUME_AND_INVERSE_CHECKS_OK`. The algebraic derivation above, not numerical sampling, proves all quantified claims.

## Relationship to prior work
Gell-Redman (2010) studies harmonic maps into conical surfaces, including cones of angle at most \(\pi\), but not the intrinsic all-radius ball-area profile or asymptotic reconstruction. Toulisse (2014) explicitly gives the hyperbolic-sector gluing model and studies minimal diffeomorphisms between cone surfaces, not ball-volume coefficients. Izmestiev (2014) studies isoperimetry of cone surfaces primarily with nonpositive cone curvature; its inequalities do not determine an off-apex profile for a positive-curvature cone. A separate published flat-cone computation has first-cut and reconstruction statements, but uses zero curvature and polynomial area growth; it does not yield the hyperbolic exponential coefficient or its universal \(-\alpha\) constant term. General hyperbolic-disk and lens identities are background, not asserted novelty. The claim's novelty is conditional on the stated source comparison; no exhaustive historical priority is asserted.

## Limitations
The argument excludes cone angles \(\ge\pi\), the apex-centered limiting case, and variable curvature. It does not assert statistical stability under noisy observation, recover the entire geometry of a general compact hyperbolic cone surface, or classify later volume-profile regularity changes. The numerical evidence covers finitely many parameter choices and is not a proof. Independent validation and complete historical priority assessment remain open.

## References
- J. Gell-Redman, *Harmonic maps into conic surfaces with cone angles less than \(2\pi\)*, first public 20 October 2010, [arXiv:1010.4156](https://arxiv.org/abs/1010.4156).
- J. Toulisse, *Minimal diffeomorphism between hyperbolic surfaces with cone singularities*, first public 10 November 2014, [arXiv:1411.2656](https://arxiv.org/abs/1411.2656).
- I. Izmestiev, *A simple proof of an isoperimetric inequality for euclidean and hyperbolic cone-surfaces*, first public 26 September 2014, [arXiv:1409.7681](https://arxiv.org/html/1409.7681v1).
