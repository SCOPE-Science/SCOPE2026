# Sharp global return-speed threshold for acceleration by Brownian resetting

## Finding
For Brownian motion with absorbing endpoints and nonabsorbing, finite-duration returns to the starting point, **some** positive Poisson reset rate can strictly reduce the mean total completion time for **some** interior starting point if and only if the dimensionless mean return drift \(A=aL/D\) exceeds \(2\). At \(A\le 2\), every interior starting point and every strictly positive reset rate strictly increase the mean. At \(A>2\), the rate of beneficial resetting need not be infinitesimal: a positive initial derivative of the mean can coexist with a later strict improvement.

A concrete example is \(L=D=1\), \(a=3\), \(x=1/100\), \(r=100\), where the bare mean \(99/20000=0.00495\) decreases to \(0.004392697465482512\ldots\), despite the strictly positive derivative at \(r=0\), equal to \(117623/800000000\).

## Assumptions and scope
Fix arbitrary \(L,D,a,D_R>0\), \(x\in(0,L)\), \(r\ge0\). During exploration \(X\) has generator \(D\partial_{xx}\), starts at \(x\), and is killed on first reaching either endpoint. An independent exponential alarm of rate \(r\), if it occurs before killing, switches the motion into a return phase on the real line; during returns both endpoint targets are **inactive**. The return dynamics from the alarm position \(y\) is \(dY_t=-a\operatorname{sgn}(Y_t-x)\,dt+\sqrt{2D_R}\,dW_t\) until the first hit of \(x\); exploration then restarts afresh at \(x\), with a new exponential clock. The complete time \(T(r,a,x)\) includes all exploration and return durations. The return hitting time has conditional mean \(|y-x|/a\), independently of \(D_R\). The same theorem holds for any independent regenerative return protocol with that conditional mean and no detection during return. The comparison baseline is \(T(0,a,x)\), whose mean is \(f(x)=x(L-x)/(2D)\).

