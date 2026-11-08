# Sharp dimension-dependent calibration of row-normalized and polar directions

## Finding

For an integer \(m\ge2\), a real \(m\times n\) full-row-rank matrix \(V\), \(n\ge m\), having all row norms equal to one, set \(G=VV^{\mathsf T}\). The observed minimum average-off-diagonal ratio is
\[
r_{\min}(G)=\min_{1\le i\le m}\frac{m-1}{\sum_{j\ne i}|G_{ij}|},
\]
with a zero denominator interpreted as \(+\infty\). Let \(R>1\) and assume \(r_{\min}(G)\ge R\). Define
\[
\delta=\frac{m-1}{R},\qquad \Lambda=\min\left\{1+\delta,\frac{m+\sqrt m}{2}\right\},
\quad \mathcal E_{m,R}=\frac{m}{\Lambda+\sqrt{(m-1)\Lambda(m-\Lambda)}}.
\]
The exact worst-case fraction of the optimal spectral-norm-constrained linear descent preserved by the row-normalized direction, calibrated to the same spectral-norm budget, is
\[
\boxed{\inf_{V:\,r_{\min}(G)\ge R}\frac{\langle V,V/\|V\|_2\rangle}{\max_{\|D\|_2\le1}\langle V,D\rangle}=\mathcal E_{m,R}.}
\]
The infimum is attained for every \(m\ge2\), \(n\ge m\), and \(R>1\). When \(\delta\ge(m+\sqrt m-2)/2\), the exact value saturates at \(2/(1+\sqrt m)\) despite further weakening the required row-ratio floor.

The exact worst-case operator-norm deviation from the polar direction \(P(V)=(VV^{\mathsf T})^{-1/2}V\) is
\[
\boxed{\sup_{V:\,r_{\min}(G)\ge R}\|V-P(V)\|_2
=\max\left\{\sqrt{1+\delta}-1,\;1-\sqrt{\max\{0,1-\delta\}}\right\}.}
\]
The supremum may require a sequence of positive-definite matrices approaching a singular boundary; no rank-deficient matrix is admitted. In particular, if \(m=q^2\), \(R=q\), and \(q\to\infty\) through integers, then the observable ratio \(r_{\min}=q\) diverges although the worst-case relative descent efficiency behaves as \(q^{-1/2}\) and the norm deviation grows as \(q^{1/2}\). Uniform recovery of unit relative descent efficiency as dimensions vary holds exactly when \((m-1)/R\to0\).

## Assumptions and scope

All matrices are real, \(m\ge2\), \(n\ge m\), and \(V\) has full row rank and unit Euclidean row norms. Consequently \(G\) is positive definite with diagonal entries one and trace \(m\). We take \(\|\cdot\|_2\) to be the spectral/operator norm, \(\|\cdot\|_*\) the nuclear norm, and \(\langle A,B\rangle=\operatorname{tr}(A^{\mathsf T}B)\). Both row normalization and polar normalization are applied to the same \(V\). Row normalization therefore returns \(V\); in the efficiency comparison this direction is additionally rescaled by its exact operator norm so both candidate steps lie in the same unit operator-norm ball. This calibration is not asserted to be the learning-rate rule used by any particular optimizer.

The diagnostic is the *minimum per-row ratio* for the already unit-row matrix, not an average across matrices or a Hessian diagonal-block ratio. The result is deterministic, single-step, and finite dimensional; it makes no statistical or long-run optimizer-convergence claim.

## Proof

Write \(\lambda_1\ge\cdots\ge\lambda_m>0\) for the eigenvalues of \(G\), so \(\sum_i\lambda_i=m\). The row-ratio hypothesis gives \(\sum_{j\ne i}|G_{ij}|\le\delta\) for every row. Gershgorin's theorem therefore yields
\[
\lambda_i>0,\qquad 1-\delta\le\lambda_i\le1+\delta,\qquad \lambda_1\ge1.
\]
Positive definiteness gives the independent strict inequality \(\lambda_i>0\); the Gershgorin endpoint \(1-\delta\) may be attained when it is positive.

