# Endpoint detrending preserves spurious distance correlation: an exact Brownian-bridge covariance law

## Finding

For two independent centered finite-variance random walks, removing each observed endpoint by a linear trend does **not** restore consistency of ordinary time-paired distance correlation as an indicator of process independence. The sample coefficient converges in distribution to the distance correlation of two independent standard Brownian bridges evaluated at one common uniform time. This limit is strictly between zero and one almost surely, has support all of \([0,1]\), and makes unrestricted time-label permutation tests reject process independence with asymptotic probability one at any fixed nominal level.

There is an explicit quantitative characterization. If \(B_1,B_2\) are independent standard Brownian bridges on \([0,1]\) and \(K\) denotes the *squared distance covariance* of their joint time-occupation law, then
\[
\mathbb E K(B_1,B_2)=\frac{1}{3\pi}-\frac{\pi}{32}=0.00792852496991586\ldots>0.
\]
This expectation is **not** the expectation of squared *distance correlation*: the latter has a random denominator.

For independent *Gaussian*-increment walks, the expectation of the squared distance covariance computed from the endpoint-detrended, variance-normalized observations at all \(n\) time labels has the exact finite-sample expression
\[
\mathbb E T_n=\frac{2}{\pi}\left\{\frac{n^2-1}{6n^2}-\left(\frac{1}{n^2}\sum_{h=1}^{n-1}\sqrt{h(n-h)}\right)^2\right\},\qquad n\ge2.
\]
In particular this expectation converges to the displayed bridge constant. No finite-sample formula is asserted for non-Gaussian increments.

## Assumptions and scope

Let \((\xi_j)_{j\ge1}\) and \((\eta_j)_{j\ge1}\) be mutually independent sequences, each separately independent and identically distributed, with means zero and variances \(0<\sigma_\xi^2,\sigma_\eta^2<\infty\). Write \(X_k=\sum_{j=1}^k\xi_j\) and \(Y_k=\sum_{j=1}^k\eta_j\). For each \(n\ge2\), observe the *endpoint-linearly-detrended* values
\[
Z^X_{k,n}=\frac{X_k-(k/n)X_n}{\sigma_\xi\sqrt n},\qquad
Z^Y_{k,n}=\frac{Y_k-(k/n)Y_n}{\sigma_\eta\sqrt n},\qquad 1\le k\le n.
\]
Separate positive rescalings do not change sample distance correlation. The endpoint is included among the observations, and thus \(Z^X_{n,n}=Z^Y_{n,n}=0\).

For real data \((x_i,y_i)_{i=1}^n\), set \(a_{ij}=|x_i-x_j|\), \(b_{ij}=|y_i-y_j|\), and let \(A_{ij}=a_{ij}-\overline a_{i\cdot}-\overline a_{\cdot j}+\overline a_{\cdot\cdot}\), with \(B\) defined analogously. All means divide by \(n\) or \(n^2\), including the diagonal. Define
\[
T_n=\frac1{n^2}\sum_{i,j=1}^n A_{ij}B_{ij},\qquad
R_n=\left(\frac{T_n}{\sqrt{T_n^{XX}T_n^{YY}}}\right)^{1/2},
\]
where \(T_n^{XX}=n^{-2}\sum A_{ij}^2\), \(T_n^{YY}=n^{-2}\sum B_{ij}^2\), and \(R_n=0\) if the denominator vanishes. The permutation \(p\)-value permutes the \(n\) time labels of the second detrended series uniformly and compares the resulting \(T_n^\pi\) to \(T_n\), counting equality as rejection-tail inclusion.

For continuous paths \(f,g\), let \(D_f(s,t)=|f(s)-f(t)|-r_f(s)-r_f(t)+m_f\), with \(r_f(s)=\int_0^1|f(s)-f(u)|\,du\) and \(m_f=\int_0^1r_f(s)\,ds\). Put \(K(f,g)=\int_0^1\int_0^1D_f(s,t)D_g(s,t)\,ds\,dt\) and \(\mathcal R(f,g)=\{K(f,g)/\sqrt{K(f,f)K(g,g)}\}^{1/2}\) for nonconstant paths. A standard bridge satisfies \(B(t)=W(t)-tW(1)\).

## Proof

**1. Functional limit.** By the joint functional central limit theorem, the interpolated normalized walks converge to independent Brownian motions \((W_1,W_2)\). Applying the continuous map \(f\mapsto f(t)-tf(1)\) produces independent Brownian bridges \((B_1,B_2)\). Replacing the interpolated paths by the time-step paths associated with \(1\le k\le n\) is asymptotically negligible in the uniform norm: finite second moments imply \(\max_{k\le n}|\xi_k|/\sqrt n\to0\) in probability, and similarly for \(\eta\). The centered-distance functional \(K\) is uniformly continuous on uniformly bounded path sets; \(\mathcal R\) is continuous at nonconstant continuous path pairs. Brownian bridges are nonconstant almost surely. The continuous-mapping theorem therefore gives
\[
(R_n,T_n)\ \Rightarrow\ (\mathcal R(B_1,B_2),K(B_1,B_2)).
\]
For the first coordinate, separate scale normalization is immaterial.

