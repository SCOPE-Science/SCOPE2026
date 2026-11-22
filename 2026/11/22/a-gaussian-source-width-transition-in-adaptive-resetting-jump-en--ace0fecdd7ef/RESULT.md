# A Gaussian source-width transition in adaptive-resetting jump entropy production

## Finding

A one-dimensional Ornstein–Uhlenbeck particle can be held at an exactly prescribed compressed Gaussian stationary law by state-dependent resetting to a narrower Gaussian source. Although the full stationary position law is independent of the total reset flux, the jump-channel Schnakenberg entropy-production rate has a **sharp three-regime high-flux transition** at source-to-target variance ratio \(z=1/2\), together with a uniform logarithmic crossover.

Fix \(\kappa,D,v>0\) with \(v<D/\kappa\), let \(a=D/v-\kappa>0\), and choose a centered Gaussian reset source of variance \(w=zv\), where \(0<z<1\). For any mean reset flux \(R>R_*(z)\), there is exactly one state-dependent resetting hazard with the desired stationary target \(N(0,v)\), and its sharp nonnegativity threshold is
\[
\frac{R_*(z)}a=\begin{cases}
\dfrac{2z^{3/2}}{1-z}\exp\!\left(\dfrac{1-3z}{2z}\right),&0<z<1/3,\\[4pt]
\sqrt z,&1/3\leq z<1.
\end{cases}
\]
For that hazard, denote by \(J(R,z)\) the *jump-channel* Schnakenberg entropy-production rate, not the total physical cost of implementing reset operations. Put
\[
L=\log(R/a),\qquad p=\frac1{1-z},\qquad
K(z)=\frac{(2z^{3/2})^p}{\sqrt\pi\,(1-z)^{p-1/2}}.
\]
As \(R/a\to\infty\) at each fixed \(z\),
\[
\boxed{
J(R,z)\sim\begin{cases}
 aK(z)\dfrac{p\pi}{(p-1)\sin[\pi(p-1)]}(R/a)^{1-p}L^{p-1/2},&0<z<1/2,\\[6pt]
 \dfrac{4a^2}{5R}\sqrt{\dfrac2\pi}\,L^{5/2},&z=1/2,\\[7pt]
 \dfrac{a^2}{R}\dfrac{z(3z^2-2z+1)}{(2z-1)^{5/2}},&1/2<z<1.
\end{cases}}
\]
The critical transition has a stronger, *uniform* form. For any fixed real \(\lambda\), choose \(z=z_R=1/2+\lambda/L\). Then
\[
\boxed{\quad
\lim_{R/a\to\infty}\frac{RJ(R,z_R)}{a^2L^{5/2}}
=\Phi(\lambda):=\frac1{2\sqrt\pi}\int_0^2t^{3/2}e^{-2\lambda t}\,dt.\quad}
\]
Convergence is uniform for \(\lambda\) in any compact subset of \(\mathbb R\). In addition, \(J(R,z)>0\) and decreases strictly with \(R\) at every fixed \(z\) where the hazard is positive.

## Assumptions and scope

The continuous-space process follows \(dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t\) between resets. At a state-dependent, memoryless hazard \(r_R(X_{t^-})\), it is independently redrawn from \(\rho_w=N(0,w)\). The intended invariant density is \(\rho_v=N(0,v)\). Rates are allowed to be unbounded functions of position; strictly positive rates require \(R>R_*(z)\). In this statement, \(R\) is the *stationary mean number of reset events per unit time*, not a spatially constant Poisson hazard. The source-width ratio \(z\) is in the open interval \((0,1)\). All logarithms are natural and entropy rates are dimensionless in units of Boltzmann's constant.

The jump-channel entropy production is defined using the forward and reverse jump probability fluxes \(q(x,y)=r_R(x)\rho_v(x)\rho_w(y)\) and \(q(y,x)\):
\[
J=\frac12\iint_{\mathbb R^2}(q(x,y)-q(y,x))\log\frac{q(x,y)}{q(y,x)}\,dx\,dy.
\]
The diffusive channel is deliberately excluded from \(J\); it contributes \(a^2v/D\) to the stationary diffusion-plus-jump entropy rate, independently of \(R\) and \(z\). The physical energetic cost of implementing resets is not modeled.

## Proof

