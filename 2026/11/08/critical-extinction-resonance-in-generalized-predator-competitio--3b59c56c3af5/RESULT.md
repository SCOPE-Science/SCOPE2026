# Critical extinction resonance in generalized predator competition

## Finding
Consider the additional-food predator–prey flow
\[
\begin{aligned}
\dot x&=x\left(1-\frac{x}{K}\right)-\frac{xy}{B+x},\\
\dot y&=y\left[\eta\frac{x+\xi}{B+x}-\delta-c\xi y^{p-1}\right],
\qquad B=1+\alpha\xi.
\end{aligned}
\]
At the **critical predator-invasion equality**
\[
\delta=\eta\frac{K+\xi}{B+K},
\]
assume \(K,\alpha,\xi,\eta,c>0\), \(B>\xi\), and \(1<p\leq2\). Every solution with \(x(0),y(0)>0\) exists globally, stays positive and satisfies \(x(t)\to K\), \(y(t)\to0\). Define
\[
\beta=c\xi,\quad A=\frac{K}{B+K},\quad
\Lambda=\frac{\eta K(B-\xi)}{(B+K)^3}>0,
\quad r=p-1.
\]
For all these exponents the prey displacement is synchronized with predator abundance:
\[
\lim_{t\to\infty}\frac{K-x(t)}{y(t)}=A.
\]
For **fractional competition**, \(1<p<2\), the universal leading law is
\[
\lim_{t\to\infty}t\,y(t)^{p-1}=\frac1{(p-1)\beta}.
\]
More precisely, let \(u(t)=y(t)^{-r}\) and \(a=r\beta\). Then the *first correction* has a sharp trichotomy:
\[
\begin{array}{lll}
1<p<\tfrac32:
 &u(t)-at\longrightarrow C(x(0),y(0))\in\mathbb R;\\[3pt]
p=\tfrac32:
 &\displaystyle\lim_{t\to\infty}\frac{u(t)-at}{\log t}=\frac{\Lambda}{\beta};\\[9pt]
\tfrac32<p<2:
 &\displaystyle\lim_{t\to\infty}\frac{u(t)-at}{t^{(2r-1)/r}}
 =\frac{r\Lambda\,a^{-(1-r)/r}}{(2r-1)/r}.
\end{array}
\]
The finite constant in the first case depends on the initial state; the logarithmic and fractional-power correction coefficients are universal. At the **quadratic endpoint**, \(p=2\), prey feedback contributes already to leading order:
\[
\lim_{t\to\infty}t\,y(t)=\frac1{\beta+\Lambda}.
\]
These assertions together constitute the critical extinction and correction-law theorem.

## Assumptions and scope
The model uses the normalizations in the July 2026 source, not a time-rescaled equation. All parameters, including additional food \(\xi\), conversion efficiency \(\eta\), competition intensity \(c\), and carrying capacity \(K\), are strictly positive. The restriction \(B>\xi\), equivalent to \(1+(\alpha-1)\xi>0\), makes \(R(x)=(x+\xi)/(B+x)\) **strictly increasing**; it is needed for the global critical comparison and for \(\Lambda>0\). The critical equality is imposed exactly, rather than inferred from numerical proximity. Initial data are any strictly positive finite pair. The second-correction laws are pointwise in fixed parameters and fixed \(p\); no uniformity as \(p\to2\) is claimed.

## Proof
### Positivity, boundedness and global convergence
Write \(R(x)=(x+\xi)/(B+x)\); since \(B>\xi\),
\[
R'(x)=\frac{B-\xi}{(B+x)^2}>0.
\]
The vector field is locally Lipschitz on the closed positive quadrant, and both equations have a factor of the corresponding population, so strictly positive finite initial data remain strictly positive for every finite time of existence. The prey satisfies \(\dot x\leq x(1-x/K)\), hence is bounded by \(\max\{x(0),K\}\); the predator per-capita growth is bounded above by a finite constant minus \(\beta y^{p-1}\), hence \(y\) is bounded. Therefore solutions are global.

Scalar logistic comparison also gives \(\limsup_{t\to\infty}x(t)\leq K\). Fix \(\epsilon>0\). Eventually \(x(t)\leq K+\epsilon\), so monotonicity of \(R\) and the critical equality give
\[
\dot y\leq y\bigl[\eta(R(K+\epsilon)-R(K))-\beta y^{p-1}\bigr].
\]
The comparison scalar equation implies
\[
\limsup_{t\to\infty}y(t)
\leq\left(\frac{\eta[R(K+\epsilon)-R(K)]}{\beta}\right)^{1/(p-1)}.
\]
Letting \(\epsilon\downarrow0\) proves \(y(t)\to0\). Since \(B+x\geq B\), for any sufficiently small \(\epsilon>0\), eventually
\[
x\left(1-\frac{\epsilon}{B}-\frac{x}{K}\right)
\leq\dot x\leq x\left(1-\frac{x}{K}\right).
\]
Comparison with two logistic equations and then \(\epsilon\downarrow0\) proves \(x(t)\to K\).

