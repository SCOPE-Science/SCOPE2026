# Fractional convexification laws at a symmetric quartic dimple, with an exact limaçon model

## Finding

**Universal local law.** Let \(G_\delta\) be a smooth one-parameter family of bounded Jordan domains in the Euclidean plane, symmetric about the horizontal axis. Suppose \(\partial G_0\) is convex, has strictly positive curvature except at one leftmost point, and in a fixed Cartesian neighborhood of that point the left boundary of \(G_\delta\) is the even smooth graph \(x=f_\delta(y)\). Assume the local normal form, with uniform differentiated remainders,

\[
f_\delta(y)=c(\delta)-A\delta y^2+By^4+O(\delta^2y^2+|\delta|y^4+y^6),\qquad A,B>0.
\]

For \(\delta>0\) sufficiently small, write \(H_\delta=\operatorname{conv}G_\delta\). The area added and boundary length removed by convexification satisfy the sharp limits

\[
\boxed{\begin{aligned}
\operatorname{area}(H_\delta)-\operatorname{area}(G_\delta)
&\sim\frac{2\sqrt2}{15}\frac{A^{5/2}}{B^{3/2}}\,\delta^{5/2},\\
\operatorname{length}(\partial G_\delta)-\operatorname{length}(\partial H_\delta)
&\sim\frac{8\sqrt2}{105}\frac{A^{7/2}}{B^{3/2}}\,\delta^{7/2}.
\end{aligned}}
\]

The new straight boundary segment has endpoints at vertical coordinates \(\pm\sqrt{A/(2B)}\,\delta^{1/2}(1+O(\delta))\). For negative sufficiently small \(\delta\), the domain remains convex and both defects are zero. In particular, for analytic families the area and perimeter defects are respectively \(C^2\) but not \(C^3\), and \(C^3\) but not \(C^4\), at \(\delta=0\). The ratio of perimeter defect to \(\delta\) times area defect tends to \(4A/7\).

**Exact classical model.** For \(0<q<1\), let \(G_q\) be the region bounded by the simple Pascal limaçon

\[
(x,y)=((1+q\cos\theta)\cos\theta,(1+q\cos\theta)\sin\theta),\quad 0\le\theta\le2\pi.
\]

Define \(\Delta_A(q)=\operatorname{area}(\operatorname{conv}G_q)-\operatorname{area}(G_q)\), and \(\Delta_P(q)=\operatorname{length}(\partial G_q)-\operatorname{length}(\partial\operatorname{conv}G_q)\). Both vanish for \(q\le1/2\). For \(1/2<q<1\), put

\[
t_q=\arccos\frac{1}{2q},\qquad s_q=\sqrt{1-\frac{1}{4q^2}}.
\]

Then the convex hull replaces exactly the indented arc between \((-1/(4q),\pm s_q/2)\) by its vertical chord, and

\[
\boxed{\Delta_A(q)=\left(\frac{7q}{4}+\frac{1}{8q}\right)s_q-\left(1+\frac{q^2}{2}\right)t_q,}
\]

\[
\boxed{\Delta_P(q)=2\int_0^{t_q}\sqrt{1+q^2-2q\cos t}\,dt-s_q.}
\]

With \(\delta=q-1/2\downarrow0\), these are

\[
\boxed{\Delta_A(q)=\frac{32}{15}\delta^{5/2}+O(\delta^{7/2}),\qquad
\Delta_P(q)=\frac{512}{105}\delta^{7/2}+O(\delta^{9/2}).}
\]

## Assumptions and scope

The universal statement assumes a smooth (or analytic for the stated differentiability classification) family of embedded closed curves with a single flat point at the transition. The remainder estimate includes the corresponding estimates after differentiation in \(y\) up to order four and in \(\delta\) as needed. Outside the chart, the curvature at \(\delta=0\) is strictly positive. These hypotheses exclude simultaneous dents, corners, nonlocal bitangents and higher-order flat contact. The limaçon has \(0<q<1\), so its polar radius is positive and its boundary is a regular simple curve; the cardioid endpoint \(q=1\) is not included.

