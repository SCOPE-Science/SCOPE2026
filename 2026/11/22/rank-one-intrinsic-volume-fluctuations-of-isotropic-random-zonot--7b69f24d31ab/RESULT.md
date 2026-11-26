# Rank-one intrinsic-volume fluctuations of isotropic random zonotopes in every dimension

## Finding

Fix an integer \(d\ge3\). Let \(U_1,U_2,\ldots\) be independent and uniform on \(S^{d-1}\), and define the Euclidean zonotope \(Z_n=[0,U_1]+\cdots+[0,U_n]\subset\mathbb R^d\). Write \(V_k(n)=V_k(Z_n)\), using **Steiner-normalized** intrinsic volumes: \(\operatorname{Vol}_d(K+tB^d)=\sum_{k=0}^d\kappa_{d-k}V_k(K)t^{d-k}\). In particular \(V_d\) is volume, \(2V_{d-1}\) is surface area, and \(V_1(Z_n)=n\) deterministically.

For \(2\le k\le d\), let
\[
 s_d=\frac{\Gamma(d/2)^2}{\Gamma((d-1)/2)\Gamma((d+1)/2)},\qquad
 v_d=\frac{d-1}{d}-s_d^2>0,
\]
\[
 c_{d,k}=\left(\frac{\Gamma(d/2)}{\Gamma((d+1)/2)}\right)^{k-2}
 \frac{\Gamma((d-1)/2)}{\Gamma((d-k+1)/2)},\quad c_{d,2}=1.
\]
Then the **exact means and common-component covariances**, valid at every integer \(n\ge d\), are
\[
 \boxed{\mathbb E V_k(n)=\binom nk c_{d,k}s_d},\qquad
 \boxed{\operatorname{Cov}(V_k(n),V_2(n))=
 c_{d,k}\binom{n-2}{k-2}\binom n2 v_d}.
\]
More strongly, the exact regression residual
\[
 R_{n,k}=V_k(n)-\mathbb EV_k(n)
 -c_{d,k}\binom{n-2}{k-2}\bigl(V_2(n)-\mathbb EV_2(n)\bigr)
\]
is orthogonal in \(L^2\) to \(V_2(n)\), and satisfies \(\mathbb E R_{n,k}^2=O_{d,k}(n^{2k-3})\), with \(R_{n,2}=0\). Therefore, as \(n\to\infty\), the **joint vector** converges in distribution:
\[
 \boxed{\left(n^{1-k}\left[V_k(n)-\mathbb EV_k(n)\right]\right)_{k=2}^d
 \Longrightarrow \left(\frac{c_{d,k}}{(k-2)!}W_d\right)_{k=2}^d}.
\]
Every pair of intrinsic volumes indexed by \(2,\ldots,d\) has correlation \(1-O_d(n^{-1})\); the limiting covariance matrix has rank one.

The common random variable has a complete geometric spectral description. Define the normalized zonal Gegenbauer polynomial \(P_\ell^{(d)}(t)=C_\ell^{((d-2)/2)}(t)/C_\ell^{((d-2)/2)}(1)\), the dot-product density
\[
f_d(t)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}(1-t^2)^{(d-3)/2},\qquad -1<t<1,
\]
and, for \(m\ge1\),
\[
 b_{d,2m}=-\int_{-1}^{1}\bigl(\sqrt{1-t^2}-s_d\bigr)
 P_{2m}^{(d)}(t) f_d(t)\,dt>0,
\]
\[
 N_{d,\ell}=\frac{(2\ell+d-2)(\ell+d-3)!}{\ell!(d-2)!}.
\]
For mutually independent chi-square variables \(X_{d,2m}\sim\chi^2_{N_{d,2m}}\),
\[
 \boxed{W_d=\frac{s_d}{2}-\frac12\sum_{m=1}^\infty b_{d,2m}X_{d,2m}}.
\]
This nonnegative weighted sum converges almost surely and in \(L^1\); \(\mathbb E W_d=0\), \(\operatorname{Var}(W_d)=v_d/2>0\), and \(\operatorname{ess\,sup}W_d=s_d/2\) is sharp, while the distribution is unbounded below. In particular its common limit is **not Gaussian**. The first spectral coefficient is exactly \(b_{d,2}=s_d/[(d-1)(d+1)]\).

## Assumptions and scope

