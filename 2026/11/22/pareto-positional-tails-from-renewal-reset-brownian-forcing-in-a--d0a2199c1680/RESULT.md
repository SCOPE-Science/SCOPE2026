# Pareto positional tails from renewal-reset Brownian forcing in a harmonic trap

## Finding

Resetting **only the random forcing**, without resetting a harmonically confined particle's position, can produce a stationary spatial law with an exact algebraic tail and divergent variance despite strictly positive trap stiffness. A renewal-clock tail exponent determines an exact spatial-tail exponent and amplitude. The same model has a sharp all-clock stationary-variance principle: among clocks with a prescribed mean, deterministic reset intervals uniquely minimize stationary position variance.

Let the physical parameters satisfy \(D,\mu>0\), and let reset intervals \(T\) be strictly positive, identically distributed, independent of the driving Brownian increments, with mean \(m=\mathbb ET\in(0,\infty)\). At each renewal only the Brownian forcing restarts at zero, while the particle position remains continuous. If, for some \(c>0\) and \(\alpha>1\),
\[
\Pr(T>t)\sim c\,t^{-\alpha}\qquad(t\to\infty),
\]
then the continuous-time stationary particle position \(X\) obeys
\[
\boxed{\displaystyle
\Pr(|X|>x)\sim
\frac{c}{m(\alpha-1)}
\left(\frac{4D}{\mu^2}\right)^{\alpha-1}
\frac{\Gamma(\alpha-\tfrac12)}{\sqrt\pi}
\,x^{-2(\alpha-1)}.}
\]
In particular, for every \(p>0\), including the boundary value,
\[
\boxed{\mathbb E|X|^p<\infty\quad\Longleftrightarrow\quad p<2(\alpha-1).}
\]
Consequently the stationary distribution exists for every \(\alpha>1\) but has infinite spatial variance exactly throughout the heavy-tail window \(1<\alpha\le2\).

For **every** positive finite-mean renewal law, not just Pareto-tailed ones, its stationary variance is finite exactly when \(\mathbb E T^2<\infty\), and when finite equals
\[
\boxed{\displaystyle
\operatorname{Var}X=
\frac{D}{\mu^2 m}\left[
\mathbb ET^2-\frac{2m}{\mu}
+\frac{2(1-\mathbb Ee^{-\mu T})}{\mu^2}
\right].}
\]
At fixed \(D,\mu,m>0\), the unique variance-minimizing clock among all positive renewal laws of mean \(m\) is \(T=m\) almost surely. Its exact variance is obtained by substituting that constant into the displayed expression. The variance has no finite upper bound at fixed mean. If \(T_1\) and \(T_2\) have the same mean and \(T_1\preceq_{\mathrm{cx}}T_2\), their stationary spatial variances are ordered in the same direction, strictly when the clock laws differ, allowing infinite values at the upper end.

For the concrete Lomax/Pareto-II clock \(\Pr(T>t)=(1+t/\tau)^{-\alpha}\), \(\tau>0\), the tail coefficient simplifies to
\[
\left(\frac{4D\tau}{\mu^2}\right)^{\alpha-1}
\frac{\Gamma(\alpha-\tfrac12)}{\sqrt\pi}.
\]
These are asymptotic equivalents, not Gaussian or finite-cutoff estimates.

## Assumptions and scope

At each reset epoch the driving noise \(Y\), *not* the particle position, is reset to zero; within each interval it evolves as an independent driftless Brownian motion of covariance \(\mathbb E[B_sB_t]=2D\min(s,t)\). The particle satisfies
\[
\frac{dX_t}{dt}=-\mu X_t+Y_t.
\]
There is no independent thermal noise in \(X\). The renewal clock is independent of all Brownian excursions; the positive intervals are i.i.d. At stationarity, observation is at an ordinary uniformly chosen time, **not** necessarily immediately after a resetting event. Thus the interval containing time zero is length-biased and its age is distributed according to the equilibrium renewal law. The statement applies to the unique stationary augmented process recording position, forcing and renewal age. The spatial marginal exists even where its variance is infinite. The power-tail equivalence requires the stated regularly varying survival with positive asymptotic constant; the variance identity needs no power-tail assumption.

## Proof

**1. Brownian innovation across one complete reset interval.** Let a fresh force excursion be \(B\) and define its contribution to particle position at age \(t\) by
\[
V_t=\int_0^t e^{-\mu(t-s)}B_s\,ds
=\frac1\mu\int_0^t(1-e^{-\mu(t-u)})\,dB_u.
\]
Stochastic Fubini and Itô isometry show that \(V_t\) is centered Gaussian with strictly increasing variance
\[
 h(t)=\frac{2D}{\mu^2}\int_0^t(1-e^{-\mu u})^2\,du
=\frac{D}{\mu^3}\big(2\mu t-3+4e^{-\mu t}-e^{-2\mu t}\big).
\]
Crucially, \(h(t)\sim\kappa t\), where \(\kappa=2D/\mu^2\), while \(0<h(t)\le\kappa t\) for \(t>0\). The factor \(1/\mu\) in the long-age force response must not be omitted.

