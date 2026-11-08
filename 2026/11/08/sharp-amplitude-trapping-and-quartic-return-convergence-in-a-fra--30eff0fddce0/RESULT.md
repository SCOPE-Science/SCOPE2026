# Sharp amplitude trapping and quartic return convergence in a fractional kinetic map

## Finding
Let \(0<a<1/2\), \(\eta>2\), and consider
\[
F_{a,\eta}(x)=x-\frac{\eta x}{(1+x^2)^a},\qquad x\in\mathbb R.
\]
Set \(R=\sqrt{(\eta/2)^{1/a}-1}\) and \(H(r)=|F_{a,\eta}(r)|\) for \(r\ge0\). The only nonfixed orbit of least period two is \(\{R,-R\}\), which is locally attracting for every such parameter pair.

**Sharp global amplitude-trapping criterion.** The interval \([0,R]\) is forward invariant under \(H\) if and only if
\[
a\le\frac14\quad\text{or}\quad\left(\frac14<a<\frac12\text{ and }2<\eta\le\eta_c(a)\right),
\qquad \eta_c(a)=2\left(\frac{4a}{4a-1}\right)^a.
\]
Within this region, every initial value whose forward orbit never hits zero has \(|F_{a,\eta}^{n}(x)|\to R\). For \(0<|x|<R\), its successive amplitudes increase strictly to \(R\). If \(1/4<a<1/2\) and \(\eta=\eta_c(a)\), every nonexceptional initial amplitude, including those initially larger than \(R\), eventually enters \((0,R)\) and subsequently increases to \(R\).

**Exact quartic return at the critical tuning.** For \(1/4<a<1/2\), at \(\eta=\eta_c(a)\) put
\[
B_a=\frac{(5a-1)\sqrt{4a-1}}{4a}>0.
\]
For every orbit that never lands exactly on zero or on the period-two orbit, its amplitude \(r_n=|F_{a,\eta}^{n}(x)|\) obeys
\[
\lim_{n\to\infty}\frac{R-r_{n+1}}{(R-r_n)^2}=B_a,\qquad
\lim_{n\to\infty}\frac{R-r_{n+2}}{(R-r_n)^4}=B_a^3.
\]
Thus the original one-step map has a quadratic error law between the two phases, and the physical two-step period return has order four, with its exact nonzero coefficient. The excluded starting points form a countable set of finite preimages of \(0\), \(R\), and \(-R\).

For \(1/4<a<1/2\) and \(\eta>\eta_c(a)\), the invariant-interval property fails sharply: some \(r\in(0,R)\) satisfies \(H(r)>R\), and every sufficiently close, nonperiodic amplitude alternates sides of \(R\) at each iteration while converging to it.

## Assumptions and scope
The map is the one-dimensional smooth discrete dynamical system above with real state and fixed \(0<a<1/2\), \(\eta>2\). Its nonlinear step \(g_a(x)=x/(1+x^2)^a\) is odd, strictly increasing, and the derivative of a strictly convex even kinetic potential. The results concern this exact scalar map, not a multicomponent momentum optimizer. The exact quartic law applies only at the specified critical tuning and excludes finite-hit initial states so its denominator remains nonzero. No claims about all initial conditions converging to the cycle are made outside the amplitude-trapping region.