The dimension \(d\) is a fixed integer at least three, and \(n\to\infty\) through integers; all vectors have deterministic Euclidean length one and the normalized Haar surface law, independently. The segments are oriented \([0,U_i]\), although a reversal merely translates the zonotope and does not alter intrinsic volumes. No random segment lengths, anisotropic directions, non-Haar dependence, or growing-dimension limit are asserted. Bounds denoted \(O_{d,k}\) permit constants depending on fixed \(d,k\). The same intrinsic-volume normalization is used in every formula.

## Proof

**1. Parallelotope decomposition and exact means.** For the Steiner normalization, additivity of mixed volumes under Minkowski sums of segments yields
\[
 V_k(n)=\sum_{1\le i_1<\cdots<i_k\le n}h_k(U_{i_1},\ldots,U_{i_k}),
 \quad h_k(u_1,\ldots,u_k)=\sqrt{\det(\langle u_i,u_j\rangle)_{i,j=1}^k}.
\]
The formula follows first by expanding the volume polynomial of the Minkowski sum and then by continuity; it remains true for degenerate parallelotopes, whose Gram determinant vanishes. Let \(t=u\cdot v\). Gram–Schmidt gives the first two-vector height \(\sqrt{1-t^2}\); every subsequently appended independent uniform vector has a projection-height factor whose conditional distribution depends only on the remaining subspace dimension, not the past orientation. For a random \(U\in S^{d-1}\) and a fixed \(j\)-plane, its distance to that plane has mean
\[
 \mathbb E\operatorname{dist}(U,L_j)=
 \frac{\Gamma(d/2)\Gamma((d-j+1)/2)}
 {\Gamma((d+1)/2)\Gamma((d-j)/2)}.
\]
Multiplying these means over \(j=2,\ldots,k-1\) telescopes, giving the conditional two-vector identity
\[
 \boxed{\mathbb E\left[h_k(U_1,\ldots,U_k)\mid U_1=u,U_2=v\right]
 =c_{d,k}\sqrt{1-(u\cdot v)^2}}.
\]
The dot product of two independent Haar directions has density \(f_d\), so a beta integral gives \(\mathbb E\sqrt{1-t^2}=s_d\). This proves the expectation formula. Another beta integral gives \(\mathbb E[1-t^2]=(d-1)/d\), hence \(v_d>0\) is the genuine variance of \(\sqrt{1-t^2}\).

**2. Exact universal second-order projection.** Isotropy makes \(\mathbb E[h_k\mid U_1=u]\) constant: the first Hoeffding projection vanishes. With \(g(u,v)=\sqrt{1-(u\cdot v)^2}-s_d\), the second canonical projection of \(h_k\) is exactly \(c_{d,k}g(u,v)\). The U-statistic Hoeffding decomposition of the *sum*, not a normalized average, is
\[
 V_k(n)-\mathbb EV_k(n)
 =c_{d,k}\binom{n-2}{k-2}\sum_{i<j}g(U_i,U_j)+R_{n,k}.
\]
Because \(V_2(n)-\mathbb EV_2(n)=\sum_{i<j}g(U_i,U_j)\) and all higher canonical projections are orthogonal in \(L^2\) to the pair term, the exact covariance follows from \(\operatorname{Var}\sum_{i<j}g(U_i,U_j)=\binom n2v_d\). Distinct pairs sharing one index have zero covariance after conditioning on that index. The remaining canonical terms have orders \(3,\ldots,k\). Each bounded canonical \(j\)-kernel yields a sum of pairwise orthogonal terms indexed by its \(j\)-subsets, with variance \(O(n^j)\); the multiplicity prefactor is \(\binom{n-j}{k-j}=O(n^{k-j})\). Hence
\[
 \operatorname{Var}R_{n,k}=\sum_{j=3}^k O(n^{2(k-j)+j})
 =O_{d,k}(n^{2k-3}).
\]
This establishes exact regression orthogonality and the residual estimate, including the trivial empty sum when \(k=2\).

**3. Joint reduction to one canonical pair statistic.** Divide step 2 by \(n^{k-1}\). The residual tends to zero in \(L^2\), because its variance is \(O(n^{-1})\) after this normalization. Also
\[
 \frac{\binom{n-2}{k-2}}{n^{k-2}}\to\frac1{(k-2)!}.
\]
Since the number of intrinsic volumes in the vector is fixed and finite, the entire joint limit is determined by the single random pair statistic \(n^{-1}\sum_{i<j}g(U_i,U_j)\). Its variance tends to \(v_d/2\), strictly positive. The normalized residuals are orthogonal to the common pair term, and their mutual covariances are \(O_d(n^{-1})\) by Cauchy–Schwarz. Thus the covariance matrix converges to the rank-one matrix from the stated joint limit, and dividing by the coordinate standard deviations gives the correlation \(1-O_d(n^{-1})\).

