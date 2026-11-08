# An explicit smallest-period attracting eye in a piecewise-linear doubled circle map

## Finding
For the piecewise-linear circle map
\[
f_{a,b}(x)=\bigl(2x+a+\tfrac b2S(x)\bigr)\bmod1,
\qquad
S(x)=\begin{cases}4x-1,&0\le x\le1/2,\\3-4x,&1/2\le x<1,\end{cases}
\]
with \(a\in\mathbb R/\mathbb Z\) and \(0\le b\le1\), define \(b_c\in(0,1)\) as the unique solution of
\[
8(1+b_c)(1-b_c)^2=1
\]
and put \(b_u=(\sqrt{21}-1)/4\). Numerically \(b_c=0.731299211487387\ldots\) and \(b_u=0.895643923738960\ldots\). Define
\[
\begin{aligned}
a_-(b)&=\frac{(b+1)(4b^2-10b+9)}{2(7+2b-4b^2)},\\
a_+(b)&=\frac{-4b^3-2b^2+3b+4}{2(7-2b-4b^2)}.
\end{aligned}
\]
For **every** \(b_c<b<b_u\) and \(a_-(b)<a<a_+(b)\), the map has a regular, locally exponentially attracting *least-period-three* orbit with branch itinerary \((+,-,-)\). In the real lift chart, successive integer reductions are exactly \((0,1,2)\), and the multiplier is
\[
\lambda_3(b)=8(1+b)(1-b)^2\in(0,1).
\]
The reflected parameter interval
\[
\tfrac32-a_+(b)<a<\tfrac32-a_-(b)
\]
contains a second, disjoint attracting period-three window, with the same multiplier. The two windows are contained in non-single-minus *eye* components in the terminology of Bhattacharyya--Banerjee, rather than period-three tongues. This statement does **not** claim an exhaustive classification of all eyes.

The width of either explicitly described window is exactly
\[
w(b)=a_+(b)-a_-(b)
=\frac{(4b^2+2b-5)(8b^3-8b^2-8b+7)}{2(4b^2-2b-7)(4b^2+2b-7)}>0.
\]
Both endpoints collapse at \(b=b_c\) and \(b=b_u\). In particular, these regions are bounded away from the ceiling \(b=1\). Their **combined Euclidean parameter area** is exactly
\[
\mathcal A=2\int_{b_c}^{b_u}w(b)\,db
=0.0024418116003992040\ldots.
\]
The integrand admits the elementary partial-fraction form
\[
w(b)=b-\tfrac12+\frac{2(b-1)}{4b^2+2b-7}+\frac{2b+1}{4b^2-2b-7},
\]
so the integral is an exact expression in algebraic numbers and logarithms. Period three is the least possible period for an attracting *non-single-minus* itinerary: an attracting nonfixed orbit cannot lie entirely in the contracting half, while length two offers no itinerary with two minus symbols and a plus symbol.

## Assumptions and scope
The circle is represented by \([0,1)\). A regular orbit avoids the branch boundaries \(0\) and \(1/2\). Its two branch symbols \(+\) and \(-\) indicate membership in \((0,1/2)\) and \((1/2,1)\), respectively. Local exponential attraction is with respect to the circle topology, and all inequalities defining the two open parameter regions are strict. Area uses the usual Lebesgue measure on the parameter cylinder. The principal theorem is the explicit positive-area construction and its exact itinerary, multiplier, bounds and area; no global shape classification is asserted.

## Proof
Write \(p=2(1+b)\), \(q=2(1-b)\). The real affine expressions on the two open halves are \(L_+(t)=pt+a-b/2\) and \(L_-(t)=qt+a+3b/2\). For a candidate orbit \((x,y,z)\) with symbols \((+,-,-)\) and integer reductions \((0,1,2)\), solve
\[
 y=px+a-b/2,\quad z=qy+a+3b/2-1,\quad x=qz+a+3b/2-2.
\]
Its return coefficient is \(M=pq^2=8(1+b)(1-b)^2\). Since
\[
M'(b)=-8(1-b)(1+3b)<0\qquad(0<b<1),
\]
there is exactly one \(b_c\) with \(M=1\); on \(b_c<b<b_u\) one has \(0<M<1\). The unique affine solution is
\[
\begin{aligned}
x&=\frac{(1+q+q^2)a-q^2b/2+q(3b/2-1)+3b/2-2}{1-M},\\
y&=px+a-b/2,\qquad z=qy+a+3b/2-1.
\end{aligned}
\]
All three coordinates are strictly increasing with \(a\), because \(1+q+q^2>0\), \(p,q>0\), and \(1-M>0\).

