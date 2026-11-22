# Sharp replication-to-separation transition in symmetric Gaussian-kernel quadrature

## Finding
Let \(X\) be a centered Gaussian process on \(\mathbb R\) with squared-exponential covariance
\[
K(x,y)=\exp\!\left(-\frac{(x-y)^2}{2\ell^2}\right),\qquad \ell>0.
\]
For \(\tau>0\), estimate the Gaussian-weighted integral \(J=\int_{\mathbb R}X(x)\,\mathrm dN(0,\tau^2)(x)\) using at most two nonadaptive, independently noisy values at reflection-paired sites \(-a,+a\), \(a\ge0\). Their nonnegative measurement precisions \(p_-,p_+\) satisfy \(p_-+p_+=P>0\), with zero precision denoting an omitted channel. The loss is the unconditional mean-square error of the Bayes conditional mean.

There is exactly one sharp precision threshold
\[
\boxed{P_c=\frac{\ell^2}{\tau^2}.}
\]
For \(0<P\le P_c\), the unique optimal half-separation is \(a_*=0\); every split of the total precision at the common origin is optimal. For \(P>P_c\), the unique optimal half-separation is
\[
\boxed{a_*(P)=\frac{\ell}{\sqrt2}\sqrt{\log\!\left(\frac{1+2\tau^2/\ell^2}{1+2/P}\right)}}
\]
and the **unique** optimal allocation is \(p_-=p_+=P/2\). Thus the optimal design changes from replication/aggregation at one location to two distinct equally precise mirror observations. At the threshold the location remains uniquely \(a=0\), rather than coexisting with a separated optimum.

Writing \(S=\ell^2+\tau^2\), its minimum risk for every finite \(P>0\) is
\[
\boxed{R_*(P)=\frac1{\sqrt{1+2\tau^2/\ell^2}}-
\frac{2\ell^2\exp(-a_*^2/S)}{S\,[1+2/P+\exp(-2a_*^2/\ell^2)]}.}
\]
The separation opens with the sharp square-root law
\[
a_*(P)\sim\frac{\tau^2}{\sqrt{\ell^2+2\tau^2}}\sqrt{P-P_c}
\quad\text{as }P\downarrow P_c\text{ from above},
\]
while \(a_*(P)\to\ell\sqrt{\frac12\log(1+2\tau^2/\ell^2)}\) as \(P\to\infty\).

## Assumptions and scope
The covariance amplitude is normalized to one. The measure \(N(0,\tau^2)\) is the **integration measure**, not observation noise. Conditional on the chosen sites and precisions, active sensors return \(X(-a)+\varepsilon_-\) and \(X(a)+\varepsilon_+\) with independent centered Gaussian errors of variances \(1/p_-\) and \(1/p_+\). Errors are independent of \(X\). A precision of zero means the corresponding observation is absent, not infinite-variance data inserted into a matrix. At \(a=0\) both sensors, when active, measure the same latent quantity with independent errors. The design family is exactly the reflection-paired two-site family; the *noise precisions themselves are not constrained to be symmetric*. The result does not assert optimality among unrestricted asymmetric locations, nonlinear observation channels, or adaptive designs. It holds for every \(\ell,\tau,P>0\), including the threshold and omitted-channel boundaries.

## Proof
Set \(S=\ell^2+\tau^2\), \(\alpha=1+2\tau^2/\ell^2\), and \(k_a=\exp(-2a^2/\ell^2)\). Gaussian convolution gives
\[
m_a:=\operatorname{Cov}(J,X(\pm a))=\frac{\ell}{\sqrt S}\exp\!\left(-\frac{a^2}{2S}\right),\quad
\operatorname{Var}(J)=\alpha^{-1/2}.
\]
For strictly positive precisions, the observation covariance is
\[
\Sigma_a=\begin{pmatrix}1+1/p_-&k_a\\k_a&1+1/p_+\end{pmatrix}.
\]
Gaussian conditioning says the explained variance is \(\mathcal I(a,p_-)=m_a^2\mathbf1^\mathsf T\Sigma_a^{-1}\mathbf1\). Direct inversion, writing \(p=p_-\), \(p_+=P-p\), yields the exact identity
\[
\mathcal I(a,p)=\frac{\ell^2}{S}e^{-a^2/S}
\frac{P+2(1-k_a)p(P-p)}{1+P+(1-k_a^2)p(P-p)}.\tag{1}
\]
Continuity extends (1) to precision zero, agreeing with the single active observation. At \(a=0\), \(k_a=1\), and (1) simplifies to \(\ell^2 P/[S(1+P)]\), independent of the precision split. This is the information from one effective observation of \(X(0)\) with precision \(P\).

