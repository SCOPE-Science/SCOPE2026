# Exact finite-null variance and an explicit non-Gaussian boundary law for a cyclic rank-sum independence statistic

## Finding

The cyclic split-permute rank-sum statistic of Cai, Lei and Roeder [1] has a non-Gaussian, order-\(n^{-1}\) null fluctuation at a natural two-coordinate score excluded by its published first-order Gaussian theorem. More precisely, let \((X_i,Y_i)\), \(1\le i\le n\), be independent pairs with independent uniform coordinates on \((0,1)\). Set \(A_i=\mathbf1\{X_i>1/2\}\), use the deterministic score \(s(x,y)=(\mathbf1\{x>1/2\}+y)/2\), and cyclically identify \(Y_{n+1}=Y_1\). For every integer \(n\ge3\), define the published-form, strict-comparison statistic

\[
 R_n=\frac1{n^2}\sum_{i,j=1}^n\mathbf1\{s(X_i,Y_i)<s(X_j,Y_{j+1})\}.
\]

Then the *exact* null mean and variance are

\[
 \mathbb ER_n=\frac12-\frac1{4n},\qquad
 \operatorname{Var}(R_n)=\frac{3n-2}{48n^3}.
\]

Moreover, with \(L_n=n(R_n-1/2)\), one has \(L_n\Rightarrow L\), whose characteristic function (with its value at zero understood by continuity) is

\[
 \boxed{\quad\mathbb E e^{itL}=e^{-it/4}\left[H(t/4)\bigl(2\cosh(t/4)-H(t/4)\bigr)\right]^{-1/2},\quad
 H(x)=\frac{\sinh x}{x},\ H(0)=1.\quad}
\]

In particular, \(\mathbb EL=-1/4\), \(\operatorname{Var}(L)=1/16\), and its excess kurtosis is *exactly* \(10/3\). The limit is symmetric about \(-1/4\), nondegenerate, and non-Gaussian. The result applies to a fixed score under an independent null, not to arbitrary data-trained classifiers.

## Assumptions and scope

The statistical observation model is independent and identically distributed \((X_i,Y_i)\sim\operatorname{Unif}(0,1)\otimes\operatorname{Unif}(0,1)\). The displayed score is fixed independently of these observations. Its marginal distribution is uniform on \((0,1)\). Although the scores are distinct within each list almost surely, cross-list ties occur: almost surely equality holds precisely when \(i=j+1\) cyclically and \(A_i=A_j\). These ties arise from reuse of \(Y_i\) and contribute zero under the strict inequality. Both lists contain \(n\) observations, and all \(n^2\) cross-comparisons are included, including \(i=j\). This is the strict comparison in formula (2.2) of [1] for the specified score, not a rank statistic with midrank or random tie-breaking. No claim is made that a trained algorithm will output that score.

Although \(s\) uses both independent coordinates, its probability integral transform is exactly \(F_s(s(X,Y))=s(X,Y)=A/2+Y/2\), additive across coordinates. Thus the non-additivity hypothesis in Theorem 3.1 and Remark 3 of [1] fails; the published Gaussian theorem does not apply. The finding identifies the remaining second-order law without contradicting that theorem.

## Proof

**1. Exact signed-quadratic identity.** Let \(B_i=1-2A_i\in\{-1,1\}\); then the \(B_i\) are independent symmetric signs and independent of all the \(Y_i\). Write \(H_{ij}=\mathbf1\{Y_i<Y_j\}\), \(i,j\in\{1,\dots,n\}\), with cyclic subscripts. Since comparisons between the lower and upper score halves have deterministic outcomes, comparison with the unpermuted score list gives \(n(n-1)/2\) strict wins. The change produced by cyclically shifting the \(Y\)-coordinates is

\[
D_n=\frac12\sum_{i,j=1}^n B_i(B_{j-1}-B_j)H_{ij},
\qquad R_n=\frac{n-1}{2n}+\frac{D_n}{n^2},
\]