**2. Strict positivity and strict upper bound.** If \(K(B_1,B_2)=0\), the distance covariance independence characterization in one real dimension implies that \(B_1(U)\) and \(B_2(U)\), for a common independent uniform \(U\), are independent *conditional on the paths*. In particular their time covariance
\[
Z=\int_0^1\{B_1(t)-\overline B_1\}B_2(t)\,dt
\]
vanishes. Conditional on \(B_1\), put \(q(t)=B_1(t)-\overline B_1\), \(F(s)=\int_s^1q(t)\,dt\), and \(c=\int_0^1tq(t)\,dt\). By \(B_2(t)=W_2(t)-tW_2(1)\), stochastic Fubini gives \(Z=\int_0^1\{F(s)-c\}\,dW_2(s)\). Its conditional variance is \(\int_0^1(F(s)-c)^2\,ds>0\): if zero, \(F\) would be constant, and differentiation would force the nonconstant path \(B_1\) to be constant. Thus \(\mathbb P(Z=0\mid B_1)=0\) almost surely. Hence \(K(B_1,B_2)>0\) almost surely.

If \(\mathcal R(f,g)=1\) for continuous nonconstant paths, equality in Cauchy–Schwarz for the two centered-distance kernels requires \(D_g=aD_f\) for a positive constant \(a\). Taking diagonal values and integrating the identity yields \(r_g=ar_f\), \(m_g=am_f\), and consequently \(|g(s)-g(t)|=a|f(s)-f(t)|\) for all \(s,t\). A scaled isometry of a real interval is affine, so \(g=b\pm af\). For two pinned bridges this reduces to \(B_2=\pm aB_1\). Their values at two distinct interior times form independent nondegenerate Gaussian vectors, so this proportionality event has probability zero. Thus \(0<\mathcal R(B_1,B_2)<1\) almost surely.

**3. Full support.** The standard Brownian-bridge law has full support in the uniform norm on continuous functions vanishing at both endpoints: approximate such a function by a Brownian-motion path with a small uniform error and apply the endpoint-pinning map. Independence supplies full support of the pair. Set \(h(t)=1-|2t-1|\) on \([0,1]\), extended periodically, and for even integers \(m\) set \(g_m(t)=h(mt)\). Both \(h\) and \(g_m\) vanish at both endpoints. A Riemann-sum argument shows that \((h(U),g_m(U))\) converges weakly to the product of two uniform laws on \([0,1]\), while its two marginals remain uniform. Their distance correlation therefore tends to zero; \(\mathcal R(h,h)=1\). For any fixed \(m\) the path \(g_\lambda=(1-\lambda)h+\lambda g_m\) stays nonconstant on \([0,1]\) for all \(0\le\lambda\le1\): for \(\lambda<1\), \(g_\lambda(1/2)=1-\lambda>0=g_\lambda(0)\), and at \(\lambda=1\), \(g_m\) is nonconstant. Continuity and the intermediate-value theorem realize each target correlation in \((0,1)\) by such a pinned pair. Full support of bridge path law transfers every open interval in \((0,1)\) to positive probability, proving support \([0,1]\).

**4. Exact mean of the squared distance covariance.** Since the bridges are independent, \(\mathbb E K(B_1,B_2)\) is the squared \(L^2([0,1]^2)\)-norm of the expected centered distance kernel. Writing \(a=|s-t|\), Gaussian increments of a unit bridge have variance \(a(1-a)\), hence
\[
\mathbb E|B(s)-B(t)|=\sqrt{\frac2\pi}\,d(s,t),\qquad d(s,t)=\sqrt{a(1-a)}.
\]
The symmetry \(\sqrt{u(1-u)}=\sqrt{(1-u)u}\) makes the expected row mean independent of \(s\):
\[
\int_0^1d(s,t)\,dt=\int_0^1\sqrt{u(1-u)}\,du=B(3/2,3/2)=\frac\pi8.
\]
Also \(\int_0^1\int_0^1d(s,t)^2\,ds\,dt=2\int_0^1u(1-u)^2\,du=1/6\). Thus \(\mathbb E D_B(s,t)=\sqrt{2/\pi}\{d(s,t)-\pi/8\}\) and
\[
\mathbb E K(B_1,B_2)=\frac2\pi\left(\frac16-\frac{\pi^2}{64}\right)=\frac1{3\pi}-\frac\pi{32}.
\]
Finiteness of Brownian supremum moments justifies Fubini and expectation.

