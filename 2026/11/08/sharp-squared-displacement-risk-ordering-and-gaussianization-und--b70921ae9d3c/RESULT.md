# Sharp squared-displacement risk ordering and Gaussianization under multiplicative Brownian resetting

## Finding

**Theorem (variance-matched stationary excursion risk).** Let \(D>0\), \(r>0\), and \(-1<a<1\). Between independent rate-\(r\) Poisson events, \(X\) is Brownian motion with generator \(D\partial_{xx}\); each event replaces its pre-event position by \(aX\). Write \(X_a\) for its unique stationary position, \(q=a^2\), and
\[
Y_q=\frac{X_a}{\sqrt{\operatorname{Var}(X_a)}},
\qquad \operatorname{Var}(X_a)=\frac{2D}{r(1-q)}.
\]
The law of \(Y_q\) depends only on \(q\), not on \(D,r\) or the sign of \(a\). If \(0\le q_1<q_2<1\), then
\[
\boxed{Y_{q_2}^{\,2}\ \le_{\mathrm{cx}}\ Y_{q_1}^{\,2}},
\]
where \(U\le_{\mathrm{cx}}V\) means \(\mathbb E\Psi(U)\le\mathbb E\Psi(V)\) for every convex \(\Psi:[0,\infty)\to\mathbb R\) for which both expectations exist. All these squared variables have mean one; the ordering is nontrivial because
\[
\mathbb E[Y_q^4]=\frac{6}{1+q}.
\]

In particular, let \(R_q(t)=\mathbb E[(Y_q^2-t)_+]\), \(t\ge0\), and let \(\phi(z)=(2\pi)^{-1/2}e^{-z^2/2}\) and \(\overline\Phi(z)=\int_z^\infty\phi(u)\,du\). The entire excess-quadratic-excursion curve decreases in \(q\) and has the **sharp simultaneous bounds**
\[
\boxed{
2\big[\sqrt t\,\phi(\sqrt t)+(1-t)\overline\Phi(\sqrt t)\big]
\ \le R_q(t)\ \le
(1+\sqrt{2t})e^{-\sqrt{2t}}
}.
\]
The upper profile is attained when \(q=0\); the lower profile is approached as \(q\uparrow1\), but is not attained for any \(q<1\). For each \(t>0\) and \(0<q<1\), both inequalities are strict.

More precisely, as \(q\uparrow1\), for every compact \(K\subset(0,\infty)\), uniformly in \(t\in K\),
\[
\boxed{
R_q(t)=R_{\mathrm G}(t)
+\frac{1-q}{2(1+q)}\,t^{3/2}\phi(\sqrt t)
+O_K\big((1-q)^{3/2}\big),
}
\]
where \(R_{\mathrm G}(t)=2[\sqrt t\,\phi(\sqrt t)+(1-t)\overline\Phi(\sqrt t)]\). Thus the Gaussian-endpoint correction has an explicit strictly positive coefficient. The same comparison applies at fixed physical variance \(\sigma^2>0\) by choosing \(r=2D/[\sigma^2(1-q)]\) at each \(q\).

## Assumptions and scope

The stochastic dynamics is defined on the whole real line with no absorbing target, independent Brownian increments and independent Poisson reset times. Stationarity is sampled at an arbitrary time, not only just after a reset. The contraction \(a\) is deterministic and satisfies \(|a|<1\). Brownian diffusivity and reset rate are strictly positive. All loss comparisons refer to the **squared stationary displacement divided by its own variance**; they do not assert first-order stochastic dominance of squared displacements or of their unnormalized laws. The upper endpoint \(a=0\) is admissible; the lower Gaussian endpoint is a limit of admissible protocols, not a stationary law at \(|a|=1\). The rate asymptotic is uniform on compact subsets of positive thresholds and does not claim a uniform expansion for thresholds diverging with \(q\).

## Proof

