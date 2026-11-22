# A sign reversal and a sharp residual covariance for two extreme circular spacings

## Finding
Let \(n\ge3\) independent uniform points divide a circle of unit circumference into the cyclic gaps \(G_1,\ldots,G_n\), with cyclic indices. Set
\[
L_n=\max_{1\le i\le n}G_i,\qquad P_n=\max_{1\le i\le n}\min(G_i,G_{i+1}).
\]
The exact three-point covariance is
\[\operatorname{Cov}(L_3,P_3)=-\frac1{81}.\]
Nevertheless, the large-sample covariance is positive and has a sharp leading constant:
\[
\boxed{\lim_{n\to\infty}n^{5/2}\operatorname{Cov}(L_n,P_n)=\sqrt\pi.}
\]
Consequently \(\operatorname{Cov}(L_n,P_n)>0\) for all sufficiently large integers \(n\). No uniqueness or location of the intervening finite-sample sign transition is asserted.

## Assumptions and scope
The points are independent with the continuous uniform distribution on a unit circle, and \(n\) is a deterministic integer. Two gaps are *neighbors* if they share a sample point; the pair \((G_n,G_1)\) is included. \(L_n\) is the longest single empty arc, whereas \(P_n\) is the largest length that can be guaranteed simultaneously by **both** gaps in some adjacent pair. This is a maximum of minima, not the classical maximal sum of consecutive spacings.

## Proof
**1. Exponential normalization and covariance identity.** Let \(X_1,\ldots,X_n\) be independent rate-one exponential random variables and \(S_n=\sum_iX_i\). The cyclic spacings have the law of \((X_i/S_n)_{i=1}^n\), and this vector is independent of \(S_n\). Write
\[ A_n=\max_iX_i,\qquad B_n=\max_i\min(X_i,X_{i+1}). \]
Then \(L_n=A_n/S_n\), \(P_n=B_n/S_n\). Independence of the normalized vector and \(S_n\), together with \(\mathbb ES_n=n\) and \(\mathbb ES_n^2=n(n+1)\), gives the exact identity
\[
\boxed{n(n+1)\operatorname{Cov}(L_n,P_n)
=\operatorname{Cov}(A_n,B_n)-\frac{(\mathbb EA_n)(\mathbb EB_n)}n.}\tag{1}
\]
In particular \(\mathbb EA_n=H_n=\sum_{j=1}^n1/j\), and \(0\le\mathbb EB_n\le H_n\).

