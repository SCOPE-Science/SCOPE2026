# Sharp Gaussian occupation fluctuations under threshold resetting of sluggish diffusion

## Finding

An exact central-limit variance for the positive-half-axis occupation fraction of a threshold-reset sluggish diffusion is available for every sluggishness exponent and every nonnegative interior reset location. At the symmetric reset point, the variance simplifies to a rational function of the sluggishness exponent. Comparing with Poisson resetting at the **same long-run mean frequency of reset events**, threshold resetting has a strictly smaller asymptotic occupation variance, by an explicitly increasing factor ranging from one third to three quarters.

Write \(\beta=\alpha+2\), \(C=(\alpha+1)(\alpha+2)\), and \(\rho=x_0/L\). Define
\[
  p_{\alpha}(\rho)=1-\frac{1-\rho}{2(1-\rho^{\beta})},\qquad
  K_{\rho}(y)=(1+\min\{\rho,y\})(1-\max\{\rho,y\}),
\]
where \(0\le\rho<1\), and set \(q_{\rho}(y)=p_{\alpha}(\rho)\) for \(y<0\) and \(q_{\rho}(y)=1-p_{\alpha}(\rho)\) for \(y>0\). Its value at zero is immaterial. Then the full fluctuation coefficient is the strictly positive, elementary integral
\[
 V_{\alpha,L}(\rho)=\frac{L^{\beta}}{C(1-\rho^{\beta})}
 \int_{-1}^{1}K_{\rho}(y)
 \left[\frac12-\beta q_{\rho}(y)|y|^{\beta-1}\right]^2\,dy.
\]
For the occupation fraction \(\xi_T=T^{-1}\int_0^T\mathbf1_{\{X_t>0\}}\,dt\),
\[
  \sqrt{T}\bigl(\xi_T-p_{\alpha}(\rho)\bigr)
      \ \Longrightarrow\ \mathcal N(0,V_{\alpha,L}(\rho)),
 \qquad \lim_{T\to\infty}T\operatorname{Var}(\xi_T)=V_{\alpha,L}(\rho).
\]
In particular, with resetting to the origin \(\rho=0\),
\[
 \boxed{\ V_{\alpha,L}(0)=
 \frac{3(\alpha+1)L^{\alpha+2}}{4(\alpha+2)(\alpha+3)(2\alpha+3)}\ }.
\]
The mean inter-reset time is \(m=L^{\alpha+2}/[(\alpha+1)(\alpha+2)]\). Independent Poisson resetting of the same free diffusion to the origin at rate \(r=m^{-1}\) has occupation-fraction coefficient
\[
 V_{\mathrm P}=\frac{\alpha+1}{2(\alpha+2)r}
               =\frac{L^{\alpha+2}}{2(\alpha+2)^2}.
\]
Therefore the sharp equal-frequency ratio is
\[
 \boxed{\ \frac{V_{\alpha,L}(0)}{V_{\mathrm P}}=
 R(\alpha)=\frac{3(\alpha+1)(\alpha+2)}{2(\alpha+3)(2\alpha+3)}\ }.
\]
For every \(\alpha\ge0\), \(\frac13\le R(\alpha)<\frac34\), with equality at the lower end only for \(\alpha=0\). Moreover
\[
 R'(\alpha)=\frac{3(3\alpha^2+10\alpha+9)}{2(\alpha+3)^2(2\alpha+3)^2}>0,
 \qquad \lim_{\alpha\to\infty}R(\alpha)=\frac34.
\]

## Assumptions and scope

Fix \(\alpha\ge0\), a threshold distance \(L>0\) and a reset location \(0\le x_0<L\). Between resets, the process is the **conservative natural-scale time-change** of Brownian motion with generator \(\partial_x^2\) by the clock \(\int |B_s|^\alpha\,ds\). Thus, away from the origin, the physical-time generator is \(\mathcal Lf(x)=|x|^{-\alpha}f''(x)\). In particular, for \(\alpha>0\), the apparently singular origin is specified by this time-change, not by an arbitrary boundary extension. Each excursion begins at \(x_0\), stops upon first reaching \(\pm L\), and resets *instantaneously* to \(x_0\), with an independent Brownian excursion thereafter. Occupation of the isolated point zero has zero physical time. Observation time \(T\) is physical time; there is no pause or return duration. The comparison with Poisson resetting uses \(x_0=0\), the same free dynamics and matched **expected event frequency**, not matched spatial cost or identical stationary distributions.

## Proof

