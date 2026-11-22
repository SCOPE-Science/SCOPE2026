# A universal friction ordering of reset-clock fluctuations under power-law velocity resetting

## Finding

A deterministic, continuously driven particle with viscous damping and velocity-dependent stochastic resetting has a strict ordering of **every normalized convex waiting-time risk** as the damping changes, including its long-time reset-count Fano factor. Fix force \(F>0\), reset prefactor \(\lambda>0\), power \(\alpha>-1\), and damping \(\gamma>0\). Starting at zero velocity after each reset, the particle follows \(\dot v=F-\gamma v\); the instantaneous reset hazard is \(\lambda v^\alpha\). Let \(T_\gamma\) be an inter-reset duration, \(m_\gamma=\mathbb E T_\gamma\), and \(Z_\gamma=T_\gamma/m_\gamma\).

For every \(0<\gamma_1<\gamma_2\):

- If \(\alpha>0\), \(Z_{\gamma_1}\) is **strictly smaller in convex order** than \(Z_{\gamma_2}\).
- If \(-1<\alpha<0\), the strict convex-order comparison reverses.
- If \(\alpha=0\), all \(Z_\gamma\) are unit-mean exponential.

Thus the asymptotic reset-count Fano factor
\[
\mathcal F_\gamma=\lim_{t\to\infty}\frac{\operatorname{Var}N(t)}{\mathbb E N(t)}
=\frac{\operatorname{Var}T_\gamma}{m_\gamma^2}
\]
is **strictly increasing** in \(\gamma\) for \(\alpha>0\), **strictly decreasing** for \(-1<\alpha<0\), and identically one for \(\alpha=0\). Its sharp endpoint limits are
\[
\lim_{\gamma\downarrow0}\mathcal F_\gamma=
\frac{\Gamma(1+2/(\alpha+1))}{\Gamma(1+1/(\alpha+1))^2}-1,
\qquad
\lim_{\gamma\to\infty}\mathcal F_\gamma=1.
\]
Both inequalities relative to the endpoints are strict at finite positive damping for \(\alpha\ne0\). In particular, the lower endpoint at \(\alpha=1\) is \(4/\pi-1\), while at \(\alpha=-1/2\) the upper endpoint is \(5\).

The approach to Poissonian count noise has the sharp leading coefficient. Define
\[
\kappa=\lambda F^\alpha,\quad
\varepsilon=\kappa\gamma^{-(\alpha+1)},\quad
c_\alpha=\int_0^\infty\!\left[(1-e^{-u})^\alpha-1\right]du.
\]
For \(\gamma\to\infty\), \(\alpha>-1\),
\[
\mathcal F_\gamma=1+2c_\alpha\varepsilon+O(\varepsilon^2).
\]
Here \(c_\alpha<0\) for \(\alpha>0\), \(c_\alpha>0\) for \(-1<\alpha<0\), and \(c_0=0\); for example \(c_1=-1\), \(c_2=-3/2\), \(c_{-1/2}=2\log2\).

## Assumptions and scope

There is **no thermal acceleration noise**; the velocity resets exactly to zero; all post-reset trajectories and event clocks are independent and identically distributed. A reset does not stop the process permanently. The force and reset prefactor are held fixed when damping changes. A divergent hazard immediately after a reset when \(-1<\alpha<0\) is allowed: its cumulative integral is finite near zero. All stated waiting-time moments exist because the hazard tends to the positive constant \(\lambda(F/\gamma)^\alpha\) as the cycle ages. Convex order means \(\mathbb E\Phi(Z_{\gamma_1})\le\mathbb E\Phi(Z_{\gamma_2})\) for every convex test function for which expectations exist; strictness holds for strictly convex functions with finite expectations.

## Proof

**1. Exact renewal law.** Along one excursion,
\[
v_\gamma(t)=\frac F\gamma(1-e^{-\gamma t}),\qquad
\Pr(T_\gamma>t)=\exp\!\left[-\kappa\gamma^{-(\alpha+1)}H_\alpha(\gamma t)\right],
\quad H_\alpha(y)=\int_0^y(1-e^{-s})^\alpha ds.
\]
The cumulative hazard is finite at zero for \(\alpha>-1\) and grows linearly at infinity. Since each reset starts the same deterministic trajectory with an independent hazard clock, intervals are independent copies. Standard renewal variance asymptotics for finite second moments give the count-Fano identity in the Finding.

**2. Strict quantile-ratio ordering.** Set \(f_\alpha(y)=(1-e^{-y})^\alpha\) and define the hazard elasticity \(E_\alpha(y)=y f_\alpha(y)/H_\alpha(y)\). Its reciprocal is
\[
\frac1{E_\alpha(y)}=\int_0^1\frac{f_\alpha(sy)}{f_\alpha(y)}ds.
\]
For every fixed \(0<s<1\), the logarithmic derivative of the integrand with respect to \(y\) has the sign of
\[
\alpha\left(\frac{sy}{e^{sy}-1}-\frac{y}{e^y-1}\right).
\]
The bracket is strictly positive because \(z/(e^z-1)\) strictly decreases on \((0,\infty)\) (differentiate, or use \(e^z(1-z)<1\)). Consequently \(1/E_\alpha(y)\) strictly increases for \(\alpha>0\), strictly decreases for \(-1<\alpha<0\), and is constant for \(\alpha=0\). Integrability of \(f_\alpha(sy)\) near \(s=0\) is guaranteed by \(\alpha>-1\).

