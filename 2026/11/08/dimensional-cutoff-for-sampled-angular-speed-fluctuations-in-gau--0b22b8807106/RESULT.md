# Dimensional cutoff for sampled angular-speed fluctuations in Gaussian diffusions

## Finding

For every integer \(d\ge2\) and every sampling interval \(\Delta>0\), let \(X_t\in\mathbb R^d\) be the *stationary, centered*, nondegenerate Ornstein–Uhlenbeck diffusion
\[
 dX_t=M X_t\,dt+G\,dB_t,
\]
where \(M\) is a real Hurwitz \(d\)-by-\(d\) matrix and \(G\) is invertible. Define the **chord-based sampled angular-speed magnitude**
\[
 \Omega_\Delta(t)=\frac{\|P_{X_t^\perp}(X_{t+\Delta}-X_t)\|}{\Delta\|X_t\|}
 =\frac{\|X_t\wedge(X_{t+\Delta}-X_t)\|}{\Delta\|X_t\|^2}.
\]
This is an unbounded velocity-ratio statistic, *not* the bounded principal angular increment divided by \(\Delta\). It is defined almost surely since \(\mathbb P(X_t=0)=0\). Let \(\Sigma\) be the stationary covariance, \(E_\Delta=e^{M\Delta}\), and \(Z_\Delta\sim N(0,Q_\Delta)\), where
\[
 Q_\Delta=\int_0^\Delta e^{Ms}GG^\mathsf T e^{M^\mathsf T s}\,ds
 =\Sigma-E_\Delta\Sigma E_\Delta^\mathsf T.
\]
The innovation \(Z_\Delta\) is independent of \(X_t\). Write \(p_0=(2\pi)^{-d/2}(\det\Sigma)^{-1/2}\) and
\[
 J_d=\frac{2\pi^{d/2}\Gamma(d-1/2)}{\Gamma((d-1)/2)\Gamma(d)}.
\]
Then the **exact sharp tail constant** is
\[
 \boxed{\lim_{w\to\infty}w^d\mathbb P(\Omega_\Delta>w)
 =\frac{p_0 J_d}{d\Delta^d}\mathbb E\|Z_\Delta\|^d=:C_{d,\Delta}\in(0,\infty).}
\]
Consequently, for any real \(q>0\),
\[
 \boxed{\mathbb E\Omega_\Delta^q<\infty\ \Longleftrightarrow\ q<d.}
\]
In particular a finite-lag sampled angular speed has **infinite second moment in dimension two and finite second moment in every dimension three or higher**, even in a stationary diffusion with rotational drift. At the critical order \(q=d\), the truncated moment diverges logarithmically: \(\mathbb E[\Omega_\Delta^d\mathbf1_{\{\Omega_\Delta\le R\}}]\sim dC_{d,\Delta}\log R\).

For the reversible isotropic case \(M=-\kappa I\), \(G=\sqrt{2\kappa}\,sI\), where \(\kappa,s>0\), put \(c_\Delta=\sqrt{1-e^{-2\kappa\Delta}}/\Delta\). With independent chi random variables,
\[
 \Omega_\Delta\stackrel{\mathrm d}=c_\Delta\frac{\chi_{d-1}}{\chi_d},\qquad
 \mathbb E\Omega_\Delta^q=c_\Delta^q
 \frac{\Gamma((d-1+q)/2)\Gamma((d-q)/2)}{\Gamma((d-1)/2)\Gamma(d/2)}
 \quad(0\le q<d).
\]
For \(z=w/c_\Delta\ge0\), this specializes to
\[
 \mathbb P(\Omega_\Delta>w)=
 \begin{cases}
 1-z/\sqrt{1+z^2},&d=2,\\
 (1+z^2)^{-3/2},&d=3.
 \end{cases}
\]
Thus the two-dimensional tail constant equals \(c_\Delta^2/2\), while the three-dimensional tail constant equals \(c_\Delta^3\), and \(\mathbb E\Omega_\Delta^2=2c_\Delta^2\) in dimension three.

