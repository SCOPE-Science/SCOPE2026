# A parity law for the penultimate Gelfand number of real Schatten embeddings

## Finding

For every integer \(N\ge 2\) and every pair of exponents \(0<p<q\le\infty\), let \(I_{p,q}^{(N)}\) be the identity map from the real \(N\)-by-\(N\) Schatten \(p\) class to the Schatten \(q\) class. With \(1/\infty=0\), its **penultimate Gelfand number** is

\[
c_{N^2-1}(I_{p,q}^{(N)})=
\begin{cases}
N^{1/q-1/p},&N\text{ even},\\
(N-1)^{1/q-1/p},&N\text{ odd}.
\end{cases}
\]

The last Gelfand number is \(c_{N^2}(I_{p,q}^{(N)})=N^{1/q-1/p}\). Hence the last two values coincide exactly in even dimension, while odd dimensions have a **strict final drop**. The formulas are exact for the full quasi-Banach range \(0<p<1\) as well as the Banach range, and they include \(q=\infty\).

## Assumptions and scope

All matrices and all linear subspaces are **real**. For \(0<p<\infty\), define the Schatten quasi-norm using the singular values \(s_1(A),\ldots,s_N(A)\):

\[
\|A\|_{\mathcal S_p}=\left(\sum_{j=1}^N s_j(A)^p\right)^{1/p},
\qquad
\|A\|_{\mathcal S_\infty}=\max_j s_j(A).
\]

For a linear map \(T\) on a real vector space of dimension \(N^2\), the Gelfand numbers use the standard convention

\[
c_k(T)=\inf_{\substack{F\subseteq\mathbb R^{N\times N}\\\mathrm{codim}\,F<k}}
\ \sup_{A\in F\setminus\{0\}}\frac{\|TA\|_{\mathcal S_q}}{\|A\|_{\mathcal S_p}},
\qquad 1\le k\le N^2.
\]

Every subspace is automatically closed. In particular, \(k=N^2-1\) means \(\dim F\ge2\); it suffices to consider two-dimensional subspaces because restricting a subspace cannot increase the supremum.

## Proof

**Step 1: Singular-value lower bound.** Let a nonzero real matrix \(A\) have rank \(r\) and positive singular values \(s_1,\ldots,s_r\). The ordinary power-mean comparison, valid for any \(0<p<q<\infty\), gives

\[
\left(\sum_{j=1}^r s_j^q\right)^{1/q}
\ge r^{1/q-1/p}\left(\sum_{j=1}^r s_j^p\right)^{1/p}.
\]

For \(q=\infty\), the corresponding inequality is \(\max_j s_j\ge r^{-1/p}(\sum_j s_j^p)^{1/p}\). Consequently

\[
\frac{\|A\|_{\mathcal S_q}}{\|A\|_{\mathcal S_p}}\ge r^{1/q-1/p}.
\]

As \(1/q-1/p<0\), rank at most \(m\) forces the stronger bound \(m^{1/q-1/p}\). Equality holds when all nonzero singular values are equal.

**Step 2: Even dimensions.** Suppose \(N=2m\). Choose the real skew-orthogonal block matrix \(J=\operatorname{diag}(R,\ldots,R)\), where

\[
R=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad J^\mathsf TJ=I_N,\qquad J^\mathsf T=-J.
\]

On the real two-plane \(F=\operatorname{span}_{\mathbb R}\{I_N,J\}\), every \(A=aI_N+bJ\) satisfies

\[
A^\mathsf TA=(a^2+b^2)I_N.
\]

Every nonzero \(A\in F\) therefore has \(N\) equal positive singular values, and the ratio of Schatten quasi-norms is identically \(N^{1/q-1/p}\). Step 1 gives the same lower bound on every nonzero matrix, proving equality for even \(N\).

**Step 3: Odd dimensions.** Suppose \(N\ge3\) is odd. Let \(F\) be *any* real two-dimensional matrix subspace with basis \(A,B\). The continuous function