### Exact stable-filter relation
Put \(z=K-x\), allowing either sign for \(z\) at finite times. Its exact equation is
\[
\dot z=\left(-1+\frac zK\right)z+\frac{x}{B+x}y.
\]
Since \(y>0\), the ratio \(w=z/y\) solves the *exact linear equation*
\[
\dot w=\left(-1+\frac zK-\frac{\dot y}{y}\right)w+\frac{x}{B+x}.
\]
The already proved limits imply \(z\to0\), \(x\to K\), and
\[
\frac{\dot y}y=\eta[R(x)-R(K)]-\beta y^{p-1}\longrightarrow0.
\]
Thus the linear coefficient tends to \(-1\) and the forcing tends to \(K/(B+K)=A\). Variation of constants, splitting the integral at an arbitrary large fixed time, proves \(w(t)\to A\), independent of its initial sign. In particular, \(z=Ay+o(y)\), and \(x<K\) eventually.

### Leading decay and the fractional correction
Taylor expansion of the smooth rational function \(R\) at \(K\), combined with \(z=Ay+o(y)\), yields
\[
\eta[R(x)-R(K)]=-\eta R'(K)Ay+o(y)=-\Lambda y+o(y).
\]
Consequently
\[
\dot y=-\beta y^{p}-\Lambda y^2+o(y^2).
\]
For \(0<r=p-1<1\), set \(u=y^{-r}\). Exactly differentiating and applying the preceding asymptotic gives
\[
\dot u=r\beta+r\Lambda y^{1-r}+o(y^{1-r}).
\]
Because \(y\to0\), this first implies \(\dot u\to a=r\beta\), hence \(u(t)\sim at\) by integration. Thus
\[
\dot u-a
=r\Lambda(at)^{-h}(1+o(1)),
\qquad h=\frac{1-r}{r}>0.
\]
For \(h>1\), equivalent to \(p<3/2\), the correction is absolutely integrable and \(u-at\) has a finite real limit. At \(h=1\), equivalent to \(p=3/2\), direct integration gives \((u-at)/\log t\to r\Lambda/a=\Lambda/\beta\). For \(0<h<1\), integration gives
\[
\lim_{t\to\infty}\frac{u-at}{t^{1-h}}=
\frac{r\Lambda a^{-h}}{1-h},
\]
which is the displayed power law. The same leading derivative proves \(t y^r\to1/a\). Each asymptotic integration uses an actual limit of the integrand; no finite numerical simulation is substituted for that limit.

### Quadratic endpoint
When \(p=2\), the quadratic terms are of the same order, and the expansion instead reads
\[
\dot y=-(\beta+\Lambda)y^2+o(y^2).
\]
Integrating \((1/y)'=\beta+\Lambda+o(1)\) gives \(t y(t)\to1/(\beta+\Lambda)\), completing the theorem.

## Verification
The standalone script `verification/check.py` uses exact rational arithmetic for the defining constants and checks the three fractional-correction regimes and the quadratic endpoint with numerical ODE integration, including two different initial conditions. The auxiliary transform \(u=y^{-(p-1)}\) avoids catastrophic cancellation caused by very small predator populations. The numerical checks confirm the predicted corrections at finite large times, not the universal limit theorem. All global limits, existence statements and correction exponents are established by the proof above.

## Relationship to prior work
Goyal, Kottegoda, Verma and Parshad (first publicly posted July 21, 2026) introduce precisely this model in their equation (1.2), establish positive invariance and boundedness (Theorems 2.1–2.2), and analyze boundary-equilibrium *local* stability (Lemma 3.2), interior equilibria and high-codimension bifurcations. Their strict inequalities \(\delta\gtrless\eta(K+\xi)/(B+K)\) do not determine global behavior at equality, and their sections on bifurcations do not provide extinction exponents or the \(p=3/2\) correction threshold. The earlier work by Parshad and collaborators (2022 preprint/2023 publication) treats quadratic competition \(p=2\), not the continuum of fractional exponents \(1<p<2\). Verma and collaborators' 2025 two-patch model proves extinction results for different states and investigates a special single-patch bifurcation regime; its results do not imply the stated critical two-species asymptotics. Standard asymptotic ODE methods underlie the present proof; their existence alone is not a claim of priority. Historical completeness is not guaranteed.

## Limitations
The strict monotonicity condition \(B>\xi\), exact critical mortality equality, positive initial populations, and deterministic autonomous dynamics are essential to the stated scope. The theorem does not assert global behavior for \(B\leq\xi\), periodic or stochastic forcing, or perturbations away from the critical surface. The constant \(C\) when \(p<3/2\) is not given in closed form. The crossover from fractional to quadratic competition is nonuniform as \(p\to2\). General abstract asymptotic results or unlocated prior papers could affect historical priority, and independent validation has not been performed.

## References
1. K. Goyal, C. Kottegoda, U. Verma and R. D. Parshad, *Additional Food Enhances the Bifurcation Structure of Predator Competition Models*, arXiv:2607.18613, first posted July 21, 2026. https://arxiv.org/abs/2607.18613
2. R. D. Parshad, S. Wickramsooriya, K. Antwi-Fordjour and A. Banerjee, *Additional food causes predator “explosion” — unless the predators compete*, arXiv:2208.00153, first posted July 30, 2022. https://arxiv.org/abs/2208.00153
3. U. Verma, K. Goyal, C. Kottegoda and R. D. Parshad, *An additional food driven biological control patch model, incorporating generalized competition*, arXiv:2510.06111, first posted October 7, 2025. https://arxiv.org/abs/2510.06111
