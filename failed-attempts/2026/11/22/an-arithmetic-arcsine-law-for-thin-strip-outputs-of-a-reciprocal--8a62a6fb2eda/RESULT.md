# An arithmetic arcsine law for thin-strip outputs of a reciprocal sine-square map

## Finding

For arbitrary fixed \(a,b>0\), define the map
\[
F_{a,b}(x,y)=\bigl(\sin^2(a\pi/x+b y),\;\sin^2(b\pi y+a x)\bigr),\qquad (x,y)\in(0,1)^2.
\]
Let \(X_\delta\sim\operatorname{Unif}(0,\delta)\) and \(Y\sim\operatorname{Unif}(0,1)\) be independent, where \(0<\delta<1\), and denote by \(\nu_\delta\) the law of \(F_{a,b}(X_\delta,Y)\).

For \(0<v<1\), let \(M_b(v)\) be the number of solutions of \(\sin^2\rho=v\) with \(0<\rho<b\pi\). Then the probability measures \(\nu_\delta\) converge in **total variation** to the probability distribution on \((0,1)^2\) with density
\[
\boxed{\displaystyle p_b(u,v)=\frac{M_b(v)}{2b\pi^2\sqrt{u(1-u)v(1-v)}}.}
\]
This density is defined almost everywhere; it may be assigned either one-sided value at the finitely many target levels corresponding to \(\sin^2(b\pi)\). The limit **does not depend on \(a\)** and has independent coordinates: its first marginal is the arcsine law, while its second is the pushforward of uniform phase on \((0,b\pi)\) under \(\sin^2\).

Moreover, both marginals are arcsine **if and only if** \(2b\) is a positive integer. In that case
\[
\boxed{\displaystyle p_b(u,v)=\frac1{\pi^2\sqrt{u(1-u)v(1-v)}}}
\]
and the limit is independent of **both** parameters.

