# A sharp angular-information threshold for planar Gaussian Nyström covariance design

## Finding

Let \(A,K\in\mathbb R^{2\times2}\) be real symmetric positive-definite matrices. Draw \(g\sim\mathcal N(0,K)\) and form the one-column Nyström approximation
\[
\widehat A=A g\,(g^{\mathsf T}Ag)^{-1}g^{\mathsf T}A.
\]
The expected nuclear-norm error (equal to the trace of the positive semidefinite residual) is **exactly**
\[
\boxed{\mathbb E\,\operatorname{tr}(A-\widehat A)
=\frac{\sqrt{\det A\det K}\,\operatorname{tr}A+
(\det A)\operatorname{tr}K}{\operatorname{tr}(AK)+2\sqrt{\det A\det K}}.}
\tag{1}
\]
Thus covariance orientation enters through one mixed trace, rather than through the eigenvalues alone.

More precisely, if \(A\) has eigenvalues \(a>b>0\), \(K\) has eigenvalues \(c>d>0\), and \(\theta\in[0,\pi/2]\) is the acute angle between their principal eigenvectors, put \(\Delta=\sqrt{abcd}\). Then
\[
\mathcal E(\theta)=\frac{\Delta(a+b)+ab(c+d)}{
ac+bd+2\Delta-(a-b)(c-d)\sin^2\theta}.\tag{2}
\]
This function is strictly increasing in \(\theta\). At fixed covariance eigenvalues, alignment of the leading eigendirections is uniquely best up to eigenvector signs; exchanging eigendirections is uniquely worst. Write \(r=c/d\ge1\). The two sharp extrema are
\[
\mathcal E_{\min}(r)=b+\frac{a-b}{1+\sqrt{ar/b}},\qquad
\mathcal E_{\max}(r)=b+\frac{a-b}{1+\sqrt{a/(br)}}.\tag{3}
\]
At \(r=1\) both equal \(\sqrt{ab}\); for \(r>1\), \(\mathcal E_{\min}(r)<\sqrt{ab}<\mathcal E_{\max}(r)\).

**Angular-information threshold.** Suppose a rough leading eigenvector of \(A\) is available, but the actual principal eigenvector may deviate from it by any acute angle at most \(\vartheta\in[0,\pi/2]\). Choose the principal eigendirection of \(K\) along the estimate and allow any covariance condition number \(r\ge1\). Then the exact minimax expected trace error over this uncertainty set is an **infimum**
\[
\boxed{\inf_{r\ge1}\sup_{0\le\theta\le\vartheta}\mathcal E(\theta,r)
=\min\left\{\sqrt{ab},\;\frac{ab}{a\cos^2\vartheta+b\sin^2\vartheta}\right\}.}\tag{4}
\]
The sharp switch occurs at
\[
\boxed{\vartheta_c=\arctan\left(\frac ab\right)^{1/4}.}\tag{5}
\]
For \(\vartheta<\vartheta_c\), the minimax infimum is approached only as \(r\to\infty\) (concentrate the sketch on the estimated leading eigendirection). For \(\vartheta>\vartheta_c\), the unique optimal covariance shape has \(r=1\) (isotropic); at equality, isotropy attains the infimum and singular-concentration sequences approach the same value, but every finite \(r>1\) is strictly worse. In particular, with no eigendirection information (\(\vartheta=\pi/2\)), isotropy is uniquely minimax. Common positive covariance scaling is immaterial.

This is a discontinuous design recommendation, not a discontinuity of the risk: for some uncertainty angles a modest amount of anisotropy worsens the risk even though extreme concentration eventually helps. The infimum for \(\vartheta<\vartheta_c\) is not attained among strictly positive-definite covariances.

There is also a sharp high-anisotropy information-accuracy tradeoff. With \(K\) having eigenvalue ratio \(r\), as \(r\to\infty\) and \(\theta\to0\) jointly,
\[
\boxed{\mathcal E(\theta,r)-b=
(a-b)\sqrt{\frac b{ar}}+\frac{b(a-b)}a\theta^2+
 o\big(r^{-1/2}+\theta^2\big).}\tag{6}
\]
The crossover between concentration error and orientation error occurs at \(\theta\asymp r^{-1/4}\). This is a two-scale asymptotic assertion, not a finite-sample probability bound.

## Assumptions and scope

Every matrix is real \(2\times2\), symmetric and strictly positive definite, and the sketch is a **single** centered Gaussian vector with fixed covariance \(K\succ0\). All formulae are in exact real arithmetic; the Gaussian draw is nonzero almost surely and \(g^{\mathsf T}Ag>0\). For the uniqueness and asymptotic statements assume \(a>b>0\) and, where specified, \(r>1\). At \(a=b\), every covariance and orientation has the same risk \(a\). At \(c=d\), orientation is irrelevant. The angular-uncertainty minimax comparison fixes \(a,b\), bounds the acute eigenvector error by \(\vartheta\), and restricts Gaussian covariance to a principal axis along the estimated eigendirection and a condition number \(r\ge1\). It is not algorithmic optimality over other sketch distributions or spectral-estimation procedures.

