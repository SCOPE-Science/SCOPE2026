# Two-mode covariance spectrum for circular Bernoulli run frequencies

## Finding

For a labeled cyclic iid Bernoulli sample of length \(n\), let \(C_r\) count maximal success-runs of *exactly* length \(r\). Fix integers \(R\ge2\), \(n\ge 2R+3\), and a probability \(0<p<1\), with \(q=1-p\) and \(a_r=q^2p^r\). Then for every \(1\le r,s\le R\),

\[
\operatorname{Cov}(C_r,C_s)
=n\left[\mathbf 1_{\{r=s\}}a_r+a_ra_s\left(\frac2q-r-s-3\right)\right].
\]

In particular, when \(r\ne s\), this covariance is negative, zero, or positive precisely when \(p\) is below, equal to, or above \(1-2/(r+s+3)\). Thus the off-diagonal sign phase diagram depends only on the sum of the two run lengths.

Let \(D=\operatorname{diag}(a_1,\ldots,a_R)\) and \(H=(nD)^{-1/2}\operatorname{Cov}(C_1,\ldots,C_R)(nD)^{-1/2}\). Define \(v_r=\sqrt{a_r}\), \(w_r=r\sqrt{a_r}\), and \(c=2/q-3\). Then

\[
H=I_R+c vv^{\mathsf T}-vw^{\mathsf T}-wv^{\mathsf T}.
\]

Its perturbation away from the identity has rank exactly two. Put \(A_R=\sum_{r=1}^R a_r\), \(B_R=\sum_{r=1}^Rr a_r\), \(C_R=\sum_{r=1}^Rr^2a_r\), \(\tau_R=cA_R-2B_R\), and \(\Delta_R=A_RC_R-B_R^2>0\). There are \(R-2\) unit eigenvalues and exactly two exceptional eigenvalues,

\[
\lambda_\pm(R,p)=1+\frac{\tau_R\pm\sqrt{\tau_R^2+4\Delta_R}}2,
\qquad 0<\lambda_-<1<\lambda_+.
\]

For each fixed \(p\in(0,1)\), along any admissible sequence \(R\to\infty\), \(n\ge2R+3\),

\[
\lambda_\pm(R,p)\longrightarrow
1+\frac p2\left[-3(1-p)\pm\sqrt{9(1-p)^2+4p}\right].
\]

## Assumptions and scope

The \(n\) samples \(X_0,\ldots,X_{n-1}\) are mutually independent Bernoulli \((p)\) and indices are interpreted modulo \(n\). A maximal success-run of length \(r\) begins at \(i\) exactly when \(X_{i-1}=0\), \(X_i=\cdots=X_{i+r-1}=1\), and \(X_{i+r}=0\). The all-success circle contributes no run of any length in \(\{1,\ldots,R\}\). The size bound \(n\ge2R+3\) ensures that a pair of tested run windows cannot intersect both ways round the circle. No assertion is made here about longer pairs, which may have distinct wraparound corrections.

## Proof

Let \(I_{i,r}\) be the indicator that a length-\(r\) maximal run begins at \(i\). It has probability \(a_r\), and \(C_r=\sum_{i=0}^{n-1}I_{i,r}\), so \(\mathbb E C_r=na_r\). Condition on \(I_{0,r}=1\). This fixes \(r\) consecutive ones with a zero on either side. Under \(n\ge r+s+3\), the expected number of length-\(s\) runs is the sum of four exhaustive, mutually exclusive start-position classes: a run starting at \(0\), which contributes \(\mathbf1_{\{r=s\}}\); a run immediately beyond the fixed right zero, contributing \(p^s q\); a run immediately before the fixed left zero, contributing another \(p^s q\); and \(n-r-s-3\) wholly independent candidate starts, contributing \((n-r-s-3)a_s\). All remaining starts contradict a fixed zero or one. Consequently,

\[
\mathbb E[C_s\mid I_{0,r}=1]
=\mathbf1_{\{r=s\}}+2p^s q+(n-r-s-3)a_s.
\]

By cyclic translation invariance, \(\mathbb E[C_rC_s]=na_r\mathbb E[C_s\mid I_{0,r}=1]\). Subtracting \(n^2a_ra_s\) gives the displayed exact covariance, because \(2p^s q=2a_s/q\). The off-diagonal sign follows by rearranging \(2/(1-p)-r-s-3\).

