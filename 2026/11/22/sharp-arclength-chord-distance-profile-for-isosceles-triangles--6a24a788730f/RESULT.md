# Sharp arclength chord-distance profile for isosceles triangles

## Finding
Let \(T_t\) be a Euclidean isosceles triangle with equal side lengths \(1\) and base length \(t\), for \(0<t<2\). Choose \(X,Y\) independently with arclength-uniform distribution on \(\partial T_t\). Set
\[R(t)=\frac{\mathbb E\|X-Y\|}{2+t}.\]
Define \(L(t)=\log\frac{2+t}{t}\) and \(H(t)=\log\frac{2+t}{2-t}\). Then
\[
 R(t)=\frac{8+8t-2t^2+2t^3+2t^4+t^2(1+t)(4-t^2)L(t)+(4-t^2)H(t)}{6(2+t)^3}.
\]
The function is strictly increasing on \((0,1)\), strictly decreasing on \((1,2)\). Its exact range is
\[\frac16<R(t)\le\frac{2+\log3}{18},\]
with equality in the upper bound if and only if \(t=1\) (the equilateral triangle); its lower bound is sharp but unattained in a nondegenerate triangle, approached at both endpoints. More precisely,
\[
R(t)=\frac16+\frac{t^2}{12}\left(\log\frac2t-2\right)+O\left(t^3\log\frac1t\right)\quad(t\downarrow0),
\]
\[
R(2-s)=\frac16+s\left(\frac1{96}\log\frac1s+\frac{7\log2-5}{48}\right)+O\left(s^2\log\frac1s\right)\quad(s\downarrow0),
\]
\[
R(1)-R(t)=\frac{2(\log3-1)}{81}(t-1)^2+O(|t-1|^3)\quad(t\to1).
\]

## Assumptions and scope
The triangle is nondegenerate and Euclidean. Points are independent and **uniform in boundary arclength**, not area-uniform and not vertices. The variable \(t\) is the base-to-leg ratio; similarity reduces all isosceles triangles to \(0<t<2\). The third singular limit \(t\to0\) collapses the short base, while \(t\to2\) flattens the apex, so the rates are not interchangeable.

## Proof
**Exact integration.** For sides of lengths \(a,b\) meeting at an angle of cosine \(q=(a^2+b^2-c^2)/(2ab)\), put
\[I(a,b,c)=\int_0^a\int_0^b\sqrt{x^2+y^2-2qxy}\,dy\,dx.\]
Integration of \(\nabla\!\cdot(z\|z\|)=3\|z\|\) on the parallelogram \(z=xu-yv\), with \(u\cdot v=q\), gives
\[I(a,b,c)=\frac13\left[a\int_0^b\sqrt{a^2+y^2-2qay}\,dy+b\int_0^a\sqrt{x^2+b^2-2qbx}\,dx\right].\]
The arclength same-side integral is \(a^3/3\). Elementary antiderivatives give
\[
I(1,1,t)=\frac13-\frac{t^2}{6}+\frac{t^3}{6}+\frac{t^2(4-t^2)}{12}L(t),
\]
\[
I(1,t,1)=\frac{t^4-t^3}{12}+\frac t3+\frac{t^3(4-t^2)}{24}L(t)+\frac{4-t^2}{24}H(t).
\]
Consequently \(R(t)=\big((2+t^3)/3+2I(1,1,t)+4I(1,t,1)\big)/(2+t)^3\), yielding the displayed formula.

