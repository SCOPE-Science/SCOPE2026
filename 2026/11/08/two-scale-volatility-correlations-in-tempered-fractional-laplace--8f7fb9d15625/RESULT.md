# Two-scale volatility correlations in tempered fractional Laplace motion

## Finding

Consider the gamma-clock, quenched-gamma-diffusivity, exponentially tempered Gaussian transport process defined below. For a window length \(L>0\) and a nonoverlapping observation gap \(g\geq0\), let
\[
A_L=X(L)-X(0),\quad B_{L,g}=X(2L+g)-X(L+g),\quad R(L,g)=\operatorname{Corr}(A_L^2,B_{L,g}^2).
\]
For every \(L>0\), the function \(g\mapsto R(L,g)\) is **strictly decreasing**, but approaches a **strictly positive** limit \(R(L,\infty)\). For fixed physical parameters, the following **gap-uniform** asymptotic is valid:
\[
\boxed{R(L,g)=\frac{1}{2\alpha+3}-\frac{3(\alpha+1)}{(2\alpha+3)^2\eta L}+O(L^{-2}),\qquad L\longrightarrow\infty,\quad g\geq0.}
\]
In particular, the plateau depends on the fixed-per-trajectory diffusivity shape \(\alpha\), and its first correction depends on the gamma-clock rate \(\eta\), but neither depends on the Hurst parameter \(H\), tempering time \(\tau\), diffusivity scale \(\beta\), or the separation \(g\). Here the remainder is bounded uniformly over *all* \(g\geq0\), even when \(g\) depends on \(L\).

At the next order the temporal memory reappears. Set
\[
a=\Gamma(2H+1)\tau^{2H-1},\qquad
\rho(z)=2\int_z^\infty(u-z)H(2H-1)u^{2H-2}e^{-u/\tau}\,du.
\]
If \(Z_g\sim\operatorname{Gamma}(\eta g,\text{rate }\eta)\), with \(Z_0=0\), then for each fixed \(g\geq0\),
\[
\boxed{\lim_{L\to\infty}L^2\bigl[R(L,g)-R(L,\infty)\bigr]
=\frac{\alpha+1}{2(2\alpha+3)a^2}\,\mathbb E\rho(Z_g)^2.}
\]
This limit is strictly positive for every finite gap and decreases strictly to zero as \(g\to\infty\). In particular, the adjacent-window excess satisfies
\[
\boxed{\lim_{L\to\infty}L^2\bigl[R(L,0)-R(L,\infty)\bigr]
=\frac{(\alpha+1)(2H-1)^2\tau^2}{2(2\alpha+3)}.}
\]
These statements are parts of one two-scale correlation theorem, not claims about independent samples of the random diffusivity.

## Assumptions and scope

Fix \(1/2<H\leq1\), \(\tau>0\), \(\eta>0\), \(\alpha>0\), and \(\beta>0\). Write
\[
C_H(u)=H(2H-1)u^{2H-2}e^{-u/\tau}\quad(u>0),
\qquad v(s)=2\int_0^s(s-u)C_H(u)\,du.
\]
Let \(B\) be a centered Gaussian process with stationary increments, \(B(0)=0\), and increment variance \(\mathbb E[B(s)-B(t)]^2=v(|s-t|)\). Such a process exists: for \(H<1\), \(C_H(|u|)\) is a positive mixture of exponential covariance kernels; for \(H=1\), it is an exponential covariance kernel. Integrability of \(C_H\) at zero makes the integrated process well defined.

Let \(S\) be an independent gamma Lévy subordinator with \(S(t)\sim\operatorname{Gamma}(\eta t,\text{rate }\eta)\), giving \(\mathbb ES(t)=t\) and \(\operatorname{Var}S(t)=t/\eta\). Independently sample \(D\sim\operatorname{Gamma}(\alpha,\text{scale }\beta)\) **once per entire path**, and define \(X(t)=\sqrt D\,B(S(t))\). The same \(D\) must be retained across both observation windows. The gamma clock and Gaussian parent remain independent of \(D\). At \(g=0\), the clock increment across the gap is identically zero. The notation \(R(L,\infty)\) always means \(\lim_{g\to\infty}R(L,g)\), not an extra observation at infinite time.

The primary mathematical classification is MSC2020 82C31 (stochastic methods in time-dependent statistical mechanics). This is an exact model-specific theorem; no inference about empirical measurement noise or time-varying individual diffusivity is made.

## Proof

