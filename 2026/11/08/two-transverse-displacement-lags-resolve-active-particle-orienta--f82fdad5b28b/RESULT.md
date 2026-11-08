# Two transverse displacement lags resolve active-particle orientation-resetting rates, while one full lag can fail

## Finding

For a planar active Brownian particle whose *orientation*, but not position, is reset at Poisson times to a fixed direction, **the mean drift and two transverse displacement variances at distinct finite lags recover all three unknown parameters**: propulsion speed, orientation-reset rate, and rotational diffusivity. No orientation measurements are needed. The exact range of compatible observations is characterized by a single strict ratio interval.

The two-lag requirement is not merely a count of unknowns: even the *full two-dimensional mean and covariance* at a single lag can have two distinct positive-parameter explanations. An exact rational pair of ambiguity branches is supplied below.

## Assumptions and scope

Let \(v,r,d>0\), \(D\ge0\), and let \(B_t\) be standard planar Brownian motion independent of the angular Brownian motion and reset clock. The planar position \((X_t,Y_t)\) obeys

\[
\mathrm dX_t=v\cos\Theta_t\,\mathrm dt+\sqrt{2D}\,\mathrm dB_t^{(1)},\qquad
\mathrm dY_t=v\sin\Theta_t\,\mathrm dt+\sqrt{2D}\,\mathrm dB_t^{(2)}.
\]

The heading \(\Theta_t\), taken modulo \(2\pi\), diffusively evolves with generator \(d\partial_{\theta\theta}\) and resets instantaneously to zero at independent Poisson rate \(r\). It begins in its unique stationary distribution; the initial position is arbitrary. Translational diffusivity \(D\) and the reset direction are known. All observations are **exact ensemble quantities**. Write \(\Delta X_t=X_t-X_0\), \(\Delta Y_t=Y_t-Y_0\) and fix any two \(0<t_1<t_2<\infty\).

Define the drift and thermal-subtracted transverse excesses

\[
u=\frac{\mathbb E\Delta X_t}{t},\qquad
A_i=\operatorname{Var}(\Delta Y_{t_i})-2Dt_i,\qquad R=\frac{A_2}{A_1}.
\]

The drift \(u\) is independent of the chosen positive \(t\). Define \(H_\lambda(t)=\int_0^t(t-s)e^{-\lambda s}\,\mathrm ds=[e^{-\lambda t}-1+\lambda t]/\lambda^2\) for \(\lambda>0\).

**Complete range and inversion.** Precisely the triples satisfying

\[
u>0,\qquad A_1>0,\qquad \frac{t_2}{t_1}<R<\left(\frac{t_2}{t_1}\right)^2
\]

arise from unique \((v,r,d)\in(0,\infty)^3\). Recover \(\lambda=r+d\) uniquely from \(R=H_\lambda(t_2)/H_\lambda(t_1)\), then \(z=r/d\) uniquely from

\[
\frac{(1+z)^2}{z^2(4+z)}=\frac{A_1}{4u^2H_\lambda(t_1)},
\]

and finally

\[
\boxed{v=\frac{u(1+z)}{z},\quad r=\frac{\lambda z}{1+z},\quad d=\frac{\lambda}{1+z}.}
\]

**One-lag nonidentifiability.** At \(t=1\) and \(D=1\), the identical one-lag mean vector and covariance matrix

\[
\mathbb E(\Delta X,\Delta Y)=(1,0),\qquad
\operatorname{Cov}((\Delta X,\Delta Y)^{\mathsf T})=\begin{pmatrix}76/25&0\\0&3\end{pmatrix}
\]

are attained by two distinct strictly positive parameter triples whose reset-to-rotation ratios are \(z_1=2/13\) and \(z_2=1/4\). Thus adding the longitudinal variance at the same lag does not always replace a second lag.

## Proof

**Step 1: stationary angular harmonics and covariances.** The angular generator is

\[
\mathcal Lf(\theta)=d f''(\theta)+r[f(0)-f(\theta)].
\]

