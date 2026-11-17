# Two distinct optimal resetting rates for non-Gaussian inertial transport

## Finding
Consider free inertial transport in one dimension with velocity-only Poisson resetting. Although the long-time displacement is diffusive, its positive fourth cumulant has a distinct optimal resetting rate from the leading *standardized* excess kurtosis.

For damping \(\gamma>0\), noise intensity \(D>0\), velocity-reset rate \(\lambda>0\), and \(z=\lambda/\gamma\), put \(C_j=\lim_{t\to\infty}\operatorname{cum}_j(X_t)/t\) for even cumulants of the integrated displacement. These limits exist, and
\[
 C_2=\frac{4D}{\gamma^2(z+1)(z+2)},\qquad
 C_4=\frac{96D^2}{\gamma^5}\frac{z(7z^2+28z+27)}{(z+1)^3(z+2)^3(z+3)(z+4)}>0.
\]
The leading standardized kurtosis coefficient is
\[
 K(z)=\lim_{t\to\infty}\gamma t\left(\frac{\mathbb E X_t^4}{(\mathbb E X_t^2)^2}-3\right)
 =\frac{6z(7z^2+28z+27)}{(z+1)(z+2)(z+3)(z+4)}.
\]
The *absolute* rate \(C_4\) has a unique global maximum at \(z=z_{\rm abs}\), whereas \(K\) has a unique global maximum at \(z=z_{\rm rel}\). The two optimizers are the unique positive roots, respectively, of
\[
 P_{\rm abs}(z)=35z^6+406z^5+1806z^4+3782z^3+3487z^2+600z-648
\]
and
\[
 P_{\rm rel}(z)=7z^6+56z^5+116z^4-160z^3-959z^2-1344z-648.
\]
In particular,
\[
 \frac14<z_{\rm abs}<\frac13<2<z_{\rm rel}<3,
 \qquad z_{\rm abs}\simeq0.3091071443,\quad z_{\rm rel}\simeq2.5565366198.
\]
Thus maximizing the fourth-cumulant growth and maximizing the long-time *relative* non-Gaussianity prescribe sharply different reset frequencies; neither optimum depends on \(D\) or \(\gamma\) after division by damping.

## Assumptions and scope
Let \(W\) be standard one-dimensional Brownian motion, and let an independent rate-\(\lambda\) Poisson clock trigger instantaneous changes \(V\mapsto0\) while leaving \(X\) unchanged. Between resets,
\[
 dX_t=V_t\,dt,\qquad dV_t=-\gamma V_t\,dt+\sqrt{2D}\,dW_t.
\]
Take \(X_0=V_0=0\) and \(\gamma,D,\lambda>0\). All assertions are over the entire strict positive parameter domain and concern the asymptotic large-time cumulants of the *unreset position*. The normalized fourth moment uses the zero mean \(\mathbb E X_t=0\). No confining position trap, position reset, refractory phase, or active-force feedback is assumed.

## Proof
**1. Gaussian cycle reward.** Conditional on a reset interval of length \(\tau\), its displacement is Gaussian with mean zero and conditional variance
\[
 q(\tau)=\frac{2D}{\gamma^2}\int_0^\tau(1-e^{-\gamma u})^2\,du
 =\frac{2D}{\gamma^3}\, f(\gamma\tau),
 \quad f(u)=u-\frac32+2e^{-u}-\frac12e^{-2u}.
\]
At every reset the velocity becomes zero; independent Brownian increments make the completed cycle displacements conditionally independent given the Poisson intervals. If \(T_1,T_2,\ldots\) are the exponential inter-reset times, and \(A_t\) is the age after the last reset, then, conditional on the entire clock,
\[
 X_t\mid(T_1,T_2,\ldots)\sim N(0,S_t),\quad
 S_t=\sum_{j\le N_t}q(T_j)+q(A_t).
\]
Consequently \(\mathbb E X_t^2=\mathbb E S_t\) and \(\operatorname{cum}_4(X_t)=3\operatorname{Var}(S_t)\) exactly, for every positive time.

**2. Renewal-reward growth.** Set \(T\sim\operatorname{Exp}(\lambda)\) and \(m=\mathbb E q(T)/\mathbb ET=\lambda\mathbb E q(T)\). Exponential durations have moments of every order and \(q(\tau)\le 2D\tau/\gamma^2\); the centered renewal-reward variance theorem therefore applies, with the incomplete terminal interval contributing a negligible term on the linear-in-time scale:
\[
 \lim_{t\to\infty}\frac{\mathbb E S_t}{t}=m,\qquad
 \lim_{t\to\infty}\frac{\operatorname{Var}(S_t)}{t}
 =\frac{\mathbb E[(q(T)-mT)^2]}{\mathbb ET}
 =\lambda\mathbb E[(q(T)-mT)^2].
\]
The same formula follows by differentiating the renewal transform for the additive reward twice near zero. This is a variance growth theorem, not a finite-time independence assumption for the residual age.

