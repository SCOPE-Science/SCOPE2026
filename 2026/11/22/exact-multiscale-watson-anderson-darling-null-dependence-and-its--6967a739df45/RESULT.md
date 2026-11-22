# Exact multiscale Watson–Anderson–Darling null dependence and its nonvanishing correlation floor

## Finding

For every integer sample size \(n\ge 2\) and generalized Watson integration order \(m\ge2\), consider the ordinary Anderson–Darling statistic \(A_n\) and the order-\(m\) generalized Watson statistic \(U_n^{[m]}\), computed on the **same** independent sample under a fully specified continuous null. Then
\[
\boxed{\operatorname{Cov}(A_n,U_n^{[m]})=\frac{n-1}{n}\,\kappa_m},
\qquad
\kappa_m=\frac{2(-1)^{m-1}}{(2m)!}\int_0^1 B_{2m}(z)\,[2(1-z)+4z\log z] \,dz>0.
\]
Here \(B_{2m}\) is the ordinary Bernoulli polynomial. Every \(\kappa_m\) is a **positive rational number**; the first new instances are \(\kappa_2=7/10800\), \(\kappa_3=41/2540160\), and \(\kappa_4=19/46656000\).

Put \(a=\pi^2/3-3\) and \(b=4-\pi^2/3\). Exact variances are
\[
\operatorname{Var}(A_n)=\frac{b+2(n-1)a}{n},\qquad
\operatorname{Var}(U_n^{[m]})=\frac{4(n-1)}n\frac{\zeta(4m)}{(2\pi)^{4m}}.
\]
Consequently the positive Pearson correlation \(\rho_{n,m}\) is strictly **increasing in \(n\)** and strictly **decreasing in \(m\)**. Despite that order-wise decrease, the correlation does not vanish as \(m\to\infty\): for every fixed \(n\ge2\),
\[
\boxed{\lim_{m\to\infty}\rho_{n,m}=
\frac{2[\gamma+\log(2\pi)-\operatorname{Ci}(2\pi)]}{\pi^2}\sqrt{\frac{1-1/n}{[b+2(n-1)a]/n}}>0.}
\]
In particular, the sequential large-order then large-sample correlation floor is approximately \(0.6487643381\). The order-two large-sample correlation is approximately \(0.662010596\). These claims are about second moments, not about a joint distribution or calibrated joint critical values.

## Assumptions and scope

Let \(F_0\) be a known continuous cumulative distribution and \(X_1,\ldots,X_n\) independent with that law, with \(n\ge2\). The probability-integral-transformed variables \(V_i=F_0(X_i)\) are iid uniform on \((0,1)\), and \(F_n\) below denotes their empirical CDF. Define
\[
A_n=n\int_0^1\frac{[F_n(t)-t]^2}{t(1-t)}\,dt.
\]
Following Hwang and Kuriki, let the generalized Watson statistic of integer order \(m\ge1\) have the equivalent sample-kernel definition
\[
U_n^{[m]}=\frac1n\sum_{i=1}^n\sum_{j=1}^n h_m(V_i,V_j),\qquad
h_m(x,y)=\frac{(-1)^{m-1}}{(2m)!}B_{2m}(|x-y|).
\]
This is their recursively centered integrated-empirical-measure statistic, with \(m=1\) equal to the conventional Watson statistic. Bernoulli polynomials use \(B_0=1\) and \(\sum_{j=0}^{r}\binom{r+1}{j}B_j=0\) for \(r\ge1\), and \(B_r(z)=\sum_{j=0}^r\binom rj B_{r-j}z^j\). All stated integrals are finite under the simple null. No parameter is fitted, no ties occur almost surely, and \(m\) is a fixed positive integer in each finite-sample statement.

## Proof

**1. Canonical quadratic kernels.** Write \(Y_x(t)=\mathbf1_{\{x\le t\}}-t\), and
\[
a(x,y)=\int_0^1\frac{Y_x(t)Y_y(t)}{t(1-t)}\,dt
=-1-\log\big(\max(x,y)[1-\min(x,y)]\big).
\]
Then \(A_n=n^{-1}\sum_{i,j}a(V_i,V_j)\). Both \(a\) and \(h_m\) are symmetric and canonical, meaning their integral against the uniform law in either argument is zero. For \(h_m\), this follows from \(\int_0^1 B_{2m}(|x-y|)dy=0\); alternatively use its absolutely convergent Fourier expansion. Moreover \(h_m(x,x)=(-1)^{m-1} B_{2m}(0)/(2m)!\) is independent of \(x\). After centering, covariance contributions from kernel pairs sharing at most one index vanish by canonicality. The generalized Watson diagonal is deterministic, leaving just the two orderings of each off-diagonal matching pair. Therefore
\[
\operatorname{Cov}(A_n,U_n^{[m]})=\frac{2(n-1)}n\,\mathbb E[a(V_1,V_2)h_m(V_1,V_2)].
\]

