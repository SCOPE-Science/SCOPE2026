# Exact weighted-Wiener grid ambiguity and the smoothness-one alias transition

## Finding

Let \(d\ge 1\), \(m_j\in\mathbb N\), \(r_j>0\) for \(1\le j\le d\). On the probability torus \(\mathbb T^d=(\mathbb R/\mathbb Z)^d\), consider the complex weighted Wiener space
\[
\mathcal A_{\mathbf r}=\left\{f(x)=\sum_{k\in\mathbb Z^d}a_k e^{2\pi i k\cdot x}:\quad
\|f\|_{\mathcal A_{\mathbf r}}:=\sum_{k\in\mathbb Z^d}\left(\prod_{j=1}^d(1+|k_j|)^{r_j}\right)|a_k|<\infty\right\}.
\]
For any translate \(G=x_0+\prod_{j=1}^d\{0,1/m_j,\ldots,(m_j-1)/m_j\}\) and the radius of functions invisible to these point measurements,
\[
R(G)=\sup\{\|f\|_{L^2(\mathbb T^d)}:\ \|f\|_{\mathcal A_{\mathbf r}}\le 1,\ f|_G=0\},
\]
we obtain the **exact finite-sample formula**
\[
\boxed{R(G)=\max_{1\le j\le d}\frac{\sqrt2}{F_{m_j}(r_j)},\qquad
F_m(r)=\begin{cases}
1+(m+1)^r,&0<r\le1,\\
(1+\lfloor m/2\rfloor)^r+(1+\lceil m/2\rceil)^r,&r\ge1.
\end{cases}}
\]
The two branches agree at \(r=1\). The value is independent of the grid translate. Every extremizer is a two-frequency difference supported on one coordinate axis, for an axis maximizing the displayed fraction; its pair of frequencies is an equal-cost pair described below. In particular, in dimension one the only optimal unordered alias pairs are
\[
\begin{array}{ll}
\{0,m\},\{-m,0\},&0<r<1,\\
\{-a,m-a\}\ (a=0,1,\ldots,m),&r=1,\\
\{-a,m-a\}\ (a\in\{\lfloor m/2\rfloor,\lceil m/2\rceil\}),&r>1.
\end{array}
\]
At \(r=1\) there is an exact change from endpoint to centered aliasing, with a whole family of intermediate extremizers at the transition.

Moreover the maximum \(L^2\)-distance between two unit-ball functions agreeing on \(G\) equals **\(2R(G)\)**. Consequently every reconstruction algorithm, including nonlinear algorithms, based only on these grid data incurs worst-case error at least \(R(G)\).

For \(d=1\) the radius is asymptotic to \(C_r m^{-r}\), where \(C_r=\sqrt2\) for \(0<r\le1\) and \(C_r=2^{r-1/2}\) for \(r>1\). By the previously published optimized non-linear sampling upper bound for \(\mathcal A_1^r\) in \(L^2\), of order \(m^{-(r+1/2)}\) times a finite logarithmic power, equally spaced sampling is polynomially inferior to suitably selected sampling locations for every fixed \(r>0\).

## Assumptions and scope

All functions and coefficients are complex-valued, the \(L^2\) norm uses normalized Haar measure, and each \(r_j\) is strictly positive. A grid is a **fixed** prescribed set of point evaluations, not a minimization over all designs. The radius is a nullspace invariant and a universal recovery lower bound; it is *not* asserted to equal the full minimax error of optimal reconstruction on that grid. The source space is the weighted coefficient \(\ell^1\) space (the \(\theta=1\) case of the Wiener scale), not a Sobolev Hilbert space.

