# Sharp condition-number-only envelopes for volume-sampled block Kaczmarz

## Finding

Let \(A\in\mathbb R^{m\times N}\) have full column rank, \(m\ge N\ge2\), and let its Gram matrix \(B=A^{\mathsf T}A\) have spectral condition number \(\kappa\ge1\). For every block size \(1\le k\le N\), sample a \(k\)-row block with probability proportional to its squared \(k\)-dimensional volume and denote the expected orthogonal row-space projector by \(F_k\). Its least eigenvalue \(\mu_k\) and its spectral condition number \(\chi_k\) obey the simultaneous sharp bounds

\[
\frac{k}{k+(N-k)\kappa}\le \mu_k\le
\frac{k\bigl[N-k+(k-1)\kappa\bigr]}{(N-1)\bigl[N-k+k\kappa\bigr]},
\]
\[
\frac{\kappa(N-1)}{N-k+(k-1)\kappa}\le\chi_k\le
\frac{(N-k)\kappa+k-1}{N-1}.
\]

All four boundaries are attained, for every admissible \((N,k,\kappa)\): the spectrum consisting of one smallest eigenvalue and \(N-1\) largest eigenvalues attains the lower \(\mu_k\) and upper \(\chi_k\) bounds, and the spectrum consisting of \(N-1\) smallest eigenvalues and one largest eigenvalue attains the other two. For \(\kappa>1\), \(2\le k<N\), these are the unique extremal spectral profiles, up to common scaling and permutation. At \(k=1\) the condition number always equals \(\kappa\), and at \(k=N\) both quantities equal one.

Consequently the sharp worst-case conditional mean-square error factor of one exact block Kaczmarz update is
\[
1-\frac{k}{k+(N-k)\kappa}.
\]
For \(0<\delta\le1\), a block size assures a fractional mean-square error reduction at least \(\delta\) for every full-rank matrix of this dimension and spectral condition number and every error vector if and only if
\[
k\ge \left\lceil\frac{\delta N\kappa}{1-\delta+\delta\kappa}\right\rceil.
\]

## Assumptions and scope

Fix integers \(m\ge N\ge2\), \(1\le k\le N\), a real full-column-rank matrix \(A\), and a consistent linear system \(Ax=b\). For a \(k\)-element row-index subset \(S\), set \(A_S\) to be its row submatrix and \(w_S=\det(A_SA_S^{\mathsf T})\ge0\). The normalizer is \(Z=\sum_{|S|=k}w_S>0\). Sample \(S\) with probability \(w_S/Z\); a zero-weight block is never selected. For positive-weight blocks, let \(P_S=A_S^{\mathsf T}(A_SA_S^{\mathsf T})^{-1}A_S\), the orthogonal projector onto the row span. Define \(F_k=\mathbb E P_S\), \(\mu_k=\lambda_{\min}(F_k)\), and \(\chi_k=\lambda_{\max}(F_k)/\lambda_{\min}(F_k)\). The condition number \(\kappa=\lambda_{\max}(B)/\lambda_{\min}(B)\) refers to \(B\), not to \(A\) itself.

Let \(\lambda_1\le\cdots\le\lambda_N\) be the eigenvalues of \(B\). For a finite set of nonnegative variables \(v\), write \(e_j(v)\) for the elementary symmetric polynomial of degree \(j\), with \(e_0=1\) and \(e_j=0\) outside its natural range. The expected projector has precisely the spectral eigenvalues
\[
p_i=\frac{\lambda_i e_{k-1}(\lambda_{-i})}{e_k(\lambda)},\qquad 1\le i\le N,
\]
where \(\lambda_{-i}\) denotes the list with \(\lambda_i\) removed. This known exact spectral transformation is the starting point; the new statement is its sharp global extremization subject only to \(\kappa\), and the resulting exact block-budget guarantee.

## Proof

**Expected-projector identity.** For every vector \(y\in\mathbb R^N\), consider the coefficient of \(z^k\) in \(\det(I+zA(I+t yy^{\mathsf T})A^{\mathsf T})\). By the principal-minor expansion, differentiation at \(t=0\) gives \(\sum_{|S|=k}w_S y^{\mathsf T}P_Sy\). Indeed \(\det(A_S(I+t yy^{\mathsf T})A_S^{\mathsf T})=w_S(1+t y^{\mathsf T}P_Sy)\) whenever \(w_S>0\), and the identity extends polynomially to zero-weight blocks. The matrix determinant lemma, Sylvester's identity, and \(B=A^{\mathsf T}A\) give
\[
\det(I+zB)\bigl(1+t z y^{\mathsf T}B(I+zB)^{-1}y\bigr).
\]
In an eigenbasis of \(B\), the coefficient of \(z^k t\) is \(\sum_i\lambda_i e_{k-1}(\lambda_{-i})|y_i|^2\). Since \(Z=e_k(\lambda)\), the claimed formula for \(p_i\) follows by polarization. In particular \(\sum_i p_i=k\). For \(k<N\),
\[
p_j-p_i=\frac{(\lambda_j-\lambda_i)e_{k-1}(\lambda_{-i,-j})}{e_k(\lambda)},
\]
so \(p_i\) follows the same order as \(\lambda_i\); for \(k=N\), all \(p_i=1\).

