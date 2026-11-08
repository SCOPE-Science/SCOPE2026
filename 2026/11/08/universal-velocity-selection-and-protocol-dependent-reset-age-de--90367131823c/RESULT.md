# Universal velocity selection and protocol-dependent reset-age delay at extreme displacement

## Finding

Consider a stationary one-dimensional inertial Brownian particle subjected to independent Poisson resetting. Two schemes are considered: a complete reset to zero position and zero velocity, and a complete position reset with a fresh equilibrium-Gaussian velocity. Both exhibit the following exact large-positive-position conditional law. Put
\[
\kappa=\frac{D_v}{\gamma^2},\qquad S=\frac{D_v}{\gamma},\qquad \beta=\sqrt{\frac r\kappa},\qquad d_0=\frac{3}{2\gamma},\qquad d_M=\frac1\gamma.
\]
Let \(T\) be the elapsed time since the most recent reset in the stationary process, and let \(j\in\{0,M\}\) identify the reset scheme. For either \(j\), as the conditioned position \(x\to+\infty\),
\[
\left(\frac{T-x/(2\sqrt{\kappa r})}{\sqrt{x}},\;V\right)\ \Big|\ (X=x)
\quad\Longrightarrow\quad
\mathcal N\!\left(0,\frac1{4\sqrt\kappa\,r^{3/2}}\right)
\otimes\mathcal N(\sqrt{\kappa r},S).
\]
The limiting fluctuations of reset age and instantaneous velocity are independent. Moreover, the reset scheme survives in the **unscaled conditional mean age**:
\[
\mathbb E[T\mid X=x]
=\frac{x}{2\sqrt{\kappa r}}+d_j+\frac1{2r}+o(1),\qquad
\operatorname{Var}(T\mid X=x)
=\frac{x}{4\sqrt\kappa\,r^{3/2}}+\frac1{2r^2}+o(1).
\]
In particular, the two conditional mean ages differ asymptotically by \(1/(2\gamma)\), even though the selected velocity laws agree. The stationary position density has the previously established exponential tail
\[
p_j(x)\sim\frac\beta2e^{-rd_j}e^{-\beta x}.
\]
For the more directly observable threshold event \(X>R\), the full joint rare-event law is, as \(R\to\infty\),
\[
\left(X-R,\frac{T-R/(2\sqrt{\kappa r})}{\sqrt R},V\right)\ \Big|\ (X>R)
\quad\Longrightarrow\quad
\mathrm{Exp}(\beta)\otimes
\mathcal N\!\left(0,\frac1{4\sqrt\kappa\,r^{3/2}}\right)
\otimes\mathcal N(\sqrt{\kappa r},S).
\]
Here \(\mathrm{Exp}(\beta)\) has density \(\beta e^{-\beta z}\) for \(z\ge0\). At large negative displacement the velocity-mean sign reverses while all other displayed constants remain unchanged. All limits hold for each fixed strictly positive triple \((\gamma,D_v,r)\); no uniformity as those parameters tend to zero is claimed.

## Assumptions and scope

Between resets, the position and velocity evolve on the entire real line according to
\[
dX_t=V_t\,dt,\qquad dV_t=-\gamma V_t\,dt+\sqrt{2D_v}\,dB_t,
\quad \gamma>0,\ D_v>0.
\]
At the points of an independent rate-\(r>0\) Poisson process the position becomes zero, and either (scheme \(0\)) velocity becomes zero, or (scheme \(M\)) velocity is independently redrawn from \(\mathcal N(0,D_v/\gamma)\). No physical-time cost is attached to the instantaneous reset. The stationary process exists by regeneration. Its reset age \(T\) has \(\mathrm{Exp}(r)\) distribution before conditioning on the particle position. The conditional distribution given \(X=x\) is the regular conditional distribution obtained from the joint stationary density, defined for nonzero real \(x\).

The symbol \(\mathcal N(m,s)\) denotes a Gaussian distribution of mean \(m\) and **variance** \(s\). The stated threshold law concerns sampling the particle at a stationary random observation time, **not** sampling the velocity at an actual level-crossing time, which would produce a velocity-weighted distribution.

## Proof