For \(k>2\) the finite-sample correlation between \(V_2(n)\) and \(V_k(n)\) is strictly less than one. Indeed, when all input vectors coincide, the residual equals \(c_{d,k}s_d\binom nk(\binom k2-1)>0\). By continuity and full support this residual is nonzero with positive probability. It is centered and orthogonal to \(V_2(n)\), so the correlation is \((1+\operatorname{Var}R_{n,k}/(\beta_{n,k}^2\operatorname{Var}V_2(n)))^{-1/2}<1\), where \(\beta_{n,k}=c_{d,k}\binom{n-2}{k-2}\).

**4. Strict spectral negativity and the trace.** On \(L^2(S^{d-1},\sigma)\), define the integral operator with kernel \(B(u,v)=s_d-\sqrt{1-(u\cdot v)^2}=-g(u,v)\). The Bernstein identity
\[
 \sqrt z=\frac1{2\sqrt\pi}\int_0^\infty(1-e^{-rz})r^{-3/2}\,dr,
 \quad z\ge0,
\]
shows that for every nonconstant even spherical harmonic the coefficient of \(B\) is strictly positive: \(e^{-r(1-t^2)}=e^{-r}e^{rt^2}\) has a strictly positive power-series coefficient at each even tensor degree \(2m\), and those tensor kernels have nonzero components in each even harmonic of degree at most their order. The constant coefficient of \(B\) is zero, and the odd coefficients vanish by parity. The integral representation can be paired with mean-zero test harmonics by first truncating the \(r\)-integral, then using the integrability of \(r^{-3/2}(1-e^{-r(1-t^2)})\). Thus \(B\) is a continuous positive-semidefinite zonal kernel with strictly positive even-degree eigenvalues \(b_{d,2m}\) given by Funk–Hecke and the displayed integral. Its first is evaluated using the normalized quadratic zonal harmonic \(P_2^{(d)}(t)=(dt^2-1)/(d-1)\), and \(\mathbb E[t^2\sqrt{1-t^2}]=s_d/(d+1)\), giving \(b_{d,2}=s_d/(d^2-1)\).

Mercer's theorem on the compact sphere gives the trace identity
\[
 \sum_{m\ge1}N_{d,2m}b_{d,2m}=B(u,u)=s_d,
\]
independent of the choice of \(u\). Parseval gives
\[
 \sum_{m\ge1}N_{d,2m}b_{d,2m}^2
 =\int\!\int g(u,v)^2\,d\sigma(u)d\sigma(v)=v_d.
\]
Both sums converge absolutely (the first by positivity). In particular the common limit has finite variance and the stated sharp centering.

**5. Chi-square limit and sharp support.** Expand the pair kernel in a real orthonormal spherical-harmonic basis, and let \(g_M\) be the part of the expansion of \(g\) through degree \(2M\). For fixed \(M\), the multivariate CLT for empirical harmonic coordinates and the strong law for empirical averages of squared coordinates yield
\[
 \frac1n\sum_{i<j}g_M(U_i,U_j)
 \Longrightarrow -\frac12\sum_{m\le M}b_{d,2m}
 \bigl(X_{d,2m}-N_{d,2m}\bigr),
\]
with an independent chi-square for each degree. A uniform \(L^2\) error bound for omitted canonical pair kernels follows from their Hilbert–Schmidt norm: the omitted normalized U-statistic variance is at most a constant times \(\sum_{m>M}N_{d,2m}b_{d,2m}^2\to0\), independent of \(n\). Taking \(M\to\infty\) gives the infinite centered series. The trace identity converts it into \(W_d=s_d/2-\sum bX/2\). Its nonnegative chi-square sum converges absolutely in \(L^1\) and almost surely by the finite trace. Every term is nonnegative, proving \(W_d\le s_d/2\) almost surely. This bound is sharp: with positive probability finitely many chi-squares are tiny, and by Markov's inequality the independent nonnegative tail is tiny simultaneously. Since \(b_{d,2}>0\), its first chi-square alone has an arbitrarily large positive value, making the law unbounded below. Moreover \(\kappa_3(W_d)=-\sum_{m\ge1}N_{d,2m}b_{d,2m}^3<0\); the sum converges by the trace, so the common law cannot be Gaussian. The variance formula and joint convergence follow.