At every fixed strictly interior target \((u,v)\), define the inverse-Jacobian weight in the singular strip by
\[
W_\delta(u,v)=\sum_{\substack{F_{a,b}(x,y)=(u,v)\\0<x<\delta,\ 0<y<1}}
\frac1{|\det DF_{a,b}(x,y)|}.
\]
Every term is regular; the sum is absolutely convergent. Using the pointwise phase count \(M_b^+(v)=\#\{\rho\in(0,b\pi]:\sin^2\rho=v\}\), including equality at the upper endpoint, one has
\[
\boxed{\displaystyle W_\delta(u,v)=\delta\,\frac{M_b^+(v)}{2b\pi^2\sqrt{u(1-u)v(1-v)}}+O_{a,b,u,v}(\delta^2).}
\]
The distinction between \(M_b\) and \(M_b^+\) affects only a null set in output space.

## Assumptions and scope

All results are exact-real statements for fixed \(a,b>0\), and the input rectangle is \((0,\delta)\times(0,1)\). The map is undefined at \(x=0\), which is excluded. The outputs lie in \([0,1]^2\), while the theorem's density formulas concern \((u,v)\in(0,1)^2\). Total variation is \(\sup_E|\nu_\delta(E)-\nu(E)|\), equal to half the \(L^1\) distance between the densities. Parameter-uniform error bounds are not claimed. The density is not asserted to be stationary for repeated iterations.

## Proof

**1. Exact scalar inverse sheets.** Fix \((u,v)\in(0,1)^2\) and put \(\theta=\arcsin\sqrt v\), \(\phi=\arcsin\sqrt u\), both in \((0,\pi/2)\). All positive solutions of the second inverse equation have phases
\[
\rho=k\pi+\theta\quad\text{or}\quad\rho=(k+1)\pi-\theta,
\qquad k=0,1,2,\ldots,
\]
with ordinate \(y_\rho(x)=(\rho-a x)/(b\pi)\). When \(x\downarrow0\), the admissible phases are precisely the finite set \(0<\rho\le b\pi\); any larger phase is eventually inadmissible. The equality case is admissible for every sufficiently small positive \(x\) because \(y_\rho(x)=1-a x/(b\pi)<1\). For a fixed admissible phase, the first inverse equation reduces to
\[
\frac a x+\frac\rho{\pi^2}-\frac{a x}{\pi^2}=n+\frac\psi\pi,
\qquad\psi\in\{\phi,\pi-\phi\},
\]
for all sufficiently large positive integers \(n\). With \(L=n+\psi/\pi-\rho/\pi^2\), its unique positive solution is
\[
\boxed{\displaystyle x_{\rho,n,\psi}=\frac{2a}{L+\sqrt{L^2+4a^2/\pi^2}}=\frac aL-\frac{a^3}{\pi^2L^3}+O_{a,\rho,\psi}(L^{-5}).}
\]
Each large \(n\) gives two distinct solutions per allowed \(\rho\), with no missing small-\(x\) inverse sheets.

**2. Jacobian and summation.** Let \(A=a\pi/x+b y\), \(B=b\pi y+a x\). Direct differentiation gives
\[
\det DF_{a,b}(x,y)=-ab\left(1+\frac{\pi^2}{x^2}\right)\sin(2A)\sin(2B).
\]
At a strictly interior inverse target, \(|\sin(2A)\sin(2B)|=4\sqrt{u(1-u)v(1-v)}>0\). Thus all inverse points are regular and
\[
\frac1{|\det DF|}=\frac1{4ab(1+\pi^2/x^2)\sqrt{u(1-u)v(1-v)}}.
\]
Each branch \((\rho,\psi)\) has \(x_{\rho,n,\psi}=a/(n+O(1))+O(n^{-3})\), so its inverse-Jacobian weight is
\[
\frac{a}{4b\pi^2\sqrt{u(1-u)v(1-v)}}\frac1{(n+O(1))^2}+O_{a,b,u,v}(n^{-4}).
\]
The condition \(x<\delta\) selects \(n>a/\delta+O_{a,b,u,v}(1)\), and the reciprocal-square tail satisfies
\[
\sum_{n>a/\delta+O(1)}\frac1{(n+O(1))^2}=\frac\delta a+O_{a,b,u,v}(\delta^2).
\]
Summing two phases \(\psi\) per admissible \(\rho\) proves the inverse-Jacobian expansion and its absolute convergence. This establishes the coefficient independently of the unweighted number of inverse sheets.

**3. Pushforward density and total-variation convergence.** The determinant vanishes in the input strip only where one of two nonconstant analytic sine factors is zero; those level curves have two-dimensional Lebesgue measure zero. Covering the input strip by countably many regular inverse charts and applying change of variables shows that the pushforward of normalized area has a probability density \(q_\delta(u,v)=W_\delta(u,v)/\delta\) almost everywhere. By step 2, \(q_\delta(u,v)\to p_b(u,v)\) for almost every interior output. The limit integrates to one: \(M_b(v)/(2b\pi\sqrt{v(1-v)})\) is exactly the pushforward density of uniform \(\rho\in(0,b\pi)\) under \(v=\sin^2\rho\), and \(1/(\pi\sqrt{u(1-u)})\) is a probability density. Thus \(\int q_\delta=\int p_b=1\). Scheffé's lemma yields \(\|q_\delta-p_b\|_{L^1}\to0\), equivalently the claimed total-variation convergence. The factorization of \(p_b\) proves independence.

**4. Sharp arithmetic resonance.** If \(2b\) is a positive integer, the interval \((0,b\pi)\) is a union of complete monotonic half-periods of \(\sin^2\), so almost every target \(v\) has \(M_b(v)=2b\) inverse phases. Conversely, when \(2b\) is not an integer, the final incomplete monotone half-period contributes one extra inverse precisely to a nontrivial subinterval of output levels; thus \(M_b(v)\) is not almost everywhere constant. The limiting second marginal equals the arcsine density exactly in the former case. In particular, integer and half-integer phase gains, not just integer gains, give the same parameter-independent product-arcsine output law.

## Verification

Run `python checks/check_boundary_law.py` with Python, SymPy installed. This standalone file symbolically checks the exact Jacobian identity, constructs the explicit preimage sheets, checks their forward residuals, and compares finite annulus inverse-Jacobian densities to the derived leading density at several integer, half-integer and nonresonant gains. It also checks the zero-sheet case. These finite computations verify algebra and numerical agreement only; the infinite tail asymptotics and total-variation statement are proved in the preceding steps.

## Relationship to prior work

Zhu, Deng, Zhang and Zhu introduced the same coupled sine-square map and numerically studied its attractors, Lyapunov exponents, nonlinear randomness indicators, and a proposed encryption application [1]. The full accessible original article's mathematical model, dynamical analysis and conclusion do not give the one-step thin-strip pushforward limit. A previously developed inverse-point census for this map already counts its small-\(x\) antecedents and describes equal-weight inverse-coordinate distributions; that unweighted census is **not** claimed as new here. A separate analysis of the same map classifies accumulating fixed-point saddles [2], which is a different problem. The present theorem establishes the **inverse-Jacobian-weighted** pushforward density, the strong total-variation limit and the sharp half-integer phase-gain resonance. It does not follow from unweighted preimage counting alone.

## Limitations

The input law concentrates near an excluded singular boundary; it is neither an invariant measure nor a model of all possible initializations. The result does not claim equidistribution of long orbits, hyperchaos, cryptographic strength, state-estimation identifiability in floating-point arithmetic, or parameter-uniform rates. Its total-variation result is for exact real arithmetic. Comparison with unindexed earlier literature may alter publication priority; this is not an independent audit.

## References

1. S. Zhu, X. Deng, W. Zhang, C. Zhu, *Construction of a New 2D Hyperchaotic Map with Application in Efficient Pseudo-Random Number Generator Design and Color Image Encryption*, *Mathematics* 11 (2023), article 3171, published 2023-07-19. https://doi.org/10.3390/math11143171. Equation (1), Sections 2 and 6.
2. *Two fixed-point saddles per reciprocal phase band in a coupled sine-square map*, published mathematical research record (2026-11-02). Fixed-point band and multiplier classification, not a one-step output-density result.
