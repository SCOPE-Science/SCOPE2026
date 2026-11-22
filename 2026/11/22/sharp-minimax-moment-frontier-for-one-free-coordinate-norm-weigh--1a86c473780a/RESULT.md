# Sharp minimax moment frontier for one-free-coordinate norm-weighted Kaczmarz

## Finding

Let \(m\ge 2\), \(\beta>0\), and \(q>0\). For scalar projected rows with magnitudes \(0<s_i\le1\), \(\max_i s_i=1\), and bounded observed right-hand sides \(|d_i|\le1\), sample row \(i\) independently with probability
\[
\pi_i=\frac{s_i^\beta}{\sum_{j=1}^m s_j^\beta},
\]
and take its exact one-row Kaczmarz projection. For any positive iteration number \(k\), the sharp worst-case \(q\)-th absolute iterate moment is
\[
\mathcal R_{m,\beta,q}:=\sup_{s,d}\mathbb E|u_k|^q=
\begin{cases}
+\infty,&0<\beta<q,\\
m,&\beta=q,\\
\dfrac{1+(m-1)t_*^{\beta-q}}{1+(m-1)t_*^\beta},&\beta>q,
\end{cases}
\]
where in the final case \(t_*\in(0,1)\) is the unique root of
\[
\beta t_*^q+q(m-1)t_*^\beta=\beta-q.
\]
For \(\beta>q\), every optimizer has, up to row permutation, projected row magnitudes \((1,t_*,\ldots,t_*)\) and \(|d_i|=1\) for every \(i\). At \(\beta=q\), the value \(m\) is an unattained supremum approached as all but one row magnitude tend to zero. For \(\beta<q\), each individual fixed system has finite moments, but the supremum over the specified class is infinite.

Consequently, **uniform \(q\)-moment robustness in this precisely normalized family holds if and only if \(\beta\ge q\)**. In particular, classical projected squared-norm sampling \(\beta=2\) has a bounded second moment but no uniformly bounded moment of any order \(q>2\).

This obstruction is compatible with uniformly well-conditioned original matrices and only one corrupted measurement: for every \(0<\varepsilon\le1\), use
\[
A_\varepsilon=\begin{pmatrix}1&0\\0&1\\1&\varepsilon\end{pmatrix},\quad
b=\begin{pmatrix}0\\1\\1\end{pmatrix},\quad
I_0=\{1\},\quad x_{\mathrm{true}}=\begin{pmatrix}0\\1\end{pmatrix}.
\]
The third observation alone is corrupted by \(1-\varepsilon\). Under the stated projected sampling, for every \(k\ge1\),
\[
\mathbb E\|x_k-x_{\mathrm{true}}\|_2^q
=\frac{\varepsilon^\beta}{1+\varepsilon^\beta}(\varepsilon^{-1}-1)^q
\sim\varepsilon^{\beta-q},\qquad\varepsilon\downarrow0,
\]
and for every \(R>0\) the exact worst-family high-error tail is
\[
\sup_{0<\varepsilon\le1}\Pr\{\|x_k-x_{\mathrm{true}}\|_2\ge R\}
=\frac{1}{1+(R+1)^\beta}.
\]
The original matrix has singular values \(1\) and \(\sqrt{2+\varepsilon^2}\), hence condition number at most \(\sqrt3\).

## Assumptions and scope

There is one *trusted exact* linear subsystem whose nullspace is one-dimensional. Fix a unit nullspace direction \(v\); choose a feasible origin for which the clean solution is \(u=0\) in the affine coordinate \(x=x_{\mathrm{true}}+uv\). Let the \(m\) remaining projected row coefficients be nonzero real numbers. Reorient each equation, if needed, to write its projected coefficient as \(s_i>0\), and let \(d_i\) be its corresponding bounded observation error. Normalize the maximum projected coefficient magnitude to one and the maximum admissible error magnitude to one. Assume \(m\) is fixed, row draws are independent with replacement, probabilities are proportional to \(s_i^\beta\), and an exact projection is performed even when its residual happens to vanish. This is the **unmodified independent-row sampling variant**; it is not a residual-rejection, quantile-filtered, or variance-reduced algorithm.

The exact projection is
\[
u_{k+1}=u_k-\frac{s_i u_k-d_i}{s_i^2}s_i=\frac{d_i}{s_i}.
\]
The first update therefore erases the initial free coordinate; all later iterates have the same law. The theorem concerns the supremum over all allowed projected coefficients and noise vectors, **not** the distribution for a fixed matrix with finite row count. The only randomness is in row selection; observation errors are fixed deterministic numbers.

## Proof

**Exact distribution and reduction.** If \(I_k\) is the index drawn on the \(k\)-th update, the displayed projection gives \(u_k=d_{I_k}/s_{I_k}\) for every \(k\ge1\). Since draws are independent,
\[
\mathbb E|u_k|^q=
\frac{\sum_i s_i^{\beta-q}|d_i|^q}{\sum_i s_i^\beta}.
\tag{1}
\]
For fixed magnitudes \(s_i\), the maximum is attained precisely when every \(|d_i|=1\). Set \(s_1=1\) after permuting rows.

**Subcritical and critical cases.** For \(\beta<q\), take \(s_2=\varepsilon\downarrow0\), all other magnitudes one, and every \(|d_i|=1\). The term \(\varepsilon^{\beta-q}\) diverges while the denominator remains bounded. At \(\beta=q\), each numerator term in (1) is at most one, so the ratio is at most \(m\) because \(\sum_i s_i^q\ge1\). Set all \(m-1\) remaining magnitudes to \(\varepsilon\) and all \(|d_i|=1\), giving \(m/(1+(m-1)\varepsilon^q)\to m\). Strict positivity of the other projected magnitudes prevents attainment.

