# Unique noisy-sampling design for quartic Wiener path energy

## Finding
Let \(B\) be standard Brownian motion on \([0,1]\), \(Q_4=\int_0^1 B_t^4\,dt\), and \(Y_x=B_x+\varepsilon\), where \(\varepsilon\sim N(0,\eta)\) is independent and \(\eta\geq0\). For each fixed finite \(\eta\), among every predetermined observation time \(x\in[0,1]\), the conditional-mean estimator \(\mathbb E[Q_4\mid Y_x]\) has a **unique** minimum mean-square-error design \(x=x_4(\eta)\) in \((0,1)\). It is the unique interior root of the explicit polynomial \(P_\eta(x)\) below. This root is strictly later than the unique optimal observation time for \(Q_2=\int_0^1 B_t^2\,dt\), for the *same* noise variance. In particular,
\[
 x_4(0)=0.82176036367851510875\ldots>3/4=x_2(0),\qquad
 x_4(\eta)=1-\frac{1}{8\eta}+O(\eta^{-2})\quad(\eta\to\infty).
\]
The exact risk for every \(x\in(0,1]\) is \(R_4(x,\eta)=38/5-I_4(x,\eta)\), where
\[
 I_4(x,\eta)=\frac{72A(x)^2}{(x+\eta)^2}+\frac{24C(x)^2}{(x+\eta)^4},\qquad
 A(x)=\frac{x^2}{2}-\frac{x^4}{4},\quad C(x)=x^4\left(1-\frac{4x}{5}\right).
\]
At zero noise, \(x_4(0)\) is the unique root in \((0,1)\) of \(993x^4-1600x^3+200x^2+300=0\), giving \(R_4(x_4(0),0)=0.98279877316005239878\ldots\). The endpoint observation \(x=1\) instead gives \(R_4(1,0)=107/50\).

## Assumptions and scope
All times are selected deterministically before seeing the process. Exactly one scalar observation is taken, with independent centered Gaussian noise of **known finite variance** \(\eta\ge0\). Noise at different candidate locations is not jointly realized; each location defines its own design experiment. The estimator minimizes unconditional squared error and is the exact conditional expectation, not an ordinary plug-in power integral. Brownian variance convention is \(\mathbb E[B_sB_t]=\min(s,t)\). At \(x=0,\eta=0\) the observation is deterministic and conveys no information; define \(I_4(0,0)=0\) by continuity.

## Proof
**Gaussian-chaos risk identity.** Put \(v=x+\eta\), \(c_t=\min(t,x)\), \(Z=Y_x/\sqrt v\), and \(H_2(z)=z^2-1\), \(H_4(z)=z^4-6z^2+3\). Conditioning a jointly Gaussian pair gives
\[
\mathbb E[Q_4\mid Y_x]=1+\frac{6A(x)}vH_2(Z)+\frac{C(x)}{v^2}H_4(Z),
\]
where \(A=\int_0^1 t c_t^2\,dt\) and \(C=\int_0^1 c_t^4\,dt\). The displayed elementary integrals are exactly the polynomials above. Since \(\mathbb EH_2(Z)^2=2\), \(\mathbb EH_4(Z)^2=24\), and the Hermite polynomials are orthogonal, the explained variance is \(I_4\). Wick's rule, applied to \(B_s^4\) and \(B_t^4\), yields
\[
 \operatorname{Cov}(B_s^4,B_t^4)=72st\min(s,t)^2+24\min(s,t)^4.
\]
Integration over the unit square gives \(\operatorname{Var}(Q_4)=72/12+24/15=38/5\). The conditional-expectation orthogonality identity proves the risk formula.

**Global uniqueness certificate.** For \(0<x\le1\), direct exact differentiation gives
\[
 \frac{\partial I_4}{\partial x}=\frac{3x^3}{25(x+\eta)^5}P_\eta(x),
\]
with
\[
\begin{aligned}
P_\eta(x)={}&(300x^4-900x^2+600)\eta^3
 +(825x^5-2400x^3+1500x)\eta^2\\
&+(2030x^6-2880x^5-500x^4+1200x^2)\eta\\
&+993x^7-1600x^6+200x^5+300x^3.
\end{aligned}
\]
Set \(u=x/(1-x)\), so \(x=u/(1+u)\). The polynomial \((1+u)^7P_\eta(u/(1+u))=\sum_{k=0}^7 c_ku^k\) has coefficients, in ascending degree,
\[
\begin{aligned}
c_0&=600\eta^3,\\
c_1&=300\eta^2(14\eta+5),\\
c_2&=300\eta(39\eta^2+30\eta+4),\\
c_3&=300(55\eta^3+67\eta^2+20\eta+1),\\
c_4&=100(123\eta^3+204\eta^2+115\eta+12),\\
c_5&=5(900\eta^3+1785\eta^2+1524\eta+400),\\
c_6&=10\eta(60\eta^2+105\eta+77),\\
c_7&=-(75\eta^2+150\eta+107).
\end{aligned}
\]
For every \(\eta\ge0\), after zero coefficients are removed, this sequence has *exactly one sign change*. Descartes' rule of signs therefore gives at most one positive root, counting multiplicity. The transformed polynomial is positive at small positive \(u\) and negative for large \(u\), so exactly one positive root exists. Accordingly \(I_4\) rises, then falls strictly, on \((0,1)\); its unique global maximum is interior. This argument covers the noiseless boundary without extrapolation from a finite numerical grid.

