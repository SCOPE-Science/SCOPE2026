# Global boundary convergence and critical extinction amplitudes in a fully separated consumer–resource model

## Finding

In the deterministic one-resource model with fixed full local separation, **every strictly positive trajectory converges to the noninvasible equilibrium even when some consumers are absent at that equilibrium**. This includes neutral invasion boundaries, where the marginal consumer decays as \(1/\tau\). Its abundance and the first-order shifts of its local nutrient and the shared nutrient have explicit amplitudes, independent of the positive initial condition.

Fix \(S\ge2\) and positive \(\gamma,R_0,\beta,\alpha_i,k_i\), with distinct break-even levels \(0<c_1<\cdots<c_S<R_0\) and \(c_i=k_i/\alpha_i\). For \(i=1,\ldots,S\), let \(N_i,T_i\) be the consumer abundance and local nutrient; \(R\) is the shared nutrient. In dimensionless time \(\tau\), let
\[
\dot N_i=(\alpha_iT_i-k_i)N_i,\qquad
\dot T_i=\beta(R-T_i)-\gamma\alpha_iT_i N_i,\qquad
\dot R=R_0-R-\beta\sum_i(R-T_i).
\]
For all initial coordinates strictly positive, the limiting state is
\[
R^*=r,\quad t_i:=T_i^*=\min(c_i,r),\quad N_i^*=\frac{\beta(r-c_i)_+}{\gamma k_i},
\qquad r+\beta\sum_i(r-c_i)_+=R_0.
\]
Here \(r\) is unique and in \((c_1,R_0)\), and any absent equilibrium consumer has nonpositive invasion exponent \(\alpha_i r-k_i\).

For \(j=2,\ldots,S\), define the stationary threshold \(\beta_j=(R_0-c_j)/\sum_{i<j}(c_j-c_i)\). At \(\beta=\beta_j\), the equilibrium is on the boundary and \(r=c_j\). For every strictly positive trajectory at that threshold,
\[
\lim_{\tau\to\infty}\tau N_j(\tau)=
\frac{1}{\gamma\alpha_j^2c_j\left(\beta_j^{-1}+[1+\beta_j(j-1)]^{-1}\right)},
\qquad
\lim_{\tau\to\infty}\tau(T_j-c_j)=-\frac1{\alpha_j},\qquad
\lim_{\tau\to\infty}\tau(R-c_j)=-\frac{\beta_j}{\alpha_j(1+j\beta_j)}.
\]
At strictly noncritical rates \(\beta>\beta_j\), species \(j\) instead has \(\lim_{\tau\to\infty}\tau^{-1}\log N_j=\alpha_j(r-c_j)<0\); for \(\beta<\beta_j\) it has a positive limiting abundance.

## Assumptions and scope

These are the single-nutrient equations (3)–(5) of [1] at fixed full isolation \(\theta_i=1\): only nutrient moves between the global supply pool and each niche. The time and biomass units are those of the model, including the conversion factor \(\gamma\). The supply \(R_0\) is constant. Distinct break-even levels ensure only one zero-invasion consumer at a threshold. No stochastic forcing, other nutrients, nonlinear uptake, consumer migration, partial or adaptive isolation, or initial face with an absent consumer is included.

## Proof

**Stationary bookkeeping.** Write \(x_i=\gamma N_i\). A resident consumer fixes \(T_i=c_i\), while an absent consumer has \(T_i=R\) and is noninvasible if \(R\le c_i\). Local balances give \(x_i^*=\beta(r-c_i)_+/k_i\); substitution in the shared balance gives the equation for \(r\), whose left hand side strictly increases in \(r\). At \(r=c_1\) it is less than \(R_0\), and at \(r=R_0\) it is greater. The root decreases strictly as \(\beta\) increases. In the supply-threshold notation of [2], \(C_j=c_j+\beta\sum_{i<j}(c_j-c_i)\) at full isolation, so solving \(R_0=C_j\) gives exactly \(\beta_j\). The numerator of \(\beta_j\) decreases with \(j\) and its positive denominator increases; hence \(0<\beta_S<\cdots<\beta_2\). These thresholds are setup for the dynamical result, not a new survivor staircase.

**Global convergence with vanishing consumers.** For \(a>0\) define \(\phi_a(z)=z-a-a\log(z/a)\); use \(\phi_0(z)=z\) on \(z\ge0\). Take
\[
\mathcal V=\phi_r(R)+\sum_i\phi_{t_i}(T_i)+\sum_i\phi_{x_i^*}(x_i).
\]
At a resident, adding the uptake term of the local nutrient entropy to the consumer-entropy derivative leaves \(-\alpha_i x_i^*(T_i-t_i)\), since \(k_i=\alpha_i t_i\). At an absent consumer the analogous sum is \((\alpha_i r-k_i)x_i\). Use the local identity \(\alpha_i t_i x_i^*=\beta(r-t_i)\) and the shared identity \(R_0=r+\beta\sum_i(r-t_i)\). With \(a=R/r, b_i=T_i/t_i, d_i=t_i/r\), collecting the exchange terms gives
\[
\dot{\mathcal V}=-\frac{(R-r)^2}{R}
-\beta r\sum_i\left[d_i\left(\frac{b_i}{a}+\frac{a}{b_i}-2\right)
+(1-d_i)\left(\frac1a+\frac{a}{b_i}+b_i-3\right)\right]
+\sum_{i:x_i^*=0}(\alpha_i r-k_i)x_i.
\]
The two parentheses are nonnegative by AM–GM, since the products of the corresponding terms are one; the missing-species term is nonpositive. The resource equations have nonnegative inward forcing at zero and positive coordinates for finite times from positive data; each consumer solves a multiplicative scalar equation and stays positive at finite times. Sublevel sets bound all coordinates and bound every resource and each resident away from zero. They are compact and forward invariant in the enclosed nonnegative domain, with a smooth extension of \(\mathcal V\) there for each zero-reference consumer. Zero dissipation forces \(a=1\) from the shared term and then \(b_i=1\) for all \(i\), since \(d_i>0\) and \(b_i/a+a/b_i-2=(a-b_i)^2/(ab_i)\). Any orbit in that zero set also has constant local nutrients, forcing \(x_i=x_i^*\) via their equations even for a marginal species. LaSalle's principle yields the asserted global convergence. Taking the Cesàro limit of \((\log N_j)'=\alpha_j T_j-k_j\) gives the stated exponential rate when \(\beta>\beta_j\).