## Proof
**1. Monotone kinetic step and unique prime-two orbit.** Direct differentiation gives
\[
g_a'(r)=\frac{1+(1-2a)r^2}{(1+r^2)^{a+1}}>0,\quad
g_a''(r)=-\frac{2ar[3+(1-2a)r^2]}{(1+r^2)^{a+2}}<0\quad(r>0).
\]
If \(F(x)=y\) and \(F(y)=x\), adding the two equations yields \(g_a(x)+g_a(y)=0\). Strict increase and oddness force \(y=-x\). The nonzero cycle equation is \(\eta/(1+x^2)^a=2\), which has exactly the two solutions \(\pm R\). Its one-step derivative at either point is \(1-2e_R\), where
\[
e_R=\frac{R g_a'(R)}{g_a(R)}=\frac{1+(1-2a)R^2}{1+R^2}\in(0,1).
\]
Therefore the period-return multiplier is \((1-2e_R)^2<1\).

**2. Radial comparison and exact trapping condition.** Write \(q(r)=\eta/(1+r^2)^a\). For \(0<r<R\), \(q(r)>2\), hence \(H(r)=\eta g_a(r)-r=:h(r)>r\). For \(r>R\), \(0<q(r)<2\), so \(H(r)<r\). On \([0,R]\), \(h\) is strictly concave, \(h(0)=0\), and \(h(R)=R\). A differentiable concave function with these endpoint values satisfies \(h([0,R])\subseteq[0,R]\) exactly when \(h'(R)\ge0\): if its final slope is nonnegative it increases everywhere, whereas if negative it takes a value above \(R\) immediately to the left of the endpoint. Here
\[
h'(R)=\eta g_a'(R)-1=2e_R-1=\frac{1+(1-4a)R^2}{1+R^2}.
\]
For \(a\le1/4\) this is positive at every finite \(R\). For \(a>1/4\), it is nonnegative exactly when \(R^2\le(4a-1)^{-1}\); substituting the formula for \(R\) yields precisely \(\eta\le\eta_c(a)\). Strict negativity beyond this bound gives both the stated failure of trapping and local side-alternation, since \(-1<h'(R)<0\) and \(H\) is differentiable near \(R\).

**3. Global convergence inside the trapping region.** If \(0<r_0<R\), then \(r_n=H^n(r_0)\) is strictly increasing, remains below \(R\), and its limit must be a positive fixed point of \(H\). The only such point is \(R\): when \(H(r)=r\), the equation \(|1-q(r)|=1\) gives \(q(r)=2\) (\(q=0\) is impossible). For an initial \(r_0>R\), amplitudes strictly decrease until either crossing below \(R\), reaching \(0\), reaching \(R\), or decreasing indefinitely to a fixed point \(R\). Thus every nonzero trajectory that avoids \(0\) converges in amplitude to \(R\) in the trapping region. At the critical tuning \(h'(R)=0\) and \(h''(R)=\eta g_a''(R)<0\), so \(H(r)<R\) for every sufficiently close \(r>R\). Consequently a trajectory descending from above \(R\) cannot remain above forever and must cross into \((0,R)\), unless it hits an exceptional state. After crossing it increases strictly.

**4. Exact quartic coefficient.** At the critical tuning, \(H(R)=R\), \(H'(R)=0\), and
\[
-\frac{H''(R)}2=-\frac{\eta g_a''(R)}2=
\frac{2aR[3+(1-2a)R^2]}{(1+R^2)^2}
=\frac{(5a-1)\sqrt{4a-1}}{4a}=B_a.
\]
Taylor's theorem therefore gives \(R-H(R+\delta)=B_a\delta^2+O(|\delta|^3)\) from either side. Composition yields \(R-H^2(R+\delta)=B_a^3\delta^4+O(|\delta|^5)\). The globally convergent nonexceptional trajectory eventually lies below \(R\) and approaches it, proving both limits. A nonconstant analytic map of the line has discrete preimage sets of each finite target; here strict convexity of \(F\) on each positive halfline, oddness, and the behavior at infinity imply each inverse fibre is finite. The union of all finite iterated preimages of \(\{0,R,-R\}\) is therefore countable.

## Verification
The standalone checker `check.py` verifies the exact second-derivative and elasticity identities symbolically, six parameter/interval regimes, the critical derivative zero at three independent exponents, sampled global attraction from twelve starts, the sharp algebraic \(n^{-1/2}\) law for the separate \(\eta=2\) boundary, and the quartic two-step coefficient using 85-digit arithmetic. Reproduce with `python check.py` (Python 3, SymPy, mpmath). The full interval assertions and asymptotic statements are proved analytically above; finite samples do not establish them.

## Relationship to prior work
Itin, *Physics-Inspired Optimizers beyond the Edge of Stability* (arXiv:2610.27321, initially posted 2026-10-19), establishes local elasticity criteria for symmetric kinetic-map two-cycles, with global attraction studied numerically for several map families. It does not state the present fractional-family trapping frontier, exact parameter-independent exponent division at \(a=1/4\), or global quartic-return tuning. Ma, Kunin, Wu, and Ying, *Beyond the Quadratic Approximation* (arXiv:2204.11326, 2022), already prove almost-everywhere global convergence to a period-two orbit for one-dimensional even convex objectives with strictly decreasing curvature. That general convergence result is not claimed as new here. The contribution here concerns the sharp **one-step invariant amplitude barrier**, exact location of a globally captured superattracting two-cycle, and its **nonzero fourth-order return coefficient**. Similar high-order local cancellations in other optimization schemes are not claimed to be new in principle.

## Limitations
The amplitude-trapping criterion does not assert that trajectories fail to approach the period-two orbit outside the stated region; it only proves local side alternation and loss of one-step trapping there. The fractional exponent lies strictly in \((0,1/2)\), and momentum and multi-dimensional coupling are not treated. The exact fourth-order return law is asymptotic and excludes trajectories landing exactly on the cycle or zero. Independent mathematical validation and exhaustive historical priority confirmation have not been performed.

## References
1. Alexander Itin, *Physics-Inspired Optimizers beyond the Edge of Stability: Period-Two Orbits and Delayed Instability*, arXiv:2610.27321, first public version 2026-10-19. https://arxiv.org/abs/2610.27321
2. Chao Ma, Daniel Kunin, Lei Wu, Lexing Ying, *Beyond the Quadratic Approximation: The Multiscale Structure of Neural Network Loss Landscapes*, arXiv:2204.11326 (2022), particularly Section 4.1, Theorem 1. https://arxiv.org/abs/2204.11326