For the spectral statement, divide entry \((r,s)\) by \(n\sqrt{a_ra_s}\). It is \(\mathbf1_{\{r=s\}}+\sqrt{a_ra_s}(c-r-s)\), proving the rank-two representation. Because \(R\ge2\), vectors \(v\) and \(w\) are linearly independent; the middle coefficient matrix \(\left(\begin{smallmatrix}c&-1\\-1&0\end{smallmatrix}\right)\) is invertible. Therefore the perturbation has rank exactly two.

Its trace equals \(\tau_R\). Its two nonzero eigenvalues have product \(-\Delta_R\), as follows either by the two-dimensional characteristic polynomial or the Gram matrix \(\left(\begin{smallmatrix}A_R&B_R\\B_R&C_R\end{smallmatrix}\right)\). Strict Cauchy–Schwarz gives \(\Delta_R>0\), so one eigenvalue lies above zero and the other below zero. The covariance itself is positive definite: both the all-zero outcome (yielding \(C=0\)) and the outcomes having exactly one run of any prescribed length \(r\le R\) (yielding \(C=e_r\)) have positive probability. These \(R+1\) affinely independent count vectors exclude zero-variance nonzero linear forms. Thus \(\lambda_->0\) and the two exceptional normalized eigenvalues strictly straddle \(1\).

Finally the geometric series give \(A_R\to pq\), \(B_R\to p\), and \(C_R\to p(1+p)/q\); hence \(\tau_R\to-3pq\) and \(\Delta_R\to p^3\), yielding the stated limits.

## Verification

The accompanying standalone standard-library Python script `check.py` enumerates every binary circle at a range of admissible lengths and several rational Bernoulli parameters. It checks the exact means, all covariance entries, the rank-two identity in rational coordinates, and the trace/discriminant formulas, with exact fractions. Execute `python3 check.py` after extracting the embedded file. The proof of the infinite family and limiting spectrum is algebraic; enumeration is a finite cross-check only.

## Relationship to prior work

Inoue and Aki (2005) derive general joint generating functions and mixed-moment recurrences for counts of specified success-run lengths on a circle (their Section 4, notably Theorems 4.1 and 4.4). Those results give a broad computational route to raw moments, so the covariance entries are not claimed as a new independently unrecoverable joint law. The contribution here is an explicit all-frequency covariance kernel, sharp pairwise sign transition, and rank-two normalized covariance spectrum with its exceptional eigenvalues and limiting form. Huffer, Sethuraman and Sethuraman (2008) analyze counts of strings in infinite, generally non-identically distributed Bernoulli sequences using conditional Poisson processes; their setting and results do not state this finite circular two-mode spectrum. These comparisons do not exclude that the spectrum is implicit in older general generating functions.

## Limitations

The exact formula is proved only for \(n\ge2R+3\); wrapped overlapping windows at smaller sizes are outside scope. The claim does not establish a central limit theorem, independence of components, or any eigenvalue theorem for *unscaled* covariance matrices. Historical implicit priority remains possible because broad joint-moment formulas already exist. The limiting exceptional eigenvalues concern normalized covariance matrices as the number of listed run lengths grows under the admissible sample-size restriction.

## References

1. K. Inoue and S. Aki, *Joint distributions of numbers of success runs of specified lengths in linear and circular sequences*, Annals of the Institute of Statistical Mathematics **57** (2005), 353–368, https://doi.org/10.1007/BF02507029; open full text https://www.ism.ac.jp/editsec/aism/pdf/057_2_0353.pdf.
2. F. W. Huffer, J. Sethuraman, and S. Sethuraman, *A study of counts of Bernoulli strings via conditional Poisson processes*, arXiv:0801.2115v1, publicly submitted 2008-01-14, https://arxiv.org/abs/0801.2115.
3. K. Inoue and S. Aki, *On the conditional and unconditional distributions of the number of success runs on a circle with applications*, Statistics & Probability Letters **80** (2010), 874–885, https://doi.org/10.1016/j.spl.2010.01.022 (abstract-level comparison only).
