# A disconnected infinite-divisibility phase diagram for zero-modified Poisson–Lindley counts

## Finding

For every \(\theta>0\), the zero-modified Poisson–Lindley law is **ordinarily infinitely divisible as a real-valued probability distribution if and only if**
\[
\boxed{\pi=\pi_{\min}(\theta)\quad\text{or}\quad\pi\geq \pi_*(\theta):=-\frac{\theta^2(2\theta+3)}{(\theta+2)^2(2\theta+1)}.}
\]
Here \(\pi_{\min}\) is the zero-truncation endpoint. On the nontruncated branch, the equivalent condition at fixed \(\theta\) is that the probability of zero satisfy
\[
\Pr(X=0)\geq\frac{\theta^2(2\theta+5)}{(\theta+2)^2(2\theta+1)}.
\]
All infinitely divisible members have explicit compound-Poisson representations: **unshifted** on the nontruncated branch and **shifted by one** at the isolated zero-truncation endpoint. Under the stricter requirement that every convolution root be nonnegative integer-valued, the exact condition is just \(\pi\geq\pi_*\). For parameters strictly between truncation and the threshold, infinitely many even-degree logarithmic probability-generating-function coefficients are negative. Moreover, for any fixed positive integer \(N\), some non-infinitely-divisible members arbitrarily close below the boundary have their first \(N\) logarithmic coefficients all strictly positive. Thus no fixed finite list of canonical-coefficient checks detects the entire forbidden region.

At \(\theta=1\), the threshold is \(\pi_*=-5/27\), equivalently \(\Pr(X=0)=7/27\). The admissible choice \(\pi=-1/3\) is already outside the infinitely divisible region: its degree-two logarithmic coefficient equals \(-3/4\), although its variance-to-mean ratio is \(5/3>1\).

## Assumptions and scope

Let \(X\) take values in \(\mathbb N_0=\{0,1,2,\ldots\}\). Fix \(\theta>0\) and let
\[
\pi_{\min}(\theta)=-\frac{\theta^2(\theta+2)}{\theta^2+3\theta+1}\leq\pi\leq1.
\]
The mass function, as defined in the 2017 zero-modified Poisson–Lindley model, is
\[
\begin{aligned}
\Pr(X=0)&=\pi+(1-\pi)\frac{\theta^2(\theta+2)}{(\theta+1)^3},\\
\Pr(X=k)&=(1-\pi)\frac{\theta^2(k+\theta+2)}{(\theta+1)^{k+3}},\qquad k\geq1.
\end{aligned}
\]
Ordinary infinite divisibility refers to \(m\)-fold convolution roots on the **real line** for every positive integer \(m\). We also distinguish infinite divisibility with roots constrained to \(\mathbb N_0\). The degenerate law at zero (\(\pi=1\)) is included. The criterion used below is the standard characterization: a nondegenerate law on \(\mathbb N_0\) with positive zero mass is infinitely divisible precisely when its probability-generating function can be written \(\exp(\sum_{n\geq1}\lambda_n(z^n-1))\) with summable nonnegative \(\lambda_n\).

## Proof

**1. Rational generating function.** Put \(t=\theta+1>1\) and \(c=\theta^2/t\). Direct summation gives the base Poisson–Lindley generating function and its zero-modification:
\[
F(z)=c\frac{t+1-z}{(t-z)^2},\qquad
G(z)=\pi+(1-\pi)F(z)=\frac{N(z)}{(t-z)^2},
\]
with
\[
N(z)=\pi(t-z)^2+(1-\pi)c(t+1-z).
\]
In particular, \(G(1)=1\). If \(p_0=G(0)>0\), factor every finite zero \(r_j\) of the numerator, with multiplicity, to obtain
\[
\log G(z)=\log p_0+\sum_{n\geq1}\lambda_n z^n,
\qquad
\lambda_n=\frac{2t^{-n}-\sum_j r_j^{-n}}{n}.
\]
Here a missing numerator zero contributes zero, as happens at \(\pi=0\). This expansion is initially local at \(z=0\); on the accepted region all numerator zeros have modulus at least \(t>1\), so it also converges absolutely at \(z=1\).

**2. Nonnegative modification.** For \(0<\pi<1\), set \(s=t-z\) and \(b=(1-\pi)c>0\). Numerator zeros solve \(\pi s^2+bs+b=0\). Both solutions have strictly negative real part, since they are either negative reals or a conjugate pair with real part \(-b/(2\pi)\). Thus each corresponding \(r_j=t-s_j\) has real part exceeding \(t\), hence \(|r_j|>t\). Therefore \(\sum_j\Re(r_j^{-n})\leq2\max_j|r_j|^{-n}<2t^{-n}\), so \(\lambda_n>0\) for every \(n\). At \(\pi=0\), the only numerator zero is \(t+1\), giving \(\lambda_n=[2t^{-n}-(t+1)^{-n}]/n>0\). At \(\pi=1\), \(G(z)=1\) and the law is degenerate at zero.

