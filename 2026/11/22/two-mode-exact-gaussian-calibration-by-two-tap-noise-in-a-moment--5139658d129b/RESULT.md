# Two-mode exact Gaussian calibration by two-tap noise in a momentum recurrence

## Finding

Consider an unadjusted stochastic two-step gradient-extrapolation recurrence on a positive-definite quadratic potential. With a single fresh Gaussian vector per update, and a shared linear combination of its current and previous innovations, **the entire Gaussian target law can be reproduced exactly for every target with at most two distinct curvature eigenvalues**. For any fixed positive momentum and any three distinct curvatures in the stable domain, no common pair of real noise taps can achieve exact Gaussian-target covariance. When two curvatures are calibrated, the normalized stationary variance is strictly *below* its target at every strictly intermediate curvature and strictly *above* it at exterior curvatures in the stable domain.

The precise parameters, including existence and nonuniqueness of the two individual noise taps, are given below. This is a statement about **stationary position laws**, not exact time-lag statistics or a general nonlinear-target sampler.

## Assumptions and scope

Let \(d\ge 1\), \(H\in\mathbb R^{d\times d}\) be real symmetric positive definite, \(\alpha>0\), \(0<\eta<1\), and \(\sigma>0\), with all eigenvalues \(\lambda\) of \(H\) satisfying \(0<\alpha\lambda<1\). Write \(T=I-\alpha H\). For fixed real \(c_0,c_1\), let \((\xi_n)\) be independent \(N(0,I_d)\) vectors and consider

\[
X_{n+1}=(1+\eta)TX_n-\eta TX_{n-1}+\sigma(c_0\xi_{n+1}+c_1\xi_n).
\]

The corresponding target is the centered Gaussian \(N(0,H^{-1})\). No Metropolis correction is applied. All calculations are in exact arithmetic. An arbitrary deterministic initial condition is admissible (with the Gaussian innovations generated independently); geometric stability gives the same limiting position distribution.

For any eigenvalue \(\lambda\), put \(t=1-\alpha\lambda\in(0,1)\), and define

\[
D_\eta(t)=(1-\eta t)(1+(1+2\eta)t),\qquad q=\eta(1+2\eta)>0.
\]

For nontrivial taps define the two noise invariants

\[
A=c_0^2+c_1^2,\qquad B=\eta A+2(1+\eta)c_0c_1.
\]

**Stationary variance identity.** Every eigenmode has a unique centered stationary Gaussian law, with stationary variance \(v(\lambda)\) satisfying

\[
\boxed{\lambda v(\lambda)=\frac{\sigma^2}{\alpha}\frac{A+Bt}{D_\eta(t)}.}
\]

**Complete two-curvature calibration.** Fix any \(0<t_-<t_+<1\) and let

\[
K=1+q t_-t_+,\qquad G=1+\eta-q(t_-+t_+).
\]

Exactly calibrating the target variances at both \(t_-\) and \(t_+\) determines the two invariants uniquely:

\[
\boxed{A=\frac{\alpha K}{\sigma^2},\qquad B=\frac{\alpha G}{\sigma^2}.}
\]

Such invariants are achievable by real \(c_0,c_1\), for every allowed \(\eta,t_-,t_+\). The *ordered* tap pair is not unique, because sign and interchange can preserve both invariants. A concrete construction is given in the proof.

For this calibration, at **every** \(t\in(0,1)\),

\[
\boxed{\lambda v(\lambda)-1=\frac{q(t-t_-)(t-t_+)}{D_\eta(t)}.}
\]

Thus every mode strictly between the two calibrated values is underdispersed; every other uncalibrated mode in the stable interval is overdispersed. In particular, the midpoint deficit is exactly

\[
\lambda_{\mathrm{mid}}v(\lambda_{\mathrm{mid}})-1
=-\frac{q(t_+-t_-)^2}{4D_\eta((t_-+t_+)/2)}.
\]

