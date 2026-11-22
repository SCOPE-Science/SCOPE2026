# Sharp \(24/d^3\) pathwise–mean-square gap for Gaussian zeroth-order descent

## Finding
Consider a single unnormalized fresh Gaussian direction at each iteration of centered two-point derivative-free gradient descent on the isotropic strongly convex quadratic. Its exact mean-square stability threshold is \(2/(d+2)\), known from the covariance calculation in Song and collaborators. The **new quantified pathwise comparison** is
\[
\lim_{d\to\infty} d^3\,\mathbb E\log F_d\!\left(\frac{2}{d+2}+\frac{a}{d^3}\right)=2a-48,
\]
for every fixed real \(a\), where \(F_d(\eta)\) is the squared-norm multiplier defined below.

Thus, for every fixed \(0<a<24\), in all sufficiently large integer dimensions the stochastic iterates converge exponentially to the minimizer **almost surely**, whereas their expected squared norm grows exponentially. For each fixed \(a>24\), the same stepscale gives exponential divergence almost surely as well as in mean square. In particular the local pathwise sign crossing exists in the sharp window
\[
\eta=\frac{2}{d+2}+\frac{24+o(1)}{d^3}.
\]
The coefficient \(24\) is sharp in the fixed-\(a\) sense stated above. No uniqueness outside this local window is asserted.

## Assumptions and scope
For each integer \(d\ge2\), let \(f(x)=\tfrac12\|x\|_2^2\) on \(\mathbb R^d\). Starting from any deterministic \(x_0\ne0\), draw independent \(u_k\sim N(0,I_d)\). At a fixed arbitrary finite-difference radius \(\mu>0\), set
\[
g_k=\frac{f(x_k+\mu u_k)-f(x_k-\mu u_k)}{2\mu}\,u_k=(u_k^{\mathsf T}x_k)u_k,
\qquad x_{k+1}=x_k-\eta g_k.
\]
The stepsize \(\eta>0\) is *constant and unnormalized* (it is neither a direction-norm-normalized step nor a decaying schedule). Time tends to infinity at each fixed dimension when defining pathwise and mean-square growth rates; the later \(d\to\infty\) limit uses a sequence of separately defined problems.

Let independent \(U\sim\chi^2_1\) and \(W\sim\chi^2_{d-1}\), and define
\[
F_d(\eta)=1-2\eta U+\eta^2 U(U+W)
=(1-\eta U)^2+\eta^2 UW>0\quad\text{almost surely}.
\]
All stochastic expectations and logarithms are with respect to these two independent variables.

## Proof
**Exact independent radial law.** Conditional on the nonzero past iterate, choose its unit direction as the first coordinate. Rotational invariance of a fresh standard Gaussian makes its squared projection \(U\sim\chi^2_1\) independent of its orthogonal squared norm \(W\sim\chi^2_{d-1}\). Directly expanding the update gives \(\|x_{k+1}\|^2/\|x_k\|^2=F_d(\eta)\). Its conditional distribution is independent of every past event, so the radial factors are i.i.d. Since \(d\ge2\), their positivity is almost sure. Moreover \(\mathbb E|\log F_d(\eta)|<\infty\): positive logs are bounded by positive polynomial tails; negative logs are bounded by the negative part of \(\log(\eta^2 UW)\), whose moments exist for positive chi-squares. The strong law consequently gives
\[
\lim_{k\to\infty}\frac1k\log\frac{\|x_k\|}{\|x_0\|}=\frac12\mathbb E\log F_d(\eta)\quad\text{a.s.}
\]
**Exact second moment.** The chi-square moment identities \(\mathbb E U=1\), \(\mathbb E U^2=3\), and \(\mathbb E W=d-1\) yield
\[
\mathbb EF_d(\eta)=1-2\eta+(d+2)\eta^2.
\]
Independence therefore gives \(\mathbb E\|x_k\|^2=[1-2\eta+(d+2)\eta^2]^k\|x_0\|^2\). The strict mean-square contraction region is exactly \(0<\eta<2/(d+2)\). At its positive endpoint \(\mathbb EF_d=1\), but strict Jensen's inequality implies \(\mathbb E\log F_d<0\) because the multiplier is nonconstant; hence paths still decay almost surely.

