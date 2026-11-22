# Exact interior-launch Stratonovich diffusivity budget, monotone escape gain, and a half-budget boundary layer

## Finding

Write the reflecting endpoint as \(x=0\), the absorbing endpoint as \(x=\ell\), and the launch point as \(x=a\ell\), with \(0<a<1\) and \(b=1-a\). For any fixed mean diffusivity \(D_0>0\), the *exact global solution* to the diffusivity-budget problem has two levels. Let \(t>1\) denote the unique positive root of
\[
 b t^3-a t-b=0.
\]
The optimal interior and target-side diffusivities are respectively
\[
 D_{\rm in}=\frac{D_0}{a+b t^2},\qquad
 D_{\rm out}=\frac{D_0 t^2}{a+b t^2}.
\]
The corresponding normalized optimal mean absorption time is
\[
 \frac{D_0}{\ell^2}\inf_D \mathbb E_{a\ell}\tau
 =\frac{(2t^3-1)^2}{2(t^3+t-1)^3},\qquad
 a=\frac{t^3-1}{t^3+t-1}.
\]
The homogeneous reference time is \(\ell^2(1-a^2)/(2D_0)\). Its fractional optimal reduction
\[
 \eta(a)=1-\frac{\inf_D\mathbb E_{a\ell}\tau}{\ell^2(1-a^2)/(2D_0)}
\]
is strictly increasing over \(0<a<1\). Both endpoint laws are sharp:
\[
 \eta(a)\sim\frac{a^3}{3}\quad(a\downarrow0),\qquad
 1-\eta(a)\sim2\sqrt{1-a}\quad(a\uparrow1).
\]
The target-side interval consumes a fraction
\[
 \frac{bD_{\rm out}}{D_0}=\frac{t^3}{2t^3-1}>\frac12
\]
of the total diffusivity budget, tending to precisely one half as its relative width \(b\) vanishes. At this limit \(D_{\rm in}/D_0\to1/2\) and \(b D_{\rm out}/D_0\to1/2\).

## Assumptions and scope

Take a one-dimensional diffusion on the finite interval \([0,\ell]\), reflected at zero and killed at \(\ell\), with Stratonovich prescription and no imposed drift. For positive measurable diffusivity \(D\) with \(\int_0^\ell D(x)\,dx=\ell D_0\) and \(\int_0^\ell D(x)^{-1/2}\,dx<\infty\), define the process through the strictly increasing intrinsic coordinate \(s(x)=\int_0^x D(y)^{-1/2}\,dy\), which turns it into reflected, absorbed Brownian motion with generator \(\partial_s^2\). This specifies the physical transmission convention at a discontinuity. Piecewise constant diffusivity is admitted and unique up to null sets; if smooth diffusivity is required, the same value is a sharp approximable infimum. The launch position is strictly between the endpoints; limits at endpoints are one-sided and do not assert finite positive profiles at \(a=1\).

## Proof

