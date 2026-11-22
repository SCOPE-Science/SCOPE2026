# A sharp age–position reversal and conditional-age minimum under threshold resetting

## Finding
Consider one-dimensional drift–diffusion on the positive half-line with instantaneous renewal at its absorbing threshold. At an equilibrium inspection time, let \(X\) be position, \(A\) time since the preceding threshold reset and \(R\) time remaining until the next reset. For any initial/reset distance \(L>0\), drift \(v>0\) toward zero and diffusion coefficient \(D>0\), the following holds.

**Conditional-age geometry.** Put \(m=\min\{x,L\}\). For every \(x>0\),
\[
\mathbb E[A\mid X=x]=\frac{2D}{v^2}+\frac{|x-L|}{v}-\frac{2m}{v(e^{vm/D}-1)}.
\]
This conditional mean decreases strictly on \((0,L)\), reaches its **unique global minimum at the reinjection point** \(x=L\), and then increases linearly with slope \(1/v\) on \((L,\infty)\). Its limit as \(x\downarrow0\) is \(L/v\).

**Sharp global sign transition and time-direction asymmetry.** In the stationary regime,
\[
\operatorname{Cov}(X,A)=\frac{D^2}{v^3}-\frac{L^2}{12v},\qquad
\operatorname{Cov}(X,R)=\frac{D^2}{v^3}+\frac{L^2}{12v}.
\]
Writing \(\mathrm{Pe}=vL/(2D)\), the first covariance is positive for \(0<\mathrm{Pe}<\sqrt3\), zero exactly at \(\sqrt3\), and negative for \(\mathrm{Pe}>\sqrt3\). The second covariance is strictly positive for all parameters. Consequently,
\[
\operatorname{Cov}(X,R)-\operatorname{Cov}(X,A)=\frac{L^2}{6v}>0,
\]
independently of diffusivity, even though \(A\) and \(R\) have identical stationary marginal distributions. This constitutes a position-marked temporal asymmetry, not an entropy-production identity.

## Assumptions and scope
For each excursion start at \(X_0=L\) and solve \(dX_t=-v\,dt+\sqrt{2D}\,dW_t\) until \(\tau=\inf\{t>0:X_t=0\}\). At \(\tau\), put the particle instantly back at \(L\), restart with independent Brownian increments, and repeat. The assumptions are \(L,v,D>0\), no refractory time, no boundary overshoot and no other resetting mechanism. The first-passage time has finite mean \(\mathbb E\tau=L/v\), so the regenerative process has a unique stationary probability law. A stationary inspection is understood as the weak long-time limit (equivalently the length-biased stationary-cycle construction). All conditioned quantities refer to a version of regular conditional expectation at \(x>0\), where the stationary position density is positive. The boundary point \(x=0\) itself has zero stationary mass.

## Proof
The killed generator is \(\mathcal L=D\partial_x^2-v\partial_x\) with absorbing Dirichlet condition at zero. Its time-Laplace Green density for the initial point \(L\) is, for \(x>0\) and \(s\ge0\),
\[
G_s(x\mid L)=\frac{e^{v(L-x)/(2D)}}{q_s}\,e^{-q_s|x-L|/(2D)}\bigl(1-e^{-q_sm/D}\bigr),\quad
q_s=\sqrt{v^2+4Ds},\quad m=\min\{x,L\}.
\]
For an equilibrium random inspection, the joint stationary age–position law is \(\mathbb P(A\in dt,X\in dx)=G(x,t\mid L)\,dt\,dx/\mathbb E\tau\), where \(G(x,t\mid L)\) is the killed transition density, with time transform \(G_s\). Thus
\[
\mathbb E[A\mid X=x]=-\left.\frac{\partial}{\partial s}\log G_s(x\mid L)\right|_{s=0}.
\]
Differentiating \(q_s\) gives the stated conditional-age formula. All integrals and differentiations are justified by the exponentially decaying first-passage tail when \(v>0\).

