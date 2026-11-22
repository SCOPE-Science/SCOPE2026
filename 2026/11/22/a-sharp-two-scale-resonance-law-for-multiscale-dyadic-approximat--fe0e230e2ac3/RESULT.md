# A sharp two-scale resonance law for multiscale dyadic approximation of bounded variation

## Finding

For every positive integer \(m\), the optimal constants for the cumulative dyadic approximation residual of any real \(BV(0,1)\) function are
\[
\sup_{V(f)>0}\frac{\sum_{j=0}^{2m-1}\|f-E_jf\|_{L^2(0,1)}^2}{V(f)^2}
=\frac49(1-4^{-m}),
\qquad
\sup_{V(f)>0}\frac{\sum_{j=0}^{\infty}\|f-E_jf\|_{L^2(0,1)}^2}{V(f)^2}=\frac49.
\]
The infinite sum is finite for all such functions. At every displayed finite depth, and for the infinite sum, all nonconstant equality cases are precisely
\[
f(x)=a+b\mathbf1_{[t,1)}(x),\qquad b\ne0,\quad t\in\{1/3,2/3\},
\]
up to changes on sets of Lebesgue measure zero. Here \(a,b\) are real constants.

There is also an exact, quantitative jump-location deficit. For \(H_t=\mathbf1_{[t,1)}\), \(t\in(0,1)\), put \(d(u)=\min(\{u\},1-\{u\})\), where \(\{u\}\) is the fractional part. Then
\[
\sum_{j=0}^{2m-1}\|H_t-E_jH_t\|_2^2
=\frac49(1-4^{-m})-3\sum_{k=0}^{m-1}4^{-k}
\left(d(4^kt)-\frac13\right)^2.
\]
The same identity holds for the infinite sum with \(m\to\infty\) and \(4^{-m}\to0\). In particular, writing \(\Delta(t)=\operatorname{dist}(t,\{1/3,2/3\})\), for any \(f\in BV(0,1)\) with nonzero variation and normalized derivative-variation measure \(p=|Df|/V(f)\),
\[
\frac{\sum_{j=0}^{2m-1}\|f-E_jf\|_2^2}{V(f)^2}
\le\frac49(1-4^{-m})-3\int_{(0,1)}\Delta(t)^2\,dp(t),
\]
with the analogous infinite-depth bound using \(4/9\). Thus squared-error deficit at most \(\varepsilon\) forces \(p\{t:\Delta(t)\ge\eta\}\le\varepsilon/(3\eta^2)\) for every \(\eta>0\).

## Assumptions and scope

The underlying measure on \((0,1)\) is ordinary Lebesgue measure. \(BV(0,1)\) means real functions with distributional derivative a finite signed Borel measure \(Df\) in the open interval, and \(V(f)=|Df|((0,1))\); additive constants are immaterial. For each integer \(j\ge0\), \(E_j\) is the orthogonal \(L^2\) projection onto the functions constant on each half-open interval \([k2^{-j},(k+1)2^{-j})\), with the harmless endpoint convention. For \(m\ge1\), exactly \(2m\) residual levels \(j=0,\ldots,2m-1\) are included; the infinite objective includes all \(j\ge0\). No anchoring condition is imposed on \(f\).

## Proof

**Step 1: reduction to a jump response.** With \(\mu=Df\), the fundamental theorem for one-dimensional bounded-variation functions yields \(f(x)=a+\int_{(0,1)}H_t(x)\,d\mu(t)\) for almost every \(x\). Let \(\mathcal T_J f=((I-E_j)f)_{0\le j<J}\) in the Hilbert direct sum of \(J\) copies of \(L^2(0,1)\); use \(J=\infty\) for the countable direct sum. Since \(\|H_t-E_jH_t\|_2^2\le2^{-j}/4\), the jump vectors have uniformly bounded direct-sum norm also for \(J=\infty\), so the vector-valued signed-measure integral is legitimate. The Hilbert triangle inequality gives
\[
\|\mathcal T_J f\|\le\int\|\mathcal T_J H_t\|\,d|\mu|(t)
\le V(f)\sup_{0<t<1}\|\mathcal T_J H_t\|.
\]
Single jumps attain their own responses, proving that the operator norm is the supremum of those responses.

**Step 2: exact jump response.** At level \(j\), only the unique dyadic cell containing \(t\) contributes to \((I-E_j)H_t\). Its length is \(h=2^{-j}\), its relative cut point is \(u=\{2^jt\}\), and direct integration of the two constant residual values gives
\[
\|H_t-E_jH_t\|_2^2=2^{-j}\phi(2^jt),\qquad
\phi(v)=\{v\}(1-\{v\}).
\]
For \(u\in[0,1]\), elementary case splitting at \(1/2\) gives
\[
\phi(u)+\frac12\phi(2u)=2d(u)-3d(u)^2
=\frac13-3\left(d(u)-\frac13\right)^2.
\]
Grouping the terms \(j=2k\) and \(j=2k+1\) proves the finite deficit identity and sharp upper bound. Equality requires \(d(t)=1/3\), so already the first two scales force \(t=1/3\) or \(2/3\). Conversely, multiplication by \(4\) fixes both fractional parts, so these two points make every squared deficit zero. The geometric majorant \(\sum_{j\ge J}2^{-j}/4\) ensures uniform convergence and the same sharp infinite formula and equality locations.

