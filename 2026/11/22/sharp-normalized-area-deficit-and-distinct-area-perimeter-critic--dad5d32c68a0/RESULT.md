# Sharp normalized convexification stability and two onset exponents for Cassini ovals

## Finding
Let \(a>0\), \(a<b<\sqrt2\,a\), and let \(K_{a,b}\subset\mathbb R^2\) be the compact region bounded by the Cassini oval
\[
|(x,y)-(a,0)|\,|(x,y)+(a,0)|=b^2.
\]
Write \(H_{a,b}=\operatorname{conv}(K_{a,b})\), \(\delta=4-(b/a)^4\in(0,3)\), \(D_A=|H_{a,b}|-|K_{a,b}|\) and \(D_P=P(K_{a,b})-P(H_{a,b})\), where \(P\) denotes ordinary boundary length. Then \(D_A>0\) and
\[
\boxed{\frac1{120}<\frac{D_A}{a^2\delta^{5/2}}<\frac{3\sqrt3/2-2}{3^{5/2}}.}
\]
The middle expression is strictly increasing as \(\delta\) increases over \((0,3)\). Both constants are optimal, as limits for \(b/a\uparrow\sqrt2\) and \(b/a\downarrow1\), respectively. Moreover, as \(\delta\downarrow0\) with \(a\) fixed,
\[
D_A=\frac{a^2\delta^{5/2}}{120}+O(a^2\delta^{7/2}),\qquad
D_P=\frac{a\delta^{7/2}}{3360}+O(a\delta^{9/2}),
\]
and consequently \(D_P/D_A=\delta/(28a)+O(\delta^2/a)\).

The upper and lower convex-hull facets have endpoint pairs
\[
\left(\pm\frac{a\sqrt\delta}{2},\ \pm\frac{a\sqrt{4-\delta}}2\right),
\]
with independent common signs in each facet. All four contact points lie on the circle \(x^2+y^2=a^2\).

## Assumptions and scope
The connected nonconvex regime is precisely \(1<b/a<\sqrt2\). The strict inequalities do not include the lemniscate endpoint \(b=a\), which is used only for the optimal limiting constant. The asymptotics keep \(a>0\) fixed and use the dimensionless small parameter \(\delta\). The displayed lengths refer to perimeter of the original single-loop compact region and of its convex hull, not to a different sampling measure or signed arc length.

## Proof
By dilation set \(a=1\); restore factors \(a^2\) for areas and \(a\) for lengths. The upper boundary for \(0\le x\le\sqrt{1+b^2}\) is
\[
y(x)=\sqrt{-1-x^2+\sqrt{b^4+4x^2}}.
\]
Set \(s(x)=\sqrt{b^4+4x^2}\). The derivative of \(y(x)^2\) is \(2x(-1+2/s(x))\). Since \(1<b<\sqrt2\), its sole positive interior zero is \(x_*=\sqrt{4-b^4}/2=\sqrt\delta/2\). At that point \(y_*=b^2/2=\sqrt{4-\delta}/2\). Thus \(y\) increases to \(y_*\) and then decreases. For \(x>x_*\),
\[
(y^2)''=-2+\frac4{s(x)}-\frac{16x^2}{s(x)^3}<0,
\]
so \(y''<0\) on the outer arc. Reflection symmetry and the horizontal supporting lines at \(\pm y_*\) show that the convex hull replaces precisely the two central dent arcs by horizontal segments. The contact identity \(x_*^2+y_*^2=1\) follows immediately.

The resulting exact area deficit is
\[
D_A=4\int_0^{x_*}\bigl(y_*-y(x)\bigr)\,dx,
\]
and a rationalized exact integrand is
\[
y_*-y(x)=\frac{(2-\sqrt{b^4+4x^2})^2}{4(y_*+y(x))}.
\]
Indeed \(y_*^2-y(x)^2=(2-\sqrt{b^4+4x^2})^2/4\). Set \(x=\sqrt\delta\,t/2\), \(0\le t\le1\), and define
\[
S_\delta(t)=\sqrt{4-\delta(1-t^2)},\quad
h_\delta=\frac{\sqrt{4-\delta}}2,\quad
Y_\delta(t)=\sqrt{-1-\delta t^2/4+S_\delta(t)}.
\]
Then the normalized deficit has the exact representation
\[
\frac{D_A}{\delta^{5/2}}=\frac12\int_0^1
\frac{(1-t^2)^2}{(2+S_\delta(t))^2(h_\delta+Y_\delta(t))}\,dt.
\]
For every \(0<t<1\), the positive quantities \(S_\delta,h_\delta,Y_\delta\) decrease strictly with \(\delta\in(0,3)\): the last assertion follows from
\[
\frac{d}{d\delta}Y_\delta(t)^2=-\frac{t^2}4-\frac{1-t^2}{2S_\delta(t)}<0.
\]
Consequently the integrand increases strictly in \(\delta\), giving the global strict normalized inequality once the endpoints are evaluated.