**Supercritical global optimum and equality.** Suppose \(\beta>q\), and put \(\alpha=1-q/\beta\in(0,1)\) and \(z_i=s_i^\beta\) for \(i\ge2\). By strict concavity of \(z^\alpha\), with \(h=m-1\) and \(S=\sum_{i=2}^m z_i\),
\[
\sum_{i=2}^m z_i^\alpha\le h^{1-\alpha}S^\alpha,
\]
with equality exactly when these \(h\) numbers coincide. Thus the global optimization reduces to equal weaker magnitudes \(s_2=\cdots=s_m=t\in[0,1]\), and the one-variable function
\[
F(t)=\frac{1+h t^{\beta-q}}{1+h t^\beta}.
\]
For \(0<t<1\), direct differentiation yields
\[
\operatorname{sgn}F'(t)=\operatorname{sgn}\big((\beta-q)-\beta t^q-qh t^\beta\big).
\]
The expression on the right is strictly decreasing from \(\beta-q>0\) to \(-qm<0\). Hence it has exactly one root \(t_*\in(0,1)\); \(F\) increases before and decreases after it. This proves the claimed global maximum. Strict concavity plus the unique interior maximizer proves all equality cases: the strong row is unique, all remaining magnitudes equal \(t_*\), and all observation-error magnitudes equal one.

**Well-conditioned single-corruption realization and tail.** For the displayed \(A_\varepsilon\), the first two rows form the identity and the third equals \((1,\varepsilon)\). Therefore
\[
A_\varepsilon^\mathsf TA_\varepsilon=I+(1,\varepsilon)^\mathsf T(1,\varepsilon),
\]
whose eigenvalues are \(1\) and \(2+\varepsilon^2\). With the first row enforced, the remaining projected coefficients are \(1\) and \(\varepsilon\). The second equation sets the free coordinate to one; the third sets it to \(\varepsilon^{-1}\), respectively with probabilities \((1+\varepsilon^\beta)^{-1}\) and \(\varepsilon^\beta/(1+\varepsilon^\beta)\). Relative to the clean solution \((0,1)\), the errors are zero and \(\varepsilon^{-1}-1\), giving the claimed moment formula.

For fixed \(R>0\), the error reaches at least \(R\) precisely when the third row is drawn and \(\varepsilon\le1/(R+1)\). Its sampling probability is strictly increasing in \(\varepsilon\), so the supremum is attained at \(\varepsilon=1/(R+1)\), with probability \(1/(1+(R+1)^\beta)\). The true solution has unit norm and the corruption magnitude is \(1-\varepsilon\le1\). This proves all assertions.

## Verification

`check.py` is a standalone Python 3 script using only the standard library. Run `python check.py` in a directory containing this manuscript and the checker. It evaluates exact-rational moment identities, the exact small-matrix normal equations, the noise-tail formula and critical-profile approach. Additional finite numerical checks compare the analytic unique optimum with dense and nonuniform candidate sets. These are **finite consistency tests**, not a proof of the all-parameter theorem; the latter is given above by the moment identity, strict Jensen inequality and monotone derivative.

## Relationship to prior work

Sun, Qi, Han and Xie (2026) develop subspace-constrained randomized iterative methods and an exact-subsystem projector, studying convergence in expectation primarily for the consistent linear-system setting. Lok and Rebrova (2023) introduce subspace-constrained randomized Kaczmarz, including projected squared-norm row selection, and explicitly analyze its mean-square noise horizon for inconsistent observations. Those algorithms and second-moment analyses are **not** new here. Needell (2009/2010) develops classical noisy Kaczmarz expectation/error-horizon bounds. The present claim concerns a different invariant: the **complete all-real-order minimax absolute-moment profile, strict equality configurations, endpoint robustness threshold, and a sharp single-corruption error tail on uniformly conditioned full systems**. It treats an independent-row norm-power extension of the baseline projected sampling, not residual-screened variants.

The public record “Sharp moment thresholds for Gaussian-noisy, norm-weighted Kaczmarz projections” concerns freshly Gaussian-resampled *coefficient rows* and an ensemble moment criterion. Here the coefficient matrix is fixed, only the right-hand-side observation is corrupted, and the supremum is taken over deterministic projected row geometry. Neither its dimension-dependent random-coefficient threshold nor the cited mean-square horizons imply the stated sharp finite-row minimax function.

## Limitations

The scalar reduction is essential: the exact reset identity generally fails with two or more free coordinates. This finding establishes no convergence claim for inconsistent higher-dimensional systems, no optimal filtering policy, and no guarantee for adaptive residual-based row exclusion. The worst-case risk is over a class of finite systems; no single fixed finite system has infinite moments. Exact row projections and fixed independent sampling are assumed. The public literature may contain an unindexed equivalent all-order minimax characterization; no independent audit has been performed.

## References

1. Y. Sun, H.-D. Qi, D. Han and J. Xie, *On subspace-constrained preconditioning for randomized iterative methods*, arXiv:2605.29304, v1, 2026-05-28. https://arxiv.org/html/2605.29304
2. J. Lok and E. Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*, arXiv:2309.04889, v1, 2023-09-09, in particular §3.2. https://arxiv.org/abs/2309.04889
3. D. Needell, *Randomized Kaczmarz solver for noisy linear systems*, arXiv:0902.0958, first submitted 2009-02-05; BIT Numer. Math. 50 (2010), 395–403. https://arxiv.org/abs/0902.0958
4. Public mathematical research record, *Sharp moment thresholds for Gaussian-noisy, norm-weighted Kaczmarz projections*, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-moment-thresholds-for-gaussian-noisy-norm-weighted-kaczmar--81db12815a13