**Step 3: equality and strictness for general variation measures.** For distinct \(0<s<t<1\), the covariance Gram determinant of the first-level centered jumps is
\[
\det\begin{pmatrix}
\langle(I-E_0)H_s,(I-E_0)H_s\rangle&\langle(I-E_0)H_s,(I-E_0)H_t\rangle\\
\langle(I-E_0)H_t,(I-E_0)H_s\rangle&\langle(I-E_0)H_t,(I-E_0)H_t\rangle
\end{pmatrix}
=s(1-t)(t-s)>0.
\]
Thus distinct jump-response vectors are never collinear; equality in the Hilbert triangle inequality forces the normalized variation measure to be a point mass. The only allowable point is \(1/3\) or \(2/3\), giving the displayed classification (and conversely each function listed attains equality).

**Step 4: quantitative localization.** Convexity of squared Hilbert norm gives the stronger Jensen bound
\[
\|\mathcal T_J f\|^2/V(f)^2\le\int\|\mathcal T_JH_t\|^2\,dp(t).
\]
The first summand of the jump deficit is \(3(d(t)-1/3)^2=3\Delta(t)^2\). Dropping the remaining nonnegative deficits yields the stability bound. The mass bound follows from \(\int\Delta(t)^2\,dp(t)\ge\eta^2p\{\Delta\ge\eta\}\).

**Step 5: Haar interpretation.** For the orthogonal dyadic martingale differences \(D_k=E_{k+1}-E_k\), Parseval and monotone summation give the equivalent infinite-depth identity
\[
\sum_{j\ge0}\|f-E_jf\|_2^2
=\sum_{k\ge0}(k+1)\|D_kf\|_2^2.
\]
The result is therefore an exact logarithmically level-weighted Haar-energy inequality controlled by ordinary variation. Its constant is not obtained by optimizing the individual levels separately: the separate-level bounds yield only \(1/2\), whereas the coupled exact optimum is \(4/9\).

## Verification

The standalone Python 3 program `check_multiscale.py` evaluates all rational arithmetic exactly. It independently computes the piecewise-quadratic maximum on every dyadic cell for even depths \(2,4,6,8,10,12\), checks the deficit identity at rational jump locations, and checks a signed multi-jump sample against the sharp variation bound. These are finite consistency tests; the proof for all depths and general \(BV\) inputs is the preceding analytic argument, not the enumeration. Run `python3 check_multiscale.py` using a standard Python 3 installation.

## Relationship to prior work

Allaart and Kawamura (2011) survey Takagi-type dyadic orbit sums based on the **linear tent map**. The residual analyzed here is a distinct parabolic fractional-part sum, and the relevant two-scale identity completes a sharp variation-norm inequality rather than describing Takagi level sets. Osȩkowski (2013) studies restricted weak-type estimates for Haar projections and martingale transforms; the target here is the simultaneous squared \(L^2\) residual of an entire nested family, with real ordinary variation as input norm. Goginava and Nagy (2022) study matrix summability of Walsh–Fourier series, not this sharp combined \(BV\)-to-Hilbert norm.

The closest identified related sharp results on individual dyadic resolutions, and results on exponentially weighted Haar energy, do not imply the exact logarithmic-level-weighted constant, its equality set, or the multiscale deficit. No universal claim of priority is made: historical sources not indexed by the searches could contain an equivalent inequality.

## Limitations

The theorem is one-dimensional, real-valued, uses ordinary (not periodic or anisotropic) distributional variation, and concerns the standard binary filtration. The finite sharp constants are asserted only for **even** numbers of residual levels; the theorem gives no classification for arbitrary odd cutoffs, other bases, signed scale weights, or nonlinear approximants. The algebraic and numerical checker cannot establish the infinite-dimensional result by itself. Originality remains subject to a full independent historical priority review.

## References

1. Pieter C. Allaart and Kiko Kawamura, *The Takagi function: a survey*, arXiv:1110.1691 (first publicly posted 2011-10-08), https://arxiv.org/abs/1110.1691.
2. Adam Osȩkowski, *Sharp Inequalities for the Haar System and Fourier Multipliers*, *Journal of Function Spaces* (2013), Article 646012, https://doi.org/10.1155/2013/646012.
3. Ushangi Goginava and Károly Nagy, *Matrix Summability of Walsh–Fourier Series*, *Mathematics* 10 (2022), 2458, https://doi.org/10.3390/math10142458.
