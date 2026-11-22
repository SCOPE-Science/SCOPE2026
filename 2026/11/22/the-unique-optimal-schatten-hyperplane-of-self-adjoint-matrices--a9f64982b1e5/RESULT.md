# The unique optimal Schatten hyperplane of self-adjoint matrices and its rank phase transition

## Finding
For every integer \(n\ge2\) and real \(0<p<\infty\), the second Gelfand number of the identity from self-adjoint Schatten \(p\) to the spectral norm is
\[
c_2=\begin{cases}2^{-1/p},&0<p\le1,\\[3pt](1+(n-1)^{1-p})^{-1/p},&p\ge1.\end{cases}
\]
The infimum is attained at exactly one codimension-one real subspace: the trace-zero hyperplane. The extremizing spectrum switches at \(p=1\) from rank two to full rank when \(n>2\).

## Assumptions and scope
The ambient space \(\mathcal H_n\) is either \(\mathrm{Sym}_n(\mathbb R)\) or \(\mathrm{Herm}_n(\mathbb C)\), considered as a **real** vector space. All subspaces and their codimensions are real. The quasi-norm is \(\|X\|_p=(\sum_{j=1}^n|\lambda_j(X)|^p)^{1/p}\), and \(\|X\|_{\mathrm{op}}=\max_j|\lambda_j(X)|\). Define \(c_2=\inf_{\operatorname{codim}_{\mathbb R} F<2}\sup_{X\in F\setminus\{0\}}\|X\|_{\mathrm{op}}/\|X\|_p\). We claim the formula for every finite positive \(p\), all \(n\ge2\), and both ambient spaces. No claim is made for nonsymmetric or non-self-adjoint matrices.

## Proof
**Step 1 (sharp norm on the trace-zero hyperplane).** Suppose \(X\ne0\), \(\operatorname{tr}X=0\). Change the sign and rescale so that \(\lambda_{\max}(X)=\|X\|_{\mathrm{op}}=1\). Its negative eigenvalues have total magnitude at least one. If \(0<p\le1\), the elementary inequality \(\sum_j t_j^p\ge(\sum_jt_j)^p\) for nonnegative \(t_j\) gives \(\|X\|_p^p\ge1+1=2\). For \(p>1\), Hölder's inequality across at most \(n-1\) negative eigenvalues gives \(\sum_{\lambda_j<0}|\lambda_j|^p\ge(n-1)^{1-p}\), hence \(\|X\|_p^p\ge1+(n-1)^{1-p}\). Both bounds are attained: respectively by \(\operatorname{diag}(1,-1,0,\ldots,0)\) and by \(\operatorname{diag}(n-1,-1,\ldots,-1)\). At \(p=1\), any trace-zero matrix with precisely one strictly positive eigenvalue and arbitrary nonpositive remainder (or its negative), after normalization, is extremizing. Strict concavity for \(p<1\), and strict convexity for \(p>1\), force the respective displayed profiles; when \(n=2\), they coincide. These arguments apply equally to real symmetric and Hermitian matrices by spectral diagonalization.

**Step 2 (every other hyperplane is worse).** Each real hyperplane has a unique normal direction, represented under the real trace pairing by a nonzero self-adjoint matrix \(A\): \(F_A=\{X:\operatorname{tr}(AX)=0\}\). If \(A\) is indefinite or singular, some unit vector \(v\) satisfies \(v^*Av=0\). The rank-one projector \(vv^*\in F_A\) has norm ratio \(1\), strictly greater than the value in Step 1. Otherwise replace \(A\) by \(-A\) if necessary to make it positive definite. Let \(0<a\le b\) be its smallest and largest eigenvalues, and let \(s=\operatorname{tr}A\); \(a/s\le1/n\), with equality precisely when \(A\) is scalar.

For \(p\ge1\), take a unit minimum-eigenvector \(v\) and \(t=a/s\). Then \(X=vv^*-tI\in F_A\), with ratio
\[
R_p(t)=\left(1+(n-1)\left(\frac{t}{1-t}\right)^p\right)^{-1/p}.
\]
This is strictly decreasing on \((0,1)\), so \(R_p(t)\ge R_p(1/n)=(1+(n-1)^{1-p})^{-1/p}\), strictly if \(A\) is nonscalar. For \(0<p<1\), choose orthonormal minimum- and maximum-eigenvectors \(v,w\); \(X=bvv^*-aww^*\in F_A\) has ratio \((1+(a/b)^p)^{-1/p}\ge2^{-1/p}\), again strictly unless \(a=b\). The same argument at \(p=1\) works in either branch. Thus the trace-zero hyperplane uniquely minimizes the restricted inclusion norm. The full ambient space has inclusion norm one, so allowing codimension zero does not reduce the infimum. This proves the formula and uniqueness.

## Verification
The file `check_symmetric_hyperplane.py` checks both endpoint spectral profiles and the lower-bound witnesses for many dimensions, exponents and deterministic positive definite normals, plus randomly generated trace-zero spectra. The observed diagnostic output was `SYMMETRIC_HYPERPLANE_DIAGNOSTIC_OK 9680`. Finite experiments are illustrations only: Steps 1 and 2 prove the universal statements.

## Relationship to prior work
Prochno (2026), Hinrichs–Prochno–Vybíral (2020/2021), and Prochno–Strzelecki (2021/2022) investigate Gelfand numbers of **full** real matrix Schatten embeddings, principally in asymptotic order. A full-matrix hyperplane always contains a rank-one matrix: for any linear normal \(A\), take a nonzero column vector \(v\), then choose \(u\perp Av\), obtaining \(u v^*\) in the hyperplane. Therefore its second Gelfand number is one, not the number above. The self-adjoint real-linear constraint changes this geometry. Earlier work on traceless projections estimates norms of projections rather than optimal restriction norms of the identity, and does not imply this classification. The natural \(n=3\), \(p\le1\) traceless-symmetric construction also appears as a witness in a prior exact full-matrix width study, but does not establish the all-dimensional, all-exponent optimal-hyperplane and equality classification.

## Limitations
Only the second Gelfand number is determined, for the spectral target norm; no higher-index or finite target-exponent formula follows. The proof uses finite-dimensional self-adjoint spectral theory and real-linear hyperplanes. Closely related classical eigenvalue optimization principles could conceal an alternative implicit statement in the literature; this is not an independent originality certification.

## References
- J. Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, arXiv:2611.08448v1 (first posted 5 November 2026), https://arxiv.org/abs/2611.08448.
- A. Hinrichs, J. Prochno and J. Vybíral, *Gelfand numbers of embeddings of Schatten classes*, arXiv:2011.06554v1, https://arxiv.org/abs/2011.06554.
- J. Prochno and M. Strzelecki, *Approximation, Gelfand, and Kolmogorov numbers of Schatten class embeddings*, arXiv:2103.13050v1, https://arxiv.org/abs/2103.13050.