**3. Exact exponential integration.** Write \(U=\gamma T\sim\operatorname{Exp}(z)\). For all integers \(k,n\ge0\),
\[
 \mathbb E[U^n e^{-kU}]=\frac{z\,n!}{(z+k)^{n+1}}.
\]
Substitution into \(f\) gives
\[
 \mathbb Ef(U)=\frac{2}{z(z+1)(z+2)},\quad
 d(z):=z\mathbb Ef(U)=\frac{2}{(z+1)(z+2)},
\]
\[
 v(z):=z\mathbb E[(f(U)-d(z)U)^2]
 =\frac{8z(7z^2+28z+27)}{(z+1)^3(z+2)^3(z+3)(z+4)}.
\]
Since \(q(T)=(2D/\gamma^3)f(U)\) and \(T=U/\gamma\), the limits in Step 2 give \(C_2=(2D/\gamma^2)d(z)\) and \(C_4=(12D^2/\gamma^5)v(z)\), which are exactly the displayed formulas. In addition, the centered fourth cumulant grows linearly while the squared variance grows quadratically, giving \(K(z)=3v(z)/d(z)^2\).

**4. Exactly one optimizer for each criterion.** Direct differentiation yields the exact identities
\[
 v'(z)=-\frac{8P_{\rm abs}(z)}{(z+1)^4(z+2)^4(z+3)^2(z+4)^2},
\]
\[
 K'(z)=-\frac{6P_{\rm rel}(z)}{(z+1)^2(z+2)^2(z+3)^2(z+4)^2}.
\]
The coefficient sequence of \(P_{\rm abs}\) is positive after its negative constant, hence has exactly one sign change. That of \(P_{\rm rel}\), in descending powers, is positive then negative, again exactly one sign change. Descartes' rule gives at most one positive root of each; because both have negative constant and positive leading coefficient, the intermediate value theorem gives at least one. The derivative signs are therefore positive then negative. Both \(v(z)\) and \(K(z)\) tend to zero at both \(0^+\) and \(+\infty\), so their unique critical points are their unique global maximizers. Direct exact substitution yields \(P_{\rm abs}(1/4)<0<P_{\rm abs}(1/3)\) and \(P_{\rm rel}(2)<0<P_{\rm rel}(3)\), proving the sharp separation.

**5. Strict non-Gaussianity at finite time.** For fixed \(t>0\), with positive probability there is no reset, giving conditional variance \(q(t)\); with positive probability there is a reset at \(u\in(0,t)\), giving \(q(u)+q(t-u)<q(t)\), since \(q'(u)=2D(1-e^{-\gamma u})^2/\gamma^2\) is strictly increasing. Thus \(\operatorname{Var}(S_t)>0\) and \(\operatorname{cum}_4(X_t)>0\), consistent with the positive long-time coefficient. This observation is subsidiary; the two optimal-rate theorems are the principal claim.

## Verification
The accompanying standalone `verify.py` uses exact exponential-polynomial integration, algebraically checks the two cumulant expressions and derivative factorizations, proves the required rational root brackets, and reproduces the fourth-cumulant growth for three reset rates through an independent Laplace-transformed Markov-generator moment hierarchy. It prints the two positive numerical roots only after symbolic tests pass. Algebraic computations support the identities; the global uniqueness argument is the analytic Descartes/intermediate-value proof, not numerical root isolation.

## Relationship to prior work
Olsen and Löwen (2024) study **the same velocity-only reset dynamics** and establish general propagator/moment recursions, including the second-moment effective diffusivity. Meylahn, Sabhapandit and Touchette (2015) study the **mathematically equivalent integrated reset Ornstein–Uhlenbeck process** and supply a more general renewal generating-function and large-deviation framework. Neither inspected full text supplies the two explicit global fourth-cumulant optimization theorems and their separation; the current result is an explicit exact specialization and classification within those existing frameworks, not a new resetting formalism. Smith and Majumdar (2022) study integrated reset Brownian motion without restoring drift, which yields the singular zero-friction boundary but not these finite-damping optima. Standard renewal-reward variance theory underlies Step 2.

## Limitations
The expression is for independent constant-rate Poisson *velocity* resets to zero and constant drag; it does not cover position resetting, colored thermal noise, non-Poisson clock laws or nonlinear friction. The long-time excess-kurtosis coefficient is not a fixed-time non-Gaussianity optimum. The zero-friction limit is singular as a rate optimization problem and is not asserted. The general generating functions and the underlying exact model were already established in earlier publications; these facts imply the new formulas are derivable from existing machinery, and an unlocated earlier explicit optimization could supersede the claimed priority. No independent audit has been performed.

## References
- K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685 (first public version 2024-01-23), https://arxiv.org/abs/2401.12685.
- J. M. Meylahn, S. Sabhapandit and H. Touchette, *Large deviations for Markov processes with resetting*, arXiv:1510.02431 (first public version 2015-10-08), https://arxiv.org/abs/1510.02431.
- N. R. Smith and S. N. Majumdar, *Condensation transition in large deviations of self-similar Gaussian processes with stochastic resetting*, arXiv:2202.03546 (first public version 2022-02-07), https://arxiv.org/abs/2202.03546.
- M. Zamparo, *Large deviation principles for renewal-reward processes*, arXiv:2207.07521 (2022), https://arxiv.org/abs/2207.07521.