Let \(V=U\operatorname{diag}(\sqrt{\lambda_i})W^{\mathsf T}\) be its thin singular-value decomposition. Its polar factor is \(P(V)=UW^{\mathsf T}\). Spectral/nuclear duality, whose maximizing direction is precisely this polar factor, gives
\[
\max_{\|D\|_2\le1}\langle V,D\rangle=\|V\|_* =\sum_i\sqrt{\lambda_i},
\qquad \langle V,V/\|V\|_2\rangle=\frac{m}{\sqrt{\lambda_1}}.
\]
Thus the ratio equals \(m/(\sqrt{\lambda_1}\sum_i\sqrt{\lambda_i})\). By Cauchy--Schwarz on the other \(m-1\) singular values,
\[
\sqrt{\lambda_1}\sum_i\sqrt{\lambda_i}
\le \lambda_1+\sqrt{(m-1)\lambda_1(m-\lambda_1)}=:H_m(\lambda_1).
\]
Here \(1\le\lambda_1\le1+\delta\), and \(\lambda_1<m\). Differentiation of \(H_m\) on \((0,m)\) shows its unique maximizing point in \([1,m]\) is \(\lambda_*=(m+\sqrt m)/2\). Equivalently the stationary equation \(2\sqrt{\lambda(m-\lambda)}=\sqrt{m-1}(2\lambda-m)\), with \(2\lambda-m>0\), has this unique solution. Hence \(H_m(\lambda_1)\le H_m(\Lambda)\), proving the claimed universal lower efficiency bound. At \(\Lambda=\lambda_*\), one computes \(H_m(\Lambda)=m(1+\sqrt m)/2\).

For equality, let \(\rho=(\Lambda-1)/(m-1)\). Then \(0\le\rho\le1/R<1\), and the positive equicorrelation matrix
\[
G_+=(1-\rho)I+\rho\mathbf1\mathbf1^{\mathsf T}
\]
has eigenvalues \(\Lambda\) and \((m-\Lambda)/(m-1)\) with multiplicity \(m-1\). It has \(r_{\min}(G_+)=1/\rho\ge R\), with \(1/0=+\infty\), and attains equality in every bound. Take \(V=G_+^{1/2}[\,I_m\ \ 0\,]\), with the zero block absent if \(n=m\); it has unit rows and full row rank.

For the deviation, the same singular-value decomposition gives exactly
\[
\|V-P(V)\|_2=\max_i|\sqrt{\lambda_i}-1|.
\]
Using the two spectral endpoints gives the stated upper bound. Its positive-eigenvalue branch is attained by the equicorrelation matrix with \(\rho=1/R\), whose largest eigenvalue is \(1+\delta\). If \(\delta<1\), the negative-eigenvalue branch is attained by the negative equicorrelation matrix \(G_-=(1+1/R)I-(1/R)\mathbf1\mathbf1^{\mathsf T}\), with smallest eigenvalue \(1-\delta>0\). If \(\delta\ge1\), use \(G_-(\varepsilon)=(1+\theta)I-\theta\mathbf1\mathbf1^{\mathsf T}\), \(\theta=(1-\varepsilon)/(m-1)\), with \(\varepsilon\downarrow0\); its row ratio is \((m-1)/(1-\varepsilon)\ge R\), its smallest eigenvalue is \(\varepsilon\), and it is positive definite. Both branches are thus sharp, including the distinction between maximum and supremum.

