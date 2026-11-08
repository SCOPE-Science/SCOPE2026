# Sharp rank-agnostic covariance loss from leading-singular-mode Landweber truncation

## Finding

**Theorem.** For any integer \(K\ge 1\), define the continuous scalar response on \([0,1]\) by
\[
 f_K(0)=0,\qquad f_K(t)=\frac{[1-(1-t)^K]^2}{t}\quad(0<t\le1).
\]
Put \(M_1=1\). For \(K\ge2\), let \(u_K\in(0,1)\) be the unique solution of
\[
 \sum_{j=0}^{K-1}u_K^j=2K u_K^{K-1},
 \qquad t_K=1-u_K,\qquad M_K=f_K(t_K).
\]
For any real data operator \(A\in\mathbb R^{m\times n}\), white observation noise with covariance \(\sigma^2 I_m\), relaxation \(\omega>0\) satisfying \(0<\omega\|A\|_2^2\le1\), and any retained rank \(1\le r<n\), run \(K\) steps of Landweber iteration from zero. Let \(\Gamma_K\) be the exact propagated-noise covariance, and let \(\Gamma_{K,r}^{B}\) retain the contributions from the \(r\) leading eigenvectors of \(B=A^{\mathsf T}A\), with their exact Landweber covariance eigenvalues. Then
\[
 \boxed{\ \|\Gamma_K-\Gamma_{K,r}^{B}\|_2
 \le M_K\inf_{\operatorname{rank}(H)\le r}\|\Gamma_K-H\|_2.\ }
\]
The constant \(M_K\) is **best possible simultaneously for every rank \(r\)**: a diagonal operator of dimension \(r+1\) realizes equality. Specifically \(M_2=32/27\), and
\[
 M_K\sim c_*K,\quad Kt_K\longrightarrow\tau_*,\quad
 e^{\tau_*}=1+2\tau_*,\quad
 c_*=\frac{(1-e^{-\tau_*})^2}{\tau_*}
 =\frac{4\tau_*}{(1+2\tau_*)^2}\approx0.407264377589.
\]
Here \(\tau_*>0\) denotes the unique positive solution. Hence the loss from selecting a covariance compression subspace by the **largest normal-operator eigenvalues**, rather than by the largest propagated-covariance eigenvalues, can grow linearly in the number of Landweber iterations even though the same rank is used.

## Assumptions and scope

The Landweber scheme is
\[
 x^{(0)}=0,\qquad x^{(k+1)}=x^{(k)}+\omega A^{\mathsf T}(y-Ax^{(k)}),\qquad
 y=Ax^\dagger+\varepsilon,
\]
where \(\mathbb E\varepsilon=0\) and \(\operatorname{Cov}(\varepsilon)=\sigma^2I_m\), with \(\sigma>0\). Gaussianity is unnecessary for the covariance identity, although Gaussian observation noise motivates the application. The noise component is the difference between the iterate with \(\varepsilon\) and the iterate with the noise set to zero. Fix a sorted eigendecomposition \(B=V\operatorname{diag}(\lambda_1,\dots,\lambda_n)V^{\mathsf T}\), with \(\lambda_1\ge\dots\ge\lambda_n\ge0\). For ties at the retention boundary, any choice of eigenvectors inside the tied eigenspace is permitted. Write \(t_i=\omega\lambda_i\in[0,1]\). The exact covariance and the normal-operator-selected rank-\(r\) covariance truncation are
\[
 \Gamma_K=\sigma^2\omega V\operatorname{diag}(f_K(t_i))V^{\mathsf T},\qquad
 \Gamma_{K,r}^{B}=\sigma^2\omega\sum_{i=1}^{r}f_K(t_i)v_iv_i^{\mathsf T}.
\]
No claim is made about a randomized approximation's eigenvector accuracy, regularization bias, residual correction, confidence coverage, or timestep choices beyond \(\omega\|A\|_2^2\le1\). The inequality includes rank-deficient operators and zero covariance. If the optimal rank-\(r\) error is zero, so is the normal-operator-selected error.

## Proof

**Step 1 (noise propagation).** The noise-to-iterate map after \(K\) steps is
\[
 L_K=\omega\sum_{j=0}^{K-1}(I-\omega B)^j A^{\mathsf T}.
\]
Thus \(\Gamma_K=\sigma^2L_KL_K^{\mathsf T}\). On a nonzero eigenmode \(\lambda_i\) of \(B\), the squared gain is
\[
 \omega^2\lambda_i\left(\sum_{j=0}^{K-1}(1-\omega\lambda_i)^j\right)^2
 =\omega\frac{[1-(1-\omega\lambda_i)^K]^2}{\omega\lambda_i}
 =\omega f_K(t_i).
\]
At a zero eigenvalue the gain vanishes, consistent with \(f_K(0)=0\). This proves the displayed covariance decomposition.

