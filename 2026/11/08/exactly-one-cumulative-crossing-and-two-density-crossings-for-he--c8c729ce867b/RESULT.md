# Universal weak-disorder crossing times for quenched Brownian first passage

## Finding
Fix a distance \(x>0\) and a mean diffusivity \(\mu>0\). Let \(Z\) be any bounded, nonconstant real random variable with \(\mathbb E[Z]=0\), and set \(D_\varepsilon=\mu(1+\varepsilon Z)\) for sufficiently small positive \(\varepsilon\) such that \(D_\varepsilon>0\). At time zero independently sample \(D_\varepsilon\) and hold it fixed throughout a one-dimensional Brownian path \(x+\sqrt{2D_\varepsilon}B_t\), absorbed on reaching zero. Compare its first-passage distribution with that of the constant-diffusivity process at \(\mu\).

Write \(t_1(\varepsilon)<t_2(\varepsilon)\) for the two positive crossings of the first-passage *density* functions, and \(t_c(\varepsilon)\) for the single positive crossing of the cumulative first-passage distributions. Their existence, uniqueness, and order \(t_1<t_c<t_2\) follow from the previously established general crossing theorem for static diffusivity mixtures and are **not claimed as new** here. The quantitative weak-disorder conclusion is
\[
\boxed{\begin{aligned}
\lim_{\varepsilon\downarrow0}t_1(\varepsilon)
 &=\frac{x^2}{2\mu(3+\sqrt6)},\\
\lim_{\varepsilon\downarrow0}t_c(\varepsilon)
 &=\frac{x^2}{6\mu},\\
\lim_{\varepsilon\downarrow0}t_2(\varepsilon)
 &=\frac{x^2}{2\mu(3-\sqrt6)}.
\end{aligned}}
\]
All three constants are independent of the law of \(Z\) apart from boundedness, nondegeneracy, and centering. The common cumulative absorption probability at the middle crossing tends to \(\operatorname{erfc}(\sqrt{3/2})\); the common survival probability tends to \(\operatorname{erf}(\sqrt{3/2})\). The leading law is independent of the variance of \(Z\), although that variance controls the vanishing amplitude of the difference.

## Hypotheses and interpretation
The diffusion coefficient is sampled once, not refreshed along a path. The comparator uses the same arithmetic mean \(\mu\), which is constant in \(\varepsilon\). The target is the absorbing origin of a half-line, the Brownian generator is \(D\partial_{xx}\), and the crossing times are strictly positive finite zeros. The theorem asserts limits of the *locations* of crossings as \(\varepsilon\to0+\); it does not assert that the crossing distributions remain different at \(\varepsilon=0\), where they coincide identically. Nothing is claimed for unbounded \(Z\), changing mean, or time-fluctuating diffusivity.

## Proof
For each \(D>0\), the reflection principle gives
\[
F_D(t)=\operatorname{erfc}\left(\frac{x}{2\sqrt{Dt}}\right),\qquad
f_D(t)=\frac{x}{\sqrt{4\pi t^3}}D^{-1/2}\exp\left(-\frac{x^2}{4Dt}\right).
\]
Thus the heterogeneous laws are expectations of these expressions over \(D_\varepsilon\). Set \(s=x^2/(4t)\) and define
\[
K_\varepsilon(s)=\mathbb E\left[D_\varepsilon^{-1/2}
\exp\left(s\left(\mu^{-1}-D_\varepsilon^{-1}\right)\right)\right]-\mu^{-1/2}.
\]
The density difference has the same sign as \(K_\varepsilon(s)\). For every nondegenerate positive bounded diffusivity law, \(K_\varepsilon(0)>0\) by strict Jensen convexity, \(K_\varepsilon(s)\to\infty\) as \(s\to\infty\) because positive mass lies above its mean, and \(K_\varepsilon''(s)>0\). The cumulative difference is positive at sufficiently short times and negative at sufficiently long times (the former from mass above \(\mu\) and exponential tails, the latter from strict Jensen applied to \(D^{-1/2}\)). Its derivative is therefore negative somewhere, forcing \(K_\varepsilon\) to be negative at an interior point. Strict convexity yields exactly two simple positive density roots and exactly one cumulative crossing between them. These structural facts, including their stronger arbitrary-positive-law form, were proved previously in *A unique Brownian first-passage crossover for every static diffusivity mixture* (2026-11-08); they are recalled to justify the asymptotic root labels, not presented as new conclusions.