**Critical-dimensional expansion.** Write \(c_d=2/(d+2)\) and \(\eta_d=c_d+a/d^3\), with fixed real \(a\); this is positive for all large \(d\). Set \(Y_d=F_d(\eta_d)-1\). Direct exact evaluation gives
\[
\mathbb E Y_d=(d+2)\eta_d(\eta_d-c_d)=\frac{2a}{d^3}+O(d^{-5}).
\]
At the critical stepsize \(c_d\),
\[
Y_d^{(0)}=c_d^2 U(U+W-d-2),
\qquad \mathbb E (Y_d^{(0)})^2=\frac{96(d+6)}{(d+2)^4}.
\]
For completeness, expanding the square with \(\mathbb EU^2=3\), \(\mathbb EU^3=15\), \(\mathbb EU^4=105\), \(\mathbb EW=d-1\), and \(\mathbb EW^2=(d-1)(d+1)\) proves the exact identity \(\mathbb E[U^2(U+W-d-2)^2]=6(d+6)\). By the same finite chi-square moment bounds, uniformly for \(a\) in a fixed compact interval,
\[
\mathbb E Y_d^2=\frac{96}{d^3}+O(d^{-4}),\qquad \mathbb E|Y_d|^p=O(d^{-3p/2})\quad\text{for each fixed integer }p\ge2.
\]
The latter follows from \(U\)'s fixed moments, the \(O(d^{p/2})\) absolute centered moments of \(W\), and \(\eta_d=O(d^{-1})\). On \(\{|Y_d|\le1/2\}\), Taylor's formula bounds the difference between \(\log(1+Y_d)\) and \(Y_d-Y_d^2/2\) by a constant times \(|Y_d|^3\); its expectation is \(O(d^{-9/2})\). For the complement, Markov's inequality using arbitrarily high fixed moments gives \(\Pr(|Y_d|>1/2)=O(d^{-M})\) for every fixed \(M\). Its logarithmic contribution is negligible: since \(F_d\ge\eta_d^2UW\), the negative log is controlled by chi-square log moments plus \(O(\log d)\), and the positive log by \(F_d\), whose fixed moments are bounded. Cauchy–Schwarz then bounds the exceptional contribution by \(o(d^{-3})\). The same high-moment bound controls the omitted linear and quadratic tails. Consequently,
\[
\mathbb E\log F_d(\eta_d)
=\mathbb E Y_d-\tfrac12\mathbb E Y_d^2+o(d^{-3})
=\frac{2a-48}{d^3}+o(d^{-3}),
\]
with errors uniform for bounded \(a\). This establishes the claimed sharp limit.

**Phase interpretation.** For fixed \(0<a<24\), \(\mathbb EF_d(\eta_d)>1\) for large \(d\) yet \(\mathbb E\log F_d(\eta_d)<0\); hence second moments grow geometrically while almost all paths decay exponentially. For fixed \(a>24\), both have positive exponents. Continuity in \(\eta\) of \(\mathbb E\log F_d(\eta)\) at positive \(\eta\), justified by local integrable chi-square log bounds, and the intermediate value theorem show that, for every fixed \(\varepsilon>0\) and large \(d\), at least one sign crossing lies between \(c_d+(24-\varepsilon)/d^3\) and \(c_d+(24+\varepsilon)/d^3\). No behavior is claimed exactly at the coefficient \(a=24\), and no global uniqueness is needed.

## Verification
The standalone `verify.py` checks exact chi-square moment identities using integer arithmetic, the precise covariance multiplier, and numerical gamma-product quadrature for illustrative dimensions. It passes independently of any previous output or log. Its finite numerical examples are consistency tests; the dimension-uniform estimates, strict signs for all sufficiently large dimensions, and almost-sure claims follow from the proof rather than finite computation.

## Relationship to prior work
Song et al., *Zeroth-Order Optimization at the Edge of Stability* (2026), derive mean-square ZO-GD stability via a covariance operator, including the isotropic threshold, and formulate multi-probe covariance recursions. That threshold is prior work, not asserted new here. Ye (2026) establishes high-probability last-iterate guarantees for a **norm-normalized, decaying** Gaussian two-point recursion; those parameter choices do not imply constant-step pathwise stability. A published scalar-probe analysis, *Probe averaging can reverse almost-sure stability in Gaussian zeroth-order descent* (2026), quantifies the \(8/n\) split as the **number of scalar probes** increases, rather than the \(24/d^3\) gap as the **ambient dimension of a single unnormalized Gaussian direction** increases. A classical stochastic-subspace descent analysis covers expectation and probabilistic convergence results without the present local logarithmic coefficient. The original contribution here is exclusively the sharp ambient-dimensional pathwise/mean-square split.

## Limitations
Only isotropic quadratic objectives, fresh standard Gaussian directions, exact same-evaluation central differences and unnormalized fixed positive steps are covered. The infinite-time limit comes before the large-dimension limit. The local sign change is established in a window; global uniqueness of the pathwise stability boundary or its equality case is not established. The original mean-square condition and the strong-law criterion are not new. Historical novelty is based on specified inspected sources and record searches, not an exhaustive mathematical priority certification. Independent mathematical review has not been performed.

## References
1. M. Song, L. Zhang, B. Li, N. He, M. Muehlebach, S. Oh, *Zeroth-Order Optimization at the Edge of Stability*, arXiv:2604.14669v1, first public 2026-04-16, especially §4 and Appendix B.3. https://arxiv.org/html/2604.14669v1
2. H. Ye, *High-Probability Last-Iterate Guarantees for Two-Point Gaussian Zeroth-Order Stochastic Gradient Descent*, arXiv:2606.20446, first public 2026-06-18, §2–5. https://academ.us/article/2606.20446/
3. *Probe averaging can reverse almost-sure stability in Gaussian zeroth-order descent*, 2026, published mathematical result. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-probe-averaging-can-reverse-almost-sure-stability-in-gaussian-ze--bd4e7bf676c0
4. D. Kozak, S. Becker, A. Doostan, L. Tenorio, *A stochastic subspace approach to gradient-free optimization in high dimensions*, arXiv:2003.02684 (2020), *Computational Optimization and Applications* 79 (2021), 339–368. https://arxiv.org/abs/2003.02684
