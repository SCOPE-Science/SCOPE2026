# Sharp orientation and sampling-budget transitions in one-node stochastic Lanczos log-determinants

## Finding

Let \(A\) be any real symmetric positive-definite \(2\times2\) matrix with distinct eigenvalues \(a>b>0\), and let \(z^{(1)},\ldots,z^{(N)}\) be independent vectors with independent fair Rademacher coordinates, for an arbitrary integer \(N\ge1\). Use exactly one Lanczos step per vector to estimate \(L=\log\det A\), namely

\[
\widehat L_N=\frac1N\sum_{j=1}^N 2\log\left(\frac{(z^{(j)})^{\mathsf T}Az^{(j)}}{2}\right).
\]

Write \(A=R_\theta\operatorname{diag}(a,b)R_\theta^{\mathsf T}\) for a planar rotation, and define

\[
r=\frac{a-b}{a+b}\in(0,1),\qquad t=|\sin(2\theta)|\in[0,1],\qquad
B_0=-\log(1-r^2)>0,\qquad \kappa=\frac ab>1.
\]

For *every* such \(A\), \(N\), and orientation, the **exact mean-squared error** is

\[
\boxed{F_N(t)=\mathbb E(\widehat L_N-L)^2
=\left[\log\frac{1-r^2t^2}{1-r^2}\right]^2
+\frac1N\left[\log\frac{1+rt}{1-rt}\right]^2.}
\]

The two terms are, respectively, squared quadrature bias and stochastic probe variance. In particular, across all rotations with these eigenvalues, the **sharp worst-orientation risk** is

\[
\boxed{\max_{0\le t\le1}F_N(t)=\max\left\{B_0^2,\frac{(\log\kappa)^2}{N}\right\}.}
\]

Set \(N_{\mathrm{worst}}=(\log\kappa/B_0)^2\). If \(N<N_{\mathrm{worst}}\), the only worst orientations (as represented by \(t\)) have \(t=1\), when the quadrature bias vanishes but stochastic variation remains. If \(N>N_{\mathrm{worst}}\), the only worst orientations have \(t=0\), when the stochastic variance vanishes but the quadrature bias persists. At equality, both endpoints are worst, with no other maximizers.

There is a **second, distinct transition** for best orientation. Set \(N_{\mathrm{best}}=2/B_0\). If \(N\le N_{\mathrm{best}}\), \(t=0\) is the unique minimizer. If \(N>N_{\mathrm{best}}\), the unique minimizing \(t\in(0,1)\) solves

\[
\boxed{N=\frac{\log\bigl((1+rt)/(1-rt)\bigr)}{rt\,\log\bigl((1-r^2t^2)/(1-r^2)\bigr)}.}
\]

These transitions exhaust all minimizers and maximizers on \([0,1]\), including the endpoint and equality cases. In the weak-anisotropy limit \(r\downarrow0\), the two critical probe budgets satisfy \(N_{\mathrm{best}}\sim2/r^2\) and \(N_{\mathrm{worst}}\sim4/r^2\); they are separated by an asymptotic factor of two. In particular, adding probes beyond the worst-orientation transition cannot remove the fixed one-node quadrature-bias floor \(B_0^2\). For \(a=b\), which is excluded from the strict transition theorem, the estimator is exact for every probe and orientation.

## Assumptions and scope

The matrix is real, symmetric, strictly positive definite, and two-dimensional; the eigenvalues satisfy \(a>b>0\). Probe coordinates are independent and uniformly distributed over \(\{-1,+1\}\), and probes are independent across repetitions. The estimator is the *unmodified, one-node* stochastic Lanczos quadrature estimate of \(\operatorname{tr}\log A\); it uses the first Rayleigh quotient and does not invoke deflation, preconditioning, exact spectral information, control variates, or additional Lanczos steps. Angles are coordinate-basis orientations, not stochastic random variables. No assertions are made about higher dimensions, other probe laws, or finite-precision stability.

## Proof

**1. Identification of the sampled two-point law.** Let \(m=(a+b)/2\). The diagonal sum of \(A\) is \(2m\), and its off-diagonal entry equals \(mr\sin(2\theta)\), up to an irrelevant sign convention for the rotation. Thus for any Rademacher vector \(z=(z_1,z_2)\),

\[
\frac{z^{\mathsf T}Az}{2}=m\bigl(1+r\sin(2\theta)z_1z_2\bigr).
\]

The product \(z_1z_2\) is itself a fair sign. Therefore each one-node output equals \(2\log(m(1+rt))\) or \(2\log(m(1-rt))\), each with probability \(1/2\), after relabeling the signs. Meanwhile \(\det A=ab=m^2(1-r^2)\). Direct averaging gives

\[
\mathbb E\widehat L_N-L
=\log\frac{1-r^2t^2}{1-r^2}=:B(t)\ge0,
\qquad
\operatorname{Var}(\widehat L_N)
=\frac1N\left[\log\frac{1+rt}{1-rt}\right]^2=:\frac{U(t)^2}{N}.
\]

This proves the exact risk formula for every integer \(N\ge1\). The independence across probes is used only for the factor \(1/N\). The scale \(m\) cancels from the error.

**2. No interior worst orientations.** For \(0<t<1\), the functions \(B\) and \(U\) satisfy

\[
B'(t)=-\frac{2r^2t}{1-r^2t^2},\qquad
U'(t)=\frac{2r}{1-r^2t^2},\qquad
F_N'(t)=\frac{4r}{1-r^2t^2}\left(\frac{U(t)}N-rt B(t)\right).
\]

Define \(H(t)=U(t)/(rtB(t))\), which is positive on \((0,1)\). The quotient

\[
\frac{U(t)}{rt}=2\sum_{k=0}^{\infty}\frac{(rt)^{2k}}{2k+1}
\]

