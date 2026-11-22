# Microscopic two-jump extremizers for sharp periodic heat approximation of bounded-variation functions

## Finding

Let \(\mathbb T=\mathbb R/\mathbb Z\) carry probability-normalized Lebesgue measure, let \(H_t=\exp(t\partial_x^2)\) be the heat semigroup, and let \(V(f)=|Df|(\mathbb T)\) denote full circular distributional variation of a real function. For every \(t>0\), the exact, attained best constant in
\[
\|(I-H_t)f\|_{L^2(\mathbb T)}\le C_t V(f),\qquad f\in BV(\mathbb T),
\]
is
\[
C_t^2=\max_{0\le d\le1/2}E_t(d),\qquad
E_t(d)=\frac1{2\pi^2}\sum_{n=1}^\infty
\frac{(1-e^{-4\pi^2tn^2})^2\sin^2(\pi nd)}{n^2}.
\]
Every nonconstant extremizer is, up to almost-everywhere equality, a constant plus a nonzero real multiple of the indicator of a circular arc of optimal shorter length \(d\); the arc may be rotated or complemented.

Define
\[
F(z)=\frac1\pi\int_0^\infty
\frac{(1-e^{-v^2})^2\sin^2(zv)}{v^2}\,dv,\qquad z\ge0.
\]
There is a unique \(z_*>0\) satisfying
\[
\operatorname{erfc}(z_*/\sqrt2)=2\operatorname{erfc}(z_*),
\qquad z_*=0.992269655382050\ldots.
\]
For **every** maximizing shorter arc length \(d_t\),
\[
\lim_{t\downarrow0}\frac{d_t}{2\sqrt t}=z_*,\qquad
\lim_{t\downarrow0}\frac{C_t^2}{\sqrt t}=F(z_*)
=\frac{1-e^{-z_*^2}-2^{-1/2}(1-e^{-z_*^2/2})}{\sqrt\pi}
=0.198313496197009\ldots.
\]
Consequently \(C_t\sim0.445324035054262\,t^{1/4}\). By contrast, for any *fixed* arc length \(d\in(0,1/2]\),
\[
\lim_{t\downarrow0}\frac{E_t(d)}{\sqrt t}
=\frac{1-1/\sqrt2}{\sqrt\pi}=0.165247303146324\ldots.
\]
Thus optimizing over microscopic two-jump separations raises the limiting **squared** error coefficient by a factor \(1.20010125685020\ldots\) over every fixed positive separation.

## Assumptions and scope

All norms are Lebesgue norms on the *unit-length* circle; no additional factor of \(2\pi\) is included. The heat generator is \(\partial_x^2\), hence the nonzero Fourier multiplier of \(H_t\) is \(e^{-4\pi^2tn^2}\). All input functions are real, viewed modulo almost-everywhere equality, and \(V(f)=|Df|(\mathbb T)\) includes both jumps of an arc. For \(0<d<1\), an arc indicator has \(V=2\). Constants have zero variation and are excluded from the quotient. The asymptotic assertion quantifies over *every* maximizer \(d_t\) and does not assert uniqueness of the maximizing length at arbitrary fixed \(t>0\).

## Proof

**1. A reduction to pairs of jumps, including equality.** Let \(f\in BV(\mathbb T)\) be real and nonconstant and write its signed derivative measure \(\mu=Df\), of total mass zero and norm \(V=|\mu|(\mathbb T)>0\). Its Jordan decomposition is
\[
\mu=\frac V2(\mu_+-\mu_-),
\]
where \(\mu_+\) and \(\mu_-\) are probability measures. For a pair \((a,b)\), let \(A_{a,b}\) be the oriented counterclockwise circular arc from \(a\) to \(b\); then \(D\mathbf1_{A_{a,b}}=\delta_a-\delta_b\). With \(\pi=\mu_+\otimes\mu_-\), differentiation gives
\[
f\equiv \frac V2\int_{\mathbb T^2}\mathbf1_{A_{a,b}}\,d\pi(a,b)
\quad\text{modulo constants}.
\]
Applying \(I-H_t\), Minkowski's integral inequality, and rotation/reflection invariance yields
\[
\frac{\|(I-H_t)f\|_2}{V}
\le\frac12\int\|(I-H_t)\mathbf1_{A_{a,b}}\|_2\,d\pi
\le\max_{0\le d\le1/2}\frac12\|(I-H_t)\mathbf1_{[0,d]}\|_2.
\]
The bound is attained by any maximizing arc. Equality in both inequalities is rigid: the Hilbert norm is strictly convex, and all nonzero arc residuals attaining the common maximum must agree as vectors after the normalization above. Since \(I-H_t\) is injective on the mean-zero Fourier subspace, the corresponding indicators agree modulo constants, hence their signed derivative measures agree. It follows that \(\mu\) is a nonzero scalar multiple of one difference of Dirac masses, so \(f\) is an arc indicator up to scaling and addition of a constant. Conversely such functions at maximizing lengths attain equality. There is no difficulty from any coincident pairs \(a=b\): their residuals vanish and hence cannot carry positive weight in an equality case.

