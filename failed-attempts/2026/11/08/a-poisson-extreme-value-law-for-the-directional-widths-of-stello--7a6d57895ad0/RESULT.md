# A Poisson extreme-value law for the directional widths of stellohedra

## Finding

For every integer \(m\ge 3\), consider the unweighted simplex-sum stellohedron
\[
K_m=\sum_{S\subseteq[m]}\operatorname{conv}\{e_0,e_i:i\in S\}
       +\sum_{i=1}^{m}\{e_i\}\subset\mathbb R^{m+1}.
\]
The singleton terms are translations and do not affect widths. The polytope is \(m\)-dimensional in its affine hyperplane. Let \(W_m\) be its Euclidean width in a Haar-uniform unit direction of the linear hyperplane perpendicular to \((1,\ldots,1)\). Write \(\Phi\) and \(\phi\) for the standard-normal CDF and density, and set
\[
a_m=\Phi^{-1}(1-1/m),\qquad
\mu_m=\sqrt2\,\frac{\Gamma((m+1)/2)}{\Gamma(m/2)}.
\]
Let \(M_m\) be a real random variable with CDF
\[
\Pr(M_m\le t)=\Phi(t)\left(\frac{1+\Phi(t)}2\right)^m.
\]
Then the **exact finite-dimensional mean width** is
\[
\boxed{\mathbb E W_m=\frac{2^{m+1}}{\mu_m}\,\mathbb E M_m.}
\]
The expectation on the right is the convergent one-dimensional integral
\[
\mathbb E M_m=\int_0^\infty \left[1-\Phi(t)\left(\frac{1+\Phi(t)}2\right)^m
-\Phi(-t)\left(\frac{1+\Phi(-t)}2\right)^m\right]dt.
\]
Let \((E_j)_{j\ge1}\) be independent exponential random variables of rate one, \(\Gamma_j=E_1+\cdots+E_j\), and
\[
T=\sum_{j=1}^{\infty}2^{-j}(-\log\Gamma_j).
\]
This series converges absolutely almost surely and in every fixed \(L^p\), \(p<\infty\). With \(T_1,T_2\) independent copies of \(T\),
\[
\boxed{a_m\left(\frac{\sqrt m}{2^m}W_m-2a_m\right)
\ \xrightarrow{d}\ T_1+T_2.}
\]
Convergence also holds for the first two moments of the displayed normalized quantity. In particular, with Euler's constant \(\gamma\) and the dilogarithm \(\operatorname{Li}_2(z)=\sum_{r\ge1}z^r/r^2\),
\[
\boxed{\mathbb E W_m=\frac{2^m}{\sqrt m}
\left(2a_m+\frac{2(\gamma-\log2)}{a_m}+o(a_m^{-1})\right),}
\]
\[
\boxed{\frac{m a_m^2}{4^m}\operatorname{Var}(W_m)
\longrightarrow 2\left[\frac{\pi^2}{6}-2\operatorname{Li}_2(1/2)
+\operatorname{Li}_2(1/4)\right].}
\]
The last constant is strictly positive (approximately \(1.4962113060\)), and the limiting law is non-Gaussian.

## Assumptions and scope

The realization is the **specific unweighted Euclidean Minkowski sum** written above; combinatorial equivalence or an arbitrary affine deformation is not sufficient. All summands \(\operatorname{conv}\{e_0,e_i:i\in S\}\) have coefficient one, including the singleton \(S=\varnothing\). Directions are uniform on the sphere in the \(m\)-dimensional zero-sum subspace; the width is the full length of the orthogonal one-dimensional projection, not a support value or half-width. All asymptotics take \(m\to\infty\) through integers. The constant \(\mu_m\) is the mean radius of an \(m\)-dimensional standard Gaussian.

## Proof