**1. Excursion renewal and first moment.** Let \(B\) be Brownian motion of generator \(\partial_x^2\), started at \(x_0\), and \(S=\inf\{s:|B_s|=L\}\). Define the physical excursion duration and positive occupation reward by
\[
 \tau=\int_0^S |B_s|^\alpha\,ds,\qquad
 H=\int_0^S |B_s|^\alpha\mathbf1_{\{B_s>0\}}\,ds.
\]
The time-change construction makes these the actual physical-time observables. The killed Brownian Green kernel is
\[
 G(x,y)=\frac{(L+\min\{x,y\})(L-\max\{x,y\})}{2L}.
\]
By Green occupation integration,
\[
 \mathbb E_{x_0}\tau=\frac{L^\beta-x_0^\beta}{C},\quad
 \frac{\mathbb E_{x_0}H}{\mathbb E_{x_0}\tau}
 =p_{\alpha}(\rho)=1-\frac{1-\rho}{2(1-\rho^\beta)}.
\]
The latter is the known renewal occupation mean; it is reproduced to fix normalization and the exact time-change convention. Because \(|B_s|^\alpha\le L^\alpha\) before exit, \(\tau\le L^\alpha S\). The exit time \(S\) has a positive exponential moment. Hence all required excursion reward and duration moments exist.