For a genuinely circulating isotropic three-dimensional diffusion, let \(M=-\kappa I+K\), with \(K\) the skew generator of rotation about the third coordinate at rate \(\omega\in\mathbb R\) and the same \(G=\sqrt{2\kappa}\,sI\). Writing \(\rho=e^{-\kappa\Delta}\) and \(c=\cos(\omega\Delta)\), the second moment remains exactly finite:
\[
 \boxed{\mathbb E\Omega_\Delta^2=
 \frac{2(1-\rho^2)+(4\rho^2/15)(1-c)(3+2c)}{\Delta^2}.}
\]
Define the signed axial chord-speed component by \(\Omega_{\Delta,3}^{\mathrm{sgn}}=[X_t\times(X_{t+\Delta}-X_t)]_3/(\Delta\|X_t\|^2)\). Its mean is \(2\rho\sin(\omega\Delta)/(3\Delta)\), which is nonzero when \(\sin(\omega\Delta)\ne0\). Hence this finite-variance example can exhibit nonzero mean circulation; nothing here establishes reliable single-trajectory motor performance.

## Assumptions and scope

The dimension is an arbitrary but fixed integer at least two; the sampling lag is fixed and strictly positive. The drift is Hurwitz, the instantaneous diffusion matrix \(G\) is invertible, and the process starts in its unique centered Gaussian invariant law. All norms and projections are Euclidean. The asymptotic \(w\to\infty\) is taken **before** any small-lag limit. No assertion is made for rank-deficient noise, singular stationary covariance, non-Gaussian stationary laws, dimension one, or the principal-angle statistic.

## Proof

**1. Gaussian innovation.** Variation of constants gives \(X_{t+\Delta}=E_\Delta X_t+Z_\Delta\), where \(Z_\Delta\) is independent of \(X_t\) and has the positive-definite covariance \(Q_\Delta\). Set \(A=E_\Delta-I\). For \(X_t=ru\), \(r>0\) and \(u\in S^{d-1}\), the event \(\Omega_\Delta>w\) is equivalent to
\[
 \|P_{u^\perp}(Aru+Z_\Delta)\|>\Delta rw.
\]

**2. Exact tail.** Substitute \(r=t/w\) in the Gaussian polar-coordinate integral. For \(p\) the density of \(X_t\),
\[
 w^d\mathbb P(\Omega_\Delta>w)
 =\int_{S^{d-1}}\!\int_0^\infty t^{d-1}p(tu/w)
 \mathbb P\big(\|P_{u^\perp}(Atu/w+Z_\Delta)\|>\Delta t\big)\,dt\,d\sigma(u).
\]
For \(w>2\|A\|/\Delta\), the displayed event forces \(\|Z_\Delta\|>\Delta t/2\). The Gaussian density \(p\) is bounded, so the integrand has an integrable majorant \(Ct^{d-1}\mathbb P(\|Z_\Delta\|>\Delta t/2)\) uniformly in \(u\). Dominated convergence gives the limit
\[
 \frac{p_0}{d\Delta^d}\int_{S^{d-1}}
 \mathbb E\|P_{u^\perp}Z_\Delta\|^d\,d\sigma(u).
\]
For any fixed nonzero vector \(z\), rotational invariance of surface measure gives
\[
 \int_{S^{d-1}}\|P_{u^\perp}z\|^d\,d\sigma(u)
 =\|z\|^d\int_{S^{d-1}}(1-u_1^2)^{d/2}\,d\sigma(u)
 =J_d\|z\|^d.
\]
The final sphere integral is \(|S^{d-2}|B(1/2,d-1/2)\), giving the stated gamma expression. This calculation shows that the leading tail is **independent of the drift matrix except through the stationary density at zero and innovation covariance**. Full-rank noise makes \(C_{d,\Delta}\) strictly positive.

**3. Sharp moment cutoff.** The tail integration identity \(\mathbb E\Omega_\Delta^q=q\int_0^\infty w^{q-1}\mathbb P(\Omega_\Delta>w)\,dw\), with a positive \(w^{-d}\) asymptotic, proves finiteness exactly when \(q<d\). The same identity after truncation gives the critical logarithmic coefficient \(dC_{d,\Delta}\); the boundary correction \(R^d\mathbb P(\Omega_\Delta>R)\) is bounded and does not alter that coefficient.