**Step 2 (exact scalar envelope).** For \(K=1\), \(f_1(t)=t\), increasing on \([0,1]\), and \(M_1=1\). For any \(K\ge2\), the derivative for \(0<t<1\), writing \(u=1-t\), has the sign of
\[
 2K(1-u)u^{K-1}-(1-u^K)
 =(1-u)\left(2Ku^{K-1}-\sum_{j=0}^{K-1}u^j\right).
\]
The last factor, after division by \(u^{K-1}\), has the sign of
\[
 2K-\sum_{j=0}^{K-1}u^{-j}.
\]
As \(u\) increases strictly from zero to one, the sum strictly decreases from infinity to \(K\). Consequently it crosses \(2K\) exactly once. Therefore \(f_K\) strictly increases on \((0,t_K)\), strictly decreases on \((t_K,1)\), and \(t_K\) is its unique maximizer. Since \(f_K(1)=1\), \(M_K>1\). The unimodality also gives the key **ordered-filter comparison**: for every \(0\le t\le s\le1\),
\[
 f_K(s)\ge\min\{f_K(t),1\},\qquad
 f_K(t)\le M_K f_K(s).
\]
Indeed, if \(f_K(t)\le1\), the first inequality implies \(f_K(s)\ge f_K(t)\); otherwise it implies \(f_K(s)\ge1\ge f_K(t)/M_K\). The same comparison for \(K=1\) follows by monotonicity. This argument covers endpoints and zero eigenvalues.

**Step 3 (dimension- and rank-independent bound).** Let \(E_B=\|\Gamma_K-\Gamma_{K,r}^{B}\|_2\) and \(E_*=\inf_{\operatorname{rank}(H)\le r}\|\Gamma_K-H\|_2\). Since the covariance is positive semidefinite, its optimal spectral-norm rank-\(r\) error is the \((r+1)\)-st largest eigenvalue, \(E_*=\sigma^2\omega\,\operatorname{ord}_{r+1}^{\downarrow}\{f_K(t_1),\ldots,f_K(t_n)\}\), by the usual rank-approximation singular-value principle. Meanwhile
\[
 E_B=\sigma^2\omega\max_{j>r}f_K(t_j).
\]
Choose an omitted index \(j_*>r\) attaining the maximum. Since \(t_i\ge t_{j_*}\) for all \(i\le r\), Step 2 yields \(f_K(t_i)\ge f_K(t_{j_*})/M_K\) for these \(r\) retained indices. The omitted index \(j_*\) itself supplies one more eigenvalue of at least this size. Hence the \((r+1)\)-st largest covariance eigenvalue is at least \(E_B/M_K\), giving \(E_B\le M_KE_*\). No positivity of the normal operator's smallest eigenvalues is required.

**Step 4 (sharpness for every rank).** Fix \(K\ge2\) and \(r\ge1\). Take \(n=m=r+1\), \(\omega=1\), and
\[
 A=\operatorname{diag}(\underbrace{1,\ldots,1}_{r\text{ times}},\sqrt{t_K}).
\]
The \(r\) leading eigenvalues of \(B\) equal one and its last eigenvalue is \(t_K<1\). Hence \(\Gamma_K=\sigma^2\operatorname{diag}(1,\ldots,1,M_K)\). The normal-operator-selected rank-\(r\) covariance misses the last coordinate and has spectral error \(\sigma^2M_K\), whereas the best rank-\(r\) covariance approximation has spectral error \(\sigma^2\). Equality follows. For \(K=1\), every normal-operator leading-eigenmode truncation is optimal, and \(M_1=1\) is sharp. At \(K=2\), \(f_2(t)=t(2-t)^2\) attains its maximum at \(t=2/3\), with value \(32/27\).