**Strict ordering with quadratic-energy sensing.** Let \(F(x)=\int_0^1 c_t^2dt=x^2(1-2x/3)\). The explained variance for \(Q_2\) is \(I_2(x,\eta)=2F(x)^2/v^2\). Its unique maximum is
\[
 x_2(\eta)=\frac{3-6\eta+\sqrt{36\eta^2+60\eta+9}}8\in(0,1).
\]
At this point \((F/v)'=0\). On \((0,1)\) exact differentiation gives
\[
 \left(\frac{A}{F}\right)'=\frac{3(x-2)(x-1)}{2(2x-3)^2}>0,
 \qquad \left(\frac{C}{F^2}\right)'=\frac{72(x-1)}{5(2x-3)^3}>0.
\]
Thus \((A/v)'\) and \((C/v^2)'\) are both strictly positive at \(x_2(\eta)\). Both terms in \(I_4\) therefore increase at this point. The established unique turning point of \(I_4\) must lie strictly to its right. This proves \(x_4(\eta)>x_2(\eta)\) for every finite noise level.

**Boundary and asymptotics.** At \(\eta=0\), the interior stationarity equation reduces to the quartic given under Finding and has exactly one root by the same sign certificate. At \(\eta\to\infty\), the first variance component dominates and \(A\) has its unique maximum on \([0,1]\) at \(1\); hence \(x_4(\eta)\to1\). Substituting \(x=1-c/\eta\) into the exact stationarity derivative yields \(\partial_x I_4=\eta^{-3}(72c-9)+O(\eta^{-4})\). The implicit-function theorem applied to the rescaled derivative at \(1/\eta=0\) gives a root branch \(c=1/8+O(\eta^{-1})\); global uniqueness identifies that branch with the optimum, proving the stated expansion.

## Verification
`verify_quartic_design.py` performs exact symbolic integrations, Gaussian-covariance and derivative identities, all eight coefficient identities of the Descartes certificate, the quadratic-energy comparison derivatives, and the noiseless endpoint and root evaluations; it also performs supplementary dense numerical comparisons for seven noise levels. Run `python verify_quartic_design.py` with the package's requirements. The symbolic identities and sign certificate, *not* the finite evaluations, establish the all-parameter theorem.

## Relationship to prior work
Foster, Lyons and Oberhauser's *An Optimal Polynomial Approximation of Brownian Motion* (arXiv:1904.06998, first posted 15 April 2019) gives Gaussian polynomial path representations and exact conditional estimates of a **quadratic** Brownian time integral using endpoint and space-time-area information; it does not optimize a single noisy observation for an integrated fourth power. Cui and Chronopoulou's *Optimal Sampling for Estimation of Fractional Brownian Motion* (arXiv:2304.07661) optimizes observation schedules for **aggregate state-reconstruction distortion** under deterministic or level-triggered sampling, not a nonlinear quartic integral and its two Hermite projections. Kałuża, Morkisz and Przybyłowicz (arXiv:1812.10708) address minimax approximate Itô integration with noisy information, a different error and observation model. Standard Gaussian conditioning and Hermite orthogonality are acknowledged as known tools; the asserted finding is the exact global one-observation quartic design and its strict comparison with the quadratic target, not a new conditioning formula.

## Limitations
The theorem does not cover adaptive or multiple measurements, non-Gaussian observation noise, stochastic or unknown noise variances, arbitrary linear observations of the full path, or other stochastic kernels. At infinite noise there is only a limiting design, not a finite-variance optimum at the endpoint. Publication priority is qualified: an older unindexed work could possibly contain an equivalent design; the accessible compared results do not imply it. The numerical comparison grid is not a proof of uniqueness. Independent scientific review has not been performed.

## References
1. J. Foster, T. Lyons, H. Oberhauser, *An Optimal Polynomial Approximation of Brownian Motion*, arXiv:1904.06998v1, 15 April 2019, https://arxiv.org/abs/1904.06998.
2. X. Cui, A. Chronopoulou, *Optimal Sampling for Estimation of Fractional Brownian Motion*, arXiv:2304.07661v1, 16 April 2023, https://arxiv.org/abs/2304.07661.
3. A. Kałuża, P. M. Morkisz, P. Przybyłowicz, *Optimal Approximation of Stochastic Integrals in Analytic Noise Model*, arXiv:1812.10708v1, 27 December 2018, https://arxiv.org/abs/1812.10708.