**4. Isotropic law.** In the reversible isotropic case, write \(X_t=sRU\) with \(R\sim\chi_d\), \(U\) uniform on the unit sphere, independent of the Gaussian innovation. Conditional on \(U\), the perpendicular innovation norm divided by \(s\sqrt{1-e^{-2\kappa\Delta}}\) is \(\chi_{d-1}\), independent of \(R\). The deterministic increment \((e^{-\kappa\Delta}-1)X_t\) has no perpendicular component. This yields the chi ratio, its gamma moments, and the two beta-prime survival functions by direct integration.

**5. Circulating three-dimensional case.** For rotation about the third axis, \(e^{M\Delta}=\rho R_\phi\), \(\phi=\omega\Delta\), and \(X_t=sRU\) with isotropic direction \(U\). Conditional transverse-noise variance is \(2s^2(1-\rho^2)\), and \(\mathbb E(R^{-2})=1\) for \(R\sim\chi_3\). The deterministic transverse contribution to the second moment is \(\rho^2\mathbb E[1-(U^\mathsf T R_\phi U)^2]/\Delta^2\). Since \(\mathbb E U_3^2=1/3\) and \(\mathbb E U_3^4=1/5\), that orientation average equals \(4(1-c)(3+2c)/15\), proving the displayed second-moment formula. The signed axial mean uses \(\mathbb E(U_1^2+U_2^2)=2/3\).

## Verification

Run `python3 check.py` with a standard Python installation. The checker tests the gamma moment identities, exact survival functions, sphere integral constants, the two- and three-dimensional tail constants, and fixed-seed Gaussian samples for two- and three-dimensional reversible and rotating three-dimensional cases. It checks both the finite second moment and nonzero mean axial rotation in a circulating example. Finite sampling is **diagnostic only**, not proof of a tail exponent, moment divergence or universal classification; those follow from the preceding analysis.

## Relationship to prior work

Viot et al., *Destructive effect of fluctuations on the performance of a Brownian gyrator* (arXiv:2307.05248, first public 2023-07-11; journal DOI 10.1039/D3SM01606D), derive the \(|\mathcal W|^{-3}\) density tails and divergent angular-velocity variance for a **two-dimensional** Brownian gyrator, including an explicit discrete-time treatment and supplementary calculations. The present result recovers that two-dimensional moment obstruction for the absolute chord-based statistic but adds the **full spatial-dimension cutoff**, an explicit anisotropic Gaussian stationary tail constant, exact isotropic distributions, and a finite-variance three-dimensional example with nonzero mean axial circulation. Dotsenko et al. (arXiv:2309.10807) study two-dimensional random-acceleration gyration, not the multi-dimensional sampled OU angular-speed threshold. Bae et al. (2021) study inertial effects on a two-dimensional gyrator, not this dimension-indexed stationary sampled-statistic law. The Gaussian/chi-ratio and sphere-integration ingredients are elementary and not claimed as new general probability theory.

## Limitations

The estimator uses an unbounded *velocity-ratio* definition; a bounded principal angle divided by a fixed sampling interval has different moment properties. At every fixed dimension \(d\ge3\), second moments are finite for fixed lag, but they diverge as the observation interval tends to zero in the overdamped isotropic model. Finite variance is not evidence of regular rotation in a single trajectory or useful power output. The general anisotropic model is linear Gaussian with nondegenerate noise; extension to nonlinear and singular-noise dynamics is unproved. Earlier unindexed analyses of general Gaussian velocity-ratio laws could subsume parts of this result; priority is not independently certified.

## References

- P. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni, and G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248 (first posted 2023-07-11), https://arxiv.org/abs/2307.05248; *Soft Matter* **20** (2024), 3154–3160, https://doi.org/10.1039/D3SM01606D.
- V. Dotsenko, G. Oshanin, L. Pastur, and P. Viot, *Irregular gyration of a two-dimensional random-acceleration process in a confining potential*, arXiv:2309.10807 (2023), https://arxiv.org/abs/2309.10807.
- Y. Bae, S. Lee, J. Kim, and H. Jeong, *Inertial effects on the Brownian gyrator*, *Physical Review E* **103** (2021), 032148, https://doi.org/10.1103/PhysRevE.103.032148.
