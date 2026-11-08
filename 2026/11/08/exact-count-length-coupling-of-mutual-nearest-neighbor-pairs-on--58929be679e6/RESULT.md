# Exact count–length coupling of mutual nearest-neighbor pairs on an interval

## Finding
For \(n\ge5\) iid uniform points on \((0,1)\), form the directed nearest-neighbor graph with a unique nearest neighbor per point (ties have probability zero). Define \(R_n\) as the number of unordered pairs joined in *both* directions and \(W_n\) as the sum of the corresponding Euclidean edge lengths, **once per mutual pair**. Their exact moments include
\[
\mathbb E R_n=\frac n3,\quad \mathbb E W_n=\frac{2n+3}{18(n+1)},\quad
\operatorname{Cov}(R_n,W_n)=\frac{64n+105}{2700(n+1)}>0.
\]
The previously known marginal count variance is \(\operatorname{Var}(R_n)=2n/45\), whereas the length variance is
\[
\operatorname{Var}(W_n)=\frac{3168n^2+16453n+13035}{81000(n+1)^2(n+2)}.
\]
The joint central limit theorem is
\[
\left(\frac{R_n-n/3}{\sqrt n},\sqrt n\left(W_n-\frac{2n+3}{18(n+1)}\right)\right)
\xrightarrow{d}N_2\left(0,
\begin{pmatrix}2/45&16/675\\16/675&44/1125\end{pmatrix}\right).
\]
In particular \(\operatorname{Corr}(R_n,W_n)\to8/(3\sqrt{22})\), a strictly positive limit despite the disparate scales of count and total length. For the exceptional sizes, \(\operatorname{Cov}(R_3,W_3)=0\) and \(\operatorname{Cov}(R_4,W_4)=1/27\). The expectation formulas hold already for \(n\ge3\).

## Assumptions and scope
Let \(U_1,\ldots,U_n\) be independent uniform points on \((0,1)\), ordered as \(U_{(1)}<\cdots<U_{(n)}\), and put \(D_i=U_{(i+1)}-U_{(i)}\) for \(1\le i\le n-1\). Set \(m=n-1\). For \(m\ge2\), define \(I_i=1\) when \(D_i\) is strictly smaller than its existing neighboring *interpoint* gap(s), otherwise \(I_i=0\). The boundary gaps from \(0\) to the first sample point and from the last sample point to \(1\) **do not** affect the nearest neighbor choices. Then \(R_n=\sum_{i=1}^m I_i\) and \(W_n=\sum_{i=1}^m D_i I_i\). The claims concern Euclidean, not circular, distances; no distance threshold is imposed. The probabilities of ties are zero.

## Proof
**1. Exponential spacing representation.** Take independent unit exponentials \(E_0,E_1,\ldots,E_m,E_{m+1}\), put \(S=\sum_{j=0}^{m+1}E_j\), and use \(D_i\stackrel d=E_i/S\). The normalized gap vector is independent of \(S\), which has gamma shape \(n+1\). Let \(Y_i=E_i I_i\), \(Z=\sum_iY_i\). Then \(W_n\stackrel d=Z/S\), while \(R_n\) is independent of \(S\). It follows exactly that
\[
\mathbb E W_n=\frac{\mathbb EZ}{n+1},\quad
\operatorname{Cov}(R_n,W_n)=\frac{\operatorname{Cov}(R_n,Z)}{n+1},
\]
\[
\operatorname{Var}(W_n)=\frac{\operatorname{Var}(Z)}{(n+1)(n+2)}-\frac{(\mathbb EZ)^2}{(n+1)^2(n+2)}.
\]
The second identity uses independence of normalized spacings and the gamma sum; in particular it is **not** the incorrect shortcut \(\mathbb E[1/S]=1/\mathbb ES\).

**2. Local means and first mixed covariance.** For each endpoint interpoint gap, \((p_i,q_i):=(\mathbb EI_i,\mathbb EY_i)=(1/2,1/4)\). For each interior gap, \((p_i,q_i)=(1/3,1/9)\). Thus \(\mathbb ER_n=n/3\) and \(\mathbb EZ=(2n+3)/18\). The variables associated with gap positions separated by more than two are independent. For the mixed sum \(\operatorname{Cov}(R_n,Z)=\sum_{i,j}\operatorname{Cov}(I_i,Y_j)\), the contributions for every position, every neighboring pair, and every distance-two pair are, respectively:

| Position or unordered pair | Diagonal contribution, or sum of two directions |
| --- | --- |
| endpoint diagonal | \(1/8\) |
| interior diagonal | \(2/27\) |
| endpoint–interior neighbors | \(-5/36\) |
| interior–interior neighbors | \(-2/27\) |
| endpoint–interior distance two | \(1/18\) |
| interior–interior distance two | \(16/675\) |

There are two endpoint diagonals, \(m-2\) interior diagonals, two endpoint–interior neighboring pairs, \(m-3\) interior neighboring pairs, two endpoint–interior distance-two pairs and \(m-4\) interior distance-two pairs for \(m\ge4\). Therefore
\[
\operatorname{Cov}(R_n,Z)=\frac14+\frac{2(m-2)}{27}-\frac5{18}-\frac{2(m-3)}{27}+\frac19+\frac{16(m-4)}{675}
=\frac{64n+105}{2700}.
\]
For example, the nontrivial interior distance-two mixed moment comes from
\[
\mathbb E[I_iY_{i+2}]=\int_0^\infty\!\int_0^\infty b\,e^{-2a-2b-\max(a,b)}\,da\,db=\frac{11}{225};
\]
subtracting \((1/3)(1/9)\) gives \(8/675\) per direction. For the endpoint distance-two pair, the corresponding two weighted joint moments are \(23/288\) and \(11/96\); subtracting products of the boundary and interior means gives \(1/18\) when both directions are combined. This proves the exact mixed covariance.

