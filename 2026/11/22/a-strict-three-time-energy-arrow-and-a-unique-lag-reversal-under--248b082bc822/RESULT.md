# A strict three-time energy arrow and a unique lag reversal under common partial resetting

## Finding

Consider at least three noninteracting one-dimensional harmonically confined Brownian particles, sharing one Poisson clock of rate \(r>0\). A clock event multiplies **every** particle position by the same fixed \(a\in[0,1)\); between events, particle \(i\) follows \(dX_i=-\kappa X_i\,dt+\sqrt{2D}\,dW_i\), where \(\kappa,D>0\) and the Wiener processes are independent. Work in the unique stationary law. Set
\[
q=a^2,\quad \theta=\frac{r}{2\kappa},\quad
A=1+\theta(1-q),\quad B=2+\theta(1-q^2),\quad C=3+\theta(1-q^3),\quad \Delta=B-A=1+\theta q(1-q).
\]
For three **distinct** particle labels let \(Y_i=\kappa X_i^2/D\) and define their connected, ordered, three-time energy correlation (dimensionless gaps \(s,t\ge0\)) by
\[
\mathcal C(s,t)=\operatorname{cum}\!\left(Y_1(0),Y_2\!\left(\frac{s}{2\kappa}\right),Y_3\!\left(\frac{s+t}{2\kappa}\right)\right).
\]
With the strictly positive constants
\[
V_2=\frac{\theta(1-q)^2}{A^2B},\qquad
H=\frac{2\theta(1-q)^2}{A\Delta},\qquad
T=\frac{2\theta(1-q)^3}{AB\Delta C},
\]
the **exact formula valid for every** \(q\in[0,1)\), \(\theta>0\), and \(s,t\ge0\) is
\[
\boxed{\mathcal C(s,t)=e^{-A(s+t)}\bigl[HV_2-Te^{-\Delta s}\bigr].}
\]
Consequently the temporal-order asymmetry is strict and parameter-universal:
\[
\boxed{\mathcal C(s,t)<\mathcal C(t,s)\quad\text{if and only if}\quad 0\le s<t.}
\]
Although every distinct-particle *two-time* connected energy correlation is \(V_2e^{-A|h|}\), and is therefore insensitive to reversing time, the ordered three-time observable detects an arrow of time for every nontrivial contraction and positive reset rate.

There is also a complete sign classification. If \(\theta(1-q^2)\ge1\), then \(\mathcal C(s,t)>0\) for every \(s>0,t\ge0\); at \(s=0\) it is positive above threshold and exactly zero on the threshold. If \(\theta(1-q^2)<1\), then for each fixed \(t\ge0\) the correlation has exactly one zero as \(s\) varies, located at
\[
\boxed{s_* =\frac{1}{\Delta}\log\!\left(\frac{A^2}{\theta(1-q)C}\right)>0.}
\]
It is strictly negative for \(0\le s<s_*\) and strictly positive for \(s>s_*\). This concerns the **connected correlation of three distinct squared positions**, not single-particle energy skewness or thermodynamic heat.

## Assumptions and scope

The model is an exact continuous-time Ornstein–Uhlenbeck process with a common, externally triggered Poisson position-multiplication event. The contraction \(a\) is nonnegative and strictly less than one; no independent resetting and no particle interactions are present. Measurements are at stationary chronological times. The three labels must be distinct so their conditional Brownian fluctuations factorize. Neither a weak-reset diffusion approximation nor a large-population limit is required; the result holds already for three particles. The dimensionless energy normalization and time rescaling above are essential.

## Proof

Condition on the entire shared Poisson-clock history. Since all Wiener processes are independent, the particle positions are then mutually independent centered Gaussians with the same conditional variance \(D U/\kappa\). Their random normalized variance \(U\) evolves between clock events by \(dU/d\tau=1-U\), in dimensionless time \(\tau=2\kappa t\), and jumps \(U\mapsto qU\) at clock rate \(\theta\). Its generator on smooth functions is
\[
(\mathcal L f)(u)=(1-u)f'(u)+\theta[f(qu)-f(u)].
\]
A stationary construction from the infinite past gives \(0<U\le1\), uniqueness, and moments of every order. For \(m_n=\mathbb E[U^n]\), stationarity and the generator yield
\[
m_0=1,\qquad m_n=\frac{n\,m_{n-1}}{n+\theta(1-q^n)}\quad(n\ge1).
\]
In particular \(\mu=m_1=A^{-1}\), \(m_2=2/(AB)\), and \(m_3=6/(ABC)\). Thus \(\operatorname{Var}(U)=V_2\), and its third centered cumulant is
\[
K_3=m_3-3\mu m_2+2\mu^3
=\frac{2\theta(1-q)^3[\theta(1-q^2)-1]}{A^3BC}.
\]
The equal-time sign of this stationary third cumulant is consistent with the limit of a previously derived finite-population stationary energy-cumulant result. The new assertion concerns its complete unequal-time structure.