**5. Exact finite Gaussian mean.** For Gaussian increments, each normalized detrended sequence at \(k=1,\ldots,n\) has exactly the joint law of a standard bridge evaluated at \(k/n\). For \(i,j\) put \(a_{ij}=|i-j|/n\) and \(d_{ij}=\sqrt{a_{ij}(1-a_{ij})}\). Each expected absolute separation is \(\sqrt{2/\pi}\,d_{ij}\). Because \(d_{ij}\) depends on the cyclic difference and \(\sqrt{u(1-u)}=\sqrt{(1-u)u}\), every row of the deterministic matrix \((d_{ij})\) has the same mean
\[
m_n=\frac1{n^2}\sum_{h=1}^{n-1}\sqrt{h(n-h)}.
\]
Centering this mean-distance matrix consequently subtracts \(m_n\) from every entry. Independence between the two full detrended series allows the expectation of their centered-distance product to factor. Finally, direct summation gives \(n^{-2}\sum_{i,j}d_{ij}^2=(n^2-1)/(6n^2)\). Substitution proves the exact finite formula. Standard Riemann-sum convergence yields \(m_n\to\pi/8\), and hence the limit constant.

**6. Permutation failure.** Double centering gives the exact combinatorial identity, valid for arbitrary fixed observations,
\[
\mathbb E_\pi(T_n^\pi\mid\text{data})=\frac{\overline a_{\cdot\cdot}\overline b_{\cdot\cdot}}{n-1}.
\]
Since \(T_n^\pi\ge0\) for real one-dimensional Euclidean distance covariance, conditional Markov inequality yields \(p_n\le \overline a_{\cdot\cdot}\overline b_{\cdot\cdot}/\{(n-1)T_n\}\) whenever \(T_n>0\). The normalized means and \(T_n\) converge jointly to finite Brownian-bridge functionals, with the limiting \(K(B_1,B_2)>0\) almost surely by step 2. The ratio is tight and \(\mathbb P(T_n=0)\to0\). Thus \(p_n\to0\) in probability and \(\mathbb P(p_n\le\alpha)\to1\) for every fixed \(0<\alpha<1\).

## Verification

`CHECKER.py` requires only standard Python. It checks the exact Brownian-bridge increment covariance by 5,000-plus rational identities, the beta integral, the time-invariant mean distance by quadrature, the Gaussian finite-grid formula by independently centering matrices at 51 different sample sizes, the exact permutation expectation through complete enumeration for small sizes, and affine invariance and support endpoints. A seeded 400-replicate Gaussian bridge simulation gives a mean squared distance covariance of approximately \(0.008579388\) at grid size 65, compared with the exact finite expectation \(0.008299332\). The checker reports 6,155 passing assertions. Its finite diagnostics are **not** proofs of the infinite claims; those follow from the six analytic steps above.

## Relationship to prior work

Zhu and Xie (2026, arXiv:2611.16614v1) prove the nonsensical sample distance-correlation limit and permutation failure for the **undetrended** independent random walks, and calculate the distinct Brownian-*motion* numerator mean \(26/(75\pi)-1/12\). Their full primary text provides the path-distance representation and a continuum mapping argument. It does not state the endpoint-detrended bridge limit, the bridge numerator constant, or the exact finite Gaussian bridge-grid mean. Those distinctions are the mathematical subject here; the distance-correlation characterization and permutation identity themselves are prior results and are not claimed to be new.

Székely, Rizzo and Bakirov (2007) introduced distance correlation and its independence characterization; Lyons (2013) explains the centered-distance construction and its metric-space generality. The present result combines these known foundations with a different Gaussian bridge kernel and its cyclic row-mean simplification. No priority or uniqueness is claimed beyond the inspected sources.

## Limitations

This is a mathematical calculation, not a calibrated new hypothesis test. The false-rejection result is for **unrestricted** permutation of time labels, not a dependence-preserving resampling design. Distributional convergence needs only independent centered finite-variance innovations; the exact finite-grid mean requires Gaussian increments and the specified variance normalization. The explicit constant is the expectation of the **squared distance covariance numerator** of the limiting occupation measure; no formula for the mean normalized correlation, density of its law, finite-sample error rate, or optimal inference procedure is asserted. Literature searches and direct primary-text comparison do not establish worldwide historical priority; unindexed work could overlap.

## References

1. Liping Zhu and Zhongming Xie, *Nonsense nonlinear correlations between independent random walks*, arXiv:2611.16614v1, first posted 12 November 2026. https://arxiv.org/html/2611.16614v1
2. G. J. Székely, M. L. Rizzo and N. K. Bakirov, *Measuring and testing dependence by correlation of distances*, Annals of Statistics **35** (2007), 2769–2794. https://doi.org/10.1214/009053607000000505
3. Russell Lyons, *Distance covariance in metric spaces*, Annals of Probability **41** (2013), 3284–3305. https://arxiv.org/abs/1106.5758