Finally, for \(m=q^2\) and \(R=q\), choose the positive equicorrelation witness \(\rho=1/q\). Its eigenvalues are \(1+q-1/q\) and \(1-1/q\) with multiplicity \(q^2-1\). Consequently \(r_{\min}=q\), the efficiency is \((1+o(1))q^{-1/2}\), and the deviation is \((1+o(1))q^{1/2}\). For a varying sequence \((m,R)\), if \(\delta=(m-1)/R\to0\), Gershgorin places all singular values uniformly at \(1+o(1)\), forcing efficiency to one. Conversely, if \(\delta\not\to0\), choose a subsequence with \(\delta\ge c>0\), and the positive equicorrelation example with \(\rho=\min\{c/2,1/2\}/(m-1)\) (for small dimensions decrease this positive constant if necessary) has \(r_{\min}\ge R\) while the efficiency stays below one by an amount depending on \(c\) along any fixed-dimension or diverging-dimension subsequence. Thus the uniform limit condition is necessary as well.

## Verification

Running `python verify.py` with Python 3 and NumPy checks direct singular-value decompositions against the analytical efficiency and deviation formulas over random full-row-rank matrices, both signed equicorrelation extremal families, the sharp piecewise spectral boundary, and exact rational trace/eigenvalue identities. The packaged checker returned `PASS: 10699 finite, spectral, rational and extremal checks`. The proof above, not the finite tests, establishes the full quantified result; no test enumerates all real matrices or all dimensions.

## Relationship to prior work

Deng et al., *RMNP: Row-Momentum Normalized Preconditioning for Scalable Matrix-Based Optimization* (2026), Section 3.2 and Appendix B, introduce exactly the average-off-diagonal row statistic used here, report empirical values, and motivate direct row normalization. They do not give an exact sharp worst-case spectral-ball alignment or a dimension-scaled threshold for the statistic.

Zhang and Lin, *The Row Normalization Puzzle in Muon* (2026), Theorems 3.1--3.2 and Lemma B.2, analyze a different row-normalization operation applied **after** polar orthogonalization, with convergence bounds and dimension-dependent loss of alignment; these do not yield the exact constrained-RMNP extremizers above. Deng et al., *How Does Orthogonalization Adapt to the Neural Network Hessian Structure?* (2026), especially Appendix F, establish exact coincidence for diagonal Gram matrices and analyze expected Gram diagonal dominance at initialization; they do not derive this sharp deterministic finite-dimensional ratio frontier. Pethick et al., *Training Deep Learning Models with Norm-Constrained LMOs* (2025), Section 3.1 and Tables 1--2, explicitly identify row and spectral norm-ball linear minimization oracles, without optimizing the cross-norm efficiency subject to a prescribed finite Gram row-ratio floor. Spectral/nuclear duality, Gershgorin bounds, and Cauchy--Schwarz are established ingredients rather than new results.

## Limitations

This result does not infer that a high ratio reported on **unscaled** unequal-row momentum matrices guarantees a high efficiency after row normalization. The theoretical ratio is evaluated on a unit-row matrix. The result does not assert a training-loss separation between RMNP and Muon, does not analyze momentum history, noisy gradients, Hessian curvature, time-dependent steps, or actual optimizer learning-rate scaling. A prior general sharp matrix-norm optimization theorem might subsume the specialization; mathematical priority is not independently certified.

## References

- T. Pethick, W. Xie, K. Antonakopoulos, Z. Zhu, A. Silveti-Falls, and V. Cevher, *Training Deep Learning Models with Norm-Constrained LMOs*, arXiv:2502.07529 (2025). https://arxiv.org/abs/2502.07529
- S. Deng, Z. Ouyang, T. Pang, Z. Liu, R. Jin, S. Yu, and Y. Yang, *RMNP: Row-Momentum Normalized Preconditioning for Scalable Matrix-Based Optimization*, arXiv:2603.20527v1, publicly submitted 2026-03-20. https://arxiv.org/html/2603.20527v1
- Y. Zhang and Z. Lin, *The Row Normalization Puzzle in Muon*, arXiv:2609.39114v1 (2026). https://arxiv.org/abs/2609.39114
- *How Does Orthogonalization Adapt to the Neural Network Hessian Structure? A Gradient Self Outer-Product Analysis at Initialization*, arXiv:2610.28975v1 (2026), especially Appendix F. https://arxiv.org/abs/2610.28975