**2. Mixed-kernel integral.** Symmetry and the substitution \(z=|x-y|\) give, for any integrable \(\phi\) with the present logarithmic integrability,
\[
\mathbb E[a(V_1,V_2)\phi(|V_1-V_2|)]
=\int_0^1\big[2(1-z)+4z\log z\big]\phi(z)\,dz.
\]
One direct derivation is to integrate the explicit \(a(x,y)\) over \(0<x<y<1\), set \(y=x+z\), and use \(\int_0^{1-z}\log[(x+z)(1-x)]dx=-2(1-z)-2z\log z\). Substituting \(h_m\) proves the formula for \(\kappa_m\).

**3. Exact rationality and examples.** Every coefficient of \(B_{2m}(z)\) is rational; the elementary integrals \(\int_0^1 z^r dz=1/(r+1)\) and \(\int_0^1 z^{r+1}\log z\,dz=-1/(r+2)^2\) show \(\kappa_m\in\mathbb Q\). For an independent polynomial identity, integration by parts twice using \(B'_{r}(z)=rB_{r-1}(z)\) yields
\[
\kappa_m=\frac{4(-1)^m}{(2m+2)!}\int_0^1\frac{B_{2m+2}(0)-B_{2m+2}(z)}{z(1-z)}\,dz.
\]
The numerator vanishes at both endpoints, so its quotient is a polynomial and the integral is rational. Exact coefficient arithmetic yields the displayed fractions; the bundled standard-library verification program independently implements both polynomial identities.

**4. Positivity and monotonicity in order.** The Fourier expansion of the periodic Bernoulli kernel is absolutely convergent:
\[
h_m(x,y)=2\sum_{k=1}^{\infty}\frac{\cos[2\pi k(x-y)]}{(2\pi k)^{2m}}.
\]
For each positive integer \(k\), introduce
\[
I_k=\int_0^1\frac{1-\cos(2\pi kt)}{t(1-t)}\,dt
=2[\gamma+\log(2\pi k)-\operatorname{Ci}(2\pi k)]>0.
\]
Writing the Fourier transform of \(Y_x(t)\) in the \(x\)-coordinate and integrating its squared modulus against \(1/[t(1-t)]\) gives
\[
\kappa_m=8\sum_{k=1}^{\infty}\frac{I_k}{(2\pi k)^{2m+2}}>0.
\]
For a real \(s\ge1\), define \(P(s)=\sum_{k\ge1}I_k k^{-2s-2}\) and \(Q(s)=\sum_{k\ge1}k^{-4s}\). By the variance calculations below, at each fixed sample size the correlation is a positive constant (independent of \(s\)) times \(P(s)/\sqrt{Q(s)}\). Let \(\mu_s(k)\propto I_k k^{-2s-2}\) and \(\nu_s(k)\propto k^{-4s}\). Differentiation of the absolutely convergent series shows
\[
\frac{d}{ds}\log\frac{P(s)}{\sqrt{Q(s)}}
=2\left[\mathbb E_{\nu_s}\log k-\mathbb E_{\mu_s}\log k\right]<0.
\]
Indeed, \(\mu_s(k)/\nu_s(k)\propto I_k k^{2s-2}\) is strictly increasing in \(k\), since \(I'(x)=2[1-\cos(2\pi x)]/x\ge0\) with strict increase between distinct integer arguments. This monotone likelihood ratio gives strict expectation ordering. Hence \(\rho_{n,m}\) decreases strictly for integer \(m\ge1\). As \(s\to\infty\), both sums are first-harmonic dominated, yielding the stated nonzero correlation floor.

**5. Variances and monotonicity in sample size.** Canonicality gives, for a symmetric canonical kernel \(q\),
\[
\operatorname{Var}\left(\frac1n\sum_{i,j}q(V_i,V_j)\right)
=\frac1n\operatorname{Var}(q(V,V))
+\frac{2(n-1)}n\mathbb E[q(V_1,V_2)^2].
\]
For \(a\), elementary beta-logarithm integration gives \(\operatorname{Var}(a(V,V))=b\) and \(\mathbb E[a(V_1,V_2)^2]=a\), establishing the Anderson–Darling variance above. For \(h_m\), the diagonal is constant and Fourier orthogonality gives
\[
\mathbb E[h_m(V_1,V_2)^2]=2\sum_{k=1}^{\infty}(2\pi k)^{-4m}
=\frac{2\zeta(4m)}{(2\pi)^{4m}}.
\]
Thus the generalized Watson variance follows. Since \(a>0\) and \(b>0\), for each fixed \(m\) the squared correlation is a positive constant times \((n-1)/[2a(n-1)+b]\), strictly increasing in \(n\ge2\). The explicit limit as \(m\to\infty\) follows from the first Fourier harmonic, \(I_1\), and the variance formula; letting \(n\to\infty\) afterwards yields the reported numerical constant.

## Verification

Run `python3 check.py` with Python 3 and the standard library; the script independently computes Bernoulli coefficients as exact fractions, evaluates both formulas for \(\kappa_m\) for orders \(1\) through \(9\), confirms positivity and the listed rational constants, checks Fourier quadrature against the rational integral for orders \(1\) and \(2\), and verifies sample-size/order monotonicity on multiple grids. It additionally performs independently seeded direct null simulations using sorted observations and the Bernoulli-polynomial sample kernel at \(n=2\) and \(n=5\). The checker reports 129 passed assertions. Numerical tests only corroborate the symbolic proof; they do not establish the all-sample-size or all-order quantifiers. The case \(m=1\), which reproduces the previously published covariance \((n-1)/(36n)\), is tested only as a normalization check and **not claimed as new**.

## Relationship to prior work

Hwang and Kuriki (first publicly posted April 9, 2024) introduce the generalized Watson sequence and its kernel, eigenexpansion, limiting distribution and comparisons among test families. Their treatment gives the **marginal** law of each generalized statistic, not the exact finite-sample cross-covariance with the **ordinary** Anderson–Darling statistic established here. Stephens (1974) develops Fourier/Legendre decompositions of classical goodness-of-fit statistics; those components alone do not state the mixed finite-sample covariance for every higher Watson integration order.

An earlier published finite-sample calculation for classical \(m=1\) Watson versus Anderson–Darling finds \((n-1)/(36n)\). It is explicitly excluded from the new scope; the formulas here extend it to all integer orders \(m\ge2\), with an order-monotone correlation and a strictly positive correlation floor requiring mixed-frequency calculations. The spectral eigenvalues and separate moments of the 2024 paper do **not** alone determine the cross-family mixed kernel integral.

## Limitations

Only iid observations under a **fully specified continuous null**, and the exact Hwang–Kuriki generalized Watson normalization, are covered. Estimating model parameters, ties, discontinuous null laws, and modified or two-sample statistics change the setting. Correlation does not identify the full joint distribution or justify an uncorrected test combination. The order limit is taken at fixed sample size; no simultaneous growing-order/sample-size limit is claimed. Positive rationality of the coefficients does not mean that every proposed formula for a different generalized Anderson–Darling order is covered. Absolute priority is uncertain: older papers on component decompositions or integrated empirical processes may contain an equivalent unstated or differently expressed result.

## References

1. H.-K. Hwang and S. Kuriki, *Integrated empirical measures and generalizations of classical goodness-of-fit statistics*, arXiv:2404.06040, first submitted 2024-04-09, Sections 3.1–3.5, particularly Theorem 3.3. https://arxiv.org/abs/2404.06040
2. M. A. Stephens, *Components of goodness-of-fit statistics*, Annales de l'Institut Henri Poincaré, Section B 10(1) (1974), 37–54. https://www.numdam.org/article/AIHPB_1974__10_1_37_0.pdf
3. N. Henze and Ya. Yu. Nikitin, *Watson-type goodness-of-fit tests based on the integrated empirical process*, 2002, cited in Hwang and Kuriki's generalized-Watson development. https://www.researchgate.net/publication/268315464_Watson-type_goodness-of-fit_tests_based_on_the_integrated_empirical_process
4. *Exact finite-sample covariance of Watson and Anderson–Darling goodness-of-fit statistics*, publicly available result, October 13, 2026, covering the classical first Watson order only. https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-exact-finite-sample-covariance-of-watson-and-anderson-darling-go--6e915b815835