**Least eigenvalue.** Rescale the spectrum so that \(\lambda_1=1\) and \(\lambda_N=\kappa\); all remaining \(u_j\) lie in \([1,\kappa]\). The above identity yields
\[
\mu_k=\frac{1}{1+e_k(\kappa,u)/e_{k-1}(\kappa,u)}.
\]
For any positive variables \(v\), the ratio \(e_k(v)/e_{k-1}(v)\) is nondecreasing in each coordinate: upon exposing one variable \(s\), it has the form \((a+sb)/(b+sc)\), with derivative \((b^2-ac)/(b+sc)^2\ge0\). The sign is Newton's elementary-symmetric log-concavity inequality \(e_{k-1}(v_{-s})^2\ge e_{k-2}(v_{-s})e_k(v_{-s})\). In the interior \(k<N\) the relevant inequality is strict whenever the coordinate varies and there are enough positive terms. Hence \(\mu_k\) decreases as any \(u_j\) increases. Its minimum occurs when all \(u_j=\kappa\), and maximum when all \(u_j=1\). Substitution into the elementary-symmetric formula gives precisely the two claimed expressions for \(\mu_k\). The boundary \(k=N\) follows from \(F_N=I\).

**Expected-projector conditioning.** For \(2\le k<N\), put \(a=e_{k-1}(u)\) and \(b=e_{k-2}(u)\); both are positive. The extremal spectral ratio simplifies to
\[
\chi_k=\kappa\frac{a+b}{a+\kappa b} =\kappa\frac{a/b+1}{a/b+\kappa}.
\]
The ratio \(a/b=e_{k-1}(u)/e_{k-2}(u)\) increases strictly in every \(u_j>0\) by the same Newton inequality. If \(\kappa>1\), the outer rational function is strictly increasing. Taking all \(u_j=1\) gives \(a/b=(N-k)/(k-1)\), whereas taking all \(u_j=\kappa\) gives \(a/b=\kappa(N-k)/(k-1)\). These endpoints yield the stated lower and upper bounds for \(\chi_k\), respectively. When \(k=1\), \(F_1=B/\operatorname{tr}B\) and \(\chi_1=\kappa\); when \(k=N\), \(\chi_N=1\). Newton strictness also proves the claimed uniqueness of interior extremal profiles. Diagonal positive-definite \(A\) with the stipulated squared diagonal entries realizes all profiles, so no unattainable spectral condition is used.

**Sharp mean-square reduction and budget.** The update error is \(e^+=(I-P_S)e\), and orthogonal projection gives \(\mathbb E\|e^+\|^2=\|e\|^2-e^{\mathsf T}F_ke\). The largest conditional factor is \(1-\mu_k\), attained on a least-eigenvalue error vector. Optimizing over matrices of the specified \((N,\kappa)\) produces the worst-case factor displayed above. Solving \(k/[k+(N-k)\kappa]\ge\delta\) for the integer \(k\) gives the exact threshold. Sharpness follows from the one-small-eigenvalue profile and its corresponding error eigenvector.

## Verification

`verify.py` independently checks the spectral-polynomial bounds in exact rational arithmetic on 5,704 integer-valued full spectra across \(2\le N\le7\), \(1\le\kappa\le5\), and every allowed block size. It executes 153,536 exact assertions, including both sharp endpoint spectra. Separately, 972 checks construct randomly rotated real full-rank matrices, enumerate all their actual row-block projectors, and compare the resulting averaged projector against the polynomial formula. The maximum observed Frobenius discrepancy was below \(3\times10^{-15}\). Run `python verify.py` with Python 3 and NumPy. These are finite supplementary checks, not the proof for arbitrary real spectra.

For a concrete design example, \(N=5\), \(\kappa=9\), \(k=2\) gives \(2/29\le\mu_2\le2/7\) and \(3\le\chi_2\le7\); both endpoints in each inequality are realized by the stated multiplicity-one spectral profiles.

## Relationship to prior work

Entezari, Banerjee, and Kalantari (2026) derived the exact eigenvalue transformation of expected projectors under volume sampling and discussed spectral equalization; that formula is explicitly treated here as known. Xiang, Xie, and Zhang (2025) provided a block-Kaczmarz convergence analysis with volume sampling and a different, generally coarser spectral lower bound. Rodomanov and Kropotov (2019/2020) developed related exact volume-sampling inverse and elementary-symmetric identities for randomized coordinate descent. The contribution here is the sharp extremal result simultaneously for the minimum eigenvalue and spectral ratio at fixed ambient dimension, block size, and sole Gram condition-number constraint, including attaining spectra and a necessary-and-sufficient worst-case one-step block budget. The cited papers were compared for mathematical implication, not just title similarity; these specific envelopes and their joint extremizers were not located in the inspected material.

## Limitations

The guarantees are conditional, one-step, exact-arithmetic, and concern consistent full-column-rank real systems with exact determinantal block sampling. They do not give an implementation cost bound, a minimax rate for adaptive or correlated multi-step block choices, or a finite-precision error guarantee. The transformed-spectrum identity itself is previously known, and independent verification of the historical priority of the new sharp optimization remains necessary.

## References

1. Entezari, Banerjee, and Kalantari, *Volume Sampling and Spectral Equalization in Randomized Alternating Projections*, arXiv:2610.12346 (first public version 2026-10-08), https://arxiv.org/abs/2610.12346.
2. Xiang, Xie, and Zhang, *Randomized block Kaczmarz with volume sampling: Momentum acceleration and efficient implementation*, arXiv:2503.13941 (2025), https://arxiv.org/abs/2503.13941.
3. Rodomanov and Kropotov, *A Randomized Coordinate Descent Method with Volume Sampling*, arXiv:1904.04587 (2019), https://arxiv.org/abs/1904.04587.
