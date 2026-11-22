# A noncentral chi-square crossover for locally anisotropic random three-dimensional zonotopes

## Finding

Let \(\sigma\) be normalized area measure on the Euclidean unit sphere \(S^2\subset\mathbb R^3\), let \(P_2(t)=(3t^2-1)/2\), and let \(\varepsilon_n\to0\) be a deterministic real sequence. For each sufficiently large integer \(n\), sample independent vectors \(U_{n,1},\ldots,U_{n,n}\) from the probability density \(1+\varepsilon_nP_2(u_3)\) with respect to \(\sigma\). Form the unit-generator zonotope \(Z_n=\sum_{i=1}^n[0,U_{n,i}]\) and write \(V_n=\operatorname{Vol}_3(Z_n)\).

For each integer \(m\ge1\), set
\[
a_m=\frac{\pi}{4}\frac{\binom{2m}{m}^{2}}{16^m(2m-1)(2m+2)},\qquad a_1=\frac\pi{64}.
\]
If \(\sqrt n\,\varepsilon_n\to c\in\mathbb R\), then
\[
\boxed{\frac{V_n-\mathbb EV_n}{n^2}\ \Longrightarrow\ W_c
 =\frac\pi{16}+\frac{\pi c^2}{640}
 -\frac{\pi}{128}X_{1,c}-\frac12\sum_{m=2}^{\infty}a_mX_m},
\]
where \(X_{1,c}\) is a noncentral chi-square variable with five degrees of freedom and noncentrality \(c^2/5\), and the mutually independent \(X_m\), \(m\ge2\), are central chi-square variables with \(4m+1\) degrees of freedom. The series converges almost surely and in \(L^1\). Its centered law has
\[
\boxed{\operatorname{Var}(W_c)=\frac1{12}-\frac{\pi^2}{128}+\frac{\pi^2 c^2}{20480}},\qquad
\boxed{\operatorname{ess\,sup}W_c=\frac\pi{16}+\frac{\pi c^2}{640}},
\]
and no finite lower endpoint. Thus even a vanishing angular density perturbation changes the limiting geometry at precisely order \(n^{-1/2}\), by noncentralizing **one five-dimensional harmonic sector** rather than adding an independent Gaussian random variable.

If instead \(\sqrt n\,|\varepsilon_n|\to\infty\) while \(\varepsilon_n\to0\), then
\[
\boxed{\frac{V_n-\mathbb EV_n}{n^{5/2}|\varepsilon_n|}
\ \Longrightarrow\ N\!\left(0,\frac{\pi^2}{20480}\right).}
\]
In particular \(\sqrt n\,\varepsilon_n\to0\) recovers the known isotropic second-chaos law \(W_0\); the two regimes meet in an explicit noncentral chi-square crossover. These conclusions hold for both signs of the anisotropy parameter.

## Assumptions and scope

The coordinates \(u_1,u_2,u_3\) are in a fixed orthonormal frame and the distinguished axis is \(e_3\). Density positivity holds eventually whenever \(\varepsilon_n\to0\), because \(-1/2\le P_2\le1\). Each row contains independent identically distributed **unit** vectors, but the common angular distribution may depend on \(n\). The volume is ordinary three-dimensional Euclidean volume, without a factor of \(n^{-3}\). The centering is always the **exact expectation under the row's density**, not the uniform-sphere expectation \(\binom n3\pi/8\). All limits are along integer \(n\to\infty\), with the ambient dimension fixed.

Spherical harmonics below are orthonormal in \(L^2(\sigma)\), not in unnormalized surface measure. Thus the normalized zonal quadratic harmonic is \(\sqrt5 P_2(u_3)\). We use \(N(0,v)\) for a centered Gaussian of variance \(v\), and \(\chi_d^2(\lambda)\) for a noncentral chi-square law with \(d\) degrees of freedom and noncentrality \(\lambda\).

## Proof