A more general alias lemma holds. If \(H\subset\mathbb T^d\) is any finite subgroup and \(w_k\ge1\) are positive weights tending to infinity as \(\|k\|_\infty\to\infty\), set \(\|f\|_w=\sum_kw_k|a_k|\). Write
\[
q(H,w)=\min_{k\ne\ell:\ (k-\ell)|_H\equiv0}(w_k+w_\ell).
\]
Then, on any coset of \(H\), the exact \(L^2\) nullspace radius is \(\sqrt2/q(H,w)\); all equality cases are two opposite Fourier coefficients on a minimizing alias pair, with phase adjusted for the coset translation. The minimum exists by properness of the weights. The stated grid theorem is an exact evaluation of this natural pair invariant for polynomial product weights.

## Proof

**1. Aliasing and a sharp weighted zero-sum lemma.** Let \(G=x_0+H\). Multiply each Fourier coefficient \(a_k\) by \(e^{2\pi i k\cdot x_0}\); this preserves its magnitude and the \(L^2\) norm. The characters of the finite group \(H\) are precisely the residue classes of \(\mathbb Z^d\) modulo the annihilator \(H^\perp\). By finite-group Fourier inversion and absolute convergence, vanishing at every point of \(G\) is equivalent to the sum of the adjusted coefficients being zero separately in every residue class.

Fix one such class \(C\). Let \(u\le v\) be its two smallest weights, counted with multiplicity, and let \((b_k)_{k\in C}\in\ell^1\) satisfy \(\sum_{k\in C}b_k=0\). Write \(L=\sum|b_k|\), \(W=\sum w_k|b_k|\). Every coefficient satisfies \(|b_k|\le L-|b_k|\), hence \(\max|b_k|\le L/2\). Choose an index \(k_0\) with smallest weight \(u\). The remaining weights are at least \(v\), and \(|b_{k_0}|\le L/2\), so
\[
W\ge u|b_{k_0}|+v(L-|b_{k_0}|)\ge\frac{u+v}{2}L.
\]
Likewise
\[
\sum_{k\in C}|b_k|^2\le(\max|b_k|)L\le\frac{L^2}{2},
\qquad
\|b\|_{\ell^2(C)}\le\frac{\sqrt2}{u+v}W.
\]
Equality in the second bound requires precisely two nonzero coefficients of equal magnitude. Their zero sum forces opposite phases. Equality in the weighted bound requires their weights to be the smallest two. The witness \((b_k,b_\ell)=(c,-c)\), with \(|c|=(u+v)^{-1}\), attains equality.

Across the finitely many residue classes, the orthogonal \(\ell^2\) sums satisfy
\[
\sum_C\|b\|_{\ell^2(C)}^2\le\frac{2}{q(H,w)^2}\sum_C W_C^2
\le\frac{2}{q(H,w)^2}\left(\sum_C W_C\right)^2.
\]
If equality holds and the total norm is nonzero, all mass belongs to one residue class; the preceding equality characterization gives exactly one two-frequency alias pair. Parseval proves the general lemma and the characterization of all extremizers.

**2. Evaluating the product-grid invariant.** For the rectangular subgroup, two distinct Fourier frequencies are aliases exactly when their difference has coordinates divisible by the corresponding \(m_j\). At least one coordinate \(j\) differs by a nonzero multiple of \(m_j\). Since every weight factor is at least one,
\[
w_k+w_\ell\ge(1+|k_j|)^{r_j}+(1+|\ell_j|)^{r_j}\ge F_{m_j}(r_j).
\]
The last inequality follows by moving any pair of integers separated by a positive multiple of \(m_j\) toward zero until their distance is exactly \(m_j\), without increasing either absolute value. The least sum at that distance therefore has the form
\[
F_m(r)=\min_{a\in\{0,\ldots,m\}}\big[(1+a)^r+(1+m-a)^r\big].
\]
For \(0<r<1\), strict concavity forces the two endpoints; for \(r>1\), strict convexity forces the one or two central integers; for \(r=1\), the expression is identically \(m+2\). Conversely, pairs \(k=-a e_j\) and \(\ell=(m_j-a)e_j\) attain the one-dimensional minimum on each coordinate axis, with all other coordinates zero. Therefore \(q(G,w)=\min_jF_{m_j}(r_j)\) and the formula follows. Strict positivity of each exponent rules out additional off-axis minimizers: a nonzero transverse coordinate strictly increases its product weight.