**2. Exact joint law.** For \(0\le p\le1\), let \(R_n(p)\) be the probability that a cyclic word of \(n\) independent Bernoulli-\(p\) variables has no neighboring pair of ones. A two-state transfer matrix gives
\[
R_n(p)=\lambda_+(p)^n+\lambda_-(p)^n,\quad
\lambda_\pm(p)=\frac{1-p\pm\sqrt{(1-p)(1+3p)}}2.\tag{2}
\]
For \(u,v\ge0\), define \(p=e^{-v}\), \(q=e^{-u}\), and \(F_n(u,v)=\Pr(A_n\le u,B_n\le v)\). When \(u<v\), \(B_n\le A_n\) implies \(F_n(u,v)=(1-q)^n\). When \(u\ge v\), conditional on all \(X_i\le u\), the events \(X_i>v\) are independent with probability \(p'=(p-q)/(1-q)\), whence
\[
F_n(u,v)=(1-q)^nR_n\!\left(\frac{p-q}{1-q}\right),\quad u\ge v\ge0.\tag{3}
\]
Also \(F_{A_n}(u)=(1-e^{-u})^n\) and \(F_{B_n}(v)=R_n(e^{-v})\). For nonnegative square-integrable variables the covariance is the integrated difference of their joint and product distribution functions, so
\[
\operatorname{Cov}(A_n,B_n)=
\int_0^\infty\!\int_0^\infty
\left[F_n(u,v)-F_{A_n}(u)F_{B_n}(v)\right]du\,dv.\tag{4}
\]
All expressions in (2)–(4) are finite-size identities and give an independent numerical route to the covariance.

**3. Sharp residual dependence of the exponential extremes.** We prove
\[\lim_{n\to\infty}\sqrt n\,\operatorname{Cov}(A_n,B_n)=\sqrt\pi.\tag{5}\]
Set \(u=\log n+x\) and \(v=(\log n+y)/2\), with fixed real \(x,y\). Then \(q=n^{-1}e^{-x}\), \(p=n^{-1/2}e^{-y/2}\), and \(u>v\) for all sufficiently large \(n\). From (2), as \(p\downarrow0\),
\[
\log\lambda_+(p)=-p^2+O(p^3),\quad
\frac{d}{dp}\log R_n(p)=-2np+O(np^2)+o(1)
\]
uniformly for \(p\) in compact multiples of \(n^{-1/2}\); the second eigenvalue has exponentially negligible \(n\)-th power. Since \(p-p'=q(1-p)/(1-q)=q(1+o(1))\), (3) implies the pointwise limit
\[
\sqrt n\,[F_n(u,v)-F_{A_n}(u)F_{B_n}(v)]
\longrightarrow 2e^{-x-y/2}\exp(-e^{-x}-e^{-y}).\tag{6}
\]
The limit may be integrated. Here are explicit tail controls, rather than an appeal to pointwise convergence alone. On \(u\ge v\ge\log2\) and \(q\le p/2\), the transfer-matrix expression yields \(|R_n'(s)|\le Cns\exp(-cns^2)\) for \(s\in[p/2,p]\), with absolute constants \(c,C>0\). Hence the integrand in (6), after multiplication by \(\sqrt n\), is bounded by a constant multiple of \(e^{-x-y/2}\exp[-e^{-x}-ce^{-y}]\), which is integrable on \(\mathbb R^2\). The narrow region \(p/2<q\le p\) contributes \(O(n^{-1})\): use \(1-R_n(p)\le np^2\), the bound \((1-q)^n\le e^{-nq}\), and integrate after the substitution \(z=np\). The region \(u<v\) contributes \(O((\log n)/n)\) by the same bounds and splitting \(v\) at \(\log n\). The remaining region \(v<\log2\) contributes exponentially little, using (2) and the exponential bound for \((1-q)^n\) when \(q\) is large. Thus the complementary regions are \(o(n^{-1/2})\), establishing uniform integrability of the scaled joint-CDF difference.

The Jacobian for \((u,v)=(\log n+x,(\log n+y)/2)\) is **\(1/2\)**, so (4) and (6) give
\[
\begin{aligned}
\lim_{n\to\infty}\sqrt n\operatorname{Cov}(A_n,B_n)
&=\frac12\int_{\mathbb R^2}2e^{-x-y/2}e^{-e^{-x}-e^{-y}}\,dx\,dy\\
&=\left(\int_{\mathbb R}e^{-x}e^{-e^{-x}}dx\right)
\left(\int_{\mathbb R}e^{-y/2}e^{-e^{-y}}dy\right)
=\Gamma(1)\Gamma(1/2)=\sqrt\pi.
\end{aligned}\tag{7}
\]
Finally, \((\mathbb EA_n)(\mathbb EB_n)/n\le H_n^2/n=O((\log n)^2/n)=o(n^{-1/2})\). Substituting (5) into (1) proves the announced \(n^{5/2}\)-scaled covariance limit and eventual positivity.

**4. Negative exact boundary.** At \(n=3\), every pair of distinct gaps is neighboring, so \(B_3\) is the second largest of three independent exponentials. Their ascending-order spacings are independent exponentials with rates \(3,2,1\). Consequently \(\mathbb EA_3=11/6\), \(\mathbb EB_3=5/6\), and \(\operatorname{Cov}(A_3,B_3)=1/9+1/4=13/36\). Formula (1) becomes
\[
\operatorname{Cov}(L_3,P_3)
=\frac{13/36-(11/6)(5/6)/3}{12}=-\frac1{81}.
\]

## Verification
Run `python3 check.py` in a directory containing this document and the checker. The checker independently enumerates the cyclic Bernoulli no-adjacency event for small dimensions, verifies the transfer-matrix expression, reconstructs the exact three-gap covariance using rational arithmetic, and numerically integrates the finite-sample CDF formula at increasing sample sizes to test the predicted \(\sqrt\pi\) scaling. Numerical checks are consistency tests; the asymptotic theorem is established by the preceding estimates and not by the finite experiments.

## Relationship to prior work
Classical exponential representations of uniform spacings and Gumbel limits for their largest component are reviewed by Pyke (1965). Mijatović and Vysotsky (2015) study maxima of **sums** of consecutive spacings and use Watson's theorem for weak convergence. That is different from our maximum of adjacent **minima** and does not give the mixed covariance decay rate. Johnson and Fu (2014) discuss approximation of runs and patterns; their run-count approximation is pertinent to (2) but does not provide the normalization-induced covariance sign reversal or constant. Existing broad extreme-value and Poisson approximation theorems provide background for first-order marginal weak limits but not a stated second-order covariance result of the form (7).

## Limitations
The result does **not** identify the least positive-covariance sample size, nor claim a unique finite-sample sign change. The numerical integration supports but cannot replace the analytic asymptotic argument. No claim is made for nonuniform sampling, noncyclic boundary conventions, or maxima of sums of adjacent gaps. Historical priority cannot be proved conclusively by a literature search, and independent validation has not been performed.

## References
1. A. Mijatović and V. Vysotsky, *On the weak limit law of the maximal uniform k-spacing*, arXiv:1508.00944 (first posted 2015-08-05), https://arxiv.org/abs/1508.00944.
2. R. Pyke, *Spacings*, Journal of the Royal Statistical Society, Series B 27 (1965), 395–449, https://doi.org/10.1111/j.2517-6161.1965.tb00602.x.
3. B. C. Johnson and J. C. Fu, *Approximating the distributions of runs and patterns*, Journal of Statistical Distributions and Applications 1 (2014), article 5, https://doi.org/10.1186/2195-5832-1-5.
4. G. S. Watson, *Extreme values in samples from m-dependent stationary stochastic sequences*, Annals of Mathematical Statistics 25 (1954), 798–800.