**3. Exact length variance.** The local covariance table for \(Y_i\) is: \(3/16\) on endpoint diagonals, \(5/81\) on interior diagonals, \(-1/36\) for adjacent endpoint–interior pairs, \(-1/81\) for adjacent interior pairs, \(1/48\) for distance-two endpoint–interior pairs, and \(73/10125\) for distance-two interior pairs; all more distant pairs have covariance zero. The last entry follows from
\[
\mathbb E[Y_iY_{i+2}]=\int_0^\infty\!\int_0^\infty ab\,e^{-2a-2b-\max(a,b)}\,da\,db=\frac{22}{1125}.
\]
The boundary distance-two moment is \(7/144\). Summing gives
\[
\operatorname{Var}(Z)=\frac38+\frac{5(m-2)}{81}-\frac19-\frac{2(m-3)}{81}+\frac1{12}+\frac{146(m-4)}{10125}
=\frac{4168n+15285}{81000}.
\]
The gamma normalization in Step 1 yields the displayed exact \(\operatorname{Var}(W_n)\). Standard local-minimum indicator enumeration gives \(\operatorname{Var}(R_n)=2n/45\) for \(n\ge5\), also independently checked using the verifier.

**4. Joint Gaussian limit.** Away from the two boundary gaps the stationary vector sequence \((I_i,Y_i,E_i)\) is 2-dependent and has all moments. By the multivariate finite-dependent central limit theorem, its normalized sums converge jointly to Gaussian limits; the finitely many boundary terms disappear at square-root scale. The long-run covariance coefficients are
\[
\lim_{n\to\infty}\frac{\operatorname{Var}R_n}{n}=\frac2{45},\quad
\lim_{n\to\infty}\frac{\operatorname{Cov}(R_n,Z)}n=\frac{16}{675},\quad
\lim_{n\to\infty}\frac{\operatorname{Var}Z}{n}=\frac{521}{10125}.
\]
Gamma–Dirichlet independence gives \(\operatorname{Cov}(R_n,S)=0\) and \(\operatorname{Cov}(Z,S)=\mathbb EZ\); also \(\operatorname{Var}S=n+1\). Applying the delta method to \(W_n=Z/S\), using \(S/n\to1\) and \(\mathbb EZ/n\to1/9\), yields limiting length variance \(521/10125-1/81=44/1125\) and unchanged cross-covariance \(16/675\). The claimed bivariate CLT follows. The limiting correlation is
\[
\frac{16/675}{\sqrt{(2/45)(44/1125)}}=\frac8{3\sqrt{22}}.
\]

**5. Small-size exceptions.** For \(n=3\), exactly one gap is a local minimum so \(R_3\equiv1\) and the covariance vanishes. For \(n=4\), the two extreme gaps are simultaneously minima precisely when the middle interpoint gap is the largest. The same exponential calculation gives \(\operatorname{Cov}(R_4,W_4)=1/27\); its exceptional local distance-two pair has two boundary gaps.

## Verification
The standalone, standard-library-only `verify.py` enumerates every rank ordering of the \(n-1\) interpoint gaps for \(3\le n\le9\), conditional on exact means and second moments of exponential order statistics. It checks 33 exact rational formulas, covering both covariance exceptions and all five main finite identities at larger sizes. Execute `python verify.py`; no internet access, optional dependencies or approximate numerical tolerance are used. These finite checks corroborate, but do not replace, the all-size integral proof or the m-dependent central limit theorem.

## Relationship to prior work
Bahadır and Ceyhan (first publicly available arXiv version, 2016) establish the *unweighted* reciprocal-pair count's mean, variance, recurrence, and marginal Gaussian limit and its representation as local minima of uniform spacings. Penrose and Wade (arXiv 2006) establish expectations and variances of total power-weighted lengths of the *whole directed* one-dimensional nearest-neighbor graph. Neither separate marginal law supplies the mixed statistic \(\operatorname{Cov}(R_n,W_n)\), the length restricted to reciprocal edges, or their explicit joint Gaussian covariance matrix. The marginal count result is used as prior art, not claimed as new.

## Limitations
The model is restricted to iid uniform sampling on one finite interval. The length statistic counts each reciprocal edge once; counting both directed arcs would double the length and all cross-covariances. These results do not assert distribution-free behavior for arbitrary nonuniform densities or validity in higher dimensions. General spatial stabilization theories may cover existence of related central limits without yielding the exact constants. The review is not independent; historical priority beyond the inspected sources remains uncertain.

## References
1. M. D. Penrose and A. R. Wade, *Limit theory for the random on-line nearest-neighbour graph*, arXiv:math/0603561v1, first public 2006-03-23, especially Theorem 2.3 on the directed nearest-neighbor edge-length moments. https://arxiv.org/abs/math/0603561
2. S. Bahadır and E. Ceyhan, *On the Number of Reflexive and Shared Nearest Neighbor Pairs in One-Dimensional Uniform Data*, arXiv:1605.01940v1, first public 2016-05-06, especially Lemma 2.1, Section 3.1 and Section 4. https://arxiv.org/abs/1605.01940