1. **Exact first-passage reduction.** In the intrinsic coordinate, the mean time to reach the absorbing endpoint starting at \(s_0=s(a\ell)\), with reflecting point zero, solves \(u''=-1\), \(u'(0)=0\), \(u(s_\ell)=0\). Therefore \(\mathbb E\tau=[s_\ell^2-s_0^2]/2\). Introduce the normalized interval lengths \(a,b\), let \(z(y)=D(\ell y)/D_0\) for \(0\le y\le1\), and set \(S_1=\int_0^a z(y)^{-1/2}dy\) and \(S_2=\int_a^1 z(y)^{-1/2}dy\). The dimensionless time is exactly \(S_1S_2+S_2^2/2\).

2. **Global reduction to two levels.** Let \(u\) and \(v\) be the mean normalized diffusivities on the two subintervals. The budget is \(au+bv=1\). Strict Jensen convexity of \(z\mapsto z^{-1/2}\) gives \(S_1\ge a/\sqrt u\) and \(S_2\ge b/\sqrt v\), with simultaneous equality if and only if \(z\) is constant separately on both intervals. As the exact time is strictly increasing in each positive \(S_i\), every non-two-level profile is strictly suboptimal relative to its associated two-level profile. This proves global reduction without relying merely on a stationarity equation.

3. **Unique two-level minimizer.** Parameterize \(t=\sqrt{v/u}>0\); the budget requires \(u=(a+bt^2)^{-1}\) and \(v=t^2/(a+bt^2)\). The dimensionless time becomes
\[
 F(t)=(a+bt^2)\left(\frac{ab}{t}+\frac{b^2}{2t^2}\right),\qquad
 F'(t)=\frac{ab}{t^3}(bt^3-at-b).
\]
The cubic is negative at zero and at one, has exactly one positive zero by its one-valley derivative, and is eventually positive; consequently that zero is greater than one and is the unique global minimizer. The divergence of \(F(t)\) at both zero and infinity excludes missing boundary minimizers. Substituting the cubic gives \(a=(t^3-1)/(t^3+t-1)\), \(b=t/(t^3+t-1)\) and the stated normalized minimum.

4. **Strict gain law.** Set \(K=t^3+t-1\) and
\[
 R(t)=1-\eta=\frac{(2t^3-1)^2}{t(2t^3+t-2)K}.
\]
Direct differentiation and factorization yield
\[
 R'(t)=-\frac{(t-1)^2(2t^3-1)(2t^3+1)\bigl(2t^4+4t^3+3t^2+2t-2\bigr)}{t^2 K^2(2t^3+t-2)^2}<0
\]
for every \(t>1\). Indeed the quartic factor is at least its value nine at \(t=1\), while all other denominator and numerator factors have the displayed signs. Since \(a'(t)=(2t^3+1)/K^2>0\), \(\eta\) is strictly increasing in the original launch fraction.

5. **Endpoint and budget limits.** At \(t\downarrow1\), exact series give \(1-R(t)=9(t-1)^3+O((t-1)^4)\) and \(a=3(t-1)+O((t-1)^2)\), hence \(\eta\sim a^3/3\). At \(t\to\infty\), \(b=t/K\sim t^{-2}\) and \(R(t)\sim2/t\), giving \(1-\eta\sim2\sqrt b\) and \(F(t)\sim2b^{3/2}\). Finally \(b v=t^3/(2t^3-1)\) and \(a u=(t^3-1)/(2t^3-1)\), proving the sharp half-budget split.

## Verification

Execute the standalone file `check.py` with Python 3, SymPy and SciPy installed: `python check.py`. It checks all exact derivative and rational identities, both endpoint constants, 11 independent numeric scalar optimizations, and 330 random heterogeneous-profile comparisons with the analytic global minimum. Numerical checks are auxiliary; the preceding Jensen, cubic-root and polynomial-sign arguments prove the claims for all stated parameters and admissible profiles.

## Relationship to prior work

Menon's 2026 work already derives the general variational condition, identifies the interior plateau and numerically finds a two-level Stratonovich optimum for a nonboundary launch. Its Fig. 4 and Eqs. (46)–(52) are prior coverage for the *qualitative two-layer structure*, which is not claimed here as new. The distinct assessed result is the explicit entire launch-position algebraic solution, strict monotonic improvement theorem, exact cubic onset, square-root target-layer asymptotic, and half-budget allocation law, replacing numerical-only interior-position characterization in the referenced source.

Menon, dos Santos and Anteneodo (2023), arXiv:2311.00818, already give the arbitrary-profile Stratonovich first-passage identity and discuss fixed-average comparisons; that identity is reused, not renamed as new. Their full text develops comparisons for specified diffusivity shapes rather than the exact full-budget optimal interior-launch problem. Tung and Lawley (2026), arXiv:2512.19646, address general first passage and small absorbing targets in three-dimensional heterogeneous media, not this fixed-budget one-dimensional optimization.

## Limitations

The result assumes a freely selectable positive spatial diffusivity with only an average budget; a pointwise cap, lower bound, smoothness constraint, different stochastic prescription, spatial dimension, or generalized boundary mechanism changes the optimizer. The interface is defined by the intrinsic-coordinate Stratonovich transmission convention. For smooth-only profiles, an approximating sequence realizes the stated infimum but the discontinuous exact optimizer lies outside the smooth class. No inference about higher-dimensional optima or first-passage variance is made. Related unindexed optimization results remain a publication-priority uncertainty, and no independent mathematical audit has been performed.

## References

1. L. Menon, *Optimal heterogeneous diffusivity profiles for mean first-passage minimization*, arXiv:2611.17470v1 (first public 2026-11-12), https://arxiv.org/abs/2611.17470 . Read in full, especially Eqs. (12), (46)–(52), Figs. 4–5, and Appendix B.
2. L. Menon Jr., M. A. F. dos Santos and C. Anteneodo, *Random-search efficiency in a bounded interval with spatially heterogeneous diffusion coefficient*, arXiv:2311.00818v1 (2023-11-01), https://arxiv.org/abs/2311.00818 . Full text, especially Secs. 2.1 and 2.4.
3. H.-R. Tung and S. D. Lawley, *Escape from heterogeneous diffusion*, arXiv:2512.19646 (2025-12-22), https://arxiv.org/abs/2512.19646 . Abstract and scope comparison.