**2. Stationary reset-epoch law and its moment control.** If \(Q\) denotes position immediately after a force reset, consecutive cycles satisfy the independent affine recursion
\[
Q_{n+1}=e^{-\mu T_n}Q_n+V_{T_n},
\]
with independent fresh clock and Brownian excursion for every cycle. Since \(\mathbb E\log e^{-\mu T}=-\mu m<0\), the backward affine series converges to a unique stationary reset-epoch law. More quantitatively, for any \(q\ge1\) with \(q<2\alpha\), the Gaussian bound \(h(T)\le\kappa T\) gives \(\mathbb E|V_T|^q<\infty\). The perpetuity series, Minkowski's inequality and \(\mathbb Ee^{-q\mu T}<1\) then yield \(\mathbb E|Q|^q<\infty\). For a general clock with merely \(\mathbb ET<\infty\), choosing \(q=1\) gives the stationary construction. For a Pareto exponent \(\alpha>1\), choose
\[
\max\{1,2(\alpha-1)\}<q<2\alpha.
\]
Hence \(\Pr(|Q|>x)=o(x^{-2(\alpha-1)})\). No assumption of finite second moment of the reset interval is hidden in this step.

**3. Equilibrium age and the exact leading spatial tail.** Let \(A\) be the elapsed age in the stationary renewal interval. Renewal reward gives
\[
\Pr(A>a)=\frac1m\int_a^\infty\Pr(T>u)\,du
\sim \frac{c}{m(\alpha-1)}a^{-(\alpha-1)}.
\]
The last equivalence follows directly from integration of the regularly varying survival. The previous-epoch position \(Q\) is independent of the current interval and its Brownian excursion. At a stationary observation time,
\[
 X\ \stackrel{d}{=}\ e^{-\mu A}Q+\sqrt{h(A)}Z,
 \qquad Z\sim N(0,1),
\]
with \(Z,A,Q\) mutually independent. Since \(h\) is increasing and \(h(a)\sim\kappa a\), the positive random variable \(h(A)\) has tail
\[
\Pr(h(A)>z)\sim
\frac{c\kappa^{\alpha-1}}{m(\alpha-1)}z^{-(\alpha-1)}.
\]
Multiplication by the independent \(Z^2\), whose moments of all orders exist, gives by a direct conditioning argument (or the regular-variation product lemma)
\[
\Pr\big(\sqrt{h(A)}|Z|>x\big)\sim
\frac{c\kappa^{\alpha-1}}{m(\alpha-1)}
\mathbb E|Z|^{2(\alpha-1)} x^{-2(\alpha-1)}.
\]
The explicit Gaussian moment is \(\mathbb E|Z|^{2\delta}=2^\delta\Gamma(\delta+\tfrac12)/\sqrt\pi\). Finally, \(|e^{-\mu A}Q|\le|Q|\), and the high moment from Step 2 makes its tail negligible at the claimed scale. Applying the two-sided triangle inequality with any relative tolerance \(\varepsilon>0\), then sending \(\varepsilon\downarrow0\), proves the exact constant for \(X\).

**4. Exact sharp moment cutoff.** For every \(p>0\), the layer-cake identity
\[
\mathbb E|X|^p=p\int_0^\infty x^{p-1}\Pr(|X|>x)\,dx
\]
combined with the positive finite asymptotic constant proves finiteness exactly when \(p<2(\alpha-1)\), including divergence at the boundary. Thus a confining harmonic force cannot make the spatial variance finite for \(1<\alpha\le2\) when only its *driving noise* renews.

**5. Exact stationary variance for arbitrary renewal clocks.** Let \(C_Y(t)=\mathbb E[Y_0Y_t]\) for nonnegative lag \(t\). If there is a renewal between the observations, their force excursions are independent and have zero mean. Otherwise Brownian covariance is \(2D\) times the earlier age. The equilibrium renewal occupation formula gives, whenever \(\mathbb ET^2<\infty\),
\[
C_Y(t)=\frac{D}{m}\mathbb E[(T-t)_+^2],\qquad t\ge0.
\]
The bounded harmonic convolution and Fubini give the exact resolvent identity
\[
\operatorname{Var}X=\frac1\mu\int_0^\infty e^{-\mu t}C_Y(t)\,dt.
\]
Using
\[
\int_0^T e^{-\mu t}(T-t)^2dt=
\frac{T^2}{\mu}-\frac{2T}{\mu^2}
+\frac{2(1-e^{-\mu T})}{\mu^3}
\]
proves the variance formula. When \(\mathbb ET^2=\infty\), equilibrium age has infinite expectation. Since \(h(a)\sim\kappa a\), the independent-current-excursion variance \(\mathbb Eh(A)\) diverges, and the cross term with the previous-epoch position has zero expectation under conditional centering; hence \(\mathbb EX^2=\infty\), without unjustified exchange of infinite covariances.