**1. Exact stationary design and minimum feasible flux.** The adjoint Ornstein–Uhlenbeck generator is \(\mathcal L^*\rho=\kappa\partial_x(x\rho)+D\partial_x^2\rho\). Direct differentiation gives
\[
\mathcal L^*\rho_v=-a(1-x^2/v)\rho_v.
\]
Stationarity and the normalization \(R=\int r_R\rho_v\) force, uniquely for prescribed \(R\),
\[
r_R(x)=-a(1-x^2/v)+R\frac{\rho_w(x)}{\rho_v(x)}.
\]
Write \(Y=x^2/(2w)\) when \(x\sim\rho_w\). Then \(Y\) has density \(e^{-y}y^{-1/2}/\sqrt\pi\), and
\[
f_z(Y):=\frac{\mathcal L^*\rho_v(x)}{\rho_w(x)}
=a\sqrt z(2zY-1)e^{(1-z)Y},\qquad
h_R(x):=\frac{r_R(x)\rho_v(x)}{\rho_w(x)}=R+f_z(Y).
\]
The negative part of \(f_z\) is confined to \(0\leq Y<1/(2z)\). Maximizing \(a\sqrt z(1-2zY)e^{(1-z)Y}\) on that interval gives an interior maximum \(Y_*=(1-3z)/(2z(1-z))\) when \(z<1/3\), and the endpoint maximum at zero when \(z\geq1/3\). This is precisely \(R_*(z)\). Since \(\int\mathcal L^*\rho_v=0\), \(\mathbb E_w f_z=0\), hence the prescribed \(R\) really is the mean reset flux. For \(R>R_*\), the hazard is continuous and everywhere positive, with large-position growth \(r_R(x)\sim ax^2/v\). The dynamics is non-explosive: after resets it has independent, identically distributed positive-length excursions from \(\rho_w\), and the jump rate is locally bounded along each continuous excursion. Standard regenerative occupation identities, or uniqueness of the resolvent of the killed diffusion plus reinjection, identify \(\rho_v\) as the invariant probability law.

**2. Exact jump entropy.** By the definition of \(h_R\), \(q(x,y)=\rho_w(x)\rho_w(y)h_R(x)\). Antisymmetrizing the logarithmic flux ratio gives
\[
J=\operatorname{Cov}_{\rho_w}(h_R,\log h_R)
=\mathbb E_w\left[f_z\log\left(1+\frac{f_z}{R}\right)\right].
\]
The integrals are finite for every fixed \(z>0\) and \(R>R_*\): in the positive tail the integrand has weight bounded by a polynomial times \(e^{-zY}\). The covariance is strictly positive because \(h_R\) is not constant and \(\log\) increases strictly. Differentiation under the integral gives
\[
\partial_RJ(R,z)=-\frac1R\mathbb E_w\frac{f_z^2}{R+f_z}<0.
\]
The stationary diffusion current is \(j(x)=ax\rho_v(x)\), so its entropy-production term is \(\int j^2/(D\rho_v)\,dx=a^2v/D\).

**3. Heavy-tail exponent and the subcritical law.** Let \(F=f_z/a\) and \(\theta=1-z\). In the positive tail, \(F\sim B(z)Y e^{\theta Y}\), with \(B(z)=2z^{3/2}\). The Gamma-half survival asymptotic \(\Pr(Y>y)\sim e^{-y}/\sqrt{\pi y}\) and inversion of \(B(z)y e^{\theta y}\) yield
\[
\Pr(F>s)\sim K(z)s^{-p}(\log s)^{p-1/2},\qquad s\to\infty.
\]
The negative part of \(F\) is bounded, giving only an \(O(a^2/R)\) contribution to \(J\). For \(1<p<2\), integrate the positive part by tails with \(g_R(s)=s\log(1+s/R)\). Regular variation and dominated tail bounds reduce the leading constant to
\[
\int_0^\infty\left(\log(1+t)+\frac{t}{1+t}\right)t^{-p}dt
=\frac{p\pi}{(p-1)\sin[\pi(p-1)]}.
\]
This gives the first line of the three-regime formula, including its exact amplitude.

**4. Critical and finite-second-moment regimes.** At \(z=1/2\), the last tail formula has \(p=2\) and \(K=\sqrt{2/\pi}\). Its truncated second moment grows as \((4K/5)(\log s)^{5/2}\). In the entropy integral, the part where \(F\) exceeds \(R/a\) contributes only \(O((a^2/R)L^{3/2})\), a logarithmic order smaller, giving the second line. For \(z>1/2\), direct integration against the Gamma-half density gives the exact finite second moment
\[
\mathbb E_w f_z^2=a^2\frac{z(3z^2-2z+1)}{(2z-1)^{5/2}}.
\]
The inequality \(0\leq s\log(1+s/R)\leq s^2/R\) for \(s\geq0\), together with the bounded negative part, permits dominated convergence in \(R J(R,z)\to\mathbb E_w f_z^2\), establishing the third line.

**5. Uniform critical window.** Fix \(\Lambda<\infty\), restrict \(|\lambda|\leq\Lambda\), and put \(z_R=1/2+\lambda/L\). Under \(Y=L t\), for every \(0<t<2\), the ratio \(f_{z_R}(Lt)/R\to0\), uniformly on closed subintervals of \((0,2)\). Hence the entropy integrand is asymptotic to \(f^2/R\); the Gamma-half density gives the normalized limiting measure
\[
\frac{R}{a^2L^{5/2}}\mathbb E_w\left[f_{z_R}\log(1+f_{z_R}/R);Y/L\in dt\right]
\longrightarrow\frac{t^{3/2}e^{-2\lambda t}}{2\sqrt\pi}\,dt.
\]
On \(0<Y\leq2L\), the elementary bound \(f\log(1+f/R)\leq f^2/R\) for positive \(f\) gives an integrable, uniform envelope after the above normalization. Its negative-part contribution is \(O(a^2/R)\). For \(Y>2L\), the bounds \(|f|\leq Ca(1+Y)e^{(1-z_R)Y}\), \(\log(1+f/R)\leq C(1+Y)\), and the Gamma-half density imply an upper contribution \(O(aR^{-1}L^{3/2})\), uniformly for \(|\lambda|\leq\Lambda\). Divide by \(a^2R^{-1}L^{5/2}\) and apply dominated convergence, first away from \(t=2\) and then to the shrinking boundary band. The claimed integral and compact-uniform convergence follow. At \(\lambda=0\), \(\Phi(0)=(4/5)\sqrt{2/\pi}\), recovering the critical coefficient.

