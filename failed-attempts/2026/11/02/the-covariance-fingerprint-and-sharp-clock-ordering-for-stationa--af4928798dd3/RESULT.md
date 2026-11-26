# The covariance fingerprint and sharp clock ordering for stationary renewal-reset Brownian motion

## Finding

Let a one-dimensional Brownian particle be instantaneously reset to the origin at renewal times. For *equilibrium-stationary* resetting, the temporal covariance encodes the entire inter-reset waiting-time law, even when the Brownian diffusivity is initially unknown. Also, at any fixed mean reset interval, deterministic resetting with the appropriate *stationary random phase* uniquely minimizes the variance of the finite-window time-averaged signed position, simultaneously for every observation window.

Precisely, for every lag \(h\ge0\),
\[
C(h)=\mathbb E[X_0X_h]=\frac{D}{m}\mathbb E[(L-h)_+^2],\qquad m=\mathbb E L.
\]

With derivatives taken from the right at possible atoms of the waiting-time law, this implies
\[
D=-\frac{C'_+(0)}2,\qquad m=-\frac{C'_+(0)}{C''_+(0)},\qquad
\mathbb P(L>h)=\frac{C''_+(h)}{C''_+(0)}\quad(h\ge0).
\]

For the stationary-window average \(\overline X_T=T^{-1}\int_0^T X_t\,dt\), let \(V_T=\operatorname{Var}(\overline X_T)\). Then
\[
V_T=\frac{2D}{mT^2}\mathbb E[\Phi_T(L)],\qquad
\Phi_T(\ell)=\begin{cases}
T\ell^3/3-\ell^4/12,&0\le\ell\le T,\\
T^2\ell^2/2-T^3\ell/3+T^4/12,&\ell\ge T.
\end{cases}
\]
For every \(T>0\) the unique minimizer over all waiting-time laws of fixed positive mean \(m\) is \(L=m\) almost surely. Its sharp variance is
\[
V_T^{\mathrm{det}}=\begin{cases}
\dfrac{D}{m}\bigl(m^2-2mT/3+T^2/6\bigr),&0<T\le m,\\[2mm]
\dfrac{2Dm^2}{3T}-\dfrac{Dm^3}{6T^2},&T\ge m.
\end{cases}
\]
For comparison, exponentially distributed reset intervals of the same mean have \(V_T^{\mathrm{Pois}}=4Dm^2(T-m+me^{-T/m})/T^2\); the long-window variance ratio \(V_T^{\mathrm{Pois}}/V_T^{\mathrm{det}}\) tends to \(6\).

The same covariance gives the exact nonzero-frequency power spectral density, with the two-sided Fourier convention,
\[
S(\omega)=2\int_0^\infty C(h)\cos(\omega h)\,dh
=\frac{4D}{\omega^2}\left(1-\frac{\mathbb E\sin(\omega L)}{m\omega}\right),\qquad \omega\ne0.
\]
The cosine integral is interpreted as its convergent improper integral, and the zero-frequency value can be infinite.

The long-window variance identifies a sharp extra moment requirement:
\[
\lim_{T\to\infty}T V_T=\frac{2D}{3m}\mathbb E[L^3]\in(0,\infty],
\]
where the limit is infinite if the third moment diverges. If \(\mathbb P(L>t)\sim c t^{-\beta}\) with \(c>0\), \(\beta>2\), then
\[
V_T\sim\begin{cases}
\dfrac{4Dc}{m(\beta-1)(\beta-2)(3-\beta)(4-\beta)}T^{2-\beta},&2<\beta<3,\\[2mm]
\dfrac{2Dc}{m}\dfrac{\log T}{T},&\beta=3,\\[2mm]
\dfrac{2D\mathbb E[L^3]}{3mT},&\beta>3.
\end{cases}
\]
Thus a finite stationary position variance needs a second reset-clock moment, whereas the ordinary inverse-window asymptotic variance needs the third.

## Assumptions and scope

Fix \(D>0\), an iid strictly positive renewal period \(L\) with \(m=\mathbb EL\in(0,\infty)\), and \(\mathbb E L^2<\infty\). Reset times form the *stationary* renewal process on the real line. The interval enclosing time zero has the length-biased distribution \(\ell\mathbb P(L\in d\ell)/m\), and, conditional on its length, time zero is uniformly located inside it. The process has position zero at each reset and on every interval is an independent Brownian path whose variance increment is \(2D\,dt\). Hence \(\mathbb E X_t=0\) and \(\mathbb E X_t^2=D\mathbb E L^2/m<\infty\). A deterministic clock has a **uniform phase**; observing exactly at every reset is a different, nonstationary initialization. No density or nonlattice assumption is imposed on \(L\).