Its resetting and elliptic diffusion yield a unique stationary probability distribution. For integer \(n\ge1\), stationarity applied to \(\cos(n\theta)\) and \(\sin(n\theta)\) gives

\[
\mathbb E\cos(n\Theta)=\frac{r}{r+n^2d},\qquad
\mathbb E\sin(n\Theta)=0.
\]

In particular, with \(\lambda=r+d\) and \(z=r/d\),

\[
\mathbb E\cos\Theta=\frac{z}{1+z},\quad
\mathbb E\sin^2\Theta=\frac2{z+4},\quad
\operatorname{Var}(\cos\Theta)=\frac{2+5z}{(4+z)(1+z)^2}.
\]

The angular generator maps both centered observables \(\sin\Theta\) and \(\cos\Theta-\mathbb E\cos\Theta\) to \(-\lambda\) times themselves. The Markov semigroup therefore gives stationary lag covariances \(e^{-\lambda s}\) times their respective lag-zero variances. Independent translational Brownian noise adds \(2Dt\) to each displacement variance and no cross covariance. Integrating the stationary velocity covariance twice yields

\[
\mathbb E\Delta X_t=\frac{vz}{1+z}t,
\]

\[
\operatorname{Var}(\Delta Y_t)-2Dt
=\frac{4v^2}{z+4}H_\lambda(t),
\]

\[
\operatorname{Var}(\Delta X_t)-2Dt
=\frac{2v^2(2+5z)}{(z+4)(1+z)^2}H_\lambda(t).
\]

Reflection symmetry about the reset axis makes the cross covariance zero. These identities also match the stationary-start forward formulas in Baouche et al. (2024), Eqs. (17)–(18), with their \(\Lambda=z\).

**Step 2: strict invertibility of the lag ratio.** For positive \(\lambda\), write \(w_{t,\lambda}(s)=(t-s)e^{-\lambda s}\mathbf1_{0<s<t}\). Differentiation under the integral shows

\[
\frac{\partial}{\partial\lambda}\log H_\lambda(t)
=-\frac{\int_0^t s w_{t,\lambda}(s)\,\mathrm ds}{\int_0^t w_{t,\lambda}(s)\,\mathrm ds}.
\]

For \(t_2>t_1\), the likelihood ratio \(w_{t_2,\lambda}(s)/w_{t_1,\lambda}(s)=(t_2-s)/(t_1-s)\) is strictly increasing on \((0,t_1)\), and the longer-lag weight has additional positive support \((t_1,t_2)\). Hence its normalized distribution strictly stochastically dominates the shorter-lag one, in particular has strictly larger mean \(s\). It follows that

\[
\frac{\mathrm d}{\mathrm d\lambda}\log\frac{H_\lambda(t_2)}{H_\lambda(t_1)}<0.
\]

The elementary dominated-convergence limits are

\[
\lim_{\lambda\downarrow0}\frac{H_\lambda(t_2)}{H_\lambda(t_1)}
=\left(\frac{t_2}{t_1}\right)^2,
\qquad
\lim_{\lambda\to\infty}\frac{H_\lambda(t_2)}{H_\lambda(t_1)}=\frac{t_2}{t_1}.
\]

The map is therefore a continuous strictly decreasing bijection onto the stated open interval, giving one and only one positive \(\lambda\).

**Step 3: strict invertibility of the rate ratio.** Substitute \(v=u(1+z)/z\) into the transverse formula. Then

\[
\frac{A_1}{4u^2H_\lambda(t_1)}=g(z),\qquad
g(z)=\frac{(1+z)^2}{z^2(z+4)}.
\]

For every \(z>0\),