**2. Centered excursion variance.** Put \(p=p_{\alpha}(\rho)\), \(h(x)=\mathbf1_{\{x>0\}}\), and \(Z=H-p\tau\). Define the unique continuous \(u\), with continuous first derivative and Dirichlet values \(u(\pm L)=0\), satisfying
\[
 -u''(x)=|x|^\alpha(h(x)-p).
\]
Direct integration on either side of the origin yields
\[
 u(x)=\frac1C\begin{cases}
 \dfrac{1-2p}{2}L^\beta+\dfrac12L^{\beta-1}x
 -(1-p)x^\beta,&x\ge0,\\[3pt]
 \dfrac{1-2p}{2}L^\beta+\dfrac12L^{\beta-1}x
 +p(-x)^\beta,&x<0.
 \end{cases}
\]
Its first derivative agrees at zero, and substituting \(p\) gives \(u(x_0)=0\). Apply ordinary Itô calculus to \(u(B_{s\wedge S})\) (there is no local-time term because \(u'\) is continuous). At \(S\), both \(u(B_S)\) and \(u(x_0)\) vanish, and the centered reward \(Z\) equals the stopped Brownian stochastic integral \(\int_0^S\sqrt2\,u'(B_s)\,dW_s\). Thus Itô isometry and the killed Green formula give the exact identity
\[
 \mathbb E_{x_0}Z^2=2\int_{-L}^{L}G(x_0,y)[u'(y)]^2\,dy.
\]
In dimensionless coordinates \(y/L\), the displayed derivative equals
\[
 u'(Ly)=\frac{L^{\beta-1}}C
 \left[\frac12-\beta q_\rho(y)|y|^{\beta-1}\right].
\]
Substitution and division by \(\mathbb E\tau\) yields precisely \(V_{\alpha,L}(\rho)\). Positivity follows because the Green kernel is positive in the open interval and \(u'\) is not identically zero.

**3. Gaussian limit and second moments.** Independent restarts supply iid pairs \((\tau_j,H_j)\). Their centered rewards \(Z_j=H_j-p\tau_j\) have mean zero and finite exponential moments. The classical renewal-reward central limit theorem gives
\[
 \sqrt T(\xi_T-p)\Longrightarrow \mathcal N\left(0,
 \frac{\mathbb E Z_1^2}{\mathbb E\tau_1}\right).
\]
The incomplete last excursion is negligible at scale \(\sqrt T\). Exponential tails of the bounded-domain exit times give the uniform moment control needed for convergence of \(T\operatorname{Var}(\xi_T)\) as well. This proves the general assertion.

**4. Exact symmetric constant.** At \(x_0=0\), \(p=1/2\) and
\[
 u'(x)=\frac{L^{\alpha+1}-(\alpha+2)|x|^{\alpha+1}}{2C}.
\]
The Green integral reduces to
\[
 \frac{\mathbb E_0 Z^2}{\mathbb E_0\tau}=
 \frac{L^\beta}{2C}\int_0^1(1-y)
 [1-\beta y^{\beta-1}]^2\,dy.
\]
The integral equals \(3(\alpha+1)^2/[2(\alpha+3)(2\alpha+3)]\), yielding the stated closed constant, including the normal-diffusion boundary \(\alpha=0\).

**5. Equal-frequency comparison.** At the origin, a free excursion of deterministic duration \(t\) has sign-occupation fraction variance \((1-\mu)/4\), with \(\mu=1/\beta\), by the known Lamperti law. For independent exponential Poisson cycles of rate \(r\), their second duration moment is \(2/r^2\). Renewal reward therefore gives \(V_{\mathrm P}=r\,(1-\mu)\mathbb E\tau_{\mathrm P}^2/4=(1-\mu)/(2r)\). Equating \(r\) to the inverse mean threshold excursion time gives the quoted ratio. Direct differentiation establishes strict monotonicity and endpoint bounds. The calculation does **not** follow merely from comparing stationary spatial distributions, since occupation variance is a temporal observable.

## Verification

The standalone `checker.py` uses exact rational polynomial integrations (integer \(\alpha\), rational \(\rho\)) to compare the first two centered-reward-moment representations and independent Green-energy representations. It separately checks noninteger exponents by piecewise numerical quadrature and compares finite-difference killed-chain solutions with the continuous coefficients. Running `python checker.py` passes 300 assertions. Representative exact symmetric coefficients at \(L=1\) are \(V_{0,1}(0)=1/24\), \(V_{1,1}(0)=1/40\), and \(V_{2,1}(0)=9/560\); the respective equal-frequency ratios are \(1/3\), \(9/20\), and \(18/35\). Computational checks are finite corroboration, not a substitute for Steps 1–5.

## Relationship to prior work

Frimpong, Bresque and Roldán (arXiv:2610.21962v1, first posted 2026-10-15), Section 6.1.2 and equations (72)–(75), derive the threshold-reset occupation *law of large numbers* and its deterministic limit, and note fluctuation scaling of order \(T^{-1/2}\) without the exact coefficient. Their Section 6.1.1, equation (71), gives the Poisson-reset Gaussian variance. The present result uses their physical model, known occupation mean and Poisson reference, but supplies the threshold **central-limit variance**, the full reset-location quadrature and the strict exact equal-frequency protocol factor. These conclusions are not a reformulation of the first-moment occupation law.

Den Hollander, Majumdar, Meylahn and Touchette (arXiv:1801.09909), Sections II and IV, study Brownian additive occupation functionals with **Poisson** resetting; their general renewal transform and occupation calculations are important background, but do not give the stopped-excursion variance for position-triggered sluggish diffusion. Bressloff (arXiv:2009.01968) treats a Poisson-reset run-and-tumble particle, a different process. Biswas, Majumdar and Pal (arXiv:2603.25338) optimize first-passage search with threshold resetting, not time-averaged sign-occupation variance. The standard renewal-reward CLT and stopped-Brownian Poisson equations are credited as established tools; the claimed contribution is their exact application, constants and protocol comparison. A related exact stationary *radial* ordering under matched reset frequency, identifier `205973d7-b09c-4079-9192-c7dff5ed8265`, addresses one-time distributions, not temporal variance.

## Limitations

The formulas concern a continuous natural-scale diffusion, not an exact finite-lattice walk, and require instantaneous complete reset, fixed boundaries, and \(\alpha\ge0\). The equal-rate strict improvement is shown at the symmetric reset location \(x_0=0\); no all-location protocol dominance is claimed. Comparing equal mean reset-event rates is not comparing equal per-event return costs or stationary positional laws. No finite-observation-time Gaussian error bound or large-deviation rate function is claimed. More general published regenerative-functional results could imply the abstract CLT, so novelty attaches specifically to the exact coefficient and monotone protocol ratio; no independent priority audit has been performed.

## References

1. T. D. Frimpong, L. Bresque and É. Roldán, *Sluggish random walks with resetting: nonequilibrium aspects*, arXiv:2610.21962v1 (2026-10-15), https://arxiv.org/abs/2610.21962. In particular Sections 2, 3, 6.1.1 and 6.1.2.
2. F. den Hollander, S. N. Majumdar, J. M. Meylahn and H. Touchette, *Properties of additive functionals of Brownian motion with resetting*, arXiv:1801.09909 (2018), https://arxiv.org/abs/1801.09909.
3. P. C. Bressloff, *Occupation time of a run-and-tumble particle with resetting*, arXiv:2009.01968 (2020), https://arxiv.org/abs/2009.01968.
4. A. Biswas, S. N. Majumdar and A. Pal, *Optimal threshold resetting in collective diffusive search*, arXiv:2603.25338 (2026), https://arxiv.org/abs/2603.25338.