**Step 5 (sharp large-iteration law).** Define \(g(\tau)=(1-e^{-\tau})^2/\tau\) for \(\tau>0\). For every fixed \(\tau>0\),
\[
 \frac{f_K(\tau/K)}{K}\longrightarrow g(\tau).
\]
Since \(1-(1-t)^K\le\min\{Kt,1\}\) for \(0\le t\le1\), setting \(\tau=Kt\) gives the uniform bound
\[
 \frac{f_K(t)}{K}\le\min\{\tau,\tau^{-1}\}.
\]
The scaled maximizers \(Kt_K\) are therefore eventually confined to a compact subset of \((0,\infty)\): they cannot approach either zero or infinity while their value exceeds the positive reference \(g(1)/2\). Uniform convergence on such compacts identifies every limit point as a maximizer of \(g\). Differentiation shows that a positive critical point of \(g\) satisfies \(e^\tau=1+2\tau\); by strict convexity of the exponential there is exactly one positive solution \(\tau_*\), which is the unique maximum (the endpoints of \(g\) both vanish). Thus \(Kt_K\to\tau_*\) and \(M_K/K\to g(\tau_*)\). Using \(e^{\tau_*}=1+2\tau_*\) gives the alternate closed form for \(c_*\).

## Verification

The standalone `verify.py` recomputes the scalar critical point, checks the exact \(K=2\) fraction, tests the ordered-spectrum inequality for random matrices and all tested truncation ranks, reconstructs propagated covariance directly by finite Landweber sums, and checks the explicit sharp diagonal examples and asymptotic constants. In the recorded run, **24,486 supplementary deterministic assertions passed**, including direct covariance recurrences and sharp examples at several ranks. This finite testing is not an exhaustive proof; Steps 1–5 supply the all-dimension, all-rank proof. Run from this package with `python verify.py` (requires Python 3 and NumPy).

## Relationship to prior work

Abhishek and Holman (2026), Section 3.6 and equations (3.26)–(3.27), develop the approximation of Landweber propagated covariance using a low-rank approximation of the normal operator. Their Section 3.5 already gives the full covariance spectral formula, and their Section 3.6 explicitly recognizes elevated uncertainty from smaller singular values. Those observations, the Landweber filter, the low-rank approximation principle, and the use of residual stochastic correction are **prior work**. The theorem here is the exact, sharp, uniform operator-norm comparison between a leading-normal-mode covariance truncation and the best covariance rank truncation, valid at all ranks and with an optimal factor that grows linearly in the iteration count. It does not analyze the accuracy of the authors' full residual-corrected stochastic procedure.

Ito and Jin (2019), *Regularized Linear Inversion with Randomized Singular Value Decomposition*, study randomized SVD for regularized solution approximation and relative solution errors; their work does not furnish the same propagated-covariance rank-selection comparison in the inspected full text. Gazzola and Sabaté Landman (2020) review spectral-filtering and early-stopped inverse solvers; their account supplies background but not the sharp comparison law identified here. The rank-\(r\) spectral-norm best-approximation principle is classical, not new.

## Limitations

The theorem concerns deterministic exact leading-eigenspace selection of \(A^{\mathsf T}A\) with exact covariance weights, white noise, fixed integer iterations, and nonovershooting relaxation \(0<\omega\|A\|_2^2\le1\). It does **not** prove instability of randomized low-rank eigenvector estimates, failure of confidence-interval coverage, loss of statistical optimality, or an error bound for the full residual-corrected estimator. Bias and variance must be treated separately. Equivalent unindexed formulations in broader spectral-approximation theory may exist; the available literature review does not establish global priority.

## References

1. A. Abhishek and S. Holman, *Uncertainty Quantification for Landweber Iteration with Randomized Normal-Operator Approximation*, arXiv:2610.00882v1, publicly posted 1 October 2026, Sections 3.3, 3.6, Appendix 5.1. https://arxiv.org/html/2610.00882v1
2. K. Ito and B. Jin, *Regularized Linear Inversion with Randomized Singular Value Decomposition*, arXiv:1909.01947v1, publicly posted 4 September 2019. https://arxiv.org/abs/1909.01947
3. S. Gazzola and M. Sabaté Landman, *Krylov Methods for Inverse Problems: Surveying Classical, and Introducing New, Algorithmic Approaches*, GAMM-Mitteilungen 43 (2020), e202000017, first published 28 September 2020, DOI:10.1002/gamm.202000017. https://doi.org/10.1002/gamm.202000017
4. J. M. Bardsley, *Computational Uncertainty Quantification for Inverse Problems*, SIAM (2018), Chapter 2: *Regularization by Spectral Filtering*, DOI:10.1137/1.9781611975383.ch2. Full chapter was not accessible during this comparison; its topic remains a historical-priority risk.