\[
\frac{g'(z)}{g(z)}=-\frac{2}{z(1+z)}-\frac{1}{z+4}<0,
\]

and \(g(z)\) decreases continuously from \(+\infty\) to zero. Therefore precisely one positive \(z\) matches any positive observed amplitude. The stated formulas recover positive \(v,r,d\), which reproduce all observations. This proves necessity, sufficiency and global injectivity.

**Step 4: strict one-lag ambiguity despite the full covariance.** At any single time, define the ratio of longitudinal to transverse *thermal-subtracted* variances. Step 1 gives

\[
h(z)=\frac{\operatorname{Var}(\Delta X_t)-2Dt}{\operatorname{Var}(\Delta Y_t)-2Dt}=
\frac{2+5z}{2(1+z)^2},\qquad
h'(z)=\frac{1-5z}{2(1+z)^3}.
\]

Thus \(h\) increases to its strict maximum \(h(1/5)=25/24\), then decreases. In particular

\[
h(2/13)=h(1/4)=26/25,\qquad
g(2/13)=325/24,\quad g(1/4)=100/17.
\]

Set \(u=1\), \(t=1\), \(D=1\), and target transverse excess \(A=1\). Because \(H_\lambda(1)\) decreases continuously and strictly from \(1/2\) to zero, there are unique positive rates \(\lambda_1,\lambda_2\) solving

\[
H_{\lambda_1}(1)=6/325,\qquad H_{\lambda_2}(1)=17/400.
\]

For each \(z_i\), set \(v_i=(1+z_i)/z_i\), \(r_i=\lambda_i z_i/(1+z_i)\), and \(d_i=\lambda_i/(1+z_i)\). Both triples are strictly positive, yield the same mean \((1,0)\), and have thermal-subtracted variances \((26/25,1)\), hence the stated full covariance. They are distinct because their \(z\) differ. This completes the theorem.

## Verification

The standalone Python 3 script `CHECK.py` checks the exact rational identities for both ambiguity branches, independently evaluates the Markov-generator forward moment formulas, reconstructs parameters from pairs of finite lags in 200 seeded positive-parameter cases, and checks the strict lag-ratio bounds on a separate grid. It reports 1,063 exact or numerical diagnostic assertions. Numerical inversion uses bisection only; no sampled grid substitutes for the analytical monotonicity proof. An illustrative exact-model data set with \((v,r,d,D)=(3,2,1,1/2)\) at \((t_1,t_2)=(1/2,2)\) reconstructs \((v,r,d)\) as \((3,2,1)\).

## Relationship to prior work

Baouche, Franosch, Meiners and Kurzthaler (2024) provide the orientational resetting model, its stationary heading law, drift, finite-time displacement variance formulas, full intermediate scattering function, and forward applications. Their Eqs. (17)–(18) are rederived here and **credited**. The added statement is the complete *inverse* range, global two-lag recovery, and a constructive one-lag full-covariance obstruction; none is asserted by the forward moment formulas themselves. Kumar, Sadekar and Basu (2020) discuss the same orientation-reset mechanism, often with a fixed initial heading, and the resulting forward fluctuation regimes. They do not give this stationary-heading, two-lag inverse classification. The ordinary scalar exponential-covariance method determines a relaxation rate once its amplitude is known; the distinct issue here is simultaneous unknown speed and two rates, resolved through two independent monotone reductions and a matching one-lag counterexample.

## Limitations

The assertion is **structural identifiability from exact ensemble moments**. It requires strictly positive \(v,r,d\), known \(D\) and reset direction, stationary initial heading, and two distinct strictly positive lag times. It does not cover an unknown translational diffusion, arbitrary reset-angle distributions, renewal rather than Poisson resetting, noisy or finite-sample data, parameter-estimation conditioning near the open compatibility boundaries, or position resetting. The one-lag counterexample concerns first and second displacement moments, not the full one-lag probability distribution. Independent publication-priority review has not been performed; an equivalent result in unindexed calibration literature remains possible.

## References

1. Y. Baouche, T. Franosch, M. Meiners and C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769 (first public version 2024-05-10), especially Eqs. (17)–(18) and Appendix C. https://arxiv.org/abs/2405.06769
2. V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294 (first public version 2020-08-07), especially Sec. V. https://arxiv.org/abs/2008.03294
