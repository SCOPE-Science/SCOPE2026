# Static-state blindness and a sharp temporal-memory crossover under run-and-tumble resetting

## Finding

A non-absorbing thermal run-and-tumble particle on the whole line resets its position to a fixed site, while independently flipping its direction at each reset with probability \(\eta\). **Its entire stationary joint position–direction law is independent of \(\eta\), but every positive-lag stationary position covariance decreases strictly with \(\eta\).** The covariance is exactly a two-rate expression, and its long-time relaxation crosses sharply between direction-memory and reset-memory control.

Fix \(v,D,\alpha,r>0\) and \(0\le\eta\le1\). Let \(S_t\in\{-1,1\}\), and between resets let
\[
 dX_t=vS_t\,dt+\sqrt{2D}\,dW_t,
\]
where \(S_t\) changes sign at rate \(\alpha\). Independently, Poisson resets at rate \(r\) set \(X_t=x_{\mathrm R}\) and flip \(S_t\) with probability \(\eta\) (otherwise retaining its sign). There is no absorbing boundary. Work in the unique stationary law and put \(Y_t=X_t-x_{\mathrm R}\), \(\beta_\eta=\alpha+\eta r\), and
\[
 V=\frac{2D}{r}+\frac{2v^2}{r(r+2\alpha)},\qquad B=\frac{v^2}{r+2\alpha}.
\]
For every \(t\ge0\),
\[
 \boxed{C_\eta(t):=\operatorname{Cov}(Y_0,Y_t)
 =V e^{-rt}+B\int_0^t e^{-r(t-u)}e^{-2\beta_\eta u}\,du.}
\]
Equivalently, for \(r\ne2\beta_\eta\),
\[
 C_\eta(t)=V e^{-rt}+B\frac{e^{-2\beta_\eta t}-e^{-rt}}{r-2\beta_\eta},
\]
while at resonance \(r=2\beta_\eta\),
\[
 C_\eta(t)=e^{-rt}(V+Bt).
\]
In particular, if \(0\le\eta_1<\eta_2\le1\), then \(C_{\eta_1}(t)>C_{\eta_2}(t)\) for **every** \(t>0\), despite the identical one-time stationary laws. If the other model parameters are known, a single fixed positive-lag covariance therefore determines \(\eta\) uniquely.

The exact long-time relaxation rate is
\[
 \lim_{t\to\infty}-\frac1t\log C_\eta(t)=\min\{r,2\alpha+2\eta r\}.
\]
When \(0<\alpha<r/2\), this changes at the unique interior threshold \(\eta_c=\tfrac12-\alpha/r\): the leading decay is \(e^{-2\beta_\eta t}\) for \(\eta<\eta_c\), \(t e^{-rt}\) at \(\eta=\eta_c\), and \(e^{-rt}\) for \(\eta>\eta_c\). If \(\alpha\ge r/2\), the relaxation rate equals \(r\) for all \(\eta\), with resonance only at the boundary \(\alpha=r/2,\eta=0\).

The integrated stationary covariance is also explicit:
\[
 \boxed{\int_0^\infty C_\eta(t)\,dt=\frac{V}{r}+\frac{v^2}{2r(r+2\alpha)(\alpha+\eta r)},}
\]
and decreases strictly in \(\eta\).

## Assumptions and scope

The theorem concerns the stationary law on \(\mathbb R\times\{-1,1\}\), not first-passage motion with an absorbing target. All rates and the thermal diffusion coefficient are strictly positive; \(\eta\) includes both endpoints. The reset point \(x_{\mathrm R}\in\mathbb R\) is arbitrary and removed by centering. Brownian motion, ordinary velocity-flip times, reset times, and independent Bernoulli reset-flip marks have the independence stipulated above. All covariances are ensemble covariances in the stationary process. The result covers all \(t\ge0\), with the negative-lag covariance determined by symmetry.

## Proof

**1. Generator and stationary direction balance.** For a twice differentiable test function \(f\), the generator is
\[
 \begin{aligned}
 \mathcal L_\eta f(y,s)={}&vs\,\partial_y f(y,s)+D\partial_y^2 f(y,s)
 +\alpha[f(y,-s)-f(y,s)]\\
 &+r\big[(1-\eta)f(0,s)+\eta f(0,-s)-f(y,s)\big].
 \end{aligned}
\]
The autonomous direction process is the symmetric two-state chain of switching rate \(\beta_\eta=\alpha+\eta r>0\); its unique invariant marginal assigns probability \(1/2\) to each sign. In the stationary forward equation the incoming reset mass at \(y=0\), for either sign, is consequently \(r[(1-\eta)/2+\eta/2]=r/2\). Thus the stationary joint forward equation, including the source, is independent of \(\eta\). Its uniqueness follows by conditioning on the most recent reset, whose backward age has law \(\operatorname{Exp}(r)\), and on the asymptotically fair direction at that reset: between that reset and observation there are no further resets and the dynamics is the ordinary diffusive telegraph process. This construction also shows finiteness of all polynomial stationary moments.

More explicitly, let \(k\in\mathbb R\) and \(s_k=r+Dk^2\). Transforming the two no-reset direction equations and integrating over the exponential age gives the stationary transforms
\[
 \begin{aligned}
 \mathbb E[e^{ikY}]&=\frac{r(s_k+2\alpha)}{s_k(s_k+2\alpha)+v^2k^2},\\
 \mathbb E[S e^{ikY}]&=\frac{i r v k}{s_k(s_k+2\alpha)+v^2k^2}.
 \end{aligned}
\]
Neither contains \(\eta\). In particular \(\mathbb E[Y]=0\), and the stationary law is the same for every reset-flip probability. This stationary insensitivity, without thermal broadening, was already established for the run-and-tumble protocol in Evans–Majumdar (2018); it is a premise and not the originality claim here.

