# A sharp one-changepoint boundary for upper-record extropy and smooth increasing-hazard blind alternatives

## Finding
For the population contrast \(\Delta(F)=J(U_{2,2})-J(X)\) selected by Chaudhary and Gupta [1] in their upper-record extropy exponentiality test, the complete family of two-phase increasing-hazard exponential lifetimes has an explicit, universal phase diagram. Let \(a,b,\tau>0\), and give \(X\) survival function
\[
 S(x)=\exp\{-ax-b(x-\tau)_+\},\qquad x\geq0.
\]
Put \(q=a\tau\). Then
\[
 \boxed{\Delta(F)=\frac b4e^{-4q}\bigl(e^{2q}-1-4q-8q^2\bigr).}
\]
There is exactly one positive \(q_*=1.731442936471894\ldots\) with \(e^{2q_*}=1+4q_*+8q_*^2\). The contrast is strictly negative for \(0<q<q_*\), vanishes for \(q=q_*\), and is strictly positive for \(q>q_*\). Thus the natural nonexponential increasing-failure-rate alternative with a change from hazard \(a\) to \(a+b\) at time \(q_*/a\) is **exactly invisible to this single population contrast**.

The normalized contrast \(\Delta/b\) has exactly two critical points: a negative global minimum at
\[
 q_-=-W_0(-1/4)=0.3574029561813889\ldots
\]
and a positive global maximum at
\[
 q_+=-W_{-1}(-1/4)=2.1532923641103496\ldots,
\]
where \(W_0\) and \(W_{-1}\) are the two real branches of the Lambert \(W\) function. Their values are, respectively, \(-0.08425249834277349\ldots\) and \(0.001248267115581495\ldots\), a magnitude ratio of \(67.4955682891\ldots\), independent of both hazard rates. The zero at \(q_*\) is transverse. Moreover, the blindness is **not a discontinuous-hazard artifact**: there exist nonexponential full-support distributions with strictly positive real-analytic densities and strictly increasing, real-analytic hazards for which the same \(\Delta(F)\) is exactly zero.

## Assumptions and scope
Here \(J(Y)=-\frac12\int_0^\infty f_Y(x)^2\,dx\) is differential extropy for an absolutely continuous nonnegative random variable. The second upper \(2\)-record \(U_{2,2}\) has density \(f_{U_{2,2}}(x)=4[-\log S(x)]S(x)f(x)\) [1, equation (1.7) with both indices two]. Densities in the two-phase family are bounded and positive except for an allowed hazard/density jump at \(x=\tau\); all integrals exist. The parameters \(a>0\), \(b>0\), and \(\tau>0\) are arbitrary and fixed. The hazard is nondecreasing and jumps upward by \(b\), so the alternative is nonexponential. At the limiting boundary \(q=0\) the distribution is exponential and is excluded from the uniqueness claim for positive \(q\).

The theorem concerns the **population contrast**, not a guarantee about rejection probability, studentization, Monte Carlo critical values, or uniformity of an empirical estimator. It does not contradict the characterization in [1] using a whole family of indices; that characterization is stronger than the particular selected \((2,2)\) contrast.

## Proof
Let \(u=-\log S(x)\) be cumulative hazard and write \(h(u)=f(x(u))/S(x(u))\), where \(x(u)\) is the inverse cumulative-hazard map. Then \(du=h(u)\,dx\), \(f(x(u))=h(u)e^{-u}\), and
\[
 J(X)=-\frac12\int_0^\infty h(u)e^{-2u}\,du.
\]
Since \(f_{U_{2,2}}(x(u))=4u h(u)e^{-2u}\), the second extropy is
\[
 J(U_{2,2})=-8\int_0^\infty u^2h(u)e^{-4u}\,du.
\]
Consequently, with the integrable kernel
\[
 g(u)=\frac12e^{-2u}-8u^2e^{-4u},
\qquad \Delta(F)=\int_0^\infty h(u)g(u)\,du,
\]
we have \(\int_0^\infty g(u)\,du=\frac14-8\cdot\frac{2!}{4^3}=0\). For the specified two-phase law, \(h(u)=a+b\mathbf1\{u\ge q\}\), and direct integration yields
\[
 \Delta(F)=b\int_q^\infty g(u)\,du=\frac b4\bigl[e^{-2q}-(1+4q+8q^2)e^{-4q}\bigr].
\]
A separate direct evaluation gives
\[
 J(X)=-\frac14(a+be^{-2q}),\qquad
 J(U_{2,2})=-\frac a4-be^{-4q}\left(2q^2+q+\frac14\right),
\]
which confirms the subtraction and the normalization independently.