## Verification

The companion standalone script `checks/verify_jump_width.py` uses Python 3 and SciPy. Its 47 deterministic checks include independent scalar minimization of the feasible reset threshold, Gaussian-half quadrature of the zero-mean flux correction, integration of the exact second moment, positivity and strict high-rate ordering, and representative ratios to each asymptotic regime and the critical window. The broad asymptotic tolerances deliberately account for slow logarithmic convergence. These finite computations corroborate identities but **do not** establish any infinite-rate claim; the proof above supplies those limiting arguments.

## Relationship to prior work

The initiating thermodynamic motivation is Farago's 2026 harmonic resetting-cycle analysis [1], which studies ordinary reset clocks and endpoint/trajectory KL accounting, **not** the state-dependent exact Gaussian inverse policy or the source-width transition of its jump-channel entropy. General adaptive-resetting and nonequilibrium steady-state methods were developed earlier by Keidar and collaborators [2]. Mori, Olsen and Krishnamurthy [3] derive entropy production for resetting to a random distribution at a **constant** hazard; their Gaussian-source large-deviation transition is in observation time and is not the high-reset-flux source-width transition proved here.

Most directly, Chu and collaborators' November 2026 paper [4], especially Supplement S2–S3, already establishes both the **general** stationary inverse-hazard equation and the **general** jump-flux covariance formula. Those two identities are prior work and **are not claimed as new**. The specific calculated minimax rate \(R_*(z)\), the three explicit Gaussian high-flux entropy regimes, and the compact-uniform crossover profile \(\Phi\) are the distinct proposed finding; they are not stated in the inspected sections of [4]. General Gaussian stationary engineering with a spatially **constant** reset hazard and a non-Gaussian reset law [5] has different control variables and does not imply this state-dependent entropy result without a new analysis. Existing Gaussian reset-cycle comparisons [6] concern endpoint Jeffreys divergences or reset cadence rather than this stationary Schnakenberg jump channel.

## Limitations

This is a one-dimensional, centered, compressed-Gaussian design with \(0<z<1\), unbounded admissible spatial hazards, exact stationary targeting, and independent finite-variance reset draws. It does not establish optimality among reset sources, finite-flux error bounds, robust experimental realization with bounded control, or any rate for the physical work of implementing resets. The limiting jump contribution vanishes for large \(R\), but the diffusion-channel entropy production remains exactly \(a^2v/D\); **total entropy production does not vanish** in this model. No independent review or experiment is asserted. Although no exact covering result was found in the specified comparisons, generic published formulas may make a mathematically equivalent version derivable elsewhere; publication priority requires further expert evaluation.

## References

[1] O. Farago, *The Resetting Heat Engine: A Thermodynamic Cycle of Thermal Expansion and Compression*, arXiv:2605.28445, first public May 27, 2026; https://arxiv.org/abs/2605.28445 (PDF Sections II–III examined).

[2] T. D. Keidar, O. Blumer, B. Hirshberg, S. Reuveni, *Adaptive resetting for informed search strategies and the design of non-equilibrium steady-states*, Nature Communications 16, 7259 (2025); https://doi.org/10.1038/s41467-025-62398-2 (accessible open full PDF examined).

[3] F. Mori, K. S. Olsen, S. Krishnamurthy, *Entropy production of resetting processes*, Physical Review Research 5, 023103 (2023); arXiv:2211.15372; https://doi.org/10.1103/PhysRevResearch.5.023103 (open full PDF examined).

[4] D. B. K. Chu, R. Goerlich, I. Steinitz, Y. Roichman, B. Hirshberg, *Bypassing the Entropy Production Speed Limit of State-to-State Transitions with Adaptive Resetting*, arXiv:2611.22712, first public November 17, 2026; https://arxiv.org/abs/2611.22712 (including Supplemental Sections S2–S3 examined; supporting comparison, not the date-eligible initiating source).

[5] *Exact Gaussian stationary-state engineering by non-Gaussian stochastic resets*, published published-finding corpus research record 2026/11/2, identifier `08050fc52754`; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-gaussian-stationary-state-engineering-by-non-gaussian-stoc--08050fc52754 (available claim/summary compared).

[6] *A unique reset-cadence reversal and a logarithmic temperature frontier for Gaussian reset cycles*, published published-finding corpus research record 2026/11/2, identifier `31e22fdf4f67`; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-unique-reset-cadence-reversal-and-a-logarithmic-temperature-fr--31e22fdf4f67 (available claim/summary compared).
