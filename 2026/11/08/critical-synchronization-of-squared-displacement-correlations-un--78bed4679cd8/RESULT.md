# Critical synchronization of squared-displacement correlations under independently reset fluctuating diffusivity

## Finding
For independently reset Brownian coordinates subject to one shared, separately reset random diffusivity, the ratio of their stationary cross-coordinate and same-coordinate squared-displacement lag covariances is explicitly computable, strictly increasing with lag, and exhibits a sharp reset-rate boundary.

Let \(\alpha,\beta,\Lambda>0\) denote the individual-coordinate reset rate, shared-diffusivity reset rate, and diffusivity-noise amplitude, respectively. Define
\[
H_{\alpha,\beta}(t)=\int_0^t e^{(\alpha-\beta)s}\,ds,
\qquad K=\frac{80\Lambda^4}{\alpha^2\beta^2(\alpha+\beta)}.
\]
In the unique stationary law, for every \(t\ge0\) and distinct \(i,j\),
\[
\begin{aligned}
C_{\mathrm{same}}(t)&:=\operatorname{Cov}(X_i(0)^2,X_i(t)^2)
 =K e^{-\alpha t}\bigl(7\alpha+\beta+\alpha^2H_{\alpha,\beta}(t)\bigr),\\
C_{\mathrm{cross}}(t)&:=\operatorname{Cov}(X_i(0)^2,X_j(t)^2)
 =K e^{-\alpha t}\bigl(\alpha+\alpha^2H_{\alpha,\beta}(t)\bigr).
\end{aligned}
\]
The positive ratio \(R(t)=C_{\mathrm{cross}}(t)/C_{\mathrm{same}}(t)\) is strictly increasing, with \(R(0)=\alpha/(7\alpha+\beta)\), and
\[
\lim_{t\to\infty}R(t)=
\begin{cases}
1,&\alpha\ge\beta,\\
\displaystyle\frac{\alpha\beta}{\beta^2+6\alpha\beta-6\alpha^2},&\alpha<\beta.
\end{cases}
\]
At the critical matching of rates \(\alpha=\beta\), the deficit has the **exact** algebraic law
\[
1-R(t)=\frac{7}{8+\alpha t}.
\]
For \(\alpha>\beta\), the deficit instead decays exponentially as
\[
1-R(t)\sim\frac{(6\alpha+\beta)(\alpha-\beta)}{\alpha^2}
 e^{-(\alpha-\beta)t}.
\]
For \(\alpha<\beta\), it approaches a strictly positive constant. Thus matching the two clocks produces a critical algebraic relative-correlation tail, although each unnormalized covariance still decays exponentially times at most a linear polynomial.

A spatial corollary quantifies persistent common-environment fluctuations. With \(Q_d=d^{-1}\sum_{i=1}^d X_i^2\),
\[
\frac{\operatorname{Var}(Q_d)}{(\mathbb E Q_d)^2}
=\frac{5\alpha}{\alpha+\beta}
+\frac{5(6\alpha+\beta)}{d(\alpha+\beta)}
\ \longrightarrow\ \frac{5\alpha}{\alpha+\beta}>0
\quad\text{as }d\to\infty.
\]

## Assumptions and scope
Fix an arbitrary integer \(d\ge2\). Let \(B,W_1,\ldots,W_d\) be independent standard Brownian motions, and let \(N_1,\ldots,N_d,N_{\omega}\) be independent Poisson processes, all independent of the Brownian motions. Each \(N_i\) has rate \(\alpha\), while \(N_{\omega}\) has rate \(\beta\). Between jumps,
\[
 d\Omega_t=\sqrt2\Lambda\,dB_t,\qquad
 dX_i(t)=\sqrt2\Omega_t\,dW_i(t).
\]
At a jump of \(N_i\), **only** \(X_i\) is set to zero. At a jump of \(N_{\omega}\), **only** \(\Omega\) is set to zero. All other variables remain unchanged. In particular the coordinates do not share a position-reset clock; they share only the stochastic environmental diffusivity \(\Omega^2\). The factor \(\sqrt2\) fixes the generator normalization. All claims concern this continuous-time, stationary model, not synchronized resetting or a finite-time transient initialized from the origin.

The process has a unique stationary law: construct \(\Omega_t\) from the Brownian increment since the most recent environment reset and each \(X_i(t)\) from its Ito integral since its most recent individual reset. Two-sided independent Poisson processes have finite backward ages almost surely. This produces a stationary version. For any two initial states coupled with the same future driving noises, after the first environment reset and then a subsequent reset of each coordinate the states agree permanently. Hence the stationary law is unique. Its polynomial moments through degree four are finite: the environment-reset age has finite moments of all orders, and conditional Ito isometry and Gaussian fourth moments, followed by Cauchy–Schwarz for time integrals, give the corresponding finite coordinate moments.