\[
\theta\longmapsto\det(\cos\theta\,A+\sin\theta\,B)
\]

changes sign (or is identically zero) under \(\theta\mapsto\theta+\pi\), because the determinant has odd degree \(N\). The intermediate value theorem gives some \(\theta\) for which the determinant vanishes. Since \(A,B\) are linearly independent, \(\cos\theta\,A+\sin\theta\,B\ne0\), and hence this pencil contains a nonzero matrix of rank at most \(N-1\). Step 1 forces the supremum over \(F\) to be at least \((N-1)^{1/q-1/p}\).

For the reverse inequality, form \(J_{N-1}\) as in Step 2 and take the real plane

\[
F_0=\operatorname{span}_{\mathbb R}
\left\{
\begin{pmatrix}I_{N-1}&0\\0&0\end{pmatrix},
\begin{pmatrix}J_{N-1}&0\\0&0\end{pmatrix}
\right\}.
\]

Every nonzero element of this plane has exactly \(N-1\) identical positive singular values and one zero singular value, so its ratio is exactly \((N-1)^{1/q-1/p}\). This matches the lower bound for odd \(N\).

**Step 4: The final index.** For \(k=N^2\), one-dimensional subspaces are admissible. Step 1 gives \(N^{1/q-1/p}\) as a universal lower bound, attained on \(\operatorname{span}_{\mathbb R}\{I_N\}\). This recovers the known final-index formula and proves the stated parity contrast. \(\square\)

## Verification

The attached standalone `checker.py` uses exact integer arithmetic to reconstruct the skew-orthogonal block matrices and test \(A^\mathsf TA=(a^2+b^2)\operatorname{diag}(I_{N-(N\bmod2)},0)\) on dimensions \(2\) through \(15\) and integer parameters \(-4\le a,b\le4\). It also tests antisymmetry and orthogonality. These finite tests are supporting diagnostics only; the universal assertions follow from Steps 1–4, including the odd-determinant argument.

To replay, extract `checker.py` from this finding and run `python checker.py` using Python 3. No third-party dependencies are required.

## Relationship to prior work

Prochno's 2026 paper [1] determines the asymptotic order of Gelfand numbers for Schatten embeddings in a quasi-Banach range and records the exact **last** index in its discussion of matrix subspaces. Hinrichs, Prochno and Vybíral [2], and Prochno and Strzelecki [3], develop the broader finite-dimensional estimates. Their displayed endpoint estimates do not distinguish parity at the **penultimate** index. The present result supplies an exact value there in every real dimension and for all \(0<p<q\le\infty\); the determinant obstruction and conformal two-planes make the real-field qualification essential.

The proof uses only the classical power-mean inequality, the intermediate value theorem, and elementary real skew-orthogonal matrices. We do not claim these ingredients or the previously known last-index value as new. A related exact statement may exist in older matrix-pencil or widths literature under different terminology; this is a residual literature-priority risk.

## Limitations

The formula pertains to the **real** matrix field. The odd-dimensional lower-bound argument relies on sign reversal of the real determinant along a circle and is not a classification of complex matrix pencils. No formula is asserted for other Gelfand indices, rectangular matrices, or all maximizing subspaces. The computed finite diagnostics are not a substitute for the general proof. Independent mathematical validation has not been performed.

## References

1. J. Prochno, *Gelfand numbers of Schatten class embeddings in the quasi-Banach range*, arXiv:2611.08448v1, publicly submitted 2026-11-05, especially Section 1.1 and the matrix-subspace discussion.
2. A. Hinrichs, J. Prochno, J. Vybíral, *Gelfand numbers of embeddings of Schatten classes*, arXiv:2011.06554v1 (2020); *Mathematische Annalen* **380** (2021), 1563–1593.
3. J. Prochno, M. Strzelecki, *Approximation, Gelfand, and Kolmogorov numbers of Schatten class embeddings*, arXiv:2103.13050v1 (2021); *Journal of Approximation Theory* **277** (2022), 105736.