The recovery identities concern the *exact* continuous-lag covariance; they do not assert statistical consistency or stability for noisy, discretely sampled observations. The optimization is at fixed mean period and fixed diffusivity, for the variance of the **signed time average**. The heavy-tail classification adds the stated regular-variation assumption.

## Proof

**(1) Stationary covariance.** Let \(A\) and \(R\) be the age and forward residual at zero. Conditional on the enclosing interval having length \(\ell\), \(A\) is uniform on \([0,\ell]\) and \(R=\ell-A\). If no reset occurs in \((0,h]\), the two positions share the same Brownian increments over the past \(A\) time units, so the conditional product expectation is \(2DA\). If a reset intervenes, the post-reset Brownian path is independent of the past and has mean zero, hence the conditional product expectation is zero. Integrating over the size-biased equilibrium interval,
\[
C(h)=\frac{2D}{m}\mathbb E\left[\int_0^L a\,\mathbf1_{\{a+h<L\}}\,da\right]
=\frac{D}{m}\mathbb E[(L-h)_+^2].
\]
All expectations are finite by the second-moment hypothesis. The law at equality \(R=h\) causes no ambiguity because the Brownian position at a resetting instant is zero.

**(2) Inversion including atomic reset laws.** Dominated one-sided differentiation of the squared positive part gives
\[
C'(h)=-\frac{2D}{m}\mathbb E[(L-h)_+],\qquad
C''_+(h)=\frac{2D}{m}\mathbb P(L>h).
\]
The first derivative is continuous; the second is interpreted as the right derivative of \(C'\), not necessarily an everywhere classical continuous second derivative. Strict positivity of \(L\) gives \(C'_+(0)=-2D\), \(C''_+(0)=2D/m\). Therefore the displayed reconstruction recovers \(D\), \(m\) and the entire right-continuous tail, including its jumps at atoms. In particular two distinct period laws cannot share the same covariance when diffusivity is allowed to vary.

**(3) Finite-window variance and strict optimization.** The covariance is stationary and even, so Fubini's theorem gives
\[
V_T=\frac{2}{T^2}\int_0^T(T-h)C(h)\,dh
=\frac{2D}{mT^2}\mathbb E\left[\int_0^T(T-h)(L-h)_+^2\,dh\right].
\]
The inner integral is the displayed piecewise polynomial \(\Phi_T\). On \(0<\ell<T\) its second derivative is \(\ell(2T-\ell)>0\), while on \(\ell>T\) it is \(T^2>0\), with matching first derivative at \(\ell=T\). Thus \(\Phi_T\) is strictly convex on \((0,\infty)\). Jensen's strict inequality gives \(\mathbb E\Phi_T(L)\ge\Phi_T(m)\), with equality *only* if \(L=m\) almost surely. Substitution yields the sharp piecewise formulas. Evaluating the same covariance for an exponential period of mean \(m\) gives \(C(h)=2Dm e^{-h/m}\) and the Poisson comparison. This all-horizon optimization is stronger than minimizing only stationary spatial variance \(C(0)\).