## Proof

**1. Reduction to a Gaussian ratio.** For any nonzero \(g\), write \(v=A^{1/2}g\) and \(P=vv^{\mathsf T}/(v^{\mathsf T}v)\). Then \(A-\widehat A=A^{1/2}(I-P)A^{1/2}\succeq0\) has rank one. Using \(\operatorname{tr}(A-\widehat A)=\operatorname{tr}A-(g^{\mathsf T}A^2g)/(g^{\mathsf T}Ag)\) and the \(2\times2\) Cayley–Hamilton identity \(A^2-(\operatorname{tr}A)A+(\det A)I=0\), we obtain
\[
\operatorname{tr}(A-\widehat A)=\det A\,\frac{g^{\mathsf T}g}{g^{\mathsf T}Ag}.\tag{7}
\]

**2. Exact angular integral.** Write \(g=K^{1/2}z\) for \(z\sim\mathcal N(0,I_2)\), set \(C=K^{1/2}AK^{1/2}\), and use the uniformity of the direction \(u=z/\|z\|\) on the unit circle. For every symmetric \(C\succ0\),
\[
\mathbb E_u\frac{uu^{\mathsf T}}{u^{\mathsf T}Cu}
=(C+\sqrt{\det C}\,I)^{-1}.\tag{8}
\]
To check this nonstandard identity, orthogonally diagonalize \(C\) with eigenvalues \(\lambda_1,\lambda_2>0\). The off-diagonals integrate to zero by symmetry. The elementary substitution \(t=\tan\phi\) gives
\[
\frac1{2\pi}\int_0^{2\pi}\frac{d\phi}{\lambda_1\cos^2\phi+\lambda_2\sin^2\phi}
=\frac1{\sqrt{\lambda_1\lambda_2}}.
\]
If \(I_j\) is the corresponding mean of the squared \(j\)-th circle coordinate divided by the denominator, then \(I_1+I_2=1/\sqrt{\lambda_1\lambda_2}\) and \(\lambda_1I_1+\lambda_2I_2=1\). Solving, including the repeated-eigenvalue limit, gives \(I_j=[\sqrt{\lambda_j}(\sqrt{\lambda_1}+\sqrt{\lambda_2})]^{-1}\), exactly the diagonal of the right side of (8).

Consequently, with \(\Delta=\sqrt{\det A\det K}\), (7) and (8) yield
\[
\mathbb E\operatorname{tr}(A-\widehat A)
=(\det A)\operatorname{tr}\big[K(C+\Delta I)^{-1}\big]
=(\det A)\operatorname{tr}(A+\Delta K^{-1})^{-1}.\tag{9}
\]
The last equality uses a congruence. For a \(2\times2\) invertible matrix \(B\), \(\operatorname{tr}(B^{-1})=\operatorname{tr}(B)/\det B\). Expanding \(B=A+\Delta K^{-1}\), and using \(\Delta^2=(\det A)(\det K)\), gives exactly (1).

**3. Sharp eigenvector orientation.** Orthogonal invariance permits \(A=\operatorname{diag}(a,b)\) and \(K=R_\theta\operatorname{diag}(c,d)R_\theta^{\mathsf T}\). Direct multiplication yields
\[
\operatorname{tr}(AK)=ac+bd-(a-b)(c-d)\sin^2\theta.\tag{10}
\]
The numerator in (1) is independent of \(\theta\) and strictly positive. Equations (2), strict monotonicity, and the endpoint formulae (3) follow. Scale invariance follows immediately from (1).