**1. Exact Gaussian mixture.** On an interval of length \(t>0\) following a reset, \((X_t,V_t)\) is a centered, nondegenerate bivariate Gaussian. Write
\[
A_j(t)=\operatorname{Var}(X_t),\quad
B_j(t)=\operatorname{Cov}(X_t,V_t),\quad
C_j(t)=\operatorname{Var}(V_t).
\]
Let \(q=e^{-\gamma t}\). Direct integration of the Ornstein–Uhlenbeck solution gives
\[
\begin{aligned}
A_0(t)&=\frac\kappa\gamma(2\gamma t-3+4q-q^2), &B_0(t)&=\kappa(1-q)^2,&C_0(t)&=S(1-q^2),\\
A_M(t)&=2\kappa\left(t-\frac{1-q}\gamma\right),&B_M(t)&=\kappa(1-q),&C_M(t)&=S.
\end{aligned}
\]
These identities follow, for instance, by representing the zero-initial-velocity process as stochastic integrals with kernels \(1-e^{-\gamma(t-s)}\) and \(e^{-\gamma(t-s)}\); the equilibrium initial-velocity contribution then adds the covariance of \(((1-q)V_0/\gamma,qV_0)\). Since the two stochastic-integral kernels are not proportional on any interval of positive length, \(A_j(t)C_j(t)-B_j(t)^2>0\). Consequently
\[
V\mid(X=x,T=t)\ \sim\ \mathcal N\!\left(\frac{B_j(t)x}{A_j(t)},\ C_j(t)-\frac{B_j(t)^2}{A_j(t)}\right).
\]
Renewal at the most recent Poisson reset gives the exact joint measure
\[
\Pr(T\in dt,X\in dx,V\in dv)
=r e^{-rt}\,\phi_{A_j(t),B_j(t),C_j(t)}(x,v)\,dt\,dx\,dv,
\]
where \(\phi\) is the corresponding centered Gaussian density. In particular, the unnormalized conditional density of \(T\) given \(X=x\) is
\[
 w_{j,x}(t)=\frac{r e^{-rt}}{\sqrt{2\pi A_j(t)}}
\exp\!\left[-\frac{x^2}{2A_j(t)}\right],\quad t>0.
\]

**2. Effective age law and an exponentially accurate comparison.** For fixed \(\gamma,D_v,r\), as \(t\to\infty\),
\[
A_j(t)=2\kappa(t-d_j)+O(e^{-\gamma t}),\quad
B_j(t)=\kappa+O(e^{-\gamma t}),\quad
C_j(t)=S+O(e^{-\gamma t}).
\]
Let \(x>0\), \(u_x=x/(2\sqrt{\kappa r})\), and set \(u=t-d_j\). The reference conditional density of \(u>0\) is
\[
q_x(u)=\frac{u^{-1/2}\exp[-ru-x^2/(4\kappa u)]}{I_x(r)},\qquad
I_x(r)=\int_0^\infty u^{-1/2}e^{-ru-x^2/(4\kappa u)}\,du
=\sqrt{\frac\pi r}\,e^{-\beta x}.
\]
The comparison is strong enough to control the first two age moments. Indeed, \(A_j(t)\le 2\kappa t\) for all \(t>0\), and hence \(w_{j,x}(t)\) away from a fixed relative neighborhood of \(u_x\) is exponentially small compared with its total integral. To see the exponential separation, use the strictly convex Laplace phase
\[
\Psi_x(u)=ru+\frac{x^2}{4\kappa u},\qquad
\Psi_x(u_x)=\beta x,
\]
whose value rises by a positive multiple of \(x\) when \(u/u_x\) leaves \([1/2,2]\). In the central region \(t=d_j+u\), \(u\in[u_x/2,2u_x]\), the covariance remainder is exponentially small, while \(x^2/A_j(t)^2\) stays bounded. Thus the actual age law and the translated reference density \(q_x(t-d_j)\) have exponentially small total-variation discrepancy, with exponentially small errors also in their polynomially weighted integrals. (For the exact density at very small \(t\), the Gaussian exponential suppresses any power singularity of \(1/\sqrt{A_j(t)}\); the same Laplace gap argument controls this endpoint.)

Consequently, the conditional density normalization is
\[
p_j(x)=\int_0^\infty w_{j,x}(t)\,dt
\sim\frac{r e^{-rd_j}}{\sqrt{4\pi\kappa}}I_x(r)
=\frac\beta2e^{-rd_j}e^{-\beta x},
\]
recovering the known exponential position tail. Differentiating the exact reference integral \(I_x(r)\) at fixed \(x\),
\[
\mathbb E_{q_x}u=-\partial_r\log I_x(r)
=\frac{x}{2\sqrt{\kappa r}}+\frac1{2r},
\qquad
\operatorname{Var}_{q_x}(u)=\partial_r^2\log I_x(r)
=\frac{x}{4\sqrt\kappa\,r^{3/2}}+\frac1{2r^2}.
\]
The exponentially accurate comparison proves both unscaled conditional-age asymptotics, including the scheme-dependent constant delay.

