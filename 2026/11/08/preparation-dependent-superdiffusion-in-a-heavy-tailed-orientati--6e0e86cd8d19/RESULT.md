# Preparation-dependent superdiffusion in a heavy-tailed orientationally reset swimmer

## Finding

For a planar active Brownian swimmer that resets **only its heading** at independent Lomax renewal times with survival
\[\mathbb P(T>t)=(1+t/\tau)^{-\alpha},\qquad 1<\alpha<2,\quad \tau>0,\]
the longitudinal displacement has an exact superdiffusive variance exponent \(3-\alpha\). The leading coefficient depends on how the renewal clock is initialized. Let \(\mu=\tau/(\alpha-1)\), \(c=\tau^\alpha\), and \(k=1-\mathbb E e^{-dT}\in(0,1)\), with positive rotational diffusivity \(d\) and propulsion speed \(v\). For observation starting immediately after a reset (fresh preparation) and observation of the same dynamics with an equilibrium-stationary renewal clock and heading (stationary preparation), respectively,
\[
\begin{aligned}
\operatorname{Var}(X_t-X_0)_{\rm fresh}&\sim \frac{2c}{\mu^3(2-\alpha)(3-\alpha)}\left(\frac{vk}{d}\right)^2t^{3-\alpha},\\
\operatorname{Var}(X_t-X_0)_{\rm stationary}&\sim \frac{2c}{\mu^3(\alpha-1)(2-\alpha)(3-\alpha)}\left(\frac{vk}{d}\right)^2t^{3-\alpha}.
\end{aligned}
\]
The ratio of stationary to fresh leading coefficients is exactly \(1/(\alpha-1)\). In either preparation the perpendicular displacement has \(\operatorname{Var}(Y_t-Y_0)=O(t)\), despite the superdiffusive longitudinal variance. Both preparations have the same positive asymptotic longitudinal drift \(v k/(d\mu)\); for equilibrium-stationary preparation this is also the exact drift at every \(t\ge0\).

## Assumptions and scope

Let \(v,d,\tau>0\), \(D_{\mathrm t}\ge0\), and \(1<\alpha<2\). Between renewal times a swimmer has heading \(\theta_t\) and planar position \((X_t,Y_t)\) satisfying
\[d\theta_t=\sqrt{2d}\,dB_t,\qquad dX_t=v\cos\theta_t\,dt+\sqrt{2D_{\mathrm t}}\,dW_t^x,\qquad dY_t=v\sin\theta_t\,dt+\sqrt{2D_{\mathrm t}}\,dW_t^y.\]
The three driving Brownian motions are independent; renewal interarrival times \(T_1,T_2,\ldots\) are i.i.d., strictly positive, independent of the Brownian motions, and have the stated Lomax survival. At every renewal only \(\theta\) is reset to zero, while position is continuous. The resetting line points along the positive \(X\)-axis. In fresh preparation, time zero is a renewal instant, and \(\theta_0=0\). In stationary preparation, use a two-sided equilibrium renewal process, with time-zero age distribution \(\mathbb P(A\in da)=\mathbb P(T>a)\,da/\mu\), correctly coupled to the residual lifetime and to Brownian heading evolution since the last renewal. Spatial displacement always means \((X_t-X_0,Y_t-Y_0)\); a stationary spatial location law is not asserted. Variances are centered about the true preparation-specific means, not the deterministic linear drift.

For the Lomax law, \(\mathbb E T=\mu=\tau/(\alpha-1)\) but \(\mathbb E T^2=\infty\). The coefficient \(k\) can be independently evaluated from
\[k=d\int_0^\infty e^{-ds}(1+s/\tau)^{-\alpha}\,ds=1-\alpha e^{d\tau}(d\tau)^\alpha\Gamma(-\alpha,d\tau),\]
where \(\Gamma(a,z)\) denotes the upper incomplete gamma function. The two displayed formulas are equivalent by integration by parts.

## Proof

