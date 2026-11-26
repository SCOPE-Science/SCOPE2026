# Universal extinction-rate transition at a doubly critical two-patch Allee threshold

## Finding
Consider the density-dependent two-patch population system defined below. At the exact migration–mortality balance \(e=B\), its Allee threshold \(m_c=1/H\) separates two **different universal algebraic extinction laws**. For every strictly positive initial condition and every \(m\ge m_c\), the first-patch population tends to zero and the second-patch population tends to its logistic boundary value. If \(m>m_c\),
\[
\lim_{t\to\infty}t u(t)=\frac{1}{H-1/m},
\qquad
\lim_{t\to\infty}\frac{v(t)-v_0-a u(t)}{u(t)^2}=\frac{a(H-1/m)}{s}.
\]
At the doubly critical value \(m=m_c\),
\[
\boxed{\lim_{t\to\infty}t u(t)^2=\frac{1}{2H^2}},
\qquad
\boxed{\lim_{t\to\infty}\frac{v(t)-v_0-a u(t)}{u(t)^3}=\frac{aH^2}{s}}.
\]
Thus a *quadratic* center drift gives \(t^{-1}\) extinction, whereas cancellation of that drift gives \(t^{-1/2}\) extinction, with a universal leading amplitude and a higher-order patch-response lag. The limits are independent of positive initial densities.

## Assumptions and scope
For \(t\ge0\), let \(u(t),v(t)\) solve
\[
\begin{aligned}
\dot u&=u\left(\frac{u}{m+u}-e-hu+\delta(v-u)\right),\\
\dot v&=v\left(s(1-v)+\delta(u-v)\right),
\end{aligned}
\]
with \(u(0)>0\), \(v(0)>0\), and parameters \(s,\delta,h,m>0\), \(0<e<1\). Define
\[
 B=\frac{s\delta}{s+\delta},\quad H=h+B,\quad
 v_0=\frac{s}{s+\delta},\quad a=\frac{\delta}{s+\delta}.
\]
Assume \(e=B\) and \(m\ge1/H\). In particular these conditions require \(B<1\). Time and parameters are in the original normalized units of the cited ODE. Conclusions concern only strictly positive finite initial densities. The source's model, its coexistence thresholds and local boundary classification are prior work.

## Proof
**Positive global solutions and boundedness.** Each coordinate has its own nonnegative multiplicative factor, so positive coordinates stay positive while a finite solution exists. For \(M=u+v\), the two density-dependent dispersal terms sum to \(-\delta(u-v)^2\). Since \(u/(m+u)\le1\),
\[
 \dot M\le (1-e)u+sv-hu^2-sv^2
 \le C M-c M^2,
\]
where \(C=\max\{1-e,s\}\) and \(c=\min\{h,s\}/2>0\). Consequently solutions exist globally, are bounded, and have bounded first and second derivatives.

**Extinction at and above the double threshold.** Define \(U=\limsup_{t\to\infty}u(t)\) and \(V=\limsup_{t\to\infty}v(t)\). The comparison \(\dot v\ge v[s-(s+\delta)v]\) yields \(\liminf v\ge v_0>0\). By the elementary bounded-trajectory fluctuation lemma, times approaching the limsup of a bounded differentiable component may be chosen so that its derivative tends to zero. Applying this to \(v\), whose limit-point values are positive, gives
\[
 V\le\frac{s+\delta U}{s+\delta}=v_0+aU.
\]
If \(U>0\), applying the same lemma to \(u\), and substituting the upper bound for \(V\) into its per-capita derivative, gives
\[
 0\le\frac{U}{m+U}-e-hU+\delta(v_0+aU-U)
 =U\left(\frac1{m+U}-H\right)<0.
\]
The last inequality follows from \(m\ge1/H\) and \(U>0\), a contradiction. Hence \(u(t)\to0\). Applying the fluctuation inequalities for liminf and limsup to the second equation now shows \(v(t)\to v_0\). The global conclusion does not rely on a local stability result or numerical phase portrait.

**Fast-tracking coordinate and exact identities.** Put
\[
 w(t)=v(t)-v_0-a u(t),\qquad G_m(u)=\frac{u}{m+u}-Hu.
\]
Because \((s+\delta)(v_0+a u)=s+\delta u\), straightforward differentiation gives the *exact* equations
\[
 \dot u=u[G_m(u)+\delta w],\qquad
 \dot w=-(s+\delta)v w-a\dot u.
\]
From the established limits, \(\dot u/u=G_m(u)+\delta w\to0\). Thus \(u\) is asymptotically subexponential and is slowly varying on every fixed time window.