**3. Joint Gaussian selection.** For the reference density \(q_x\), set \(Z_x=(u-u_x)/\sqrt{x}\). Its moment-generating function is obtained from the same explicit integral:
\[
\mathbb E e^{sZ_x}
=e^{-su_x/\sqrt x}\frac{I_x(r-s/\sqrt{x})}{I_x(r)}
\longrightarrow
\exp\!\left[\frac{s^2}{8\sqrt\kappa\,r^{3/2}}\right]
\]
for each fixed \(s\) in a neighborhood of zero. Hence \(Z_x\) converges to the centered Gaussian with variance \(1/(4\sqrt\kappa\,r^{3/2})\). The shift \(d_j/\sqrt x\) disappears. Under the joint conditioning \(X=x,T=t\), the exact Gaussian velocity law in Step 1 satisfies, uniformly whenever \(|t-u_x|\le K\sqrt x\) for fixed \(K\),
\[
\frac{B_j(t)x}{A_j(t)}\longrightarrow\sqrt{\kappa r},
\qquad C_j(t)-\frac{B_j(t)^2}{A_j(t)}\longrightarrow S.
\]
The age-tightness from Step 2 and uniform conditional Gaussian convergence imply the displayed *independent* joint age–velocity limit. The statement for negative \(x\) follows by symmetry.

**4. Exceedance and overshoot.** From Step 2, uniformly for every bounded \(z\ge0\),
\[
\frac{p_j(R+z)}{p_j(R)}\longrightarrow e^{-\beta z},\qquad
\frac{\Pr(X>R+z)}{\Pr(X>R)}\longrightarrow e^{-\beta z}.
\]
The same Laplace bounds give tightness of the overshoot \(X-R\). Conditioning first on \(X=R+z\) for bounded \(z\), Steps 2–3 apply uniformly; centering at \(R\) rather than \(R+z\) changes the scaled age by \(O(1/\sqrt R)\). Integrating over \(z\) and removing the bounded cutoff proves the claimed independent exponential–Gaussian–Gaussian triple. This concludes the proof.

## Verification

The standalone `verify.py` computes the exact finite-age covariance functions and numerically integrates the renewal mixture using Simpson quadrature. It checks positive definiteness, the algebraic relations between the two reset prescriptions, the published marginal-tail prefactor, the conditional velocity mean and variance, and both the constant age offset and the age-variance profile. Two distinct parameter triples and two large-position values are tested. Run with `python verify.py` from the directory containing that file. The checks are bounded numerical corroboration; the infinite-position statements are proved in the previous section, not inferred from these tests.

## Relationship to prior work

Franke and Sokolov (2026) introduced and analyzed precisely these two reset prescriptions. Their exponential marginal-position tails, the position-density shape near the origin, and finite-time kurtosis are **prior results**; the new claim does not assert their novelty. Gupta (2018/2019) considered resetting position without resetting velocity and obtained the same equilibrium-initial-velocity marginal-position description but did not study this jointly conditioned extreme event. Singh (2020) gave a joint position–velocity stationary law for the *undamped random-acceleration process*, where the large-displacement saddle and tail are different. Montero, Palassini and Masoliver (2023/2024) derived the general renewal formula for a fixed-state-reset inertial particle and computed level-crossing intensities; their general stationary joint-mixture representation is acknowledged here and is the natural starting identity. Their large-reset-rate crossing asymptotics do not explicitly provide the fixed-reset-rate far-position joint conditional Gaussian law, the independence from overshoot, or the reset-prescription-dependent order-one age shift proved here. The latter facts are analytic consequences that require a moving-saddle conditional-limit calculation, not merely a change of notation in a previously stated result.

## Limitations

The analysis concerns a single particle, Gaussian thermal noise, constant damping and strictly positive fixed rate and damping. It does not establish uniform limits when resetting rate, damping, diffusivity or the reset-velocity distribution vary with the conditioned position. Physical return delays, correlated resetting events, position-dependent friction and particles sampled at *crossing times* are excluded. Originality was assessed through accessible primary texts, topical literature searches and published research records; absence of an exact prior statement is not a guarantee of publication priority. No independent mathematical audit has been performed.

## References

1. H. Franke and I. M. Sokolov, “Resetting of underdamped Brownian motion,” *Physical Review E* **113**, 064125 (2026), published 2026-06-11, https://doi.org/10.1103/qyl8-6q9h.
2. D. Gupta, “Stochastic resetting in underdamped Brownian motion,” arXiv:1812.07227 (first submitted 2018-12-18), https://arxiv.org/abs/1812.07227.
3. P. Singh, “Random acceleration process under stochastic resetting,” *Journal of Physics A* **53**, 405005 (2020), arXiv:2007.05576, https://arxiv.org/html/2007.05576v1.
4. M. Montero, M. Palassini and J. Masoliver, “The effect of stochastic resettings on the counting of level crossings for inertial random processes,” *Physical Review E* **110**, 014116 (2024), arXiv:2312.13968, https://arxiv.org/abs/2312.13968.