**1. Reduction of longitudinal motion to renewal counts.** Let \(N(t)\) count heading-reset events in \((0,t]\). Itô's formula for \(\cos\theta_t\), incorporating its jump back to one at each reset, gives
\[
\cos\theta_t-\cos\theta_0=-d\int_0^t\cos\theta_s\,ds-\sqrt{2d}\int_0^t\sin\theta_s\,dB_s+\sum_{j=1}^{N(t)}(1-\cos\theta_{S_j^-}).
\]
For complete fresh cycles define \(Z_j=1-\cos\theta_{S_j^-}\), where the pre-reset heading is that of an independent Brownian segment of length \(T_j\) started at zero. Then \(0\le Z_j\le2\), these rewards are i.i.d., and \(\mathbb E Z_j=k=1-\mathbb E e^{-dT}\). Thus, in fresh preparation,
\[X_t-X_0=\frac{vk}{d}N(t)+R_t,\]
where \(R_t\) consists of bounded endpoints, the sum of centered cycle rewards scaled by \(v/d\), the angular Itô martingale, and the independent translational Brownian displacement. Its second moment satisfies \(\mathbb E R_t^2=O(t+1)\). Indeed, let \(K=N(t)+1\). It is a stopping index in the i.i.d. completed *potential* cycles, and the centered bounded-reward martingale stopped at \(K\) has \(L^2\) norm squared \(\operatorname{Var}(Z_1)\mathbb E K=O(t+1)\). Removing the one uncompleted reward is uniformly bounded. The angular martingale has quadratic-variation expectation at most \(2dt\). The stationary version differs only by an initial, possibly long, **residual** cycle: its terminal reset reward is bounded by two, and later cycles have the same i.i.d. law. The same second-moment remainder bound holds, because stationary expected renewal counts are \(t/\mu\). For both preparations the mean-renewal theorem and the \(L^2\) bound give drift \(vk/(d\mu)\). For stationary preparation the exact mean follows also from \(\mathbb E\cos\theta_0=\mu^{-1}\int_0^\infty e^{-da}\mathbb P(T>a)da=k/(d\mu)\).

In both cases, \(\operatorname{Var}N(t)=\Theta(t^{3-\alpha})\), as shown below. By Cauchy--Schwarz, the covariance of \(N(t)\) with \(R_t\) is \(O(t^{(4-\alpha)/2})=o(t^{3-\alpha})\) because \(\alpha<2\), while \(\operatorname{Var}R_t=O(t)\). Therefore
\[\operatorname{Var}(X_t-X_0)\sim (vk/d)^2\operatorname{Var}N(t).\]
The effective coefficient is nonzero because \(v,k,d>0\).

**2. Exact renewal asymptotics for fresh preparation.** Set \(f\) for the density of \(T\), \(\widehat f(s)=\mathbb E e^{-sT}\), and \(u(t)=\sum_{n\ge1} f^{*n}(t)\) for the ordinary renewal density. The Lomax tail gives, by splitting \(\int_0^\infty e^{-st}\mathbb P(T>t)dt\) at large times,
\[\widehat f(s)=1-\mu s+b s^\alpha+o(s^\alpha),\quad b=\frac{c\Gamma(2-\alpha)}{\alpha-1}>0,\qquad s\downarrow0.\]
Consequently
\[\widehat u(s)=\frac{\widehat f(s)}{1-\widehat f(s)}=\frac1{\mu s}+\frac{b}{\mu^2}s^{\alpha-2}+o(s^{\alpha-2}).\]
For clarity on the Tauberian step: the Lomax density is a positive mixture of exponential densities. Indeed its survival is the Laplace transform of a Gamma mixing law. Therefore \((1-\widehat f(s))/s\) is a Stieltjes function; the reciprocal divided by \(s\) is again Stieltjes, so \(u(t)\) is completely monotone, with nonnegative, nonincreasing correction \(u(t)-1/\mu\). Applying the monotone-density Karamata theorem to its last Laplace asymptotic yields
\[u(t)=\frac1\mu+\frac{c}{\mu^2(\alpha-1)}t^{1-\alpha}+o(t^{1-\alpha}).\]
Write \(\beta=2-\alpha\in(0,1)\), \(C=c/[\mu^2(\alpha-1)]\), and \(A=C/\beta\). Hence the fresh expected count \(m(t)=\mathbb E N(t)=\int_0^t u(s)ds\) satisfies
\[m(t)=t/\mu+A t^\beta+o(t^\beta).\]
The exact factorial-moment identity is
\[\mathbb E[N(t)(N(t)-1)]=2\int_0^t m(t-s)u(s)\,ds.\]
Insert the expansions, use convolution of regularly varying functions, and collect all terms larger than order \(t\):
\[\mathbb E[N(N-1)]=t^2/\mu^2+\frac{4A}{\mu(\beta+1)}t^{\beta+1}+o(t^{\beta+1}).\]
The \(\mathbb EN\) contribution to \(\mathbb EN^2\) is only \(O(t)\), while
\[(\mathbb EN)^2=t^2/\mu^2+(2A/\mu)t^{\beta+1}+o(t^{\beta+1}).\]
Subtracting gives
\[\operatorname{Var}N_{\rm fresh}(t)\sim\frac{2A(1-\beta)}{\mu(1+\beta)}t^{1+\beta}=\frac{2c}{\mu^3(2-\alpha)(3-\alpha)}t^{3-\alpha}.\]
The use of the smooth Lomax law and monotone renewal density justifies the time-domain expansions; a leading-term Tauberian statement for \(\mathbb EN^2\) alone would not justify subtraction of the leading squared mean.