**1. Exact support reduction.** Let \(G_0,G_1,\ldots,G_m\) be independent standard normals, and let \(P\) project onto the zero-sum hyperplane. Then \(PG/\|PG\|\) is uniform on the intrinsic sphere. For any deterministic \(g\), order the leaf coordinates as \(g_{(1)}\ge\cdots\ge g_{(m)}\) and \(g_{[1]}\le\cdots\le g_{[m]}\). Support functions add under Minkowski addition. A subset of leaves selected with independent probability \(1/2\) has its first selected leaf at decreasing rank \(j\) with probability \(2^{-j}\). Consequently the exact normalized support range is
\[
R_m(g):=2^{-m}\sum_{S\subseteq[m]}
\left[\max(g_0,\{g_i:i\in S\})-\min(g_0,\{g_i:i\in S\})\right]
=\sum_{j=1}^{m}2^{-j}\left[(g_{(j)}-g_0)_++(g_0-g_{[j]})_+\right].
\]
Here \((x)_+=\max(x,0)\), with an empty subset giving zero range. In particular
\[
W_m=\frac{2^m R_m(G)}{\|PG\|}.
\]
This identity remains true with the singleton translations in \(K_m\): they cancel exactly from opposite supports.

**2. Exact expectation.** Introduce independent Bernoulli-\(1/2\) selectors \(B_i\). The random maximum of \(G_0\) and the selected \(G_i\)'s has the stated CDF, because the event that every selected leaf is at most \(t\) has probability \(((1+\Phi(t))/2)^m\). Its negative has the distribution of the corresponding minimum. Thus \(\mathbb E R_m(G)=2\mathbb E M_m\). Translation invariance and positive homogeneity imply \(R_m(G)=\|PG\|R_m(PG/\|PG\|)\). The Gaussian radius and the intrinsic direction are independent, so division by \(\mu_m=\mathbb E\|PG\|\) proves the finite formula.

**3. Upper and lower extremes.** Since \(m\,[1-\Phi(a_m+x/a_m)]\to e^{-x}\) for each fixed \(x\), the point processes of \(a_m(G_i-a_m)\) near the upper tail and \(a_m(-G_i-a_m)\) near the lower tail converge jointly to independent Poisson processes of intensity \(e^{-x}dx\). This is seen directly from multinomial factorial moments: the two disjoint tail events have probabilities asymptotic to \(e^{-x}/m\). Their decreasing ordered points are, in distribution, \((-\log\Gamma_j)_{j\ge1}\) and an independent copy.

To pass from finitely many extremes to the geometric weights, note that the normalized maximal support \(2^{-m}\sum_S\max(G_0,G_i:i\in S)\) is the conditional expectation of \(M_m\) given the Gaussian sample. The maximum \(M_m\), centered at \(a_m\) and multiplied by \(a_m\), has uniformly bounded moments of every fixed order: its explicit CDF above and the Gaussian Mills bounds give an exponential upper tail and a double-exponential lower tail, apart from smaller Gaussian tails where its argument is negative. For a fixed \(J\), if a Bernoulli-selected leaf is among the top \(J\), the maximum equals that selected leaf unless \(G_0\) exceeds it. The latter error vanishes in every fixed moment as \(m\to\infty\), because the hub is among the largest \(J\) of the \(m+1\) i.i.d. coordinates with probability at most \(J/(m+1)\). On the complementary event no top-\(J\) leaf is selected, of probability \(2^{-J}\), Hölder's inequality and the uniform moment bounds control the normalized error in \(L^2\) by \(O(2^{-J/4})\). The analogous argument for minima yields the weighted sums of the two independent Poisson extremes, with \(L^2\) moment convergence. Since \(\|PG\|/\sqrt m=1+O_{L^p}(m^{-1/2})\) for every fixed \(p\) (with the needed reciprocal moments for large \(m\)), the radius replacement changes the centered, \(a_m\)-scaled expression by \(O_{L^2}(a_m^2/\sqrt m)=o(1)\). This proves the limit law and moment convergence.