**1. The geometric kernel and the uniform-sphere decomposition.** The standard zonotope determinant identity gives exactly
\[
 V_n=\sum_{i<j<k}h(U_{n,i},U_{n,j},U_{n,k}),\quad h(u,v,w)=|\det(u,v,w)|.
\]
Under independent uniform \(\sigma\) arguments, conditional integration in the third argument gives \(\mathbb E_\sigma[h(u,v,W)]=\frac12\sqrt{1-(u\cdot v)^2}\); the total mean is \(\mu=\pi/8\). Hence the uniform-sphere Hoeffding decomposition is the pointwise identity
\[
 h(u,v,w)=\mu+g(u,v)+g(u,w)+g(v,w)+h_3(u,v,w),
\]
where \(g(u,v)=\frac12\sqrt{1-(u\cdot v)^2}-\mu\), and \(h_3\) has zero \(\sigma\)-conditional mean in any one or two remaining variables. The first-order uniform-sphere projection vanishes. Consequently, with \(G_n=\sum_{i<j}g(U_{n,i},U_{n,j})\) and \(H_n=\sum_{i<j<k}h_3(U_{n,i},U_{n,j},U_{n,k})\),
\[
 V_n-\mathbb EV_n=(n-2)(G_n-\mathbb EG_n)+(H_n-\mathbb EH_n).
\]
The identity is algebraic and therefore remains valid **even though the row distribution is not uniform**.

**2. Rigorous bound for the cubic residual under the moving law.** Write \(f_\varepsilon(u)=1+\varepsilon P_2(u_3)\). The bounded kernel \(h_3\) is canonical for \(\sigma\). For two distinct triple summands with two shared indices, conditioning on those indices shows their covariance is \(O(\varepsilon^2)\), because integrating out the third vector inserts one \(\varepsilon P_2\) factor. For one shared index, the corresponding conditional expectation inserts two such factors, so the covariance is \(O(\varepsilon^4)\). Disjoint triples are independent, and each individual variance is uniformly bounded. Counting respectively \(O(n^4)\), \(O(n^5)\), and \(O(n^3)\) pairs yields the **uniform** estimate
\[
 \operatorname{Var}(H_n)=O(n^3+n^4\varepsilon_n^2+n^5\varepsilon_n^4).
\]
Thus the centered cubic remainder vanishes in \(L^2\) upon division by \(n^2\) if \(\sqrt n\,\varepsilon_n\) is bounded. It also vanishes upon division by \(n^{5/2}|\varepsilon_n|\) when \(\varepsilon_n\to0\) and \(\sqrt n|\varepsilon_n|\to\infty\). No finite enumeration substitutes for this uniform variance argument.

**3. Spherical harmonic spectrum and the one moving mode.** By Funk–Hecke, the bounded zonal kernel \(g\) has zero degree-zero and odd eigenvalues. Its degree-\(2m\) eigenvalue is \(-a_m\), with multiplicity \(4m+1\). Indeed,
\[
 -a_m=\frac14\int_{-1}^1\sqrt{1-t^2}\,P_{2m}(t)\,dt;
\]
expanding the polynomial and integrating each even power by the beta integral evaluates the expression above. Equivalently, the uniform-sphere spectral calculation in the cited isotropic-zonotope result gives the same coefficients, with the trace and square-summability identities
\[
 \sum_{m\ge1}(4m+1)a_m=\frac\pi8,\qquad
 \sum_{m\ge1}(4m+1)a_m^2=\frac16-\frac{\pi^2}{64}.
\]
Choose orthonormal real harmonics \(Y_{2m,j}\) of each even degree, with \(Y_{2,1}(u)=\sqrt5P_2(u_3)\). Then the absolutely trace-convergent addition-theorem expansion of \(g\) is
\[
 g(u,v)=-\sum_{m\ge1}a_m\sum_{j=1}^{4m+1}Y_{2m,j}(u)Y_{2m,j}(v).
\]
Under \(f_{\varepsilon_n}\sigma\), all these harmonic means vanish except
\[
 \mathbb E Y_{2,1}(U_{n,i})=\varepsilon_n/\sqrt5.
\]
This identity follows exactly from harmonic orthogonality and \(\int P_2^2d\sigma=1/5\). It also gives \(\mathbb Eg(U,V)=-a_1\varepsilon_n^2/5\). By the sphere addition theorem, \(\sum_jY_{2m,j}(u)^2=4m+1\) at every unit vector, giving the finite-row identity
\[
 G_n=-\frac12\sum_{m\ge1}a_m\left[
 \sum_j\left(\sum_{i=1}^nY_{2m,j}(U_{n,i})\right)^2-n(4m+1)
 \right].
\]