For uniqueness of the positive zero, set \(R(q)=e^{2q}/(1+4q+8q^2)\). Then
\[
 \frac{R'(q)}{R(q)}=\frac{2(8q^2-4q-1)}{1+4q+8q^2}.
\]
Thus \(R\) decreases strictly on \((0,(1+\sqrt3)/4)\), increases strictly thereafter, starts at \(R(0)=1\), and tends to infinity. It has exactly one positive return to level one, namely \(q_*\), giving the claimed strict signs. Since
\[
 \frac{d}{dq}\Delta(F)=-\frac b2e^{-4q}(e^{2q}-16q^2),
\]
its two critical points solve \(e^q=4q\). The function \(e^q/q\) decreases on \((0,1)\), increases on \((1,\infty)\), attains \(e<4\) at one, and tends to infinity at both ends. Hence there are exactly two critical points \(q_-<1<q_+\), with the Lambert-\(W\) values stated. The derivative signs show they are respectively the unique global minimum and global maximum on \(q>0\), because \(\Delta(0)=0\) and \(\Delta(q)\to0^+\) at infinity. The zero lies strictly between them; there \(g(q_*)<0\), so \(\Delta'(q_*)=-bg(q_*)>0\).

For the analytic extension, fix any \(a,b>0\) and integer \(k>0\) and define
\[
 h_{k,t}(u)=a+\frac b{1+e^{-k(u-t)}},\qquad
 x_{k,t}(u)=\int_0^u\frac{dv}{h_{k,t}(v)},\quad u\ge0.
\]
Because \(a<h_{k,t}(u)<a+b\), the function \(x_{k,t}\) is strictly increasing onto \([0,\infty)\). Its inverse \(u_{k,t}(x)\) defines a proper survival law \(S_{k,t}(x)=e^{-u_{k,t}(x)}\), with positive real-analytic density \(f_{k,t}=h_{k,t}(u_{k,t})S_{k,t}\) and real-analytic physical-time hazard \(\lambda_{k,t}(x)=h_{k,t}(u_{k,t}(x))\). The derivative \(h'_{k,t}(u)=bk\ell_k(u-t)(1-\ell_k(u-t))\) is strictly positive, where \(\ell_k(z)=(1+e^{-kz})^{-1}\), hence \(\lambda'_{k,t}(x)>0\) at all finite \(x\).

For this law, \(\Delta_{k}(t)=b\int_0^\infty g(u)\ell_k(u-t)\,du\) is continuous in \(t\). Dominated convergence gives \(\Delta_k(1)\to\Delta_{\rm step}(1)<0\) and \(\Delta_k(2)\to\Delta_{\rm step}(2)>0\). Therefore for all sufficiently large \(k\), there is \(t_k\in(1,2)\) with \(\Delta_k(t_k)=0\). Indeed
\[
 \sup_t\bigl|\Delta_k(t)-\Delta_{\rm step}(t)\bigr|
 \le \frac{2b\log2}{k}\|g\|_\infty,
\]
by integrating the absolute difference between the logistic step and the Heaviside step on the entire real line. Since the step contrast has a unique zero in \([1,2]\), every such choice \(t_k\) tends to \(q_*\); transversality even gives \(|t_k-q_*|=O(k^{-1})\). This proves strictly increasing, analytic, nonexponential blind alternatives on the full half-line.

## Verification
The standalone `checker.py` uses independent direct quadrature of both density squares in physical time, compares it with the two analytic extropy formulas at 54 parameter triples, bisects the zero and the two stationary points, and verifies smooth-logistic blind roots at four steepness values. It passes 185 checks using Python's standard library. Numerical checks corroborate, but do not replace, the analytic existence, uniqueness, classification, and smooth approximation proofs.

## Relationship to prior work
Chaudhary and Gupta [1], publicly posted January 6, 2023, give the upper \((n,k)\)-record formula, their general characterization for all \(k\), and select the single \((n,k)=(2,2)\) contrast for numerical testing. Their analytic and numerical sections do not state the one-changepoint classification, its unique nonexponential increasing-hazard zero, the two exact sensitivity extrema, or persistence under strict analytic IFR smoothing. Xiong, Zhuang, and Qiu [2] use extropy of standard upper \(k\)-records rather than the selected upper \((2,2)\)-record contrast; [1] itself distinguishes their statistic from its own. Hashempour and Mohammadi [3] study cross-inaccuracy between the record density and the parent density, rather than squared extropy of the record density. The cumulative extropy IFRA tests of [4] use different functionals. Generic change-point survival models and Laplace integrations supply ingredients, not the stated source-specific sharp phase diagram. Full-text comparison with [2] was prevented by access restrictions; this remains a priority risk and no negative full-text finding is claimed for it.

## Limitations
The zero-contrast law is not claimed to have asymptotically nominal rejection probability under the particular finite-sample test; a vanishing population discrepancy alone does not determine the empirical null/alternative fluctuation laws. The extremal contrast magnitudes depend linearly on \(b\), so the dimensionless ratio is specific to the stated one-change-point family. The analytic approximation proves existence of blind alternatives but not uniqueness of the logistic root for any finite \(k\). Independent historical priority assessment, especially of the full text of [2], remains outstanding.

## References
1. S. K. Chaudhary and N. Gupta, *Testing exponentiality using extropy of upper record values*, arXiv:2301.02698v1, first posted 2023-01-06, https://arxiv.org/abs/2301.02698 . Definitions (1.7), Theorem 1, and Section 3.
2. P. Xiong, W. Zhuang, and G. Qiu, *Testing exponentiality based on the extropy of record values*, Journal of Applied Statistics, published online 2020-10-31, https://doi.org/10.1080/02664763.2020.1840535 .
3. M. Hashempour and M. Mohammadi, *A new measure of inaccuracy for record statistics based on extropy*, Probability in the Engineering and Informational Sciences, published online 2023-03-10, https://doi.org/10.1017/S0269964823000086 .
4. A. A. Alqefari, *Nonparametric Tests for Exponentiality Against IFRA Alternatives Based on Cumulative Extropy Measures*, Entropy 28 (2026), 208, https://doi.org/10.3390/e28020208 .