**1. Stationary representation.** The stationary characteristic function \(\varphi\) satisfies the exact generator equation
\[
(r+Dk^2)\varphi(k)=r\varphi(ak).
\]
Repeated substitution and \(|a|<1\) give uniquely
\[
\varphi(k)=\prod_{j=0}^\infty
\left(1+\frac{D}{r}q^j k^2\right)^{-1}.
\]
The product converges locally uniformly. This is the characteristic function of \(\sum_{j\ge0}a^jL_j\), where independent \(L_j\) have centered Laplace law of variance \(2D/r\). The series converges in \(L^2\). Coupling two solutions with the same Brownian and Poisson noise yields a difference multiplied by \(a\) at each reset, so the invariant law is unique and attractive. Reflection signs of \(a\) disappear because each \(L_j\) is symmetric.

Let \(E_j\) be independent unit-mean exponential variables and \(Z_j\) independent standard normals, with the two collections independent. Since \(L_j\overset d=\sqrt{2D/r}\sqrt{E_j}Z_j\), the series, conditional on all \(E_j\), is centered Gaussian. Introducing an independent standard normal \(Z\), this proves the distributional identity
\[
Y_q\overset d=\sqrt{V_q}\,Z,
\qquad
V_q=(1-q)\sum_{j=0}^\infty q^jE_j.
\]
Here \(\mathbb EV_q=1\) and \(\operatorname{Var}(V_q)=(1-q)/(1+q)\). Consequently \(\mathbb E Y_q^4=3\mathbb EV_q^2=6/(1+q)\).

**2. Countable majorization.** For \(0\le q<1\), let \(w_j(q)=(1-q)q^j\). These weights decrease, sum to one, and have prefix mass \(\sum_{j=0}^{m-1}w_j(q)=1-q^m\), strictly decreasing with \(q\) for every positive integer \(m\). The precise countable version needed here follows by finite truncation: for each sufficiently large integer \(n\), replace the tail mass \(q^n\) by \(n\) equal coefficients \(q^n/n\). The resulting vector of \(2n\) weights is decreasing if \(n\ge q/(1-q)\), and its first \(k\) partial sums are \(1-q^k\) for \(k\le n\), and \(1-(1-(k-n)/n)q^n\) for \(n<k\le2n\). Therefore the vector for \(q_1<q_2\) majorizes the vector for \(q_2\).

For any convex \(F\), the finite-weight function
\[
(u_1,\ldots,u_{2n})\longmapsto
\mathbb EF\!\left(\sum_{j=1}^{2n}u_jE_j\right)
\]
is convex and permutation-symmetric, hence Schur-convex. Applying finite majorization gives the desired expectation inequality for the truncated sums. Both truncated sums differ in \(L^1\) from their infinite series by at most \(2q^n\), so the inequality passes to the limit for convex Lipschitz functions; lower supporting affine functions and monotone piecewise-linear approximations extend it to all convex functions with defined expectations. Thus \(V_{q_2}\le_{\mathrm{cx}}V_{q_1}\). Conditional on the independent \(Z^2\), multiplication by its nonnegative value preserves convexity in \(V\); integrating establishes \(Y_{q_2}^2\le_{\mathrm{cx}}Y_{q_1}^2\).

**3. Sharp endpoint profiles and strictness.** For \(q=0\), \(V_0\) is exponential and \(Y_0\) is a centered unit-variance Laplace random variable. Its squared exceedance probability is \(\Pr(Y_0^2>s)=e^{-\sqrt{2s}}\); integration over \(s\ge t\) gives \(R_0(t)=(1+\sqrt{2t})e^{-\sqrt{2t}}\). As \(q\uparrow1\), \(\mathbb E(V_q-1)^2=(1-q)/(1+q)\to0\). Using the same \(Z\) for all \(q\), \(V_qZ^2\to Z^2\) in \(L^1\), hence \(R_q(t)\to\mathbb E[(Z^2-t)_+]\); normal integration gives the displayed Gaussian formula. Monotonicity in Step 2 supplies both simultaneous sharp bounds.

For \(t>0\), Jensen's inequality conditional on \(Z^2>0\) is strict on the lower side: \(V_q\) has a continuous law with full support on \((0,\infty)\), so \((vZ^2-t)_+\) changes slope across values receiving positive probability. For \(q>0\), Jensen applied to the genuine convex combination \(V_q=\sum_jw_j(q)E_j\) is strict on the upper side for the same reason (the independent exponentials have positive probabilities on both sides of every positive threshold). Equality at \(t=0\) holds since all the squared variables have mean one.

