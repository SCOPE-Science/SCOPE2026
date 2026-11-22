# Sharp phase-count and order-cost barriers for rotationally symmetric Gaussian derivative estimation

## Finding

There are two sharp resource boundaries for the one-dimensional rotationally symmetric Stein estimator (RSSE), when the smoothing radius tends to zero and derivative order is allowed to vary.

**Sharp phase threshold.** Fix any integer \(p\ge2\) and any phase count \(n\ge1\). Bounded limiting variance for *every* input satisfying the source's boundedness and local-analyticity assumptions holds if and only if \(n\ge p\). The sufficiency half is Theorem 5 of Fang–Wang–Zeng–Zhou [1]. For \(n<p\), put \(m=1+((p-1)\bmod n)\), so \(1\le m<p\) and \(n\mid(p-m)\). There is an explicit globally bounded, locally analytic real-on-real input with \(u^{(p)}(0)=1\) for which

\[
\operatorname{Var}(\mathcal E_{p,n,\sigma}[u])\sim
C_{p,m}\,\sigma^{-2(p-m)},\qquad
C_{p,m}=\frac{(2m)!}{(m!)^2}\sum_{j=0}^{m}
\frac{(p-j)!\binom pj^{2}}{2^{m-j}(m-j)!}>0.
\]

In particular, with just one phase fewer than the derivative order, \(n=p-1\), the exact leading coefficient is \(C_{p,1}=(2p+1)p!\) and the variance grows like \(\sigma^{-2(p-1)}\).

**Sharp order-dependent Monte Carlo cost.** At every adequate phase count \(n\ge p\), there is an explicit bounded, locally analytic input with \(u^{(p)}(0)=1\) and the *same* limiting single-probe variance

\[
V_p=\binom{2p}{p}\sum_{k=0}^{p}\frac{\binom pk^2}{2^k}-1
=\binom{2p}{p}2^{-p}P_p(3)-1,
\]

where \(P_p\) is the ordinary Legendre polynomial. As \(p\to\infty\),

\[
\boxed{\displaystyle V_p\sim
\frac{1+\sqrt2}{\pi 2^{5/4}}\,
\frac{(6+4\sqrt2)^p}{p}.}
\]

Thus, even when \(n\ge p\) removes smoothing-radius variance divergence, for these normalized witnesses a sample mean of \(K\) independent probes has limiting mean-square error \(V_p/K\), so a fixed target mean-square error requires \(K\) of exponential order in \(p\). Increasing \(n\) above \(p\) does not change this limiting variance. The two assertions are a single classification of phase-budget and sampling-budget barriers for this estimator; neither is a minimax lower bound over all possible differentiation methods.

## Assumptions and scope

Let \(X\sim N(0,1)\); let \(H_p\) be the *probabilists'*, monic Hermite polynomial, defined by \(H_0=1\), \(H_1(x)=x\), and \(H_{p+1}(x)=xH_p(x)-pH_{p-1}(x)\). For positive \(\sigma\), integers \(p\ge2,n\ge1\), and \(\omega=e^{2\pi i/n}\), define

\[
\mathcal E_{p,n,\sigma}[u](X)
=\frac{H_p(X)}n\sum_{j=0}^{n-1}
(\sigma\omega^j)^{-p}\bigl[u(\sigma\omega^jX)-u(0)\bigr].
\]

All variances refer to this real-valued random estimator for the explicitly constructed inputs below. The admissible class consists of measurable \(u:\mathbb C\to\mathbb C\) that are globally bounded, real-valued on the real line, and holomorphic on a disk centered at zero. The source's local-analyticity condition requires no holomorphy outside that disk.

For any \(1\le m\le p\), let

\[
u_{p,m}(z)=\begin{cases}z^m/m!+z^p/p!,&|z|\le1,\ m<p,\\ z^p/p!,&|z|\le1,\ m=p,\\ 0,&|z|>1.\end{cases}\]

These inputs are bounded and analytic on the open unit disk, and satisfy \(u_{p,m}^{(p)}(0)=1\). The first theorem uses \(u_{p,m}\) with \(m<p\) as prescribed by \(n\); the second uses \(u_{p,p}\). For the sample-cost asymptotic, first take \(\sigma\downarrow0\) at each *fixed* \(p\), then take \(p\to\infty\). The number of Gaussian probes \(K\) is independent of the phase count \(n\).

## Proof

**1. Root-of-unity filtering and exact sample laws.** For integer \(s\), \(\frac1n\sum_{j=0}^{n-1}\omega^{js}=\mathbf1_{\{n\mid s\}}\). Because every evaluation at \(\sigma\omega^jX\) has the same modulus \(\sigma|X|\), the cutoff is shared by all phases. For \(m<p\) with \(n\mid(p-m)\), therefore, for *every* \(\sigma>0\),

\[
\mathcal E_{p,n,\sigma}[u_{p,m}](X)=
\mathbf1_{\{|X|\le\sigma^{-1}\}}H_p(X)
\left(\sigma^{m-p}\frac{X^m}{m!}+\frac{X^p}{p!}\right).
\]

For \(m=p\) and \(n\ge p\), the same calculation yields

\[
\mathcal E_{p,n,\sigma}[u_{p,p}](X)=
\mathbf1_{\{|X|\le\sigma^{-1}\}}H_p(X)\frac{X^p}{p!}.
\]

