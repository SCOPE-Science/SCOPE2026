# Sharp parity transition for row-sum-corrected balanced-sign diagonal estimation

## Finding

Let \(n\ge2\) and let an arbitrary real \(n\times n\) matrix \(A\) be accessed through exact matrix--vector products. Once \(r=A\mathbf1\) has been computed, an exchangeable random-sign estimator of \(\operatorname{diag}A\) has an exact, optimizable mean-square risk. In its natural affine-correction class the optimal sign distribution is uniform over vectors with the smallest attainable absolute sign sum: zero for even \(n\), and one for odd \(n\). This yields a parity-dependent zero-variance classification and an exact comparison that accounts for the extra deterministic matrix--vector product.

Write \(B=A-\operatorname{Diag}(\operatorname{diag}A)\), \(b=B\mathbf1\), and choose \(m\ge1\). Let \(z^{(1)},\ldots,z^{(m)}\) be independent copies of a random vector in \(\{-1,1\}^n\) whose law is invariant under every coordinate permutation. Put \(\rho=\mathbb E[z_i z_j]\) for \(i\ne j\), assume \(\rho<1\), and define

\[
\widehat d_\rho=\frac{1}{1-\rho}\left(\frac1m\sum_{t=1}^{m}z^{(t)}\odot(Az^{(t)})-\rho r\right).
\]

This is unbiased for every \(A\), and its **exact** squared Euclidean mean error is

\[
\boxed{\mathbb E\|\widehat d_\rho-\operatorname{diag}A\|_2^2
=\frac{\|B\|_F^2+\rho\|B\mathbf1\|_2^2}{m(1-\rho)}.}\tag{1}
\]

Within the class of permutation-invariant sign laws and the uniquely universally unbiased affine correction using the two vector observations \(z\odot Az\) and \(A\mathbf1\), every non-diagonal \(A\) attains its smallest risk precisely when

\[
\rho=\rho_n:=\begin{cases}-1/(n-1),&n\text{ even},\\ -1/n,&n\text{ odd}.\end{cases}
\]

The exact resulting risks are

\[
\boxed{\mathcal R_{n,m}(A)=
\begin{cases}
\displaystyle\frac{(n-1)\|B\|_F^2-\|B\mathbf1\|_2^2}{mn},&n\text{ even},\\[6pt]
\displaystyle\frac{n\|B\|_F^2-\|B\mathbf1\|_2^2}{m(n+1)},&n\text{ odd}.
\end{cases}}\tag{2}
\]

For even \(n\), the error is identically zero for every draw exactly when all off-diagonal entries **within each row** are equal. Equivalently, for arbitrary nonsymmetric \(A\), \(A_{ij}=c_i\) for every \(j\ne i\); among symmetric matrices, this is exactly \(A=D+c(\mathbf1\mathbf1^{\mathsf T}-I)\) with \(D\) diagonal. For odd \(n\), zero risk is possible only if \(A\) is diagonal. Thus dense symmetric constant-coupling matrices admit exact diagonal recovery with one all-ones product and one balanced product in even dimensions, but retain positive risk in odd dimensions when \(c\ne0\).

A cost-matched comparison uses \(m+1\) independent-entry Rademacher matvecs for the standard estimator, versus \(m\) balanced matvecs plus the one all-ones matvec. For **every** nondiagonal real matrix, the balanced estimator then has strictly smaller risk if \(n=2\) for any \(m\ge1\), or if even \(n\ge4\) with \(m\ge n\), or if odd \(n\ge3\) with \(m\ge n+1\). These thresholds are sharp for general matrices: at \(m=n-1\) (even \(n\ge4\)) or \(m=n\) (odd \(n\ge3\)), nonzero matrices with \(B\mathbf1=0\) tie; for smaller \(m\), such examples favor the standard estimator. This does **not** imply superiority for every matrix at smaller budgets or optimality among arbitrary probing algorithms.

## Assumptions and scope

The matrix \(A\in\mathbb R^{n\times n}\) is arbitrary; symmetry, positivity, sparsity and diagonal dominance are not assumed. All matrix--vector products are exact. A probe is a sign vector with a permutation-invariant distribution; distinct probes are sampled independently. The baseline uses independent-coordinate fair signs. The estimator family permits only a coordinatewise affine combination of \(z_i(Az)_i\) and the known row sum \(r_i\), with coefficients depending on the probe law, not on the unknown matrix. Here \(\odot\) is coordinatewise multiplication. The all-ones product costs one matrix--vector multiplication. Risk is the expectation of squared Euclidean error, not a high-probability bound. For \(\rho=1\), all signs are identical in every probe and the stated affine estimator is undefined; this degenerate law is excluded.

