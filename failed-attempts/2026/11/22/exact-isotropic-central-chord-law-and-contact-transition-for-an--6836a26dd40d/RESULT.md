# Exact isotropic central-chord law and contact transition for an unequal orthogonal bicylinder

## Finding

Let \(0<a<b\) and \(K_{a,b}=\{(x,y,z):x^2+y^2\le a^2,\ y^2+z^2\le b^2\}\). For Haar-uniform \(U\in S^2\), the center-through chord length \(L=\mathcal H^1(K_{a,b}\cap\mathbb R U)\) has support \([2a,2\sqrt{a^2+b^2}]\). Put \(R=\sqrt{a^2+b^2}\), \(s=\sqrt{1-4a^2/l^2}\), and, for \(l>2b\), \(t=\sqrt{1-4b^2/l^2}\), \(J(s,t)=\frac2\pi[s\arcsin(t/\sqrt{1-s^2})+t\arcsin(s/\sqrt{1-t^2})-\arctan(st/\sqrt{1-s^2-t^2})]\). Its CDF is \(0\) below \(2a\); \(s\) for \(2a<l\le2b\); \(s+t-J(s,t)\) for \(2b<l<2R\); and \(1\) above \(2R\). The sharp threshold and endpoint laws are \(F(2a+\varepsilon)\sim\sqrt{\varepsilon/a}\), \(F(2b+\varepsilon)-F(2b)\sim\frac2{\pi\sqrt b}\arcsin(a/b)\sqrt\varepsilon\), and \(\Pr\{L>2R-\varepsilon\}\sim\frac{2\sqrt R}{3\pi ab}\varepsilon^{3/2}\). Above the internal threshold \(l=2b\), the respective chord-contact density contributions from the two defining cylinders are \(f_a(l)=\frac{4a^2}{l^3s}[1-\frac2\pi\arcsin(t/\sqrt{1-s^2})]\) and \(f_b(l)=\frac{4b^2}{l^3t}[1-\frac2\pi\arcsin(s/\sqrt{1-t^2})]\); in particular conditional first-contact weights tend to \(a^2/R^2,b^2/R^2\) as \(l\uparrow2R\).

This is an exact distribution of *origin-passing* Euclidean chord lengths under uniform directions, not Crofton-random translated chords, and it separately resolves which of the two cylindrical constraints limits a chord.

## Assumptions and scope

Assume real radii \(0<a<b\). The two infinite circular cylinders have perpendicular axes and intersect at the origin: \(K_{a,b}=\{x^2+y^2\le a^2,\ y^2+z^2\le b^2\}\). Independently of the chosen orientation, a line through the origin is specified by \(U\in S^2\) distributed according to normalized spherical area. A length threshold is written \(l\), with \(R=\sqrt{a^2+b^2}\). Formulae on open intervals extend continuously to their endpoints; conditional contact labels are defined away from sets of ties of zero spherical measure.

## Proof

For a fixed direction \(u=(u_x,u_y,u_z)\), the radius to the first-cylinder boundary is \(a/\sqrt{1-u_z^2}\), while the radius to the second-cylinder boundary is \(b/\sqrt{1-u_x^2}\). Thus the whole central chord has length
\[
L(u)=2\min\left\{\frac a{\sqrt{1-u_z^2}},\frac b{\sqrt{1-u_x^2}}\right\}.
\]
Each absolute Cartesian coordinate of a Haar direction on \(S^2\) is uniform on \([0,1]\). For \(l>2a\), the first-cylinder event \(L_a\le l\) is \(|u_z|\le s(l)\); for \(l>2b\), the second-cylinder event \(L_b\le l\) is \(|u_x|\le t(l)\). Inclusion-exclusion gives \(F_L=s+t-J(s,t)\) where \(J(s,t)=\Pr(|u_z|\le s,|u_x|\le t)\). Because \(l<2R\), \(s^2+t^2<1\), allowing one to evaluate this intersection without saturation. The projection of uniform spherical area to the \((u_z,u_x)\) unit disk has density \(1/(2\pi\sqrt{1-u_z^2-u_x^2})\). Integrating four symmetric rectangular quadrants gives
\[
J(s,t)=\frac2\pi\int_0^s\arcsin\frac t{\sqrt{1-z^2}}\,dz.
\]
Integration by parts and an elementary tangent substitution evaluate this as the displayed arctangent expression. When \(l\le2b\), the second event is empty and \(F_L=s\). The largest possible chord occurs where \(s^2+t^2=1\), namely \(l=2R\); every \(l\) between the two endpoints has a direction attaining it.