**2. Undersampling divergence.** Orthogonality gives \(\mathbb E[H_p(X)X^m]=0\) for \(m<p\). For any fixed polynomial \(Q\) and nonnegative integer \(r\), \(\mathbb E[|Q(X)|\mathbf1_{\{|X|>\sigma^{-1}\}}]=o(\sigma^r)\), by Gaussian tails. Consequently the variance of the first exact law, multiplied by \(\sigma^{2(p-m)}\), converges to \(\mathbb E[H_p(X)^2X^{2m}]/(m!)^2>0\); contributions from the second summand and squares of means are asymptotically negligible. The Hermite product identity

\[
H_p(X)^2=\sum_{k=0}^{p}k!\binom pk^2H_{2p-2k}(X)
\]

and \(\mathbb E[H_{2j}(X)X^{2m}]=(2m)!/[2^{m-j}(m-j)!]\) for \(0\le j\le m\), zero for \(j>m\), yield the finite positive formula for \(C_{p,m}\). At \(m=1\), the two surviving terms give \((2p+1)p!\). Thus every \(n<p\) fails the asserted uniform bounded-variance guarantee. For \(n\ge p\), the existing Theorem 5 [1], under exactly the stated admissible assumptions, proves bounded variance; together these establish necessity and sufficiency.

**3. Fixed-order variance formula.** For \(u_{p,p}\), the exact law above converges in \(L^2\) as \(\sigma\downarrow0\) to \(H_p(X)X^p/p!\). Gaussian integration by parts gives \(\mathbb E[H_p(X)X^p]=p!\). Its variance is therefore

\[
V_p=\frac{\mathbb E[H_p(X)^2X^{2p}]}{(p!)^2}-1
=\binom{2p}{p}\sum_{k=0}^{p}2^{-k}\binom pk^2-1.
\]

The binomial–Legendre polynomial identity \(\sum_{k=0}^p\binom pk^2t^k=(1-t)^pP_p((1+t)/(1-t))\), applied at \(t=1/2\), proves the alternative expression. Since every \(n\ge p\) produces the same exact single-sample law for this witness, the variance cannot be reduced by adding more phases on this example.

**4. Sharp growing-order rate.** For \(x>1\), the standard integral representation

\[
P_p(x)=\frac1\pi\int_0^\pi\bigl(x+\sqrt{x^2-1}\cos\theta\bigr)^p\,d\theta
\]

combined with Laplace's method at the unique maximum \(\theta=0\) gives

\[
P_p(3)\sim\frac{(3+2\sqrt2)^{p+1/2}}{2^{3/4}\sqrt{2\pi p}}.
\]

Also \(\binom{2p}{p}\sim4^p/\sqrt{\pi p}\). Multiplication by \(2^{-p}\) gives the displayed constant and base \(2(3+2\sqrt2)=6+4\sqrt2\). The subtracted one is negligible. For \(K\) independent samples, the zero-radius limit is unbiased, with variance \(V_p/K\), proving the stated sample-cost law.

## Verification

The accompanying standalone `verify.py` uses Python standard-library exact integer and rational arithmetic to check Hermite orthogonality, the product moment identity, the explicit positive coefficient for all specified test orders, exact root-of-unity filtering, the Legendre identity, and growing-order numerical ratios. Running `python3 verify.py` prints `VERIFY_OK 1721`. These finite checks are corroboration only: the proof above supplies the quantified all-order claims.

## Relationship to prior work

Fang, Wang, Zeng, and Zhou [1], equations (13)–(17), establish the roots-of-unity filter and fixed-order limiting variance structure; Theorem 5 proves sufficiency of \(n\ge p\). These are explicitly **prior results**, not discoveries claimed here. New claims are the necessity side with exact blowup constants for every undersampled phase count, and the evaluated exact variance plus sharp growing-derivative sample complexity on admissible witnesses. The work's general finite-order variance formula implies the starting expression for the second calculation, but does not state the Legendre evaluation or high-order exponential rate. The classical binomial–Legendre identity and Laplace method themselves are standard tools.

Bornemann [2] analyzes high-order numerical differentiation via deterministic Cauchy integrals, where contour-radius selection controls floating-point accuracy; this differs from randomized Hermite-weighted Gaussian probe variance. Shi, Hu, Lin, and Kawaguchi [3] investigate stochastic Taylor-mode automatic differentiation, a different sampling construction. The comparison does not rule out all unindexed literature on the same joint phase/sample bounds.

## Limitations

The classification is for one spatial dimension and the specified roots-of-unity RSSE. The witnesses are globally bounded and locally holomorphic but not entire (their cutoff is discontinuous outside the analytic neighborhood). They depend on derivative order and, for undersampling, phase count. The exponential statement concerns a particular normalized input family, independent Gaussian probes, and the sequential limits \(\sigma\downarrow0\) then \(p\to\infty\). It does not imply an exponential lower bound for every input, all alternative estimators, or a hardware cost theorem; it does not contest stable performance at the modest derivative orders tested in [1].

## References

1. S. Fang, X. Wang, H. Zeng, T. Zhou. *Variance Stable Gaussian Smoothing Estimator for Arbitrary High-order Derivatives*, arXiv:2611.19909v1, first posted November 15, 2026. https://arxiv.org/html/2611.19909v1
2. F. Bornemann. *Accuracy and Stability of Computing High-Order Derivatives of Analytic Functions by Cauchy Integrals*, arXiv:0910.1841 (2009). https://arxiv.org/abs/0910.1841
3. X. Shi, Z. Hu, X. Lin, K. Kawaguchi. *Stochastic Taylor Derivative Estimator: Efficient and Accurate High-Order Derivatives for Neural Networks*, arXiv:2412.00088 (2024). https://arxiv.org/abs/2412.00088