**1. Conditional fourth moments.** Let \(U,V\) be independent copies of \(S(L)\), let \(Z\) have the law of \(S(g)\), and take all three independent. Define the nonnegative parental covariance
\[
c(u,z,w)=\int_0^u\!\int_0^w C_H(z+s+t)\,dt\,ds.
\]
Conditional on \(D,U,Z,V\), the two increments are jointly centered Gaussian, with variances \(Dv(U)\), \(Dv(V)\), and covariance \(Dc(U,Z,V)\). This follows by stationarity of the Gaussian noise and independence of the gamma-clock increments. Put
\[
M_L=\mathbb Ev(U),\qquad N_L=\mathbb Ev(U)^2,\qquad K_{L,g}=\mathbb Ec(U,Z,V)^2.
\]
Isserlis' identity yields
\[
\operatorname{Cov}(A_L^2,B_{L,g}^2)=\operatorname{Var}(D)M_L^2+2\mathbb E[D^2]K_{L,g},
\]
\[
\operatorname{Var}(A_L^2)=3\mathbb E[D^2]N_L-(\mathbb ED)^2M_L^2.
\]
The two squared-window variances are identical. Since \(\mathbb ED=\alpha\beta\), \(\operatorname{Var}D=\alpha\beta^2\), and \(\mathbb E[D^2]=\alpha(\alpha+1)\beta^2\), division gives the **exact finite-window identity**
\[
\boxed{R(L,g)=\frac{M_L^2+2(\alpha+1)K_{L,g}}{3(\alpha+1)N_L-\alpha M_L^2}.}\tag{1}
\]
The denominator is positive because it is proportional to \(\operatorname{Var}(A_L^2)\), which is strictly positive. Equation (1) also proves cancellation of \(\beta\).

**2. Strict gap monotonicity and the floor.** The kernel \(C_H(u)\) is strictly positive and strictly decreasing for every \(u>0\). Consequently, \(c(u,z,w)>0\) and is strictly decreasing in \(z\) when \(u,w>0\). Gamma increments can be coupled as \(Z_{g_2}=Z_{g_1}+Z_{g_2-g_1}\), with the added increment strictly positive almost surely for \(g_2>g_1\). Thus \(K_{L,g}\) and \(R(L,g)\) strictly decrease with \(g\). Since
\[
0<c(u,z,w)\leq\int_0^\infty\!\int_0^\infty C_H(z+s+t)\,dt\,ds=\rho(z)/2
\]
and \(\rho(z)\to0\), dominated convergence gives \(K_{L,g}\to0\) as \(g\to\infty\). Therefore
\[
R(L,\infty)=\frac{M_L^2}{3(\alpha+1)N_L-\alpha M_L^2}>0.
\]
Notice that the established one-window kurtosis \(\kappa_L=3(\alpha+1)N_L/(\alpha M_L^2)\) gives \(R(L,\infty)=1/[\alpha(\kappa_L-1)]\). The far-gap floor alone is therefore not asserted as novel independently of the earlier kurtosis result.

**3. Gamma-clock asymptotics and gap uniformity.** Direct integration gives
\[
a=2\int_0^\infty C_H(u)\,du=\Gamma(2H+1)\tau^{2H-1},\quad
b=2\int_0^\infty uC_H(u)\,du=a(2H-1)\tau.
\]
Splitting these integrals at \(s\) yields the *exact* identity \(v(s)=as-b+\rho(s)\). Exponential tempering implies \(0<\rho(s)\leq C e^{-s/(2\tau)}\) for a finite parameter-dependent constant \(C\). The gamma Laplace transform and its first derivative give
\[
\mathbb Ee^{-qS(L)}=\left(\frac{\eta}{\eta+q}\right)^{\eta L},\qquad
\mathbb E[S(L)e^{-qS(L)}]=L\frac{\eta}{\eta+q}\left(\frac{\eta}{\eta+q}\right)^{\eta L}.
\]
For some \(c>0\), this proves \(M_L=aL-b+O(e^{-cL})\) and
\[
N_L-M_L^2=a^2L/\eta+O(Le^{-cL}).
\]
Moreover, the bound from step 2 gives \(0\leq K_{L,g}\leq b^2/4\), independently of \(g\). Inserting these estimates into (1), with \(k=2\alpha+3\), yields uniformly in every \(g\geq0\),
\[
R(L,g)=\frac{M_L^2+O(1)}{kM_L^2+3(\alpha+1)a^2L/\eta+O(Le^{-cL})}
=\frac1k-\frac{3(\alpha+1)}{k^2\eta L}+O(L^{-2}).
\]
No finite numerical enumeration is used in this asymptotic argument.