**Stable-filter lemma.** If \(p>0\) is fixed and \(\dot u/u^p\to L\in\mathbb R\), then
\[
 \frac{w(t)}{u(t)^p}\longrightarrow-\frac{aL}{s}.
\]
Indeed, solve the linear \(w\) equation by variation of constants:
\[
 w(t)=e^{-\int_T^t(s+\delta)v(z)\,dz}w(T)
 -a\int_T^t e^{-\int_r^t(s+\delta)v(z)\,dz}\dot u(r)\,dr.
\]
After dividing by \(u(t)^p\) and writing \(\tau=t-r\), the pointwise integrand tends to \(e^{-s\tau}L\): the derivative ratio tends to \(L\), and \(u(t-\tau)/u(t)\to1\). Since \(\dot u/u\to0\), for any small \(\eta>0\) the ratio \(u(t-\tau)^p/u(t)^p\) is at most \(e^{p\eta\tau}\) on the eventual tail, while the exponential filter is bounded by \(e^{-(s-\eta)\tau}\). Choose \(\eta\) so that \(s>(p+1)\eta\), and apply dominated convergence. The initial contribution and finite early-time segment vanish exponentially even after normalization by \(u(t)^p\), completing the lemma.

**Ordinary critical branch.** If \(m>1/H\), put \(c_m=H-1/m>0\). The stable-filter lemma with \(p=1\), \(L=\lim\dot u/u=0\), yields \(w/u\to0\). Since \(G_m(u)/u\to-c_m\),
\[
 \dot u/u^2=G_m(u)/u+\delta w/u\to-c_m.
\]
Integration of \(d(u^{-1})/dt=-\dot u/u^2\to c_m\) yields \(tu(t)\to1/c_m\). Applying the filter lemma again with \(p=2\), \(L=-c_m\), yields \(w/u^2\to a c_m/s\).

**Double cancellation and cubic slowing.** At \(m=1/H\), the exact per-capita drift reduces to
\[
 G_{1/H}(u)=-\frac{H^2u^2}{1+Hu}.
\]
First \(w/u\to0\) by the filter lemma with \(p=1\). Thus
\[
 \dot u/u^2=-H^2u/(1+Hu)+\delta w/u\to0.
\]
The lemma with \(p=2\) now gives \(w/u^2\to0\). Hence
\[
 \dot u/u^3=-\frac{H^2}{1+Hu}+\delta w/u^2\to-H^2.
\]
Integrating \(d(u^{-2})/dt=-2\dot u/u^3\to2H^2\) yields \(t u(t)^2\to1/(2H^2)\). A final use of the lemma with \(p=3\), \(L=-H^2\), yields \(w/u^3\to aH^2/s\). This proves every asserted limit for every strictly positive initial condition.

## Verification
The standalone `verify.py` performs exact symbolic identity checks on the nonlinear vector field and tracking variable, rational parameter substitutions covering both sides of the critical value, and numerical integrations at two exact parameter sets. On execution it reports 38 passed checks. An illustrative choice is \(s=1\), \(\delta=1/2\), \(e=1/3\), \(h=1/6\), so \(B=1/3\), \(H=1/2\) and \(m_c=2\). Numerical integrations at \(t=10^5\) give \(tu^2\approx2.01173\) for \(m=2\), compared with its proved limit \(2\); for \(m=3\), they give \(tu\approx5.99777\), compared with its proved limit \(6\). Numerical checks are finite illustrations only; the displayed proof establishes all infinite-time statements.

## Relationship to prior work
Xia, Chen, Srivastava and Parshad (2023), arXiv:2310.10558, introduce exactly this normalized two-patch nonlinear-dispersal system. Their Theorems 2.2 and 2.3 classify coexistence and the qualitative local boundary equilibrium at \(e=B\), including the degenerate \(m=1/H\) value; their local normal-form calculation exhibits the cancellation of the quadratic term. Their Theorem 2.7 establishes global convergence to a positive equilibrium on the *other* side, namely \(e<B\) or \(e=B,m<1/H\). These source results and the standard center-manifold/normal-form implications are prior art, not claimed here. The assessed extension gives an all-positive-data global extinction assertion on the equality branch \(e=B,m\ge1/H\), *with precise initial-condition-independent decay amplitudes and the first nonzero deviation of the second patch from the moving logistic nullcline*. Results on critical relaxation of other Allee-type models concern different vector fields and do not directly imply the stated coefficients. A more general asymptotic theorem might subsume the extension.

## Limitations
The dynamics are deterministic and well mixed within each of two patches, with nonlinear density-dependent dispersal, no external forcing and exact parameter equality \(e=B\). The asymptotic limits are for fixed parameters and positive initial conditions, not uniform in parameters near the double threshold. No claim is made for spatial PDE solutions, finite stochastic populations, the boundary initial set \(u(0)=0\), or transient monotonicity of either coordinate. The qualitative local equilibrium and noncritical positive-equilibrium regimes were established previously. There has been no independent scientific audit or definitive exhaustive priority certification.

## References
1. Y. Xia, L. Chen, V. Srivastava and R. D. Parshad, *Stability and bifurcation analysis of a two-patch model with Allee effect and dispersal*, arXiv:2310.10558 (first public version October 16, 2023), https://arxiv.org/abs/2310.10558, especially Section 2.1, Theorems 2.2, 2.3 and 2.7.
2. Y. Kang and N. Lanchier, *Expansion or extinction: deterministic and stochastic two-patch models with Allee effects*, arXiv:1003.0121 (2010), https://arxiv.org/abs/1003.0121; related patch persistence/extinction phenomenon but a different dispersal model.
