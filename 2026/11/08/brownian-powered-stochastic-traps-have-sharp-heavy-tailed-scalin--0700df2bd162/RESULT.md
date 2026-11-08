# Brownian-powered stochastic traps have sharp heavy-tailed scaling laws

## Finding

Let \(B\) and \(W\) be independent standard one-dimensional Brownian motions starting at zero. For fixed \(p>0\), \(D>0\), \(\lambda>0\), \(a\ge0\), and deterministic \(x_0\in\mathbb R\), consider the time-dependent overdamped Langevin equation
\[
\mathrm dX_t=-(a+\lambda |B_t|^p)X_t\,\mathrm dt+\sqrt{2D}\,\mathrm dW_t,\qquad X_0=x_0.
\]
Then, jointly with the rescaled instantaneous fluctuating environment,
\[
\left(\frac{B_t}{\sqrt t},\ t^{p/4}X_t\right)
\ \xRightarrow[t\to\infty]{}\ 
\left(G,\sqrt{\frac D\lambda}\,\frac{Z}{|G|^{p/2}}\right),
\]
where \(G\) and \(Z\) are independent standard normal random variables. For the square-Brownian stiffness of Gupta and Klapp, \(p=2\), the rescaled position has the centered Cauchy law of scale \(\sqrt{D/\lambda}\). Neither the nonnegative static stiffness \(a\) nor the deterministic initial position changes this limit.

Writing \(Y_p=\sqrt{D/\lambda}\,Z/|G|^{p/2}\), its two-sided tail has the sharp asymptotic
\[
\lim_{R\to\infty}R^{2/p}\mathbb P(|Y_p|>R)
=\frac{2^{1/2+1/p}}{\pi}\,\Gamma\!\left(\frac12+\frac1p\right)
\left(\frac D\lambda\right)^{1/p}.
\]
Consequently, for every \(s>0\), the limiting absolute moment \(\mathbb E|Y_p|^s\) is finite **if and only if** \(s<2/p\). This statement concerns moments of the limiting law; it makes no assertion that moments of the rescaled prelimit positions converge.

## Assumptions and scope

The thermal and environmental Brownian motions are independent, with quadratic variation equal to elapsed time. Time is measured in the dimensionless units in which the environmental Brownian diffusivity is one. The drift coefficient is \(a+\lambda|B_t|^p\) with the given positive parameters and no time-dependent environment reset. Every assertion is a one-time large-time distributional limit (together with the stated simultaneous environmental coordinate), not convergence of sample paths or of unbounded observables.

## Proof

**1. Conditional Gaussian representation.** For any continuous realization of the environmental Brownian path, the integrating-factor solution is Gaussian with mean and variance
\[
M_t=x_0\exp\!\left[-at-\lambda\int_0^t|B_s|^p\,\mathrm ds\right],
\]
\[
V_t=2D\int_0^t\exp\!\left[-2au-2\lambda\int_{t-u}^{t}|B_s|^p\,\mathrm ds\right]\,\mathrm du.
\]
Therefore the joint law of the environment and position at time \(t\) can be represented using a fresh standard normal \(Z\), independent of the environment, as \(X_t=M_t+\sqrt{V_t}Z\). The formula follows from Itô isometry applied conditionally to \(W\); positivity of \(V_t\) is immediate for \(t>0\).

**2. Singular-endpoint integral lemma.** Let \(f:[0,1]\to[0,\infty)\) be continuous with \(f(1)>0\), and let \(p>0\). Then for any \(a\ge0\), \(\lambda>0\),
\[
\int_0^{t^{1+p/2}}\!\exp\!\left[-\frac{2ay}{t^{p/2}}-2\lambda t^{1+p/2}\!\int_{1-y/t^{1+p/2}}^1 f(v)\,\mathrm dv\right]\,\mathrm dy
\longrightarrow\frac1{2\lambda f(1)}.
\]
Indeed, fix \(\delta\in(0,1)\) such that \(f(v)\ge c>0\) on \([1-\delta,1]\). For \(y\le\delta t^{1+p/2}\), the integrand is bounded by \(e^{-2\lambda cy}\) and for each fixed \(y\) converges to \(e^{-2\lambda f(1)y}\). Dominated convergence applies on this truncated interval extended by zero. On the remaining interval the integral inside the exponent is at least \(\delta c\), so the contribution is bounded by \(t^{1+p/2}e^{-2\lambda\delta c\,t^{1+p/2}}\), which tends to zero. This establishes the lemma without a uniform lower bound on \(f\) away from the endpoint.