**3. Exact equilibrium-renewal variance.** A stationary renewal clock has intensity \(1/\mu\), \(\mathbb EN_{\rm stationary}(t)=t/\mu\), and second-factorial product density \(u(h)/\mu\) at time separation \(h>0\). Therefore, without any finite second moment assumption,
\[\operatorname{Var}N_{\rm stationary}(t)=\frac t\mu+\frac2\mu\int_0^t(t-s)\left(u(s)-\frac1\mu\right)ds.\]
Substitution of \(u(s)-1/\mu\sim C s^{\beta-1}\) yields
\[\operatorname{Var}N_{\rm stationary}(t)\sim\frac{2C}{\mu\beta(1+\beta)}t^{\beta+1}=\frac{2c}{\mu^3(\alpha-1)(2-\alpha)(3-\alpha)}t^{3-\alpha}.\]
The ratio is exactly \(1/(\alpha-1)\). The equilibrium process genuinely differs from an immediate reset: its first residual lifetime has survival \((1+t/\tau)^{1-\alpha}\), rather than \((1+t/\tau)^{-\alpha}\).

**4. No perpendicular superdiffusion.** Apply Itô's formula to \(\sin\theta\), including jump \(-\sin\theta_{S_j^-}\). It expresses \(\int_0^t\sin\theta_s ds\) as bounded endpoints plus a bounded-integrand Brownian martingale and a sum of renewal rewards \(\sin\theta_{S_j^-}\). Given each interval duration, a Brownian heading has a symmetric distribution; each reward has zero conditional mean and absolute value at most one. The same stopping-index argument bounds the reward-sum second moment by \(O(t+1)\), even though \(\mathbb ET^2=\infty\). The initial equilibrium residual segment changes at most one bounded reward. Adding independent translational diffusion proves \(\operatorname{Var}(Y_t-Y_0)=O(t)\).

## Verification

The self-contained \(checker.py\) performs deterministic checks of the exact renewal-count asymptotic constants, the preparation coefficient ratio and independently integrated angular-reward mean, then uses fixed-seed renewal-count simulations as finite diagnostics. For \(\alpha=3/2\), \(\tau=d=v=1\), \(\mu=2\), and \(k\approx0.484255687717\), the exact longitudinal prefactors are approximately \(0.0781678570\) (fresh) and \(0.1563357141\) (stationary). The simulation checks are not used to establish the asymptotics; those follow from the renewal-density argument above. The checker and all its dependencies are embedded with this result.

## Relationship to prior work

Baouche, Franosch, Meiners and Kurzthaler (2024) establish the renewal model for active Brownian particles subject to orientational resetting, including a general renewal-convolution representation and the equilibrium-age initialization; their evaluated long-time diffusive moments specialize to exponential reset waiting times. Kumar, Sadekar and Basu (2020) examine Poisson resetting protocols for active Brownian motion. Horii, Lefevere, Itami and Nemoto (2022) study anomalous variance of renewal reward and counting processes, including the marginal infinite-variance threshold; their counting-process methods are an acknowledged ingredient here. The conclusion assessed here is the *combined* longitudinal superdiffusion coefficient, exact stationary-to-fresh factor and transverse contrast for a heading-only reset swimmer under a heavy-tailed clock, not the renewal-count identity in isolation or the general renewal model.

## Limitations

The result assumes a Lomax reset interval law with \(1<\alpha<2\), fixed positive swimming speed and rotational diffusivity, and independent Brownian angular segments. It does not assert the same prefactors for arbitrary regularly varying laws without additional renewal-density conditions, nor a Gaussian limit, nor stationarity of the unconfined position. The transverse bound does not classify its exact diffusion coefficient. General renewal-reward theory and earlier finite-moment orientational-reset results provide substantial related coverage and possible stronger unindexed priority claims. A weak or finite-time simulation alone would not certify these infinite-time asymptotics.

## References

1. Y. Baouche, T. Franosch, M. Meiners and C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769 (first posted 2024-05-10), https://arxiv.org/abs/2405.06769.
2. H. Horii, R. Lefevere, M. Itami and T. Nemoto, *Anomalous fluctuations of renewal-reward processes with heavy-tailed distributions*, arXiv:2203.08584 (first posted 2022-03-16), https://arxiv.org/abs/2203.08584.
3. V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294 (first posted 2020-08-07), https://arxiv.org/abs/2008.03294.