**3. Negative modification and the unique crossing.** For \(\pi_{\min}<\pi<0\), put \(q=(1-\pi)c/(-\pi)>0\). In the variable \(s=t-z\), the numerator equation is \(s^2-q(s+1)=0\), with solutions
\[
s_\pm=\frac{q\pm\sqrt{q^2+4q}}2,\quad
\rho=t-s_+,\quad\eta=t-s_-.
\]
We have \(\eta>t\). As \(\pi\) increases from \(\pi_{\min}\) to zero, \(q\) increases strictly, so \(\rho\) decreases strictly from zero to minus infinity. Hence there is a single parameter at which \(\rho=-t\). Substituting \(z=-t\) in \(N(z)=0\) yields
\[
\pi_*(\theta)=-\frac{c(2t+1)}{4t^2-c(2t+1)}
=-\frac{\theta^2(2\theta+3)}{(\theta+2)^2(2\theta+1)}.
\]
This is strictly above the admissible lower endpoint because
\[
\pi_*-\pi_{\min}
=\frac{\theta^2(\theta+1)^3(2\theta+5)}{(\theta+2)^2(2\theta+1)(\theta^2+3\theta+1)}>0.
\]
Thus \(\rho\leq-t\) exactly when \(\pi\geq\pi_*\) within the negative-modification range.

For \(\pi_*\leq\pi<0\), every odd-degree coefficient is
\[
\lambda_n=\frac{2t^{-n}+|\rho|^{-n}-\eta^{-n}}n>0
\quad(n\text{ odd}),
\]
while for even \(n\),
\[
\lambda_n=\frac{2t^{-n}-|\rho|^{-n}-\eta^{-n}}n
\geq\frac{t^{-n}-\eta^{-n}}n>0.
\]
Because all logarithmic coefficients are nonnegative and summable, \(G(1)=1\) implies \(\sum_{n\geq1}\lambda_n=-\log p_0\); therefore \(G(z)=\exp\{\sum_{n\geq1}\lambda_n(z^n-1)\}\), a compound-Poisson generating function with jump intensities \(\lambda_n\) and, when nondegenerate, jump probabilities \(\lambda_n/(-\log p_0)\).

For \(\pi_{\min}<\pi<\pi_*\), one has \(-t<\rho<0\). In this region
\[
\lambda_{2m}=\frac{2t^{-2m}-|\rho|^{-2m}-\eta^{-2m}}{2m}
\sim -\frac{|\rho|^{-2m}}{2m}<0\quad(m\to\infty),
\]
since \(0<|\rho|<t<\eta\). The necessary nonnegative canonical-coefficient condition fails. At \(\pi=\pi_{\min}\), \(p_0=0\) and the law has support beginning at one, so it cannot have infinitely divisible roots all supported on \(\mathbb N_0\). This establishes the classification for \(\pi>\pi_{\min}\). Indeed, because \(p_0>0\) and the law is supported on \(\mathbb N_0\), any real-valued convolution root is also supported on \(\mathbb N_0\): a root cannot take negative values, has a positive atom at zero, and any noninteger positive value together with zero-valued copies would produce a noninteger sum. Thus the compound-Poisson coefficient obstruction also rules out ordinary real-valued infinite divisibility in the open excluded interval.

**4. Isolated infinitely divisible truncation endpoint.** At \(\pi=\pi_{\min}\), \(G(0)=0\), but ordinary infinite divisibility on the real line need not fail: a deterministic integer shift is itself divisible into fractional real-valued shifts. Writing \(G(z)=zH(z)\), direct summation of the positive-count masses gives
\[
H(z)=p_1\frac{1-u z}{(1-z/t)^2},\qquad
p_1=(1-\pi_{\min})\frac{\theta^2(\theta+3)}{t^4},\quad
u=\frac{\theta+2}{t(\theta+3)}<\frac1t.
\]
The sole numerator zero of \(H\) is \(1/u>t\). Therefore the logarithmic coefficients of \(H\) are
\[
\mu_n=\frac{2t^{-n}-u^n}{n}>0\qquad(n\geq1).
\]
Since \(H(1)=1\), it is a compound-Poisson generating function and \(G(z)=z\exp\{\sum_{n\geq1}\mu_n(z^n-1)\}\). Thus the truncated law is the sum of deterministic one and an independent compound-Poisson count. For each \(m\) it has real-valued i.i.d. convolution roots equal in law to \(1/m\) plus a compound-Poisson count with jump intensities \(\mu_n/m\). Its minimum support point one rules out roots supported entirely on \(\mathbb N_0\). Together with Step 3 this proves the claimed **disconnected ordinary-infinite-divisibility set**, with the strictly excluded open interval \(\pi_{\min}<\pi<\pi_*\).

