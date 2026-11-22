# A flat normal Lyapunov spectrum with Gaussian fluctuations on a cubic predator-free boundary

## Finding
Consider the real extension of the two-dimensional discrete predator–prey map of Hong and Zhang (2023),
\[
\begin{aligned}
N_{j+1}&=N_j+\frac h\varepsilon\left[\frac{N_j(1-N_j)(N_j-\theta)}{1+fP_j}-N_jP_j\right],\\
P_{j+1}&=P_j+h(N_j-m)P_j.
\end{aligned}
\]
Choose \(\theta=1/2\), \(h=2\sqrt2\), \(\varepsilon=\sqrt2/4\), arbitrary \(f>0\), and \(m>0\). The invariant axis \(P=0\) carries a compact invariant interval
\[
I=\left[\frac12-\frac1{\sqrt2},\frac12+\frac1{\sqrt2}\right]
\]
with an ergodic arcsine probability \(\mu\). The invariant probability's normal linearized cocycle is the product of the scalar factors \(1+h(N_j-m)\). Its almost-everywhere normal Lyapunov exponent is exactly
\[
\boxed{L(m)=\begin{cases}
0,&|A(m)|\le2,\\
\log\!\left(\frac{|A(m)|+\sqrt{A(m)^2-4}}2\right),&|A(m)|>2,
\end{cases}\qquad A(m)=1+2\sqrt2\left(\frac12-m\right).}
\]
In particular, the entire mortality interval
\[
\boxed{\frac12-\frac1{2\sqrt2}\le m\le\frac12+\frac3{2\sqrt2}}
\]
has the **same zero normal Lyapunov exponent**, whereas \(L(m)>0\) for all other \(m>0\).

At the intrinsic midpoint \(m_*=1/2+1/(2\sqrt2)\), take \(N_0\sim\mu\) and define the stationary finite-horizon normal log-amplitude
\[
S_n=\log\left|\prod_{j=0}^{n-1}\bigl(1+h(N_j-m_*)\bigr)\right|.
\]
For every positive integer \(n\) and every nonnegative integer \(k\), the exact covariance, variance, and fluctuation limit are
\[
\boxed{\begin{aligned}
\mathbb E S_n&=0,\\
\operatorname{Cov}(\log|1+h(N_0-m_*)|,\log|1+h(N_k-m_*)|)&=\frac{\pi^2}{12\,3^k},\\
\operatorname{Var}(S_n)&=\frac{\pi^2}{6}n-\frac{\pi^2}{8}(1-3^{-n}),\\
\frac{S_n}{\sqrt n}&\ \Longrightarrow\ \mathcal N\!\left(0,\frac{\pi^2}{6}\right).
\end{aligned}}
\]
The last convergence is in distribution over stationary initial conditions; it is not an orbitwise assertion. Thus a zero asymptotic transverse exponent coexists with explicit, genuinely growing square-root-scale normal logarithmic fluctuations.

## Assumptions and scope
All equations are interpreted on real phase space; the theorem is specifically about the invariant axis \(P=0\), the invariant interval \(I\), and the **infinitesimal normal quotient**, not a positive-predator orbit. The interval \(I\) includes negative prey coordinates and prey coordinates above carrying capacity. It is **not wholly biologically admissible**. Consequently no claim of physical predator invasion, nonlinear persistence, extinction, or a biologically invariant positive phase-space region follows. The fear parameter \(f>0\) drops out on \(P=0\). The initial prey state has the stationary arcsine law for ensemble identities; the exponent holds for \(\mu\)-almost every fixed initial prey state. The discrete set of seeds for which a normal multiplier vanishes can be excluded without changing any probabilistic statement. Natural logarithms are used throughout.

## Proof
**1. Exact expanding cubic boundary.** With \(z=\sqrt2(N-1/2)\), the prey map at \(P=0\) is
\[
z_{j+1}=3z_j-4z_j^3=-T_3(z_j),\qquad T_3(\cos\omega)=\cos(3\omega).
\]
The interval \([-1,1]\) is invariant. Writing \(z_0=\cos\omega\), its exact orbit is \(z_j=(-1)^j\cos(3^j\omega)\). Haar-distributed \(\omega\) on \([0,2\pi)\) pushes forward to the arcsine law \(dz/(\pi\sqrt{1-z^2})\). The angle endomorphism \(\omega\mapsto3\omega+\pi\pmod{2\pi}\) preserves Haar measure and is mixing, hence ergodic, so \(\mu\) is invariant and ergodic.

**2. Full normal exponent plateau.** The Jacobian along the invariant axis is upper triangular, and the induced one-dimensional normal quotient multiplies by \(1+h(N-m)=A(m)+2z\). Its \(n\)-step product is thus exact; the prey-to-predator off-diagonal entry in the full Jacobian does not affect the normal quotient. By Birkhoff's ergodic theorem, the almost-everywhere logarithmic exponent is
\[
L(m)=\frac1{2\pi}\int_0^{2\pi}\log|A(m)+2\cos\omega|\,d\omega.
\]
All these logarithmic observables are integrable, even where the multiplier has a zero. The classical harmonic logarithmic-potential identity gives zero for \(|A|\le2\), and \(\log((|A|+\sqrt{A^2-4})/2)\) otherwise. The two roots of \(|A(m)|=2\) give precisely the displayed mortality interval.

