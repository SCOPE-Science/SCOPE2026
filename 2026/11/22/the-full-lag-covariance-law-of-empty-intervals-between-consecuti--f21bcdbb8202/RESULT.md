# The full lag-covariance law of empty intervals between consecutive powers

## Finding

Fix an integer \(k\ge2\). Let \(H_k(n)\) equal one when the open interval \((n^k,(n+1)^k)\) contains no \(k\)-full integer, and zero otherwise. An integer is \(k\)-full when every prime dividing it occurs to exponent at least \(k\). Perfect \(k\)th powers do not lie in the open interval, so this is also the no-*nonpower* indicator.

Set
\[
\Lambda_k=\left\{(b_1^{k+1}\cdots b_{k-1}^{2k-1})^{1/k}:b_j\ge1,\ \prod_{j=1}^{k-1}b_j\ge2\text{ is squarefree}\right\},
\qquad p_\lambda=\lambda^{-1},
\]
\[
D_k=\prod_{\lambda\in\Lambda_k}(1-p_\lambda),\qquad
C_k=\prod_{\lambda\in\Lambda_k}(1-2p_\lambda).
\]
For \(s\in[0,1)\), define the circular overlap function
\[
g_p(s)=(p-s)_++(p+s-1)_+,\qquad a_+=\max(a,0).
\]
For every positive integer \(t\), the limiting covariance
\[
R_k(t)=\lim_{N\to\infty}\frac1N\sum_{n=1}^N H_k(n)H_k(n+t)-D_k^2
\]
exists and has the absolutely convergent product
\[
R_k(t)=\prod_{\lambda\in\Lambda_k}
\left(1-2p_\lambda+g_{p_\lambda}(\{tp_\lambda\})\right)-D_k^2.
\tag{1}
\]
Here \(\{x\}\) denotes fractional part.

**Lag-distribution theorem.** For any bounded continuous function \(F:\mathbb R\to\mathbb R\),
\[
\lim_{T\to\infty}\frac1T\sum_{t=1}^T F(R_k(t))
=\mathbb E F(Z_k),
\quad
Z_k=\prod_{\lambda\in\Lambda_k}
(1-2p_\lambda+g_{p_\lambda}(U_\lambda))-D_k^2,
\tag{2}
\]
where the \(U_\lambda\) are independent uniform random points of the unit circle. This law has support exactly
\[
[C_k-D_k^2,\;D_k-D_k^2],
\tag{3}
\]
which is also the set of subsequential limits of \(R_k(t)\) for \(t\to\infty\). It has a **unique atom** at \(C_k-D_k^2\) with probability exactly \(C_k>0\); off that point its measure is absolutely continuous. Its first two moments are
\[
\mathbb EZ_k=0,
\qquad
\operatorname{Var}(Z_k)=
\prod_{\lambda\in\Lambda_k}
\left((1-p_\lambda)^4+\frac23p_\lambda^3-p_\lambda^4\right)-D_k^4>0.
\tag{4}
\]
In particular, the zero-window indicator has persistent correlations of both signs at arbitrarily large integer lags; those correlations do not converge to zero.

## Assumptions and scope

The integer \(k\ge2\) is fixed throughout. The first average is over starting indices \(n\), with \(t\ge1\) fixed before \(N\to\infty\). The second average is over integer lags \(t\), *after* these first limits have been taken. These are distinct limiting procedures. All products run over the explicit infinite set \(\Lambda_k\), not a finite truncation. The proven elementary bounds \(\lambda>2\) and \(\sum_{\lambda\in\Lambda_k}1/\lambda<\infty\) ensure convergence. The same proof applies to any fixed \(k\), without a uniform error estimate as \(k\) varies.

## Proof