**2. Exact Fourier formula.** With \(\widehat g(n)=\int_0^1g(x)e^{-2\pi inx}\,dx\), for \(n\ne0\),
\[
\left|\widehat{\mathbf1_{[0,d]}}(n)\right|^2
=\frac{\sin^2(\pi nd)}{\pi^2n^2}.
\]
Parseval, pairing \(n\) and \(-n\), and dividing by \(V^2=4\) give precisely \(E_t(d)\). Uniform absolute convergence in \(d\) makes its maximum attained. The identity
\[
\sum_{n=1}^\infty\frac{\sin^2(\pi nd)}{n^2}
=\frac{\pi^2}2d(1-d),\qquad 0\le d\le1,
\]
also yields an exponentially convergent computational expression
\[
E_t(d)=\frac{d(1-d)}4-
\frac1{2\pi^2}\sum_{n=1}^\infty
\frac{e^{-4\pi^2tn^2}\bigl(2-e^{-4\pi^2tn^2}\bigr)
\sin^2(\pi nd)}{n^2}.
\]

**3. Uniform small-time passage from the circle to the line.** On \(\mathbb R\) define the single-step residual
\[
r_t(x)=\mathbf1_{(0,\infty)}(x)-H_t^{\mathbb R}\mathbf1_{(0,\infty)}(x)
=\frac12\operatorname{sgn}(x)
\operatorname{erfc}\left(\frac{|x|}{2\sqrt t}\right)
\quad (x\ne0).
\]
The residual of the interval \([0,d]\) is \(R_t^d(x)=r_t(x)-r_t(x-d)\). Its periodization equals the circular arc residual. By the Gaussian bound \(\left|r_t(x)\right|\le\frac12e^{-x^2/(4t)}\) and the Gaussian product integral,
\[
\int_{\mathbb R}|r_t(x-a)r_t(x-b)|\,dx
\le\frac{\sqrt{2\pi t}}4e^{-(a-b)^2/(8t)}.
\]
For \(0\le d\le1/2\), every cross-term between distinct integer translates of \(R_t^d\) has a pair of centers separated by at least \(1/2\), so summing the Gaussian tail shows, uniformly in \(d\),
\[
\left|\frac14\|\operatorname{per}(R_t^d)\|_{L^2(\mathbb T)}^2
-\frac14\|R_t^d\|_{L^2(\mathbb R)}^2\right|
\le C\sqrt t\,e^{-1/(32t)}
\]
for all sufficiently small \(t>0\), with an absolute \(C\). Fourier-Plancherel on \(\mathbb R\), followed by \(v=2\pi\sqrt t\,|\xi|\), gives the **exact line identity**
\[
\frac14\|R_t^d\|_{L^2(\mathbb R)}^2
=\sqrt t\,F\left(\frac d{2\sqrt t}\right).
\]
Consequently,
\[
\sup_{0\le d\le1/2}\left|
\frac{E_t(d)}{\sqrt t}-F\left(\frac d{2\sqrt t}\right)
\right|\le C e^{-1/(32t)}.
\]