The optimal even-dimensional design draws uniformly from all sign vectors with exactly \(n/2\) positive coordinates; the odd-dimensional design draws from either of the two layers with \((n\pm1)/2\) positives (or any mixture of those two layers). Flipping all signs leaves each observed vector \(z\odot Az\) unchanged, so the two odd layers give equivalent estimator distributions.

## Proof

**1. Pair correlation and its sharp parity bound.** Coordinate exchangeability makes \(\mathbb E[z_i z_j]=\rho\) independent of \(i\ne j\). Set \(S=\sum_i z_i\). The identity \(S^2=n+2\sum_{i<j}z_i z_j\) gives

\[
\rho=\frac{\mathbb E S^2-n}{n(n-1)}.
\]

If \(n\) is even, \(S\) is even and \(S^2\ge0\); if \(n\) is odd, \(S\) is odd and \(S^2\ge1\). These bounds yield \(\rho\ge\rho_n\). Equality forces \(S=0\) almost surely in even dimensions and \(|S|=1\) almost surely in odd dimensions. Exchangeability forces the conditional distribution on each fixed-sum layer to be uniform. Conversely, these uniform layers attain equality.

**2. Unique universal affine correction.** Since \(z_i^2=1\) and \(\mathbb E[z_i z_j]=\rho\) for distinct indices,

\[
\mathbb E[z_i(Az)_i]=A_{ii}+\rho\sum_{j\ne i}A_{ij}
=(1-\rho)A_{ii}+\rho r_i.
\]

Hence (1) defines an unbiased estimator. A universal affine estimator \(a\,z_i(Az)_i+b\,r_i\) is unbiased for every possible diagonal and off-diagonal row precisely when \(a(1-\rho)=1\) and \(a\rho+b=0\). For \(\rho<1\), this uniquely gives \(a=(1-\rho)^{-1}\), \(b=-\rho/(1-\rho)\).

**3. Exact risk without fourth-order moment assumptions.** Fix row \(i\), set \(a_j=A_{ij}\) for \(j\ne i\), \(s_i=\sum_{j\ne i}a_j\), and \(q_i=\sum_{j\ne i}a_j^2\). The random part of \(z_i(Az)_i\) is \(\sum_{j\ne i}a_j z_i z_j\). Its square has expectation \(q_i+\rho(s_i^2-q_i)\), while its mean is \(\rho s_i\). Direct subtraction yields

\[
\operatorname{Var}(z_i(Az)_i)
=(1-\rho)(q_i+\rho s_i^2).
\]

The correction divides this variance by \((1-\rho)^2\); averaging independent probes divides by \(m\). Summing the coordinate variances (cross-coordinate covariances are irrelevant to expected squared Euclidean error) proves (1), since \(\sum_iq_i=\|B\|_F^2\) and \(\sum_i s_i^2=\|B\mathbf1\|_2^2\).

**4. Universal optimality and zero-variance spaces.** For fixed \(A\), differentiating (1) in the *achievable correlation parameter* \(\rho<1\) gives

\[
\frac{d}{d\rho}\left(\frac{\|B\|_F^2+\rho\|B\mathbf1\|_2^2}{1-\rho}\right)
=\frac{\|B\|_F^2+\|B\mathbf1\|_2^2}{(1-\rho)^2}.
\]

This is strictly positive for every \(B\ne0\). The smallest possible \(\rho\) is therefore the unique optimal correlation, and its sign laws were classified in step 1. Substitution proves (2). For even \(n\), rowwise Cauchy--Schwarz gives \(s_i^2\le(n-1)q_i\), with equality exactly when the \(n-1\) off-diagonal entries in row \(i\) coincide. Thus (2) vanishes precisely for the claimed row-constant pattern. Symmetry forces all row constants to be equal because the off-diagonal entries connect every pair. For odd \(n\), \(nq_i-s_i^2\ge q_i\), and the total risk vanishes exactly when all \(q_i=0\), namely \(B=0\).

**5. Cost-matched exact threshold.** With \(m+1\) independent-coordinate Rademacher probes the standard estimator has risk \(\|B\|_F^2/(m+1)\). In the even case, subtracting its risk from (2) has the sign of

\[
(n-1-m)\|B\|_F^2-(m+1)\|B\mathbf1\|_2^2.
\]