The coefficients use physical Euclidean area, Euclidean arclength, and the defining parameter \(\delta\), not a rescaled curvature parameter. The convex hull is taken of the **filled** Jordan domain; taking the hull of its boundary gives the same result.

## Proof

**1. Local convex-hull structure.** From the normal form,

\[
f_\delta'(y)=y(-2A\delta+4By^2+O(\delta^2+|\delta|y^2+y^4)).
\]

For positive small \(\delta\) there are exactly two nonzero stationary points in the chart, \(\pm y_\delta\), with

\[
y_\delta^2=\frac{A}{2B}\delta+O(\delta^2).
\]

These are the two equal global leftmost points of the nearby curve: strict curvature on the compact complement keeps that complement uniformly outside a sufficiently small neighborhood of the unique leftmost point of \(\partial G_0\). On the arcs beyond \(\pm y_\delta\), \(f_\delta''\) is positive, while the omitted center arc lies strictly to the right of their common tangent line. Thus the outer arcs and the vertical segment joining the stationary points form one closed convex boundary, with continuously matched tangents. For \(\delta<0\) small, \(f_\delta''>0\) in the chart and curvature is positive elsewhere, so \(G_\delta\) itself is convex.

**2. Universal area coefficient.** The added region is bounded horizontally by \(f_\delta(y_\delta)\) and \(f_\delta(y)\) for \(|y|<y_\delta\). With \(Y=\sqrt{A/(2B)}\), substitute \(y=\sqrt\delta\,z\):

\[
\begin{aligned}
\Delta_A(\delta)
&=2\int_0^{y_\delta}[f_\delta(y)-f_\delta(y_\delta)]\,dy\\
&=2B\delta^{5/2}\int_0^Y(z^2-Y^2)^2\,dz+O(\delta^{7/2})\\
&=\frac{16B}{15}Y^5\delta^{5/2}+O(\delta^{7/2}).
\end{aligned}
\]

The last coefficient simplifies to the stated \(2\sqrt2 A^{5/2}/(15B^{3/2})\).