Differentiate the inclusion-exclusion formula. Since \(J_s=(2/\pi)\arcsin(t/\sqrt{1-s^2})\) and \(J_t=(2/\pi)\arcsin(s/\sqrt{1-t^2})\), the chain rule gives the two positive contact contributions stated in the finding. Their sum is the chord-length density; the event of simultaneous contact has probability zero for \(a<b\).

At the lower endpoint use \(s(2a+\varepsilon)=\sqrt{\varepsilon/a}(1+O(\varepsilon))\). At the internal threshold, \(t(2b+\varepsilon)=\sqrt{\varepsilon/b}(1+O(\varepsilon))\), while \(J_t(s,0)=(2/\pi)\arcsin\sqrt{1-a^2/b^2}\), yielding the claimed square-root coefficient. At the top endpoint, set \(\Delta=1-s^2-t^2=4R^2/l^2-1=\varepsilon/R+O(\varepsilon^2)\). The four small spherical components of \(\{|u_z|>s,|u_x|>t\}\) lie near the four directions \((\pm a/R,0,\pm b/R)\). In local orthonormal coordinates \((v,w)\), the two active boundary inequalities become a wedge of tangential width proportional to \(\Delta\) and transverse width proportional to \(\sqrt\Delta\). Directly integrating its quadratic spherical graph gives the normalized area \(\frac{2R^2}{3\pi ab}\Delta^{3/2}+o(\Delta^{3/2})\), equal to \(\frac{2\sqrt R}{3\pi ab}\varepsilon^{3/2}+o(\varepsilon^{3/2})\). For the contact-label ratio, expand both density contributions at the common endpoint; their ratio tends to \(a^2:b^2\). These calculations require fixed strictly unequal positive radii.

## Verification

The included `checker.py` computes the exact CDF, its independently integrated cap-intersection probability, derivative contact decomposition and upper-edge quadrature. Its deterministic parameter-grid tests and an independently generated Haar Monte Carlo sample check the proposed branches and endpoint coefficients; these are numerical corroboration only, not a substitute for the analytic proof.

Run `python checker.py` in an environment with Python 3, NumPy and SciPy; no unpublished data inputs are required.

## Relationship to prior work

The classical Steinmetz-solid construction, including unequal radii, is documented in the 1999 geometry reference by Weisstein. It does not give the Haar center-chord distribution. Published directions and section-area analyses of equal-radius tricylinders concern different functionals. A previous rectangular-box central-chord law uses different radial constraints. The formula can also be viewed as a specialized orthogonal spherical-cap intersection probability; generic spherical solid-angle methods give the needed integration technique. Searches of adjacent results did not find this full unequal-cylinder contact-labelled distribution, but this is not a proof of historical priority.

## Limitations

Only two mutually orthogonal infinite circular cylinders through the origin with fixed radii \(a<b\) are covered. The probability is Haar on directions through the origin, not on translated lines or boundary points. The equal-radius collision is deliberately excluded from the interior-threshold asymptotic. The result does not provide an inverse characterization among all convex bodies. Independently established literature priority is not claimed.

## References

- Eric W. Weisstein, *Steinmetz Solid*, CRC Concise Encyclopedia of Mathematics historical archive, dated 1999-05-26, https://archive.lib.msu.edu/crcmath/math/math/s/s724.htm.
- *Bicylindric Curve*, MathCurve reference, https://www.mathcurve.com/courbes3d.gb/bicylindric/bicylindric.shtml (geometric background, historical date not used).
- Published mathematical records concerning the orthogonal tricylinder's central sections and the centered rectangular box's Haar chord distribution (comparison only).