At \(\delta=0\), the integrand limit is \((1-t^2)^2/32\), hence the prefactor \(1/2\) gives \(\int_0^1(1-t^2)^2dt/64=(8/15)/64=1/120\). At \(\delta=3\), the limiting Cassini oval is the Bernoulli lemniscate with polar equation \(r^2=2\cos2\theta\) on each lobe. Its total area is \(2\), while the convex hull has first-quadrant area \(3\sqrt3/8\): a rectangle of area \(\sqrt3/4\) and an outer curved segment of area \(\sqrt3/8\). The latter equals the polar sector area \(\frac12\int_0^{\pi/6}r^2d\theta=\sqrt3/4\) minus the triangle area \(\sqrt3/8\). Thus the limiting hull area is \(3\sqrt3/2\), and the area deficit tends to \(3\sqrt3/2-2\). Division by \(3^{5/2}\) yields the sharp upper constant.

For the critical onsets, uniformly in \(t\in[0,1]\) as \(\delta\downarrow0\), expansion of the exact rationalized formula yields
\[
y_*-y(\sqrt\delta\,t/2)=\frac{\delta^2(1-t^2)^2}{128}+O(\delta^3),\quad
y'(\sqrt\delta\,t/2)=\frac{\delta^{3/2}t(1-t^2)}{16}+O(\delta^{5/2}).
\]
The exact perimeter excess is
\[
D_P=4\int_0^{x_*}\bigl(\sqrt{1+y'(x)^2}-1\bigr)dx.
\]
Substitute the expansions and \(\int_0^1t^2(1-t^2)^2dt=8/105\). These give \(D_A=\delta^{5/2}/120+O(\delta^{7/2})\) and \(D_P=\delta^{7/2}/3360+O(\delta^{9/2})\). Restoring the dimensions finishes the proof.

## Verification
An independent standard-library checker is included at `verification/check_cassini.py`. Run `python3 verification/check_cassini.py`. It tests the rationalized identity, numerical agreement of two area formulas, monotonicity at nine parameter choices, the exact endpoint constants, and the perimeter expansion. These finite calculations corroborate but do not replace the analytic proof above.

## Relationship to prior work
Karataş (2013), sections 2.3 and 2.5, established the area quadrature of a Cassini oval and a perimeter integral for its convex hull, including its tangent-contact abscissa. Those ingredients and the classical convexity threshold are not claimed as new. The contribution here is the sharp *global monotone normalization* of the area missing from the convex hull, its two best constants, and the coupled area/perimeter onset exponents with exact coefficients. The first endpoint remains the classical Bernoulli lemniscate, whose area is also classical.

## Limitations
The global inequality applies only to the connected peanut-shaped regime, not to disjoint two-loop Cassini sets. The asymptotic is a one-parameter limit at fixed focal spacing. The prior literature gives enough geometry to express the exact area difference as a quadrature; no novelty is asserted for that elementary reduction. No independent specialist validation or exhaustive historical-priority determination has been performed.

## References
- M. Karataş, *A Multi Foci Closed Curve: Cassini Oval, Its Properties and Applications*, Doğuş Üniversitesi Dergisi 14(2), 231–248 (2013), publicly dated 2013-07-01. https://dergipark.org.tr/en/pub/doujournal/article/1043098 ; full text https://fileserver-az.core.ac.uk/download/45464639.pdf .
- *Cassini oval*, mathematical overview of the classical family and its shape regimes, https://en.wikipedia.org/wiki/Cassini_oval (accessed 2026-11-15 UTC).