## Verification

The companion `verify_rankone.py` reproduces gram-determinant zonotope volumes using independent convex-hull volume calculations in dimensions three and four; checks the gamma constants and low Gegenbauer spectral signs and degree-two coefficient in dimensions three through five; reconstructs the nontrivial two-vector conditional mean by independent angular sampling; and checks the explicit three-dimensional third-order Hoeffding residual variance. Execute `python verify_rankone.py` with the packages in `requirements.txt`. These are finite diagnostics for normalization and algebra, not proofs of an infinite spectral theorem or historical priority. The exact proof is in the preceding five steps.

## Relationship to prior work

Schneider and Schuster (2012 arXiv version) develop rotation-invariant Minkowski classes and spherical-harmonic methods; their paper is a deterministic foundation rather than a stochastic joint intrinsic-volume law. Paouris and Pivovarov (2015 preprint; primary 52A22, 52A40) study stochastic intrinsic-volume inequalities for intersections of Euclidean balls; those are different random bodies. Breiding, Bürgisser, Lerario and Mathis (2021 preprint) supply wedge and zonoid-algebra methods, including expected absolute determinants, but not this joint second-order fluctuation vector. Schneider (2022 preprint) gives all intrinsic-volume means for iid segment zonotopes and a central limit theorem under a nonzero first Hoeffding projection; **that nondegeneracy fails here**, since the unit Haar-directions have a constant one-vector conditional mean. Neither the Gaussian theorem nor the mean identity supplies this degenerate joint law.

An earlier publicly accessible result, *Second-order volume fluctuations of isotropic three-dimensional random zonotopes* (2026), already establishes the one-dimensional \(d=3,k=3\) non-Gaussian volume marginal and analyzes the same pair sine kernel. Another earlier result, *Exact surface-area fluctuations of independently rotated three-dimensional Minkowski sums* (2026), handles independent rotations of **full-dimensional fixed bodies**; approximating a segment by thin full-dimensional bodies may recover the separate three-dimensional \(V_2\) marginal by continuity. This marginal is therefore not asserted as new. Neither prior theorem establishes cross-intrinsic-volume dependence or the all-dimensional joint vector. These earlier results are explicitly credited and not claimed as new. The contribution assessed here is the **simultaneous rank-one collapse of all \(d-1\) nontrivial intrinsic volumes, in every fixed dimension**, together with its exact finite-sample pair covariances and strictly one-sided common law. A still-unidentified equivalent extension in stochastic-geometry or degenerate U-statistics literature remains possible.

## Limitations

The segment lengths are fixed and directions independent and Haar-isotropic. All asymptotics fix \(d\); no dimension-uniform errors, random-weight analogues, finite-sample joint distribution, rates sharper than the given fixed-dimension variance bound, or independent mathematical validation are asserted. The full proof uses standard external theorems (Steiner zonotope identity, canonical U-statistics, Funk–Hecke, Mercer, finite-dimensional CLT), whose precise hypotheses have been checked above. Numerical comparisons are corroborative only; priority remains provisional.

## References

1. R. Schneider and F. E. Schuster, *Rotation invariant Minkowski classes of convex bodies*, arXiv:1207.7286v1 (first submitted 2012-07-31), https://arxiv.org/abs/1207.7286 .
2. G. Paouris and P. Pivovarov, *Random ball-polyhedra and inequalities for intrinsic volumes*, arXiv:1510.07292v1 (2015-10-25), https://arxiv.org/abs/1510.07292 .
3. P. Breiding, P. Bürgisser, A. Lerario and L. Mathis, *The zonoid algebra, generalized mixed volumes, and random determinants*, arXiv:2109.14996v1 (2021-09-30), https://arxiv.org/abs/2109.14996 .
4. R. Schneider, *Random zonotopes and valuations*, arXiv:2202.06774v1 (2022-02-14), https://arxiv.org/abs/2202.06774 .
5. *Second-order volume fluctuations of isotropic three-dimensional random zonotopes*, publicly available research record (2026-11-01), cited for the previously known spatial-volume marginal.
6. *Exact surface-area fluctuations of independently rotated three-dimensional Minkowski sums*, publicly available research record (2026-11-02), cited for the distinct full-dimensional rotated-body setting.
