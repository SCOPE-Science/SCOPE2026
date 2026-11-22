# Optimal asynchronous scalar observations of Brownian-bridge Lévy area under a precision budget

## Finding

Let \(U,V\) be independent standard Brownian bridges on \([0,1]\), and define the *doubled signed stochastic area*
\[
A=\int_0^1U_t\,\mathrm dV_t-\int_0^1V_t\,\mathrm dU_t.
\]
Suppose a design permits **exactly one scalar point measurement of each coordinate**, possibly at different times:
\[
Y_1=U_s+\epsilon_1,\qquad Y_2=V_t+\epsilon_2,
\]
where \(s,t\in[0,1]\), the independent Gaussian errors are independent of both bridges, their precisions \(p,q>0\) give variances \(p^{-1},q^{-1}\), and \(p+q=P\) for a fixed \(P>0\). The estimator is the exact conditional mean \(\widehat A=\mathbb E[A\mid Y_1,Y_2]\); risk means \(\mathbb E[(A-\widehat A)^2]\).

**Theorem.** For every \(P>0\), the complete set of globally optimal designs consists of the two coordinate-swapped arrangements
\[
(s,t,p,q)=(x_P,1-x_P,P/2,P/2)
\quad\text{and}\quad
(1-x_P,x_P,P/2,P/2).
\]
Here \(x_P\) is the unique root in \((1-1/\sqrt2,1/3)\) of
\[
2x^3-4x^2+x+\frac4P(1-3x)=0.
\]
The exact minimum Bayes risk is
\[
R(P)=\frac13-\left[\frac{x_P^2(1-2x_P)}{x_P(1-x_P)+2/P}\right]^2.
\]
As total precision increases, \(x_P\) decreases strictly from \(1/3\) toward \(1-1/\sqrt2\). More precisely,
\[
\lim_{P\downarrow0}x_P=\frac13,\qquad
\lim_{P\uparrow\infty}x_P=1-\frac1{\sqrt2},
\]
and the maximal captured variance \(G(P)=1/3-R(P)\) satisfies
\[
G(P)=\frac{P^2}{2916}+o(P^2)\quad(P\downarrow0),\qquad
\lim_{P\uparrow\infty}G(P)=17-12\sqrt2.
\]
Thus even arbitrarily precise *two scalar point samples* capture no more than \(3(17-12\sqrt2)\approx0.0883118\) of the total area variance, whereas simultaneous samples \(s=t\) capture exactly zero.

## Assumptions and scope

The bridge coordinates are independent, centered, continuous Gaussian semimartingales with covariance \(K(u,v)=\min(u,v)-uv\) and pinned endpoints. All designs are nonadaptive: times and precisions are chosen without observing the bridges. Exactly one noisy scalar sample of \(U\) and one of \(V\) are allowed, with *independent* instrument noises of known variances. The total precision constraint is additive, not a total sample-count constraint or an unequal-cost constraint. The area has no factor \(1/2\); using geometric area would divide its variance and risk by four. No optimization over general linear path functionals or over measurements of both coordinates at each time is asserted.

## Proof

**1. The exact area and observation covariance.** Standard bridge innovation decompositions yield \(\mathrm dU_t=\mathrm dW^1_t-U_t(1-t)^{-1}\mathrm dt\) and similarly for \(V\). The drift terms cancel in the antisymmetric area, so independent martingale isometry gives
\[
\mathbb EA=0,\qquad \mathbb EA^2=2\int_0^1t(1-t)\,\mathrm dt=\frac13.
\]
Because the two coordinates are independent, the Gaussian covariance identity for stochastic Riemann sums gives
\[
C(s,t):=\mathbb E[A U_sV_t]
=\int_0^1[K(r,s)\,\partial_r K(r,t)-K(r,t)\,\partial_rK(r,s)]\,\mathrm dr.
\]
For \(0<s<t<1\) the integrand is zero outside \((s,t)\), and equals \(s(1-t)\) inside. Consequently \(C(s,t)=s(t-s)(1-t)\). For \(t<s\), interchange coordinates to obtain \(C(s,t)=-t(s-t)(1-s)\). For \(s=t\), \(C=0\).

**2. Conditional expectation and Bayes risk.** The observations \(Y_1,Y_2\) are independent centered Gaussians of variances
\[
v_1=s(1-s)+1/p,\qquad v_2=t(1-t)+1/q.
\]
The area is a bilinear (second-Wiener-chaos) functional with one factor in each independent coordinate. Orthogonal Gaussian regression of each coordinate, or direct Wick conditioning, therefore gives the **exact** conditional mean
\[
\widehat A=\frac{C(s,t)}{v_1v_2}Y_1Y_2.
\]
Its variance is \(C(s,t)^2/(v_1v_2)\), and orthogonality of conditional expectation yields
\[
\mathbb E[(A-\widehat A)^2]=\frac13-\frac{C(s,t)^2}{v_1v_2}.
\]
Boundary and simultaneous designs have zero gain. Every finite positive budget admits a strictly interior positive-gain design, so all optimizers have distinct interior times and positive precision in both channels.