**3. Universal perimeter coefficient.** The removed arc has length \(2\int_0^{y_\delta}\sqrt{1+f_\delta'(y)^2}\,dy\); the replacing chord has length \(2y_\delta\). Hence

\[
\begin{aligned}
\Delta_P(\delta)
&=2\int_0^{y_\delta}(\sqrt{1+f_\delta'(y)^2}-1)\,dy\\
&=\delta^{7/2}\int_0^Y(-2Az+4Bz^3)^2\,dz+O(\delta^{9/2})\\
&=\frac{128B^2}{105}Y^7\delta^{7/2}+O(\delta^{9/2}).
\end{aligned}
\]

This gives the second universal constant. Uniform analytic implicit-function expansions in \(\delta\) and \(\sqrt\delta\) yield one-sided integer-power correction series multiplying the leading fractional powers. Smoothness of the original family makes the defects zero on the other side, proving the stated differentiability orders. Dividing the two displayed coefficients gives \(4A/7\).

**4. Global limaçon geometry.** Write \(c=\cos\theta\). The horizontal coordinate is \(x=c+qc^2\). If \(q\le1/2\), the signed curvature numerator is \(1+3q\cos\theta+2q^2\ge(1-q)(1-2q)\ge0\), proving convexity. If \(q>1/2\), the unique minimum of \(c+qc^2\) over \([-1,1]\) occurs at \(c=-1/(2q)\). Its two parameter values give the points \((-1/(4q),\pm s_q/2)\). The curvature numerator is strictly positive on the remaining arc, because there \(c\ge-1/(2q)\) and \(1+3qc+2q^2\ge 2q^2-1/2>0\). The vertical chord and this remaining arc therefore form the whole convex-hull boundary.

**5. Limaçon exact integrals.** Set \(t=\pi-\theta\) for the upper removed half-arc. It has

\[
x(t)=-\cos t+q\cos^2t,\quad y(t)=(1-q\cos t)\sin t,
\quad 0\le t\le t_q.
\]

The added area is

\[
2\int_0^{t_q}\left(x(t)+\frac1{4q}\right)(\cos t-q\cos2t)\,dt.
\]

Elementary integration and \(\cos t_q=1/(2q)\) simplify it to the asserted closed formula. The original half-arc speed is \(\sqrt{1+q^2-2q\cos t}\); replacing both half-arcs with the chord of length \(s_q\) gives the stated perimeter integral. The filled limaçon has area \(\pi(1+q^2/2)\), so its hull area is that value plus \(\Delta_A(q)\).

**6. Normal form for the example.** At \(q=1/2+\delta\), expand about \(\theta=\pi\) and invert the nonzero derivative \(dy/dt=1-q\) at \(t=0\). This yields

\[
x(y,\delta)=(-1/2+\delta)-4\delta y^2+2y^4+O(\delta^2y^2+\delta y^4+y^6).
\]

Thus \(A=4\), \(B=2\). Substitution into steps 2–3 gives \(32/15\) and \(512/105\). In particular the universal ratio becomes \(16/7\).

## Verification

The accompanying standalone Python checker evaluates the exact area formula against the defining cap integral, evaluates the perimeter deficit against its arc integral, and compares both convex-hull area and perimeter to polygonal convex hulls sampled independently from the polar parametrization. It checks the leading coefficients at several positive offsets from the transition. Independent high-precision quadrature also gave, for \(\delta=0.0001\), the normalized ratios \(\Delta_A/\delta^{5/2}=2.132404068887\ldots\) and \(\Delta_P/\delta^{7/2}=4.874971717202\ldots\), approaching \(32/15\) and \(512/105\). The analytic normal-form integration, not the finite tests, proves the limiting statements.

To reproduce: run `python check.py` with Python 3.9 or newer. The checker uses only the standard library.

## Relationship to prior work

Classical treatments of Pascal's limaçon give the convex-to-dimpled threshold and the double tangent. The 2015 *Handbook of Mathematics* explicitly gives both tangency coordinates, and Masih–Kanas (2020) independently gives the extremum of the real coordinate of a normalized limaçon. These are credited as prior ingredients, not claimed as new. Standard descriptions give area and perimeter of the original, unconvexified curve. The claim here is the **paired fractional convexification defects**, their sharp Euclidean coefficients, and their common local normal-form theorem for a broad class of smooth curves, not the existence or location of the double tangent. A semantic search of published related geometric findings identified polygonal convexification onset and a different involute-hull regularity transition, neither implying these generic smooth-dimple exponents and coefficients. This does not certify historical priority.

## Limitations

The universal theorem needs symmetry, single-point quartic degeneracy and uniform smoothness. Multiple simultaneous dents, curvature of higher vanishing order, asymmetric unfolding or nonlocal bitangent competition can produce different laws. The example assumes \(q<1\); the cardioid cusp at \(q=1\) is excluded. The complete perimeter correction is an exact one-dimensional integral, not an elementary closed form. Historical novelty is provisional and no external independent audit has been conducted.

## References

1. I. N. Bronshtein, K. A. Semendyayev, G. Musiol and H. Mühlig, *Handbook of Mathematics*, sixth edition (Springer, 2015), Section 2.12.3, p. 99, DOI: https://doi.org/10.1007/978-3-662-46221-8 .
2. V. S. Masih and S. Kanas, “Subclasses of Starlike and Convex Functions Associated with the Limaçon Domain,” *Symmetry* **12** (2020), 942, https://doi.org/10.3390/sym12060942 .
3. E. W. Weisstein, “Limaçon,” *MathWorld*, https://mathworld.wolfram.com/Limacon.html (classical formulas and terminology).
4. J. He, “Area in Polar Coordinates,” University of Houston Math 1432 Lecture 13, dated February 26, 2008, https://www.math.uh.edu/~jiwenhe/Math1432/lectures/lecture13.pdf (dated archival geometric example).