**4. Unique Gaussian-profile maximum.** Differentiation under the Gaussian-regularized integral, with the Dirichlet integral for the unregularized term, gives for \(z>0\)
\[
F'(z)=\frac12\left[2\operatorname{erfc}(z)-
\operatorname{erfc}(z/\sqrt2)\right].
\]
The Gaussian hazard function \(h(x)=2e^{-x^2}/(\sqrt\pi\operatorname{erfc}(x))\) is strictly increasing for \(x\ge0\): indeed
\[
\frac1{h(x)}=\int_0^\infty e^{-u^2-2xu}\,du,
\]
which is strictly decreasing. Hence
\[
\frac{d}{dz}\log\frac{\operatorname{erfc}(z/\sqrt2)}{
\operatorname{erfc}(z)}
=h(z)-\frac1{\sqrt2}h(z/\sqrt2)>0.
\]
The ratio rises strictly from \(1\) at \(z=0\) to infinity (by the Gaussian-tail asymptotic); it reaches \(2\) exactly once, at \(z_*\). Accordingly \(F\) strictly increases on \([0,z_*]\) and strictly decreases on \([z_*,\infty)\). Integration of \(F'\) gives
\[
F(z)=z\left[\operatorname{erfc}(z)-\frac12\operatorname{erfc}(z/\sqrt2)\right]
+\frac{1-e^{-z^2}-2^{-1/2}(1-e^{-z^2/2})}{\sqrt\pi}.
\]
Thus the displayed exact coefficient follows by inserting the root equation. As \(z\to\infty\), this formula tends to \((1-1/\sqrt2)/\sqrt\pi<F(z_*)\).

**5. Localization of every optimizer.** The uniform estimate of Step 3 implies \(\sup_d E_t(d)/\sqrt t\to F(z_*)\), since \(2z_*\sqrt t\in(0,1/2)\) for small \(t\). If \(d_t\) maximizes \(E_t\), the corresponding \(z_t=d_t/(2\sqrt t)\) must satisfy \(F(z_t)\to F(z_*)\). Strict uniqueness of the global maximum and the strict drop at infinity force \(z_t\to z_*\). A fixed \(d>0\) instead has \(z_t\to\infty\), giving the fixed-separation coefficient. The theorem follows.

## Verification

The standalone `check.py` uses only the Python standard library. It checks the complementary-error-function root, the profile coefficient and its separated-jump limit, direct Fourier sums against the accelerated exact identity at multiple times/separations, and finite-time maximizers against the microscopic scaling. Execute with `python3 check.py`. The reported pass count refers solely to these **finite** computations. Infinite-dimensional extremizer rigidity, uniform periodization and global Gaussian-profile uniqueness are analytical steps proved above, not consequences of the checker.

## Relationship to prior work

Miranda, Pallara, Paronetto and Preunkert established heat-semigroup characterizations of perimeter and BV via \(L^1\)-type heat leakage and short-time limits; their text also discusses a fixed-volume \(L^2\) rearrangement inequality for smoothed indicators. Neither comparison gives the operator norm of \(I-H_t\) from the circular variation seminorm to \(L^2\), nor maximizes its two-heat-time residual energy over arc lengths allowed to shrink with \(t\). Bramanti, Miranda and Pallara study analogous BV characterizations on Carnot groups, again with distinct norm and geometric hypotheses.

For comparison, sharp estimates for periodic Poisson-mixture residuals concern Fourier multipliers \(m_n=\int_0^1r^{|n|}d\nu(r)\) and yield antipodal rather than microscopic extremizers. The heat multipliers \(e^{-4\pi^2tn^2}\) are **not** such a mixture: a moment sequence must satisfy \(m_2\ge m_1^2\), whereas here \(m_2=e^{-16\pi^2t}<e^{-8\pi^2t}=m_1^2\). Sharp periodic Fejér residuals have instead the cutoff multiplier \((1-|n|/N)_+\), and their limiting sine-integral optimization does not imply this Gaussian error-function law. These differences concern the precise claims and their logical implications, not titles alone.

## Limitations

The conclusion is for real scalar data on the unit circle, the classical Gaussian heat semigroup with fixed positive time, ordinary full circular variation, and the normalized \(L^2\) residual. It does not classify the number of maximizing arc lengths for each positive finite time, prove an all-time transition to antipodal arcs, or extend to complex-valued variation, non-Gaussian semigroups or other target norms. A previously unindexed equivalent theorem remains a historical-priority risk. The numerical constants are rounded; the defining root, series and integrals are exact.

## References

1. M. Miranda Jr., D. Pallara, F. Paronetto and M. Preunkert, *Short-time Heat Flow and Functions of Bounded Variation in \(\mathbb R^N\)*, public preprint posted 2005-02-19 at https://cvgmt.sns.it/paper/801/ (full text https://cvgmt.sns.it/media/doc/paper/801/MPPP.pdf); later Ann. Fac. Sci. Toulouse Math. 16 (2007), 125–145, DOI:10.5802/afst.1142.
2. M. Bramanti, M. Miranda Jr. and D. Pallara, *Two characterization of BV functions on Carnot groups via the heat semigroup*, arXiv:1107.3996, first posted 2011-07-20, https://arxiv.org/abs/1107.3996.
3. Gaussian heat kernel, Plancherel's identity and the complementary error function: classical analytic identities, explicitly normalized in the proof above.
