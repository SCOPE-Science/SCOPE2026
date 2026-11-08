# Exactly one cumulative crossing and two density crossings for heterogeneous Brownian first passage

## Finding

Let a one-dimensional particle start at distance \(x>0\) from an absorbing origin. Its diffusion coefficient \(D\) is independently sampled once at initialization and then held fixed. Assume \(0<d_-\leq D\leq d_+<\infty\) almost surely and \(D\) is nonconstant, where \(d_-\) and \(d_+\) are its essential extrema. Write \(\mu=\mathbb E[D]\). Compare its first hitting time \(T_D\) with \(T_\mu\), the first hitting time of Brownian motion with the fixed coefficient \(\mu\).

**Exact crossing classification.** The difference of the first-passage densities \(f_D(t)-f_\mu(t)\) has exactly two positive zeros \(0<t_1<t_2\), both simple, and has the chronological signs \(+,-,+\). The difference of absorption probabilities \(F_D(t)-F_\mu(t)\) has exactly one positive zero \(t_c\), with
\[
 t_1<t_c<t_2,\qquad
 F_D(t)>F_\mu(t)\ (0<t<t_c),\qquad
 F_D(t)<F_\mu(t)\ (t>t_c).
\]
In particular, the heterogeneous population is ahead at short deadlines and behind at long deadlines, with no repeated reversal. The crossing is quantitatively bracketed by
\[
 \frac{x^2}{6d_+}<t_c<\frac{x^2}{6d_-}.
\]
All three times scale exactly as \(x^2\) under a change of initial distance.

**Universal weak-disorder positions.** For the family \(D_\varepsilon=\mu(1+\varepsilon Z)\), with a bounded nonconstant random variable \(Z\) satisfying \(\mathbb E Z=0\), \(\mu>0\), and sufficiently small \(\varepsilon>0\) so that \(D_\varepsilon>0\), the chronological crossings satisfy
\[
 \lim_{\varepsilon\downarrow0}t_1(\varepsilon)
 =\frac{x^2}{2\mu(3+\sqrt6)},\qquad
 \lim_{\varepsilon\downarrow0}t_c(\varepsilon)
 =\frac{x^2}{6\mu},\qquad
 \lim_{\varepsilon\downarrow0}t_2(\varepsilon)
 =\frac{x^2}{2\mu(3-\sqrt6)}.
\]
The common absorption probability at the cumulative crossing tends to \(\operatorname{erfc}(\sqrt{3/2})\), or equivalently the common survival probability tends to \(\operatorname{erf}(\sqrt{3/2})\). These limits do not depend on the law of \(Z\) beyond its boundedness, centering, and nondegeneracy.

## Assumptions and scope

The conditional dynamics are \(X_t=x+\sqrt{2D}\,B_t\), where \(B_t\) is standard Brownian motion and \(D\) is independent of the full Brownian path. For a fixed value of \(D\), the infinitesimal generator is \(D\partial_{xx}\). The target is the absorbing point zero on the half-line. The probability distribution of \(D\) may be continuous, atomic, or mixed; no density or symmetry of this distribution is assumed. The compact positive support hypothesis permits differentiation and endpoint asymptotics without extra integrability qualifications.

The standard reflection principle gives the exact, previously known mixture formulas
\[
 F_D(t)=\mathbb E\left[\operatorname{erfc}\left(\frac{x}{2\sqrt{Dt}}\right)\right],\quad
 F_\mu(t)=\operatorname{erfc}\left(\frac{x}{2\sqrt{\mu t}}\right),
\]
\[
 f_D(t)=\frac{x}{\sqrt{4\pi t^3}}\mathbb E\left[D^{-1/2}
 e^{-x^2/(4Dt)}\right],\quad
 f_\mu(t)=\frac{x}{\sqrt{4\pi t^3}}\mu^{-1/2}
 e^{-x^2/(4\mu t)}.
\]
For clarity, the claim concerns one particle per sampled environment, ensemble-averaged first-passage statistics, and a mean-matched *constant* comparator. It does not assert a single crossing for a diffusivity fluctuating in time along an individual trajectory.

## Proof