For the Markov process \(U\), conditional first and second moments are, exactly,
\[
\mathbb E[U_s\mid U_0=u]=\mu+(u-\mu)e^{-As},
\]
\[
\mathbb E[U_s^2\mid U_0=u]=m_2+\frac{2(u-\mu)}{\Delta}e^{-As}
+\left[u^2-m_2-\frac{2(u-\mu)}{\Delta}\right]e^{-Bs}.
\]
These follow by solving \(\mathcal L u=1-Au\) and \(\mathcal L u^2=2u-Bu^2\). By conditional independence of distinct Brownian particles given the clock,
\[
\mathcal C(s,t)=\operatorname{cum}(U_0,U_s,U_{s+t}).
\]
Moreover the Markov property and the conditional first moment give
\[
\mathcal C(s,t)=e^{-At}\,\mathbb E[(U_0-\mu)(U_s-\mu)^2].
\]
Using the second-moment semigroup and the first three stationary moments, the last expectation equals
\[
HV_2e^{-As}+(K_3-HV_2)e^{-Bs},\quad
H=\frac2\Delta-2\mu=\frac{2\theta(1-q)^2}{A\Delta}>0.
\]
Direct factorization yields \(HV_2-K_3=T>0\), proving the displayed closed form. In particular,
\[
\mathcal C(s,t)-\mathcal C(t,s)
=T e^{-A(s+t)}\left(e^{-\Delta t}-e^{-\Delta s}\right),
\]
which has the stated strict sign whenever \(s\ne t\).

For the sign classification, the bracket \(HV_2-Te^{-\Delta s}\) increases strictly with \(s\) and tends to the positive value \(HV_2\). Its initial value is \(K_3\), whose sign is that of \(\theta(1-q^2)-1\). When this is negative, it has one and only one zero. Solving gives \(s_*=(1/\Delta)\log(T/(HV_2))\); using \(T/(HV_2)=A^2/[\theta(1-q)C]\) gives the stated expression. The identity \(A^2-\theta(1-q)C=\Delta[1-\theta(1-q^2)]\) makes the positive-root condition exact, including the equality boundary.

## Verification

`verify.py` independently checks the three stationary-moment identities, the two conditional polynomial-semigroup equations, the connected triple-correlation identity, the two sign-factorizations and four exact-parameter families with numerical lag evaluations. `simulate.py` uses a separate exact Poisson-event simulation of the latent variance process and checks both sides of the lag reversal in representative parameters. Both scripts completed successfully; the deterministic proof above, not the Monte Carlo output, establishes the universal claims.

For \(q=1/4\) and \(\theta=1/2\), the unique crossover is \(s_*=0.335733380164\ldots\). At \(s=0.1\) the ordered three-energy cumulant is negative for all finite second gaps; at \(s=0.9\) it is positive. If \(\theta=2\) at the same \(q\), it is positive for all nonnegative gaps.

## Relationship to prior work

Tobias Galla, *A diffusion approximation for systems with frequent weak resetting* (arXiv:2602.21635, first version 25 February 2026), develops the shared partial-reset model and studies induced stationary two-particle squared-position correlations in a weak-reset approximation (main text and Supplemental Section S2). The result here treats the **exact Poisson jump process** for all allowed contractions and classifies **ordered three-time, three-particle connected correlations**, which are not supplied by those stationary second-order formulas.

De Mauro, Biroli, Majumdar and Schehr (arXiv:2509.06658) develop stationary conditional independence for simultaneous complete resetting with general waiting laws. De Mauro, Majumdar and Schehr (arXiv:2606.31634) analyze confined complete-reset gases and their stationary correlations. Their complete-reset setting differs from a common partial contraction at all three times; neither cited abstract asserts the present temporal classification. A previously indexed finite-population common-partial-reset result already determines the **stationary, equal-time** third-cumulant sign, and a related result already gives **two-time** cross-energy covariances. These covered pieces are not offered as new findings. The present contribution is the strict three-time reversal inequality together with the complete unequal-time sign-reversal law.

## Limitations

The statistical observable is a connected **triple energy correlation** for distinct labeled particles, not entropy production, heat, or a single-particle time-asymmetry statistic. No measurement-noise or interaction robustness is claimed. Publication-priority uncertainty remains for any unindexed general higher-order correlation formula; full text of some adjacent complete-reset work was not available in this review. The scientific review is not independent validation.

## References

- T. Galla, *A diffusion approximation for systems with frequent weak resetting*, arXiv:2602.21635 (first version 25 February 2026), https://arxiv.org/html/2602.21635.
- G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (first version 8 September 2025), https://arxiv.org/abs/2509.06658.
- G. de Mauro, S. N. Majumdar, G. Schehr, *Effects of confinement in a Brownian gas with simultaneous stochastic resetting and dynamically emergent correlations*, arXiv:2606.31634 (first version 30 June 2026), https://arxiv.org/abs/2606.31634.
