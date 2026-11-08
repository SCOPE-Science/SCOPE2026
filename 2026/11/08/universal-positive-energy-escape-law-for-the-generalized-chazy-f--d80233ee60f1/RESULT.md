# Universal positive-energy escape law for the generalized Chazy flow

## Finding

For each integer \(q\geq1\), every trajectory of the generalized Chazy system specified below on a positive level \(H=h>0\) exists in forward time, remains in its initial sign component, and escapes to spatial infinity at an exact algebraic rate. Writing \(\sigma=\operatorname{sgn}(x(0))\), the universal limits are

\[
\lim_{t\to\infty}\frac{|x(t)|^{q+2}}t=(q+2)h,\qquad
\lim_{t\to\infty}\sigma\,|x(t)|^{q+1}y(t)=h.
\]

In particular, \(|x(t)|\sim((q+2)ht)^{1/(q+2)}\), and no positive-energy trajectory is bounded or periodic. Both coefficients are independent of the remaining initial-data coordinates.

## Assumptions and scope

The autonomous flow is defined on the open set \(x\ne0\) by

\[
\dot x=y,\quad \dot y=z,\quad
\dot z=-|x|^qz-(q+1)\frac{|x|^q}{x}y^2,
\qquad q\in\{1,2,3,\ldots\}.
\]

Its first integral is

\[
H(x,y,z)=xz-\tfrac12y^2+x|x|^q y.
\]

The hypothesis is exactly \(h:=H(x(0),y(0),z(0))>0\). No bound on the initial condition is needed. Indeed at \(x=0\) the continuous extension of the integral would be nonpositive, so every positive-energy initial state automatically lies in one of the two smooth sign components. Time is the unrescaled physical time of the displayed system.

## Proof

Direct differentiation on either sign component gives \(\dot H=0\). The vector field is equivariant under \((x,y,z)\mapsto(-x,-y,-z)\), which also preserves \(H\); it therefore suffices to treat \(x(0)>0\). Define

\[
w=z+x^q y.\]

The differential equations and the first integral become the exact triangular energy identities

\[
\dot x=y,\qquad \dot y=w-x^q y,\qquad
\dot w=-x^{q-1}y^2,\qquad
xw-\tfrac12y^2=h.
\]

Because \(h>0\) and \(x>0\), we have \(w=(h+y^2/2)/x>0\), and monotonicity gives \(w\le w_0\). Thus throughout the existence interval,

\[
x\ge h/w_0>0.\]

For negative \(y\), \(\dot y=w-x^qy>0\), whereas for positive \(y\), \(\dot y\le w_0-(h/w_0)^q y\). Therefore \(y\) is bounded above and below. Since \(\dot x=y\), the variable \(x\) cannot diverge in finite forward time. On every finite time interval, \(w\le w_0\), \(x\ge h/w_0\), and \(z=w-x^q y\) stay bounded, so the usual ODE continuation theorem gives a global forward solution that cannot cross \(x=0\).

If \(y\le0\) for all large times, then \(x\) is decreasing and bounded between \(h/w_0\) and an upper constant \(M\). On this interval \(\dot y\ge h/M\), a contradiction. At any zero of \(y\), \(\dot y=w>0\), so eventually \(y>0\) permanently and \(x\) increases. If increasing \(x\) had a finite limit \(M\), then \(\dot y\ge h/M-M^q y\), forcing \(\liminf y\ge h/M^{q+1}>0\), again a contradiction. Hence \(x(t)\to\infty\).

Because \(w\le w_0\) and \(x\to\infty\), for each fixed \(\delta>0\) the vector field points strictly downward on \(y=\delta\) for all sufficiently large times. An orbit with \(y\ge\delta\) would then decrease until it crosses that level, so \(y(t)\to0\). The energy relation also yields \(xw=h+y^2/2\to h\).

It remains to establish the sharp coefficient rather than just a decay bound. Fix \(0<\varepsilon<1\) and introduce two comparison graphs

\[
b_\pm(x)=(1\pm\varepsilon)h x^{-(q+1)}.
\]

On either graph, the derivative of the signed displacement is exactly

\[
\left.\frac{d}{dt}(y-b_\pm(x))\right|_{y=b_\pm(x)}
=\mp\frac{\varepsilon h}{x}
+\left(q+\tfrac32\right)(1\pm\varepsilon)^2\frac{h^2}{x^{2q+3}}.
\]

For sufficiently large \(x\), the derivative at the upper graph is strictly negative and at the lower graph strictly positive. Once the orbit enters the strip \(b_-(x)\le y\le b_+(x)\), it cannot leave. Both entrance barriers are eventually crossed: if \(y\ge b_+(x)\) forever, then the exact equation \(\dot y=(h+y^2/2)/x-x^qy\), together with \(y\to0\), implies \(\dot y\le-\varepsilon h/(2x)\) at late times; but \(\int^\infty dt/x(t)=\infty\) because \(\dot x=y\) is bounded, contradicting \(y>0\). Likewise, if \(y\le b_-(x)\) forever, \(\dot y\ge\varepsilon h/x\) and the same divergent integral contradicts bounded \(y\). Thus eventually

\[
(1-\varepsilon)h\le x^{q+1}y\le(1+\varepsilon)h.
\]

As \(\varepsilon\downarrow0\), we obtain \(x^{q+1}y\to h\). Consequently \(\frac{d}{dt}x^{q+2}=(q+2)x^{q+1}y\to(q+2)h\), and integration divided by \(t\) proves the first limit. Symmetry completes the proof for negative initial \(x\).

## Verification

All identities in the proof are obtained by differentiating explicit expressions. The critical nonstandard step is the sign of the two moving-barrier derivatives; its exact expression is displayed above, with a leading term of order \(x^{-1}\) and an error of order \(x^{-2q-3}\). The divergence of \(\int^\infty dt/x(t)\) follows from the proved global bound on \(y=\dot x\). These analytic verifications cover all integer \(q\ge1\) and all positive-energy initial data without finite enumeration.

As a supplementary numerical cross-check, direct initial-value integration was performed at \(q=1,2,3\) and \(h=1/2,2\) to time 2000. The ratio \(|x(t)|^{q+2}/((q+2)ht)\) was within 0.001 of one and the ratio \(x^{q+1}y/h\) within 0.00003 of one in all six trials. These finite tests are not used to establish the universal theorem.

## Relationship to prior work

Llibre, Novaes and Valls (2023, arXiv:2307.00087) introduce the generalized Chazy differential equation, its first integral and families of periodic trajectories on negative integral levels. The present theorem studies the complementary positive-energy levels and supplies their complete forward escape and velocity asymptotics; periodic-cylinder existence or a Floquet argument does not imply this global escape law. Earlier work by Géronimi, Feix and Leach (1999) treats periodic solutions and limit cycles. A full text of that earlier source was not available for direct comparison. Positive-energy equivalents in other parametrizations or unindexed literature remain possible.

## Limitations

The theorem makes no classification of zero- or negative-energy trajectories, backward-time solutions or noninteger exponent values. It does not assert that all positive-energy orbits approach the same geometric curve beyond the two stated normalized asymptotic limits. The originality assessment is provisional with respect to unavailable full-text literature; no independent mathematical audit has been performed.

## References

1. J. Llibre, D. D. Novaes and C. Valls, *Existence of a cylinder foliated by periodic orbits in the generalized Chazy differential equation*, arXiv:2307.00087, publicly available 2023-06-30.
2. C. Géronimi, M. R. Feix and P. G. L. Leach, *Periodic Solutions and Associated Limit Cycle for the Generalised Chazy Equation*, 1999, DOI:10.1007/BFb0105938.