For \(a>0\), put \(z=p(P-p)\in[0,P^2/4]\) and differentiate the rational factor in (1):
\[
\frac{\partial}{\partial z}\left[\frac{P+2(1-k_a)z}{1+P+(1-k_a^2)z}\right]
=\frac{(1-k_a)[2+P(1-k_a)]}{[1+P+(1-k_a^2)z]^2}>0.\tag{2}
\]
Thus equal precisions are strictly and uniquely optimal for every separated pair. Equation (2) also covers allocations with one omitted channel. With \(p_-=p_+=P/2\), the explained variance becomes
\[
F_P(a)=\frac{2\ell^2}{S}\frac{e^{-a^2/S}}{1+2/P+e^{-2a^2/\ell^2}}.\tag{3}
\]
Set \(s=a^2\). The logarithmic derivative of (3) is
\[
\frac{\mathrm d}{\mathrm ds}\log F_P(\sqrt s)
=\frac{(\ell^2+2\tau^2)e^{-2s/\ell^2}-\ell^2(1+2/P)}{\ell^2S[1+2/P+e^{-2s/\ell^2}]}.\tag{4}
\]
The numerator is **strictly decreasing** in \(s\ge0\), approaches a strictly negative limit, and is positive at \(s=0\) exactly when \(P>\ell^2/\tau^2\). Consequently (4) proves a unique global maximizer: \(s=0\) at or below the threshold, and otherwise the unique positive root \(e^{-2s/\ell^2}=(1+2/P)/(1+2\tau^2/\ell^2)\). Because equal precision is optimal for every positive \(a\) and every allocation at \(a=0\) ties, these are the *complete* global optima within the stated family. Subtracting (3) at the optimizer from \(\operatorname{Var}(J)\) establishes the risk formula.

For the onset, put \(P=P_c+\delta\) with \(\delta\downarrow0\). Since \(1+2/P=1+2/P_c-2\delta/P_c^2+O(\delta^2)\), expansion of the positive-root formula gives \(a_*^2=\ell^2\delta/[\alpha P_c^2]+O(\delta^2)\), proving the displayed square-root law. Sending \(P\to\infty\) proves the noiseless-spacing limit. Every step uses finite positive parameters and covers both boundary regimes.

## Verification
The standalone `verify_gaussian_design.py` independently inverts the raw two-observation covariance matrix and compares it with (1), checks each candidate against the claimed optimum over broad deterministic random grids of parameters and allocations, tests omitted channels and the exact threshold, and checks the square-root onset. Run `python3 verify_gaussian_design.py` using only the standard library. Its observed output was `PASS: 78817 independent numerical formula/competitor/boundary checks`. These finite tests support implementation and algebra but are not a substitute for the analytic strict inequalities (2) and (4), which establish the theorem for the entire continuous parameter domain.

As an illustrative exact benchmark, for \(\ell=\tau=1\), the critical precision is \(P_c=1\), the separated high-precision limit is \(\sqrt{\log3/2}\), and at \(P=10\) the optimum is \(a_*=0.6768643630278356\ldots\). The risk remains positive for every finite budget.

## Relationship to prior work
Karvonen and Särkkä (2017, arXiv:1703.06359) give efficient weights for fully symmetric kernel-quadrature node sets, but do not optimize two-location placement under a freely divisible noise-precision budget. Karvonen and Särkkä (2018, arXiv:1803.09532) study scaled Gauss–Hermite nodes and approximate Gaussian-kernel quadrature weights, including numerical comparisons; their main Theorem 2.2 does not state the precision-dependent replication threshold. Karvonen, Kanagawa, and Särkkä (2018, arXiv:1812.08509) analyze positivity/magnitude of noiseless Bayesian-quadrature weights rather than this resource-allocation phase diagram. Cai, Lam, and Scarlett (2022, arXiv:2202.10615) provide noisy kernel-quadrature error rates and algorithm-independent bounds rather than an exact fixed-two-channel Gaussian-measure design. Hayakawa, Oberhauser, and Lyons (2021, arXiv:2107.09597) construct positive-weight quadrature via subsampling under a different criterion. Published special-model kernel-design results on a rank-three circle kernel have a related collision phenomenon but neither imply nor numerically determine this Gaussian target/RBF-kernel threshold. These comparisons concern statements and hypotheses, not title similarity; they do not establish absolute historical priority.

## Limitations
Reflection-paired sites are a genuine design constraint. The proof does not establish that the same configuration is optimal when two locations can move independently, nor does it cover more than two observation channels, fixed per-channel setup costs, unequal precision costs, correlated errors, nonlinear observation design, or misspecified covariance. In particular, the square-root transition is claimed for this *mirror-pair* optimization and must not be advertised as a theorem for all two-node designs. Search cannot exclude earlier equivalent formulas outside the inspected works; independent validation of correctness and publication priority has not been performed.

## References
1. T. Karvonen and S. Särkkä, *Fully symmetric kernel quadrature*, arXiv:1703.06359 (first public version 2017-03-18), https://arxiv.org/abs/1703.06359.
2. T. Karvonen and S. Särkkä, *Gaussian kernel quadrature at scaled Gauss–Hermite nodes*, arXiv:1803.09532 (first public version 2018-03-26), https://arxiv.org/abs/1803.09532.
3. T. Karvonen, M. Kanagawa, and S. Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509 (first public version 2018-12-20), https://arxiv.org/abs/1812.08509.
4. S. Hayakawa, H. Oberhauser, and T. Lyons, *Positively Weighted Kernel Quadrature via Subsampling*, arXiv:2107.09597 (first public version 2021-07-20), https://arxiv.org/abs/2107.09597.
5. X. Cai, C. T. Lam, and J. Scarlett, *On Average-Case Error Bounds for Kernel-Based Bayesian Quadrature*, arXiv:2202.10615 (first public version 2022-02-22), https://arxiv.org/abs/2202.10615.