**1. Strict density sign structure.** Introduce the inverse-time variable \(s=x^2/(4t)\) and define
\[
 K(s)=\mathbb E\left[D^{-1/2}\exp\left(s\left(\frac1\mu-\frac1D\right)\right)\right]-\mu^{-1/2},\qquad s\geq0.
\]
The sign of \(f_D(t)-f_\mu(t)\) is exactly the sign of \(K(s)\). Since \(u\mapsto u^{-1/2}\) is strictly convex and \(D\) is nonconstant, Jensen's inequality gives
\[
 K(0)=\mathbb E[D^{-1/2}]-\mu^{-1/2}>0.
\]
Twice differentiating under the expectation gives
\[
 K''(s)=\mathbb E\left[D^{-1/2}\left(\frac1\mu-\frac1D\right)^2
 \exp\left(s\left(\frac1\mu-\frac1D\right)\right)\right]>0
\]
for all \(s\geq0\). The inequality is strict because a nonconstant \(D\) takes values other than its mean with positive probability. Moreover \(\Pr(D>\mu)>0\); restrict the expectation to \(D\geq\mu+\delta\) for some \(\delta>0\) with positive probability to see that \(K(s)\to\infty\) as \(s\to\infty\).

**2. One guaranteed negative interval.** Write \(z=\sqrt{s}\) and
\[
 \Delta(z)=\mathbb E\left[\operatorname{erfc}(z/\sqrt D)\right]
 -\operatorname{erfc}(z/\sqrt\mu),\qquad z\geq0.
\]
The expansion \(\operatorname{erfc}(v)=1-2v/\sqrt\pi+O(v^3)\), uniformly for \(v=z/\sqrt D\) under the support assumption, yields
\[
 \Delta(z)=-\frac{2z}{\sqrt\pi}
 \big(\mathbb E[D^{-1/2}]-\mu^{-1/2}\big)+O(z^3)<0
\]
for all sufficiently small positive \(z\). Conversely, since \(D>\mu+\delta\) with positive probability for a suitable \(\delta>0\), the standard Gaussian tail asymptotic for \(\operatorname{erfc}\) shows that the mixture tail for those environments eventually dominates the mean-diffusivity term; thus \(\Delta(z)>0\) for all sufficiently large \(z\). Here \(\Delta(0)=0\) and \(\Delta(z)\to0\) as \(z\to\infty\). Consequently \(\Delta'\) must be positive somewhere. But direct differentiation gives the exact identity
\[
 \Delta'(z)=-\frac2{\sqrt\pi}e^{-z^2/\mu}K(z^2),
\]
so \(K\) is negative at some positive argument.

By strict convexity, positivity at zero, divergence to positive infinity, and negativity somewhere between, \(K\) has exactly two distinct, simple positive roots \(0<s_1<s_2\). It is positive on \([0,s_1)\cup(s_2,\infty)\) and negative on \((s_1,s_2)\). Reversing the inverse-time order proves exactly two density crossings \(t_1=x^2/(4s_2)\) and \(t_2=x^2/(4s_1)\) with chronological signs \(+,-,+\).

**3. Unique cumulative crossing.** The derivative identity shows that \(\Delta\), in increasing \(z\), strictly decreases up to \(\sqrt{s_1}\), strictly increases between \(\sqrt{s_1}\) and \(\sqrt{s_2}\), and strictly decreases thereafter. In particular, its first local minimum is negative. Its later local maximum is positive because \(\Delta(z)>0\) at large \(z\) yet decreases to zero on the last interval. It follows that \(\Delta\) crosses zero **exactly once**, at a unique \(z_c\in(\sqrt{s_1},\sqrt{s_2})\). Returning to time with \(t_c=x^2/(4z_c^2)\) proves both the crossing inequalities and the chronological signs.

**4. A distribution-free crossing bracket.** For fixed \(z>0\), put \(g_z(u)=\operatorname{erfc}(z/\sqrt u)\). Two derivatives give
\[
 g_z''(u)=\frac{z(2z^2-3u)}{2\sqrt\pi\,u^{7/2}}e^{-z^2/u}.
\]
If \(z^2\geq3d_+/2\), then \(g_z\) is strictly convex across a nontrivial part of the support and Jensen's inequality gives \(\Delta(z)>0\). If \(z^2\leq3d_-/2\), it is strictly concave across a nontrivial part of the support and gives \(\Delta(z)<0\). By the already proved uniqueness,
\[
 \frac{3d_-}{2}<z_c^2<\frac{3d_+}{2},
\]
which is equivalent to the claimed time bracket.

**5. Weak-heterogeneity limits.** Let \(D_\varepsilon=\mu(1+\varepsilon Z)\). Its essential extrema approach \(\mu\) as \(\varepsilon\downarrow0\), so the time bracket immediately yields \(t_c(\varepsilon)\to x^2/(6\mu)\). The common cumulative survival probability follows by continuity. To find both density-crossing limits, put \(h_s(u)=u^{-1/2}e^{-s/u}\); Taylor expansion under the bounded expectation, with \(\mathbb E Z=0\), gives uniformly for \(s\) in compact sets,
\[
 \frac{K_\varepsilon(s)}{\varepsilon^2}
 \longrightarrow\frac{\operatorname{Var}(Z)}{2\sqrt\mu}
 \left[\left(\frac s\mu\right)^2-3\frac s\mu+\frac34\right].
\]
Indeed, \(h_s''(\mu)=h_s(\mu)\mu^{-2}[(s/\mu)^2-3s/\mu+3/4]\), with cancellation of the common \(e^{-s/\mu}\) factor in the definition of \(K\). The limiting polynomial has distinct positive roots \(\mu(3\pm\sqrt6)/2\), with opposite signs on the interval between them. Uniform convergence gives a root of \(K_\varepsilon\) near each root for all small \(\varepsilon\); the strict-convexity argument establishes that these are the only positive roots. Converting to time gives the announced two limits. Every step holds for any bounded nonconstant centered \(Z\).

## Verification

Run `python3 verify_crossings.py` with Python 3, NumPy, SciPy, and SymPy. The program independently differentiates the complementary-error-function expression symbolically, calculates the strict-convexity roots and the cumulative crossing numerically for a balanced two-diffusivity law, 180 seeded random atomic laws, and four Gauss–Legendre approximations of a uniform diffusivity law. The finite test suite passed **1,852** checks spanning 185 laws. All universal sign-count and limit statements above are proved analytically; representative finite calculations do not establish the infinite family theorem.

For \(\Pr(D=1)=\Pr(D=4)=1/2\), \(\mu=5/2\), and \(x=1\), numerical roots give \(t_1\approx0.04134906\), \(t_c\approx0.07643348\), and \(t_2\approx0.46169020\), correctly ordered and with \(1/24<t_c<1/6\).

## Relationship to prior work

Uchida, Miyoshi, and Washizu (first posted February 28, 2025) derive the general time-averaged-diffusivity complementary-error-function representation (their equation 18), establish early-arrival properties, and derive a crossover for **ergodic time-varying** diffusivity. That source supplies the basic representation, not the all-positive-time single crossing for **nonergodic quenched** laws or the exact two density crossings and weak-disorder thresholds proved here. Sposini, Chechkin, and Metzler (2018/2019) examine the survival crossover for a specific dynamically varying diffusivity model; this does not imply the claimed arbitrary-law theorem. Budini and Cáceres (2017) derive superstatistical first-passage statistics, not this crossing classification. Sposini and collaborators (2024) establish the early-search advantage for extreme searches among many independent particles in heterogeneous ensembles, a related but different observable. Lanoiselée, Moutal, and Grebenkov (2018) analyze diffusion-limited reactions under dynamic heterogeneity rather than static arbitrary-law exact crossing counts.

## Limitations

The diffusivity is sampled once and held constant throughout each trajectory. It is bounded strictly away from zero and infinity. For arbitrary unbounded or time-fluctuating diffusivities, derivatives, asymptotics, and sign counts can require different arguments or fail. The comparison is to the arithmetic-mean diffusivity, not to a matched harmonic mean or a time-dependent effective diffusivity. All mean first-passage times on this half-line are infinite, so this result is about deadline-dependent absorption and the full density, not a finite mean first-passage advantage. Originality is assessed against the inspected literature and accessible research records, not against an exhaustive independent publication-priority audit.

## References

1. G. Uchida, H. Miyoshi, and H. Washizu, *First passage time properties of diffusion with a broad class of stochastic diffusion coefficients*, arXiv:2502.20705, first public February 28, 2025. https://arxiv.org/abs/2502.20705
2. V. Sposini, A. V. Chechkin, and R. Metzler, *First passage statistics for diffusing diffusivity*, arXiv:1809.09186, first public September 24, 2018. https://arxiv.org/abs/1809.09186
3. A. A. Budini and M. O. Cáceres, *First passage time for superstatistical Fokker–Planck models*, arXiv:1712.04996, first public December 13, 2017. https://arxiv.org/abs/1712.04996
4. V. Sposini, S. Nampoothiri, A. Chechkin, E. Orlandini, F. Seno, and F. Baldovin, *Being Heterogeneous Is Advantageous: Extreme Brownian Non-Gaussian Searches*, arXiv:2403.10143, first public March 15, 2024. https://arxiv.org/abs/2403.10143
5. Y. Lanoiselée, N. Moutal, and D. S. Grebenkov, *Diffusion-limited reactions in dynamic heterogeneous media*, Nature Communications 9, 4398 (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC6199324/