**4. Mean and variance constants.** For integer \(j\ge1\), the gamma logarithm has \(\mathbb E[-\log\Gamma_j]=\gamma-H_{j-1}\), where \(H_k=\sum_{r=1}^k1/r\). Summing against \(2^{-j}\), using \(\sum_{j\ge1}2^{-j}H_{j-1}=\log2\), gives \(\mathbb ET=\gamma-\log2\). For \(i\le j\), beta-gamma independence gives \(\Gamma_i=U_{i,j}\Gamma_j\), where \(U_{i,j}\) is independent of \(\Gamma_j\); hence
\[
\operatorname{Cov}(-\log\Gamma_i,-\log\Gamma_j)=\psi_1(j),
\]
where \(\psi_1\) is the trigamma function. Regrouping yields
\[
\operatorname{Var}(T)=\sum_{j\ge1}(2^{1-j}-3\,4^{-j})\psi_1(j).
\]
The identity \(\sum_{j\ge1}z^j\psi_1(j)=\frac{z}{1-z}(\pi^2/6-\operatorname{Li}_2(z))\), valid for \(0<z<1\), evaluates this as \(\pi^2/6-2\operatorname{Li}_2(1/2)+\operatorname{Li}_2(1/4)\). Its positivity follows already from the positive diagonal covariance contribution and nonconstant \(T\). Independence of the two tails gives twice that variance. The limit is not Gaussian: on \(E_1<e^{-2t}\), the term \(2^{-1}(-\log E_1)\) exceeds \(t\), while the remaining series has a fixed-probability lower bound independent of \(E_1\) (use \(E_1\le1\) and \(\Gamma_j\le 1+E_2+\cdots+E_j\)). Thus \(\Pr(T>t-C)\) is bounded below by a positive multiple of \(e^{-2t}\) for large \(t\). The sum of two independent copies inherits an at-least-exponential right tail, impossible for a nondegenerate Gaussian. Taking moments of the limiting theorem gives both asymptotic formulas.

## Verification

Run `python verify_stellohedron.py` with Python 3, NumPy, and SciPy. The checker enumerates every relevant simplex-subset support term for dimensions two through eight and compares it to the sorted-order formula; numerically quadratures the exact mean law and compares it with independent spherical Monte Carlo; checks the trigamma-to-dilogarithm identity; simulates the independent exponential-series limit; and tests the prescribed finite-dimensional scaling. The output marker is `STELLOHEDRON_WIDTH_POISSON_LIMIT_CHECKS_PASSED`. Sampling is corroboration, not a proof of the asymptotic theorem.

## Relationship to prior work

The Minkowski-sum realization and the name stellohedron are classical; see Postnikov--Reiner--Williams, §10.4, and Postnikov's foundational generalized-permutohedron framework. Bayer and coauthors (first arXiv public version March 12, 2024) discuss the same stellohedral building set and its relationship to generalized parking-function polytopes. These works provide the geometric object, its combinatorics, and related face structure, not this random-direction width distribution or its Poisson-series fluctuations. The Gaussian extreme-value point process and beta-gamma identities are standard ingredients and are not claimed as novel. The contribution assessed here is their precise geometric synthesis, including the exact finite width integral and the non-Gaussian fluctuation variance constant.

## Limitations

Only the explicit unweighted simplex-sum realization is covered; general positive weights on tubes, other graph associahedra, oblique metrics, and non-Haar sampling are not. No convergence rate beyond the displayed leading asymptotics is proved. Historical priority of an equivalent result expressed in Gaussian order-statistic or stellohedron terminology is not independently certified; the theorem requires external mathematical review before broader claims of priority.

## References

- A. Postnikov, V. Reiner, L. Williams, *Faces of Generalized Permutohedra*, arXiv:math/0609184, originally posted September 6, 2006; §10.4 on the stellohedron.
- A. Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163, originally posted July 7, 2005; coordinate-simplex Minkowski sums.
- M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387, originally posted March 12, 2024; §3 on the stellohedral building set.
- S. Forcey and M. Ronco, *Algebraic structures on graph associahedra*, *J. London Math. Soc.* 106 (2022), 1189–1231, DOI:10.1112/jlms.12596 (comparative combinatorial context; abstract inspected).