For the shifted grid, the extremizing pair uses coefficients of equal absolute value and relative phase chosen so the two characters cancel at \(x_0\); no amplitude change is needed. This proves translate independence and the complete equality list.

**3. Information diameter and algorithmic consequence.** If \(f,g\) both belong to the unit Wiener ball and have the same grid samples, then \(h=(f-g)/2\) is in the unit ball and vanishes on the grid. Hence \(\|f-g\|_2\le2R(G)\). Equality is attained by an invisible extremizer \(h\) and the pair \(f=h\), \(g=-h\). Every reconstruction rule produces the same output for this pair; by the triangle inequality its error is at least \(R(G)\) on one of them.

For \(d=1\), the displayed formula gives the asymptotic constant by elementary expansion. The optimized sampling upper bound in Moeller (2026, Theorem 7.4) for \(\theta=1,q=2,d=1\) is \(O_r(m^{-(r+1/2)}(\log m)^{3r+3/2})\), with \(r>0\). Consequently the ratio between the best possible error on the fixed equispaced grid and the unrestricted optimal sampling error is at least a constant multiple of \(m^{1/2}/(\log m)^{3r+3/2}\), hence diverges. The earlier upper bound is credited, not reproved here.

## Verification

The analytic proof covers every Fourier series in the source space, not only finite trigonometric polynomials. A standalone standard-library script, `verify_alias_wiener.py`, checks the exact discrete minimizers for 27 grid sizes and several exponents, searches alias pairs over larger frequency windows, verifies two-mode zero samples, tests random multiblock finite Fourier nullspaces, and independently enumerates selected two-dimensional product-grid alias pairs. Its output is `WEIGHTED_WIENER_ALIAS_KERNEL_FINITE_CHECK_OK 9029`. These finite checks corroborate the formulas; they are not substitutes for the infinite-dimensional proof.

## Relationship to prior work

Moeller (arXiv:2611.12558, first posted 9 November 2026), Sections 2–3 and 6–7, defines the same weighted Wiener scale and obtains rates for **optimized** Gelfand and nonlinear sampling widths, including the upper bound used in the comparison. It does not state the exact fixed-grid nullspace norm, all equality configurations, or the smoothness-one frequency-pair transition. Moeller–Stasyuk–Ullrich (2026, Theorem 6.1) supplies an earlier optimized sampling upper bound with a related logarithmic exponent; Kolomoitsev–Lomako–Tikhonov (2023, Sections 5–6) studies interpolation/quasi-interpolation on grids and asymptotic approximation estimates, not this exact zero-fiber radius. Classical Fourier aliasing and convexity are essential inputs, rather than claimed as new. The new statement is about a prescribed data geometry, so it is not a disguised restatement of optimized-width asymptotics.

## Limitations

No assertion is made about real-valued signals, \(\theta\ne1\) Wiener coefficient norms, noise robustness, arbitrary non-subgroup sample sets, or the exact full minimax reconstruction error for a fixed grid. The sharp result is an information-theoretic obstruction for the specified complex weighted Wiener balls. All coverage comparisons are best knowledge; equivalent classical sampling formulas not indexed in the inspected sources remain a priority risk. Independent mathematical validation has not been performed.

## References

1. M. Moeller, *Gelfand and sampling numbers of weighted Wiener spaces* (first posted 9 November 2026), arXiv:2611.12558, https://arxiv.org/abs/2611.12558 .
2. M. Moeller, S. Stasyuk, and T. Ullrich, *Best m-term trigonometric approximation in weighted Wiener spaces and applications*, Advances in Operator Theory 11 (2026), https://doi.org/10.1007/s43036-025-00480-8 .
3. Y. Kolomoitsev, T. Lomako, and S. Tikhonov, *Sparse Grid Approximation in Weighted Wiener Spaces*, Journal of Fourier Analysis and Applications 29 (2023), https://doi.org/10.1007/s00041-023-09994-2 .