**3. Correlations at the distinguished midpoint.** At \(m=m_*\), the multiplier is \(2z_j\), so \(S_n=\sum_{j=0}^{n-1}\phi(3^j\omega)\), with \(\phi(t)=\log|2\cos t|\). The sign \((-1)^j\) disappears in the absolute value. The \(L^2\) Fourier series
\[
\phi(t)=\sum_{r=1}^{\infty}\frac{(-1)^{r+1}}r\cos(2rt)
\]
converges in \(L^2([0,2\pi])\) and has mean zero. Orthogonality shows the lag-\(k\) covariance equals
\[
\frac12\sum_{r=1}^{\infty}\frac{(-1)^{r+1}(-1)^{3^kr+1}}{r\,(3^kr)}
=\frac1{2\cdot3^k}\sum_{r=1}^{\infty}\frac1{r^2}
=\frac{\pi^2}{12\cdot3^k}.
\]
The signs agree because \(3^k\) is odd. This calculation uses \(L^2\) approximation followed by Cauchy–Schwarz, not pointwise interchange at the logarithmic singularities. Stationarity gives
\[
\operatorname{Var}S_n=n\frac{\pi^2}{12}+2\sum_{k=1}^{n-1}(n-k)\frac{\pi^2}{12\cdot3^k}.
\]
The exact geometric sum \(\sum_{k=1}^{n-1}(n-k)3^{-k}=n/2-3/4+(3/4)3^{-n}\) yields the stated variance for every \(n\ge1\).

**4. Central limit theorem, not just a moment extrapolation.** Let \(T(t)=3t+\pi\pmod{2\pi}\) and let \(\mathcal P\) be its Perron–Frobenius operator on Haar \(L^2\):
\[
\mathcal P g(t)=\frac13\sum_{j=0}^2 g\left(\frac{t-\pi+2\pi j}{3}\right).
\]
Since the Fourier series has only even frequencies and the transfer operator deletes frequencies not divisible by three, \(\mathcal P\phi=\phi/3\) in \(L^2\). Put \(\psi=\phi-\phi\circ T/3\); then \(\mathcal P\psi=0\), and \(\psi\in L^2\) has \(\int\psi^2=\frac89\int\phi^2=2\pi^2/27\). The sequence \(\psi\circ T^j\) is a stationary, ergodic **reverse martingale difference** sequence for the decreasing filtration \(T^{-j}\mathcal B\). Its conditional quadratic variation obeys the ergodic theorem and its Lindeberg condition follows by truncation in \(L^2\); the reverse martingale central limit theorem therefore gives
\[
\frac1{\sqrt n}\sum_{j<n}\psi\circ T^j\Longrightarrow\mathcal N(0,2\pi^2/27).
\]
The exact telescoping relation
\[
S_n=\frac32\sum_{j<n}\psi\circ T^j+\frac12(\phi\circ T^n-\phi)
\]
has a remainder bounded in \(L^2\) independently of \(n\). Slutsky's theorem gives the displayed Gaussian limit with variance \((3/2)^2(2\pi^2/27)=\pi^2/6\).

## Verification
Run `python3 verify.py` with Python 3 and SymPy. The included standalone checker verifies the conjugacy and normal-multiplier identities symbolically, 120 finite-horizon variance identities in exact rational arithmetic, six transfer-operator values and five independent stationary quadratures. The output ends with `ALL CHECKS PASS`. These finite tests support the algebra but are not the justification of the all-parameter formulas or the distributional limit, which follow from the proof above.

## Relationship to prior work
Hong and Zhang (2023) formulate the exact predator–prey map and study equilibria, flip and Neimark–Sacker bifurcations, and numerical chaos near positive equilibria. Their full article does not provide this cubic invariant-axis conjugacy, normal mortality plateau, exact covariance or Gaussian fluctuation result. The classical Chebyshev conjugacy, logarithmic Fourier expansions, Birkhoff theorem, Jensen's integral and reverse martingale limit theorem are established tools; none is asserted new. Anteneodo (2003) gives a general Fourier method and an exact covariance for the logistic-map *derivative*, with a distinct bounded-variance phenomenon and map of degree two. A publicly indexed calculation for a different coupled-logistic population map gives a parameterized normal log-covariance for the doubling map and its two natural multiplier zeros; that calculation does not state this tripling-map normal cocycle, its explicit \(3^{-k}\) spectrum or its Gaussian limit. The contribution here is the exact algebraic locus inside the cited predator–prey recurrence and the linked stationary normal fluctuation law, not an abstract claim that expanding maps have central limit theorems.

## Limitations
The parameter locus has fixed prey shape and step-size ratio and is not generic. The invariant real interval crosses outside the physically positive prey region, so biological persistence or invasion is not established. At other mortality values the variance and limit law are not classified here, although the Lyapunov exponent is. The zero exponent and central limit law hold for the normal *linearization* and stationary prey sampling, not the nonlinear planar predator process. The result does not prove a quenched limit law at a fixed seed or uniform estimates over all initial angles. Equivalent applications of classical Fourier/transfer-operator tools not captured by indexed or inspected literature remain a publication-priority risk.

## References
1. B. Hong and C. Zhang, *Bifurcations and chaotic behavior of a predator-prey model with discrete time*, AIMS Mathematics 8 (2023), 13390–13410, first published April 6, 2023, DOI: https://doi.org/10.3934/math.2023678 ; complete open-access PDF: https://www.aimspress.com/aimspress-data/math/2023/6/PDF/math-08-06-678.pdf .
2. C. Anteneodo, *Statistics of finite-time Lyapunov exponents in the Ulam map*, arXiv:nlin/0309065, September 24, 2003, https://arxiv.org/abs/nlin/0309065 ; especially its Fourier-correlation discussion.
3. *Exact transverse-log covariance spectrum on the chaotic axis of a coupled logistic population map*, publicly indexed mathematical note, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-transverse-log-covariance-spectrum-on-the-chaotic-axis-of--634dc48171fb .