For the *new quantitative limit*, put \(a=s/\mu\). Since \(Z\) is bounded and \(\mathbb E Z=0\), the Taylor expansion
\[
(1+\varepsilon Z)^{-1/2}
\exp\left[a\left(1-(1+\varepsilon Z)^{-1}\right)\right]
=1+\varepsilon Z\left(a-\frac12\right)
+\frac{\varepsilon^2Z^2}{2}\left(a^2-3a+\frac34\right)+O(\varepsilon^3)
\]
is uniform for \(s\) on compact subsets of \([0,\infty)\). Therefore
\[
\frac{K_\varepsilon(s)}{\varepsilon^2}
\longrightarrow \frac{\operatorname{Var}(Z)}{2\sqrt\mu}
\left[\left(\frac{s}{\mu}\right)^2-3\frac{s}{\mu}+\frac34\right]
\quad\text{uniformly on compact }s\text{-sets}.
\]
The limiting quadratic has two distinct, simple positive zeros \(s_\pm=\mu(3\pm\sqrt6)/2\), and the limiting signs alternate across them. Continuity and uniform convergence give one \(K_\varepsilon\) root near each \(s_\pm\) for sufficiently small \(\varepsilon>0\). The preceding strict-convexity theorem excludes any additional roots, so both roots converge to their corresponding \(s_\pm\). Time reverses inverse-time order: \(t_1=x^2/(4s_+)\), \(t_2=x^2/(4s_-)\). These identities yield the first and third limits.

For the cumulative crossing write \(z=x/(2\sqrt t)\), and define \(g_z(u)=\operatorname{erfc}(z/\sqrt u)\). Direct differentiation gives
\[
g_z''(u)=\frac{z(2z^2-3u)}{2\sqrt\pi\,u^{7/2}}e^{-z^2/u}.
\]
On a nonconstant distribution supported inside \([d_-,d_+]\), strict Jensen convexity/concavity yields the previously established crossing bracket
\[
\frac{x^2}{6d_+}<t_c<\frac{x^2}{6d_-}.
\]
For \(D_\varepsilon=\mu(1+\varepsilon Z)\), both essential endpoints converge to \(\mu\). Squeezing the unique crossing proves \(t_c(\varepsilon)\to x^2/(6\mu)\). The common probability at that time is the continuous constant-law limit \(F_\mu(x^2/(6\mu))=\operatorname{erfc}(\sqrt{3/2})\). This completes the proof. \(\square\)

## Verification and limitations
The original `verify_crossings.py` checks the kernel derivatives and representative finite-mixture crossing geometry. An independent numerical comparison for symmetric two-point laws \(D=\mu(1\pm\varepsilon)\) at \(\mu=x=1\) confirms convergence of all three time locations to the stated constants. These finite checks corroborate the proof but are not an unrestricted argument.

The earlier 2026 general theorem already supplies single cumulative crossing, exactly two density crossings, the full time sign pattern, and the strict support bracket, under *weaker* assumptions than used here. These facts are not new in this revised result. The surviving contribution is the universal **three-location weak-disorder asymptotic**, which isolates the natural first-passage time scale at which small quenched heterogeneity reverses its advantage, as well as the two universal density boundaries surrounding it. The result does not establish higher-order corrections, finite-\(\varepsilon\) universality, or historical priority over all unindexed perturbative analyses.

## References
1. *A unique Brownian first-passage crossover for every static diffusivity mixture* (2026-11-08), complete theorem and proof, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-a-unique-brownian-first-passage-crossover-for-every-static-diffu--ef2108b88c43 .
2. G. Uchida, H. Miyoshi, H. Washizu, *First passage time properties of diffusion with a broad class of stochastic diffusion coefficients*, arXiv:2502.20705; Phys. Rev. E 113, 064108 (2026), https://arxiv.org/html/2502.20705v2 .
3. V. Sposini et al., *Being heterogeneous is disadvantageous: Brownian non-Gaussian searches*, Phys. Rev. E 109, 034120 (2024), https://arxiv.org/html/2403.10138v1 .