**3. Brownian scaling and the conditional variance limit.** For each \(t>0\), the rescaled environmental path \((B_{tv}/\sqrt t)_{0\le v\le1}\) has the law of a standard Brownian path \((\mathcal B_v)_{0\le v\le1}\). With \(T_t=t^{1+p/2}\), a change of variables in the conditional variance yields the following equality in joint law with the environment's endpoint:
\[
\left(\frac{B_t}{\sqrt t},t^{p/2}V_t\right)
\stackrel{\mathrm d}=\left(\mathcal B_1,
2D\int_0^{T_t}\exp\!\left[-\frac{2ay}{t^{p/2}}
-2\lambda T_t\int_{1-y/T_t}^1|\mathcal B_v|^p\,\mathrm dv\right]\,\mathrm dy\right).
\]
Almost surely \(\mathcal B_1\ne0\). Apply the preceding deterministic lemma pathwise to \(f(v)=|\mathcal B_v|^p\) to obtain
\[
\left(\mathcal B_1,t^{p/2}V_t\right)
\longrightarrow\left(\mathcal B_1,\frac D{\lambda|\mathcal B_1|^p}\right)
\quad\text{almost surely under the displayed scaling coupling}.
\]
Similarly, for that coupling, \(t^{p/4}M_t\) tends to zero almost surely because \(\int_0^1|\mathcal B_v|^p\,\mathrm dv>0\). Conditional Gaussian representation and the continuous-mapping theorem now give the claimed joint weak convergence.

**4. Tail and moment threshold.** Put \(q=2/p\) and \(c=\sqrt{D/\lambda}\). For \(R>0\), condition on \(|Z|\):
\[
\mathbb P(|Y_p|>R)
=\mathbb E\!\left[F\!\left(\left(\frac{c|Z|}{R}\right)^q\right)\right],\qquad
F(u)=\mathbb P(|G|<u).
\]
The half-normal distribution satisfies \(F(u)/u\to\sqrt{2/\pi}\) as \(u\downarrow0\) and \(F(u)\le\sqrt{2/\pi}\,u\) for all \(u\ge0\). Dominated convergence gives
\[
R^q\mathbb P(|Y_p|>R)\longrightarrow
\sqrt{\frac2\pi}\,c^q\mathbb E|Z|^q
=\frac{2^{1/2+q/2}}{\pi}\Gamma\!\left(\frac{q+1}2\right)c^q,
\]
which is the displayed constant. Independence gives \(\mathbb E|Y_p|^s=c^s\mathbb E|Z|^s\mathbb E|G|^{-ps/2}\), and the last Gaussian negative moment is finite precisely when \(ps/2<1\). At \(p=2\), symmetry identifies \(Z/|G|\) in law with the ratio \(Z/G\), which is the standard Cauchy distribution.

## Verification

The companion file `verify.py` provides independent numerical quadrature checks of the singular-endpoint conditional-variance formula against a known continuous path at three powers and three times, three checks of the Cauchy characteristic function, and three checks of the sharp two-sided tail constants, plus the exact Cauchy-prefactor identity. All 16 checks passed when executed with Python, SciPy, and NumPy. The analytic dominated-convergence argument, rather than numerical discretization, proves the infinite-time theorem. Finite-time moments are finite because \(|M_t|\le |x_0|\) and \(V_t\le2Dt\); nonuniform integrability is possible after rescaling.

## Relationship to prior work

Gupta and Klapp (arXiv:2609.33751v1, first publicly submitted September 27, 2026) study exactly the Brownian-square stiffness model and derive the thermal position's first four moments and their algebraic decay. Their analysis explicitly describes the difficulty of averaging its conditional Gaussian density. The present result concerns the **entire rescaled law**, identifies the Cauchy law for that model, and gives a power-law family for all positive stiffness powers. Their separate stationary Ornstein–Uhlenbeck stiffness model (arXiv:2507.20915) has a different environment and does not imply this nonstationary scaling. The normal-ratio/Cauchy identity itself is classical and is not claimed as new; Pillai (arXiv:1602.08181) is an explicit reference. Novelty, insofar as supported by the examined sources, lies in the model-specific scaling limit, its joint environmental dependence, and its sharp power-law family.

## Limitations

The weak limit applies to fixed \(p>0\) and positive \(D,\lambda\), with \(a\ge0\). It does not determine convergence rates, convergence of prelimit moments, multitime or pathwise limits, or the distribution of finite-time heat and work. An independently performed audit has not been obtained. A wider unpublished or unindexed theorem about random-stiffness Langevin processes could overlap the result.

## References

1. D. Gupta and S. H. L. Klapp, *Non-stationary Statistics and Energetics of Brownian Motion under Stochastic Harmonic Confinement*, arXiv:2609.33751v1 (September 27, 2026), https://arxiv.org/abs/2609.33751 .
2. D. Gupta and S. H. L. Klapp, *Nonequilibrium fluctuations in a harmonic trap with annealed stochastic stiffness*, arXiv:2507.20915 (2025), https://arxiv.org/abs/2507.20915 .
3. N. S. Pillai, *Ratios and Cauchy Distribution*, arXiv:1602.08181 (2016), https://arxiv.org/abs/1602.08181 .