**Critical asymptotics for all positive orbits.** Fix the threshold \(\beta=\beta_j\), so \(r=c_j\); write \(y=x_j\) and let \(z\) denote deviations in all the remaining coordinates from equilibrium. The linearized subsystem on the face \(y=0\) is Hurwitz (its eigenvalues have strictly negative real parts). To see this, first omit the absent larger consumers, which are decoupled at linear order in their own equations and contribute the strictly negative eigenvalues \(\alpha_i r-k_i\), \(i>j\). In the subsystem consisting of all resources and resident consumers, the Hessian of \(\mathcal V\) is positive definite. Its quadratic time derivative is nonpositive and contains a negative multiple of \((R-r)^2\) and positive-weight negatives of the squared normalized nutrient differences \((a-b_i)^2\) to quadratic order. Hence a trajectory with zero quadratic dissipation has all resource deviations zero. The linearized local equations then force all resident consumer deviations zero. A positive definite quadratic Lyapunov function with this invariant zero set eliminates all linear modes with nonnegative real part.

Denote this stable face Jacobian, now including the larger consumers, by \(B\), and the linear forcing from \(y\) by a column vector \(b\). Smoothness gives locally
\[
\dot z=(B+E(z,y))z+(b+e(z,y))y,\qquad E(z,y)\to0,\quad e(z,y)\to0,
\]
by integrating the derivative along the segment from equilibrium. Along a positive trajectory \(y>0\) and \(\dot y/y=\alpha_j(T_j-r)\to0\). Consequently \(w=z/y\) solves \(\dot w=(B+o(1))w+b+o(1)\) and tends to \(-B^{-1}b\). Indeed a positive definite solution of \(B^{\mathsf T}P+PB=-I\) gives uniform exponential stability of the homogeneous equation after sufficiently large time, and the discrepancy from \(-B^{-1}b\) is forced by a term tending to zero. Thus this argument applies directly to the approaching orbit without assuming it lies on a chosen center manifold.

The vector \((y=1,z=-B^{-1}b)\) solves the zero-eigenvalue equations. They give \(\delta T_i=0\) for \(i<j\), \(\delta x_i=0,\ \delta T_i=\delta R\) for \(i>j\), and \(\delta T_j=\delta R-\alpha_j r/\beta\). Substituting these relations into the shared balance gives
\[
\delta R=-\frac{\alpha_j r}{1+\beta(j-1)},\qquad
\delta T_j=-\alpha_j r\left(\frac1\beta+\frac1{1+\beta(j-1)}\right).
\]
It follows that \((1/y)'=-\alpha_j (T_j-r)/y\to C=-\alpha_j\delta T_j>0\), and hence \(\tau y\to1/C\). Using \(N_j=y/\gamma\), \(\tau(T_j-r)\to\delta T_j/C\), and \(\tau(R-r)\to\delta R/C\) gives all three amplitudes.

## Relationship to other results and limitations

ElGamel–Mugler [1] introduce the model and treat two-species stationary coexistence in supplementary equations (S15)–(S24). The survivor staircase is already available as a supply-entry criterion in [2], which covers a broader range of fixed common isolation fractions away from its thresholds. The entropy convergence result [3] applies in a broader fixed-isolation model under the hypothesis of a strictly positive stationary state. The contribution here is the extension to equilibrium faces with missing consumers, including at a zero invasion exponent, and the universal marginal abundance and nutrient amplitudes. Related chemostat results include [4], whose strict parameter conditions and single shared resource with intraspecific competition do not yield the local-nutrient critical law here. The conclusions are not empirical forecasts or stochastic times to extinction; the literature comparison is bounded, including older compartmental work not all accessible in full.

## References

1. ElGamel and Mugler, *Spatial structure promotes coexistence, resilience, and synergy in microbial communities*, [arXiv:2611.00222v1](https://arxiv.org/html/2611.00222v1), Eqs. (3)–(5) and Supplement §VI.
2. [*Sharp survivor staircases and a resource ceiling in a shared-local nutrient model*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-sharp-survivor-staircases-and-a-resource-ceiling-in-a-shared-loc--44e97c901f6c/RESULT.md), Finding and model assumptions.
3. [*Global coexistence rigidity for spatially compartmentalized consumer–resource systems*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-global-coexistence-rigidity-for-spatially-compartmentalized-cons--a1b3ab5c3a1b/RESULT.md), Finding and entropy proof.
4. Abdellatif, Fekih-Salem and Sari, *Competition for a single resource and coexistence of several species in the chemostat*, [DOI:10.3934/mbe.2016012](https://doi.org/10.3934/mbe.2016012), Proposition 7.