**4. The next-order gap signal.** Couple \(U=S_1(L)\) and \(V=S_2(L)\) using two independent gamma subordinators, and keep \(Z=S_3(g)\) independent. As \(L\to\infty\), both \(U\) and \(V\) tend to infinity almost surely. Monotone convergence for the parental covariance integral, followed by bounded convergence, gives
\[
K_{L,g}\longrightarrow\frac14\mathbb E\rho(Z_g)^2
\]
for each fixed \(g\). The exact difference of (1) from its far-gap limit is \(2(\alpha+1)K_{L,g}/[3(\alpha+1)N_L-\alpha M_L^2]\). Its denominator divided by \(L^2\) tends to \((2\alpha+3)a^2\), proving the boxed second-order result. At \(g=0\), \(\rho(0)=b\), so the coefficient becomes \((\alpha+1)(b/a)^2/[2(2\alpha+3)]\). Strict decay to zero with \(g\) follows from the strict decrease of \(\rho\) and the gamma subordinator coupling. This completes the proof.

## Verification

The accompanying standard-library Python 3 program `verify.py` independently evaluates the exact \(H=1\) special case over a parameter grid, including the conditional covariance identity, strict gap ordering, the universal first correction, the next-order gap contrast, and the far-gap kurtosis relation. It reports 846 bounded deterministic numerical and algebraic checks. In that special case,
\[
C_H(u)=e^{-u/\tau},\qquad v(s)=2\tau\bigl[s-\tau(1-e^{-s/\tau})\bigr],\quad c(u,z,w)=\tau^2(1-e^{-u/\tau})(1-e^{-w/\tau})e^{-z/\tau},
\]
so every clock average in (1) is expressible using \(\mathbb Ee^{-qS(L)}\). The program does not prove the full \(1/2<H\leq1\) theorem; that proof is in the preceding section. Run with `python3 verify.py`.

## Relationship to prior work

Zhao, Wang and Metzler (2026) introduced this three-component model (gamma clock, tempered fractional Gaussian parent, gamma-distributed quenched diffusivity) and obtained the one-time MSD, kurtosis, non-Gaussianity parameter and displacement density. The present theorem uses those model definitions; it does **not** claim them as new. The one-window kurtosis already determines the far-gap floor by the elementary identity in proof step 2. What is added is the exact joint fourth-order *two-window* identity, strict separation law, gap-uniform \(L^{-1}\) correction, and the \(L^{-2}\) residual-memory profile.

Wang and Chen (2020) derive general superstatistical ergodicity-breaking and time-averaged-MSD fluctuations; this establishes the relevance of permanent diffusivity heterogeneity, but gives neither the present tempered gamma-clock two-window formula nor the quantified gap correction. Wang, Liang, Chechkin and Metzler (2024) study untempered gamma-subordinated fractional Brownian motion with drift, without the static gamma-diffusivity mixture of the present theorem. Wang and collaborators (2025) study linear increment autocovariances for different fractional Brownian *diffusing-diffusivity* constructions, rather than the squared-increment covariance of this quenched-diffusivity, tempered gamma-clock model.

## Limitations

The results require \(H>1/2\), finite positive \(\tau\), a gamma Lévy clock with stationary independent increments, and a single shared per-trajectory diffusivity. They do not cover antipersistent fractional noise, a diffusivity resampled between windows, an arbitrary time-dependent diffusivity, localization error, or experimental finite-ensemble bias. The expansion is uniform in observation-gap length for **fixed** model parameters; its constants are not asserted uniform as \(H\downarrow1/2\), \(\tau\to\infty\), or \(\alpha\to\infty\). The new multi-window formulas are analytically derived consequences of the specified stochastic model, not claims of independent experimental verification or absolute publication priority.

## References

- Y. Zhao, W. Wang and R. Metzler, *Non-Gaussian transport in tempered fractional Laplace motion*, arXiv:2610.40113v1 (first public 2026-10-29), https://arxiv.org/html/2610.40113v1 .
- X. Wang and Y. Chen, *Ergodic property of Langevin systems with superstatistical, uncorrelated or correlated diffusivity*, arXiv:2011.06500v1 (2020), https://arxiv.org/html/2011.06500v1 .
- W. Wang, Y. Liang, A. V. Chechkin and R. Metzler, *Paradoxical non-Gaussian behavior in fractional Laplace motion with drift*, arXiv:2412.14674v1 (2024), https://arxiv.org/html/2412.14674v1 .
- W. Wang, Q. Wei, A. V. Chechkin and R. Metzler, *Different behaviors of diffusing diffusivity dynamics based on three different definitions of fractional Brownian motion*, arXiv:2504.19190v1 (first public 2025-04-27), https://arxiv.org/html/2504.19190v1 .