Write \(Q_\gamma(p)\) for the waiting-time quantile, put \(z=-\log(1-p)>0\), and set \(y_\gamma=\gamma Q_\gamma(p)\). The quantile equation is
\[
H_\alpha(y_\gamma)=\frac{z\gamma^{\alpha+1}}\kappa.
\]
For fixed \(z\), \(y_\gamma\) strictly increases with \(\gamma\). Implicit differentiation gives
\[
\frac{\partial\log Q_\gamma(p)}{\partial\log z}=
\frac1{E_\alpha(y_\gamma)}.
\]
Therefore \(Q_{\gamma_2}(p)/Q_{\gamma_1}(p)\) strictly increases with \(p\) when \(\alpha>0\), and strictly decreases when \(-1<\alpha<0\). This is a strict star/relative-dispersion order, including *the whole distribution*, not just its variance.

**3. Convex order after normalization.** Divide each quantile by its mean. Since both normalized quantiles integrate to one over \(0<p<1\), their strictly monotone ratio crosses one exactly once. For \(\alpha>0\), the larger-damping quantile lies below the smaller-damping quantile at low ranks and above at high ranks; the signs reverse when \(\alpha<0\). The integrated-quantile criterion for equal-mean convex order proves the claims, strictly for strictly convex tests. Taking \(\Phi(x)=x^2\) proves strict monotonicity of the inter-reset squared coefficient of variation and hence of \(\mathcal F_\gamma\).

**4. Sharp limits.** For \(\gamma\downarrow0\), the cumulative hazard converges to \(\kappa t^{\alpha+1}/(\alpha+1)\). The waiting time thus converges in moments to a Weibull law of shape \(\alpha+1\). Uniform integrability follows by bounding small-positive-damping survivals by a fixed positive-damping exponential-tail survival when \(\alpha>0\), and by the limiting Weibull survival when \(\alpha<0\). This gives the stated gamma-function endpoint.

For strong damping define the terminal hazard \(r_\infty=\kappa\gamma^{-\alpha}\) and scaled interval \(Y=r_\infty T_\gamma\). Its exact survival is \(\Pr(Y>y)=\exp[-\varepsilon H_\alpha(y/\varepsilon)]\). Let
\[
D_\alpha(u)=H_\alpha(u)-u-c_\alpha.
\]
Both \(D_\alpha\) and \(uD_\alpha(u)\) are absolutely integrable: \(D_\alpha\) is bounded at zero and decays exponentially at infinity. Therefore, with \(\varepsilon\downarrow0\), comparison with \(e^{-y-c_\alpha\varepsilon}\) yields
\[
\mathbb EY=e^{-c_\alpha\varepsilon}+O(\varepsilon^2),\qquad
\mathbb EY^2=2e^{-c_\alpha\varepsilon}+O(\varepsilon^3).
\]
Substitution into \(\mathbb EY^2/(\mathbb EY)^2-1\) proves the expansion \(1+2c_\alpha\varepsilon+O(\varepsilon^2)\), and gives convergence to unit-mean exponential after normalization. The coefficient has its claimed sign by inspection of the integrand defining \(c_\alpha\).

## Verification

Run `python verify.py` with Python 3, NumPy and SciPy. The program independently integrates exact survival functions for \(\alpha=-1/2,1,2\), confirms strict Fano-factor directions at five damping values each, checks the quantile-ratio ordering at forty-one probability ranks, and checks first-order strong-damping asymptotics. This numerical check is a consistency test, not an exhaustive proof; the infinite-parameter assertion rests on the analytical elasticity and quantile argument above.

## Relationship to prior work

Takeishi and Akimoto (2026) introduced the velocity-power resetting model, derived frictionless Weibull inter-reset times for general \(\alpha\), and treated the damped deterministic \(\alpha=1\) model through its stationary velocity distribution. Those known distributions and the model itself are not new here. The new claim is the **global, parameter-uniform convex-order comparison across every positive friction level**, for all \(\alpha>-1\), together with the sharp Fano bounds and strong-friction coefficient.

Eule and Metzger (2016) developed general renewal-reset stationary-state theory; it underlies the counting-process interpretation but does not state this friction-dependent distributional order. The stochastic-order concepts are classical, including the distributional comparisons discussed by Arab, Hadjikyriakou and Oliveira (2025); the specific driven velocity-hazard order and sharp asymptotics are derived here. These comparisons do not establish publication priority against every unindexed source.

## Limitations

The result does not include thermal velocity noise, random post-reset velocities, randomly fluctuating damping, or nonlinear drag. It does not claim an exact finite-time Fano factor, only the long-time limit. The strong-damping expansion has fixed \(F,\lambda,\alpha\); it is not uniform as \(\alpha\downarrow-1\) or as the physical parameters vary. Strict scientific novelty is assessed relative to checked accessible literature and indexed records, not certified against all unpublished work. Independent verification has not been performed.

## References

1. Y. Takeishi and T. Akimoto, *Breakdown of Linear Response Induced by Velocity-Dependent Stochastic Resetting*, arXiv:2603.14164, first publicly submitted 15 March 2026. https://arxiv.org/abs/2603.14164
2. S. Eule and J. J. Metzger, *Non-equilibrium steady states of stochastic processes with intermittent resetting*, New Journal of Physics 18, 033006 (2016); arXiv:1510.07876. https://arxiv.org/abs/1510.07876
3. I. Arab, M. Hadjikyriakou, P. E. Oliveira, *Stochastic orders and shape properties for a new distorted proportional odds model*, Statistical Papers 66, article 107 (2025). https://doi.org/10.1007/s00362-025-01730-w
4. M. Shaked and J. G. Shanthikumar, *Stochastic Orders*, Springer (2007), for standard quantile-based stochastic-order terminology.