## Proof
The generator for smooth polynomials is
\[
\mathcal L f=\Lambda^2\partial_{\omega\omega}f
+\omega^2\sum_{i=1}^d\partial_{x_ix_i}f
+\alpha\sum_{i=1}^d\bigl[f(\mathbf x^{(i\to0)},\omega)-f(\mathbf x,\omega)\bigr]
+\beta\bigl[f(\mathbf x,0)-f(\mathbf x,\omega)\bigr].
\]
Write \(Y=\Omega^2\). Stationarity of the test polynomials \(Y,Y^2,X_i^2,X_i^2Y,X_i^4,X_i^2X_j^2\) gives the triangular system
\[
\begin{aligned}
0&=2\Lambda^2-\beta\mathbb EY,\\
0&=12\Lambda^2\mathbb EY-\beta\mathbb EY^2,\\
0&=2\mathbb EY-\alpha\mathbb EX_i^2,\\
0&=2\mathbb EY^2+2\Lambda^2\mathbb EX_i^2-(\alpha+\beta)\mathbb E(X_i^2Y),\\
0&=12\mathbb E(X_i^2Y)-\alpha\mathbb EX_i^4,\\
0&=4\mathbb E(X_i^2Y)-2\alpha\mathbb E(X_i^2X_j^2)\quad(i\ne j).
\end{aligned}
\]
The final equation uses **two independent coordinate reset clocks**; replacing the coefficient \(2\alpha\) by \(\alpha\) would describe a different model. Solving yields
\[
\begin{aligned}
\mathbb EY&=\frac{2\Lambda^2}{\beta},
&\mathbb EY^2&=\frac{24\Lambda^4}{\beta^2},\\
\mathbb EX_i^2&=\frac{4\Lambda^2}{\alpha\beta},
&\mathbb E(X_i^2Y)&=\frac{8\Lambda^4(6\alpha+\beta)}{\alpha\beta^2(\alpha+\beta)},\\
\operatorname{Var}(X_i^2)&=K(7\alpha+\beta),
&\operatorname{Cov}(X_i^2,X_j^2)&=K\alpha,\\
\operatorname{Cov}(X_i^2,Y)&=\frac{40\Lambda^4}{\beta^2(\alpha+\beta)}
=\frac{K\alpha^2}{2}.
\end{aligned}
\]
The centered subspace spanned by \(X_j^2-\mathbb EX_j^2\) and \(Y-\mathbb EY\) is invariant under the Markov semigroup, because
\[
\mathcal L(X_j^2-\mathbb EX_j^2)
=-\alpha(X_j^2-\mathbb EX_j^2)+2(Y-\mathbb EY),
\qquad \mathcal L(Y-\mathbb EY)=-\beta(Y-\mathbb EY).
\]
Therefore the conditional expectation at lag \(t\) is
\[
\mathbb E[X_j(t)^2-\mathbb EX_j^2\mid \mathbf X(0),\Omega(0)]
=e^{-\alpha t}\left[(X_j(0)^2-\mathbb EX_j^2)
+2H_{\alpha,\beta}(t)(Y(0)-\mathbb EY)\right].
\]
Multiplying by centered \(X_i(0)^2\) and taking stationary expectations gives both displayed covariance formulas, for \(i=j\) and \(i\ne j\).

Because \(H'_{\alpha,\beta}(t)=e^{(\alpha-\beta)t}>0\), differentiating
\[
R(t)=\frac{\alpha+\alpha^2H_{\alpha,\beta}(t)}{7\alpha+\beta+\alpha^2H_{\alpha,\beta}(t)}
\]
shows strict increase. The three asymptotic regimes follow respectively from \(H\sim e^{(\alpha-\beta)t}/(\alpha-\beta)\), \(H=t\), and \(H\to1/(\beta-\alpha)\). For \(\alpha<\beta\), the denominator \(\beta^2+6\alpha\beta-6\alpha^2\) is strictly positive because \(\beta>\alpha\). Finally, expanding \(\operatorname{Var}(d^{-1}\sum_iX_i^2)\) into diagonal and off-diagonal covariances gives the stated exact spatial fluctuation identity.

## Verification
Run `python verify.py` with Python 3 and SymPy. It independently constructs the polynomial generator, solves its stationary moment equations, checks both two-time covariance expressions, verifies monotonicity and the equal-rate limit, and checks the full finite-\(d\) radial variance identity. These are exact symbolic checks of stated algebraic identities; they supplement, rather than replace, the stationary-existence and asymptotic arguments above.

## Relationship to prior work
Santra, Basu and Sabhapandit (2022) introduced the Brownian stochastic-diffusivity model with a **single joint** reset of the entire position vector and the environment, and derived one-time radial laws and relaxation results. The model here instead resets each coordinate independently and resets the common environment with its own independent clock; the resulting off-diagonal quadratic two-time covariances and their rate-matching boundary are different observables. Kumar, Sadekar and Basu (2020) compare reset protocols for an active Brownian particle with orientation dynamics, rather than the shared unbounded stochastic diffusivity and independently reset coordinates considered here. Stojkoski and collaborators (2021) obtain time correlations for standard Brownian motion under resetting, rather than the two-clock common-volatility quadratic cross-correlation regime. Existing one-coordinate mixed-reset moment identities can supply some stationary marginal moments but not the independently reset multi-coordinate covariance or its long-lag ratio without a further calculation.

## Limitations
The result is for positive Poisson rates and a Brownian environment \(\Omega\) with diffusivity \(\Omega^2\); it does not establish the same threshold for general random environmental processes, renewal reset clocks, partial resets, nonzero position reset points, or correlated driving Brownian motions. The large-\(d\) statement is a second-moment non-self-averaging assertion, not convergence of full distributions. The critical algebraic behavior belongs to the **ratio** of two decaying covariances, not to a nondecaying observable or a thermodynamic phase transition. The literature comparison does not establish publication priority against every possible prior result.

## References
- I. Santra, U. Basu and S. Sabhapandit, *Effect of stochastic resetting on Brownian motion with stochastic diffusion coefficient*, arXiv:2205.00549v1 (first posted 2022-05-01), https://arxiv.org/abs/2205.00549.
- V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294v1 (first posted 2020-08-07), https://arxiv.org/abs/2008.03294.
- V. Stojkoski, T. Sandev, L. Kocarev and A. Pal, *Autocorrelation functions and ergodicity in diffusion with stochastic resetting*, arXiv:2107.11686 (first posted 2021-07-24), https://arxiv.org/abs/2107.11686.