**1. Arithmetic rays and independence.** Unique factorization gives the disjoint decomposition of non-perfect-power \(k\)-full integers into rays \((a\lambda)^k\), with \(a\ge1\) integer and \(\lambda\in\Lambda_k\). Narumi and Tachiya [1, Lemma 2] prove that for every finite set of distinct parameters \(\lambda_1,\ldots,\lambda_m\), the numbers \(1,p_{\lambda_1},\ldots,p_{\lambda_m}\) are rationally linearly independent, by Besicovitch's fractional-power theorem. Consequently the Kronecker–Weyl theorem equidistributes \((\{np_{\lambda_j}\})_{j\le m}\) on the \(m\)-torus. Their equation (10) gives the required summability; directly, dropping the squarefree restriction bounds the sum by \(\prod_{j=1}^{k-1}\zeta(1+j/k)-1<\infty\). Each \(p_\lambda<1/2\).

**2. First limiting correlation and control of infinite tails.** The ray indexed by \(\lambda\) meets the open window \((n^k,(n+1)^k)\) if and only if \(\{np_\lambda\}\in(1-p_\lambda,1)\). The excluded arc on the unit circle has length \(p_\lambda\). Its intersection with a translate by \(tp_\lambda\) has length \(g_{p_\lambda}(\{tp_\lambda\})\). Hence the probability of missing the ray in both windows, over equidistributed phases, equals \(1-2p_\lambda+g_{p_\lambda}(\{tp_\lambda\})\). Independence for any *finite* set of parameters proves the finite-product version of (1), together with the finite-product one-window density.

To pass from a finite set \(E\subset\Lambda_k\) to all rays, note that each ray contributes at most \(\lfloor(N+t+1)/\lambda\rfloor\) nonpower integers whose \(k\)th roots lie below \(N+t+1\). Each such number can occupy at most one of the integer-indexed unit windows. The number of starting indices \(1\le n\le N\) for which either window meets a ray outside \(E\) is thus at most \(2(N+t+1)\sum_{\lambda\notin E}p_\lambda\). After division by \(N\) and fixing \(t\), this tends uniformly to zero as \(E\) exhausts \(\Lambda_k\). Since every factor lies in \([1-2p_\lambda,1-p_\lambda]\), the product also converges absolutely. This gives (1) and the density \(D_k\).

**3. Equidistribution over *lags*.** Define \(R_{k,E}(t)\) by retaining \(E\) in both products. From \(0\le g_p\le p\) we have, uniformly in \(t\),
\[
|R_k(t)-R_{k,E}(t)|\le4\sum_{\lambda\notin E}p_\lambda.
\tag{5}
\]
For fixed finite \(E\), rational independence gives joint equidistribution of \((\{tp_\lambda\})_{\lambda\in E}\). Thus averages of bounded continuous tests of \(R_{k,E}(t)\) converge to their Haar expectations. The uniform tail bound (5), uniform continuity on the bounded correlation interval, and then exhaustion of \(E\) establish (2). The independent-product random variables in (2) converge uniformly with respect to all phases by the same summable tail argument.

**4. Exact support, atom, and absence of other atoms.** Each local factor ranges continuously over \([1-2p,1-p]\); the infinite product is a continuous function on the compact connected infinite torus because of uniform tail convergence. Its image is therefore exactly the interval between the products of its coordinate minima and maxima, which are \(C_k\) and \(D_k\). The finite-lag phases are dense in every finite-dimensional projection by Kronecker, and the product is uniformly approximable by finitely many coordinates, so every point of this image is a limit along arbitrarily large integer lags. This proves (3) and the full cluster-set claim.

For a uniform phase \(U\), the local overlap \(g_p(U)\) is zero with probability exactly \(1-2p\). Conditional on being positive, its law is uniform on \((0,p)\) (two equal linear triangular wings). Therefore the product is at its minimum exactly when *every* coordinate is in its flat arc; this event has probability \(\prod(1-2p_\lambda)=C_k\). On its complement, choose the first coordinate at which the overlap is positive in any fixed enumeration. Conditional on all other coordinates, that coordinate has a continuous density on a nondegenerate interval, and all remaining factor products are strictly positive. The countable union over possible first coordinates shows that the remaining law is absolutely continuous. Thus there is exactly one atom.