For \(\eta>0\), no common two-tap choice can have \(\lambda v(\lambda)=1\) at three distinct curvatures in the assumed interval. At the different boundary \(\eta=0\), the familiar equal-tap noise choice \(c_0=c_1=\sqrt{\alpha/(2\sigma^2)}\) gives exactly the target stationary covariance at *all* curvatures with \(0<\alpha\lambda<1\). The latter zero-momentum phenomenon is established background, not an originality claim.

## Proof

**1. Mode stability and stationary law.** Diagonalize \(H\) orthogonally. Each scalar mode obeys

\[
x_{n+1}=a x_n-b x_{n-1}+\sigma(c_0\zeta_{n+1}+c_1\zeta_n),\qquad
 a=(1+\eta)t,\quad b=\eta t.
\]

The homogeneous characteristic polynomial is \(z^2-az+b\). Its Jury inequalities are

\[
1-b>0,\qquad 1-a+b=1-t>0,\qquad 1+a+b=1+(1+2\eta)t>0.
\]

Therefore both roots are strictly inside the unit circle. Adding \(\zeta_n\) to the state makes a stable three-dimensional affine Gaussian Markov chain with a unique stationary law. The stationary position marginal is Gaussian and initial-condition-independent. Orthogonal modal innovations are independent, so the full limiting position covariance is diagonal in an eigenbasis of \(H\).

**2. Exact variance with colored noise.** Write \(v=\mathbb E[x_n^2]\), \(r=\mathbb E[x_nx_{n-1}]\) at stationarity. Since \(\zeta_n\) is independent of all previous innovations, \(\mathbb E[x_n\zeta_n]=\sigma c_0\). The stationary covariance identities read

\[
(1+b)r=av+\sigma^2c_0c_1,
\]
\[
(1-a^2-b^2)v+2ab r=\sigma^2(c_0^2+c_1^2+2ac_0c_1).
\]

Eliminating \(r\) gives

\[
v=\frac{\sigma^2\big((1+b)(c_0^2+c_1^2)+2a c_0c_1\big)}{(1-b)((1+b)^2-a^2)}.
\]

Now \((1+b)^2-a^2=(1-t)(1+(1+2\eta)t)\) and \(\alpha\lambda=1-t\). Substituting the definitions of \(A,B,D_\eta\) proves the displayed normalized stationary variance identity. No numerical limiting argument is needed.

**3. Necessary and sufficient parameters for two modes.** Exact target variance for a mode \(t\) is equivalent to

\[
\frac{\sigma^2}{\alpha}(A+Bt)=D_\eta(t)=1+(1+\eta)t-qt^2.
\]

The unique affine interpolant to the right side at \(t_-\) and \(t_+\) is \(K+Gt\) with the stated coefficients; this gives the unique \(A,B\). To see that actual real taps realize the resulting invariants, observe that real numbers \(c_0,c_1\) with \(c_0^2+c_1^2=A>0\) have a prescribed product precisely when \(|c_0c_1|\le A/2\). In terms of \(G/K=B/A\), this is

\[
-1\le\frac{G}{K}\le 1+2\eta.
\]

Both inequalities are strictly satisfied here, since

\[
K+G=2+\eta-q(t_-+t_+-t_-t_+)>2(1-\eta^2)>0
\]

and

\[
(1+2\eta)K-G=\eta(1+(1+2\eta)t_-)(1+(1+2\eta)t_+)>0.
\]

For an explicit pair set \(P=(B-\eta A)/(2(1+\eta))\), \(u=\sqrt{A+2P}\), and \(w=\sqrt{A-2P}\), and choose \(c_0=(u+w)/2\), \(c_1=(u-w)/2\). Then \(c_0^2+c_1^2=A\) and \(c_0c_1=P\). The limiting joint Gaussian distribution therefore has exactly the target position law when the spectrum consists of the two calibrated values (with arbitrary multiplicities).

**4. Error sign and sharp impossibility.** The difference between the interpolation line and the quadratic denominator factors exactly:

\[
(K+Gt)-D_\eta(t)=q(t-t_-)(t-t_+).
\]

Since \(D_\eta(t)>0\) on \((0,1)\), division gives the sharp signed error and midpoint formula. If the target covariance were exact at three distinct \(t\) values, the nonzero quadratic \(D_\eta(t)-(\sigma^2/\alpha)(A+Bt)\) would have three distinct zeros. Its quadratic coefficient is \(-q\ne0\), a contradiction. This proves the three-curvature obstruction for every real tap choice, including choices other than the two-curvature interpolant.

At \(\eta=0\), \(D_0(t)=1+t\), and \(c_0=c_1=\sqrt{\alpha/(2\sigma^2)}\) makes \((\sigma^2/\alpha)(A+Bt)=1+t\) identically. This verifies, but does not newly establish, the known zero-momentum boundary.

## Verification

The standalone dependency-free `verify.py` checks the variance identity against an **independently assembled exact-rational 3-by-3 stationary Lyapunov equation** for varied parameters, verifies the interpolation, positivity and signed remainder identities, and checks one explicit three-mode contrast. Run `python verify.py` with Python 3. The program reports its number of passed exact-rational checks; a finite check complements rather than proves the arbitrary-dimensional statements.

As a reproducible illustrative choice, set \(\eta=1/2\), \(\alpha=1/2\), \(\sigma^2=2\), \(t_-=1/4\), and \(t_+=2/3\). Invariants \(K=7/6\), \(G=7/12\) permit \(c_0^2=7/24\) and \(c_1=0\). The two endpoint modes have the exact target law, but the intermediate mode \(t=11/24\) has normalized position variance \(826/851\), an exact relative deficit of \(25/851\). Thus tuning both endpoint modes does not remove the interior error.

## Relationship to prior work

Schuh (2026) studies kinetic Langevin samplers that exploit the **exact harmonic evolution** in a splitting method and derives contraction and invariant-measure error bounds. That approach uses a different state update and full harmonic integration; it does not present the two-tap/noise-only calibration classification for the explicit gradient-extrapolation recurrence defined above. Its concern with harmonic accuracy and cost motivates the separate noise-design question addressed here.

Leimkuhler and Matthews (2012) introduced an earlier colored-noise Brownian sampling modification. The \(\eta=0\), equal-tap exact Gaussian stationary covariance is a known consequence of that construction, and is **explicitly excluded from the claimed contribution**. This finding instead fixes nonzero momentum and classifies common-noise two-mode attainability and its signed bias between calibrated modes.

General autoregressive/moving-average covariance identities underlie the proof. Their use and the existence of exact Gaussian harmonic integrators are not asserted to be new. The new claim is the sharp feasible two-curvature interpolant, strict intermodal sign law, and universal three-curvature obstruction under this particular common two-tap, one-fresh-innovation recurrence.

## Limitations

Only constant-coefficient positive-definite quadratics with \(0<\alpha\lambda<1\) are considered, with fixed positive momentum and independent standard Gaussian innovations. The theorem concerns stationary **position** covariance/Gaussian position law; joint velocity/position laws, temporal autocorrelations, nonlinear potentials, state-dependent taps, extra independent noises, and mode-specific noise filters are not classified. A method using full matrix-valued noise parameters or exact harmonic integration need not obey the three-curvature obstruction. The zero-momentum equality is prior art. The originality comparison is best-knowledge only; previously unindexed equivalent ARMA parameter-design results remain possible. No independent mathematical audit has been performed.

## References

1. K. Schuh, *Convergence and non-asymptotic error analysis for kinetic Langevin samplers using the exact harmonic Langevin integrator*, arXiv:2605.24070 (first public version May 22, 2026), https://arxiv.org/abs/2605.24070 .
2. B. Leimkuhler and C. Matthews, *Rational Construction of Stochastic Numerical Methods for Molecular Sampling*, arXiv:1203.5428 (March 24, 2012), https://arxiv.org/abs/1203.5428 .