where \(B_0=B_n\). This can also be verified directly by comparing, within each of the two \(A\)-classes, the rank of every incoming \(Y_{j+1}\) with the outgoing \(Y_j\). Now define the number of cyclic ascents

\[
T_n=\sum_{i=1}^n\mathbf1\{Y_i<Y_{i+1}\}
\]

and for \(i<k\)

\[
C_{ik}=\mathbf1\{Y_i<Y_{k+1}\}+\mathbf1\{Y_k<Y_{i+1}\}-1.
\]

Since \(\sum_{i\ne j}B_iB_jH_{ij}=\sum_{i<j}B_iB_j\), regrouping signed terms yields the exact identity

\[
\boxed{\quad R_n=\frac{n-1}{2n}+\frac{1}{2n^2}\left(T_n+\sum_{i<k}B_iB_kC_{ik}\right).\quad} \tag{1}
\]

**2. Finite mean and variance.** Conditional on all \(Y_i\), distinct products \(B_iB_k\), \(i<k\), are orthogonal centered Rademacher chaoses. Thus the conditional mean of the parenthesis in (1) is \(T_n\), and its conditional variance is \(\sum_{i<k}C_{ik}^2\). Every unordered pair satisfies \(\mathbb EC_{ik}^2=1/2\): for non-neighboring indices the two indicators are independent fair Bernoulli variables, and for cyclic neighbors one indicator vanishes identically and the other is a fair Bernoulli variable. Cyclic ascents of \(n\ge3\) independent continuous observations have \(\mathbb ET_n=n/2\) and \(\operatorname{Var}(T_n)=n/12\). The latter follows by adding indicator variances \(n/4\) and the \(n\) adjacent covariances \(-1/12\), with nonadjacent comparisons independent. The law of total variance in (1) gives

\[
\mathbb E R_n=\frac{n-1}{2n}+\frac{n/2}{2n^2},\qquad
\operatorname{Var}(R_n)=\frac1{4n^4}\left(\frac n{12}+\frac12\binom n2\right)=\frac{3n-2}{48n^3}.
\]

**3. A second Gaussian chaos rather than a first-order central limit.** Put \(Z_i=(Y_i,Y_{i+1})\in[0,1]^2\) and introduce the symmetric, bounded Hilbert–Schmidt kernel

\[
\kappa((u,v),(u',v'))=\mathbf1\{u<v'\}+\mathbf1\{u'<v\}-1.
\]

Then \(C_{ik}=\kappa(Z_i,Z_k)\) exactly. Let \(K\) be the compact self-adjoint integral operator defined by this kernel under uniform area measure, with nonzero eigenvalues \((\lambda_r)\), repeated by multiplicity and signed. Its squared Hilbert–Schmidt norm is \(\sum_r\lambda_r^2=\int\kappa^2=1/2\).

For every finite eigenfunction truncation, the standardized sums \(n^{-1/2}\sum_i B_i e_r(Z_i)\) satisfy a joint centered normal CLT with *identity* covariance. Indeed, away from the cyclic wrap, the process \((B_i,Z_i)\) is one-dependent; for each nonzero eigenvalue take the bounded representative \(e_r=Ke_r/\lambda_r\). The single wrap term is negligible, and off-diagonal covariances vanish because \(\mathbb E(B_iB_j)=0\) whenever \(i\ne j\). The diagonal eigenfunction-square means obey a one-dependent law of large numbers. Hence the finite truncation of the quadratic term in (1), divided by \(n\), converges to \(\tfrac12\sum_r\lambda_r(G_r^2-1)\) over the retained modes, where the \(G_r\) are independent standard normals. By orthogonality of the unordered sign pairs, the squared \(L^2\) error is bounded by the squared Hilbert–Schmidt tail for the nonadjacent pairs, whose marks are independent. The \(O(n)\) adjacent pairs contribute \(O(1/n)\) for each fixed truncation, by boundedness. Taking \(n\to\infty\) first and then enlarging the truncation proves