**2. Exact equal-time moments.** Direct generator calculations give
\[
 \mathcal L_\eta y=vs-ry,\quad
 \mathcal L_\eta s=-2\beta_\eta s,\quad
 \mathcal L_\eta(ys)=v-(r+2\alpha)ys,
\]
\[
 \mathcal L_\eta y^2=2vys+2D-ry^2.
\]
At stationarity, \(\mathbb E[YS]=v/(r+2\alpha)\), and \(\mathbb E[Y^2]=V\). In particular, reset-associated direction flips do not enter the \(YS\) balance: every reset sets the product to zero regardless of the new sign.

**3. Conditional regression and two-time covariance.** For an initial pair \((Y_0,S_0)=(y,s)\), the orientation mean is \(\mathbb E[S_t\mid s]=s e^{-2\beta_\eta t}\). The position mean satisfies
\[
 \frac{d}{dt}\mathbb E[Y_t\mid y,s]
 =v s e^{-2\beta_\eta t}-r\mathbb E[Y_t\mid y,s],\qquad \mathbb E[Y_0\mid y,s]=y.
\]
Hence
\[
 \mathbb E[Y_t\mid y,s]=e^{-rt}y+vs\int_0^t e^{-r(t-u)}e^{-2\beta_\eta u}\,du.
\]
Multiply by \(Y_0\), take the stationary mean, and substitute the equal-time moments from step 2. This proves the full covariance formula and the continuous resonant value.

**4. Strict ordering, identification, and sharp decay.** For \(\eta_1<\eta_2\) and \(t>0\), the difference of the two covariance integrands is strictly positive for every \(u\in(0,t)\). Since \(B>0\), strict covariance ordering follows; continuity and strict monotonicity make the map from \(\eta\) to any fixed positive-lag covariance injective when other parameters are fixed. Evaluating the elementary exponential convolution shows that its slowest rate is \(\min(r,2\beta_\eta)\), with a positive leading coefficient in either nonresonant regime and the explicit positive \(Bt\) prefactor at resonance. Since \(\beta_\eta=\alpha+\eta r\), the stated complete threshold classification follows, including endpoint cases.

**5. Integrated covariance.** The convolution is nonnegative. Tonelli's theorem and \(\alpha>0\) give
\[
 \int_0^\infty\!\int_0^t e^{-r(t-u)}e^{-2\beta_\eta u}\,du\,dt
 =\frac1{2r\beta_\eta}.
\]
Inserting \(B\) yields the exact integral and strict dependence on \(\eta\).

## Verification

Run the included script using Python with NumPy and SciPy:

```bash
python checker.py
```

The script independently checks the covariance formula against the finite-dimensional backward semigroup on a grid of 1,080 parameter/lag combinations. It checks the invariant characteristic transform against a direct matrix resolvent at nine more parameter/wavenumber combinations. Finally, it samples 100,000 exact stationary backward ages and uses event-driven path evolution, with future Brownian increments integrated out conditionally, to check covariance at three velocity-reset protocols. The random seed is fixed for reproducibility. The analytic argument above, not Monte Carlo or a finite grid, supplies all-parameter and all-time assertions.

## Relationship to prior work

Evans and Majumdar (2018, arXiv:1808.06450) introduced the protocol in the pure run-and-tumble case and proved that its stationary position distribution is independent of the reset-flip probability. That static invariance and the underlying renewal formalism are prior results. Pal and collaborators (2024, arXiv:2407.03762) added translational thermal diffusion and examined first-passage search times and their dependence on flipping at resets; their analyzed observables are absorbed hitting times, not the unrestricted stationary two-time position covariance. Bressloff (arXiv:2411.15544, first submitted 2024-11-23) develops a general stochastic-calculus formulation for diffusive run-and-tumble particles with resets to a prescribed complete state, not an explicit covariance for probabilistic reset reversals. The present assertion concerns the strictly ordered *two-time* covariance, an exact one-lag identifiability result and a sharp spectral decay crossover, not a new stationary invariance theorem or a new generator formalism.

## Limitations

The result assumes a constant-rate Poisson reset clock independent of the particle state, a symmetric two-state orientation process, independent Gaussian thermal noise, and instantaneous resetting to one location. Neither an absorbing target, asymmetric tumbling, state-dependent reset events, partial positional resets, nor non-Poisson inter-reset distributions are covered. Single-lag identification presumes that the other parameters are known; it does not address noisy finite-sample inference. A slowest-rate crossover of an autocorrelation is a spectral relaxation transition, not a thermodynamic phase transition or a nonanalytic change in the stationary marginal. Publication priority is not independently certified; a general Markov-generator theorem might imply parts of the result without displaying this specific closed form.

## References

1. M. R. Evans and S. N. Majumdar, *Run and tumble particle under resetting: a renewal approach* (first public 2018-08-20), arXiv:1808.06450, https://arxiv.org/abs/1808.06450.
2. P. S. Pal, J.-M. Park, A. Pal, H. Park and J. S. Lee, *Is active motion beneficial for target search with resetting in a thermal environment?* (first public 2024-07-04), arXiv:2407.03762, https://arxiv.org/abs/2407.03762.
3. P. C. Bressloff, *Stochastic calculus of run-and-tumble motion: an applied perspective* (first public 2024-11-23), arXiv:2411.15544, https://arxiv.org/abs/2411.15544.