**5. Zero-probability form and finite-test obstruction.** Substituting \(\pi_*\) into \(p_0\) simplifies to \(\theta^2(2\theta+5)/[(\theta+2)^2(2\theta+1)]\). At \(\pi=\pi_*\), every coefficient \(\lambda_n\) is strictly positive. Each of the first \(N\) coefficients varies continuously with \(\pi\) near this interior admissible parameter, because \(p_0>0\). Thus for any \(N\) a sufficiently close \(\pi<\pi_*\) has \(\lambda_1,\ldots,\lambda_N>0\), but the preceding argument forces negative even coefficients at sufficiently large indices.

At \(\theta=1\), \(\pi=-1/3\), the first masses are \(p_0=1/6\), \(p_1=1/3\), \(p_2=5/24\). Consequently
\[
\lambda_2=\frac{p_2}{p_0}-\frac{p_1^2}{2p_0^2}=-\frac34.
\]
The model's first two moments give \(\mathbb E X=2\) and \(\operatorname{Var}(X)=10/3\), showing that overdispersion alone does not ensure compound-Poisson divisibility.

## Verification

The standalone `checker.py` independently derives the first canonical coefficients from exact probability masses via \(k p_k=\sum_{j=1}^k j\lambda_j p_{k-j}\), rather than relying solely on the numerator-root expansion. It checks normalization, admissibility, root locations at the threshold, exact rational examples on both sides, 74 critical-boundary jump intensities, and positive initial coefficients just below the boundary. Run with `python checker.py` in an environment with SymPy. The proof of all-degree positivity and eventual negativity is analytic; no finite numerical search is used to infer either infinite assertion.

## Relationship to prior work

Xavier, Santos-Neto, Bourguignon and Tomazella (first public preprint, 12 December 2017) define the zero-modified Poisson–Lindley family and study estimation and zero inflation/deflation, but the material inspected does not contain a sharp infinite-divisibility classification including the isolated shifted endpoint. The standard theorem characterizing infinitely divisible nonnegative integer laws as compound-Poisson laws is established prior work of Steutel and van Harn and related literature. A published classification for **zero-inflated negative-binomial counts of fixed integer shape** treats a different parent family and modification domain: neither its distribution formula nor its result yields the present threshold for a zero-deflated mixture of geometric and shape-two negative-binomial counts. Relevant subsequent Poisson–Lindley regression and autoregressive papers focus on modeling and estimation, not the displayed all-parameter boundary in the accessible material.

## Limitations

This result distinguishes ordinary real-valued infinite divisibility from the stronger requirement of nonnegative integer-valued convolution roots. It does not address binomial-thinning self-decomposability, all possible multivariate extensions, or inference properties. The sharp zero-modification boundary is model-specific and does not imply an identical cutoff for other zero-modified count families. Historical priority remains subject to examination of inaccessible earlier publications, especially the full 2021 autoregressive article and earlier conference literature. A reproduction script checks exact finite cases but is not itself a proof of the infinite sign claims, which are proved above. Independent mathematical validation has not been performed.

## References

1. D. Xavier, M. Santos-Neto, M. Bourguignon and V. Tomazella, *Zero-Modified Poisson-Lindley distribution with applications in zero-inflated and zero-deflated count data*, initial arXiv submission 12 December 2017, https://arxiv.org/abs/1712.04088 .
2. K. van Harn and F. W. Steutel, *Generalized renewal sequences and infinitely divisible lattice distributions*, Stochastic Processes and their Applications 5 (1977), 47–55, https://doi.org/10.1016/0304-4149(77)90049-7 .
3. W. Bertoli, K. S. Conceição, M. G. Andrade and F. Louzada, *Bayesian approach for the zero-modified Poisson–Lindley regression model*, Brazilian Journal of Probability and Statistics 33 (2019), 826–860, https://doi.org/10.1214/19-BJPS447 .
4. M. Sharafi, Z. Sajjadnia and A. Zamani, *A first-order integer-valued autoregressive process with zero-modified Poisson-Lindley distributed innovations*, first online 25 January 2021, https://doi.org/10.1080/03610918.2020.1864644 .