## Proof
**1. Exact one-cycle comparison.** Let \(\tau\) be the no-reset exploration exit time; let \(R\) be independent \(\operatorname{Exp}(r)\). Write \(p=\Pr_x(\tau<R)>0\), and \(H(y)=|y-x|/a\). Renewal gives
\[
\mathbb E T=\mathbb E(\tau\wedge R)+\mathbb E[\mathbf1_{R<\tau}(H(X_R)+\mathbb ET)].
\]
The ordinary Brownian exit-time potential satisfies \(Df''=-1\), \(f(0)=f(L)=0\). Dynkin's formula, stopped at \(R\wedge\tau\), yields
\[
f(x)=\mathbb E(\tau\wedge R)+\mathbb E[\mathbf1_{R<\tau}f(X_R)].
\]
Subtracting yields the exact identity
\[
\boxed{p\big(\mathbb ET-f(x)\big)=\mathbb E\!\left[\mathbf1_{R<\tau}\left(\frac{|X_R-x|}{a}+f(x)-f(X_R)\right)\right].}
\]
Because \(|f'(y)|\le L/(2D)\), if \(a\le2D/L\), each integrand is nonnegative. Strict positivity for every \(r>0\) and interior \(x\) follows from the strict inequality \(f(y)-f(x)<(L/(2D))|y-x|\) whenever \(x,y\in(0,L)\) and \(y\ne x\), together with the positive density of alarm positions away from \(x\). Thus no rate can improve the mean at or below \(A=2\). The formula also proves finiteness by the positive escape probability \(p\) and bounded alarm positions.

**2. Exact finite-rate expression.** Introduce \(u=x/L\in(0,1)\), \(\kappa=L\sqrt{r/D}>0\), and \(A=aL/D\). Let \(S=\sinh(\kappa u)+\sinh(\kappa(1-u))\). The killed Brownian resolvent is
\[
G_r(x,y)=\frac{\sinh(\sqrt{r/D}\min(x,y))\sinh(\sqrt{r/D}(L-\max(x,y)))}{D\sqrt{r/D}\sinh(L\sqrt{r/D})}.
\]
From \(p=S/\sinh\kappa\), \(\mathbb E(\tau\wedge R)=(1-p)/r\), and \(\mathbb E[|X_R-x|\mathbf1_{R<\tau}]=r\int_0^L G_r(x,y)|y-x|\,dy\), the independent-cycle geometric sum gives
\[
\frac{D}{L^2}\mathbb ET=E(u,\kappa)+\frac{\Delta(u,\kappa)}{A},
\quad E=\frac{\sinh\kappa-S}{\kappa^2 S},
\]
\[
\Delta=\frac{2\sinh(\kappa u)\sinh(\kappa(1-u))-\kappa[u\sinh(\kappa(1-u))+(1-u)\sinh(\kappa u)]}{\kappa S}.
\]
This integral evaluation follows by splitting the resolvent integral at \(y=x\) and integrating products of \(\sinh\) against the linear distance. All denominators are positive, and \(\Delta\) is a sum-of-distances expectation, hence strictly positive.

**3. Sharp attainability above the threshold.** For every fixed \(\kappa>0\), Taylor expansion as \(u\downarrow0\) gives
\[
\lim_{u\downarrow0}\frac{E(u,\kappa)}{u}=\frac{\tanh(\kappa/2)}{\kappa},\qquad
\lim_{u\downarrow0}\frac{\Delta(u,\kappa)}{u}=1-\frac{\kappa}{\sinh\kappa}.
\]
Since \((D/L^2)f(x)=u(1-u)/2\), the limiting normalized mean difference, divided by \(u\), is
\[
\Phi_A(\kappa)=\frac{\tanh(\kappa/2)}{\kappa}+\frac{1-\kappa/\sinh\kappa}{A}-\frac12.
\]
Taking \(\kappa\to\infty\) yields \(\Phi_A(\kappa)\to 1/A-1/2<0\) whenever \(A>2\). Choose a **finite** \(\kappa\) sufficiently large, then a strictly positive \(u\) sufficiently small, to obtain \(\mathbb ET<f(x)\). This proves the global sharp threshold and both directions of the if-and-only-if statement.

**4. Weak-resetting reversal.** In units \(L=D=1\), differentiation at \(r=0\), justified by the finite killed-Brownian moments, gives
\[
\left.\frac{d}{dr}\mathbb ET(r,A,u)\right|_{r=0}
=\int_0^1G_0(u,y)\left(\frac{|y-u|}{A}+f(u)-f(y)\right)dy
=\frac{u(u-1)[A(5u^2-5u+1)-8u^2+8u-4]}{24A}.
\]
At \(A=3\), \(u=1/100\), the last quantity equals \(117623/800000000>0\). But substituting \(\kappa=10\) into the exact finite-rate formula gives \(\mathbb ET=0.004392697465482512\ldots<0.00495\). An independent exact rational Taylor interval calculation certifies the strict comparison. Hence testing only the small-rate derivative cannot decide whether resetting ever helps.

## Verification
The included `checker.py` uses only Python's standard library. It constructs rigorous rational upper/lower bounds on the three required hyperbolic sines using Taylor polynomials and geometric tail bounds, verifies the strict finite-rate improvement, and verifies the exact positive rational weak-reset coefficient. It additionally compares the closed distance-integral formula against numerical quadrature of the independently stated killed Green kernel at several parameter pairs, a diagnostic rather than an infinite proof. Run `python3 checker.py`.

## Relationship to prior work
Sunil, Blythe, Evans and Majumdar (arXiv:2503.03697v1, first public 5 March 2025) introduced a linear reset-distance cost for discrete-time continuous-space walks on a half-line and computed cost laws. Dubey and Pal (arXiv:2610.18814v1, first public 13 October 2026) studied stochastic-return first passage in harmonic switching traps with target detection during returns, a different absorption and geometry mechanism. Chen, Tang and Li (arXiv:2611.23790v1, publicly released 18 November 2026, used here as a later comparison source) derived the exact mean time for precisely the two-absorbing-boundary linear-return model and a **weak-reset** threshold \(A=4\). Their criterion is explicitly infinitesimal-rate; their full-text sections III and VII do not give the sharp all-rate global threshold \(A=2\), the above global obstruction argument, or the finite-rate counterexample when the weak derivative is positive. The present statement is a new global optimization classification within that already-solved mean-time model, not a claim of a new generator, renewal identity, or mean-time transform. Previous general demonstrations of finite-rate benefit despite weak-rate detriment on star graphs concern different geometry and no finite return cost.

## Limitations
The gain criterion is existential in initial position and positive rate, not an optimal-rate formula at each fixed position. It requires two absorbing endpoints, return inactivation of both targets, regenerative restart at the same original interior position, and mean return duration exactly equal to distance divided by drift strength. The full return-time distribution need not be inverse Gaussian for the **mean** theorem. This does not prove that every \(A>2\) improves every starting position, or extend the threshold to target-active returns, arbitrary potentials, non-Poisson alarms, or higher-dimensional domains. Independent scientific validation and complete exhaustive priority certification have not been performed.

## References
- J. C. Sunil, R. A. Blythe, M. R. Evans and S. N. Majumdar, *The cost of resetting discrete-time random walks*, arXiv:2503.03697v1 (5 March 2025), https://arxiv.org/html/2503.03697v1.
- A. Dubey and A. Pal, *Towards synergy between theory and experiments: First-passage processes under resetting with stochastic return protocols*, arXiv:2610.18814v1 (13 October 2026), https://arxiv.org/abs/2610.18814.
- H. Chen, C. Tang and G. Li, *Finite-time stochastic resetting in bounded domains: competing targets, energetic cost, and optimal search strategies*, arXiv:2611.23790v1 (18 November 2026; later comparison source), https://arxiv.org/html/2611.23790v1.