**6. Sharp fixed-mean design.** Write
\[
g(t)=t^2-\frac{2t}{\mu}+\frac{2(1-e^{-\mu t})}{\mu^2}.
\]
Then \(\operatorname{Var}X=D\mathbb Eg(T)/(\mu^2m)\), with extended-real expectation. Its second derivative \(g''(t)=2(1-e^{-\mu t})>0\) for every \(t>0\). Strict Jensen gives a unique global minimizer \(T=m\); ordinary convex-order monotonicity follows. If the second moment is unbounded, the displayed variance grows without bound at fixed mean, realized as a limit through positive two-point laws with an increasingly remote rare interval. No maximizer with finite variance exists.

## Verification

The accompanying `verification.py` (dependencies in `requirements.txt`) recomputes the Gaussian innovation variance using an independent direct Itô-integral quadrature; compares the closed stationary variance against two independent routes for deterministic, Poisson, Erlang-two and positive two-point renewal intervals; checks convex-order bounds; checks the exact Pareto tail coefficient of the current-cycle Gaussian-age mixture at five increasing thresholds for three different tail exponents; and checks the full renewal-epoch/age variance decomposition for finite-variance Pareto clocks. Execute `python3 verification.py` in the extracted directory. All deterministic consistency assertions must pass. These calculations do not prove any universal claim: the recurrence, renewal-age theorem, regular-variation tail argument, and strict Jensen proof above do that.

## Relationship to prior work

Guéneau, Majumdar and Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453 (first public 2023-06-15), analyze the **same** harmonically filtered Brownian forcing, the reset-epoch affine recursion, and stationary statistics under *periodic* and *Poisson* forcing resets. Those observations, including their Gaussian increment variance and Kesten representation, are known background and are not claimed as new. The mathematical statement assessed here is the **arbitrary heavy-tailed renewal** extension with a sharp continuous-time spatial-tail coefficient and complete moment cutoff, plus the all-renewal-clock stationary variance identity and its strict optimizer. Their periodic/Poisson cases alone have no heavy-clock power-law tail and do not determine the general all-clock result.

Barkai, Flaquer-Galmés and Méndez, arXiv:2306.13621 (2023), study equilibrium renewal ages for **direct position-reset Brownian motion**, not a continuous position driven by a separately reset Brownian force. Direct Brownian reset positions and the exploration phase of a two-stage harmonic-return model can display a formally similar power exponent under Pareto clocks. Such analogies motivate the tail mechanism but do not assert the law of the filtered, position-preserving particle or its exact variance formula. Published mathematical results on *alternating-renewal active propulsion in harmonic traps* give a different Laplace-transform variance envelope; those results concern bounded binary propulsion, not unbounded reset Brownian forcing. Published results on Pareto-driven Brownian exploration with OU first-hit return have two separate on/off phase tails but restart the **particle position itself** at regeneration; they do not cover this force-only renewal process. Publication priority relative to unindexed general renewal-filter theorems remains a risk.

## Limitations

The model is one-dimensional, overdamped and harmonically confined, with independent driftless Brownian forcing excursions, i.i.d. positive renewal intervals, and **forcing-only** resets. The spatial marginal alone is generally not Markov. The exact power-law coefficient needs a genuinely regularly varying interval survival with nonzero asymptotic constant; it is not claimed for arbitrary oscillatory long tails. The variance identity is an extended-real statement, with a finite formula only for finite second waiting-time moment. The all-clock minimizer assumes a fixed mean interval, fixed \(D\), and fixed \(\mu\). No rates of convergence in the extreme-tail equivalent, experimental finite-sample estimator, multi-particle interaction result, or arbitrary nonlinear-trap extension is claimed. Originality is subject to independent publication-priority review.

## References

1. M. Guéneau, S. N. Majumdar, G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453, first public 2023-06-15, https://arxiv.org/abs/2306.09453.
2. E. Barkai, L. Flaquer-Galmés, V. Méndez, *Ergodic properties of Brownian motion under stochastic resetting*, arXiv:2306.13621, 2023, https://arxiv.org/abs/2306.13621.
3. A. Nagar, S. Gupta, *Diffusion with stochastic resetting at power-law times*, arXiv:1512.02092 (2015), https://arxiv.org/abs/1512.02092.
4. *Sharp dwell-time noise bounds and trap-spectroscopic recovery for alternating-renewal propulsion*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-dwell-time-noise-bounds-and-trap-spectroscopic-recovery-fo--3baa3630f98c.
5. *Two exact spatial tail exponents for Pareto-driven harmonic first-hit returns*, published mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-two-exact-spatial-tail-exponents-for-pareto-driven-harmonic-firs--909fa6bb7163.