**Global monotonicity.** Differentiation and simplification yield
\[6(2+t)^3R'(t)=F(t)=A(t)L(t)+(t-6)H(t)+2t(t-1)(2t+7),\]
where \(A(t)=-t(t+4)(2t^2-t-2)\). Set \(Q(t)=2t^3+9t^2+3t-6\); then \(A(t)+t-6=-(t-1)Q(t)\). Use the logarithm identity \(L(t)-H(t)=\log((2-t)/t)=2\operatorname{arctanh}(1-t)\). Define \(K(t)=2\operatorname{arctanh}(t-1)/(t-1)\), continuously extended by \(K(1)=2\), to obtain \(L(t)=H(t)-(t-1)K(t)\), and hence
\[F(t)=-(t-1)G(t),\qquad G(t)=A(t)K(t)+Q(t)H(t)-2t(2t+7).\]
We show \(G(t)>0\) on \([1/8,15/8]\), and give simpler analytic bounds on both tails. For \(0<t\le1/8\), \(A(t)/t\ge8\), \(L(t)>\log16>8/3\), \(H(t)\le256t/255\), and \(2t(t-1)(2t+7)\ge-14t\). Therefore
\[F(t)>t\left(\frac{64}{3}-\frac{1536}{255}-14\right)>0.\]
For \(15/8\le t<2\), \(A(t)<0\), \(L(t)\ge 2/(t+1)\) and \(H(t)>3\), the last bound coming from the first five positive terms of the \(\operatorname{arctanh}(t/2)\) series evaluated at \(15/16\). Consequently
\[F(t)\le\frac{2A(t)}{t+1}+3(t-6)+2t(t-1)(2t+7)
 =\frac{(t-2)(11t+9)}{t+1}<0.\]
On the remaining closed interval, `verify.py` uses rational interval arithmetic, not point sampling. It encloses \(H(t)=2\operatorname{arctanh}(t/2)\) and \(K(t)=2\sum_{k\ge0}(t-1)^{2k}/(2k+1)\) by 160-term power series with rigorous positive remainder bounds. For each of 512 rational subintervals, interval multiplication bounds \(A(t)K(t)+Q(t)H(t)-2t(2t+7)\) from below; the least computed exact rational bound exceeds \(0.5766\). All operations use `fractions.Fraction` integers with explicitly outward-rounded fixed-point enclosures; no floating comparison establishes positivity. This proves \(F(t)>0\) for \(t<1\) and \(F(t)<0\) for \(t>1\) globally.

**Endpoints and equality.** Direct limits, Taylor expansion and the derivative formula at \(t=1\) give the claimed sharp endpoint and quadratic coefficients; \(R'(1)=0\) and \(R''(1)=4(1-\log3)/81<0\). Strict monotonicity proves uniqueness of the maximum and rules out equality in the lower bound.

## Verification
Run `python3 verify.py` with standard Python 3. This is an exact rational *continuous-interval positivity certificate*, not a finite sample of parameter values. A separate direct two-dimensional integration of each unordered side pair agreed numerically with the analytic formula at \(t=0.2,0.6,1,1.5,1.95\) to within \(8\times10^{-12}\) in the normalized statistic. Symbolic differentiation independently returned the stated derivative, second derivative, endpoint series and large-ratio tail estimate. Numerical quadratures are corroboration only; the proof relies on the exact integral reduction and analytic/interval inequalities.

## Relationship to prior work
Shen's planar mean-distance theorem [1] concerns boundary-versus-interior expectations; the separate perimeter result [2] gives the universal strict lower bound \(1/6\) for planar convex bodies. Neither statement determines the full isosceles-triangle shape profile, its unique equilateral maximizer, or its two distinct logarithmic degeneration laws. Tokmachev's work [3] establishes the universal disk maximum in the planar convex class, which does not classify the extremal member *within triangles*. The presented result refines the universal lower bound within a natural one-parameter family but does not improve it for all convex bodies.

## Limitations
The global monotonicity and sharp expansions apply only to the similarity family of nondegenerate isosceles Euclidean triangles. No assertion is made for scalene triangles, area-uniform sampling, or other distance powers. The interval certificate is executable and finite but its correctness also depends on the elementary enclosure and Taylor-remainder arguments explicitly shown above. Literature searches are not a guarantee of historical priority. Independent mathematical validation has not been performed.

## References
[1] E. Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances*, arXiv:2608.06470v1, first public 2026-08-06, https://arxiv.org/abs/2608.06470.

[2] E. Shen, *A Sharp Perimeter Inequality for Mean Distances on Convex Curves*, arXiv:2611.21661v1, first public 2026-11-07, https://arxiv.org/html/2611.21661v1.

[3] A. S. Tokmachev, *The Mean Distance Between Random Points on the Boundary of a Convex Figure*, original Russian proceedings article 2022; English translation, Journal of Mathematical Sciences 286 (2024), 798–806, https://www.mathnet.ru/eng/znsl7205.