**4. First Gaussianization correction.** Define \(g_t(v)=\mathbb E[(vZ^2-t)_+]\) for \(v>0\). Direct differentiation of the normal tail integral gives
\[
g_t''(v)=\frac{(t/v)^{3/2}\phi(\sqrt{t/v})}{v},
\quad
g_t'''(v)=\frac{(t/v)^{3/2}\phi(\sqrt{t/v})}{2v^2}\left(\frac tv-5\right).
\]
For \(t\) in any fixed compact subset of \((0,\infty)\), the third derivative is bounded uniformly over \(v>0\). Taylor expansion at \(v=1\), expectation, and \(\mathbb E(V_q-1)=0\) therefore give
\[
R_q(t)=g_t(1)+\frac12g_t''(1)\operatorname{Var}(V_q)
+O_K(\mathbb E|V_q-1|^3).
\]
Independence of exponentials gives the exact fourth central moment
\[
\mathbb E(V_q-1)^4=
\frac{6(1-q)^4}{1-q^4}
+3\left(\frac{1-q}{1+q}\right)^2
=O((1-q)^2).
\]
By Hölder, \(\mathbb E|V_q-1|^3=O((1-q)^{3/2})\). Since \(g_t''(1)=t^{3/2}\phi(\sqrt t)\), substitution proves the stated uniform expansion.

## Verification

The included `checker.py` independently checks finite majorization prefix inequalities, mixture-variance and fourth-moment identities, the two exact endpoint stop-loss formulas, and conditional Gaussian integration. It also performs seeded exponential-mixture diagnostic integration at four rescaling strengths and two excursion thresholds. Running `python3 checker.py` produced **205 passing deterministic assertions**. Finite computations are diagnostics; the universal order and asymptotic rate follow from the proof above.

For orientation, at threshold \(t=4\) the exact Gaussian and Laplace endpoint excess losses are respectively \(0.07946307436\ldots\) and \(0.22628204337\ldots\). They compare expected **excess squared displacement**, not the raw probability of exceeding the threshold.

## Relationship to prior work

Biroli, Feld, Hartmann, Majumdar and Schehr [1] establish the stationary distribution of Brownian motion under deterministic position rescaling, and analyze mean first-passage times. Their stationary law is a premise here, not claimed as new. Kolb and Wübker [2] give an independent stationary Laplace-series representation and study convergence rates and positive conditioning; the square-risk order is not among their stated results. The Schur-convex majorization principle used in Step 2 is classical; compare Proschan's related peakedness result [3]. That weighted-average principle alone does not contain the physical fixed-variance comparison, its explicit sharp Gaussian/Laplace excess-loss envelopes, or the quantitative correction coefficient. Pierce [4] independently establishes the earlier stationary Fourier product and the limiting Gaussian/Laplace crossover. The present result is the combined model-specific risk ordering and its sharp endpoint approach, not a claim of inventing majorization or the stationary law.

## Limitations

The result concerns stationary single-time **squared** displacements and convex excess-energy losses, not pointwise tail ordering, unnormalized spatial tails, first-passage times, multi-time fluctuations, or general random rescaling factors. No claim of a new general majorization theorem is made. The correction is only for fixed positive thresholds (uniform over positive compact sets), not moving rare-event thresholds. The mathematical derivation and available literature comparisons have not undergone independent validation; general stochastic-order results outside the inspected primary sources could contain a stronger formulation.

## References

[1] M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (first posted 2024-06-12), https://arxiv.org/html/2406.08387v1.

[2] M. Kolb and A. Wübker, *Brownian Motion With Partial Resetting Conditioned to Stay Positive*, *Bulletin of the London Mathematical Society* (2026), https://doi.org/10.1112/blms.70314.

[3] F. Proschan, *Peakedness of Distributions of Convex Combinations*, *Annals of Mathematical Statistics* **36** (1965), 1703–1706, https://doi.org/10.1214/aoms/1177699798. This is cited for the established majorization/peakedness tradition, not for a claim about the specific stationary model.

[4] J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215v1 (first posted 2022-04-14), https://arxiv.org/html/2204.07215v1.