**4. No finite anisotropy can be a strict minimizer under angular uncertainty.** For the worst permitted angle \(\vartheta\), put \(t=\sqrt r\ge1\), \(\alpha=a\cos^2\vartheta+b\sin^2\vartheta\), and \(\beta=a\sin^2\vartheta+b\cos^2\vartheta\). Equation (2) is the rational function
\[
F(t)=\frac{ab(t^2+1)+\sqrt{ab}(a+b)t}{\alpha t^2+2\sqrt{ab}t+\beta}.
\]
The sign of \(F'(t)\) is the sign of
\[
D(t)=\sqrt{ab}[2ab-(a+b)\alpha]t^2
+2ab(\beta-\alpha)t
+\sqrt{ab}[(a+b)\beta-2ab].
\]
For \(\vartheta<\pi/4\), its leading and linear coefficients are negative and \(D(1)=[\sqrt{ab}(a+b)+2ab](\beta-\alpha)<0\), so \(F\) is decreasing for all \(t\ge1\). At \(\vartheta=\pi/4\), \(D(t)=\sqrt{ab}(a-b)^2(1-t^2)/2\), also negative for \(t>1\). For \(\vartheta>\pi/4\), the constant and linear coefficients are positive and \(D(1)>0\). If the leading coefficient is nonnegative, \(F\) is increasing; if negative, \(D\) has just one positive zero, at which \(F\) has a **maximum**, not a minimum. Thus \(F\) has no interior minimum on \((1,\infty)\). Its endpoint values are \(F(1)=\sqrt{ab}\) and \(\lim_{t\to\infty}F(t)=ab/\alpha\), proving (4). These endpoint values cross exactly when \(\alpha=\sqrt{ab}\), equivalently \(\tan^2\vartheta=\sqrt{a/b}\), proving (5) with the asserted strictness. The special case of fully unknown orientation is \(\vartheta=\pi/2\).


**5. Two-scale high-condition-number law.** At alignment, (3) gives \(\mathcal E(0,r)-b=(a-b)/(1+\sqrt{ar/b})=(a-b)\sqrt{b/(ar)}+o(r^{-1/2})\). Meanwhile (2), with \(c=r,d=1\), can be written
\[
\mathcal E(\theta,r)=\frac{\mathcal E(0,r)}{1-\eta_r\sin^2\theta},\qquad
\eta_r=\frac{(a-b)(r-1)}{ar+b+2\sqrt{abr}}\longrightarrow\frac{a-b}a.
\]
As \(\theta\to0\), the difference from \(\mathcal E(0,r)\) equals \(b(a-b)\theta^2/a+o(\theta^2)\) jointly with \(r\to\infty\). Adding the expansions proves (6), including its stated two-variable remainder. Both leading coefficients are strictly positive, giving the \(r^{-1/4}\) balancing scale.

## Verification

`verify.py` checks equation (7) against (1) by exact symbolic algebra for six rational positive-definite matrix pairs; compares (1) with deterministic full-circle quadrature for 45 noncommuting positive-definite pairs; tests sharp endpoint and interior orientation inequalities; checks the angular-information threshold, exact example and two-scale limit. It produced `verification_output.txt` with 712 passing assertions. The analytic integration and strict minimax inequalities above, not numerical tests, establish the theorem.

For \(A=\operatorname{diag}(4,1)\) and covariance eigenvalues \((9,1)\), the sharp expected residuals are \(10/7\) in aligned orientation and \(14/5\) in opposite orientation, compared with \(2\) for isotropic sampling. The best possible rank-one trace residual is \(1\), approached by perfectly aligned covariance as \(r\to\infty\).

## Relationship to prior work

Persson, Boullé and Kressner (arXiv:2404.00960, first public April 1, 2024), Sections 2.1–2.2 and Theorems 2.1/2.4, analyze correlated-Gaussian Nyström approximations through covariance quality factors and expectation bounds, but their stated general results use positive oversampling and do not give the exact one-vector planar risk, the sharp fixed-spectrum alignment law or the minimax isotropy comparison. Their Remark 2.8 explains the relationship to randomized SVD; that relationship does not supply the correlated one-column expectation formula.

Persson and Kressner (arXiv:2209.11023, Sections 2–3) use isotropic Gaussian Nyström sketches for monotone matrix functions and establish approximation bounds, not the covariance-dependent planar design law. Tropp, Yurtsever, Udell and Cevher (arXiv:1706.05736, Sections 2–4) develop randomized Nyström reconstruction and isotropic sketch error bounds. These establish the method and background but not the exact formula (1) and its minimax consequences. The special case \(K=I\), \(\mathbb E\operatorname{tr}(A-\widehat A)=\sqrt{\det A}\), also follows from standard two-coordinate Gaussian range-projection calculations and is not separately claimed as new. The contribution is the correlated-covariance angular-information threshold, exact covariance design landscape and sharp competing-error scales.

## Limitations

The theorem is a mathematically exact planar benchmark, not a multidimensional risk formula. A covariance aligned with the dominant eigenvector requires prior spectral information and may be expensive or unavailable; optimization across all algorithms, sketch widths, distributions, matrix dimensions, numerical precision, or wall-clock cost is **not** claimed. The angular minimax law assumes a bounded eigendirection error and the chosen covariance centered on the estimate; for the favorable concentrated regime its infimum requires unbounded covariance condition number, not an attainable positive-definite optimum. Published specialist results under generic Gaussian quadratic-form ratio language may precede parts of the identity. The cited primary sources were examined at the indicated relevant sections; this does not establish priority against all literature.

## References

1. D. Persson, N. Boullé and D. Kressner, *Randomized Nyström approximation of non-negative self-adjoint operators*, arXiv:2404.00960, first public version 2024-04-01. https://arxiv.org/abs/2404.00960
2. D. Persson and D. Kressner, *Randomized low-rank approximation of monotone matrix functions*, arXiv:2209.11023, first public version 2022-09-22. https://arxiv.org/abs/2209.11023
3. J. A. Tropp, A. Yurtsever, M. Udell and V. Cevher, *Fixed-Rank Approximation of a Positive-Semidefinite Matrix from Streaming Data*, arXiv:1706.05736, first public version 2017-06-18. https://arxiv.org/abs/1706.05736
