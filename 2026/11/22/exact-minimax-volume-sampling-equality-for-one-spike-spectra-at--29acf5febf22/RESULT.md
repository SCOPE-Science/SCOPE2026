# Exact minimax–volume-sampling equality for one-spike spectra at all interior subset sizes

## Finding

For all integers \(n\ge4\) and \(2\le k\le n-2\), and all real \(a,b>0\), consider the spectrum
\[
\lambda=(a+b,\underbrace{a,\ldots,a}_{n-1\text{ times}}).
\]
Define the worst-orientation best-subset Nyström trace error and the fixed-size determinantal (volume) sampling expectation as in Problem 4.7 of [1]. Then
\[
\boxed{\quad x_k(\lambda)=y_k(\lambda)=
 a(n-k)\frac{a+(k+1)b/n}{a+kb/n}.\quad}
\]
The maximizing orthogonal orientations are characterized exactly: if \(K=aI+bvv^{\mathsf T}\), where \(\|v\|_2=1\), they are precisely the orientations with
\[
|v_i|^2=\frac1n\qquad (1\le i\le n).
\]
Thus the spectral expectation bound from determinant sampling is *attainable by even an optimal deterministic subset choice* throughout the non-endpoint range for every one-spike positive-definite spectrum.

## Assumptions and scope

All matrices are real and symmetric. Fix \(n,k,a,b\) satisfying the strict restrictions above. Let \([n]=\{1,\ldots,n\}\). For each positive-definite \(K\in\mathbb R^{n\times n}\) with eigenvalue multiset \(\lambda\) and each \(I\subset[n]\) with \(|I|=k\), write
\[
R_I(K)=K-K_{:,I}K_{I,I}^{-1}K_{I,:},\qquad E_I(K)=\operatorname{tr}R_I(K).
\]
Every principal \(K_{I,I}\) is invertible. Define
\[
x_k(\lambda)=\max_{K:\,\operatorname{spec}(K)=\lambda}\ \min_{|I|=k}E_I(K),
\quad
 y_k(\lambda)=\mathbb E_{I\sim k\text{-DPP}(K)}E_I(K)
 =\frac{(k+1)e_{k+1}(\lambda)}{e_k(\lambda)}.
\]
Here \(k\)-DPP assigns probability proportional to \(\det K_{I,I}\) to each \(k\)-subset; \(e_j\) denotes the elementary symmetric polynomial of degree \(j\). The expectation is orientation-independent, as stated in [1] and [2]. The asserted novel range is \(2\le k\le n-2\); the separately known endpoint \(k=n-1\) is not a new claim.

## Proof

**1. Rank-one normal form and exact residual.** Any such matrix has form \(K=aI+bvv^{\mathsf T}\) with \(\|v\|_2=1\). Put \(J=[n]\setminus I\), \(s_I=\sum_{i\in I}v_i^2\). Sherman–Morrison gives
\[
(aI_I+bv_Iv_I^{\mathsf T})^{-1}
=a^{-1}I_I-\frac{b}{a(a+bs_I)}v_Iv_I^{\mathsf T}.
\]
Consequently the only nonzero block of \(R_I(K)\) is its Schur complement on \(J\):
\[
R_I(K)_{J,J}=aI_J+\frac{ab}{a+bs_I}v_Jv_J^{\mathsf T},
\]
and therefore, using \(\|v_J\|_2^2=1-s_I\),
\[
E_I(K)=a(n-k)+\frac{ab(1-s_I)}{a+bs_I}.\tag{1}
\]
No sign assumption on the coordinates of \(v\) is needed.

