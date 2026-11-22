# A sharp cubic area and quartic perimeter transition for finite circular-involute hulls

## Finding

Let \(z(t)=e^{it}(1-it)\in\mathbb C\), \(t\geq0\), be the unit-circle involute, and let \(K_T=\operatorname{conv}\{z(t):0\leq t\leq T\}\), \(T>0\). There is exactly one threshold \(\alpha\in(\pi,3\pi/2)\) satisfying \(\tan\alpha=\alpha\), numerically \(\alpha=4.493409457909064\ldots\). For \(T\leq\alpha\), the whole generating arc lies on the curved hull boundary. For \(T>\alpha\), exactly the terminal interval \([s(T),T]\) remains on that curved boundary: its left endpoint \(s(T)>0\) is uniquely determined by
\[
T=\frac{\Delta-\sin\Delta}{1-\cos\Delta},\qquad \Delta=T-s(T)\in(\alpha,2\pi).
\]
The hull boundary consists of that terminal involute arc followed by its closing chord. Its area \(A(T)\) and perimeter \(P(T)\) have the exact formulas in the proof.

Put \(\rho=\sqrt{1+\alpha^2}\), \(k=1-\rho^{-1}\), and define the analytic comparison expressions
\[
A_0(T)=\frac{T^3}{6}+\frac{T\cos T-\sin T}{2},\qquad
P_0(T)=\frac{T^2}{2}+\sqrt{T^2+2-2\cos T-2T\sin T}.
\]
For \(T\leq\alpha\) these equal the actual hull area and perimeter. As \(T\downarrow\alpha\) from above, respectively,
\[
A(T)-A_0(T)=\frac{(\rho+1)k^3}{12}(T-\alpha)^3+O((T-\alpha)^4),
\]
\[
P(T)-P_0(T)=-\frac{k^4}{24}(T-\alpha)^4+O((T-\alpha)^5).
\]
Both constants are strictly positive in absolute value. Consequently the hull area is \(C^2\) but not \(C^3\), and the hull perimeter is \(C^3\) but not \(C^4\), at this unique first contact transition. Moreover the exposed-arc parameter length approaches one full turn according to
\[
T-s(T)=2\pi-2\sqrt{\pi/T}+O(T^{-3/2})\quad(T\to\infty).
\]

## Assumptions and scope

All geometry is Euclidean in \(\mathbb R^2\). The source circle has radius one; any other radius multiplies perimeter by that radius and area by its square. The generating involute is the single branch parametrized above, starting at its cusp at \(t=0\). \(K_T\) is the convex hull of the **entire continuous arc**, not of a finite point sample. A point is exposed here when it is the unique maximizer of a linear functional; at the transition endpoint the supporting chord also shares a support line, so its contact point is a boundary point but not strictly exposed in the unique-maximizer sense. More precisely, the relative interiors of the listed involute arcs are strictly exposed, and the listed parameter ranges exhaust the curved hull boundary. Area is positive unsigned planar area; the comparison \(A_0\) for \(T>\alpha\) is a *signed closing-path area*, not asserted to equal any nonconvex set's unsigned area.

## Proof

**1. Support test.** Differentiation gives \(z'(t)=te^{it}\) and \(\operatorname{Im}(\overline{z(t)}z'(t))=t^2\). The clockwise normal to a regular tangent at parameter \(u>0\) is \(-ie^{iu}\). Its scalar product with \(z(v)-z(u)\) is \(-H_u(v-u)\), where
\[
H_u(w)=u(1-\cos w)+\sin w-w\cos w,
\qquad H_u'(w)=(u+w)\sin w.
\]
For \(0\leq v<u\), \(H_u(v-u)>0\): as a function of \(v\), its only internal critical points are \(v=u-j\pi\), where its values are \(j\pi>0\) for positive even \(j\), and \(2u-j\pi>0\) for odd \(j\) with \(v\geq0\); at \(v=0\) it is \(u-\sin u>0\). For \(u<v\leq T\) and \(T-u<2\pi\), \(H_u\) rises until \(w=\pi\) and then falls, so the tangent supports the entire arc precisely when \(H_u(T-u)\geq0\). Writing \(d=T-u\), this is
\[
H_u(T-u)=(1-\cos d)\left(T-f(d)\right),\quad
f(d)=\frac{d-\sin d}{1-\cos d}.
\]
If \(T-u\geq2\pi\), the later point \(z(u+2\pi)\) has strictly greater support in the same normal direction; therefore the old point cannot be on a curved exposed boundary.

**2. Unique terminal arc.** Direct differentiation yields
\[
f'(d)=\frac{2(1-\cos d)-d\sin d}{(1-\cos d)^2}>0\qquad(0<d<2\pi).
\]
For \(d\leq\pi\) positivity is equivalent to \(\sin(d/2)>(d/2)\cos(d/2)\), and for \(\pi\leq d<2\pi\) it is immediate since \(\sin d\leq0\). Also \(f(d)-d=(d\cos d-\sin d)/(1-\cos d)\); its numerator has derivative \(-d\sin d\), hence has exactly one positive zero \(\alpha\) in \((\pi,3\pi/2)\). Thus \(f(d)\leq d\) on \((0,\alpha]\), and for every \(T>\alpha\) there is a unique \(\Delta\in(\alpha,2\pi)\) with \(f(\Delta)=T\). This proves the asserted supporting-tangent interval with \(s=T-\Delta\). Before threshold the support test holds for all \(0<u\leq T\).