For odd \(n\), the corresponding sign is that of

\[
(n-m)\|B\|_F^2-(m+1)\|B\mathbf1\|_2^2.
\]

These expressions are strictly negative for every nonzero \(B\) in the stated upper-budget regimes. If \(n\ge3\), nonzero off-diagonal matrices with all row sums zero exist: in each row, choose two distinct off-diagonal positions, set them to \(+1\) and \(-1\), and set the rest to zero. They give equality at the boundary and reverse the inequality below it. The exceptional \(n=2\) case has zero balanced risk for every \(A\), so wins strictly for all nondiagonal \(A\) and every \(m\ge1\).

## Verification

The standalone Python program `verify.py` uses only the standard library and exact rational arithmetic. It enumerates every permutation-invariant fixed-positive-count orbit for \(2\le n\le9\), checks the pair correlation, unbiasedness, exact coordinate variances, optimal-correlation inequalities, parity classification witnesses and matched-budget transition witnesses. Execution yielded **1,423 exact-rational assertions passed**. This finite computation independently tests the algebraic identities, but is not an exhaustive proof for all dimensions; the proof above is the all-dimensional certificate.

For example, with \(n=4\) and \(A=D+c(\mathbf1\mathbf1^{\mathsf T}-I)\), the balanced estimator has identically zero error while ordinary iid sign probing has expected squared error \(12c^2/m\). With \(n=5\) and the same off-diagonal pattern, the optimal balanced risk is \(10c^2/(3m)\) versus iid risk \(20c^2/m\), a factor of six smaller at the same number of randomized probes, after paying for the deterministic all-ones product.

Reproduce with: `python3 verify.py`. No third-party dependencies are required.

## Relationship to prior work

Baston and Nakatsukasa [1] (first public January 26, 2022) analyze conventional Rademacher/Gaussian diagonal estimators and Diag++. Hallman, Ipsen and Saibaba [2] establish bounds for several conventional random-vector families. Dharangutte and Musco [3] give a tight error analysis for the iid-coordinate Hutchinson diagonal estimator, whose exact expected squared error is the baseline \(\|B\|_F^2/m\). Epperly, Tropp and Webber [4] develop XDiag, an exchangeable estimator that averages leave-one-out low-rank corrections; **their exchangeability acts on the set of probe vectors**, not on the coordinates of a single fixed-sum sign vector. XDiag uses a different construction and may outperform the restricted family studied here.

The mathematical contribution here is the all-dimensional *within-probe negative-dependence* design, its unique row-sum affine correction, sharp parity-dependent zero-error classification, and exact extra-query-adjusted threshold. The ordinary iid risk and more general diagonal-estimation frameworks are prior art, and this result does not imply a global minimax theorem over all matrix-free algorithms.

## Limitations

Optimality holds only among permutation-invariant sign-probe distributions with the **universally unbiased affine row-sum correction stated above**. The observations are exact, and the all-ones oracle call is counted separately. Other adaptive, structured, low-rank or nonlinear estimators may have smaller risk. Coordinate-uniform error bounds and non-Euclidean risks are not established. Random probes are independent across draws; using sampling without replacement between draws is not covered. The zero-error assertion is for the described structural matrix classes, not arbitrary dense matrices. A specialist equivalent treatment using finite-population sampling or graph probing may exist; this literature comparison is not a proof of novelty.

## References

1. R. A. Baston and Y. Nakatsukasa, *Stochastic diagonal estimation: probabilistic bounds and an improved algorithm*, first posted January 26, 2022, https://arxiv.org/abs/2201.10684, full text https://ar5iv.labs.arxiv.org/html/2201.10684.
2. E. Hallman, I. C. F. Ipsen and A. K. Saibaba, *Monte Carlo Methods for Estimating the Diagonal of a Real Symmetric Matrix*, first posted February 6, 2022, https://arxiv.org/abs/2202.02887, full text https://ar5iv.labs.arxiv.org/html/2202.02887.
3. P. Dharangutte and C. Musco, *A Tight Analysis of Hutchinson's Diagonal Estimator*, https://arxiv.org/abs/2208.03268, full text https://ar5iv.labs.arxiv.org/html/2208.03268.
4. E. N. Epperly, J. A. Tropp and R. J. Webber, *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation*, https://arxiv.org/abs/2301.07825, §2.4 (XDiag), full text https://ar5iv.labs.arxiv.org/html/2301.07825.