**4. Critical-window limit and infinite-tail control.** If \(\sqrt n\varepsilon_n\to c\), then for each finite collection of harmonic coordinates the triangular-array multivariate central limit theorem applies: the row laws tend uniformly to \(\sigma\), the coordinate covariance tends to the identity, and every coordinate is bounded. The normalized sums converge jointly to independent unit Gaussians, except for a mean shift \(c/\sqrt5\) in \(Y_{2,1}\). Thus the squared degree-two norm tends to \(\chi_5^2(c^2/5)\), and higher squared norms tend independently to \(\chi_{4m+1}^2\). The mean-subtracted limit of \(G_n/n\) is therefore
\[
 -\frac12\sum_{m\ge1}a_m\left(X_{m,c}-(4m+1)-\mathbf1_{m=1}\frac{c^2}{5}\right).
\]
For any cutoff \(M\ge1\), the degree-greater-than-\(2M\) remainder kernel is canonical not only for \(\sigma\), but also for **each** density \(f_\varepsilon\sigma\), because it has no degree-two component: integration against \(1+\varepsilon P_2\) annihilates it in either argument. Distinct pair summands of this remainder are therefore orthogonal. Since the densities are uniformly bounded for small \(\varepsilon\), its \(n^{-1}\)-scaled second moment is bounded by a fixed constant times \(\sum_{m>M}(4m+1)a_m^2\), uniformly in \(n\). This tends to zero and justifies the infinite series independently of finite-mode tests. Step 2 removes \(H_n\). Finally, \(\sum_m(4m+1)a_m=\pi/8\) and \(a_1=\pi/64\) yield the claimed explicit \(W_c\).

For the variance, each independent noncentral chi-square has variance \(2(d+2\lambda)\); the trace identity gives \(\operatorname{Var}(W_c)=\frac12\sum_m(4m+1)a_m^2+a_1^2c^2/5\). All coefficients \(a_m>0\); the noncentral and central chi-square variables may be jointly arbitrarily near zero on any finite set with positive probability, and the nonnegative infinite tail has arbitrarily small expectation beyond a large cutoff. Thus the displayed constant is the sharp essential supremum. Any one unbounded chi-square term forces an unbounded lower support.