**3. Global centering *and* precision balance.** By swapping coordinate labels if necessary, take \(s<t\). Set \(a=s\), \(b=1-t\), \(g=t-s\), so \(a,b,g>0\) and \(a+b=1-g=:L\). The gain is \(a^2b^2g^2/(v_1v_2)\). Its denominator normalized by \(a^2b^2\) is exactly
\[
D=1+\frac{g}{ab}+\frac1{ab}\left(\frac{1+g/b}{q}+\frac{1+g/a}{p}\right)+\frac1{a^2b^2pq}.
\]
Fix \(g\) and \(P=p+q\). The arithmetic-geometric mean inequality gives \(ab\le L^2/4\) and \(pq\le P^2/4\). The function \(f_g(z)=\sqrt{1+g/z}\), \(z>0\), is strictly convex since
\[
f_g''(z)=\frac{g(3g+4z)}{4z^{5/2}(g+z)^{3/2}}>0.
\]
Cauchy-Schwarz followed by Jensen implies
\[
\frac{1+g/b}{q}+\frac{1+g/a}{p}
\ge\frac{(f_g(a)+f_g(b))^2}{P}
\ge\frac4P\left(1+\frac{2g}{L}\right).
\]
Every positive term in \(D\) is hence bounded below by its value at \(a=b=L/2\), \(p=q=P/2\), with simultaneous equality *only* there. For every fixed gap \(g\), the unique gain-maximizing design is centered and precision-balanced. This establishes global reduction, not merely a symmetry heuristic.

**4. Unique optimal gap and monotonic law.** Write \(a=b=x\in(0,1/2)\) and \(\eta=2/P\). Maximizing gain is equivalent to maximizing
\[
h_\eta(x)=\frac{x^2(1-2x)}{x(1-x)+\eta}>0.
\]
An exact differentiation gives
\[
h_\eta'(x)=\frac{x\,[x(2x^2-4x+1)+2\eta(1-3x)]}{[x(1-x)+\eta]^2}.
\]
Let \(r=1-1/\sqrt2\). The numerator in brackets is positive on \((0,r]\), negative on \([1/3,1/2)\), and strictly decreasing on \((r,1/3)\), because its derivative is \(6x^2-8x+1-6\eta<0\) there. It thus has exactly one zero \(x_\eta\in(r,1/3)\), which is the unique global maximum. Implicit differentiation shows \(\mathrm dx_\eta/\mathrm d\eta>0\) (since \(1-3x_\eta>0\)); equivalently \(x_P\) decreases strictly with \(P\). Endpoint and asymptotic expressions follow by taking \(\eta\to\infty\) and \(\eta\downarrow0\), with
\[
\left[\frac{r(1-2r)}{1-r}\right]^2=(3-2\sqrt2)^2=17-12\sqrt2
\]
and \(h_\eta(1/3)\sim(1/27)/\eta\). As \(\eta=2/P\), the low-budget gain is \(P^2/2916+o(P^2)\). Strict equality classifications in Steps 3–4 give exactly the two label-swapped optimizers. This proves the theorem.

## Verification

The standalone file `verification/check.py` (with `verification/requirements.txt`) checks the normalized denominator identity, the stationarity polynomial, the convexity derivative, the high-precision closed form, and the bridge variance. It also checks exact covariance Riemann sums on four meshes aligned with \(1/3,2/3\), and compares the analytic optimum with 84,000 independent random admissible designs across seven budgets. The executable was run successfully from the actual package directory. These finite tests are supplementary; the quantified theorem rests on the displayed algebra and global inequalities.

## Relationship to prior work

Foster–Habermann (first available preprint 2021) treats Fourier and polynomial Brownian-bridge expansions for Lévy-area approximation, with explicit error rates for Gaussian series truncations. Kastner–Rößler (2022) reviews and compares Fourier-based algorithms for iterated stochastic integrals. Dickinson (2007) proves general Gaussian-information approximation results and asymptotic lower bounds; its abstract and available literature context do not specify the finite two-coordinate noisy point-sampling and fixed precision-allocation problem here. A related earlier exact two-*planar*-observation calculation optimizes four scalar channel measurements at two common times, not two asynchronous scalar measurements with a joint precision constraint. The latter's covariance geometry does not give the strict joint balancing inequality or the present budget law. No claim is made that a bounded literature search proves publication priority.

## Limitations

The result treats a pinned standard Brownian bridge with independent coordinates and a prescribed two-scalar observation architecture. It neither addresses Brownian-motion endpoint information nor multi-time vector observations, correlated measurement noises, unequal precision prices, unknown covariance parameters, or general nonadaptive Gaussian linear measurements. The strict budget law is not an unrestricted optimal approximation theorem for Lévy area. The available public abstract of Dickinson (2007), rather than the complete original text, was inspected; a fuller priority comparison remains desirable. Independent validation has not been performed.

## References

- J. Foster and K. Habermann, *Brownian bridge expansions for Lévy area approximations and particular values of the Riemann zeta function*, arXiv:2102.10095, first public 19 February 2021. https://arxiv.org/abs/2102.10095 ; full open article https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/brownian-bridge-expansions-for-levy-area-approximations-and-particular-values-of-the-riemann-zeta-function/6C1D65580D064B415E14AF19DAE55517
- F. Kastner and A. Rößler, *An analysis of approximation algorithms for iterated stochastic integrals and a Julia and Matlab simulation toolbox*, *Numerical Algorithms* 93 (2023), first online 12 December 2022. https://doi.org/10.1007/s11075-022-01401-z
- A. S. Dickinson, *Optimal Approximation of the Second Iterated Integral of Brownian Motion*, *Stochastic Analysis and Applications* 25 (2007), 1109–1128. https://doi.org/10.1080/07362990701540592
