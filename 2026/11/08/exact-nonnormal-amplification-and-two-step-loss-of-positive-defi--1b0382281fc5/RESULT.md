# Exact nonnormal amplification and two-step loss of positive definiteness in frozen-Sylvester square-root refinement

## Finding
Let \(0<t<1\), \(K\ge 1\), and define
\[
Z=\begin{pmatrix}K&0\\0&1\end{pmatrix},\qquad
S=\begin{pmatrix}K&t\sqrt K\\t\sqrt K&1\end{pmatrix},\qquad A=S^2.
\]
Let \(\mathcal L_Z(H)=ZH+HZ\). Apply exact-arithmetic frozen-Sylvester refinement from \(X_0=Z\):
\[
X_{j+1}=X_j+\mathcal L_Z^{-1}(A-X_j^2),\qquad j=0,1,\ldots.
\]
Then \(A,Z,S\) are real symmetric positive definite; \(S=A^{1/2}\) is the principal square root, and the relative Frobenius error of \(Z\) tends to zero as \(K\to\infty\) at each fixed \(t\). Nevertheless, the first refinement *amplifies* absolute square-root error by an unbounded factor, and the second iterate is indefinite whenever \(K>2\sqrt2/t^2\). Explicitly,
\[
X_1=\begin{pmatrix}K+t^2/2&t\sqrt K\\t\sqrt K&1+Kt^2/2\end{pmatrix},\quad
X_2=\begin{pmatrix}K-t^4/(8K)&t\sqrt K(1-t^2/2)\\t\sqrt K(1-t^2/2)&1-K^2t^4/8\end{pmatrix}.
\]
The Jacobian at the fixed point \(S\) has spectrum \(\{-t,0,0,t\}\) on all real \(2\times2\) matrices, independent of \(K\), yet its Frobenius-induced operator norm is
\[
\|DF(S)\|_{F\to F}=t\sqrt{(K+K^{-1})/2}\longrightarrow\infty.
\]
Thus uniform local *spectral* stability and fixed relative spectral equivalence between the positive-definite initial guess and the principal root do not provide a uniform transient-error or positive-definiteness guarantee.

## Assumptions and scope
All matrices are real \(2\times2\) and all operations are exact. Parameters satisfy \(K\ge1\) and \(0<t<1\); no commuting assumption is made. The map \(F(Y)=Y+\mathcal L_Z^{-1}(A-Y^2)\) uses the **same** Sylvester operator \(\mathcal L_Z\) at every iteration. The comparison concerns Frobenius root error and matrix positive definiteness, not error in a Schur-factor implementation or effects of rounding.

## Proof

### 1. Positive definiteness, sector control, and relative error
The determinant and leading entry of \(S\) are \(K(1-t^2)>0\) and \(K>0\). Hence \(S\succ0\), and \(A=S^2\succ0\) has principal square root \(S\). Also \(Z\succ0\). Since
\[
Z^{-1/2}SZ^{-1/2}=\begin{pmatrix}1&t\\t&1\end{pmatrix},
\]
its eigenvalues are precisely \(1-t\) and \(1+t\). In particular \((1-t)Z\preceq S\preceq(1+t)Z\), uniformly in \(K\). Yet
\[
\frac{\|Z-S\|_F}{\|S\|_F}
=\frac{t\sqrt{2K}}{\sqrt{K^2+1+2Kt^2}}
\longrightarrow0\qquad(K\to\infty).
\]
These observations are independent of any convergence result for the iteration.

### 2. First and second steps
Writing \(E=S-Z\), the identity
\[
A-Z^2=ZE+EZ+E^2=\mathcal L_Z(E)+Kt^2I
\]
gives \(X_1=S+\mathcal L_Z^{-1}(Kt^2I)\), and hence
\[
X_1-S=\operatorname{diag}(t^2/2,Kt^2/2).
\]
The first iterate is positive definite because it is \(S\) plus a positive diagonal matrix. Its error ratio is **exactly**
\[
\frac{\|X_1-S\|_F}{\|Z-S\|_F}
=\frac{t}{2\sqrt2}\sqrt{K+K^{-1}}
\longrightarrow\infty.
\]
For the next correction let \(D=X_1-S=\operatorname{diag}(t^2/2,Kt^2/2)\). Then
\[
A-X_1^2=-(SD+DS+D^2).
\]
The \((1,1)\)-entry of the correction equals \(-t^2/2-t^4/(8K)\); the \((2,2)\)-entry equals \(-Kt^2/2-K^2t^4/8\); and each off-diagonal entry equals \(-t^3\sqrt K/2\). Adding these to \(X_1\) produces the stated \(X_2\). For \(K>2\sqrt2/t^2\) its \((2,2)\)-entry is strictly negative whereas its \((1,1)\)-entry is positive (since \(K\ge1\) and \(t<1\)), so \(X_2\) is indefinite. This threshold is exact for negativity of that displayed diagonal entry; no assertion is made that it is the earliest possible loss of positive definiteness.