is strictly increasing in \(t>0\), while \(B(t)\) is strictly decreasing and positive. Hence \(H\) is strictly increasing. Its endpoint limits are

\[
\lim_{t\downarrow0}H(t)=\frac2{B_0},\qquad
\lim_{t\uparrow1}H(t)=+\infty.
\]

Since the sign of \(F_N'\) equals the sign of \(H(t)-N\), the risk either increases everywhere (if \(N\le2/B_0\)) or decreases and then increases with one strict interior minimum (if \(N>2/B_0\)). In particular it has no interior maximum. Its only possible maxima are the two endpoints, with

\[
F_N(0)=B_0^2,\qquad F_N(1)=\frac{\log^2((1+r)/(1-r))}{N}=\frac{(\log\kappa)^2}{N}.
\]

Their strict comparison proves the sharp worst-orientation switch and all equality cases. Moreover, the worst-orientation transition always comes *after* the best-orientation transition: writing \(W(r)=\log((1+r)/(1-r))\), the quantity \(W(r)^2-2B_0\) vanishes as \(r\downarrow0\) and has derivative \(4(W(r)-r)/(1-r^2)>0\). Hence \(N_{\mathrm{worst}}>N_{\mathrm{best}}\) whenever \(r>0\), so equality of the two endpoint risks cannot hide a flat or monotone interior maximum. The same monotonicity of \(H\) proves both regimes, the unique interior minimizer equation, and its existence for every \(N>2/B_0\). At \(N=2/B_0\), \(F_N'(t)>0\) for all \(t>0\), so \(t=0\) remains the *unique* minimizer.

**3. A checkable numerical example.** For \(a=9\), \(b=1\), one has \(r=4/5\), \(B_0=\log(25/9)\), and the thresholds are approximately \(N_{\mathrm{best}}=1.95761518897\) and \(N_{\mathrm{worst}}=4.62533887901\). For one probe, the minimizing orientation is \(t=0\) and the worst is \(t=1\). For ten probes, the minimizing orientation is \(t\approx0.91471834563\), with \(F_{10}(t)\approx0.41280907\); the worst is \(t=0\), with \(F_{10}(0)\approx1.04377127\), while \(F_{10}(1)\approx0.48277958\). These decimals are illustrations, not proof.

## Verification

A standalone Python 3 script, `verify.py`, independently enumerates the four equally probable sign probes and (for up to four probes) all probe sequences, and compares their exact finite-distribution moments with the formula. It also checks the endpoint bound and unique-minimum prediction on numerical grids across five eigenvalue ratios and a range of integer probe budgets. Run `python3 verify.py` without third-party dependencies. The recorded output is `verification_output.txt`. All continuous-parameter and global statements are proved in the preceding algebra; numerical grids do not establish them.

## Relationship to prior work

Ubaru, Chen and Saad (2017), Algorithm 1 and section 4.3, introduce the Rademacher-probe SLQ estimator and furnish general log-determinant error bounds. Their result directly supplies the computational method but does not state the exact two-eigenvalue orientation MSE, the maximal risk switch, or the best-orientation transition here. Cortinovis and Kressner (2020 preprint; later journal publication) obtain tail bounds for randomized matrix-function traces and apply them to determinants, but these do not determine the present joint bias-variance risk or its complete angular extremizers. Chen, Trogdon and Ubaru (2022) provide broad matrix-free spectral quadrature error theory rather than the exact two-coordinate classification. Li, Han, Huang, Wathen and Zhu (2023) analyze asymmetric SLQ quadrature and optimize the division of error budgets across iterations and random probes; their general bounds do not imply the two exact orientation thresholds or the minimax equality derived above. These are comparisons of claims and scope, not claims that stochastic Lanczos quadrature or its bias-variance decomposition is new.

## Limitations

The theorem is an exact two-dimensional benchmark, **not** a general-purpose recommendation to rotate unknown matrices: the best orientation depends on spectral information that may be unavailable without extra work. Matrix–vector-query efficiency in large dimensions and all other SLQ designs is outside its scope. For a two-eigenvalue matrix, two Lanczos steps recover the spectral quadratic form \(z^{\mathsf T}\log(A)z\) exactly, but its Rademacher trace estimator can still vary; this should not be conflated with exact log-determinant recovery from one random vector. The result establishes mean-squared error, not concentration at fixed confidence. Specialist older results using equivalent Bernoulli two-point models could contain the same optimization, so precedence remains subject to independent literature verification. No independent scientific audit has been performed.

## References

1. S. Ubaru, J. Chen and Y. Saad, *Fast Estimation of tr(f(A)) via Stochastic Lanczos Quadrature*, SIAM Journal on Matrix Analysis and Applications 38 (2017), 1075–1099, doi:10.1137/16M1104974, publicly released October 3, 2017. Full text: https://www.cs.cornell.edu/courses/cs6241/2020sp/readings/Ubaru-2017-fast.pdf.
2. A. Cortinovis and D. Kressner, *On randomized trace estimates for indefinite matrices with an application to determinants*, arXiv:2005.10009, first posted May 20, 2020. https://arxiv.org/abs/2005.10009.
3. T. Chen, T. Trogdon and S. Ubaru, *Randomized matrix-free quadrature: unified and uniform bounds for stochastic Lanczos quadrature and the kernel polynomial method*, arXiv:2204.01941, first posted April 5, 2022. https://arxiv.org/abs/2204.01941.
4. W. Li, Z. Han, Y. Huang, A. Wathen and S. Zhu, *An Analysis on Stochastic Lanczos Quadrature with Asymmetric Quadrature Nodes*, arXiv:2307.00847, first posted July 3, 2023. https://arxiv.org/abs/2307.00847.