Direct substitution shows \(y(a_-)=1/2\) and \(z(a_+)=1\). Set \(E_-(b)=4b^2-2b-7\), \(E_+(b)=4b^2+2b-7\), and \(Q(b)=4b^2+2b-5\). At the two endpoints,
\[
\begin{aligned}
x(a_-)&=\frac{4b^2-6b+1}{2E_-},&x(a_+)&=\frac{2(b-1)}{E_+},\\
x(a_-)-\tfrac12&=\frac{-2(b-2)}{E_-},&x(a_+)-\tfrac12&=\frac{-(4b^2-2b-3)}{2E_+},\\
y(a_+)-\tfrac12&=\frac{Q}{2E_+},&y(a_+)-1&=\frac1{E_+},\\
z(a_-)-\tfrac12&=\frac{-(2b+1)}{E_-},&z(a_-)-1&=\frac{-Q}{2E_-}.
\end{aligned}
\]
For \(b_c<b<b_u\), one has \(E_-<0\), \(E_+<0\), \(Q<0\), \(4b^2-6b+1<0\), and \(4b^2-2b-3<0\). Thus \(0<x(a_\pm)<1/2\), \(1/2\le y(a_-)<y(a_+)<1\), and \(1/2<z(a_-)<z(a_+)\le1\). Since \(x,y,z\) increase with \(a\), every strict parameter pair in the claimed interval has all three points in their intended open halves and the integer reductions are valid. The three-point cyclic orbit cannot have period one because \(x\) and \(y\) lie in different halves. Since the proposed period is three, the least period must therefore be three, its least period is exactly three. Its return derivative \(M\in(0,1)\) proves local exponential attraction.

The factors \(Q<0\) and \(M-1<0\), together with \(E_-E_+>0\), give the positive displayed width; its zeros at \(b_u\) and \(b_c\) follow by substitution. For the reflection, define \(R(x)=1/2-x\pmod1\) and \(a'=1/2-a\pmod1\). An affine check on each half gives \(f_{a',b}(R(x))=R(f_{a,b}(x))\); the lifted expressions differ by integers \(1\) (plus branch) and \(3\) (minus branch). Hence the other explicit window is the parameter reflection and has the same multiplier and width. The original interval lies around \(a\in(0.52,0.56)\) while its reflection lies around \(a\in(0.94,0.98)\); the strict separation also follows directly from the displayed endpoint rational expressions. Integrating the exact width yields the area formula.

Finally, a non-single-minus period-one or period-two attracting orbit would need at least two minus visits and at least one plus visit, which is impossible with fewer than three positions. The necessity of a plus visit for every nonfixed attracting orbit is Lemma 4.1 of the cited source, and Theorem 2.5 there identifies the non-single-minus parameter components as eyes.

## Verification
The accompanying `check.py` independently reconstructs the affine cycle, proves the identity of the rational width and its partial fraction decomposition, verifies the exact endpoint equalities and symbolic reflection, isolates the unique multiplier root, checks exact rational branch locations at \(b=4/5\), and evaluates the definite integral at high precision. Its rational-polynomial root counts verify that no unlisted sign changes occur across the relevant interval; the printed numerical quadrature is a check of the exact integral definition, not a proof of a global parameter census. Run with `python check.py` using SymPy and mpmath.

## Relationship to prior work
Bhattacharyya--Banerjee (2025), Sections 2, 4 and 7, introduce the precise piecewise-linear family and distinguish non-single-minus eyes from tongues. Their period-three construction has *one* contracting visit, while their illustrated non-single-minus eyes have period five. The source establishes no displayed rational \((+,-,-)\) period-three eye window, its exact coefficient bounds or its positive area. Its qualitative eye criterion is used, not presented as new. Earlier analytic double-standard-map literature concerns a different nonlinear family, not an exact affine-branch chart. Exact attracting prime-two tongue results for this same map address the \((+,-)\) multiplier \(4(1-b^2)\), not the present \((+,-,-)\) multiplier, and do not imply this construction.

## Limitations
This is an exact **sufficient** construction of two disjoint parameter windows for one lift itinerary and its reflection; it is not asserted that they exhaust all period-three eyes or are complete connected components of the hyperbolic set. Nothing is claimed about other attractors, global basins, or nonlinear behavior at the endpoint corners. Numerical area evaluation is supplementary to the exact definite integral. Definitive historical priority and independent validation remain open.

## References
Bhattacharyya, A., and Banerjee, K., *On the Piecewise Linear Perturbations of the Doubling Map*, arXiv:2510.11441v1, October 13, 2025, https://arxiv.org/abs/2510.11441. In particular Sections 2, 4 and 7 and Theorem 2.5.

Misiurewicz, M., and Rodrigues, A., *Double Standard Maps*, Communications in Mathematical Physics (2007), cited for historical context and the distinction from an analytic perturbation family, not used for the proof.