**5. Moment calculation and nontriviality.** For \(U\) uniform and \(0<p<1/2\), direct integration of the two linear wings yields
\[
\mathbb E g_p(U)=p^2,\qquad
\mathbb E[g_p(U)^2]=\frac23p^3.
\]
Writing \(f_p=1-2p+g_p(U)\), it follows that
\[
\mathbb Ef_p=(1-p)^2,
\quad
\mathbb Ef_p^2=(1-p)^4+\frac23p^3-p^4.
\]
Independence and bounded convergence prove (4). Since every \(p_\lambda\in(0,1/2)\), the correction \(p_\lambda^3(2/3-p_\lambda)\) is strictly positive; the overall variance is positive. Finally \(0<C_k<D_k^2<D_k<1\), because \(1-2p<(1-p)^2\) for each \(p>0\). Thus the support extends strictly across zero, proving nonvanishing correlations of both signs at arbitrarily large lags.

## Verification

The accompanying standard-library script `verify_autocorrelation.py` carries out exact-integer ray-membership enumeration for eight squarefree bases of the \(k=2\) family over 500,000 windows, compares the observed pair frequencies at seven lags with the finite-parameter torus products, checks the two local overlap integrals numerically, and checks the exact endpoint and variance expressions. It reports the numerical tolerances explicitly. These finite tests corroborate algebraic formulas only. The infinite limiting statements are proved above using rational independence, torus equidistribution, and summable tails.

To reproduce: `python3 verify_autocorrelation.py` (Python standard library only).

## Relationship to prior work

Xiong and Zaharescu [3] established one-window count distributions. Narumi and Tachiya [1, Theorems 1–2] extend these to two **adjacent** power intervals; their Corollary 1 already proves the density \(C_k\) of simultaneous empty adjacent windows, so neither that density nor the one-window product \(D_k\) is new. Their Lemma 2 supplies the rational-independence input, which is used here explicitly rather than claimed as new. Their more recent paper [2] concerns large values and first occurrences of window counts.

The contribution here is the *entire integer-lag covariance spectrum* and its **second-level limiting probability law over shifts**, notably the unique point mass, absolutely continuous remainder, precise interval support/cluster set, and strict positive variance formula. A single fixed-shift extension of [1] would not establish those distributional and measure-type statements.

## Limitations

The result does not give effective convergence rates in \(n\) or in the subsequent lag limit \(T\), nor a simple closed form for the density of the absolutely continuous component. It concerns the empty-window indicator, not the full multi-lag joint distribution of all window counts. Its proof uses the published fractional-power linear-independence lemma. Implicit earlier results on infinite-dimensional Kronecker codings might subsume the general method; the exact arithmetic specialization and full law have been compared with the identified primary literature, but exhaustive literature coverage is not claimed.

## References

[1] Shusei Narumi and Yohei Tachiya, “On the number of \(k\)-full integers between three successive \(k\)th powers,” arXiv:2512.07438, first publicly posted 2025-12-08. https://arxiv.org/abs/2512.07438

[2] Shusei Narumi and Yohei Tachiya, “On the behavior of the number of \(k\)-full integers between successive \(k\)-th powers,” arXiv:2611.20656, first publicly posted 2026-11-16. https://arxiv.org/abs/2611.20656

[3] Maosheng Xiong and Alexandru Zaharescu, “\(k\)-full integers between successive \(k\)-th powers,” *Indagationes Mathematicae* 22 (2011), 77–86, doi:10.1016/j.indag.2011.08.003.

[4] A. S. Besicovitch, “On the linear independence of fractional powers of integers,” *Journal of the London Mathematical Society* 15 (1940), 3–6, as invoked in [1, Lemma 2].