\[
\boxed{\quad L_n\Rightarrow-\frac14+\frac14\sum_r\lambda_r(G_r^2-1).\quad} \tag{2}
\]

The series converges in \(L^2\); the shift \(-1/4\) comes from \(-1/2+T_n/(2n)\to-1/4\).

**4. Complete spectrum.** Let \(Ag(u)=\int_u^1g(v)\,dv-\tfrac12\int_0^1g(v)\,dv\), and embed univariate functions into the square through \(Ug(u,v)=g(u)\) and \(Vg(u,v)=g(v)\). The kernel operator is \(K=UAV^*-VAU^*\). Exchanging \(u,v\) anticommutes with \(K\), so every nonzero eigenvalue occurs in a positive/negative pair. The range of \(K\) consists of sums of a function of \(u\) and a function of \(v\); consequently its positive squared spectrum can be determined from the antisymmetric subspace \(g(u)-g(v)\), with \(\int_0^1g=0\).

On that subspace \(K\) sends \(g(u)-g(v)\) to \(-(Ag)(u)-(Ag)(v)\). Applying \(K\) again gives the antisymmetric representative \(-P_0A(Ag+PAg)\), where \(P\) projects onto constants and \(P_0=I-P\). For an eigenvalue square \(\omega^{-2}>0\), differentiating once yields \(\omega^{-2}g'=Ag+PAg\). Since \(Ag(0)=Ag(1)=0\), the value of the right side at zero is half its integral. Differentiating again gives the boundary problem

\[
g''+\omega^2g=0,\qquad\int_0^1g=0,\qquad g(1)-g(0)=2g'(0).
\]

Conversely, for a solution of this problem with \(\omega\ne0\), \(\omega^{-2}g'-Ag\) is constant by the differential equation. The boundary condition makes that constant equal to \(PAg\); integrating and using zero mean recovers \(\omega^{-2}g=-P_0A(Ag+PAg)\). In the basis \(\cos(\omega(u-1/2)),\sin(\omega(u-1/2))\), the zero-mean condition sets the cosine coefficient to zero unless \(\sin(\omega/2)=0\), and the remaining boundary condition imposes \(\sin(\omega/2)=\omega\cos(\omega/2)\) on a nonzero sine coefficient. Thus there is one frequency \(2\pi m\) for each \(m=1,2,\ldots\), and one positive root \(\rho_m\in(2m\pi,(2m+1)\pi)\) of \(\tan(\rho_m/2)=\rho_m\) for each \(m=0,1,\ldots\). The latter count follows from strict convexity of the tangent on each of those branches, with slope \(1/2\) at the left edge, and negativity on the intervening branches. Each antisymmetric eigenfunction of \(K^2\) with positive eigenvalue pairs with a symmetric one via \(K\), giving eigenvalues \(\pm1/\omega\). These account for all nonzero eigenvalues of \(K\).

Thus (2) is equivalently

\[
L=-\frac14+\frac14\sum_{\omega}\frac{G_{\omega,+}^2-G_{\omega,-}^2}{\omega},
\]

with independent standard normals. For each frequency the characteristic-function factor is \((1+t^2/(4\omega^2))^{-1/2}\). Euler's \(\sinh\) product for \(\omega=2\pi m\), together with the normalized entire function

\[
\frac{\sin(z/2)-z\cos(z/2)}{-z/2}
=\prod_{m\ge0}\left(1-\frac{z^2}{\rho_m^2}\right),
\]

at \(z=it/2\) produces the characteristic function stated in the finding. To see that the product includes all zeros, the sine solution of the boundary problem for a nonzero complex zero would give the eigenvalue \(z^{-2}\) of the positive self-adjoint operator \(K^2\); thus \(z\) must be real. The positive zeros are simple (the tangent-minus-line function crosses with strictly positive slope). The normalized entire function is even and of order one, so pairing the sign-opposite zeros in its canonical product leaves only a constant factor, fixed at one by the value at zero. Every characteristic-function factor is positive for real \(t\).

**5. Non-Gaussianity and exact kurtosis.** The Taylor expansion of the normalized entire function is \(1-(5/24)z^2+(3/640)z^4+O(z^6)\); comparing elementary symmetric sums gives \(\sum_m\rho_m^{-2}=5/24\) and \(\sum_m\rho_m^{-4}=49/1440\). Adding the frequencies \(2\pi m\) yields

\[
\sum_{\omega}\omega^{-2}=\frac14,\qquad\sum_{\omega}\omega^{-4}=\frac5{144}.
\]

The paired representation therefore gives \(\operatorname{Var}(L)=\tfrac14\sum\omega^{-2}=1/16\). A difference of two independent \(\chi_1^2\) variables has fourth cumulant \(96\), hence \(\operatorname{cum}_4(L)=96\cdot4^{-4}\sum\omega^{-4}=5/384\). Dividing by the square of the variance yields excess kurtosis \(\boxed{10/3}\), strictly positive and therefore excluding any Gaussian limiting law.

## Verification

The independent standard-library script `check.py` exhaustively enumerates all \(2^n n!\) null configurations for each \(n=3,4,5,6\), checking both algebraic identities against the literal double comparison, and verifying the exact mean and variance as rational numbers. It also compares the spectral trace and product to independently root-found frequencies and performs seeded simulation spot checks. The script reports 100,725 passed assertions. These computations support, but do not replace, the analytic proof of the infinite-dimensional limit and product formula.

## Relationship to prior work

Cai, Lei and Roeder [1,2] define exactly this cyclic comparison statistic and establish a Gaussian limit under strict non-additivity of the score's probability integral transform; their Remark 3 explicitly excludes the class examined here. The present result is a boundary analysis with an explicit two-coordinate score, exact finite-size moments, the second-order normalization, a complete spectrum, and a closed characteristic function. It does not contradict the source Gaussian theorem or establish any behavior for learned classifiers.

General degenerate U-statistic chaos expansions and weak-dependence spectral methods predate this computation [3–5]. They provide general machinery for understanding quadratic-normal limits, but the spectral boundary problem, finite-sample exact variance, and hyperbolic characteristic function for this specific cyclic statistic require the calculations above. This relationship is not a claim that no other source could have established an equivalent result.

## Limitations

The score is deliberately chosen from the additive exception and is fixed, not produced by a specified training algorithm. Conclusions concern its strict held-out null law; no trained-classifier power, consistent testing under alternatives, performance of the estimated variance denominator in [1], or finite-sample calibration guarantee is claimed. Relevant broader literature may contain unrecognized equivalent specializations.

## References

1. Z. Cai, J. Lei, K. Roeder, *Asymptotic Distribution-Free Independence Test for High Dimension Data*, arXiv:2110.07652, first posted 2021-10-14. https://arxiv.org/abs/2110.07652
2. Z. Cai, J. Lei, K. Roeder, *Asymptotic Distribution-Free Independence Test for High-Dimension Data*, Journal of the American Statistical Association 119 (2024), 1794–1804, DOI:10.1080/01621459.2023.2218030. https://doi.org/10.1080/01621459.2023.2218030
3. I. S. Borisov, N. Volodko, *Orthogonal series and limit theorems for canonical U- and V-statistics of stationary connected observations*, arXiv:0906.5465 (2009). https://arxiv.org/abs/0906.5465
4. E. Carlstein, *Degenerate U-Statistics Based on Non-Independent Observations*, Calcutta Statistical Association Bulletin 37 (1988), 55–66. https://doi.org/10.1177/0008068319880106
5. J. Shao, *Asymptotic distributions of degenerated U-statistics*, Statistical Theory and Related Fields 9 (2025), 434–443. https://doi.org/10.1080/24754269.2025.2579414