**(4) Spectrum.** The established derivatives satisfy \(C(\infty)=C'(\infty)=0\), \(C''_+\ge0\), and \(\int_0^\infty C''_+(h)\,dh=2D/m\,\mathbb EL=2D\). Twice integrating the convergent cosine transform by parts gives
\[
S(\omega)=\frac{4D}{\omega^2}-\frac{2}{\omega^2}\int_0^\infty C''_+(h)\cos(\omega h)\,dh
=\frac{4D}{\omega^2}\left(1-\frac{\mathbb E\sin(\omega L)}{m\omega}\right).
\]
The right-side expression is nonnegative because \(\sin z\le z\) for positive \(z\); its possible zeros and oscillations are compatible with periodic-clock spectra. For clocks with finite third moment, the limit at zero is \(2D\mathbb E L^3/(3m)\).

**(5) Third-moment threshold and heavy-tail regimes.** Integrating the nonnegative covariance and using Tonelli gives \(2\int_0^\infty C(h)\,dh=(2D/3m)\mathbb E L^3\), possibly infinite. Since \(TV_T=2\int_0^T(1-h/T)C(h)\,dh\), monotone convergence for each fixed \(h\) gives the asserted extended limit. If \(\mathbb P(L>t)\sim ct^{-\beta}\) and \(\beta>2\), then
\[
\mathbb E[(L-h)_+^2]=2\int_h^\infty (z-h)\mathbb P(L>z)\,dz
\sim \frac{2c}{(\beta-1)(\beta-2)}h^{2-\beta}.
\]
For \(2<\beta<3\), integrate the regularly varying covariance against the triangular averaging kernel using \(\int_0^1(1-z)z^{2-\beta}\,dz=[(3-\beta)(4-\beta)]^{-1}\). At \(\beta=3\), the covariance has tail \(Dc/(mh)\), giving the stated logarithm. Above \(\beta=3\), the third moment is finite and the preceding integrated-covariance identity yields the inverse-time constant. These cases exhaust the specified exponent range. 

## Verification

The self-contained script `verify_covariance.py` checks the exponential and fixed-length cases by independently integrating covariance and reset lengths; it cross-checks two-point renewal mixtures using a separate size-biased age calculation; verifies Lomax-period covariance and averaging formulas for tail exponents below, at and above three; checks inversion, convex-clock comparisons, and independently integrates both Poisson and periodic-clock spectra. Running `python verify_covariance.py` completed 143 numerical/algebraic comparisons. The proof does **not** rely on numerical extrapolation to infinite time or a simulated sample-path approximation. General-law validity follows from the analytical argument above.

## Relationship to prior work

The renewal framework and stationary spatial propagator for general reset-time distributions are established in Singh, Górska and Sandev (arXiv:2203.04046) and Masó-Puigdellosas, Campos and Méndez (arXiv:2205.01613). Flaquer-Galmés, Méndez and Campos (arXiv:2306.13621) analyze spatial stationary laws and explicitly find the sharp deterministic clock extremizes a **one-time stationary mean-square displacement**, which is therefore *not* claimed as new here. Majumdar and Oshanin (arXiv:1806.03435) derive covariance and spectral formulas for **constant-rate Poisson resetting**, providing a special case of our expression. The more recent non-Poisson joint-particle study arXiv:2509.06658 concerns correlations between distinct simultaneously resetting particles at a fixed age, rather than the present single-particle two-time covariance. The evaluated combination here is the non-Poisson stationary two-time formula, exact inverse clock identification including unknown diffusivity and atoms, the unique **all-horizon signed-time-average variance** optimizer, and the third-moment boundary. Generic renewal reward theory and covariance inverse problems may imply special parts; priority has not been independently certified.

## Limitations

The result is for complete instantaneous returns to the origin, independent Brownian excursions and a correctly equilibrium-initialized renewal clock, with a finite second interarrival moment. General initial conditions need not have the same two-time covariance. The inverse map may be ill-conditioned when estimated from finite noisy data, and no such statistical rate is proved. The strictly optimal variance concerns signed-position time averages, not occupation fractions, hitting times, or all possible observables. The power-law asymptotics require the stated regularly varying tail. This is an analytical result with self-review; independent scientific auditing and definitive novelty assessment have not been performed.

## References

1. R. K. Singh, K. Górska and T. Sandev, *General approach to stochastic resetting*, arXiv:2203.04046 (first version, 8 March 2022), especially general-renewal and spatial-MSD analysis.
2. A. Masó-Puigdellosas, D. Campos and V. Méndez, *Conditioned backward and forward times of diffusion with stochastic resetting: a renewal theory approach*, arXiv:2205.01613 (2022), Sections II–IV.
3. R. Flaquer-Galmés, V. Méndez and D. Campos, *Ergodic properties of Brownian motion under stochastic resetting*, arXiv:2306.13621 (2023), stationary spatial moment and sharp-clock results.
4. S. N. Majumdar and G. Oshanin, *Spectral content of fractional Brownian motion with stochastic reset*, arXiv:1806.03435 (2018), Sections II–III (Poisson-specific covariance/PSD).
5. Non-Poisson simultaneous-reset Brownian particle study, arXiv:2509.06658 (2025), introduction and two-particle spatial-correlation analysis (distinct observable).