For \(T>\alpha\), the line tangent at \(s\) also contains \(z(T)\), because \(H_s(T-s)=0\); the chord from \(z(T)\) to \(z(s)\) follows the positive tangent direction \(e^{is}\), since \(\sin\Delta<0\). Every earlier point lies strictly on the inner side of each terminal-arc tangent (by the first support inequality), so no earlier point becomes an alternative hull boundary arc. The terminal arc turns through \(\Delta<2\pi\); its tangent lines are globally supporting, and its endpoint-to-start chord is globally supporting as the tangent at \(s\). It therefore bounds the convex hull, with no missing pieces. For \(T\leq\alpha\), all arc tangents support globally, so the entire arc and its single endpoint chord bound the hull. At \(T=\alpha\), the endpoint chord is tangent at the initial cusp. In the postcritical case \(s>0\), every \(t<s\) is strictly inside the resulting closed hull: all terminal-arc support inequalities are strict for it, including the chord tangent at \(s\).

**3. Exact intrinsic volumes.** Write \(s=0,\Delta=T\) for \(T\leq\alpha\), otherwise use the contact solution. Integrating \(|z'(t)|=t\) and the oriented area integrand \(\operatorname{Im}(\overline{z(t)}z'(t))=t^2\), and closing by the chord, gives for every \(T>0\)
\[
P(T)=\frac{T^2-s^2}{2}+|z(T)-z(s)|,
\]
\[
A(T)=\frac{T^3-s^3}{6}-\frac{(1+sT)\sin\Delta-\Delta\cos\Delta}{2}.
\]
For \(T>\alpha\) the chord length also simplifies to \(1-\cos\Delta-T\sin\Delta\). Substitution \(s=0\) yields precisely \(A_0,P_0\).

**4. Critical regularity.** The contact equation and the implicit function theorem apply at \(T=\alpha\). From \(\sin\alpha=\alpha\cos\alpha\), \(\cos\alpha=-1/\rho\), and differentiation of \(f\), one gets \(f'(\alpha)=\rho\). Hence for \(\eta=T-\alpha\downarrow0\),
\[
s(T)=k\eta+O(\eta^2),\qquad k=1-1/\rho>0.
\]
For a variable initial cut \(v\in[0,s(T)]\), define the area enclosed by the parameter arc \([v,T]\) and its chord by the same signed integral \(A(T,v)\). Differentiating with respect to \(v\) gives
\[
\partial_v A(T,v)=-\frac v2 H_v(T-v).
\]
Uniformly for \(0\leq v\leq s(T)\), the support gap satisfies
\[
H_v(T-v)=(\rho+1)(v-k\eta)+O(\eta^2).
\]
Integrating from \(v=0\) to \(v=s(T)\) proves the cubic coefficient.

For the perimeter comparison set \(Q=z(T)-z(v)=e^{iv}(-J+iH)\), with \(H=H_v(T-v)\) and \(J=1-\cos(T-v)-T\sin(T-v)>0\) near the threshold. Then the derivative of arc length plus chord length is exactly
\[
\partial_v P(T,v)=v\left(\frac{J}{\sqrt{J^2+H^2}}-1\right).
\]
Since \(J=\rho+1+O(\eta)\), its uniform leading term is \(-v(v-k\eta)^2/2\). Integrating to \(s(T)\) proves the negative quartic coefficient. Analyticity on each side gives the stated sharp differentiability orders. Finally, \(f(2\pi-u)=4\pi/u^2+\pi/3+O(u)\), yielding \(u=2\sqrt{\pi/T}+O(T^{-3/2})\) for the exposed window.

## Verification

Run `python3 checker.py` with Python 3 (standard library only). The checker independently constructs convex hulls of 7,001 sampled points for 11 parameter values from \(T=0.25\) to \(T=50\); compares polygon area, perimeter, and earliest exposed-arc parameter against the proved formulas; and tests the cubic and quartic coefficients on five decreasing positive offsets. It passed 44 assertions. The numerical polygons are supplemental finite approximations and are not used as infinite or exhaustive proof. The critical identities and support inequalities above provide the analytic argument.

## Relationship to prior work

The circular involute parametrization is classical; see the MacTutor reference below. Longinetti, Manselli and Venturi (first published 27 July 2016) study involutes of general convex boundaries and bounding regions for self-distancing curves, including convex-hull constructions; their investigated domains and results differ from the exact terminal exposed interval, first contact equation, and the area/perimeter singularity orders here. Previously published finite-hull results for Archimedean and logarithmic spiral arcs concern different parametrizations, supporting-chord equations and onset geometry; their statements do not imply the displayed circular-involute coefficients. A search-based priority comparison cannot rule out all historical or unpublished equivalent results.

## Limitations

The theorem is for one specified branch of the involute of a circle, convex hulls of *continuous finite arcs*, and Euclidean area/perimeter. No claim is made for arbitrary involutes or other spiral families, or for a general theorem giving the same transition exponents. The formulas are exact, but the analytic comparison functions above are not the unsigned area/perimeter of a convex hull beyond the critical point. Historical originality has not been independently established.

## References

1. M. Longinetti, P. Manselli, A. Venturi, *Bounding Regions to Plane Steepest Descent Curves of Quasiconvex Families*, Journal of Applied Mathematics (2016), article 4873276, first published 27 July 2016. https://doi.org/10.1155/2016/4873276
2. MacTutor History of Mathematics, *Involute of a Circle*, https://mathshistory.st-andrews.ac.uk/Curves/Involute/ (classical parametrization; publication date of this webpage not used for temporal eligibility).