To show its shape, for \(0<x<L\) set \(z=vx/D\) and \(g(z)=z/(e^z-1)\). Direct differentiation yields
\[
\frac{d}{dx}\mathbb E[A\mid X=x]=-\frac{1+2g'(z)}{v},\quad
1+2g'(z)=\frac{e^{2z}-1-2ze^z}{(e^z-1)^2}
=\frac{2e^z(\sinh z-z)}{(e^z-1)^2}>0.
\]
Thus the derivative is strictly negative for \(0<x<L\). When \(x>L\), the minimum \(m=L\) is constant and the derivative is \(1/v\). Continuity at \(L\), positivity of the density, and the limit at zero complete the unique-minimum conclusion.

For the moment calculation define \(U_f(y)=\mathbb E_y\int_0^\tau f(X_t)\,dt\), and \(V_f(y)=\mathbb E_y\int_0^\tau t f(X_t)\,dt\). Dynkin's formula and the Markov property give \(-\mathcal LU_f=f\), \(-\mathcal LV_f=U_f\), with zero value at \(y=0\). Selecting the solutions with admissible polynomial growth gives
\[
\begin{aligned}
U_1(y)&=y/v,\\
U_x(y)&=y^2/(2v)+Dy/v^2,\\
U_{x^2}(y)&=y^3/(3v)+Dy^2/v^2+2D^2y/v^3,\\
V_1(y)&=y^2/(2v^2)+Dy/v^3,\\
V_x(y)&=y^3/(6v^2)+Dy^2/v^3+2D^2y/v^4.
\end{aligned}
\]
These identities can be verified directly by substitution into their boundary-value equations. The regenerative occupation formula divides each of these values at \(y=L\) by \(U_1(L)=L/v\). It follows that
\[
\begin{aligned}
\mathbb E X&=L/2+D/v, &\operatorname{Var}(X)&=L^2/12+D^2/v^2,\\
\mathbb E A&=L/(2v)+D/v^2, &\mathbb E[AX]&=L^2/(6v)+DL/v^2+2D^2/v^3.
\end{aligned}
\]
Subtracting the product of the means proves the stated \(\operatorname{Cov}(X,A)\) and its sign transition. Finally, the strong Markov property gives \(\mathbb E[R\mid X=x]=x/v\) for every \(x>0\). Therefore \(\operatorname{Cov}(X,R)=\operatorname{Var}(X)/v\), proving the second formula and the time-direction gap. Equality of the stationary marginal laws of age and residual time follows separately from stationarity of the regenerative renewal process: both have survivor \(\mathbb P(A>t)=\mathbb P(R>t)=\mathbb E[(\tau-t)_+]/\mathbb E\tau\).

## Verification
The supplementary checker `checks/age_position_check.py` substitutes the five polynomial potentials into the killed-generator equations, checks the covariance identities symbolically, and compares the exact occupation integrals against direct time integration of the absorbing Brownian reflection kernel for four positive parameter triples. It also integrates the killed transition density at five observation positions to check the conditional-age formula numerically. Dependencies are stated in `checks/requirements.txt` and reproduction consists of installing those packages and executing `python checks/age_position_check.py`. The analytic proof, not the finite collection of numerical tests, establishes the assertions for all positive parameters.

## Relationship to prior work
Das, Majumdar and Pal [1] introduced a threshold-reset drift–diffusion analysis, deriving the renewal propagator, Green resolvent, stationary density and low spatial moments. Their exact Green resolvent is an important premise also used here; the new claim is the **conditional renewal-age geometry and the strict sign/forward–backward classification**, not a new propagator or stationary density. De Bruyne, Randon-Furling and Redner [2] treat first-passage resetting and optimization, while Falcao and Evans [3] analyze the corresponding interacting Brownian mechanism and its stationary relaxation. Pal, Kostinski and Reuveni [4] explain the marginal renewal age/residual inspection bias. The equal-marginal observation in the present result is classical; the marked conditional mean and its sharp \(\mathrm{Pe}=\sqrt3\) covariance reversal are the proposed contribution.

## Limitations
The statement concerns the minimal constant-drift half-line model with instantaneous complete renewal. It does not establish an ordering for whole conditional age distributions, does not extend automatically to nonlinear drift, finite boundaries, partially transmitting thresholds or finite-time data, and does not calculate thermodynamic entropy production. The derived covariance threshold is exact but does not by itself imply a universal phase transition beyond this model. Publication priority is qualified by possible unindexed equivalent calculations; none were identified in the inspected sources.

## References
[1] R. Das, S. N. Majumdar, A. Pal, *Non-equilibrium dynamics of drift–diffusion process under threshold resetting*, arXiv:2609.24438, first posted 2026-09-21. https://arxiv.org/abs/2609.24438

[2] B. De Bruyne, J. Randon-Furling, S. Redner, *Optimization and Growth in First-Passage Resetting*, arXiv:2009.03419, 2020. https://arxiv.org/html/2009.03419v2

[3] R. Falcao, M. R. Evans, *Interacting Brownian Motion with Resetting*, arXiv:1610.03503, 2016. https://arxiv.org/html/1610.03503v1

[4] A. Pal, S. Kostinski, S. Reuveni, *The inspection paradox in stochastic resetting*, arXiv:2108.07018, 2021. https://arxiv.org/abs/2108.07018