### 3. Jacobian, spectral radius, and exact operator norm
For every real perturbation \(H\), differentiation of \(F\) at \(S\) yields
\[
DF(S)[H]=H-\mathcal L_Z^{-1}(SH+HS)=-\mathcal L_Z^{-1}(EH+HE),
\quad E=\begin{pmatrix}0&t\sqrt K\\t\sqrt K&0\end{pmatrix}.
\]
Use the Frobenius-orthonormal basis
\[
B_1=E_{11},\;B_2=(E_{12}+E_{21})/\sqrt2,\; B_3=E_{22},\;B_4=(E_{12}-E_{21})/\sqrt2.
\]
In that basis \(DF(S)\) has matrix
\[
-t\begin{pmatrix}
0&1/\sqrt{2K}&0&0\\
\sqrt{2K}/(K+1)&0&\sqrt{2K}/(K+1)&0\\
0&\sqrt{K/2}&0&0\\
0&0&0&0
\end{pmatrix}.
\]
The nonzero eigenvalues are \(-t,t\), with two additional zero eigenvalues. The two nonzero singular values are
\[
t\sqrt{(K+K^{-1})/2},\qquad \frac{2t\sqrt K}{K+1}.
\]
For \(K\ge1\), the first is no smaller than the second: squaring their ratio reduces to \((K^2+1)(K+1)^2\ge8K^2\), equivalent to \((K-1)^2(K^2+4K+1)\ge0\). This proves both the spectrum and the exact Frobenius-operator norm asserted above.

### 4. Small exact witness
With \(t=1/2\) and \(K=16\),
\[
Z=\operatorname{diag}(16,1),\quad
S=\begin{pmatrix}16&2\\2&1\end{pmatrix},\quad
A=\begin{pmatrix}260&34\\34&5\end{pmatrix},
\]
while
\[
X_1=\begin{pmatrix}129/8&2\\2&3\end{pmatrix},\qquad
X_2=\begin{pmatrix}32767/2048&7/4\\7/4&-1\end{pmatrix}.
\]
Thus both the inputs and the first iterate are positive definite, but the second iterate is indefinite even with exact rational arithmetic.

## Verification
Run `python verify.py` in an environment with `sympy` installed. It reconstructs the Sylvester corrections, root and iterate identities, the complete four-dimensional Jacobian, its characteristic polynomial, and the exact witness. Additional deterministic parameter evaluations are consistency checks, not substitutes for the all-parameter proof above. No numerical experiment is used to infer the unboundedness statements.

## Relationship to prior work
Gao, Kressner and Shao [1], Sections 2.1 and 3.1, explicitly introduce the fixed-Jacobian Sylvester refinement and establish sufficient convergence conditions in terms of a norm of the inverse Sylvester operator and the absolute initial error. This note addresses a different question: **uniformly bounded transient root error and preservation of positive definiteness under fixed relative root/initial-guess spectral equivalence**. The construction does not satisfy the paper's small-absolute-error convergence hypothesis uniformly as \(K\) grows, and therefore does not contradict its theorems. Higham [2] investigates exact Newton and inverse-based variants, including their finite-precision stability; these updates are not this fixed-Sylvester exact-arithmetic map. Sra [3] studies geometric square-root iterations, a distinct construction. No claim of an unconditional square-root solver failure is intended.

## Limitations
This is a structured two-dimensional family with unbounded conditioning as \(K\to\infty\); it does not establish failure for uniformly well-conditioned inputs or for approximations actually returned by a backward-stable low-precision Schur decomposition. The fixed-Jacobian method is *locally* convergent at each fixed \(K\) because its Jacobian has spectral radius \(t<1\); its local basin need not have a radius uniform in \(K\). The calculation is in exact arithmetic, not a finite-precision stability test. The second-step positivity threshold controls a diagonal sign and is not asserted to be the earliest definiteness transition. Formal independent audit and an exhaustive historical novelty determination have not been performed.

## References
[1] B. Gao, D. Kressner, M. Shao, *A mixed precision algorithm for the matrix square root* (2026), arXiv:2607.12430v1, first publicly posted July 14, 2026, https://arxiv.org/abs/2607.12430.

[2] N. J. Higham, *Newton's method for the matrix square root*, Mathematics of Computation 46 (1986), 537–549, https://doi.org/10.2307/2007992. Public full text: https://webspace.science.uu.nl/~zegel101/NUMWISb/Higham1986.pdf.

[3] S. Sra, *On the Matrix Square Root via Geometric Optimization* (2016), https://arxiv.org/abs/1507.08366.