**2. Optimal subset and unique worst orientation.** Let \(w_i=v_i^2\ge0\), \(\sum_iw_i=1\), and let \(w_{(1)}\ge\cdots\ge w_{(n)}\) be their decreasing rearrangement. For \(0\le s\le1\), the scalar function in (1) has derivative
\[
\frac{d}{ds}\left(a(n-k)+\frac{ab(1-s)}{a+bs}\right)
=-\frac{ab(a+b)}{(a+bs)^2}<0.
\]
Thus the best subset maximizes \(s_I\), giving \(s_*=\sum_{i=1}^k w_{(i)}\). Averaging the first \(k\) entries of a decreasing list gives
\[
s_*\ge\frac{k}{n}.
\]
For \(1\le k<n\), equality holds only when all \(w_i=1/n\): if either the average of the first \(k\) or the average of the remaining \(n-k\) differed, monotonic order would force a strict inequality. Conversely, a flat squared-coordinate vector attains equality for every subset. Because the function in (1) is strictly decreasing, the maximum over all orientations occurs exactly for such flat vectors. Substitution yields
\[
x_k(\lambda)=a(n-k)+\frac{ab(1-k/n)}{a+bk/n}
=a(n-k)\frac{a+(k+1)b/n}{a+kb/n}.
\]
Every unit \(v\) with \(|v_i|=1/\sqrt n\) is the leading eigenvector of a real orthogonal orientation of the given spectrum, so the maximum and its exact equality cases are genuinely attained.

**3. Determinantal expectation.** For the one-spike eigenvalues, direct selection of either zero or one copy of the exceptional \(b\)-increment gives, for \(1\le j\le n\),
\[
e_j(\lambda)=\binom nj a^j+\binom{n-1}{j-1}b a^{j-1}
=\binom nj a^{j-1}\left(a+\frac{jb}{n}\right).
\]
The ratio identity \((k+1)\binom n{k+1}/\binom nk=n-k\) yields
\[
y_k(\lambda)=(k+1)\frac{e_{k+1}(\lambda)}{e_k(\lambda)}
=a(n-k)\frac{a+(k+1)b/n}{a+kb/n}=x_k(\lambda).
\]
This completes the proof. It uses no limiting approximation or finite-precision assumption.

## Verification

Run `python verify.py` with the standard library. The program constructs \(K=aI+bvv^{\mathsf T}\) from integer vectors, evaluates actual rational Schur-complement traces through exact Gaussian elimination, exhausts subsets for finitely many small dimensions, and separately tests the elementary-symmetric-polynomial and optimizer formulas. It reports 90 orientation cases and 2,586 exact rational equalities for \(4\le n\le8\) and all interior \(k\). These tests are reproducibility checks only; the proof above covers every integer \(n,k\) and real \(a,b\) in scope.

## Relationship to prior work

Problem 4.7 of the first-public version of [1] explicitly defines the two quantities and proves equality for the endpoint \(k=n-1\) using Schur–Horn, leaving other subset sizes open. The present statement addresses the entire *interior* \(2\le k\le n-2\) in the structurally canonical one-spike spectral class and determines all worst orientations. The general \(k\)-DPP expected-trace identity and broader kernel-approximation guarantees are established in [2] and reviewed in [3]; they provide the common upper bound \(x_k\le y_k\), but not the explicit attainment statement for all one-spike interior ranks. In particular, optimizing a random pivot rule or studying its expected error is not the same as the max-over-orientations/min-over-subsets problem here.

## Limitations

The result does not resolve the arbitrary-spectrum version of Problem 4.7, multiple nontrivial spectral spikes, approximate or noisy Nyström approximation, or finite-precision numerical stability. Its maximizing-orientation uniqueness requires \(b>0\); the scalar case \(b=0\) is excluded and has no unique orientation. Historical-priority comparisons include primary open sources and related low-rank literature but are not exhaustive; an independent expert audit has not been performed.

## References

[1] N. Amsel et al., *Linear Systems and Eigenvalue Problems: Open Questions from a Simons Workshop*, arXiv:2602.05394v1 (first public 2026-02-05), section 4.2, Problem 4.7. https://arxiv.org/pdf/2602.05394v1

[2] M. Fornace and M. Lindsey, *Column and row subset selection using nuclear scores: algorithms and theory for Nyström approximation, CUR decomposition, and graph Laplacian reduction*, arXiv:2407.01698 (2024), sections 2 and 5, appendix C. https://arxiv.org/abs/2407.01698

[3] Y. Chen, E. N. Epperly, J. A. Tropp, and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, Communications on Pure and Applied Mathematics (2024/2025), section C.4. https://doi.org/10.1002/cpa.22234