**5. Supercritical local anisotropy.** Suppose \(\varepsilon_n\to0\) and \(\sqrt n|\varepsilon_n|\to\infty\). Direct integration of the pair kernel gives its first Hoeffding projection under the **row law** exactly as
\[
 \mathbb E[g(u,U)]-\mathbb Eg(U,U')=-a_1\varepsilon_n\bigl(P_2(u_3)-\varepsilon_n/5\bigr).
\]
After subtracting the first projection from \(G_n-\mathbb EG_n\), the pair kernel is degenerate and bounded, so its residual sum has variance \(O(n^2)\) uniformly for small \(\varepsilon_n\). Consequently its contribution to \((n-2)(G_n-\mathbb EG_n)\) has standard deviation \(O(n^2)\), negligible against \(n^{5/2}|\varepsilon_n|\). The leading term is exactly
\[
 -a_1\varepsilon_n(n-2)(n-1)\sum_{i=1}^n\bigl(P_2(U_{n,i,3})-\varepsilon_n/5\bigr).
\]
The bounded triangular-array central limit theorem and \(\operatorname{Var}_\sigma(P_2)=1/5\) give the displayed Gaussian variance \(a_1^2/5=\pi^2/20480\). Step 2 also makes the cubic residual negligible at this scale, completing the proof.

## Verification

The accompanying standalone `verify_anisotropy.py` evaluates Legendre integrals through degree 24, the first spectral coefficient, partial trace and Hilbert–Schmidt identities, and independent spherical-quadrature checks of the exact \(P_2\) conditional projection at five polar latitudes. It samples from the tilted density using rejection sampling and independently calculates triple determinants at small sizes. It also verifies the critical and supercritical variance normalizations and noncentral-chi-square first moments. Execute `python verify_anisotropy.py` with NumPy and SciPy. All finite computations are corroborative; the proofs of uniform remainder bounds, spectral-tail control, and the infinite limits are analytical.

## Relationship to prior work

Schneider, *Random zonotopes and valuations* (arXiv:2202.06774, first posted 2022-02-14), establishes the random-zonotope valuation framework and a central limit theorem; the present local alternative targets a moving angular distribution whose **first-order projection vanishes in the limit**, requiring a noncentral degree-two spectral analysis. Breiding, Bürgisser, Lerario and Mathis (arXiv:2109.14996) provide the geometric algebra of zonoids and random determinants. The independently posted *Second-order volume fluctuations of isotropic three-dimensional random zonotopes* (published-finding corpus, 2026) derives the \(\varepsilon=0\) eigenvalues and central chi-square series, explicitly used above; it does **not** describe the \(n^{-1/2}\) anisotropy window or the noncentralization. The published *A critical radial-noise crossover for areas of random planar zonotopes* concerns random **segment lengths in dimension two**, and gives an independent Gaussian plus exponential-series crossover. The result here instead perturbs a **fixed-unit-length angular law in dimension three** and obtains a shifted five-dimensional chi-square component within the existing series; neither theorem implies the other under a change of variables. General degenerate U-statistic and local-alternative theory underlie the method and are not claimed as new.

## Limitations

This theorem treats a single quadrupolar angular-density perturbation and fixed unit-length generators in three dimensions, not arbitrary anisotropy modes, arbitrary convex bodies, or nonindependent vectors. There is no claim of convergence rates or a closed finite-sample probability density. The precise cubic correction to the finite-sample expectation is not evaluated; the statement correctly uses exact-expectation centering. A historically unindexed equivalent local-alternative result remains a priority risk. The Schneider paper's abstract and dated public record were accessible, but its full text was not retrieved in the current comparison; no unsupported assertion is made about uninspected clauses. No independent mathematical audit has been performed.

## References

1. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774v1, first publicly posted 2022-02-14, https://arxiv.org/abs/2202.06774 .
2. P. Breiding, P. Bürgisser, A. Lerario, L. Mathis, *The zonoid algebra, generalized mixed volumes, and random determinants*, arXiv:2109.14996v1, first publicly posted 2021-09-30, https://arxiv.org/abs/2109.14996 .
3. *Second-order volume fluctuations of isotropic three-dimensional random zonotopes*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-second-order-volume-fluctuations-of-isotropic-three-dimensional--31c1b1c50e42 (published record; full theorem and proof inspected).
4. *A critical radial-noise crossover for areas of random planar zonotopes*, published-finding corpus, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-critical-radial-noise-crossover-for-areas-of-random-planar-zon--95e0628386f8 (published record; full theorem and proof inspected).
5. Standard tools: Hoeffding's decomposition for symmetric U-statistics; Funk–Hecke's theorem and the spherical-harmonic addition theorem; triangular-array central limit theorem.
